import requests
import json

def buscar_dados():
    request = requests.get("https://api.mozambiquehe.re/bridge?auth=8e508981d02a222385682437c8bc485e&player=Turokaao&platform=PLATFORM")
    todos = json.loads(request.content)
    print(todos)
    #print(todos[1]['nickname'])

#if __name__ == '__main__':
#     buscar_dados()
