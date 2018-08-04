def fact(n):
    i = n;
    res = 1;
    while(i!=0):
        res*=i;
        i-=1
    return res
print fact(10)
