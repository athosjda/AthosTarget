def inverte(string):
    nova_string = []
    for idx in range(1, len(string)+1):
        nova_string.append(string[-idx])
    return ''.join(nova_string)

def main():
    print(inverte('Athos'))
    print(inverte('Luiz'))
    print(inverte('Banana'))
    print(inverte('2022'))


if __name__ == "__main__":
    main()