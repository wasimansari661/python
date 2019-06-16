#get the string and digit in the sentence

sentence=input('enter the senetence : ')
digit_count=0
string_count=0
for i in sentence:
    if (i.isdigit()):
        digit_count+=1
    else:
        string_count+=1

print ('No of Digit' ,digit_count)
print ('No of Character', string_count)