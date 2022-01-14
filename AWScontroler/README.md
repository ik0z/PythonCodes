This repo to make OpenVPN with remotly control [ YOU don't need login to start & stop EC2 instances ] : 


# AWS Instance Part : 

1 - create the EC2 instance [ OPENVPN or any linux OS ] 

2 - lunch the instance and write this line inside crontab to schedule the tasks
```
sudo crontab -e 
```
###### Put this line in last line [ create the bashexe.sh in ur instance ] : ``` @reboot sh /home/your user/bashexe.sh ```
###### Now new line then put this line [ create the bashtimer.sh in ur instance ] : ``` @reboot sh /home/your user/bashtimer.sh ```

Explain : 
##### Bashexe to execute the python code  [ send_email.py ] with details { IP addresses ,Name of EC2 }
##### Bashtimer to make instance stop running after 2 hours 


# Controller Part [ local or with other server its up to you ]  : 

1 - you need put your credential AWS in [ aws.yml ] { key_id , secret key , region and instances id } 

2 - for manual control just you need deal with  [ ec2controller.py ] 
command : 
```
python3 ec2controller.py --help 
```

3 - Auto start stop you just with [ control_Panel.py ] 
```
python3 control_Panel.py 
```




![alt text](https://raw.githubusercontent.com/ik0z/PythonCodes/main/AWScontroler/ex.png)


Enjoy 
