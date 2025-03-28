def calculation(initial, final):
    if initial < final:
        hours = final - initial
        return f"O JOGO DUROU {hours} HORA(S)"
    elif initial > final:
        hours = (24 - initial) + final
        return f"O JOGO DUROU {hours} HORA(S)"
    return "O JOGO DUROU 24 HORA(S)"


initial, final = map(int, input().split())

print(calculation(initial, final))
