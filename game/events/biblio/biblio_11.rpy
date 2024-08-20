label biblio_11:
    # Description: Вернуть элитарные мешочки Зудиле и Бубниле.
    # Task: Активировать Зудило
    
    call show_bg_image_label from _call_show_bg_image_label_276
    show Jay Silence
    show Jay Silence:
        ypos 1085
        xalign .65
    show Bob Normal
    show Bob Normal:
        ypos 1085
        xalign .95
    show GG Normal
    show GG Normal at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "Получите-распишитесь."
    "Зудило" "Йеееее! Наше дерьмо!"
    "[gg]" "Гоните цветы, ботаники."
    "Зудило" "Бубнилыч – тащи товар."
    
    # //Bob исчезает и вправо и возвращается
    show Bob Normal behind Jay:
        ypos 1085
        ease .8 xalign 1.8
        ease .8 xalign .95

    
    "Бубнило" "......."
    "Зудило" "Вот, ландыши, взращённые в девственных садах профессионального инцела!"
    "Бубнило" "..........!!!!!!"
    
    # //Бубнило движется в сторону Зудилы, якобы ударяя его
    # //Зудило на мгновение трясётся
    show Bob Normal:
        ypos 1085
        linear .1 xalign .7
    show Jay OMG:
        linear .1 yoffset 20
        linear .1 yoffset 0
        repeat

    pause 0.5
    show Jay OMG:
        linear .1 yoffset 0
    
    "Зудило" "Эй, я же просто шучу!"

    show Bob Normal:
        ypos 1085
        ease .8 xalign .95

    show GG Smile with my_dissolve
    "[gg]" "Спасибо, что выручили."
    show Jay Silence
    with my_dissolve
    "Зудило" "Взаимно, чувачело!"

    $ location_now = "City_Shop"
    $ descript_BiblioGirl = _("Подарить цветы Нэнси.")

    
    $ events_pop("biblio_11", 0)
    $ Event("biblio_12", location = "City_Library", time = ['morning',  'afternoon'])
    $ check_event_in_allowed_events("biblio_12")

    $ add_to_inventory(name = 'Букет ландышей')
    $ descript_BiblioGirl = _("Подарить цветы Нэнси.")    
    $ locations.update({
        'City_Library':
            Location(
                'City_Library',
                buttons       = [],
                image_buttons = {}
                )}

    )
    jump main_interface_label
