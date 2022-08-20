from encodings import utf_8
import requests 
import json
import colorama 
from colorama import Fore, init

init()

def main():
    logo()

    email = input(str(Fore.BLUE + " \n What is your email > " + Fore.RESET))
    password = input(str(Fore.YELLOW + "What is your password > " + Fore.RESET))

    s = requests.Session()
    payload = {
        "email" : email,
        "password" : password
    }
    res = s.post("https://discord.com/api/v9/auth/login", json=payload)
    if res.status_code == 200:
     token = res.json()["token"]
     

     headers = {'Authorization':token, 'Content-Type':'application/json'}
     r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']   # Gets your tokens username

    with open("token.txt", "w", encoding="utf_8") as f:
        f.write(token + " - " + userName)
    
    print(input("Your token is: " +  token))


def logo():
    
    print(Fore.GREEN + """ 
   _____                            _ _           _______          _     
  / ____|                          (_) |         |__   __|        | |    
 | (___   ___ _ __ ___   __ _ _ __  _| |_ _   _     | | ___   ___ | |___ 
  \___ \ / _ \ '_ ` _ \ / _` | '_ \| | __| | | |    | |/ _ \ / _ \| / __|
  ____) |  __/ | | | | | (_| | | | | | |_| |_| |    | | (_) | (_) | \__ \\
 |_____/ \___|_| |_| |_|\__,_|_| |_|_|\__|\__, |    |_|\___/ \___/|_|___/
                                           __/ |                         
                                          |___/                          
                                 Developed by хроника#9947""" + Fore.RESET)


if __name__ == "__main__":
    main()