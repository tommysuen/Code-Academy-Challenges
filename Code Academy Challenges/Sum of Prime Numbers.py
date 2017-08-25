#Finds Sum of Prime Numbers
def Sum_of_primes(n):
    S = [x for x in range(2, n+1) if 0 not in [x % y for y in range(2, x)]]
    return S

print(sum(Sum_of_primes(100)))
     
                                    
