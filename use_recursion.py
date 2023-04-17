#     ----- FACTORIAL USING FOR LOOP -----
#    n! = 1*2*3*4*......*n
#    n! = [1*2*3*4*.....*n-1]*n

#NOTE    n! = n*(n-1)!


n = int(input('the number'))
product =1
for i in range(n) :
    product = (i+1)*product
print(product)


#    ---------  FACTORIAL USING FACTORIAL ----------
def factorial(n) :
    product = 1
    for i in range (n):
        product = product *(i+1)
    return product

A = factorial(5)
print(A)

    #   HERE RECURSION IS USING FOR THE FOMULA:  n! = n*(n-1)!
def factorial_recursive(n) :
    if n == 1 or n == 0 :
        return 1
    return n *factorial_recursive(n-1)

B = factorial_recursive (5)
print(B)
