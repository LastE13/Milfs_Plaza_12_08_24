init python:
    bag_grass_count = 0
    unlock_city_psi2 = True
    def bag_grass_search(lok):
        global bag_grass_count
        bag_grass_count += 1
        
        if bag_grass_count == 5:
            renpy.call("full_bag_grass", lok)
            Event("biblio_11", location = "JayBob") 
            renpy.jump("biblio_10")
        else:
            renpy.call("give_me_bag", lok)



label give_me_bag(lok):
    
    $ add_to_inventory(name = 'Элитный мешочек', ncopy = True)
    show screen give_item_screen(i_path+'/items/bag_grass.png', _('Элитный мешочек'),[_('Элитный мешочек Зудилы и Бубнилы')])
    $ locations[lok].image_buttons.pop('bag')
    $ print(locations[lok].image_buttons)
    pause
    hide screen give_item_screen
    "[gg]" "Нашёл"
    return
label full_bag_grass(lok):
    $ add_to_inventory(name = 'Элитный мешочек', ncopy = True)
    show screen give_item_screen(i_path+'/items/bag_grass.png', _('Элитный мешочек'),[_('Элитный мешочек Зудилы и Бубнилы')])
    $ locations[lok].image_buttons.pop('bag')
    $ print(locations[lok].image_buttons)
    pause
    hide screen give_item_screen
    "[gg_now]" "Супер!"
    "[gg_now]" "Я собрал всё, что Бубнило растерял и теперь мне нужно вернуть эту дрянь владельцам."
    return
label biblio_9:
    # Description: Найти того, кто знает, как добыть ландыши.
    # Task: Активировать Зудило и Бубнило
    
    call show_bg_image_label from _call_show_bg_image_label_253

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
    
    "[gg]" "Чуваки, мне срочно нужны ландыши."
    "[gg]" "Вне зависимости, есть они у вас или нет, но я знаю, что вы из тех, кто Титаник со дня океана достанет."
    show Jay OMG
    with my_dissolve
    "Зудило" "Ёу-ёу-ёу."
    "Зудило" "Полегче!"
    "Зудило" "У нас с Буднило от твоих комплиментов жопа слиплась."
    show Jay Normal
    with my_dissolve
    "Зудило" "Я напоминаю, раз уж ты не обращаешь на это никакого внимания – мы бизнесмены, а не ботаники."
    "Бубнило" "......."
    "[gg]" "Хватит набивать себе цену."
    "[gg]" "Раз уж вы торгуете травой, то наверняка и сами пытались что-то выращивать."
    "Зудило" "Ну пытались..."
    "[gg]" "А значит вам приходилось заниматься созданием парников и изучением растительности."
    "Зудило" "Именно так, чувачело."
    "Зудило" "Поэтому я с уверенностью могу заявить, что ландыши – не курят."
    "Зудило" "И выращивать их смысла не было."
    show Bob Mobile
    with my_dissolve
    "Бубнило" "........"
    show Jay OMG
    with my_dissolve
    "Зудило" "Чего?!"
    "Бубнило" "......................."
    "Зудило" "На кой хрен ты это делал?"
    show GG Surprise
    with my_dissolve
    "[gg]" "Что? Что он говорит, Зудило?"
    show Jay Normal
    show Bob Normal
    "Зудило" "Мдэ..."
    "Зудило" "Бубнило пытается намекнуть, что после наших неудач со взращиванием марихуаны, он решил заняться цветами."
    "Бубнило" "................................."
    "Зудило" "Говорит, что они тоже приносят бабки."
    show GG Smile with my_dissolve
    "[gg]" "Так значит, у вас есть нужные мне цветы?"
    "Зудило" "Видимо так..."
    show GG Normal with my_dissolve
    "[gg]" "Говорите стоимость – плачу!"
    "Бубнило" "................................."
    "Зудило" "Грёбаный Бубнило!"
    "Зудило" "Ты не бубнило, ты – мудило!"
    show GG Surprise with my_dissolve
    "[gg]" "Что случилось?"
    "Зудило" "Этот жиртрес потерял весь наш элитный товар."
    "Зудило" "Пять ценнейших пакетиков выпало у него из дырявого кармана."
    show GG Chagrin with my_dissolve
    "[gg]" "Сожалею, парни..."
    "Зудило" "Оставь это нытьё при себе. Нам нужен товар и никак иначе."
    show GG Skepticism with my_dissolve
    "[gg]" "Хотите сказать, что я вам должен его добыть?"
    "Зудило" "Почему бы и нет."
    "Зудило" "Поищи наши мешочки по району, ты наверняка быстро справишься."
    "Зудило" "Их всего-лишь пять штук."
    "Зудило" "Они довольно заметные, и ты легко обратишь на них внимание."
    "Зудило" "Как только соберёшь все, приноси нам, а я отправлю Бубнило принести твои сраные ландыши."
    "Зудило" "Идёт?"
    show GG Normal with my_dissolve
    "[gg]" "Любите вы всё усложнять..."
    "Зудило" "Иди уже."

    $ location_now = "City_Shop"
    
    $ events_pop("biblio_9", 0)
    $ Event("biblio_10", location = "City_Psi") #TODO я поняла что нужно будет создать еще 5 label, но где сбор предметов сделать - хз, они уже есть?
    $ descript_BiblioGirl = _("Найти 5 элитных мешочков Зудилы и Бубнилы. Зная парней, искать стоит в гетто, парке, магазинах и, возможно, на улицах, где живу я и Сьюзен.")
    if 'City_Getto' not in locations:
        $ Location(
            'City_Getto',
            buttons = []
            )
    if 'ClothesStore' not in locations:
        $ Location(
            'ClothesStore',
            buttons = []
            )
    if 'City_Psi' not in locations:
        $ Location(
            'City_Psi',
            buttons = []
            )
    
    if unlock_city_psi == False:
        $ unlock_city_psi2 = False
    $ unlock_city_psi = True
    $ print(unlock_city_psi)
  
    $ unlock_city_getto = True
    $ locations['City_Psi'].image_buttons.update({'bag':Function(bag_grass_search, "City_Psi")}) 
    $ locations['City_Park'].image_buttons.update({'bag':Function(bag_grass_search, "City_Park")}) 
    $ locations['City_Getto'].image_buttons.update({'bag':Function(bag_grass_search, "City_Getto")}) 
    $ locations['City_Shop'].image_buttons.update({'bag':Function(bag_grass_search, "City_Shop")}) 
    $ locations['City_Home'].image_buttons.update({'bag':Function(bag_grass_search, "City_Home")}) 
    
    $ check_event_in_allowed_events("biblio_10")
    #jump biblio_10
    jump main_interface_label
