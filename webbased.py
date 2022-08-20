from selenium import webdriver
import selenium                          
import time
import os 
import colorama 
from colorama import Fore, init
import requests


init()



def main():
    logo()
    os.system('title Token Finder by хроника#9947')  # Shows the title on top of the page
    email = input(Fore.YELLOW +  " \n What is the email you would like to use > " + Fore.RESET)
    password = input(Fore.BLUE + "What is the password you would like to use > " + Fore.RESET)
    os.system("cls")
    print(Fore.GREEN + "Opening Discord Login Page" + Fore.RESET)
    driver = webdriver.Chrome(executable_path='chromedriver.exe') # opens chromedriver
    options = webdriver.ChromeOptions() 
    options.add_argument("--incognito") # turns on incognito mode
    options.add_argument("start-maximized") # minimises the screen
    driver = webdriver.Chrome(chrome_options=options) 
    driver.get("https://discord.com/login") # Opens Discord Register System
    
    time.sleep(1)

    driver.find_element("xpath" , '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(email) # Puts your email into the email box
    driver.find_element("xpath" , '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(password) # Puts your password into the password box
    driver.find_element("xpath" , '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click() # Presses Login Button

    time.sleep(1)

    os.system("cls") # Clears the terminal

    print(input(Fore.RED + "Please press enter when you have solved the captcha (If no captcha press enter anyways)." + Fore.RESET)) # Waits for the captcha to be completed

    time.sleep(2)

    token = driver.execute_script(
            "let popup; popup = window.open('', '', `width=1,height=1`); if(!popup || !popup.document || !popup.document.write) console.log('Please allow popups'); window.dispatchEvent(new Event('beforeunload')); token = popup.localStorage.token.slice(1, -1); popup.close(); return token") # Gets the token of the account

    os.system("cls")
    print(Fore.GREEN + f"Your token is : {token}" + Fore.RESET) # Prints the token onto the screen

    headers = {'Authorization':token, 'Content-Type':'application/json'}
    r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']   # Gets your tokens username
        
    with open("token.txt", "w", encoding="utf-8") as f:
        f.write(token + " - " + userName)   # Writes the token and username into the file

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
    main()            # Runs the script