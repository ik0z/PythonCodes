
import requests , random , string 
import threading
import progressbar as pb
import time,sys,os
from tqdm import tqdm


#------------------- user input 
thread = int(input(" Enter number of threads : ")) 
numofpass = int(input("The number of Password : "))
beforepass = input("Add text at the beginning of the lines [ write text here or leave blank  ] ? ")
afterpass = input("Add text at the end of the lines? [ write text here or leave blank  ] ")
print("-------------------------------")
print("The passwords length ")
minpass = int(input("minimum :"))
maxpass = int(input("maximum :"))

#------------------- function generate random digits 
def randgenerator(size=6, chars=string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))
#------------------- size of min & max digits 
randSize = random.randint(minpass,maxpass)

#------------------- function to start generator the random digits and save the output in file text 
def generator():
    for i in range(numofpass):
        passlist = randgenerator(randSize)
        with open('hello.txt','a') as good :
            good.write(f"{format(beforepass)}"+passlist+f"{format(afterpass)}" + '\n')
        
#------------------- function to call the generator and show progress 
def cal():
    print("     generating wordlist please wait ...")
    print("     Number of threads is : {} ".format(thread))
    print("================================================================================================\n")
    for i in tqdm(range(100)):
        generator()
    time.sleep(0.1)

#------------------- to generate threads  
threads = []
for i in range(thread) :
    thread1 = threading.Thread(target=cal(),args=(1,))
    thread1.start()
    threads.append(thread1)
for thread2 in threads : 
    thread2.join() 
