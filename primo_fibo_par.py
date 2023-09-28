"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""

def primo_fibo_par(num:int): 
    #Es impar o par
    if(num%2!=0):
        odd_even="impar"
    elif(num%2==0):
        odd_even="par"
    #Es primo o no
    for i in range(2,num+1):
        if(num==0 or num==1):
            prime="no es primo"
            break
        elif(i==num):
            prime="es primo"
        elif(num%i==0):
            prime="no es primo"
            break
    return odd_even,prime

#Es fibonachi o no
def fibonachi(num:int):
    if (num==0 or num==1):
        return 1
    else:
        num -= 1
        return fibonachi(num)+fibonachi(num-1)
    fibo_dict={num:}

#num=int(input())
num=13

lista_fibo=[fibonachi(num)]
for i in lista_fibo:
    if num==i:
        fibo_yes="Es fibonachi"
    else:
        fibo_yes="No es fibonachi"
print(f"{num} es {primo_fibo_par(num)} y {fibo_yes}")
