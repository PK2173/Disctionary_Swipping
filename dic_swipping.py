g=['employee 1','employee 2','employee 3']
b=['Name','Age','Designation']
c=[['Aman','32','HR'],['Abhisak','28','Exicutive'],['Karan','24','Accountant']]
f=[]
for a in range(len(c)):
    e={
        b[0]:c[a][0],
        b[1]:c[a][1],
        b[2]:c[a][2]
    }
    f.append(e)
    x=zip(g,f)
    print(dict(x))
print(f)
n={}
for i in range(len(g)):
    n[g[i]]=f[i]
print(n)