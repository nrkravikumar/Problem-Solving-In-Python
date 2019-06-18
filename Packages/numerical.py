def isPrime(n):
    flag=True
    if n==2:
        return True    
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
            return flag
    if flag==True:
        return True
    return

def numberofPrimeFactors(n):
    if isPrime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if isPrime(i) and n%i==0:
            count+=1
    return count