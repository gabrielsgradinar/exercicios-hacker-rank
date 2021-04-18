if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    integeer_tuple = tuple(integer_list)

    print(hash(integeer_tuple))