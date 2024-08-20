init:
    image mail_bibliogirl = "cg/biblio/mail.png"
label biblio_1:
    # Description: Ознакомиться с “Кама-сутра».
    # Task: Активировать книгу в инвентаре 
    hide screen bag_interface
    call show_bg_image_label from _call_show_bg_image_label_270
    show GG Surprise
    show GG Surprise at go_from_left(xxalign = .15)
    with my_dissolve
    
    "[gg]" "Хм..."
    "[gg]" "Из книги выпала какая-то шпаргалка."
    "[gg]" "Это записка или просто закладка?"
    
    show screen give_item_screen(i_path+'items/ticket.png', _('Любовная записка'), _('Листочек с чьими-то записями.'))
    pause
    hide screen give_item_screen
    # Спрайт с записью
    # («Если я тебе понравилась, верни мне книгу в пятницу.»)
    show GG Think
    show mail_bibliogirl:
        xalign .5
        yalign .5
    with my_dissolve
    
    "[gg]" "Понятия не имею, что за каракули здесь написаны."
    "[gg]" "Похоже на какой-тот шифр."
    hide mail_bibliogirl with my_dissolve
    "[gg]" "Спрошу и Игоря."
    
    $ add_to_inventory(name = 'Любовная записка')
    
    $ events_pop("biblio_1", 0)
    $ Event("biblio_2", location = "Igor", button_name=_("Узнать про записку"))
    $ check_event_in_allowed_events("biblio_2")
    $ descript_BiblioGirl = _('Спросить у Игоря про странную записку.')
    jump main_interface_label
