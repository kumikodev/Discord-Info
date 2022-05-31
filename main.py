import os
import sys
import time
import requests

token = "YOUR DISCORD TOKEN"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def getIP():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except:
        return "Error"

def GetDiscordID(token):
    try:
        header = {"authorization": token}
        url = 'https://discordapp.com/api/v6/users/@me'
        r = requests.get(url, headers=header)
        return r.json()['id']
    except:
        return "Error"


def GetDiscordUsername(token):
    try:
        header = {"authorization": token}
        url = 'https://discordapp.com/api/v6/users/@me'
        r = requests.get(url, headers=header)
        return r.json()['username']
    except:
        return "Error"
def GetAllDiscordData(token):
    try:
        header = {"authorization": token}
        url = 'https://discordapp.com/api/v6/users/@me'
        r = requests.get(url, headers=header)
        return r.json()
    except:
        return "Error"


clear()    

id = GetDiscordID(token)
username = GetDiscordUsername(token)
data = GetAllDiscordData(token)

print(id)

print(username)

print(data)

print(getIP())
