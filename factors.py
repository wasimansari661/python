# program to find the factors and even and odd
try:
 num=int(input('Enter any number : '))
 #num=10
 for i in range(1,num):
    if ((num%i)==0):
        print ('Factor of : ', num, ' is ', i)
        if (i%2 ==0):
            print ('Even factor')
        else:
            print ('Odd factor')
except:
 print('Something went wrong')
finally:
    print('execute with the inpu only')