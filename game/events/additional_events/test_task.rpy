init:
    image readroom_people bg = 'mini_games/biblio/books_search/bg.png'
    image bookshelves bg =  "mini_games/biblio/books_search/bg_2.png"
    image library_bookshelves_bg = "cg/christie_root/library/bibliogirl/bg.png"
    image library_bookshelves_book = "cg/christie_root/library/bibliogirl/book.png"
    image library_bookshelves_bibliogirl_start = "cg/christie_root/library/bibliogirl/start.png"
    image library_bookshelves_bibliogirl_end = "cg/christie_root/library/bibliogirl/end.png"
    image library_bookshelves_smerm_anim_1:
        "cg/christie_root/library/bibliogirl/smerm/5.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/4.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/3.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/2.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/1.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/0.png"

    image library_bookshelves_smerm_anim_2:
        alpha 0.0
        pause .4
        alpha 1.0
        "cg/christie_root/library/bibliogirl/smerm/5.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/4.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/3.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/2.png"
        pause .15
        xoffset 48
        yoffset -13
        "cg/christie_root/library/bibliogirl/smerm/1.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/0.png"
    image library_bookshelves_smerm_anim_3:
        alpha 0.0
        xzoom -1
        xoffset 20
        pause 0.9
        alpha 1.0
        "cg/christie_root/library/bibliogirl/smerm/5.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/4.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/3.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/2.png"
        pause .15
        xoffset 89
        yoffset -19
        "cg/christie_root/library/bibliogirl/smerm/1.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/0.png"
    image library_bookshelves_smerm_anim_4:
        alpha 0.0
        xzoom -1
        xoffset 30
        pause 1.2
        alpha 1.0
        "cg/christie_root/library/bibliogirl/smerm/5.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/4.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/3.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/2.png"
        pause .15
        xoffset 107
        yoffset 9
        "cg/christie_root/library/bibliogirl/smerm/1.png"
        pause .15
        "cg/christie_root/library/bibliogirl/smerm/0.png"
    image library_bookshelves_smerm_anim = LiveComposite((1920, 1080),
    (0, 0), "library_bookshelves_smerm_anim_1",
    (0, 0), "library_bookshelves_smerm_anim_2",
    (0, 0), "library_bookshelves_smerm_anim_3",
    (0, 0), "library_bookshelves_smerm_anim_4",
    )
    image library_bookshelves_paizuri_anim 1:
        "cg/christie_root/library/bibliogirl/paizuri_1.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_2.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_3.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_4.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_5.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_6.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_7.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_8.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_9.png"
        pause .19
        "cg/christie_root/library/bibliogirl/paizuri_10.png"
        pause .19
        repeat
    image library_bookshelves_paizuri_anim 2:
        "cg/christie_root/library/bibliogirl/paizuri_1.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_2.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_3.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_4.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_5.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_6.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_7.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_8.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_9.png"
        pause .11
        "cg/christie_root/library/bibliogirl/paizuri_10.png"
        pause .11
        repeat    
    image library_bookshelves_paizuri_anim 3:
        "cg/christie_root/library/bibliogirl/paizuri_1.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_2.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_3.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_4.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_5.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_6.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_7.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_8.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_9.png"
        pause .06
        "cg/christie_root/library/bibliogirl/paizuri_10.png"
        pause .06
        repeat

    image chair_book = "locations/imagebuttons/City_Library/biblio_book.png"
label biblio_BookW:
    show GG Normal:
        xalign .15
    show BiblioGirl Smile:
        xalign .85
    "[gg]" "Лучший курьер на районе прибыл!"
    "Нэнси" "Хи-хи-хи!"
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Надеюсь, я не слишком утомляю тебя своими заботами."
    show GG Passion with my_dissolve
    "[gg]" "Ты трудишься на много больше."
    show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Оу!"
    show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Какая лестная оценка, [gg]."
    show BiblioGirl Smile with my_dissolve
    "Нэнси" "Пойдём. Время не ждёт."
    # //Оба спрайта движутся вправо
    # //Читальный зал
    # //Оба спрайта выезжает слева
    # //Читатели


    show GG Passion:
        ease 1 xalign 1.5
    show BiblioGirl Smile:
        xzoom -1
        ease 1 xalign 1.5
    with None
    pause 1
    scene readroom_people bg
    with my_dissolve 
    show GG Passion:
        xalign -.5
        ease 1 xalign .15
    show BiblioGirl Normal:
        xalign -.5
        ease 1 xalign .85
    pause 1
    "Нэнси" "Правила ты помнишь, я надеюсь."
    show BiblioGirl Normal with my_dissolve
    "Нэнси" "Посетители просят книгу, и ты им её приносишь."
    show GG Skepticism:
        yoffset 190
    with my_dissolve
    "[gg]" "Я уже на взлёте, как чёртов шатл."
    show BiblioGirl Smile with my_dissolve
    "Нэнси" "Ну вперёд, красавчик."
    show BiblioGirl Smile:
        xzoom -1
        ease 1 xalign 1.5
    with None
    pause 1

    # Повторение мини-игры
    # //При успехе мини-игры появляется табличка «Вы победили» (которая у нас есть)
    show GG Think with my_dissolve
    "[gg]" "Где Нэнси?"
    show GG Think with my_dissolve
    "[gg]" "Я думал он появиться, чтобы поблагодарить меня…"
    show GG Think with my_dissolve
    "[gg]" "Ну хорошо, поищу её сам."
    show GG Smile with my_dissolve:
        yoffset 0
    "[gg]" "Возможно она снова приготовила мне сюрприз."
    # //GG_Normal едет вправо
    # //Книжные полки
    # //Спрайт  I_dont_Book
    # //После активации спрайт
    with None
    pause 1
    scene bookshelves bg
    show chair_book
    with my_dissolve #my_fade #TODO а куда my_fade делся?
    show GG Normal:
        xalign -.5
        ease 1 xalign .1
    pause 1
    call screen book_action
    show GG Surprise
    "[gg]" "Книга?"
    show GG Surprise
    "[gg]" "Это и есть мой сюрприз?.."
    show GG Chagrin
    "[gg]" "В тот раз был поинтереснее."
    show GG Think:
        yoffset 190
    "[gg]" "Хм…"
    show GG Think
    "[gg]" "Может в этой книге тоже сокрыто какое-то послание на эльфийском языке."
    show GG Think
    "[gg]" "Стоит поискать."
    # //Boobs_Read_1
    scene black with Dissolve(.5)
    scene library_bookshelves_bg 
    show library_bookshelves_paizuri_anim 1:
        zoom .5
        alpha 0
    show library_bookshelves_book
    with Dissolve(.5)
    "[gg]" "Нет…"
    "[gg]" "Здесь определённо ничего нет."
    "[gg]" "Как странно."
    "[gg]" "Попробую пролистать все страницы на случай, если где-то стоит пометка, а я просто не заметил."
    "[gg]" "Пробегая словами книгу, могу заметить, что это какой примитивный любовный роман…"
    "[gg]" "Может это и есть одно сплошное послание и мне просто следует вчитаться в содержание?.."
    "[gg]" "Если б ещё текст не вызывал у меня приступы острого стыда.."
    "[gg]" "На какой странице я бы не очутился, везде описываются «страстные» сцены нимфоманки и парня, который только начал постигать азы любви."
    "[gg]" "Ну вот…"
    "[gg]" "Очередная глава, где значится, что так и так…"
    "[gg]" "Неутолимая женщина застаёт возлюбленного врасплох, снимает с него штаны и, скрепив его возбуждённый член между своими двумя огромными дыньками, нежно массирует детородный орган парня."
    "[gg]" "Чёрт…"
    "[gg]" "Не смотря на весь примитивизм, признаться, я и сам немного возбудился."
    "[gg]" "От рассказа веет такой аурой сексуальности, что я буквально ощущаю, как сам испытываю сисько-трах…"
    "[gg]" "Стоит отдать автору должное, он сумел меня впечатлить."
    "[gg]" "Или же…"
    # //Книга опускается
    # //Boobs_Read_anim
    # //x1
    
    show library_bookshelves_book:
        linear 1.0 yoffset 1300

    show library_bookshelves_paizuri_anim 1:
        zoom .5
        linear .5 alpha 1
    "[gg]" "Нэнси?!!.."
    "Нэнси" "Тихо, дурашка!"
    "Нэнси" "Ты же не хочешь, чтобы сюда прибежала вся библиотека?"
    "[gg]" "Не хочу."
    "Нэнси" "Ну и? Чего замер? Хи-хи-хи."
    "[gg]" "Я… Э…"
    "Нэнси" "Разве не нравится книга?"
    "[gg]" "Неожиданно впечатляющая."
    "[gg]" "Я бы даже сказал - шокирующая."
    "Нэнси" "Рада, что смогла угодить и твоим читательским интересам."
    "Нэнси" "Продолжай читать, [gg]."
    "Нэнси" "Нам обоим предстоит дойти до развязки."
    "[gg]" "Хе-хе…"
    "[gg]" "Верно подмечено, Нэнси. Я, пожалуйста, углу… углублюсь в чтение."
    "Нэнси" "Ага."
    "[gg]" "В общем… В книге значится, что женщина ускорила свои массажные ласки."
    # //x2
    show library_bookshelves_paizuri_anim 2
    "Нэнси" "Хи-хи-хи."
    "Нэнси" "Ну же, не вздыхай так тяжело. Что было дальше?"
    "[gg]" "Дальше описывается её игривый, подобострастный взгляд и лёгкая улыбка, с которой она мастерски ублажала своего партнёра."
    "[gg]" "Женщина, пылая от предвкушения, стала покрываться горячим потом…"
    "[gg]" "А член её партнёра, словно в благодарность за старательность нимфоманки, пульсировал в такт с её движениями грудей, что крепко, но ласково, массировался вдоль всего размера."
    "[gg]" "Парень тяжело и громко дышал, не решаясь сказать ни слова."
    "[gg]" "То ли от того, что боялся спугнуть свою даму, то ли потому, что находился в полном ступоре от происходящего."
    "[gg]" "Во всяком случае, оба партнёра получали желаемое удовольствие."
    "Нэнси" "Ну же? Давай дальше!"
    "Нэнси" "Хочу знать, чем закончилась эта сцена."
    # //x3
    show library_bookshelves_paizuri_anim 3
    "[gg]" "Читаю-читаю…"
    "[gg]" "Леди, которая всё это время ублажала парня, разыгралась не на шутку."
    "[gg]" "Теперь, когда она поняла, что её партнёр испытал достаточно радости от массажа, даме захотелось приблизить кульминацию."
    "[gg]" "Всячески ускоряя ритм, продолжая строить вызывающую гримасу, она с наслаждением следила за реакцией своего мужчины."
    "[gg]" "Парень, чей член давно дрожал в нетерпении, сдерживался из последних сил."
    "[gg]" "Половой орган мужчины с избытком покрылся прозрачными выделениями, давно измазав сочные груди прекрасной нимфоманки."
    "[gg]" "И парень, и женщина, оба дышали в такт, вот-вот ожидая белоснежного фонтана, что должен был залить богатое декольты дамы."
    "Нэнси" "И как, [gg]? У него получилось, а?.."
    "Нэнси" "Порадовал он свою возлюбленную?"
    # //Выбор скорости/кончить
    # //Кончить
    # //Boobs_Read_END_anim
    menu bibliogirl_cum_menu1:
        "Кончить":
            $ pass
        "Продолжить в том же темпе" if True:
            call wait_click_label from _call_wait_click_label_63
            jump bibliogirl_cum_menu1
    "[gg]" "Кончаааааюююююю!!!"
    "[gg]" "О дааааааа…."
    "[gg]" "К чёрту эту книгу, Нэнси. Я обожаю твои сиськи!"
    # //Boobs_Read_END
    scene library_bookshelves_bg 
    show library_bookshelves_bibliogirl_end
    show library_bookshelves_smerm_anim
    "Нэнси" "Хи-хи-хи!"
    "Нэнси" "Там много…"
    "Нэнси" "Так сладко пахнет и такая горячая. Ммммм…"
    "Нэнси" "Уверенна, наша концовка более реалистичная."
    "[gg]" "Ага."
    $ time.time_now = "evening"
    # //Книжные полки
    scene bookshelves bg 
    show GG Embarrassment:
        xalign .1
    show BiblioGirl Embarrassment:
        xalign .85

    show BiblioGirl Embarrassment
    "Нэнси" "Чтоб ты понимал, [gg], ты первый, кого я так отблагодарила за помощь."
    show GG Embarrassment
    "[gg]" "Я ценю это, Нэнси."
    show GG Embarrassment
    "[gg]" "Ты мне нравишься, и я всегда рад тебе помочь."
    show BiblioGirl Embarrassment
    "Нэнси" "И чтоб ты понимал, ты единственный, кто разгадал мои загадки."
    show GG Passion
    "[gg]" "Ты проверяла меня? Проверяла, можно ли быть со мной достаточно… близкой?"
    show BiblioGirl Passion
    "Нэнси" "Ну конечно."
    show BiblioGirl Passion
    "Нэнси" "Мы должны были лучше узнать друг друга."
    show BiblioGirl Passion
    "Нэнси" "И если парни, как правило, ценят в девушках их красоту, то я ценю ум и смекалку хи-хи-хи."
    show GG Passion
    "[gg]" "Ты права. Права во всём, хе-хе."
    show BiblioGirl Passion
    "Нэнси" "До встречи, красавчик."
    show GG Passion
    "[gg]" "Увидимся."
    scene black with Dissolve(.5)
    $ events_pop('biblio_BookW', 0)
    $ descript_BiblioGirl = _('')
    $ time.time_now = "morning"
    jump main_interface_label
    return

screen book_action():
    imagebutton:
        focus_mask True
        idle "locations/imagebuttons/City_Library/biblio_book.png"
        hover im.MatrixColor("locations/imagebuttons/City_Library/biblio_book.png", im.matrix.brightness(0.1))
        action Return()