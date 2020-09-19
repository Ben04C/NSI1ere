
import math
result=0
characters=0
isbnWithout=""
#Request code from user
isbn = input("Input the ISBN :");


def validate():
    print("Converting your ISBN in a readable form")
    for car in isbn:
        #test
        if car!="-":
            global characters
            characters +=1
        else:
            characters=characters
            
    isbnWithout = isbn.replace('-', '')
        
            
    if characters == 13:
        #this is a ISBN 13
        print("This is an isbn 13")
        print("Checking if it's valid...")
        sum=isbnWithout[0]+isbnWithout[1]*3+isbnWithout[2]+isbnWithout[3]*3+isbnWithout[4]+isbnWithout[5]*3+isbnWithout[6]
        sum=sum+isbnWithout[7]*3+isbnWithout[8]+isbnWithout[9]*3+isbnWithout[10]+isbnWithout[11]*3
        print(sum)
        global result
        for car in sum:
            result = result + int(car)
        leftFromDivision=int(result)%10
        test=10-leftFromDivision
        if 0 == int(isbnWithout[9]):
            print("HOORAY you ISBN is valid and this is an ISBN 10")
        if test == int(isbnWithout[12]):
            print("HOORAY you ISBN is valid and this is an ISBN 13")
        else:
            print("This isbn 13 is invalid")
            
            
    elif characters == 10:
        #This is an ISBN 10
        print("This is an isbn 10")
        print("Checking if it's valid...")
        sum=isbnWithout[0]*10+isbnWithout[1]*9+isbnWithout[2]*8+isbnWithout[3]*7+isbnWithout[4]*6+isbnWithout[5]*5+isbnWithout[6]*4
        sum=sum+isbnWithout[7]*3+isbnWithout[8]*2
        print(sum)
        for car in sum:
            result = result + int(car)
        print(result)
        simpleDivision=int(result)//11
        leftFromDivision=int(result)%11
        if 0 == int(isbnWithout[9]):
            print("HOORAY you ISBN is valid and this is an ISBN 10")
        test=11-leftFromDivision
        print(test)
        if test == int(isbnWithout[9]):
            print("HOORAY you ISBN is valid and this is an ISBN 10")
        else:
            print("This isbn 10 is invalid")
        
    else:
        if characters <10:
            print("Error: There is not enought characters")
            print("There needs to 10 numbers for an isbn 10 and 13 for an isbn 13")
        else:
            print("Error: There are too many characters")
            print("There needs to 10 numbers for an isbn 10 and 13 for an isbn 13")
            
        
        
#execute la fonction
validate()
