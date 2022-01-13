

import os , sys 
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
    elif cho.lower() =='exit' or cho.lower()=='end' :
        sys.exit()
    else : 
        print("Error input ! try again")
        continue
