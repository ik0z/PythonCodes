

# Coded By Khaled Alshammri | i5irh.a@gmail.com
# Project for satr.codes 
#-----------------
import os ,sys , base64


#----------------- menu  
def menu():
    print("\n   [ Phonebook manager ] " )
    print("""
          1. Add new user
          2. Delete user 
          3. Search [ By Name or Phone number ]
          4. Show all Users 
          
          5. Clear all contacts  
          0. To exit 
          
          8. About me
          """)
    
#---------------- About me 
def aboutme():
    message = 'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCktoYWxlZCBBbHNoYW1tcmkgfCBDb21wdXRlciBFbmdpbm5lcmluZyAKfiBpbnRlcmVzdGVkIHdpdGggY3liZXJzZWN1cml0eSAKfiBlbWFpbCA6IGk1aXJoLmFAZ21haWwuY29tCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ=='
    bytes = message.encode('ascii')
    message_bytes = base64.b64decode(bytes)
    message = message_bytes.decode('ascii')

    print(message)
aboutme()
#----------------- Users Info 

phonebook = {
    "Amal" : 1111111111,
    "Mohammed" : 2222222222,
    "Khadijah" : 3333333333,
    "Abdullah" : 4444444444,
    "Rawan" : 5555555555,
    "Faisal" : 6666666666,
    "Layla" : 7777777777 ,
    "Khaled": 8888888888
}
    
#----------------- Show all users in Dic -
def AllUser():

    for key, value in phonebook.items():
        print ("Name         : " + key)
        print ("Phone Number : " + str(value) + "\n")
                 
                 
#----------------- Add new user -  
def addUser():
    addname = input("Contact name : ")
    while True : 
        addPhoneNum = input("Enter Phone number : ")
        if len(addPhoneNum) > 10 or len(addPhoneNum) < 10: 
            print("This is invalid number try again ")
            option1 = int(input("\n Do you want to try again? [1]yes or [0]No : "))
            if option1 == 1:
                continue                    
            elif option1 == 0: 
                print(" \n Back to menu")
                menu()
            else : 
                print("[x] Invalid Option Please try again ")
            menu()         
        elif len(addPhoneNum) == 10 : 
            phonebook[addname] = "{}".format(addPhoneNum)
            print("The Contact {} and number {} is added successfully ! ".format(addname,addPhoneNum))
            break
        else : 
            print("[x] Invalid Option Please try again .1")
    
#---------------- Delete user -

def delUser():
    
    deluser = input("Please Enter the name of user : ")
    if deluser in phonebook.keys() : 
        print("User is founded ")
        del phonebook[deluser]
        print ("User  {} is removed ".format(deluser))
    else : 
        print("[!] Sorry, the user is not found")


#---------------- Search By Number *
def SearchByNumber(val): 
    for key, value in phonebook.items():
         if val == value:
             return key
 
    return "[!] Sorry, the number is not found"
        
#---------------- Search By name -
def SearchByName():
    print("")
    Sbyname = input("Please Enter the name of user : ")
    if Sbyname in phonebook.keys():
        print("\n The name : {} ".format(Sbyname))
        result= phonebook.get(Sbyname)
        print("Phone Number :",result)
    else :
        print("[!] Sorry, the user is not found ")
        
#---------------- Clear all contacts
def clearContacts():
    print("Warining : this option is delete all contacts are you sure ?") 
    selectOpdelete = input("Write 'delete' to continue :")  
    if selectOpdelete.lower()=="delete" :
        phonebook.clear()
        print("done !")
    else :
        print("Failed to clear")

#---------------- Count the user in the contacts

def countusers() : 
    print("The total users :",len(phonebook.keys()))
    print("The total numbers :",len(phonebook.values())) 
    print("\n")
#---------------- Execute program     

while True : 
    menu()
    countusers()
    try : 
        selectOp = int(input("Enter your choice :"))
        if selectOp == 1 : 
            addUser()
        elif selectOp == 2 :
            delUser()
        elif selectOp == 3 :
            print("""
                  You can use two method to search : 
                  1 . to search with [Name]
                  2 . to search with [Phone number]
                  """)
            selectSmethod = int(input("Enter your choice :"))
            if selectSmethod == 1 :
                SearchByName()
            elif selectSmethod == 2 :
                PhoneNumber = int(input("Enter the phone number : "))            
                print("Phone number username : ",SearchByNumber(PhoneNumber))
        
        elif selectOp == 4 : 
            AllUser()
        
        elif selectOp == 5 :
            clearContacts()
            continue 
        elif selectOp == 8 :
            aboutme()
        elif selectOp == 0 : 
            print(" \n GoodBye ...")
            break
        else :
            print ("[x] Invalid input ")
    except : 
        print("[x] Invalid input")

