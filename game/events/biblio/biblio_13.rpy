init:
    image ico_book = LiveComposite((1920, 1080),
        (380, 300),"mini_games/biblio/books_search/frame.png",
        (380, 300),"mini_games/biblio/books_search/11.png",)
    image ico_book_2 = LiveComposite((1920, 1080),
        (1070, 260),"mini_games/biblio/books_search/frame.png",
        (1070, 260),"mini_games/biblio/books_search/11.png",)
    image ico_book_3 = LiveComposite((1920, 1080),
        (1070, 260), im.MatrixColor("mini_games/biblio/books_search/frame.png", im.matrix.brightness(.3)),
        (1070, 260),im.MatrixColor("mini_games/biblio/books_search/11.png", im.matrix.brightness(.3)),)

    image Secret_Biblio_Tits = "cg/biblio/Secret_Biblio_Tits.png"
    
label biblio_13:
    # Description: Навестить Нэнси в любой рабочий день в библиотеке.
    # Task: Активировать Нэнси в библиотеке утром или днём.
    
    call show_bg_image_label from _call_show_bg_image_label_275
    show GG Normal
    show GG Normal:
        xalign .15
    # show BiblioGirl Smile
    # show BiblioGirl Smile:
    #     xalign .85
    show BiblioGirl Normal
    show BiblioGirl Normal:
        xalign .85
    with my_dissolve
    
    "[gg]" "Привет!"
    "Нэнси" "О, рада тебя видеть."
    "[gg]" "Я ж сказал, что приду, вот и пришёл."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Ты очень вовремя. Читальный зал переполнен, наплыв новичков."
    "Нэнси" "Они подыскивают себе подходящую литературу, и, если, смогу подобрать подходящее, станут завсегдатаями."
    show GG Skepticism with my_dissolve
    "[gg]" "Ратуешь за книголюбие?"
    "Нэнси" "Нет, просто от этого зависит моя зарплата."
    show GG Smile with my_dissolve
    "[gg]" "Я думал, ты идейная, хе-хе."
    # show BiblioGirl Skepticism with my_dissolve
    "Нэнси" "Знаешь ли..."
    "Нэнси" "Если я работаю в библиотеке, это ещё не значит, что я хочу, чтобы круглые сутки меня окружали макулатура и словоблудие мнимых интеллектуалов."
    show GG Laughs
    "[gg]" "Намёк понял – книги на праздники не дарить."
    # show BiblioGirl Laugh with my_dissolve
    "Нэнси" "Типа того."
    # show BiblioGirl Skepticism with my_dissolve
    "Нэнси" "И умного из себя не корчить."
    show GG Angry with my_dissolve
    "[gg]" "Эй!!!"
    # show BiblioGirl Laugh with my_dissolve
    "Нэнси" "Хи-хи-хи!!!"
    show GG Smile with my_dissolve
    # show BiblioGirl Surprise with my_dissolve
    "Нэнси" "Ой! Что-то мы сильно расшумелись."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Пошли, я объясняю, что надо делать."
    show GG Normal with my_dissolve
    "[gg]" "Пойдём."
    jump .start_mini_game
    label .start_mini_game_2:
        scene image "locations/bg/City_Library/afternoon.png"
        show GG Normal:
            xalign .15
        with my_dissolve
        "[gg]" "Привет!"
        show BiblioGirl Smile:
            xalign .85
        with my_dissolve
        "Нэнси" "О, рада тебя видеть."
        "[gg]" "Хочу снова попытаться помочь тебе с раздачей книг новым читателям."
        show BiblioGirl Passion with my_dissolve
        "Нэнси" "А ты настойчивый."
        show GG Skepticism:
            yalign 1.0
        with my_dissolve
        "[gg]" "Не люблю проигрывать."
        "Нэнси" "Тогда пошли."
    label .start_mini_game:
        $ biblio_search_book_time_line = .45
        $ store._ttdd_ll = [None, None, None]
        $ win_label_for_searh_book_game = "biblio_13.win"
        $ win_2_label_for_searh_book_game = "biblio_13.win_2"
        $ lose_label_for_searh_book_game = "biblio_13.lose"
        
    # //Оба спрайта движутся вправо
    # //Читальный зал
    # //Оба спрайта выезжает слева
    # //Читатели
    show GG Normal:
        ease 1 xalign 1.5
    show BiblioGirl Normal:
        ease 1 xalign 1.5
    with None
    scene readroom_people bg #TODO А читатели где?
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .15
    show BiblioGirl Normal:
        xalign -.5
        ease 1 xalign .85
    pause 1
    
    "Нэнси" "Только тссс..."
    "[gg]" "Понял-понял."
    "Нэнси" "Ребята погружены в чтение, но быстро теряют интерес и просят новую книгу."
    "Нэнси" "Твоя... То есть наша задача – запомнить, что именно они попросили, найти эту литературу в книжных стеллажах и принести им."
    "[gg]" "Звучит максимально просто."
    "Нэнси" "Да!"
    "Нэнси" "Только книг очень много и ты можешь не запомнить, или даже забыть какую книгу у тебя просили, в процессе поиска подходящей."
    "Нэнси" "Естественно, если ты ошибёшься, это скажется на настроение наших посетителей и они выберут другое заведение."
    "Нэнси" "Поэтому важно, чтобы ты как можно точнее подбирал нужное чтиво."
    "Нэнси" "Процент ошибок должен быть не больше 30\%, понимаешь?"
    "[gg]" "А если больше?"
    "Нэнси" "Придётся ждать новых посетителей и всё делать по новой."
    "[gg]" "Я справлюсь."
    # show BiblioGirl Smile with my_dissolve

    "Нэнси" "Спасибо, [gg]!"
    jump biblio_mini_games_test_start 
    
    # //Мини-игра «Дай книгу» #TODO Дальше идет мини-игра, её я не трогаю.
    # Фразы для мини игры:
    # //Когда высветились необходимые книги для поиска
    
    # "[gg]" "Пора действовать!"
    
    # //При выборе любой книги
    
    # "[gg]" "Взял!"
    
    # //Когда взял все книги
    
    # "[gg]" "Нужно скорее нести обратно!"
    # "Кнопка" "Отдать книги"
    
    # //Если читатель получает не ту книгу
    # //Текст имеет смысл сделать всплывающим над спрайтами персонажей
    # Это не та книга!
    # Ты ошибся!
    # Я это не просил!
    # //Если читатель получает ту книгу
    # Спасибо!
    # То, что нужно!
    # Подходящий выбор!
    # //Если проиграл
    # //Текст имеет смысл сделать всплывающим над спрайтами персонажей
    label .lose:
        scene readroom_people bg
        if len(pos_people) >2:
            call screen comic_frame(__("Мне здесь не нравится."), pos_people[0][0], pos_people[0][1]+150)
            call screen comic_frame(__("Я ухожу, это полный отстой."), pos_people[1][0], pos_people[1][1]+150)
            call screen comic_frame(__("Абсолютное разочарование."), pos_people[2][0], pos_people[2][1]+150)
        else:
            "Читатели" "Мне здесь не нравится."
            "Читатели" "Я ухожу, это полный отстой."
            "Читатели" "Абсолютное разочарование."
        show GG Chagrin:
            xalign .15
        with my_dissolve
        "[gg]" "Чёрт, не получилось..."
        show BiblioGirl Normal:
            xalign .85
        with my_dissolve
        "Нэнси" "[gg]..."
        show GG Chagrin with my_dissolve
        "[gg]" "Да, знаю, я тебя подвёл."
        "Нэнси" "Я всё равно благодарна тебе за попытку."
        "Нэнси" "Приходи ещё."
        menu:
            "Попытаться снова":
                jump .start_mini_game_2
            "В другой раз":
                $ time.time_now = "evening"    
                jump main_interface_label
    # //Надпись в конце
    # Попытаться снова (мини-игра повторяется)
    # В другой раз (текущий квест остаётся акивным), время суток становится вечернее. Выполнить текущее задание сегодня уже нельзя.
    # В другой раз начальный диалог чуточку меняется, чтоб не затягивать перед мини-игрой:
    
    # show GG Normal with my_dissolve
    # "[gg]" "Привет!"
    # show BiblioGirl Smile with my_dissolve
    # "Нэнси" "О, рада тебя видеть."
    # "[gg]" "Хочу снова попытаться помочь тебе с раздачей книг новым читателям."
    # show BiblioGirl Passion with my_dissolve
    # "Нэнси" "А ты настойчивый."
    # show GG Skepticism:
    #     yalign 1.0
    # with my_dissolve
    # "[gg]" "Не люблю проигрывать."
    # "Нэнси" "Тогда пошли."
    
    # Далее всё повторяется с момента:
    # //Оба спрайта движутся вправо
    # //Читальный зал
    # //Оба спрайта выезжает слева
    # //Читатели
    
    # show BiblioGirl Normal with my_dissolve
    # "Нэнси" "Только тссс..."
    label .win_2:
        scene readroom_people bg
        #call screen comic_frame(__("И в другой раз, просто прогоню тебя, если не прекратишь строить комедию. "), 700, 600)
        if len(pos_people) > 2:
            call screen comic_frame(__("Спасибо!"), pos_people[0][0], pos_people[0][1]+150)
            call screen comic_frame(__("То, что нужно!"), pos_people[1][0], pos_people[1][1]+150)
            call screen comic_frame(__("Это не та книга!"), pos_people[2][0], pos_people[2][1]+150)
        else:
            "Читатели" "Спасибо!"
            "Читатели" "То, что нужно!"
            "Читатели" "Это не та книга!"
        jump .win_1
    label .win:
        scene readroom_people bg
        if len(pos_people) > 2:
            call screen comic_frame(__("Спасибо!"), pos_people[0][0], pos_people[0][1]+150)
            call screen comic_frame(__("То, что нужно!"), pos_people[1][0], pos_people[1][1]+150)
            call screen comic_frame(__("Подходящий выбор!"), pos_people[2][0], pos_people[2][1]+150)
        else:
            "Читатели" "Спасибо!"
            "Читатели" "То, что нужно!"
            "Читатели" "Подходящий выбор!"
        
    label .win_1:
        # //Если победил в мини-игре
        # //Никакхи надписей победа не будет
        # //Один из читателей (словно мини-игра продолжается) просит какую-то книгу – не важно какую.
        show image "ico_book"
        # //Оказавшись среди полок главный герой комментирует
    
        "[gg]" "О, я точно видел эту книгу, когда искал другие."
        show GG Normal:
            ease 1 xalign 1.5
        with None
        scene bookshelves bg #TODO А читатели где?
        with my_dissolve #my_fade #TODO а куда my_fade делся?
        show GG Normal:
            xalign -.5
            ease 1 xalign .05
        pause 1
        # show image "mini_games/biblio/books_search/11.png":
        #     xpos 680
        #     ypos 510
        "[gg]" "Она где-то здесь, среди рядов вот тут..."
        
        call screen rtrn_screen(img = "ico_book_2", hvr = "ico_book_3")
        # //Появляется иконка (как в мини-игре, когда надо было выбрать подходящую книгу) в одном из мест книжной полки
        # //После клика героя
        show Secret_Biblio_Tits
        with my_dissolve
        "[gg]" "Упс!.."
        "[gg]" "Вот так неожиданность."
        "[gg]" "Стоило бы расстроиться из-за отсутствия книги, но учитывая, что я нашёл кое-что куда ценнее..."
        "[gg]" "Нэнси?"
        # show BiblioGirl Normal:
        #     xalign .85
        "Нэнси" "Ага."
        "Нэнси" "Решила тебя немножко порадовать."
        "Нэнси" "За успехи в твоём нелёгком деле."
        "[gg]" "С-спасибо..."
        "[gg]" "Неожиданно и ооо-о-о-очень приятно."
        "Нэнси" "Хи-хи-хи."
    
        # # //Читальный зал
        # # //GG_Normal выезжает справа
        # show GG Normal:
        #     ease 1 xalign -1.5
        # show BiblioGirl Normal:
        #     ease 1 xalign -1.5
        # with None
        scene readroom_people bg #TODO А читатели где?
        with my_dissolve #my_fade #TODO а куда my_fade делся?
        show GG Normal:
            xalign 1.5
            ease 1 xalign .15
        
        pause 1
        show GG Normal with my_dissolve
        "[gg]" "Что ж, мне пора уходить."
        
        # BiblioGirl_Normal выезжает справа
        show BiblioGirl Normal:
            xalign 1.5
            ease 1 xalign .85
        "Нэнси" "[gg], постой."
        "[gg]" "Да?"
        "Нэнси" "Приходи ещё, а?"
        show GG Smile with my_dissolve
        "[gg]" "Конечно. Обязательно."
        
        # //Time: Evening
        # //Хол библиотеки
        $ time.time_now = "evening"
        
        $ events_pop("biblio_13", 0)
        $ Event("biblio_14", location = "City_Library_BiblioGirl", day_start=time.day_now+1, time=["morning", "afternoon"], button_name="Помочь") #TODO !!!!!!!!!!!!!
        $ descript_BiblioGirl = _("Нэнси ждёт меня в библиотеке.")

        $ check_event_in_allowed_events("biblio_14")

        
    jump main_interface_label
