import socket
from termcolor import *
import os , sys 
from requests import get 

def logome():
    logo = cprint("""
    ╦╔╗╔╔═╗╔═╗  |     k   A   z
    ║║║║╠╣ ║ ║  |   i5irh.a@gmail.com
    ╩╝╚╝╚  ╚═╝  |  	Khaled
    """,'blue',attrs=['bold'])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    cprint("Local IP    : {}".format(s.getsockname()[0]),'yellow',attrs=['bold'])
    s.close()
    ip = get('https://api.ipify.org').text
    cprint('Public IP   : {}'.format(ip),'red',attrs=['bold'])


def proc():
    os.system("clear")
    logome()
    cprint("""
    1.Update & upgrade
    2.apt search <pkg>
    3.apt install <pkg>
    4.service < start , stop , restart , enable > 

        0 . exit
    """,'cyan',attrs=['bold']) 

    cho = input("   :@> ")  
    if int(cho) == 1 :
        os.system("sudo apt update && sudo apt upgrade -y")
        os.system("clear")
        cprint("     \n update & upgrade finished !",'green',attrs=['bold'])
        proc()
    elif int(cho)==2 :
        cprint("please enter name app or pkg :",'magenta',attrs=['bold'])
        pkgs = input("#> ")
        os.system("sudo apt search {}".format(pkgs))
        cprint("     \n done !",'green',attrs=['bold'])
        proc()
    elif int(cho)==3 :
        cprint("please enter name app or pkg :",'magenta',attrs=['bold'])
        inpkg = input("#> ")
        os.system("sudo apt install {}".format(inpkg))
        cprint("     \n done !",'green',attrs=['bold'])
        proc()
    elif int(cho)==4 : 
        os.system("clear")
        logome()
        cprint("""
        1 . start 
        2 . stop 
        3 . enable
        4 . restart 

            9 - to back menu 
            0 - to exit :) 
        """,'cyan',attrs=['bold'])
        cho1 = input("   :@> ") 
        if int(cho1) == 1 :
          try : 
                cprint("please enter name of service :",'magenta',attrs=['bold'])
                serc= input("#>")
                os.system("sudo systemctl start {}".format(serc))
                cprint("""  
                            Enter q to exit :) """,'yellow',attrs=['bold'])
                os.system("sudo systemctl status {}".format(serc))
                

          except : 
                cprint("Service not found ") 
                proc()
        elif int(cho1) == 2 :
            try : 
                cprint("please enter name of service :",'magenta',attrs=['bold'])
                serc= input("#>")
                os.system("sudo systemctl stop {}".format(serc))
                cprint("""  
                            Enter q to exit :) """,'yellow',attrs=['bold'])
                os.system("sudo systemctl status {}".format(serc))
                proc()
            except : 
                cprint("Service not found ") 
                proc()
        elif int(cho1) == 3 :
            try : 
                cprint("please enter name of service :",'magenta',attrs=['bold'])
                serc= input("#>")
                os.system("sudo systemctl enable {}".format(serc))
                cprint("""  
                            Enter q to exit :) """,'yellow',attrs=['bold'])
                os.system("sudo systemctl status {}".format(serc))
                proc()
            except : 
                cprint("Service not found ") 
                proc()
        elif int(cho1) == 4 :
            try : 
                cprint("please enter name of service :",'magenta',attrs=['bold'])
                serc= input("#>")
                os.system("sudo systemctl restart {}".format(serc))
                cprint("""  
                            Enter q to exit :) """,'yellow',attrs=['bold'])
                os.system("sudo systemctl status {}".format(serc))
                proc()
            except : 
                cprint("Service not found ") 
                proc()
        elif int(cho1) == 9 :
            proc()
        elif int(cho1) == 0 :
            cprint("    \n  Goodluck ! :)       \n",attrs=['bold'])
            exit()
        else :
            cprint("Wrong input please try again")
            proc()
    elif int(cho)==0 :
        cprint("    \n  Goodluck ! :)       \n",attrs=['bold'])
        exit()
    
    else :
        cprint("Wrong input please try again")
        proc()
proc()
