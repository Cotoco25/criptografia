import random
vida = 6
lista_palavras = ["arroz", "banana", "queijo", "alface", "frango"]

palavra_escolhida = random.choice(lista_palavras)
print(palavra_escolhida)
letras_acertadas = ["_"] * len(palavra_escolhida)

while vida >0 and "_" in letras_acertadas:
    letra = input("Qual letra vc quer?")
    if letra in palavra_escolhida:
        print("Acertou!")
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_acertadas[i] = letra
        print(letras_acertadas)
    else:
        print("Errou!")
        vida = vida-1
        print(f"sobraram {vida} vidas")

if "_" not in letras_acertadas:
    print(f"\nParabéns! A palavra era {palavra_escolhida}")
else:
    print(f"\nGame Over! A palavra era {palavra_escolhida}")