import time
import requests
import random
import os
import sys
from discord_webhook import DiscordWebhook
from os import system
import urllib.request

print( '''
____    __    ____  __    __   __       __    __  
\   \  /  \  /   / |  |  |  | |  |     |  |  |  | 
 \   \/    \/   /  |  |  |  | |  |     |  |  |  | 
  \            /   |  |  |  | |  |     |  |  |  | 
   \    /\    /    |  `--'  | |  `----.|  `--'  | 
    \__/  \__/      \______/  |_______| \______/   CrackerFIX By Boolty                                             
''')

webhook = ""

def generatecodes():
    epoch = 0
    while True:
        print( "How many codes to generate?")
        num = 5000
        codes = []
        for i in range(num):
            alphabet = "abcdefghijklmnopqrstubwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            l = list(alphabet)
            random.shuffle(l)
            shuffle = ''.join(l)
            result = shuffle[0:16]
    
            codes.append(result)
        
        g = open('codes.txt', 'r+')
        g.truncate(0)
    
        with open('codes.txt', 'w') as f:
            for item in codes:
                f.write("%s\n" % item)
    
    
        print("Done generating codes. Generated: " + str(len(open("codes.txt","r").readlines())) + " codes" )
        time.sleep(1)
    
        if len(open("codes.txt","r").readlines()) == 0:
            print("There isnt any codes. You can generate some using this program or use some external one, but make sure they are only the codes. Exiting.")
            time.sleep(1)
            sys.exit()
        print("Found ", str(len(open("codes.txt","r").readlines())) + " codes.")
    
        
    
    
        time.sleep(.3)
        print("Do you want to use discord webhooks? [1] YES [2] NO")
        #choice2 = input("")
        #if choice2=="1":
        #    print("Webhook URL: ")
        #    webhook = input()
        valid = 0
        invalid = 0
        checked = 0
        epoch += 1
        invalidList = []
        validList = []
    
        
    
        with open('codes.txt') as f:
            for line in f:
                url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{line}?with_application=false&with_subscription_plan=true"
                if requests.get(url).status_code == 200:
                    print("Found a valid nitro code: ", line)
                    if choice2: 
                        content = "found a valid code: "+" discord.gift/" + line
                        webhook = DiscordWebhook(url=webhook, rate_limit_retry=True,content=content)
                        response = webhook.execute()
                        valid += 1
                        print("discord.gift/"+line.rstrip(), "valid!!!!!!!")
                        validList.append("discord.gift/"+line.rstrip())
                    print("discord.gift/"+line.rstrip(), "valid!!!!!!!")
                    validList.append("discord.gift/"+line.rstrip())
                    valid += 1
                    with open('valid.txt', 'a') as file:
                        file.write("discord.gift/"+line.rstrip())
    
                if requests.get(url).status_code == 404:
                    print("rate limited")
    
                else:
                    print("discord.gift/"+line.rstrip(), "is invalid.")
                    invalid += 1
                    invalidList.append("discord.gift/"+line.rstrip())
                
                
    
    
                checked += 1
                title = "Invalid: " + str(invalid) + " Valid: " + str(valid) + ' Epoch: ' + str(epoch) + " Remaining: " + str(checked) + "/" + str(len(open("codes.txt","r").readlines()))
                system("title " + title )
            info = "Invalid: " + str(invalid) + " Valid: " + str(valid) + ' Epoch: ' + str(epoch) + " Remaining: " + str(checked) + "/" + str(len(open("codes.txt","r").readlines()))
            print("Finished checkings, you got ", info)
            print("Saving invalid and valid codes...")
    
            with open('invalid.txt', 'a') as g:
                for item in invalidList:
                    g.write("%s\n" % item)
    
            with open('valid.txt', 'a') as f:
                for item in validList:
                    f.write("%s\n" % item)
    
            print("Saved.")


print("[1] START FIRECRACKER [2] THANKS MY LORD FOR CODE [3] EXIT")

choice1 = input()

if choice1=="1":
    generatecodes()


if choice1=="2":
    #checkCodes()
    pass

if choice1=="3":
    sys.exit()
