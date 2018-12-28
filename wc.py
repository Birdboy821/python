#wc.py
#christopher amell 12/26/18
#Word, line, and character Counter

def main():
    file = input('what file do you want the word count for (put ending to) ')
    #opening time for letters
    dFile = open(file , 'r')
    qFile = open(file , 'r')
    rFile = open(file , 'r')
    editFile = open(file ,'a')
    x = 0 #lines
    f = 0 #words
    t = 0

    #
    eFile = dFile.read()
    aFile = qFile.readlines()
    iFile = list(rFile.read())
    for i in aFile:
        x +=1
    
    for e in eFile.split():
        w = 0 #letters
        y = eFile.split(' ')[w]
        f += 1
        for a in list(iFile):
            w += 1
            t = w #save letters

    
    print(x,'lines', f,'words' , t - x, 'characters' , file=editFile)

    #closeing time for files
    qFile.close
    dFile.close
    rFile.close
    editFile.close
main()
        
        
