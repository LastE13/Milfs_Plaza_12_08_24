label biblio_8:
    # Description: Расшифровать новое послание, воспользовавшись своим рабочим столом.
    # Task: Активировать письменный стол ГГ.
    
    call show_bg_image_label from _call_show_bg_image_label_269
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    
    # //После успеха мини-игры
    label .win:
    hide screen decoder_game
    show GG Think
    "[gg]" "«Я люблю ландыши.»"
    "[gg]" "Что ж, меня дважды просить не надо. Намёк понял!"
    "[gg]" "Нужно найти ландыши и подарить их Нэнси."
    "[gg]" "Правда, сейчас совсем не подходящая пара. Вряд ли я найду их в парке..."

    $ location_now = "GG_Room"
    $ descript_BiblioGirl = _("Найти того, кто знает, как добыть ландыши.")
    
    $ events_pop("biblio_8", 0)
    $ events_pop("round_2", 0)
    $ Event("biblio_9", location = "JayBob")
    $ check_event_in_allowed_events("biblio_9")

    jump main_interface_label
