
import requests , random , string 
import threading
import time,sys,os
import termcolor

#------------------- status symbol 
opt = termcolor.colored("[+]",'green')
note = termcolor.colored("[!]",'yellow')
os.system("clear") # command to clear terminal linux 


#------------------- user input 
print("\n========================# Options of the script #========================")
thread = int(input(f"{format(opt)} Enter number of threads : ")) 
numofpass = int(input(f"{format(opt)} The number of Password : "))
print("-------------------------------")
beforepass = input("Add text at the beginning of the lines [ write text here or leave blank  ] : ")
afterpass = input("Add text at the end of the lines? [ write text here or leave blank  ] : ")
print("-------------------------------")
print("The passwords length ")
minpass = int(input(f"{format(opt)} The min of the password :"))
maxpass = int(input(f"{format(opt)} The max of the password :"))
ftext = input(f"{format(opt)} The name of output file : ")

#------------------- function generate random digits 
def randgenerator(size=6, chars=string.digits) : # to add string for ex add this line { +string.ascii_uppercase } 
    return ''.join(random.choice(chars) for _ in range(size))
#------------------- size of min & max digits 
randSize = random.randint(minpass,maxpass)

#------------------- function to start generator the random digits and save the output in file text 
def generator():
    for i in range(numofpass):
        passlist = randgenerator(randSize)
        with open(f'{format(ftext)}.txt','a') as good :
            good.write(f"{format(beforepass)}"+passlist+f"{format(afterpass)}" + '\n')
print("-------------------------------")
print(f"{format(note)}     generating wordlist please wait ...")
print(f"{format(note)}     Number of threads is : {format(thread)} ")
print(f"{format(note)}     Output {format(ftext)}.txt")
print("===========================================\n")        


#------------------- to generate threads  
threads = []
for i in range(thread) :
    thread1 = threading.Thread(target=generator(),args=(1,))
    thread1.start()
    threads.append(thread1)
for thread2 in threads : 
    thread2.join() 
