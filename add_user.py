# importing linrary 
import os 
import subprocess 
import sys 
import getpass 
import fileinput
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

# replace function
def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

# add user function 
def add_user(): 
  
     # Ask for the input 
     username = 'chetan'
  
     # Asking for users password 
     password = input("enter your password: ")

     try: 
         # executing useradd command using subprocess module 
         command = 'useradd '+ '-G wheel ' + username
         command2 = 'echo ' + password + '| passwd chetan --stdin'
         os.system(command)
         os.system(command2)
         replace('/etc/ssh/sshd_config', 'PasswordAuthentication no', 'PasswordAuthentication yes')
     except: 
         print("Failed to add user.")                      
         sys.exit(1) 
  
add_user()
