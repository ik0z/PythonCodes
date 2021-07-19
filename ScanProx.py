import requests
import random
import threading
from termcolor import * 
from colorama import Fore, Style

req = requests.Session()

#Proxy list from here :) 
prox = open("proxy.txt",'r').read().splitlines()

#header
loghead = {

    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '267',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'x-csrftoken': 'JcuJvUzrOI7CPnkJshUS4YkNIsgDnkNg',
    'x-requested-with': 'XMLHttpRequest',

}
#User can enter number of threads 
thread = int(input(f"{Fore.CYAN} \n Enter number of threads : "))

#Function to check proxy 
def checkingproxy():
    while True : 
        proxlist = [] 

        for proxi in prox : 
             proxlist.append(proxi)
        randomprox = str(random.choice(proxlist))
    

        
        try :
            reProx = {
               'http':'http://{}'.format(randomprox),
               'https':'https://{}'.format(randomprox)
            }
            req.proxies = reProx

            loginurl = 'https://www.instagram.com/accounts/login/ajax/'
            logdata = {
                'username': 'dsdsdsdsdsdsdsdsds',
                'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1617019864:AfVQACl0aBTOos8aKdbJ2p9ZeBNRb58q0dR4dQluwI+ikYAbsCXuJDV8mIuUw7FLkRaETIfVu7kJ4hWHiYRkMatoWc6Um+cU96HQtUcQG3SUAadYzLAnKPOC88WErAYhutehlwPYq2py9fBPtN4='
            }
            
            re = req.post(loginurl, data=logdata , headers=loghead).text
            #check status is ok = good , else bad proxy
            if ('"status":"ok"') in re : 
                cprint('Good Proxy : {}'.format(randomprox),'green',attrs=['bold'])
                with open('goodproxy.txt','a') as good :
                    good.write(randomprox + '\n')
            else :
              cprint("Bad Proxy : {}".format(randomprox),'red')

        except requests.exceptions.ConnectionError :
             cprint("Bad Proxy : {}".format(randomprox),'red')



threads = []
for i in range(thread) :
    thread1 = threading.Thread(target=checkingproxy)
    thread1.start()
    threads.append(thread1)
for thread2 in threads : 
    thread2.join() 
