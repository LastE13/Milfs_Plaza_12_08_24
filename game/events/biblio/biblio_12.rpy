init:
    image GG Flow Embarrassment = Composite((807, 1080),
        (0, 0),  "GG Flow",
        (290, 298),  'GG Emo_Embarrassment',
        )
    image fell 0 = "images/cg/biblio/fell/0.png"
    image fell 1 = "images/cg/biblio/fell/1.png"
    image fell 2 = "images/cg/biblio/fell/2.png"
    image cg fell_background = "images/cg/biblio/fell/background.png"
    image fell animation_1:
        "cg/biblio/fell/animation_fell/1.png"
        pause .2
        "cg/biblio/fell/animation_fell/2.png"
        pause .2
        "cg/biblio/fell/animation_fell/3.png"
        pause .2
        "cg/biblio/fell/animation_fell/4.png"
        pause .2
        "cg/biblio/fell/animation_fell/5.png"
        pause .2
        "cg/biblio/fell/animation_fell/6.png"
        pause .2
        "cg/biblio/fell/animation_fell/7.png"
        pause .2
        "cg/biblio/fell/animation_fell/8.png"
        pause .2
        "cg/biblio/fell/animation_fell/9.png"
        pause .2
        repeat
    image fell animation_2:
        "cg/biblio/fell/animation_fell/1.png"
        pause .11
        "cg/biblio/fell/animation_fell/2.png"
        pause .11
        "cg/biblio/fell/animation_fell/3.png"
        pause .11
        "cg/biblio/fell/animation_fell/4.png"
        pause .11
        "cg/biblio/fell/animation_fell/5.png"
        pause .11
        "cg/biblio/fell/animation_fell/6.png"
        pause .11
        "cg/biblio/fell/animation_fell/7.png"
        pause .11
        "cg/biblio/fell/animation_fell/8.png"
        pause .11
        "cg/biblio/fell/animation_fell/9.png"
        pause .11
        repeat
    image fell animation_3:
        "cg/biblio/fell/animation_fell/1.png"
        pause .06
        "cg/biblio/fell/animation_fell/2.png"
        pause .06
        "cg/biblio/fell/animation_fell/3.png"
        pause .06
        "cg/biblio/fell/animation_fell/4.png"
        pause .06
        "cg/biblio/fell/animation_fell/5.png"
        pause .06
        "cg/biblio/fell/animation_fell/6.png"
        pause .06
        "cg/biblio/fell/animation_fell/7.png"
        pause .06
        "cg/biblio/fell/animation_fell/8.png"
        pause .06
        "cg/biblio/fell/animation_fell/9.png"
        pause .06
        repeat


label biblio_12:
    # Description: Подарить цветы Нэнси.
    # Task: Активировать Нэнси в библиотеке
    

    call show_bg_image_label from _call_show_bg_image_label_274
    show GG Think
    show GG Think:
        xalign .15
    #show BiblioGirl Normal
    #show BiblioGirl Normal:
        #xalign .85
    with my_dissolve
    
    
    # //В прихожей библиотеке Нэнси не окажется #TODO и как её убрать на экране до этого?????
    
    "[gg]" "Ух ты... И где она?"
    "[gg]" "Ладно, подожду."
    "[gg]" "....."
    "[gg]" "Хм..."
    "[gg]" "Быть может, она вообще сегодня не работает?.."
    "[gg]" "Пожалуй, посмотрю в читальном зале."

    show GG Normal:
        ease 1 xalign 1.5
    pause 1
    scene bookshelves bg with my_dissolve
    show GG Normal:
        xalign -.5
        ease 1 xalign .5
    pause 1
    
    # //GG_Normal движется вправо
    # //Читальный зал
    # //GG_Normal въезжает в зал слева
    
    show GG Smile with my_dissolve
    "[gg]" "Нэнси!!!"

    show GG Normal with my_dissolve
    show BiblioGirl Normal
    show BiblioGirl Books:
        xalign 1.5
        linear .5 xalign .5
    pause .5
    with vpunch
    pause .3
    scene fell 0
        

    # //BiblioGirl_Books с книгами в руках быстро едет на ГГ
    
    "Нэнси" "Не шумите, пожалу..."
    
    # //BiblioGirl_Books сталкивается с ГГ
    # //встряска экрана КОНЕЧНО ЖЕ
    # //Biblio_Upala_1
    
    "[gg]" "Чёрт!"
    "[gg]" "Извини..."
    "[gg]" "Нэнси, ты в порядке?"
    "[gg]" "Могу я попросить тебя подняться?"    
    scene cg fell_background
    show fell 1
    with my_dissolve 
    "[gg]" "Уфф... Кажется, она в отключке."
    "[gg]" "Да, ударчик был приличный."
    "[gg]" "Надеюсь, у неё нет никакого сотрясения."
    show fell 2 with my_dissolve
    "[gg]" "Судя по тому, с каким усилием она упирается в меня грудями, всякий раз набирая воздух в лёгкие – она жива."
    "[gg]" "...."
    "[gg]" "Что ж, раз она без сознания, мне самому придётся высвободиться."
    
    with my_dissolve
    # //Biblio_Upala_2anim
    # //x1
    show fell animation_1 with my_dissolve
    "[gg]" "{i}Ну же, подымайся...{/i}"
    "[gg]" "{i}Ещё немного усилий.{/i}"
    "[gg]" "{i}Я прилагаю все силы, но красота Нэнси выражается не только в её обаянии, но и в большом весе.{/i}"
    
    "[gg]" "{i}А ещё, кажется, я немного возбудился, пока тёрся об её тело в попытках вырваться.{/i}"
    "[gg]" "{i}Я уже понимаю, что все мои усилия тщетны, но не могу прекратить «пытаться»...{/i}"
    "[gg]" "{i}Каждое движение будоражит моё сознание.{/i}"
    "[gg]" "{i}Если она сейчас же не очнётся, я просто на просто кончу себе в штаны.{/i}"
    
    "[gg]" "Нэнси!"
    "[gg]" "Про... Просыпайся!"
    "[gg]" "Ну же, очнись!!!"
    "Нэнси" "[gg]?.."
    
    # //x2
    show fell animation_2 with my_dissolve
    "[gg]" "О, Нэнси! Как хорошо, что ты пришла в себя."
    "[gg]" "Я пытаюсь приподняться, но..."
    "Нэнси" "Хи-хи-хи!"
    "Нэнси" "Я это вижу. И даже чувствую."
    "[gg]" "...."
    "Нэнси" "Ты всё ещё подо мной потому что слишком слаб, или потому я сильно много вешу?"
    "[gg]" "Хех..."
    "[gg]" "Потому что... Я делаю неверные движения. Наверное."
    "Нэнси" "Но продолжаешь пытаться, верно?.."
    "[gg]" "Верно. Никак не могу успокоиться. Наверное, это уже рефлекс..."
    "Нэнси" "Что ж.. Я никуда не тороплюсь."
    "Нэнси" "Хочу, чтобы у тебя всё получилось, как надо."
    
    # //x3
    show fell animation_3 with my_dissolve
    "[gg]" "Уффф... Получается. Ещё как получается"
    "[gg]" "Ещё совсем не много, и я... и мы..."
    "Нэнси" "Встанем?"
    "[gg]" "Даааа!"
    "[gg]" "Вставлю! Ой.."
    "[gg]" "То есть, встанем!"
    "Нэнси" "Ох... [gg], ты явно делаешь успехи."
    "Нэнси" "Я практически приподнялась."
    "[gg]" "О даа.... Совсем-совсем, я уже на самой грани..."
    "[gg]" "Даааааааа!!!!"
    
    # //Biblio_Upala_End
    
    "Нэнси" "Хи-хи-хи."
    "Нэнси" "Ты совсем истощился."
    "[gg]" "Абсолютно..."
    "Нэнси" "Хорошо, я помогу нам обоим."
    
    scene bookshelves bg
    
    # //Читальный зал
    show GG Flow Embarrassment
    show GG Flow Embarrassment:
        xalign .15
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    "[gg]" "Это тебе, Нэнси..."
    $ remove_from_inventory(name = 'Букет ландышей')
    show GG Embarrassment with my_dissolve
    #show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Божечки, как это мило!"
    
    "Нэнси" "Ты настоящий джентельмен."
    
    
    "[gg]" "Стараюсь..."
    show GG Embarrassment with my_dissolve
    show BiblioGirl Smile with my_dissolve
    "Нэнси" "Кстати, мы наконец-то перешли на «ты». Хи-хи-хи."
    "[gg]" "Это ведь хорошо, правда?"
    show BiblioGirl Passion with my_dissolve
    "Нэнси" "Ага. Мы теперь достаточно близко знакомы, чтобы считаться друзьями."
    
    show GG Embarrassmen with my_dissolve
    "[gg]" "{i}Надеюсь, она не имеет в виду «фрэндзону»...{/i}"
    
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Извини, что не могу с тобой сейчас поболтать."
    show BiblioGirl Chagrin with my_dissolve
    "Нэнси" "Последнее время у меня много работы и совсем нет возможностей отдыхать."
    show GG Smile with my_dissolve
    "[gg]" "Тогда ты будешь не против, если я как-то заскочу к тебе и помогу?"
    show BiblioGirl Smile with my_dissolve
    "Нэнси" "О! Я буду исключительно рада."
    "Нэнси" "Сегодня я уж справлюсь сама, но в любой другой день тут всегда есть чем заняться."
    $ locations.update({
        'City_Library':
            Location(
                'City_Library',
                buttons       = [],
                image_buttons = {
                    'biblio_girl':Jump("christie_root_21_pre_menu")
                    }
                )}

    )
    "[gg]" "Замётано!"
    $ remove_from_inventory(name = 'Книга «Анжелика и Король»')
    $ events_pop("biblio_12", 0)
    $ Event("biblio_13", location = "City_Library_BiblioGirl", day_start=time.day_now+1, time=["morning", "afternoon"], button_name="Поздороваться") #TODO !!!!!!!!!!!!!
    $ descript_BiblioGirl = _("Навестить Нэнси в любой рабочий день в библиотеке.")

    $ check_event_in_allowed_events("biblio_13")

    
    jump main_interface_label

