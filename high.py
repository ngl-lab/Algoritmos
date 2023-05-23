def high(x):
    # https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
    words = x.split()
    tmp = 0
    aux = 0
    result = ''
    alfabeto = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26,
    }

    for word in words:
        for value in word:
            tmp += alfabeto[value]

        if tmp > aux:
            result = word
        tmp, aux = aux, tmp

    return result


teste = 'man i need a taxi up to ubud'

print(high(teste))
