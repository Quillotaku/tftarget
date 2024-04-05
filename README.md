# tftarget

Uso: python3 target.py [help|[dir|file]|mode|var]<br>
Indicar al menos `dir` o `file`.<br>
dir: Path del directorio donde se encuentran los tf para sacar todos los recursos. OBLIGATORIO<br>
file: Path del archivo de tf para sacar los recursos. OBLIGATORIO.<br>
mode: Modo de ejecución de terraform. OPCIONAL<br>
- plan
- apply
- destroy

var: Path de las variables para terraform, se puede repetir tantas veces como sea necesario. OPCIONAL.<br>

Ejemplos:<br>
- python3 target.py dir /home/ubuntu/tf
- python3 target.py file /home/ubuntu/tf/main.tf
- python3 target.py dir /home/ubuntu/tf mode plan
- python3 target.py file /home/ubuntu/tf/main.tf mode apply
- python3 target.py dir /home/ubuntu/tf -var /home/ubuntu/tf/variables.tfvars
- python3 target.py file /home/ubuntu/tf/main.tf -var /home/ubuntu/tf/variables.tfvars
- python3 target.py dir /home/ubuntu/tf mode plan -var /home/ubuntu/tf/variables.tfvars
- python3 target.py file /home/ubuntu/tf/main.tf mode apply -var /home/ubuntu/tf/variables.tfvars
- python3 target.py file /home/ubuntu/tf/main.tf -var /home/ubuntu/tf/variables.tfvars -var /home/ubuntu/tf/vars.tfvars
- python3 target.py dir /home/ubuntu/tf mode plan -var /home/ubuntu/tf/variables.tfvars -var /home/ubuntu/tf/vars.tfvars
- python3 target.py help