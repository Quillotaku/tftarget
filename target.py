import os
import json
import sys

def help():
    print("""
Uso: python3 target.py [help|[dir|file]|mode]
dir: directorio donde se encuentran los tf para sacar todos los recursos
file: archivo de tf para sacar los recursos
mode: modo de ejecución de terraform
          - plan
          - apply
          - destroy
Ejemplos:
          - python3 target.py dir /home/ubuntu/tf
          - python3 target.py file /home/ubuntu/tf/main.tf
          - python3 target.py dir /home/ubuntu/tf mode plan
          - python3 target.py file /home/ubuntu/tf/main.tf mode apply
          - python3 target.py help
""")
    sys.exit(0)

def init_params():
    params = {"dir":"", "mode":"", "help":"","file":""}
    return params

def get_params(params):
    par=init_params()
    for i in range(0,len(params)):
        if params[i] == "dir":
            par[params[i]] = params[i+1]
        elif params[i] == "file":
            par[params[i]] = params[i+1]
        elif params[i] == "mode":
            par[params[i]] = params[i+1]
        elif params[i] == "help":
            help()
    return par

def get_tf_files(dir):
    tf = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if root == dir:
                if file.endswith(".tf"):
                    tf.append(os.path.join(root, file))
    return tf

def get_data(tf):
    res = [""]
    for file in tf:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("module"):
                    module = "module."+line.split('"')[1].strip()
                    res.append(module)
                elif line.startswith("resource"):
                    resource = line.split('"')[1].strip()+"."+line.split('"')[3].strip()
                    res.append(resource)
                elif line.startswith("data"):
                    data = "data."+line.split('"')[1].strip()
                    res.append(data)
    return res

def generate_targets(res,mode):
    for i in range(1,len(res)):
        print("%3d. %s " % (i,res[i]))
    targets = input("Cuales quieres para el target? (lista separada por espacios): ")
    tg = [""]
    for target in targets.split(" "):
        try:
            if target != "0":
                tg.append(res[int(target)])
        except:
            print("No existe el target %d, se omite." % int(target))
    if mode == "":
        print(" -target ".join(tg))
    else:
        print("terraform "+mode+" -target ".join(tg))


if __name__ == "__main__":
    tf_files = []
    resources = [""]

    params = get_params(sys.argv)
    if params["dir"] != "":
        tf_files = get_tf_files(dir=params["dir"])
        resources = get_data(tf=tf_files)
    if params["file"] != "":
        resources = get_data(tf=[params["file"]])
    generate_targets(res=resources,mode=params["mode"])
    exit()

