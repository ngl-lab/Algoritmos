def binary_search(num, listValues):
    rep = 0
    if listValues == '' or listValues == []:
        rep += 1
        return f"Lista Vazia\n{rep}"

    if num == listValues[len(listValues) // 2]:
        rep += 1
        return f"Alvo {num}, corresponde ao índice {len(listValues)//2} da lista de valores, {listValues[len(listValues)//2]}\n{rep}"
    else:
        if num < listValues[len(listValues)//2]:
            rep += 1
            return binary_search(num, listValues[(num+1):len(listValues)])
        rep += 1
        return binary_search(num-1, listValues[1:(num-1)])


valores = [x for x in range(1, 11)]
num = int(input('Digite um número de 1 - 1.000.000 \n'))

print(binary_search(num, valores))


# 20 para um 1.000.000 de valores
