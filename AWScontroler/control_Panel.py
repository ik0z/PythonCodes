

import os , sys 
sshpass = 'yourpassword'
sshkey = '/home/~/aws.pem'
sshuser = 'user name'
ec21 = 'i-0~'
ec22 = 'i-0~'
print(""" EC2 instances : 
     *. i-0~ (kAz)
      """)



while True :
    print("""
          
        #####################
        #   Simple Panel    #
        #####################
          """)
    cho = input("[1] all start  | [0] all stop  :")
    if cho == '1' :
        #os.system('python3 ec2manage.py --start {}'.format(ec21))
        os.system('python3 ec2manage.py --start {}'.format(ec22))
        print("done !")
        continue
    elif cho =='0' : 
        #os.system('python3 ec2manage.py --stop {}'.format(ec21))
        os.system('python3 ec2manage.py --stop {}'.format(ec22))
        print("done !")
        continue
     elif cho.lower()=='c' :
        ipaws = input("IP Address : ")
        cho2 = input(" [ k ] for ssh pem key | [ p ] for ssh password ")
        if cho2.lower()=='k' :
            os.system('sudo ssh -i "{}" kali@{} -p 7621'.format(sshkey,ipaws))
            break
        elif cho2.lower()=='p' :
            os.system("sudo apt install sshpass")
            os.system('sudo sshpass -p {} ssh {}@{}'.format(sshpass,sshuser,ipaws))
    elif cho.lower() =='exit' or cho.lower()=='end' :
        sys.exit()
    else : 
        print("Error input ! try again")
        continue
