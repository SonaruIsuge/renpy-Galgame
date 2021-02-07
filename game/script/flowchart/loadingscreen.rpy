label splashscreen:

    stop music fadeout 1.0

    hide screen mana_ui
    hide screen quick_menu

    scene black
    pause(1)

    show text "Loading" with dissolve:
        xalign 0.9
        yalign 0.9
        
    pause(2)

    hide text with dissolve
    pause(1)

    show screen mana_ui
    show screen quick_menu

    return