import requests
import time
import string 
from colorama import init, Fore, Back, Style
import os,threading
import random


init(convert=True)
valid = 0
invalid = 0
taken = 0

characters = string.ascii_letters +  string.digits
 


        
lines = open('proxies.txt').read().splitlines()
def title():
    global valid
    global invalid
    global taken
    while True:
        os.system(f"title Boolty´s FireCracker Mod Nitro Gen Valid : [{valid}]  Invalid : [{invalid}] Taken : [{taken}]")

def nitro():
    global valid
    global invalid
    global taken
    while True:
        os.system(f"title  Boolty´s FireCracker Mod Nitro Gen Valid : [{valid}]  Invalid : [{invalid}] Taken : [{taken}]") 
        if proxymod == 'y':
            proxy =random.choice(lines)
            if proxytype == "https":
                proxies = {'https': 'https://%s' % (proxy)}
            elif proxytype == "http":
                proxies = {'http': 'http://%s' % (proxy)}
            else:
                print(" > INVALID PROXY TYPE GIVEN, RESTART REQUIRED!")
            continue

        alphabet = "abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        l = list(alphabet)
        random.shuffle(l)
        shuffle = ''.join(l)
        gift = shuffle[0:16]
        #gift = "".join(random.choice(characters) for i in range(16))
        print(f"{Fore.CYAN}[?] Testing discord.gift/{gift}")
        try:
            if proxymod == 'y':
                r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}", proxies = proxies)
            r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}")          
            if r.status_code == 404:
                print(f"{Fore.RED}[-] discord.gift/{gift} - Ratelimited")
                f = open("taken.txt", "a")
                taken += 1
                f.write("https://discord.gift/"+gift)
                f.close()
            elif r.status_code == 429:
                print(f"{Fore.RED}[-] discord.gift/{gift} - Invalid")
                invalid += 1
                time.sleep(5)
            elif r.status_code == 200: 
                print(f"{Fore.GREEN}[-] discord.gift/{gift} -Valid Code - Saved to valid.txt")
                f = open("valids.txt", "a")
                valid += 1
                f.write("https://discord.gift/"+gift)
                f.close()
        except:
            pass

threading.Thread(target = title).start()

threadcount = int(input(" > Number of threads?\n > "))
while True:
    proxymod = input('Want use Proxy list? Y or N\n ')
    Fl = proxymod[0].lower()
    if proxymod == '' or not Fl in ['y','n']:
        print('Pls only y or n...')
    else:
        break               
if proxymod == 'y':
    proxytype = input(" > HTTP or HTTPS\n > ").lower()
for i in range(threadcount):
    threading.Thread(target = nitro).start()
    time.sleep(0.1)
