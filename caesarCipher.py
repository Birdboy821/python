#caesarCipher.py
#christopher amell 12-23-2018
# encode and decode Caesar ciphers

def main():
    key = eval(input('what is your key (if decoding then use a negative) '))
    mess = input('what is your message you are encoding or decoding ')
    x = 0
    z = 0
    for i in (list(mess)):
        y = ord(mess[x])
        z = y + key
        x += 1
        print(chr(z))
main()
        
