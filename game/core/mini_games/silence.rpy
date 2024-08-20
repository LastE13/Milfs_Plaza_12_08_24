init python:
    silence_now = 0
    silence_max = 1000
    noise_people = False
    noise_pos = (0, 0)
    noise_control = False
    pos_runner = (534, 666)
    pos_thumb = (560, 478)
    xxx = 0
    direction_runner = "right"
    silence_time = 60
    list_noise_pos = [(20, 280),
            (380, 300),
            (1060, 218),
            (1250, 280),
            (525, 260),
            (640, 237)]
    def add_noise_people():
        global noise_people, list_noise_pos, noise_pos
        if noise_people or noise_control:
            return
        run = renpy.random.randint(0, 10)
        if run > 7:
            noise_people = True
            noise_pos = renpy.random.choice(list_noise_pos)
            print(noise_pos)
    def start_noise_control():
        global noise_people, noise_pos, noise_control, pos_runner, pos_thumb, xxx
        xx = renpy.random.randint(560, 682)#1308)
        pos_runner = (534, 666)
        xxx = 0
        #pos_runner = (xx+40, 666) # (550, 666), (1378, 666) 21 (45)
        pos_thumb = (xx, 478) #(560, 478), (1308, 478)
        noise_people = False
        noise_control = True
        noise_pos = (0, 0)

    def plus_minus_xx():
        global xxx, direction_runner

        if direction_runner == "right":
            if xxx + 550 < 682 +70:
                xxx += 3
            else:
                direction_runner = "left"
        if direction_runner == "left":
            if xxx + 550 > 534:
                xxx -= 3
            else:
                direction_runner = "right"

init:
    image left_bar_silence = "mini_games/silence/left_bar.png"
    image right_bar_silence = "mini_games/silence/right_bar.png"                 
    image bad_finish = "mini_games/silence/bad.png"
    image silence_button = "mini_games/silence/button.png"
    image finish_thumb = "mini_games/silence/finish.png"
    image good_finish = "mini_games/silence/good.png"
    image runner = "mini_games/silence/runner.png"
    image track = "mini_games/silence/track.png"
    image track_mini = "mini_games/silence/track_mini.png"
    

screen silence_mini_game(lose = "lose_001", win = "win_001"):
    modal True
    text "{size=76}[silence_time]" xalign .5 yalign .1
    if noise_people:
        imagebutton:
            idle "silence_button"
            hover im.MatrixColor("mini_games/silence/button.png", im.matrix.brightness(.3))
            pos noise_pos
            action Function(start_noise_control)

        timer .01 repeat True action SetVariable("silence_now", silence_now+1)

    if noise_control:
        #add "track"
        add "track_mini" xoffset 200
        add "runner" pos pos_runner xoffset xxx+200
        add "finish_thumb" pos pos_thumb xoffset 200
        timer .01 repeat True action Function(plus_minus_xx)
        button:
            background None
            xsize 1920
            ysize 1080
            if pos_thumb[0] + 32 <= xxx + 550 and xxx + 550 <= pos_thumb[0] + 106:
                action SetVariable("silence_now", silence_now - (silence_now//3*2-10)), SetVariable("noise_control", False)
            else:
                action SetVariable("noise_control", False)
        timer .01 repeat True action SetVariable("silence_now", silence_now+1)
    bar:
        range silence_max 
        value silence_now 
        xmaximum 1070
        xminimum 1070
        ymaximum 243
        yminimum 243 
        xalign .495
        yalign 1.01
        left_bar "right_bar_silence" 
        right_bar "left_bar_silence"
    
    # text "{size=66}{b}|" xpos pos_thumb[0] + 32 ypos 654 xoffset 200
    # text "{size=66}{b}|" xpos pos_thumb[0] + 106 ypos 654 xoffset 200

    # textbutton "{color=#000}{size=66}[testing_run]"  xalign .25 yalign .75
    # textbutton "{color=#000}{size=66}[silence_now]"  xalign .5 yalign .75
    # textbutton "{color=#000}{size=66}[direction_runner]|%s" %(str(xxx + pos_thumb[0]))  xalign .62 yalign .75
    # hbox:
    #     xalign .5
    #     yalign .5
    #     spacing 50
    #     textbutton "{size=66}+" action SetVariable("silence_now", silence_now+1)
    #     textbutton "{size=66}++" action SetVariable("silence_now", silence_now+10)
    #     textbutton "{size=66}-" action SetVariable("silence_now", silence_now-1)
    #     textbutton "{size=66}--" action SetVariable("silence_now", silence_now-10)
    
    # textbutton "{size=66}++" xalign .4 yalign .75 action SetVariable("xxx", xxx+10)
    timer .1 repeat True action If(silence_now < 6, SetVariable("silence_now", 6))
    timer 1.0 repeat True action Function(add_noise_people)
    timer 1 repeat True action If(silence_time > 0, SetVariable("silence_time", silence_time - 1))
    textbutton "{size=66}X" xalign .95 yalign .05 action Hide("silence_mini_game")
    if silence_now >= silence_max:
        timer .01 action Jump(lose)
        #$ renpy.jump(lose)
    if silence_time == 0:
        timer .01 action Jump(win)
        #$ renpy.jump(win)

label win_001:
    hide screen silence_mini_game
    "win wn"
    return
label lose_001:
    hide screen silence_mini_game
    "lose ls"
    return