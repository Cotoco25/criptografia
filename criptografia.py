from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

running = True
clock=time.Clock()
background_color = (112, 128, 144)



fonte = font.Font("Worldstar.ttf", 40)


email = ""
vidas = 1
email_final = ""
modo = ""

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

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_q and modo == 1:
                email += "q"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_w:
                email += "w"
        
        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_e:
                email += "e"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_r:
                email += "r"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_t:
                email += "t"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_y:
                email += "y"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_u:
                email += "u"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_i:
                email += "i"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_o:
                email += "o"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_p:
                email += "p"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_a:
                email += "a"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_s:
                email += "s"
                
        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_d:
                email += "d"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_f:
                email += "f"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_g:
                email += "g"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_h:
                email += "h"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_j:
                email += "j"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_k:
                email += "k"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_l:
                email += "l"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_z:
                email += "z"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_x:
                email += "x"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_c:
                email += "c"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_v:
                email += "v"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_b:
                email += "b"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_n:
                email += "n"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_m:
                email += "m"

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_BACKSPACE:
                email = email[:-1]

        if ev.type == KEYDOWN and vidas > 0:
            key_pressed = ev.key
            if key_pressed == K_RETURN:
                email_final = email

        if ev.type == MOUSEBUTTONDOWN and vidas > 0:
            if 50<=mouse_x<=150 and 20<=mouse_y<=90:
                if ev.button == 1:
                    modo = 1


    draw.rect(window, (120, 120, 120), (50, 20, 100, 70))
    draw.rect(window, (0, 0, 0), (50, 20, 100, 70),5)

    window.blit(fonte.render("Email", True, (0,0,0)), (60, 40))
    window.blit(fonte.render(f"{email}", True, (0,0,0)), (130, 80))
    window.blit(fonte.render(f"{email_final}", True, (0,0,0)), (130, 180))

    display.update()