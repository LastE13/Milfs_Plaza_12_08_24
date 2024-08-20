label biblio_21:
    # Description: Купить женские парики для Зудилы и Бубнилы.
    # Task: Купить женские парики в магазине одежды (60$)
    
    call show_bg_image_label from _call_show_bg_image_label_272
    show GG Think
    show GG Think at go_from_left(xxalign = .15)
    with my_dissolve

    $ location_now = 'ClothesStore'
    call talk_with_clothes_store_woman_menu from _call_talk_with_clothes_store_woman_menu

    "[gg]" "Пол дела сделано. Теперь надо возвращаться с Зудиле и Бубниле."
    #$ location_now = "City_Shop"
    $ events_pop("biblio_21", 0)
    $ Event("biblio_22", location = "JayBob")
    $ descript_BiblioGirl = _("Отдать маскировку Зудиле и Бубниле")

    $ check_event_in_allowed_events("biblio_22")

    
    jump main_interface_label
