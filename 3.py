'''Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?'''

n = 13195
l = 0
while n > 1:
    n -= 1
    for l in n:
        
        if n % l == 0:
            print(n)
