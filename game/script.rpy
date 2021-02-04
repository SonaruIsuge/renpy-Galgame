
#圖片
image shadow_big: 
    "shadow_1080 normal.png"
    zoom 2.0
    xalign 0.5 yalign 0.0
    anchor (0.5, 0)

#轉場效果
define flash = Fade(0.5, 0.5, 0.5, color="#fff")

#變數
define mana = 0

# 遊戲在此開始。

label start:

    # 顯示一個背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。
    
    scene bg starpond:
        linear 20.0 yalign 1.0

    play music "audio/star.mp3"
    
    n """
        一直以來，我有著令人困擾的秘密，
      
        不知道我此生的意義，
      
        更不知道此身為人亦或為妖。
      
        沒有特別想做的事，
      
        也沒有需要做的事，
      
        就只是渾渾噩噩的過著日子。
      
        心想過著過著，總會發現一些什麼，
      
        一成不變的生活是否能再多一些什麼呢？
        
    """
    
    stop music fadeout 1.0

label Chapter1:
    
    scene bg pond
    with fade
    
    think "眼前是個池塘，不是湖水清澈的那種，是長滿水草，棲息許多魚蝦的那種池塘"
    
    think "雖然有點突然，我現在要跳下去"
    
    think "我提著老媽叫我買的食材，詳細來說有蛋，魚還有豆腐，吸了一口氣，縱身一躍!!"
    
    think "向著湖底的亮光游去，全身感到一種熟悉的妖氣"
    
    scene bg tree 
    with flash
    
    show shadow_big

    mother "哎呀~{color=#ffff00}五步松{/color}，今天比平常早呢，歡迎回來"
    
    think "眼前是一位美少女 給人的印象大概是理想的妻子那種類型"
    
    me "哦我回來了"
    
    think "但是那種想法我一丁點都沒有 畢竟她是我老媽"
        
    scene bg tree
    with hpunch 
    
    show shadow_big
    
    think "抖了抖身上的水 讓自己不要那麼溼"
    
    mother "阿啦啦，都溼透了呢。快脫掉吧"
    
    me "什…？我都幾歲了"
    
    mother "嘛～我可是從小看到大了，有什麼好害羞的"
    
    think "我把我僅存的一點尊嚴拋開，脫光上半身並把衣服擰乾。一定要解決池塘這個問題"
    
    me "吶為什麼要弄成池塘 說到底咱一定要到人界上學嗎?"
    
    mother """
    
        松 你聽好 你的身分很特別
           
        你是最強妖的兒子，同時也是半妖，在兩個世界對你來說都很重要
           
        老媽我很對不起你，給妳這個複雜的身分....
        
        """
    
    think """
            我感到有點尷尬
            
            此時老爸提著一壺酒出現了，他銳利的眼神看著我
            
        """
    
    father "兒子阿，如果你真的這麼希望的話，就留在妖界繼承我的位置吧。"

    think """
        
        老爸是妖界的長老，雖然平時是一副廢材樣，又總是黏在老媽身邊

        但他是妖界長老aka酒吞童子，姑且是

        負責維持妖界秩序，以及維持與人界的和平
            
        但最近他尋思著要退休，打算把位置傳給我

        我老媽是人，老爸是最強妖，在維持與人界和平的立場上，我這個半妖也更站得住立場
        
        """

menu:
    
    think "這些我都懂......"

    "但是我不想，推託":

        jump chap1_refuse_inherit

    "體諒父母，繼承家業":

        jump chap1_agree_inherit

label chap1_refuse_inherit:

    me ".....我再想一下"

    think """

        我速速吃完飯回房去了

        留下無奈的老爸和滿臉困擾的老媽
        
        """

    jump Chapter1_2

label chap1_agree_inherit:

    think """
        
        好吧，我想想老爸和老媽經歷過的，我覺得我的煩惱微不足道

        原本人界和妖界很不和平，妖界有個左派組織叫隱神通
        
        他們認為人族剝奪妖怪們的權力和資源已經太久了，為何能力比較強的妖怪要隱忍?
            
        於是人界和妖界開始了長達50年(?的鬥爭，直到老爸出面阻止隱神通
        
        並且成為妖界的長老，但那些激進分子卻覺得老爸背叛妖界….

        比起其他妖怪的莽撞，老爸知道鬥爭並不是最好的答案

        在這一點上我還是蠻尊敬他的
        
        雖然他看起來只是個酒精中毒的色老頭

        ....

        """

    me "我雖然很尊敬老爸，也蠻擔心自己能不能做好，總而言之等時機到了我會盡力而為的"

    father "UMU，不愧是我兒子，那把這個喝了吧"

    think "老爸把手中的酒杯遞給我"

    me "等等阿老爸我還是高中生阿"

    father "沒事啦，老子嬰兒的時候都用酒替代奶，還不是長得頭好壯壯"

    me "不要拿我跟你相提並論好嗎?你是酒吞耶"

menu:

    think "怎麼這麼可疑，明明是自己的親生父親怎麼看起來會這麼可疑，要喝嗎?"

    "父親不會害我的，喝":

        jump chap1_drink

    "懷疑，感到不對勁":

        jump chap1_doubt

label Chapter1_2:

    ""

    return

label chap1_drink:

    think """
    
        我接過酒杯，盯著那個看起來表面張力很高的液體

        咕嚕

        一飲而盡

        味道意外的還不錯，不愧是酒吞童子的私釀酒

        """

    scene bg black
    with fade

    think "突然眼前一片黑，身體感到無比燥熱"
    
    #*妖力提升了
    $mana = 1;

    scene bg tree
    with fade

    think "在房間醒來"

    me "哭阿遲到了"

    jump chap2

label chap1_doubt:

    me "等等老爸，說起來你剛剛不是說你的嬰兒時期被灌酒嗎?"

    father "怎了?"

    me "那我呢?我的嬰兒時期是不是也被你灌酒啊??"

    think "我開始為我父母的育嬰政策擔心"

    father "沒事啦~每次都有好好的被你母親阻止"

    me "哭阿還真的有喔"

    mother "親愛的~你在幹嘛呢?"

    jump chap2

label chap2:
