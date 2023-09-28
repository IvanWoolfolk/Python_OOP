def is_prime(num):
    result=0
    for i in range(2,num+1):
        if(num%i==0):
            result+=1
    if result<=1:
        result=True
    else:
        result=False
    return result
    #
    # Escribe tu código aquí.
    #

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
