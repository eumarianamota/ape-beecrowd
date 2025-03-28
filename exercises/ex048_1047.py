def calculation(initial_hour, initial_minute, final_hour, final_minute):
    initial = (initial_hour * 60) + initial_minute
    final = (final_hour * 60) + final_minute

    if initial < final:
        hours = (final - initial) // 60
        minutes = (final - initial) % 60
        return f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)"
    elif initial > final:
        hours = ((1440 - initial) + final) // 60
        minutes = ((1440 - initial) + final) % 60
        return f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)"
    return "O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)"


ih, im, fh, fm = map(int, input().split())

print(calculation(ih, im, fh, fm))
