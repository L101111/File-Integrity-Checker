import os
import hashlib
from termcolor import colored, cprint

logo = colored('''
 _                              _             
| |       _                    (_)  _         
| |____ _| |_ _____  ____  ____ _ _| |_ _   _ 
| |  _ (_   _) ___ |/ _  |/ ___) (_   _) | | |
| | | | || |_| ____( (_| | |   | | | |_| |_| |
|_|_| |_| \__)_____)\___ |_|   |_|  \__)\__  |
                   (_____|             (____/ 
 _______ _                 _  Made by                
(_______) |               | |   heisenberg                
 _      | |__  _____  ____| |  _ _____  ____  
| |     |  _ \| ___ |/ ___) |_/ ) ___ |/ ___) 
| |_____| | | | ____( (___|  _ (| ____| |     
 \______)_| |_|_____)\____)_| \_)_____)_|     
                                              
        Welcome to Integrity Checker


    ''', 'blue')

print(logo)
def create_hashes():
    directory = input('Enter the path: ')

    if os.path.isdir(directory):
        output_file_path = os.path.join(directory, "hash_values.txt")
        with open(output_file_path, "w") as hash_file:
            for file in os.listdir(directory):
                fpath = os.path.join(directory, file)
                if os.path.isfile(fpath):
                    sha256_hash = hashlib.sha256()
                    with open(fpath, "rb") as f:
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                    hash_value = sha256_hash.hexdigest()
                    hash_file.write(f"{file}: {hash_value}\n")
        cprint(f"Hash values have been stored in {output_file_path}, 'blue'")
    else:
        cprint("Invalid directory path..." "red")

def check_integrity():
    user_home = os.path.expanduser("~")
    hv_path = os.path.join(user_home, "hash_values.txt")
    directory = input('Enter the path: ')
    print(' ')
    with open(hv_path, "r") as hash_file:
        found= True
        for line in hash_file:
            file_name, hash_value = line.strip().split(': ')
            if os.path.isfile(os.path.join(directory, file_name)):
                sha256_hash = hashlib.sha256()
                with open(os.path.join(directory, file_name), "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                current_hash = sha256_hash.hexdigest()
                if current_hash == hash_value:
                    cprint(f'{file_name.ljust(30)} [+]', 'blue')
                else :
                    cprint(f'{file_name.ljust(30)} [-]', 'red')
                    found=False
            else:
                cprint(f'{file_name.ljust(30)} not found', 'red',)
    if found:
        cprint('All hashes match!')
cprint('''
[1] Create database with hash values for files
[2] Check if file's hashes match with the database

    ''', 'yellow')




try:
    x=input(': ')
    if int(x) == 1:
        create_hashes()

    elif int(x) == 2:
        check_integrity()

    else:
        cprint('wrong parameters...')
except KeyboardInterrupt:
    print()
    cprint('exiting...', 'red')

