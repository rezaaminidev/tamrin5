L1 = ['reza' , 'ahmad' , 'hasan' , 'mohamad' , 'amirhosein' , 'hosein']
L2 = ['ali' , 'parviz' ,'reza' , 'mohamad' , 'mansoor' , 'amirhosein' , 'sfandiar']
result = []
for i in L1:
    if i not in L2:
        result.append(i)
for i in L2:
    if i not in L1:
        result.append(i)

print(result)