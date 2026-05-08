from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

running = True
clock=time.Clock()
background_color = (112, 128, 144)

def valida_email(email_cod):
    return email_cod[-8:] == "@puc.com"
    

fonte = font.Font("Worldstar.ttf", 40)

estado_email = ""
estado_senha = ""


email = ""
email_final = ""
modo = ""

senha_teclado = ""
senha_final = ""

criptografia_teclado = ""
decriptografia_teclado = ""

tela_atual = "login"

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
    senha_cripto = "" # 1. Fica de fora do loop
    for char in senha: # 2. Apenas UM loop
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
            ref = ord("a") #97
            ascii_char = ord(char) #etapa 1
            pos_alpha = ascii_char - ref #etapa 2
            pos_cesar = pos_alpha + 3 #etapa 3
            pos_resto = pos_cesar % 26 #etapa 4
            letra_cesar = chr(pos_resto + ref) #etapa 5
            senha_cripto += letra_cesar
        else:
            senha_cripto += char
            
    return senha_cripto


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



while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()

        print(mouse_x)

        if tela_atual == "login":
            if modo == 1:
                if ev.type == KEYDOWN:
                    if ev.key == K_BACKSPACE:
                        email = email[:-1]
                    elif ev.key == K_RETURN:
                        email_final = email
                        if valida_email(email_final):
                            estado_email = "valido"
                        else:
                            estado_email = "invalido"
                    else:
                        email += ev.unicode



            if modo == 2:
                if ev.type == KEYDOWN:
                    if ev.key == K_BACKSPACE:
                        senha_teclado = senha_teclado[:-1]
                    elif ev.key == K_RETURN:
                        senha_final = senha_teclado
                        if valida_senha(senha_final):
                            estado_senha = "valido"
                        else:
                            estado_senha = "invalido"
                    else:
                        senha_teclado += ev.unicode
            


            


            if ev.type == MOUSEBUTTONDOWN:
                if 50<=mouse_x<=150 and 20<=mouse_y<=90:
                    if ev.button == 1:
                        modo = 1

            if ev.type == MOUSEBUTTONDOWN:
                if 200<=mouse_x<=350 and 20<=mouse_y<=90:
                    if ev.button == 1:
                        modo = 2

            if ev.type == MOUSEBUTTONDOWN:
                if 350<=mouse_x<525 and 20<=mouse_y<=90:
                    if ev.button == 1:
                        criptografia_teclado = criptografia(senha_teclado)
            
            if ev.type == MOUSEBUTTONDOWN:
                if 580<=mouse_x<800 and 20<=mouse_y<=90:
                    if ev.button == 1:
                        decriptografia_teclado = decriptografia(criptografia_teclado)

            if estado_email == "valido" and estado_senha == "valido":
                if ev.type == MOUSEBUTTONDOWN:
                    if 1000<=mouse_x<1180 and 600<=mouse_y<=700:
                        if ev.button == 1:
                            tela_atual = "menu"

        elif tela_atual == "menu":
                if 400 <= mouse_x <= 880:
                    if 200 <= mouse_y <= 270:
                        print("Jogo 1")
                    elif 300 <= mouse_y <= 370:
                        print("Jogo 2")
                    elif 400 <= mouse_y <= 470:
                        print("Jogo 3")

    if tela_atual == "login":
        draw.rect(window, (120, 120, 120), (50, 20, 100, 70))
        draw.rect(window, (0, 0, 0), (50, 20, 100, 70),5)

        draw.rect(window, (120, 120, 120), (200, 20, 100, 70))
        draw.rect(window, (0, 0, 0), (200, 20, 100, 70),5)

        draw.rect(window, (120, 120, 120), (350, 20, 175, 70))
        draw.rect(window, (0, 0, 0), (350, 20, 175, 70),5)

        draw.rect(window, (120, 120, 120), (575, 20, 230, 70))
        draw.rect(window, (0, 0, 0), (575, 20, 230, 70),5)

        window.blit(fonte.render("Email:", True, (0,0,0)), (50, 130))
        draw.rect(window, (255, 255, 255), (50, 170, 800, 60))
        draw.rect(window, (0, 0, 0), (50, 170, 800, 60),5)

        window.blit(fonte.render("Senha:", True, (0,0,0)), (50, 250))
        draw.rect(window, (255, 255, 255), (50, 290, 800, 60))
        draw.rect(window, (0, 0, 0), (50, 290, 800, 60),5)

        window.blit(fonte.render("Senha Criptografada:", True, (0,0,0)), (50, 380))
        draw.rect(window, (255, 255, 255), (50, 420, 800, 60))
        draw.rect(window, (0, 0, 0), (50, 420, 800, 60),5)

        window.blit(fonte.render("Senha De-criptografada:", True, (0,0,0)), (50, 510))
        draw.rect(window, (255, 255, 255), (50, 550, 800, 60))
        draw.rect(window, (0, 0, 0), (50, 550, 800, 60),5)

        window.blit(fonte.render("Email", True, (0,0,0)), (60, 40))
        window.blit(fonte.render("Senha", True, (0,0,0)), (210, 40))
        window.blit(fonte.render("Criptografia", True, (0,0,0)), (360, 40))
        window.blit(fonte.render("De-Criptografia", True, (0,0,0)), (585, 40))

        if modo == 1:
            window.blit(fonte.render("modo email", True, (0,0,0)), (1000, 40))
        
        if modo == 2:
            window.blit(fonte.render("modo senha", True, (0,0,0)), (1000, 40))
        
        if modo == 3:
            window.blit(fonte.render("modo criptografia", True, (0,0,0)), (1000, 40))
        
        window.blit(fonte.render(f"{senha_teclado}", True, (0,0,0)), (60, 300))
        window.blit(fonte.render(f"{criptografia_teclado}", True, (0,0,0)), (60, 430))
        window.blit(fonte.render(f"{decriptografia_teclado}", True, (0,0,0)), (60, 560))


        window.blit(fonte.render(f"{email}", True, (0,0,0)), (60, 180))
        #window.blit(fonte.render(f"{email_final}", True, (0,0,0)), (100, 500))

        if estado_email == "valido":
            window.blit(fonte.render("email valido", True, (0,0,0)), (1000, 180))
        
        if estado_email == "invalido":
            window.blit(fonte.render("email invalido", True, (0,0,0)), (1000, 180))


        if estado_senha == "valido":
            window.blit(fonte.render("senha valido", True, (0,0,0)), (1000, 300))
        
        if estado_senha == "invalido":
            window.blit(fonte.render("senha invalido", True, (0,0,0)), (1000, 300))

        if estado_email == "valido" and estado_senha == "valido":
            draw.rect(window, (120, 120, 120), (1000, 600, 180, 100))
            draw.rect(window, (0, 0, 0), (1000, 600, 180, 100),5)
            window.blit(fonte.render("Continuar:", True, (0,0,0)), (1020, 630))
        
    if tela_atual == "menu":
        window.blit(fonte.render("Escolha o seu Jogo:", True, (0,0,0)), (450, 100))

        draw.rect(window, (150, 150, 200), (400, 200, 480, 70))
        draw.rect(window, (0, 0, 0), (400, 200, 480, 70), 5)
        window.blit(fonte.render("Casinha do matue", True, (0,0,0)), (520, 215))

        draw.rect(window, (150, 200, 150), (400, 300, 480, 70))
        draw.rect(window, (0, 0, 0), (400, 300, 480, 70), 5)
        window.blit(fonte.render("Forca", True, (0,0,0)), (590, 315))

        draw.rect(window, (200, 150, 150), (400, 400, 480, 70))
        draw.rect(window, (0, 0, 0), (400, 400, 480, 70), 5)
        window.blit(fonte.render("Adivinhacao", True, (0,0,0)), (560, 415))

    display.update()