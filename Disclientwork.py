from time import time 
from scapy.all import Ether,ARP,srp 
import os , sys ,time, ctypes, sys
from scapy.ansmachine import AnsweringMachine
from termcolor import *
from colorama import Fore, Style
from sys import platform



#--------------------------------linux OS -----------------------------
su = f"{Fore.RED}sudo python3 scprit.py"
if platform == "linux" or platform == "linux2": 
    if os.getuid() !=0 :
        cprint("""Need root privilege to this script""",'yellow',attrs=['bold'])
        cprint("        try {}""".format(su))
    else :
        example = colored(" for ex 192.168.1.0/24   OR 192.168.1.2 ",attrs=['dark'])
        def scanetwork() :
            eth_head = Ether(dst="FF:FF:FF:FF:FF:FF")
            ip_range = input("Enter IP  {}:".format(example))
            arp_opt = ARP(pdst=ip_range)

            arp_pack = eth_head / arp_opt
            result , noresult = srp(arp_pack,timeout=2)
            cprint("__________________________________________________",'cyan')
            cprint("IP's                              MAC",'cyan')
            for send , recive in result :
                rIP=recive[Ether].psrc
                rMAC=recive[Ether].hwsrc
            
                if recive[Ether].psrc=="":
                    cprint("NO Result !",'yellow') 
                else : 
                    print(recive[Ether].psrc+"             "+recive[Ether].hwsrc)
                    

                

        scanetwork()
        cprint("__________________________________________________\n",'cyan')
        us_ask = input(f" {Fore.YELLOW}   [r] to rescan or [ press any key to exit ! ] : ")

        if us_ask.lower()=='r' : 
            print("")
            scanetwork()
        else :
            cprint("see you soon (0_~)",'green',attrs=['blink'])
            time.sleep(2)
   
#------------------------- Windows OS -----------------------------------------
elif platform == "win32":
    def checkpriv():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if checkpriv():
        example = (f"{Fore.YELLOW} for ex 192.168.1.0/24   OR 192.168.1.2 ",)
        def scanetwork() :
            eth_head = Ether(dst="FF:FF:FF:FF:FF:FF")
            ip_range = input(f"{Fore.GREEN}Enter IP  {format(example)}:")
            arp_opt = ARP(pdst=ip_range)

            arp_pack = eth_head / arp_opt
            result , noresult = srp(arp_pack,timeout=2)
            print(F"{Fore.CYAN}__________________________________________________")
            print("IP's                              MAC")
            for send , recive in result :
                rIP=recive[Ether].psrc
                rMAC=recive[Ether].hwsrc
                print(rIP+"             "+rMAC)

                

        scanetwork()
        print(F"{Fore.CYAN}__________________________________________________\n")
        us_ask = input(f" {Fore.YELLOW}   [r] to rescan or [ press any key to exit ! ] : ")

        if us_ask.lower()=='r' : 
            print("")
            scanetwork()
        else :
            cprint("see you soon (0_~)",'green',attrs=['blink'])
            time.sleep(2)
    else :
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        checkpriv()
