import hashlib
import getpass

Passme = getpass.getpass('Password:')       #hide password
result = hashlib.sha512(Passme.encode())    #change type of hash md5 , sha1 ...etc
cPassme = result.hexdigest()
# To create hash :: https://sha512.online/
if cPassme == "ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413": # hash sha512 :: 123456
    print("hello")  
    # execute code here
else :
    print("failed")
    # execute code here
