def print_formatted(number):
    for i in range(1, number+1):
        width = len(bin(number)[2:])
        decimal = str(i).rjust(width,' ')
        octal = oct(i)[2:].rjust(width,' ')
        hexadecimal = hex(i)[2:].rjust(width, ' ').upper()
        binary = "{0:b}".format(i).rjust(width, ' ')

        print(f"{decimal} {octal} {hexadecimal} {binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)