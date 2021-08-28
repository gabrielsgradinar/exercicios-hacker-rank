if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lista = list(arr)

    primeiro = max(lista)

    while max(lista) == primeiro:
        lista.remove(primeiro)

    print(max(lista))
        