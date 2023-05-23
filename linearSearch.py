def linear_search(num):
    rep = 0
    for x in range(1, 1000000):
        rep += 1
        if x == num:
            return (x, rep)
    return None


num = int(input('Digite um número de 1 - 1.000.000 \n'))

print(linear_search(num))
