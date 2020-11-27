c=str(input("Introduceti CNP-ul : "))
n=0
if (len(c)!=13) :
    print('Nu este corect')
else:
    for i in c :
        if ord(i) in range(48,58) :
            n+=1
    if (n==13) :
            print('Este corect')
    else:
            print('Nu este corect')            