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
print (Fore.GREEN+ "#"*53)
print (Fore.YELLOW+ "#"*18,"SHARKZY SOFTWARE", "#"*16)
print ("#"*18, "SYSTEM INFO TOOLS v.3.0", "#"*16)
print (Fore.GREEN+"#"*53)

time.sleep(2)

print ("\nYOUR OS IS:", Fore.YELLOW+sys.platform, "operating system")
time.sleep(2)
print (Fore.GREEN+"\nYOUR SYSTEM TIME IS: ", Fore.YELLOW+time.ctime())

time.sleep(2)
print (Fore.YELLOW+"~"*53)
ac = Figlet(font='mini')
print(Fore.GREEN+ ac.renderText("   :::: WELCOME     USER :::: "))
print (Fore.YELLOW+"~"*53)
time.sleep(3)

while True:
    pasw = input(Fore.BLUE+"::::::::::::::::ENTER TOOL PASSWORD::::::::::::::::::\n"+Fore.GREEN)

    print (Fore.YELLOW+"~"*53)

    if pasw == '772003':
       print ("::::::::::::::::::PASSWORD VERIFIED::::::::::::::::::")
       break
   
    else :
        print(Fore.RED+":::::::::::::::::PASSWORD UNVERIFIED:::::::::::::::::")
        print(Fore.YELLOW+"~"*53)
        continue

print ("~"*53)
time.sleep(5)
print (Fore.GREEN+"[✓]choose an option  |")
print ("~"*22,"\n")
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

print (Fore.GREEN+"~"*53)
time.sleep(1)
usr = input("\n[+]ENTER AN OPTION: \n"+Fore.YELLOW)


if usr == '1':
    print ("GETTING MEMORY INFOMATION:\n")
    system("clear")
    system("cat /proc/meminfo")
    print ("#"*53)
    
elif usr == '2':
    time.sleep(3)
    system("clear")
    print ("CHECKING NETWORK STATUS\n")
    system("netstat")
    print ("#"*53)
    print ("THANKS @SHARKZY")
    
elif usr == '3':
    time.sleep(3)
    system("clear")
    print ("CHECKING IP INTERFACE\n")
    system("ifconfig") 
    print ("#"*53)
    print ("THANKS @SHARKZY")
    
elif usr == '4':
    time.sleep(3)
    system("clear")
    hat = input(Fore.GREEN+"[+].ENTER TARGET WEBSITE OR HOST IP:\nMake sure there is internet connection\n"+Fore.WHITE)
    while True:
        try:
            data = socket.gethostbyname("www.google.com")
            break
        except socket.gaierror:
            print("connect to the internet")
            continue
    print (Fore.YELLOW+"\n:::Getting Target info:::\n"+Fore.WHITE)
    system("ping -w 20 " +hat)
    print ("#"*53)
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
            print("#"*53)
            print ("Socket successfully created")
            print("~"*53)
        except socket.error as err:
      
             print ("socket creation failed with error ", (err))
             print ("~"*53)
 
        port = 80
        print("\nmake sure there is internet connection\n\nlet (www) be the website protocol\n\nexample: www.google.com\n ") 
        print ("~"*53)
        usr = input("enter server name or ip adress of server :\n")  
        print("~"*53)
        while True:
            try:
               host_ip = socket.gethostbyname(usr)
               break
    
            except socket.gaierror:
 
               print ("there was an error resolving the host")
               print("try checking the internet connection and  spellings")
               continue

        s.connect((host_ip, port))

        user = (host_ip, port)
        print ("~"*53)


        data = input("enter message: \n")
        data = data.encode('ascii')
        s.sendto(data, user)
        socket.close(0)
        print ("~"*53)


        print ("the socket has successfully connected to ", (usr), "at", time.ctime())
        print ("~"*53)
        print("\nmessage sent successfully")
        print ("#"*53)
        print ("THANKS @SHARKZY")
        
elif usr == '7':
    time.sleep(2)
    system("clear")
    print("GET TARGET WEBSITE\n") 
    time.sleep(1)
    while True:
        try:
            socket.gethostbyname("www.google.com")
            break
        except socket.gaierror:
            print("No internet connection") 
            continue   
 
    _host_ = input("Enter target URL ADDRESS\n"+ Fore.WHITE+ "https://") 
    try:
           _name_ = socket.gethostbyname(_host_)
    except socket.gaierror:
          print("no website found\ntry checking your internet")
          
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
        print ("#"*53)
        print ("THANKS @SHARKZY")
       
