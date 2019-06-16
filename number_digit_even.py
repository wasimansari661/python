#get the all number whose digit is all even

low_limit=int(input('Enter the low number : '))
up_limit=int(input('Enter the up number : '))
c=0

for i in range(low_limit,up_limit):
    list=[]
    flag = False
    for j in str(i):
        list.insert(c,j)
        c+=1
    for k in list:
        #print (k)
        if ((int(k)%2) != 0):
            flag=True
        elif(int(k)==0):
            flag=True
    if (flag is False):
        print('All Even digit number',i)