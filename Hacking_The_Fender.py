import csv 
#Creating an empty list of compromised users
compromised_users = []
#Defining function to add compromised passwords to the list. You would need an actual saved password.csv file 
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username']) 
#Defining a function to write a file with compromised usernames
with open('compromised_users.txt', 'w') as compromised_user_file:
  for i in compromised_users:
    compromised_user_file.write(i)

import json
#Sending a private message with JSON
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = { 'recipient': 'The Boss', 'message' : 'Mission Success'}
  json.dump(boss_message_dict, boss_message)
#writing a new password file to make it look like another hacker hacked the list
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''
  new_passwords_obj.write(slash_null_sig)