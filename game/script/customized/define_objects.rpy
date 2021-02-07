####################
##場景圖片
####################

# image black20:
#     black
#     alpha 0.2

####################
##人物圖片
####################

image shadow big: 
    "shadow_1080 normal.png"
    zoom 2.0
    xalign 0.5 yalign 0.0
    anchor (0.5, 0)

####################
##動畫
####################

image fire_ani:
    "ui mana_1.png"
    pause 0.07
    "ui mana_2.png"
    pause 0.07
    "ui mana_3.png"
    pause 0.07
    "ui mana_4.png"
    pause 0.07
    "ui mana_3.png"
    pause 0.07
    "ui mana_2.png"
    pause 0.07
    repeat

####################
##轉場效果
####################

define flash = Fade(0.5, 0.5, 0.5, color="#fff")
    
define blink = ImageDissolve("effect/blink.png", time = 0.5, ramplen = 64, reverse = True)

####################
##變數
####################

#主角妖力
define mana = 0

#chap1是否想深究變強方法
define ask_to_be_strong = False
