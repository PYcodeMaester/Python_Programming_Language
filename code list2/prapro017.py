d=[['Sona',-25.001],['Mona',-25.0001],['Mini',-25],['Rita',-25]]
#d=[['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
for j in range(len(d)):
    for i in range(0,j):
        if(d[i][1]>d[i+1][1]):
            d[i],d[i+1]=d[i+1],d[i]
        elif(d[i][1]==d[i+1][1]):
            if(d[i][0]>d[i+1][0]):
                if(d[i][0]>d[i+1][0]):
                   d[i+1],d[i]=d[i],d[i+1]
print(d)
a=[]
for i in range(0,len(d)-1):
    if(d[i+1][1]>d[i][1]):
        for j in range(i,len(d)-1):
            if(d[j+1][1]==d[j][1]):
                a.append(d[j][0])
                a.append(d[j+1][0])
        #a.sort()
        print(a)
        for k in range(0,len(a)):
            print(a[k])
        break
if(len(a)==0):
    print(d[1][0])
    
