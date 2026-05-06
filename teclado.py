def teclado(mododo, lugar):
    global email_final, modo, email, senha_teclado, criptografia_teclado
    if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_q and modo == mododo:
                lugar += "q"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_w:
                lugar += "w"
        
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_e:
                lugar += "e"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_r:
                lugar += "r"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_t:
                lugar += "t"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_y:
                lugar += "y"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_u:
                lugar += "u"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_i:
                lugar += "i"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_o:
                lugar += "o"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_p:
                lugar += "p"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_a:
                lugar += "a"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_s:
                lugar += "s"
                
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_d:
                lugar += "d"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_f:
                lugar += "f"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_g:
                lugar += "g"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_h:
                lugar += "h"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_j:
                lugar += "j"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_k:
                lugar += "k"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_l:
                lugar += "l"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_z:
                lugar += "z"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_x:
                lugar += "x"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_c:
                lugar += "c"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_v:
                lugar += "v"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_b:
                lugar += "b"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_n:
                lugar += "n"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_m:
                lugar += "m"
    
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_1:
                lugar += "1"
    
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_2:
                lugar += "2"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_3:
                lugar += "3"
    
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_4:
                lugar += "4"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_5:
                lugar += "5"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_6:
                lugar += "6"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_7:
                lugar += "7"
    
    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_8:
                lugar += "8"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_9:
                lugar += "9"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_0:
                lugar += "0"


    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_COLON:
                lugar += ":"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_AT:
                lugar += "@"

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_BACKSPACE:
                lugar = lugar[:-1]

    if ev.type == KEYDOWN and modo == mododo:
            key_pressed = ev.key
            if key_pressed == K_RETURN:
                email_final = lugar
    
    return lugar