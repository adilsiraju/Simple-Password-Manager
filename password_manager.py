#module to encrypt text.
from cryptography.fernet import Fernet

#Encryption Logic
# key + pswd + text_to_encrypt = random_text
# random_text + key + pswd = text_to_encrypt



# Below code is commented since we'll run it once only.
'''def write_key():
    key = Fernet.generate_key()
    #create a "key" file named key, in "write in byte" format
    with open("key.key", "wb") as key_file:
        #write into the key file
        key_file.write(key)
        
write_key()'''



def load_key():
    # File opened in "read-byte" mode
    file = open('key.key', 'rb')
    # Read File
    key = file.read()
    # File closed
    file.close()
    # Key is returned
    return key

key = load_key() 
fer = Fernet(key)

def view():
    #open pswd.txt file in read format
    with open('passwords.txt', 'r') as f:
        #for loop to read through every line
        for line in f.readlines():
            #remove the extra space in end of pswds.txt file
            data = line.rstrip()
            #split data in file to username and password with the " | " as separator.
            username, pswd = data.split("|")
            # encode and decrypt to display
            print("User: ",username,"\tPassword: ", 
                #  We must encode and decrypt before decoding 
                  fer.decrypt(pswd.encode()).decode())

def add():
    user = input('Username: ')
    pswd = input('Password: ')

    #open pswd.txt file in read format
    with open('passwords.txt', 'a') as f:
        #store username and password and 
        # We encrypt and encode, before decoding
        f.write(user + "|" + fer.encrypt(pswd.encode()).decode() + "\n" )


while True:
    mode = input("Do you want to 'add' a new password or 'view' existing ones ? You may also press 'q' to quit.\n").lower()
    
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue