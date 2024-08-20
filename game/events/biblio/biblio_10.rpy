label biblio_10:
    # Description: Найти 5 элитных мешочков Зудилы и Бубнилы. Зная парней, искать стоит в гетто, парке, магазинах и, возможно, на улицах, где живу я и Сьюзен.
    # Task: Собрать 5 элитных мешочков, разбросанных по локациям
    
    call show_bg_image_label from _call_show_bg_image_label_256
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve
    
    
    # # //При сборе каждого мешка
    
    # "[gg]" "Нашёл!"
    
    # # //При сборе всех мешков
    
    # "[gg]" "Супер!"
    # "[gg]" "Я собрал всё, что Бубнило растерял и теперь мне нужно вернуть эту дрянь владельцам."
    $ descript_BiblioGirl = _("Вернуть элитарные мешочки Зудиле и Бубниле.")

    $ unlock_city_psi = unlock_city_psi2

    if locations['City_Getto'].image_buttons == {}:
        $ unlock_city_getto = False
    $ events_pop("biblio_10", 0)
    $ Event("biblio_11", location = "JayBob") 
    $ check_event_in_allowed_events("biblio_11")

    jump main_interface_label
