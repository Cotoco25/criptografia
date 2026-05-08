from pygame import *
import sys
import random

init()

window = display.set_mode((1280,720))

#parte normal
running = True
clock=time.Clock()
background_color = (112, 128, 144)

def valida_email(email_cod):
    return email_cod[-8:] == "@puc.com"
    


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
if tela_atual == "login" or tela_atual == "menu":
    fonte = font.Font("Worldstar.ttf", 40)
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




#parte matue

raio_x = 140
nuvem_x=800
nuvem_y=100
velocidade_nuvem=3
velocidade_nuvem2=-3



matue_img = image.load("matue.png")
matue_img = transform.scale(matue_img, (180,200))

batman_font = font.Font("fontecarai.otf", 40)



feijao = mixer.Sound("feijao-com-farinha.mp3")
baby1 = mixer.Sound("baby1.mp3")
baby2 = mixer.Sound("baby2.mp3")
baby3 = mixer.Sound("baby3.mp3")

#programa para fazer o programa fechar com o X do windows
#se for desenhar alguma coisa, desenhar a partir do sys.exit()
modo_fundo = False

uuu=255
iii=188
ooo=99
if tela_atual == "matue":
    background_color = (uuu, iii, ooo)

modo_mouse = False

aaa = (uuu-(600//5.75))
bbb = (iii+(600//25))
ccc = (ooo+(600//3.95))






#parte forca
teclado_img = image.load("teclado.webp")
teclado_img = transform.scale(teclado_img, (1200,300))

coracao = image.load("heart.png")
coracao = transform.scale(coracao, (60,50))




dor = mixer.Sound("dor_fortnite.mp3")
acerto = mixer.Sound("acertou.mp3")
regenera = mixer.Sound("regenera.mp3")
vitoria = mixer.Sound("vitoria.mp3")
derrota = mixer.Sound("derrota.mp3")
adlib = mixer.Sound("adlib.mp3")
adlib.play()


temas = ["animais", "comidas/bebidas", "objetos", "profissoes", "marcas famosas", "PUC", "PUC RIO"]
tema_escolhido = random.choice(temas)
vidas=6
if tema_escolhido == "animais":
    lista_palavras = ["cachorro", "gato", "elefante", "leao", "girafa", "tigre", "urso", "coelho", "macaco", "pinguim", "zebra", "hipopotamo", "rinoceronte", "cavalo", "ovelha", "vaca", "porco", "galinha", "pato", "coruja", "lobo", "raposa", "cervo", "baleia", "golfinho", "tartaruga", "crocodilo", "jacare", "camelo", "panda", "leopardo", "pantera", "canguru", "coala", "foca"]

if tema_escolhido == "comidas/bebidas":
    lista_palavras = ["arroz", "banana", "queijo", "alface", "frango", "tomate", "chocolate", "pao", "leite", "feijao", "macarrao", "sorvete", "abacaxi", "cenoura", "batata", "melancia", "cafe", "churrasco", "pizza", "hamburguer", "salada", "suco", "iogurte", "bolo", "pipoca", "sanduiche", "biscoito", "manteiga", "mel", "guarana", "cerveja", "vinho", "whisky", "vodka", "tequila", "rum", "champanhe", "energetico", "agua", "pitaya"]

if tema_escolhido == "objetos":
    lista_palavras = ["celular", "computador", "televisao", "cadeira", "mesa", "cama", "sofa", "geladeira", "fogao", "microondas", "ventilador", "arcondicionado", "impressora", "teclado", "mouse", "airpods", "relogio", "carregador", "lampada", "caneta", "caderno", "mochila", "chaveiro", "carteira", "oculos", "ferramenta", "brinquedo", "roupa"]

if tema_escolhido == "profissoes":
    lista_palavras = ["medico", "engenheiro", "professor", "advogado", "enfermeiro", "policial", "bombeiro", "piloto", "cozinheiro", "jornalista", "programador", "arquiteto", "dentista", "veterinario", "psicologo", "musico", "artista", "atleta", "cientista", "agricultor", "bicalho"]

if tema_escolhido == "marcas famosas":
    lista_palavras = ["nike", "adidas", "apple", "samsung", "cocacola", "pepsi", "mcdonalds", "starbucks", "google", "facebook", "amazon", "netflix", "disney", "honda", "toyota", "ford", "chevrolet", "bmw", "benz", "audi"]

if tema_escolhido == "PUC":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]

if tema_escolhido == "PUC RIO":
    lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]
    

palavra_escolhida = random.choice(lista_palavras)
letras_acertadas = ["_"] * len(palavra_escolhida)
contador = (f"Vidas: {vidas}")

timer_erro = 0
timer = 0
timer_derrota = 0
timer_erro_chute = 0

def verificar_letra(letra):
     global vidas, timer_erro, errou_texto, letras_acertadas
     if letra in palavra_escolhida:
        acerto.play()
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == letra:
                letras_acertadas[i] = letra
     else:
        dor.play()
        vidas-=1
        timer_erro = 120

def reiniciar_jogo():
    global palavra_escolhida, letras_acertadas, vidas, timer, timer_derrota, tema_escolhido
    regenera.play()
    tema_escolhido = random.choice(temas)
    if tema_escolhido == "animais":
        lista_palavras = ["cachorro", "gato", "elefante", "leao", "girafa", "tigre", "urso", "coelho", "macaco", "pinguim", "zebra", "hipopotamo", "rinoceronte", "cavalo", "ovelha", "vaca", "porco", "galinha", "pato", "coruja", "lobo", "raposa", "cervo", "baleia", "golfinho", "tartaruga", "crocodilo", "jacare", "camelo", "panda", "leopardo", "pantera", "canguru", "coala", "foca"]
    if tema_escolhido == "comidas/bebidas":
        lista_palavras = ["arroz", "banana", "queijo", "alface", "frango", "tomate", "chocolate", "pao", "leite", "feijao", "macarrao", "sorvete", "abacaxi", "cenoura", "batata", "melancia", "cafe", "churrasco", "pizza", "hamburguer", "salada", "suco", "iogurte", "bolo", "pipoca", "sanduiche", "biscoito", "manteiga", "mel", "guarana", "cerveja", "vinho", "whisky", "vodka", "tequila", "rum", "champanhe", "energetico", "agua", "pitaya"]
    if tema_escolhido == "objetos":
        lista_palavras = ["celular", "computador", "televisao", "cadeira", "mesa", "cama", "sofa", "geladeira", "fogao", "microondas", "ventilador", "arcondicionado", "impressora", "teclado", "mouse", "airpods", "relogio", "carregador", "lampada", "caneta", "caderno", "mochila", "chaveiro", "carteira", "oculos", "ferramenta", "brinquedo", "roupa"]
    if tema_escolhido == "profissoes":
        lista_palavras = ["medico", "engenheiro", "professor", "advogado", "enfermeiro", "policial", "bombeiro", "piloto", "cozinheiro", "jornalista", "programador", "arquiteto", "dentista", "veterinario", "psicologo", "musico", "artista", "atleta", "cientista", "agricultor", "bicalho"]
    if tema_escolhido == "marcas famosas":
        lista_palavras = ["nike", "adidas", "apple", "samsung", "cocacola", "pepsi", "mcdonalds", "starbucks", "google", "facebook", "amazon", "netflix", "disney", "honda", "toyota", "ford", "chevrolet", "bmw", "benz", "audi"]
    
    if tema_escolhido == "PUC":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]

    if tema_escolhido == "PUC RIO":
        lista_palavras = ["juiza", "joisa", "bicalho", "strogonoff", "julianofloss", "mralkmin", "dralkmin", "mrcookie", "ze", "fecundacao"]
    
    palavra_escolhida = random.choice(lista_palavras)
    letras_acertadas = ["_"] * len(palavra_escolhida)
    vidas = 6
    timer = 0
    timer_derrota = 0

if tela_atual == "forca":
    background_color = (112, 128, 144)
    fonte = font.Font("fonte.ttf", 40)
chique = font.Font("fontechique.ttf", 60)
chique_pequena = font.Font("fontechique.ttf", 25)





#parte pedra papel tesoura

soma = 0
soma_adv = 0
timer = 0
escolha = ""
escolha_ia = ["pedra", "papel", "tesoura"]
adversario = random.choice(escolha_ia)

#escolha = input("escolha: ")

pedra_img = image.load("pedra.png")
pedra = transform.scale(pedra_img, (300,300))

papel_img = image.load("papel.webp")
papel = transform.scale(papel_img, (300,300))

tesoura_img = image.load("tesoura.png")
tesoura = transform.scale(tesoura_img, (310,190))

if tela_atual == "pedra":
    background_color = (112, 128, 144)
    fonte = font.Font("fonte.ttf", 40)
    chique_pequena = font.Font("fontechique.ttf", 35)
chique = font.Font("fontechique.ttf", 60)
def ia_pedra(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_empate = chique.render(f"empate", True, (255,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_empate, (600,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 255, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 0:
                    reiniciar_jogo_pedra()
        elif escolha == "papel":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (500, 300,350,300))
                draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                timer -=1
            if timer == 239:
                    soma +=1
            if timer == 0:
                    reiniciar_jogo_pedra()
        elif escolha == "tesoura":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 239:
                    soma_adv +=1
            if timer == 0:
                reiniciar_jogo_pedra()



def ia_papel(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma_adv +=1
            if timer == 0:
                reiniciar_jogo_pedra()
        if escolha == "papel":
                if timer > 0:
                    result_empate = chique.render(f"empate", True, (255,255,0))
                    escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                    window.blit(result_empate, (600,200))
                    window.blit(escolha_adversario, (490,20))
                    draw.rect(window, (255, 255, 0), (500, 300,350,300))
                    draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                    timer -=1
                if timer == 0:
                    reiniciar_jogo_pedra()
        elif escolha == "tesoura":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma +=1
            if timer == 0:
                    reiniciar_jogo_pedra()
    


def ia_tesoura(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma +=1
            if timer == 0:
                reiniciar_jogo_pedra()
        elif escolha == "papel":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (500, 300,350,300))
                draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma_adv +=1
            if timer == 0:
                reiniciar_jogo_pedra()
        elif escolha == "tesoura":
            if timer > 0:
                result_empate = chique.render(f"empate", True, (255,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_empate, (600,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 255, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 0:
                reiniciar_jogo_pedra()


def reiniciar_jogo_pedra():
    global adversario, timer, escolha
    escolha = ""
    adversario = random.choice(escolha_ia)




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
                if ev.type == MOUSEBUTTONDOWN:
                    if 400 <= mouse_x <= 880 and 200 <= mouse_y <= 270:
                        if ev.button == 1:
                            tela_atual = "matue"
                            mixer.music.load("matue.mp3")
                            mixer.music.set_volume(0.3)
                            mixer.music.play(-1)
                    elif 400 <= mouse_x <= 880 and 300 <= mouse_y <= 370:
                            tela_atual = "forca"
                            mixer.music.load("musica_fundo.mp3")
                            mixer.music.set_volume(0.5)
                            mixer.music.play(-1)
                    elif 400 <= mouse_x <= 880 and 400 <= mouse_y <= 470:
                        tela_atual = "pedra"

        elif tela_atual == "matue":
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_SPACE:
                    modo_fundo = not modo_fundo
            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_x:
                    modo_mouse = not modo_mouse


            if ev.type == MOUSEBUTTONDOWN:
                if raio_x >0 and raio_x < 430 and modo_fundo == False:
                    if ev.button == 2:
                        baby1.play()

            if ev.type == MOUSEBUTTONDOWN:
                if raio_x >430 and raio_x < 860 and modo_fundo == False:
                    if ev.button == 2:
                        baby2.play()

            if ev.type == MOUSEBUTTONDOWN:
                if raio_x >860 and raio_x < 1350 and modo_fundo == False:
                #if background_color == (13, 29, 92):
                    if ev.button == 2:
                        baby3.play()

            if ev.type == MOUSEBUTTONDOWN:
                if modo_fundo == True:
                    if ev.button == 2:
                        feijao.play()


            if modo_fundo:
                background_color = (245,178,64)
            else:
                    if modo_mouse == False:
                        if raio_x < 600:
                            background_color = (uuu-(raio_x)//5.75, iii+(raio_x//25), ooo+(raio_x//3.95))
                        else:
                            if raio_x >= 600:
                                background_color = (aaa-((raio_x-600)//5), bbb-((raio_x-600)//4.3), ccc-((raio_x-600)//4.5))
                    else:
                        if modo_mouse == True:
                            if raio_x < 600:
                                background_color = (uuu-(raio_x)//5.75, iii+(raio_x//25), ooo+(raio_x//3.95))
                            else:
                                if raio_x >= 600:
                                    background_color = (aaa-((raio_x-600)//5), bbb-((raio_x-600)//4.3), ccc-((raio_x-600)//4.5))

        elif tela_atual == "forca":
            window.fill(background_color)
            
        

            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 235<mouse_x<296 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("q")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 309<mouse_x<369 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("w")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 381<mouse_x<443 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("e")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 454<mouse_x<517 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("r")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 529<mouse_x<592 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("t")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 600<mouse_x<664 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("y")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 677<mouse_x<739 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("u")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 748<mouse_x<811 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("i")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 822<mouse_x<883 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("o")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 895<mouse_x<960 and 551<mouse_y<586:
                    if ev.button == 1:
                        verificar_letra("p")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 248<mouse_x<309 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("a")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 320<mouse_x<382 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("s")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 393<mouse_x<456 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("d")
                        
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 469<mouse_x<530 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("f")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 541<mouse_x<604 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("g")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 614<mouse_x<677 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("h")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 688<mouse_x<752 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("j")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 762<mouse_x<825 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("k")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 836<mouse_x<896 and 593<mouse_y<629:
                    if ev.button == 1:
                        verificar_letra("l")
        
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 278<mouse_x<340 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("z")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 352<mouse_x<413 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("x")
        
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 426<mouse_x<488 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("c")
            
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 499<mouse_x<560 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("v")
        
            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 571<mouse_x<635 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("b")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 645<mouse_x<708 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("n")

            if ev.type == MOUSEBUTTONDOWN and vidas > 0:
                if 719<mouse_x<781 and 637<mouse_y<674:
                    if ev.button == 1:
                        verificar_letra("m")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_q:
                    verificar_letra("q")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_w:
                    verificar_letra("w")
            
            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_e:
                    verificar_letra("e")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_r:
                    verificar_letra("r")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_t:
                    verificar_letra("t")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_y:
                    verificar_letra("y")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_u:
                    verificar_letra("u")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_i:
                    verificar_letra("i")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_o:
                    verificar_letra("o")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_p:
                    verificar_letra("p")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_a:
                    verificar_letra("a")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_s:
                    verificar_letra("s")
            
            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_d:
                    verificar_letra("d")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_f:
                    verificar_letra("f")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_g:
                    verificar_letra("g")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_h:
                    verificar_letra("h")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_j:
                    verificar_letra("j")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_k:
                    verificar_letra("k")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_l:
                    verificar_letra("l")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_z:
                    verificar_letra("z")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_x:
                    verificar_letra("x")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_c:
                    verificar_letra("c")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_v:
                    verificar_letra("v")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_b:
                    verificar_letra("b")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_n:
                    verificar_letra("n")

            if ev.type == KEYDOWN and vidas > 0:
                key_pressed = ev.key
                if key_pressed == K_m:
                    verificar_letra("m")


        
            
            
            if ev.type == KEYDOWN and vidas>1:
                    if ev.key == K_SPACE:
                        print("\n" + "="*30)
                        print("MODO CHUTE ATIVADO!")
                        print("DIGITE SUA RESPOSTA E PRESSIONE ENTER")
                        print("="*30)
                        chute = input("Seu chute: ").lower().strip()

                        if chute == palavra_escolhida:
                            print("ACERTOU TUDO!")
                            letras_acertadas = list(palavra_escolhida)
                        else:
                            print("ERROU O CHUTE!")
                            vidas -= 2 
                            timer_erro_chute = 300



        elif tela_atual == "pedra":
            if timer == 0:
                if ev.type == MOUSEBUTTONDOWN:
                        if 100<mouse_x<450 and 300<mouse_y<600:
                            if ev.button == 1:
                                escolha = "pedra"
                                timer = 240
                                draw.rect(window, (255, 0, 0), (100, 300,350,300))

                    
                if ev.type == MOUSEBUTTONDOWN:
                        if 500<mouse_x<850 and 300<mouse_y<600:
                            if ev.button == 1:
                                escolha = "papel"
                                timer = 240

                
                if ev.type == MOUSEBUTTONDOWN:
                        if 900<mouse_x<1250 and 300<mouse_y<600:
                            if ev.button == 1:
                                escolha = "tesoura"
                                timer = 240

    if tela_atual == "forca":

        if timer_erro > 0:
                errou_texto = fonte.render(f"voce errou, e agora tem {vidas} vidas", True, (255,0,0))
                window.blit(errou_texto, (370,50))
                timer_erro -= 1

        if timer_erro_chute > 0:
            mensagem_erro = fonte.render(f"Chute errado!", True, (255,0,0))
            perdeu_vida2 = fonte.render(f"Perdeu 2 vidas!", True, (255,0,0))
            window.blit(mensagem_erro, (900,200))
            window.blit(perdeu_vida2, (900,250))
            timer_erro_chute -= 1


        #PALAVRA ESCOLHIDA
        #palavra_text = font.render(palavra_escolhida, True, (0,0,0))
        #window.blit(palavra_text, (570,400))

        texto_exibido = " ".join(letras_acertadas)
        letras_text = chique.render(texto_exibido, True, (0,0,0))
        window.blit(letras_text, (400,200))


        window.blit(teclado_img, (50,450))
        #print(mouse_x,mouse_y)
        #print(vidas)
        
        tema = fonte.render(f"O tema e {tema_escolhido}", True, (255,255,0))
        window.blit(tema, (50,400))

        contador = fonte.render(f"Vidas: {vidas}", True, (255,0,0))
        window.blit(contador, (50,10))

        mensagem_chute = chique_pequena.render(f"use o modo chute com espaco, escreva sua resposta no terminal", True, (255,255,255))
        window.blit(mensagem_chute, (780,10))

        if vidas>5:
                window.blit(coracao, (170,145))

        if vidas>4:
            window.blit(coracao, (90,145))

        if vidas>3:
            window.blit(coracao, (10,145))
        
        if vidas > 2:
            window.blit(coracao, (170,70))

        if vidas > 1:
            window.blit(coracao, (90,70))
        
        if vidas >0:
            window.blit(coracao, (10,70))
        

    


        if "_" not in letras_acertadas and timer == 0:
            vitoria.play()
            timer = 180
        
        if timer > 0:
            vit_texto = fonte.render("Parabens, voce venceu!", True, (0,255,0))
            restart_texto = fonte.render("Agora o jogo ira reiniciar", True, (0,0,0))
            window.blit(vit_texto, (420,100))
            window.blit(restart_texto, (400,300))
            timer -= 1
        
        if timer == 1:
            reiniciar_jogo()
        
        if vidas == 0 and timer_derrota == 0:
            derrota.play()
            timer_derrota = 180

        if timer_derrota > 0:
            perdeu_texto = fonte.render("Voce perdeu, tente novamente!", True, (255,0,0))
            palavra_secreta = fonte.render(f"A palavra era: {palavra_escolhida}", True, (255,255,255))
            restart_texto = fonte.render("Agora o jogo ira reiniciar", True, (0,0,0))
            window.blit(palavra_secreta, (400,150))
            window.blit(perdeu_texto, (370,100))
            window.blit(restart_texto, (400,300))
            timer_derrota -= 1
        
        if timer_derrota == 1:
            reiniciar_jogo()

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
        window.blit(fonte.render("Pedra, Papel, Tesoura", True, (0,0,0)), (490, 415))
    



    if tela_atual == "matue":
        dt = clock.get_time()/1000
        keys = key.get_pressed()

        mouse_x, mouse_y = mouse.get_pos()



        #teclas

        if modo_mouse == True:
            raio_x = (mouse_x)


        #if modo_mouse == False:
        if raio_x<1150:
            if keys[K_d]:
                    raio_x = raio_x + 100 *dt
        if raio_x > 120:
            if keys[K_a]:
                    raio_x = raio_x - 100 *dt
        if raio_x <1150:
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    raio_x = raio_x + 100 *dt
        if raio_x > 120:
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 3:
                    raio_x = raio_x - 100 *dt
        
        



        #desenhar a partir daqui

        window.fill(background_color)

        if modo_mouse == False:
            draw.line(window, (255, 242, 81), (raio_x-60,130), (raio_x-120,130), 10)
            draw.line(window, (255, 242, 81), (raio_x+60 ,130), (raio_x+120,130), 10)
            draw.line(window, (255, 242, 81), (raio_x,190), (raio_x,250), 10)
            draw.line(window, (255, 242, 81), (raio_x,70), (raio_x,10), 10)
            draw.circle(window, (255, 242, 81), (raio_x,130), 60)    
        draw.rect(window, (101, 67, 33), (1000, 240, 80, 400))
        draw.circle(window, (0, 128, 0), (1040,300), 100)
        draw.rect(window, (72, 157, 37), (0,600,1280,220))
        draw.rect(window, (100, 100, 100), (350, 360,200,240))
        draw.polygon(window, (242, 136, 59), ((350,360),(550,360),(450,200)))
        draw.rect(window, (13, 22, 100), (370, 460,50,70))
        draw.rect(window, (121, 77, 27), (450, 430,75,170))
        draw.circle(window, (0,0,0), (470,520), 7)

        if modo_mouse == True:
            draw.line(window, (255, 242, 81), (mouse_x-60,mouse_y), (mouse_x-120,mouse_y), 10)
            draw.line(window, (255, 242, 81), (mouse_x+60 ,mouse_y), (mouse_x+120,mouse_y), 10)
            draw.line(window, (255, 242, 81), (mouse_x,mouse_y+60), (mouse_x,mouse_y+120), 10)
            draw.line(window, (255, 242, 81), (mouse_x,mouse_y-60), (mouse_x,mouse_y-120), 10)
            draw.circle(window, (255, 242, 81), (mouse_x,mouse_y), 60)    

        #nuvem
        nuvem_x += velocidade_nuvem
        
        if nuvem_x <= 60 or nuvem_x >= 920:
            velocidade_nuvem = -velocidade_nuvem

        #if nuvem_x > 1350:
        #    nuvem_x = -350

        draw.circle(window, (255,255,255), (nuvem_x,nuvem_y),(70))
        draw.circle(window, (255,255,255), (nuvem_x+100,nuvem_y),(70))
        draw.circle(window, (255,255,255), (nuvem_x+200,nuvem_y),(70))
        draw.circle(window, (255,255,255), (nuvem_x+300,nuvem_y),(70))


        #desenhar imagem
        window.blit(matue_img, (600,450))

        #desenhar texto
        batman_text = batman_font.render("As vezes eu fumo um baseado", True, (0,0,0))
        window.blit(batman_text, (570,400))

    if tela_atual == "pedra":
        texto_base = chique.render(f"escolha:", True, (255,255,255))
        window.blit(texto_base, (600,100))

        pontos = chique_pequena.render(f"Pontos: {soma}", True, (255,255,255))
        window.blit(pontos, (50,100))

        pontos_ia = chique_pequena.render(f"Pontos ia: {soma_adv}", True, (255,255,255))
        window.blit(pontos_ia, (50,200))

        draw.rect(window, (120, 120, 120), (100, 300,350,300))
        draw.rect(window, (120, 120, 120), (500, 300,350,300))
        draw.rect(window, (120, 120, 120), (900, 300,350,300))

        draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
        draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
        draw.rect(window, (0, 0, 0), (900, 300,350,300),5)

        

        #print(timer)
        #print(mouse_x, mouse_y)

        if adversario == "pedra":
            ia_pedra(escolha)
        
        if adversario == "papel":
            ia_papel(escolha)
        
        if adversario == "tesoura":
            ia_tesoura(escolha)

        window.blit(pedra, (130,300))
        window.blit(papel, (530,300))
        window.blit(tesoura, (930,350))

    if tela_atual != "login":
        draw.rect(window, (120, 120, 120), (1150, 600, 120, 100))
        draw.rect(window, (0, 0, 0), (1150, 600, 120, 100),5)
        window.blit(fonte.render("voltar:", True, (0,0,0)), (1160, 630))
    
    if tela_atual != "login":
        if ev.type == MOUSEBUTTONDOWN:
            if 1160<=mouse_x<1280 and 600<=mouse_y<=700:
                if ev.button == 1:
                   email = ""
                   email_final = ""
                   senha_teclado = ""
                   senha_final = ""
                   estado_email = ""
                   estado_senha = ""
                   tela_atual = "login"

    display.update()