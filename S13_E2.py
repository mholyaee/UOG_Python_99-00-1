
def power(n,m):
    P=1
    for i in range(m):
        P*=n
    return P

n=int(input("Your Measure:"))
print(10*power(n,3)-2*power(n,2)+11*n+5)
#10x^3-2x^2+11x+5
