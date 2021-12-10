import os
import sys
import time
import subprocess


#main banner function of our tool kit
def __banner__():

	timeto_end_loop = time.time()+1*5

	while time.time() < timeto_end_loop:
	    print("""
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

	    print("""
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
	    
	print("""
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
				         		 |_|            PTYHON TOOL KIT! """)

#main menu function
def __main_menu__():
	print(" ----------------------------- ")
	print("| [+] 1 -> DOS ATTACK         |")
	print("| [+] 2 -> SPREAD WORM        |")
	print("| [+] 3 -> EXTRACT PASWORDS   |")
	print("| [!] 0 -> Quit!		     |")
	print(" ----------------------------- ")


#handleeing code execution
if __name__ == '__main__':
	__banner__()
	__main_menu__()

	opt = int(input("[+] Enter Option to Perform: "))

	if opt == 0:
		print("[!] Quitting...")
		sys.exit(1)

	elif opt == 1:
		subprocess.call('./wifiter.sh')
	elif opt == 2:
		os.system('python fattynigger.py')
	elif opt == 3:
		subprocess.call('./pisher.sh')
	else:
		exit(1)
