# tftarget

Uso: python3 target.py [help|[dir|file]]<br>
dir: directorio donde se encuentran los tf para sacar todos los recursos<br>
file: archivo de tf para sacar los recursos<br>
mode: modo de ejecución de terraform<br>
- plan<br>
- apply<br>
- destroy<br>

Ejemplos:<br>
- python3 target.py dir /home/ubuntu/tf<br>
- python3 target.py file /home/ubuntu/tf/main.tf<br>
- python3 target.py dir /home/ubuntu/tf mode plan<br>
- python3 target.py file /home/ubuntu/tf/main.tf mode apply<br>
- python3 target.py help<br>