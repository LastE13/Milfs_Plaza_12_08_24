init 50 python:
    import os
    import copy
    #renpy.random.choice(seq)
    letters_list = []
    letters_combinations = []
    letters_combinations_full = []
    idle_hover_color = []
    letters_complete = []
    second_decoder = 120
    test_time = 0 # renpy.input("Ввидите желаемое время для раунда в секундах")
    for file in renpy.list_files():
        if ("1112111" in file) and file.endswith((".jpg", ".png")):
            file_name = os.path.splitext(os.path.basename(file))[0]
            name_l = "letter_" + file_name
            letters_list.append(file)
            renpy.image(name_l, file)
    '''
    Идёт провкерка какой раунд, если раунд 1 или 2, то из списка берётся 3-4 случайные буквы и записываются как искомые (для 2го раунда таких 2), если раунд больше то от 2 до 4 букв. Максимум раундов - 6.
    Комбинации не должны повторятся и должны быть на растоянни друг от друга. Так же надо набрать около 30 (включая искомые) разных комбинаций
    '''
    def desired_combinations(r = False):
        global letters_list, letters_combinations, idle_hover_color, letters_complete
        letters_combinations = []
        letters_combinations_full = []
        idle_hover_color = []
        letters_complete = []
        print("____________________")
        print("letters_complete")
        print(letters_complete)
        print(letters_combinations)
        run = renpy.random.randint(4, 6)
        for i in range(run):
            letters_combinations.append([])
            letters_combinations[-1].append(renpy.random.choice(letters_list))
            letters_combinations[-1].append(renpy.random.choice(letters_list))
            idle_hover_color.append(False)
        print(letters_complete)
        print(letters_combinations)
        combinations_full()


    def combinations_full():
        global letters_list, letters_combinations, letters_combinations_full, idle_hover_color
        letters_combinations_full = letters_combinations.copy()
        while len(letters_combinations_full) < 36:
            letters_combinations_full.append([])
            letters_combinations_full[-1].append(renpy.random.choice(letters_list))
            letters_combinations_full[-1].append(renpy.random.choice(letters_list))
            idle_hover_color.append(False)
        renpy.random.shuffle(letters_combinations_full)

    def SetName(name, index, value):
        name[index] = value
    def add_mass(mass, value):
        mass.append(value)
screen decoder_game(win, lose, seconds = 120):
    modal True
    default timer_sec = seconds
    default complete_let = 0
    add "images/mini_games/decoder/Game_bg.png"
    viewport:
        xmaximum 1430
        ymaximum 670
        add '#0000'
        xalign .63 
        yalign 0.99
        grid 6 6:
            xalign .5
            yalign 0.5
            yspacing 2
            xspacing 12
            for imgs in range(len(letters_combinations_full)):
                hbox:
                    spacing 0
                    for img in letters_combinations_full[imgs]:
                        imagebutton:
                            if idle_hover_color[imgs] or letters_combinations_full[imgs] in letters_complete:
                                idle im.MatrixColor(img, im.matrix.colorize("#1e1e1c", "#dad78c"))
                            else:
                                idle img
                            hover im.MatrixColor(img, im.matrix.colorize("#1e1e1c", "#dad78c"))
                            focus_mask True
                            hovered Function(SetName, idle_hover_color, imgs, True)
                            unhovered Function(SetName, idle_hover_color, imgs, False)
                            at transform:
                                zoom .62
                            if letters_combinations_full[imgs] not in letters_complete:
                                if letters_combinations_full[imgs] in letters_combinations:
                                    action SetScreenVariable("complete_let", complete_let + 1), Function(add_mass, letters_complete, letters_combinations_full[imgs])
                                else:
                                    action Function(add_mass, letters_complete, letters_combinations_full[imgs])
                        
                            #add img:
                                #zoom .62
                            
            if len(letters_combinations_full) < 6:
                for i in range(6-len(letters_combinations_full)):
                    add letters_list[0]:
                        zoom .01
                        alpha 0
    viewport:
        xmaximum 1060
        ymaximum 300
        add '#0000'
        xalign 0.5
        yalign 0.08
        
        grid 3 2:
            transpose True
            xalign .5
            yalign .49
            if len(letters_combinations) >= 6:
                xspacing 12
            else:
                xspacing 20

            yspacing 16
            for imgs in range(len(letters_combinations)):
                hbox:
                    if imgs > 2:
                        if len(letters_combinations) == 6:
                            xoffset 80
                        else:
                            xoffset 100

                    spacing 0
                    for img in letters_combinations[imgs]:
                        add img:
                            zoom .83
            if len(letters_combinations) == 5:
                add letters_list[0]:
                    zoom .01
                    alpha 0
    if second_decoder > 0:
        timer 1 repeat True action SetVariable("second_decoder", second_decoder - 1)
    timer timer_sec action Hide("decoder_game"), Jump(lose)
    viewport:
        xmaximum 200
        ymaximum 200
        add '#0000'
        xpos 100 
        ypos 104
        text str(second_decoder) xalign .5 yalign .5 size 120
    viewport:
        xmaximum 200
        ymaximum 200
        add '#0000'
        xpos 1630
        ypos 104
        text "%s/%s" %(complete_let, len(letters_combinations)) xalign .5 yalign .5 size 120
    for i in letters_complete:
        if i not in letters_combinations:
            timer .1 action Hide("decoder_game"), Jump(lose)
        if letters_complete != [] and sorted(letters_complete) == sorted(letters_combinations) and len(letters_combinations) > 1:
            timer .1 action Hide("decoder_game"), Jump(win)

    add "images/mini_games/decoder/Game_fg.png"
label testing_mgd:
    $ test_time = int(renpy.input("Ввидите желаемое время для раунда в секундах"))
    if test_time != 0:
        $ second_decoder = test_time
    else:
        $ second_decoder = 120
    jump round_1
    return
label round_1:
    $ desired_combinations()
    $ second_decoder = 120
    $ letters_complete = []
    show screen decoder_game("biblio_5.win", "lose_game_decoder", seconds = second_decoder)
    pause
    return
label round_2:
    $ desired_combinations()
    $ second_decoder = 120
    show screen decoder_game("biblio_8.win", "lose_game_decoder", seconds = second_decoder)
    pause
    return

label lose_game_decoder:
    "[gg]" "Понятия не имею, что за каракули здесь написаны."    
    $ location_now = 'GG_Room'
    jump main_interface_label

