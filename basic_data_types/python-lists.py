if __name__ == '__main__':
    quantidade_comandos = int(input())
    lista = []
    for _ in range(quantidade_comandos):
        comando, *numeros = input().split()
        numeros = list(map(int, numeros))

        if comando == "insert":
            lista.insert(numeros[0], numeros[1])
        
        if comando == "print":
            print(lista)
        
        if comando == "remove":
            lista.remove(numeros[0])
        
        if comando == "append":
            for n in numeros:
                lista.append(n)

        if comando == "sort":
            lista.sort()
        
        if comando == "pop":
            lista.pop()

        if comando == "reverse":
            lista.reverse()
