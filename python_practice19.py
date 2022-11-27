def primes(n=100):
    l=[]
    x=2
    while (len(l)<n):
        for i in range(2, int(x**0.5)+1):
            if(x%i==0):
                break
            else:
                l.append(x)
            x=x+1
    return l
n=int(input("Enter No of primes wanted:"))
print("List of First",n,"primes",primes(n))
print("List of first '100' primes:", primes())
                