label biblio_23:
    # Description: Выгнать банду секс-коммунистов из библиотеки.
    # Task: Активировать библиотеку на карте
    
    call show_bg_image_label from _call_show_bg_image_label_255
    show BiblioGirl Smile
    show BiblioGirl Smile:
        xalign .99
    show GG Smile
    show GG Smile at go_from_left(xxalign = -.07)
    show Incel 1
    show Incel 1:
        xalign 1.6
        ease 1 xalign .85
    show Bob Dress
    show Bob Dress at go_from_left(xxalign = .15):
        xzoom -1
        
    show Jay Dress
    show Jay Dress at go_from_left(xxalign = .3):
        xzoom -1
        
    with my_dissolve
    
    
    # //Библиотека хол
    # // BiblioGirl_Normal
    # //Incel_lider (лидер инцелов)
    # //simp (одинаковые спрайты симпов)
    # //GG_Normal выезжает слева
    # //Зудило_Wifu выезжают слева и ближе к //Incel_lider
    
    "Incel" "Вы ещё кто такие?!"
    "Зудило" "Приветики, ребятушечки."
    "Зудило" "Мы услышали, что здесь собрались самые клёвые чуваки на районе и сражаются за право трахаться."
    "Зудило" "А мы, мать вашу, как раз те, кто знает толк в сексе."
    "Зудило" "Мы... эти, как их там, женщины!"
    
    # //simp приближаются к Зудило_Wifu
    show simp1 1:
        xalign 1.69
        linear .5 xalign 0.7

    "Simp" "Вау!"
    "Simp" "Ничосе..."
    "Simp" "Мне нравится та, которая слева."
    "Incel" "Да, они красивые."
    "Incel" "Но меня не проведёшь!"
    "Incel" "Это женщины-провокаторши!!"
    "Incel" "Не видитесь на них, братья. Они призваны, чтобы отвлечь нас от настоящей борьбы!"
    "Simp" "Но ведь..."
    "Simp" "Вождь, наша борьба и заключается в том, чтобы привлечь к себе таких красоток как эти!"
    "Incel" "Нет-нет-нет. Они слишком хороши для нас."
    "Incel" "Вполне вероятно они шлюхи, а мы против проституции!"
    "Зудило" "Какого чёрта ты несёшь, хуемразь поганая?!"
    "Зудило" "Мы пёрлись сюда через весь город не для того, чтобы выслушивать пиздёжь от какого-то долбоёба."
    "Зудило" "Чувачки!"
    "Зудило" "Присоединяйтесь к нашей вечеринке. А этого дебила оставьте и дальше стоять здесь, трястись от зависти."
    "Simp" "Вождь, прости..."
    "Incel" "Неееееееееееет! Вы не можете так поступить со мной!"
    "Зудило" "Ну тогда идём с нами!"
    "Incel" "......"
    "Incel" "Хорошо... Я согласен."
    
    # //Все спрайты уходят, кроме GG_Normal и BiblioGirl_Normal
    show Incel 1:
        ease 1 xalign -1.5
    show Bob Dress:
        xzoom 1
    show Bob Dress:
        ease 1 xalign -1.5
    show Jay Dress:
            xzoom 1
    show Jay Dress:
        ease 1 xalign -1.5
    show simp1 1:
        ease 1 xalign -1.5
    show BiblioGirl Smile:
        pause .4
        ease .5 xalign .9
    "Нэнси" "Ах, [gg]! Ты снова спас меня."
    "[gg]" "Теперь это входит в привычку."
    show BiblioGirl Chagrin with my_dissolve
    "Нэнси" "Правда, вот, пока эти негодяи шумели, вся библиотека опустила."
    "Нэнси" "Люди разбежались и не торопятся к нам заходить."
    show GG Chagrin with my_dissolve
    "[gg]" "Мне очень жаль, [gg]."
    show BiblioGirl Embarrassment with my_dissolve
    "Нэнси" "Но есть и хорошая новость."
    "Нэнси" "Вся библиотека теперь в нашем распоряжении, хи-хи-хи."
    show GG Passion with my_dissolve
    "[gg]" "Тогда не будем терять не минуты."
    show BiblioGirl Passion with my_dissolve
    "Нэнси" "Постой, мой герой, постой."
    "Нэнси" "Позволь мне сперва подготовиться к нашей встрече."
    "Нэнси" "Хочу показать тебе твой подарок, что оказался внутри шкатулки."
    
    show BiblioGirl Passion:
        xzoom -1
        ease 1 xalign 1.6
    # исчезает вправо
    
    show GG Think with my_dissolve
    "[gg]" "Я весь горю от нетерпения."
    "[gg]" "Надеюсь, мне не придётся здесь простоять весь день..."
    "[gg]" "Или это снова какая-то загадка, которую мне надо решить?"
    
    # //комикс  бабл
    
    "Нэнси" "[gg]! Пора!"
    show GG Smile with my_dissolve
    "[gg]" "Ну наконец-то."
    show GG Smile:
        ease 1 xalign 1.6
    with my_dissolve
    pause .9
    jump biblio_23_sex