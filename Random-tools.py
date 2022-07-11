import sys
from os import system
import time
import socket
from colorama import Fore, Style,  Back
import pyfiglet
from pyfiglet import Figlet
import random

system("clear")
Act = pyfiglet.figlet_format("    [ System ]")
print(Fore.YELLOW+ Act, Fore.GREEN+ "                        OFFENSIVE  SECURITY v.3.0")
print (Fore.GREEN+ "#####################################################")
print (Fore.YELLOW+ "#################### SHARKZY SOFTWARE ###############")
print ("############# SYSTEM INFO TOOLS v.3.0 ###############")
print (Fore.GREEN+"#####################################################")

time.sleep(2)

print ("\nYOUR OS IS:", Fore.YELLOW+sys.platform, "operating system")
time.sleep(2)
print (Fore.GREEN+"\nYOUR SYSTEM TIME IS: ", Fore.YELLOW+time.ctime())

time.sleep(2)
print (Fore.YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ac = Figlet(font='mini')
print(Fore.GREEN+ ac.renderText("   :::: WELCOME     USER :::: "))
print (Fore.YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)

pasw = input(Fore.BLUE+"::::::::::::::::ENTER TOOL PASSWORD::::::::::::::::::\n"+Fore.GREEN)

print (Fore.YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if pasw == '772003':
   print ("::::::::::::::::::PASSWORD VERIFIED::::::::::::::::::")
   
else :
    print(Fore.RED+":::::::::::::::::PASSWORD UNVERIFIED:::::::::::::::::")
    print(Fore.YELLOW+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sys.exit()   

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(5)
print (Fore.GREEN+"[✓]choose an option  |")
print ("~~~~~~~~~~~~~~~~~~~~~~\n")
time.sleep(1)
print (Fore.WHITE+"[1].memory information\n")
time.sleep(1)
print ("[2].network status\n")
time.sleep(1)
print ("[3].system ip interface\n")
time.sleep(1)
print ("[4].ping target\n")
time.sleep(1)
print ("[5].cpu information\n")
time.sleep(1)
print ("[6].connect to a server\n")
time.sleep(1)
print("[7].Get website IP address\n")
time.sleep(1)
print("[8].Strong Password Generator\n")
time.sleep(1)
print ("[0].Exit the program ]")
time.sleep(1)

print (Fore.GREEN+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(1)
usr = input("\n[+]ENTER AN OPTION: \n"+Fore.YELLOW)


if usr == '1':
    print ("GETTING MEMORY INFOMATION:\n")
    system("clear")
    system("cat /proc/meminfo")
    print ("#######################################################")
    
elif usr == '2':
    time.sleep(3)
    system("clear")
    print ("CHECKING NETWORK STATUS\n")
    system("netstat")
    print ("#######################################################")
    print ("THANKS @SHARKZY")
    
elif usr == '3':
    time.sleep(3)
    system("clear")
    print ("CHECKING IP INTERFACE\n")
    system("ifconfig") 
    print ("#######################################################")
    print ("THANKS @SHARKZY")
    
elif usr == '4':
    time.sleep(3)
    system("clear")
    hat = input(Fore.GREEN+"[+].ENTER TARGET WEBSITE OR HOST IP:\n"+Fore.WHITE)
    print (Fore.YELLOW+"\n:::Getting Target info:::\n"+Fore.WHITE)
    system("ping -w 20 " +hat)
    print ("#######################################################")
    print ("THANKS @SHARKZY")
    
    
elif usr == '5':
    time.sleep(3)
    system("clear")    
    system("cat /proc/cpuinfo")
    
elif usr == '0':
    time.sleep(3)
    os.exit()
    print ("THANKS @SHARKZY")
            
    
elif usr == '6':
        time.sleep(3)
        system("clear")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("##################################################")
            print ("Socket successfully created")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except socket.error as err:
      
             print ("socket creation failed with error ", (err))
             print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
        port = 80
        print("\nmake sure there is internet connection\n\nlet (www) be the website protocol\n\nexample: www.google.com\n ") 
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        usr = input("enter server name or ip adress of server :\n")  
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
        try:
           host_ip = socket.gethostbyname(usr)
    
        except socket.gaierror:
 
              print ("there was an error resolving the host")
              print("try checking the internet connection and  spellings")
              sys.exit()

        s.connect((host_ip, port))

        user = (host_ip, port)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        data = input("enter message: \n")
        data = data.encode('ascii')
        s.sendto(data, user)
        socket.close(0)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


        print ("the socket has successfully connected to ", (usr), "at", time.ctime())
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nmessage sent successfully")
        print ("#######################################################")
        print ("THANKS @SHARKZY")
        
elif usr == '7':
    time.sleep(2)
    system("clear")
    print("GET TARGET WEBSITE\n") 
    time.sleep(1)
    try:
        socket.gethostbyname("www.google.com")
    except socket.gaierror:
        print("No internet connection") 
        sys.exit(0)
        print("\nTHANKS @SHARKZY")    
 
    _host_ = input("Enter target URL ADDRESS\n"+ Fore.WHITE+ "https://") 
   
    try:
           _name_ = socket.gethostbyname(_host_)
    except socket.gaierror:
          print("no website found\ntry checking your internet")
          sys.exit(0) 
          print("THANKS @SHARKY")     
          
    print("Target IP is :  ", Fore.GREEN+ _name_+ Style.RESET_ALL)
    print("\nTHANKS  @SHARKY")

elif usr == '8':
        time.sleep(2)
        system("clear")
        print("PASSWORD GENERATOR\n")
            
        try:
            num = int(input(Fore.GREEN+"Enter Password Length [1-40]: "+Style.RESET_ALL))
            print(" ")    
        except:
            print(Fore.RED+"enter correct value") 
            quit(0)
        if num >= 41:
            print(Fore.GREEN+"length range 1-40")
            quit(0) 
       
        try:       
            len = int(input(Fore.GREEN+"Number of password that should be generated: "+ Style.RESET_ALL))
            print(" ")
        except:
            print(Fore.RED+"enter correct value")
            quit(0)
            print(Style.RESET_ALL+"THANKS @SHARKZY")
    
    
        x = 'abcdefghijklmnopqrstuvwxyz'
        y = '1234567890'
        z = '@#[]'

        u = x + y + z
        for i in range(len):
            r = "".join(random.sample(u, num))
            print(r,)
            print(" ")
        print("THANKS @SHARKZY")

                
else :
        sys.exit() 
        print ("#######################################################")
        print ("THANKS @SHARKZY")
       
