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
lugar = ""
email = ""
email_final = ""
modo = ""

senha_teclado = ""

criptografia_teclado = ""



def teclado(mododo, lugar):
    if ev.type == KEYDOWN and modo == mododo:
        if event.unicode:
            lugar += str(event.unicode)
    
    return lugar

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

        if ev.type == KEYDOWN:
            if ev.unicode:
                lugar += ev.unicode


        if modo == 1:
            if ev.type == KEYDOWN:
                if ev.unicode:
                    email += ev.unicode

        if ev.type == KEYDOWN and modo == 1:
            key_pressed = ev.key
            if key_pressed == K_RETURN:
                email_final = email

        if modo == 2:
            if ev.type == KEYDOWN:
                if ev.unicode:
                    senha_teclado += ev.unicode
        
        if modo == 3:
            if ev.type == KEYDOWN:
                if ev.unicode:
                    criptografia_teclado += ev.unicode

        if valida_email(email_final):
            estado_email = "valido"
        
        if estado_email == "valido":
            window.blit(fonte.render("parabens email valido", True, (0,0,0)), (100, 500))

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
                    modo = 3



    draw.rect(window, (120, 120, 120), (50, 20, 100, 70))
    draw.rect(window, (0, 0, 0), (50, 20, 100, 70),5)

    draw.rect(window, (120, 120, 120), (200, 20, 100, 70))
    draw.rect(window, (0, 0, 0), (200, 20, 100, 70),5)

    draw.rect(window, (120, 120, 120), (350, 20, 175, 70))
    draw.rect(window, (0, 0, 0), (350, 20, 175, 70),5)

    window.blit(fonte.render("Email:", True, (0,0,0)), (50, 130))
    draw.rect(window, (255, 255, 255), (50, 170, 800, 60))
    draw.rect(window, (0, 0, 0), (50, 170, 800, 60),5)

    window.blit(fonte.render("Senha:", True, (0,0,0)), (50, 250))
    draw.rect(window, (255, 255, 255), (50, 290, 800, 60))
    draw.rect(window, (0, 0, 0), (50, 290, 800, 60),5)

    window.blit(fonte.render("Senha Criptografia:", True, (0,0,0)), (50, 380))
    draw.rect(window, (255, 255, 255), (50, 420, 800, 60))
    draw.rect(window, (0, 0, 0), (50, 420, 800, 60),5)

    window.blit(fonte.render("Email", True, (0,0,0)), (60, 40))
    window.blit(fonte.render("Senha", True, (0,0,0)), (210, 40))
    window.blit(fonte.render("Criptografia", True, (0,0,0)), (360, 40))

    if modo == 1:
        window.blit(fonte.render("modo email", True, (0,0,0)), (1000, 40))
    
    if modo == 2:
        window.blit(fonte.render("modo senha", True, (0,0,0)), (1000, 40))
    
    if modo == 3:
        window.blit(fonte.render("modo criptografia", True, (0,0,0)), (1000, 40))
    
    window.blit(fonte.render(f"{senha_teclado}", True, (0,0,0)), (60, 300))
    window.blit(fonte.render(f"{criptografia_teclado}", True, (0,0,0)), (60, 430))

    window.blit(fonte.render(f"{email}", True, (0,0,0)), (60, 180))
    window.blit(fonte.render(f"{email_final}", True, (0,0,0)), (100, 500))

    display.update()