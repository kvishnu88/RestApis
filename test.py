dic = {'a':1,'b':2,'c':3}
k = {val:key for key,val in dic.items()}
print(k)
lst = 'eihie'
lst1 = lst[::-1]
ind = -1
for i in lst:
    if i == lst[ind]:
        ind -=1
    else:
        print('Not pelendrome')
        break
else:
    print('string is pelindrome')


