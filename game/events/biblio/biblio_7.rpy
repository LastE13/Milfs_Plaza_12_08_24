label biblio_7:
    # Description: Просмотреть книгу на наличие записок.
    # Task: Активировать книгу «Анжелика и Король».

    hide screen bag_interface
    
    call show_bg_image_label from _call_show_bg_image_label_251
    show GG Think
    show GG Think:
        xalign .15
    with my_dissolve
    
    "[gg]" "Ага, здесь тоже послание на эльфийском."
    "[gg]" "Но теперь я «учёный» и знаю, как всё расшифровывать."
    
    $ events_pop("biblio_7", 0)
    $ descript_BiblioGirl = _("Расшифровать новое послание, воспользовавшись своим рабочим столом.")
    # biblio_8 Запускаем подругому, потому что это кнопка на экране
    $ Event("round_2", location = "gg_room_pc_enter")
    #jump biblio_8
    jump main_interface_label
