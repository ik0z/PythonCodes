import time , sys , base64 , os ,ctypes
from sys import platform
from termcolor import * 
import socket
from requests import get 
class bcolors:  # colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


phpcode = """<?$date = gmdate("y/m/d")  ; $time = gmdate("H:i:s")     ; $ip = getenv("REMOTE_ADDR"); $port = getenv("REMOTE_PORT"); $browser = getenv("HTTP_USER_AGENT") ; $v_fopen = fopen("track.txt","a+") ; fwrite($v_fopen , "$date *** $time *** $ip *** $port *** $browser\n") ; fclose ($v_fopen);?>"""
def logo():
    cprint("""  
    ____________________________________________________

    ╔╦╗╔═╗┌─┐┌─┐┌─┐     Khaled
     ║ ╠═╝├─┤│ ┬├┤      Track visitors [Python , php ] 
     ╩ ╩  ┴ ┴└─┘└─┘     i5irh.a@gmail.com
    ____________________________________________________
        
        """,'blue',attrs=['bold'])
No = bcolors.HEADER+"[+]"
def options():
    no1 = bcolors.OKCYAN+"1"
    no2 = bcolors.OKCYAN+"2"
    cprint("""

    {}  . Create code php to inject 
    {}  . Create & deploy php tracker 


    """.format(no1,no2),'blue')
def ipinfo():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    cprint("Private IP    : {}".format(s.getsockname()[0]),'yellow',attrs=['bold'])
    s.close()
    ip = get('https://api.ipify.org').text
    cprint('Public IP   : {}'.format(ip),'red',attrs=['bold'])
def dojob():
    
    mksp = os.system("mkdir {}\kAz".format(serpath))
    f = open("{}/kAz/index.php".format(serpath), "a")
    f.write(phpcode)
    f.close()
    f = open("{}/kAz/track.txt".format(serpath), "a")
    f.write("-")
    f.close()
    time.sleep(3)

def listen():
    ipinfo()
    cprint("-------------------------------------------------------",'yellow')
    cprint("                  Result visitors page                ",'green',attrs=['bold'])
    cprint("-------------------------------------------------------",'yellow')
    filePath = '{}/kAz/track.txt'.format(serpath)
    lastLine = None
    with open(filePath,'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print(No+""+bcolors.HEADER+line)
                lastLine = line

    while True:
        with open(filePath,'r') as f:
            lines = f.readlines()
        if lines[-1] != lastLine:
            lastLine = lines[-1]
            print(No+""+bcolors.HEADER+lines[-1])
        time.sleep(1)
#check OS 
if platform == "linux" or platform == "linux2": 

    os.system("clear")
    if os.getuid() !=0 : 
        print(bcolors.HEADER+"          This script need root privilege         ")
    else : 
        
        logo()
        print(bcolors.OKGREEN+"         WoW root privilege O_O      ")
        options()

        cho = input(bcolors.OKBLUE+"    Enter your choice : ")
        if cho == '1' :
            print(bcolors.OKGREEN+"     Copy this code and paste in any php file        ")
            print("")
            cprint(phpcode,'yellow')
            print("")
        elif cho == '2' : 
            serpath = '/var/www/html'
            print(bcolors.WARNING+"     The deploy path is : {}/kAz".format(serpath))
            os.system("rm -r {}/kAz".format(serpath))
            os.system("mkdir {}/kAz/".format(serpath))
            os.system("sudo chmod 777 {}/kAz/".format(serpath))
            time.sleep(2)
            os.system('sudo chmod 777 {}/kAz/*'.format(serpath))
            f = open("{}/kAz/index.php".format(serpath), "a")
            f.write(phpcode)
            f.close()
            f = open("{}/kAz/track.txt".format(serpath), "a")
            f.write("")
            f.close()
            print(bcolors.OKGREEN+"   deploy is done")
            time.sleep(5)
            filePath = serpath
            listen(serpath)
           


elif platform == "win32":
    os.system('cls')
    def checkpriv():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if checkpriv():
    # Code of your program here
        logo()
        cprint("\n        administrator privilege nOW 0_0 ",'green')
        options()
        chow = input(bcolors.OKBLUE+"    Enter your choice : ")
        if chow =='1' : 
            print(bcolors.OKGREEN+"     Copy this code and paste in any php file        ")
            print("")
            cprint(phpcode,'yellow')
            print("")
        elif chow == '2' :           
            serpath = input(bcolors.OKGREEN+'   Enter local server path : ')
            dojob()
            time.sleep(1)
            listen()

    else :
    # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        logo()
        print("\n         WoW administrator privilege now 0_0 ! ",'green')
        options()
        chow = input(bcolors.OKBLUE+"    Enter your choice : ")
        if chow =='1' : 
            print(bcolors.OKGREEN+"     Copy this code and paste in any php file        ")
            print("")
            cprint(phpcode,'yellow')
            print("")
        elif chow == '2' :           
            serpath = input(bcolors.OKGREEN+'   Enter local server path : ')
            dojob()
            time.sleep(1)
            listen()
