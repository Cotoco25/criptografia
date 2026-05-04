def valida_email(email):
    return email[-8:] == "@puc.com" #ja q n botou um n final, vai ate o final da string



#print(valida_email("guigui@puc.com"))

def possuiMaiuscula(palavra):
    for letra in palavra:
        if "A" <= letra <= "Z": #letra.isupper()
            return True #Retorna True se a alguma letra na palavra estiver no range de "A" ate "Z"
    return False 

def possuiMinuscula(palavra):
    for letra in palavra:
        if "a" <= letra <= "z":
            return True #Retorna True se a alguma letra na palavra estiver no range de "a" ate "z"
    return False

def possuiNumero(palavra):
    for caracter in palavra:
        if "0" <= caracter <= "9": #Retorna True se a alguma letra na palavra estiver no range de "0" ate "9"
            return True
    return False

#print(possuiMaiuscula("dsahdsagbvceesfd"))

def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero

def criptografia(senha):
    #pegar a letra e converter para decimal ("Z" = 90)
    #Subtrair o valor decimal de 65 ("Z" = 90 - 65 = 25)
    #Somar 3 ao resultado do 2 (25 + 3 = 28)
    #Obter o resto da divisão do resultado de 3 por 26(28 % 26 = 2)
    #Somar o resto a 65 e converter valor de volta p/ letra (2+65 = 67 = "C")
    for char in senha:
        senha_cripto = ""
        for char in senha:
            if char.isdigit():
                ref = ord("0") #10
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha + 3 #etapa 3
                pos_resto = pos_cesar % 10 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_cripto += letra_cesar
            elif "A" <= char <= "Z":
                ref = ord("A") #65
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha + 3 #etapa 3
                pos_resto = pos_cesar % 26 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_cripto += letra_cesar
            elif "a" <= char <= "z":
                ref = ord("a") #65
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha + 3 #etapa 3
                pos_resto = pos_cesar % 26 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_cripto += letra_cesar
            else:
                senha_cripto += char
        return senha_cripto

print (criptografia("abc123@."))
senha_cripto_nova = criptografia("abc123@.")

def decriptografia(senha_cripto_nova):
    for char in senha_cripto_nova:
        senha_decripto = ""
        for char in senha_cripto_nova:
            if char.isdigit():
                ref = ord("0") #10
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha - 3 #etapa 3
                pos_resto = pos_cesar % 10 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_decripto += letra_cesar
            elif "A" <= char <= "Z":
                ref = ord("A") #65
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha - 3 #etapa 3
                pos_resto = pos_cesar % 26 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_decripto += letra_cesar
            elif "a" <= char <= "z":
                ref = ord("a") #65
                ascii_char = ord(char) #etapa 1
                pos_alpha = ascii_char - ref #etapa 2
                pos_cesar = pos_alpha - 3 #etapa 3
                pos_resto = pos_cesar % 26 #etapa 4
                letra_cesar = chr(pos_resto + ref) #etapa 5
                senha_decripto += letra_cesar
            else:
                senha_decripto += char
        return senha_decripto

print (decriptografia(senha_cripto_nova))

print(valida_senha("Abc@1234")) #True
print(valida_senha("ABC@1234")) #False
print(valida_senha("abc@1234")) #False
print(valida_senha("Abc@234")) #False
print(valida_senha("Abc@dsaj")) #False