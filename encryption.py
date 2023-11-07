import random
import string

def reverse(text_to_encrypt):
    return text_to_encrypt[::-1]


def get_random_string():
    text=""
    for i in range(3):
        character=random.choice(string.ascii_lowercase)
        text=text+character
    return text    

def encryption():
    text_to_encrypt=input("Enter text : ")
    if(len(text_to_encrypt)<3):
        return reverse(text_to_encrypt)

    else:
        text4=""
        text1=get_random_string()
        text2=text_to_encrypt[:0]+text_to_encrypt[1:]
        text3=text_to_encrypt[0]
        text4=get_random_string()

        text5=text1+text2+text3+text4

        return text5
    


result=encryption()
print(f"Your Encrypted code is {result}")    
    

secret_code="mainnhibataunga"

def check_password():
    try:
        password=input("Enter password : ")
        if(password==secret_code):
            print("correct Password!!!")
            result=decryption()
            return result

    except:
        print("Wrong Password!!!")   


def decryption():
    text1=""
    text2=""
    encrypted_code=input("Enter encryted code : ")
    msg_len=len(encrypted_code)-6
    text1=encrypted_code[3:]
    text2=text1[:msg_len]
    last=text2[len(text2)-1]
    
    text3=last+text2[:len(text2)-1]

    return text3

final=check_password()
print(f"Your code after decreaption is {final}")