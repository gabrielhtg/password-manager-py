import os
from colorama import Fore
from colorama import Style
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

os.system('cls')

#function location
def add(kode) :
    username = input("Masukkan username : ")
    userpwd  = input("Masukkan password : ")
    
    with open("pwd.txt", "a") as file :
        file.write(username + "|" + Fernet(kode).encrypt(userpwd.encode()).decode() + "\n")
        

def view(kode) :
    with open("pwd.txt", "r") as file :
        for i in file.readlines() :
            baris = i.rstrip()
            usnm, pw = baris.split("|")
            
            try :
                print("  * Username :", usnm, "\n    Password :", Fernet(kode).decrypt(pw.encode()).decode())
                
            except :
                continue
            
def cls() :
    os.system('cls')

print("----------------------------------------------------------------------------------------")
print("                               G PASSWORD MANAGER          ")
print("----------------------------------------------------------------------------------------")
master_password = input("Input master password : ")
salt = b'\xdf;\xbd\xb7}U\x15\xcb^W\xc1\xa2\x11\xb6cr'
kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend
)

key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

cls()

while True :
    print("----------------------------------------------------------------------------------------")
    print("                               G PASSWORD MANAGER          ")
    print("----------------------------------------------------------------------------------------")
    print("  - add  (a)\n  - view (v)\n  - quit (q)")
    mode = input("Apa yang ingin anda lakukan : ").lower()

    if (mode == "add") or (mode == "a") :
        add(key)
        cls()
        
    elif (mode == "view") or (mode == "v") :
        cls()
        print("----------------------------------------------------------------------------------------")
        view(key)
        
    elif (mode == "quit") or (mode == "q") :
        break
        
    else :
        cls()
        print("----------------------------------------------------------------------------------------")
        print(Fore.RED + Style.BRIGHT + "Invalid input. Coba lagi!!" + Style. RESET_ALL)
        continue
        
print("----------------------------------------------------------------------------------------")