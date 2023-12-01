import os
from github import Github, GithubException

#Obtener los parámetros
n1=int(os.getenv('NUMERO_UNO'))
n2=int(os.getenv('NUMERO_DOS'))

#ejecutar suma y mostrar el resultado
n3=n1+n2
print(n3)
