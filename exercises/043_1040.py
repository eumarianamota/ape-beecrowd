#Beecrowd | 1040
def media(n1, n2, n3, n4) :
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
    return media


n1, n2, n3, n4 = map(float, input().split(" "))
media = media(n1, n2, n3, n4)
print(f'Media: {media:.1f}')

if media >= 7:
    print(f'Aluno aprovado.')
elif media < 5:
    print(f'Aluno reprovado.')
elif 6.9 >= media >= 5:
    print("Aluno em exame.")

    exame = float(input())
    print(f"Nota do exame: {exame}")

    new_media = (media + exame) / 2
    if new_media >= 5:
      print(f'Aluno aprovado.')
      print(f"Media final: {new_media:.1f}")
    else: 
      print(f"Aluno reprovado.")
      print(f"Media final: {new_media:.1f}")