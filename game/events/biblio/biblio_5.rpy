label biblio_5:
    # Description: Расшифровать фразу, воспользовавшись своим рабочим столом.
    # Task: Активировать письменный стол ГГ.
    
    call show_bg_image_label from _call_show_bg_image_label_271
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    label .win:
    # //После успеха мини-игры
    hide screen decoder_game
    "[gg]" "«Если я тебе понравилась, верни мне книгу в пятницу.»"
    "[gg]" "Ну и ну, я мог бы и сам догадаться."

    $ location_now = "GG_Room"
    
    $ events_pop("biblio_5", 0)
    $ events_pop("round_1", 0)

    $ Event("biblio_6", location = "City_Library_BiblioGirl", button_name="Вернуть книгу")
    $ descript_BiblioGirl = _('Вернуть “Кама-сутру» Нэнси в библиотеке в пятницу.')

    $ check_event_in_allowed_events("biblio_6")

    jump main_interface_label
