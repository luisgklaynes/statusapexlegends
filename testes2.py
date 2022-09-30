import requests


res = requests.get('https://google.com.br')
print(res)
arquivo = open ("arquivo.txt", "w")
print(res.text, file=arquivo)
arquivo.close()


