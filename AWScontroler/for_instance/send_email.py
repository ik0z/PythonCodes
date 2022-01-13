import smtplib , socket ,os
from requests import get 


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local = s.getsockname()[0]
s.close()
ip = get('https://api.ipify.org').text

curruse = os.getlogin()

contant = '''
EC2 : {} 
-----------------------
Your instance is Online now info :
local IP address  : {}  
public IP address : {}
'''.format(curruse,local,ip)
#Email content
TO = 'receiver email '
SUBJECT = 'your instance {} is Online '.format(curruse)
TEXT = '{}'.format(contant)

# Gmail Sign In
gmail_sender = 'Your Email'
gmail_passwd = 'Password'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
