import os
print()
print('PORTYPI support')
print()
print('REQUIREMENTS:\n*INSTALL python \n*INSTALL os pip package\n*INSTALL FIGLET \n*INSTALL python-nmap(pip) ')
print()
print('1.LINUX(debian)\n2.TERMUX(experimental)\n\n')
print('While installing if you face any ERRORS! just Run "support.py" file.1\nif it not automated')
print()
sys=input('enter your device : ')
if sys=='1':
    os.system('sudo apt-get install python3-pip')
    os.system('sudo apt-get install figlet')
    os.system('pip install python-nmap')
    os.system('clear')
    print('installation done!')
elif sys=='2':
    os.system('pkg install python3-pip')
    os.system('pkg install figlet')
    os.system('pip install python-nmap')
    os.system('clear')
    print('installation done!')
else:
    print('wrong option !!!')
        
import time  
import nmap  
s =input('DO YOU WANT TO CONTINUE (y/n): ')

if s=='y' or s=='yes':
    try:
        os.system('clear')
        os.system('figlet PortyPi| lolcat -a -p 4 -F 0.5 -d 5')

        #os.system('pip install python-nmap')
        
        

        
        def stp():
            os.system('clear')
            os.system('figlet fuck You | lolcat -a -d 5 -F 1')
            time.sleep(2)
            os.system('clear')
        def tryag():
            os.system('figlet tryagain | lolcat -a -d 3 -F 1')
        ns = nmap.PortScanner()

        while True:
            print('PORT Scanner in python\n \nSelect from the options you have.\nType "exit" when you want to stop')
            print()
            print('1.show all opened ports')
            print('2.find a specific port')
            print('3.show all hosts')
            print('4.check for device (on or off)')
            print('5.exit')
            print()
            usr=input('Enter the option : ')
            print()
            if usr=='1':
                IP=input('enter the ip you want to scan : ')
                if  IP=='exit':
                    stp()
                else:    
                    ns.scan(IP,'1-65535','-v --version-all')
                    print('The opened ports are : ',ns[IP]['tcp'].keys())
                
            elif usr=='2':
                while True:
                    print()
                    IP=input('Enter the host ip you want to scan port or type "exit" : ')
                    if IP=="exit":
                        stp()
                    else:
                        port=input('Port number you want to check (1-65535) ex.80 : ')
                        ns.scan(IP,port,'-v --version-all')
                        print('the port is : ',ns[IP].has_tcp(int(port)))
                continue
            elif usr=='3':
                print()
                IP=input('Enter the host ip you want to scan port  : ')
                port=input('Port number you want to check (1-65535) ex.1-40 : ')
                if IP=='exit' or port=='exit':
                    stp()
                else:
                    print()
                    print('HOSTS scanned\n',ns.all_hosts())
                    print()
                    print('IP TABLE : \n',ns.csv())
                continue
            elif usr=='4':
                os.system('clear')
                print('Check whether the host is Up or Down \n')
                IP=input('Enter the host ip you want to check : ')
                if IP=='exit':
                    stp()
                else:    
                    port='1-65535'
                    ns.scan(IP,port,'-v --version-all')
                    print(ns[IP].state() )
                    exit()
            elif usr=='5':
                stp()
                break
            elif usr=='exit' or usr=='stop':
                stp()
            else:
                print('please try valid input')
                print()
                continue
    except ModuleNotFoundError:
        print('ERROR OCCURED!!!!!')
        print()
        print('REQUIREMENTS:\n*INSTALL python \n*INSTALL os pip package\n*INSTALL FIGLET \n*INSTALL python-nmap(pip) ')
        print()
        print('1.LINUX(debian)\n2.TERMUX(experimental)\n\n')
        print('While installing if you face any ERRORS! just Run "support.py" file.1\nif it not automated')
        sys=input('enter your device : ')
        if sys=='1':
            os.system('sudo apt-get install python3-pip')
            os.system('sudo apt-get install figlet')
            os.system('pip install python-nmap')
            os.system('clear')
            print('done!')
        elif sys=='2':
            os.system('pkg install python3-pip')
            os.system('pkg install figlet')
            os.system('pip install python-nmap')
            os.system('clear')
            print('installation done!')
        else:
            print()
            print('not valid!')
            print()
            exit()

    except KeyError:
        print()
        print('invalid input \n\n TRY AGAIN !!')
        tryag()

    except AssertionError:
        print()
        print('Keep in Mind while Typing bitch')
        tryag()

    
