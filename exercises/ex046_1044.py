def Multiple(a, b):
    if a % b == 0:
        return 'Sao Multiplos'
    elif b % a == 0:
        return 'Sao Multiplos'
    else:
        return 'Nao sao Multiplos'


a, b = map(int, input().split(" "))
print(Multiple(a, b))
