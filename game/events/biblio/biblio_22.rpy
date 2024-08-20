label biblio_22:
    # Description: Купить женские парики для Зудилы и Бубнилы.
    # Task: Активировать Зудилуи Бубнилу
    
    call show_bg_image_label from _call_show_bg_image_label_263
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
    if get_item('Платья', True, True):
        "[gg]" "А вот и снова я. Заждались?"
        "Зудило" "Мы практически передумали. Ты вовремя."
        "[gg]" "Вот ваш реквизит. Одевайте и погнали."
        $ remove_from_inventory("Платья")
        "Зудило" "Парики? Это и вся маскировка?"
        "[gg]" "Ага."
        "Зудило" "С тебя 50 баксов за услугу."
        "Бубнило" ".................."
        "Зудило" "Каждому."
        show GG Surprise with my_dissolve
        "[gg]" "Имейте совесть!"
        "Зудило" "Или так, или никак."
        menu:
            "Вот, возьми (отдать {i}{b}100{/b}{/i} баксов)." if money >= 100:
                $ money -= 100
                $ show_text_animation('-100 money')
            "!Вот, возьми (отдать {i}{b}100{/b}{/i} баксов)." if money <  100:
                $ pass
            "Уйти":
                $ location_now = "City_Shop"
                jump main_interface_label

        show GG Chagrin with my_dissolve
        "[gg]" "Ладно, юный таланты."
        show GG Angry with my_dissolve
        "[gg]" "Но чтоб отыграли как следует! ПО СТАНИСЛОВСКОМУ!"
        "Бубнило" "................."
        "Зудило" "Говори прямо, чо делать надо? Какие психи? Кого отвлечь?"
        show GG Normal with my_dissolve
        "[gg]" "В библиотеке зверствуют какие-то сектанты."
        "[gg]" "Требует секс. И бесплатно. Поведутся только на женщин, готовых вступить с ними в половое сношение."
        "[gg]" "Трахаться с ними я не прошу."
        "Зудило" "Дебил, мы бы и не стали!"
        "[gg]" "Соблазните и уведите из библиотеки. Всё."
        "Зудило" "Плёвое дело, чувачело."
        "Бубнило" "................. .........."
        $ events_pop("biblio_21", 0)
        $ events_pop("biblio_22", 0)
        $ Event("biblio_23", location = "City_Library")
        $ descript_BiblioGirl = _("Выгнать банду секс-коммунистов из библиотеки.")
        $ location_now = "City_Shop"
        $ check_event_in_allowed_events("biblio_23")
    else:
        "Зудило" "Принёс"
        "[gg]" "Нет"
        "Зудило" "Дебил"
        $ location_now = "City_Shop"
        
    jump main_interface_label
