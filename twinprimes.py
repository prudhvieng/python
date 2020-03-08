ls = []
twinprime = []
for num in range (1001):
    if num>1:
        for i in range (2,num):
            if num%i == 0:
                break
        else:
            ls.append(num)
print (ls)
print (ls[-1])
for x,y in zip(ls[0::],ls[1::]):
    if y-x == 2:
        twinprime.append(x)
        twinprime.append(y)
#print (twinprime)
twinprime = list(dict.fromkeys(twinprime))
print (twinprime)
                         
        
