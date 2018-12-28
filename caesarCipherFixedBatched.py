#caesarCipherFixedBatched.py
#christopher amell 12-25-2018
# encode and decode Caesar ciphers

def main():
    key = eval(input('what is your key (if decoding then use a negative) '))
    infile = open('inputCCFB.txt', "r")
    outfile = open('outputCCFB.txt', "w")
    x = 0
    z = 0
    mess = infile.readline()
    for i in mess.split(' '):
        y = mess.split(' ')[x]
        some = 0
        for c in list(y):
            z = (ord(y[some]) + key - 1) - 96
            alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
            print(alphabet[z], file=outfile)
            some += 1
        x += 1
        print(' ', file=outfile)

    infile.close()
    outfile.close()
main()
        
