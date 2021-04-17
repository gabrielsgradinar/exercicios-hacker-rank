if __name__ == '__main__':
    n = int(input())
    pontuacoes = [[input(), float(input())] for _ in range(n)]

    segundo_maior =  sorted(list(set([notas for _, notas in pontuacoes])))[1]

    for nome, nota in sorted(pontuacoes):
        if nota == segundo_maior:
            print(nome)


