letters= "abcdefghijklmnopqrstuvwxyz"
no_of_letters=len(letters)

def encrypt_decrypt(text,mode,key):
    result=""
    if mode == "d":
        key=-key
        
    for letter in text:
        if letter.isalpha():
            is_upper=letter.isupper()
            letter= letter.lower()
            index= letters.find(letter)
            if index == -1:
                result+= letter
            else:
                new_index= (index+key)%no_of_letters
                if is_upper:
                    result+=letters[new_index].upper()
                else:
                    result+=letters[new_index]
        else:
            result+= letter
    
    return result
                
print()
print("***CEASER CIPHER***")
print()
while(True):
    print("menu \n1.encrypt\n2.decrypt\n3.exit\n")
    ch=int(input("enter your choice: "))
    if ch==1:
        print("encryption mode selected")
        print()
        key= int(input("enter key in range [1,26]: "))
        text=input("enter text to encrypt: ")
        ciphertext= encrypt_decrypt(text,"e",key)
        print("CIPHERTEXT: ",ciphertext)
        print()
    elif ch==2:
        print("decryption mode selected")
        print()
        key= int(input("enter key in range [1,26]: "))
        text=input("enter text to decrypt: ")
        originaltext= encrypt_decrypt(text,"d",key)
        print('ORIGINALTEXT: ',originaltext)
        print()
    elif ch==3:
        break
    else:
        print("invalid choice please enter again")
        print()
        
    