def recursive_binary_search(alvo, lista, inicio=0, fim = None):
    if inicio >= fim:
        return -1
    elif fim == None:
        return -1
    
