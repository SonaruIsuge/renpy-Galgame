

# 遊戲在此開始。

label start:

    show screen quick_menu
    hide screen mana_ui
    window hide

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

label chap1:
    
    window auto
    show screen mana_ui

    scene bg pond
    with fade
    
    think """
    
        眼前是個池塘，不是湖水清澈的那種，
        
        是長滿水草，棲息許多魚蝦的那種池塘

    """

    me "嘿！"

    think """
    
        隨著清澈的落水聲，我跳進了池塘中，
    
        向著湖底的亮光游去，全身感到一種熟悉的妖氣，

        我來到了人界的另一面---妖界。

    """
    
    scene bg tree 
    with flash

    play music "audio/weird.mp3"

    think "我直起溼答答的身子，抬頭一看。"
    
    show shadow big

    who "哎呀~今天比平常早呢，歡迎回來"
    
    think "眼前是一位美少女 給人的印象大概是理想的妻子那種類型"
    
    me "哦我回來了"
    
    think "但是那種想法我一丁點都沒有，畢竟她是我媽——五步春。"
    
    think "我抖了抖身上的水，好讓自己不要那麼濕。" with hpunch
    
    mother "阿啦啦，都溼透了呢。快脫掉吧！"
    
    me "什…？我都幾歲了媽！"

    think "叫我在父母面前脫光什麼的，"

    think "17歲的我還是有著自己的自尊的。"
    
    mother "嘛～我可是從小看到大了喔！有什麼好害羞的嘛？"
    
    think """
    
        這傢伙看來暫時是不會離開了...，

        沒辦法了。
        
        我把我僅存的一點尊嚴拋開，脫光上半身並把衣服擰乾。
        
        「總有一天我一定要解決池塘這個問題」
        
        我在心中默默地發了誓。
        
    """
    
    ##換場景到家中
    scene bg tree
    with fade

    show shadow big
    with dissolve

    think """
    
        7點是晚飯時間，我已經準備吃飯了，

        我家算是大豪宅的那種規模，

        從浴室走到飯廳都要個5分鐘，

        上學更是麻煩，還得通過那個池塘。
    
    """

    me "說到底我有必要要到人界上學嗎？"

    mother "松君 你聽好 你的身分很特別，你是酒吞童子的兒子，同時也是半妖。"

    mother "這兩個世界對你來說都很重要，你媽我很對不起你，給你這個複雜的身分....。"
    
    think "我感到有些尷尬，但其實這樣的生活我已經習慣了。"

    who "春~~麻煩幫我拿一下毛豆"

    hide shadow big 
    with moveoutright
            
    think "此時老爸提著一壺大的浮誇的酒瓶出現了，他銳利的眼神看著我，"
    
    father "兒子阿，如果你真的這麼希望的話，就留在妖界繼承我的位置吧！"

    me "ㄟ？"

    think """

        與父母的對話總是不經意間會被迫做出一些不想做的選擇...
        
        老爸是酒吞童子，雖然平時是一副很有威嚴的樣子，但卻總是黏在老媽身邊，

        他是妖界的長老，負責維持妖界秩序，以及維持與人界之間的和平。

        但最近他吵著要退休，打算把位置傳給我，

        我老媽是人類，老爸是妖怪當家，在維持與人界和平的立場上，

        我這個半妖在兩邊都得經營。

        """

menu:
    
    think "這些我都懂......"

    "但是我不想，推託":

        jump chap1_refuse_inherit

    "體諒父母，繼承家業":

        jump chap1_agree_inherit

label chap1_refuse_inherit:

    me "....."

    me "讓我再想一下"

    think """

        我飯也沒吃幾口就回房間去了

        完全沒有勇氣和他們對上眼阿...
        
    """

    stop music fadeout 1.0

    jump room

label chap1_agree_inherit:

    me "我會為此作準備的。"

    me "繼承當家的話，你們也是臉上有光吧！"
    
    think """
        
        當然身為半妖的我，當上當家的話，

        一定會有很多持反對意見的妖怪的，
        
        但這就是我的課題吧！

        大概老爸也想退休了，

        畢竟他也是很辛苦啊...。

        原本人界和妖界很不和平，

        在妖怪中有著「隱神通」的組織，

        他們以少數精英在人界和妖界之間作亂，

        所幸在人界有著陰陽道士所組成的「珠天」來與之對抗，

        而妖界有酒吞童子來壓制。

        我是很支持老爸的作為，

        而我是他的兒子，同時又是個半妖，

        自然而然在妖界也理所當然是被討厭的存在......。
    
    """

    father "哈哈，是嗎？，不愧是我兒子！長大了呢！"

    father "那為了紀念你的成長，把這個喝了吧！"

    think """
    
        老爸嘴裡掛著一抹壞笑，

        並把手中的酒杯遞給我，

    """
    #淡入淡出需調整
    stop music fadeout 1.0
    play music "audio/dream.mp3"

    think """

        那酒杯裡裝著透明的液體，

        它的味道香醇，酒精的氣息直逼腦門，

        這也許是遺傳，但我一聞到那個香味便不由自者的盯著它看，
    
    """

    me "等等阿老爸我還是高中生阿！"

    father "沒事啦，你可是老子的兒子呢！"

    think "我接過酒杯，仔細端詳著那杯酒。"

menu:

    father "來吧，！喝了他，這可是好東西哦！哈哈哈哈哈！！"

    "可疑，有夠可疑，怎麼看都有問題":

        jump chap1_doubt

    "但...但是...真香......":

        jump chap1_drink

label chap1_drink:

    think """
    
            父親不可能會害我的吧！

            我盯著那個看起來快突破表面張力的液體，

            這個時候靠得就是氣勢啊！！

        """

    me "咕嚕"

    think "一飲而盡..."

    me "......"

    think "不愧是酒吞童子的私釀酒，"
    
    think "濃烈卻不嗆，非常順口..."

    me "嗚呃！..."

    think "突然身體感到無比燥熱，胸口一陣難受，"

    me "這...這是？..."

    think "無法呼吸，灼燒感從胸口開始，往四肢蔓延開來，"
    
    scene bg black
    with blink

    think "我失去了視野，眼前一片漆黑。"

    think "......"
    
    #*妖力提升了
    $mana += 1;

    #表示隔天
    call splashscreen from _call_splashscreen

    me "嗯啊？頭好痛..."

    me "這是...宿醉？..."

    scene bg room
    with fade

    think "我看了一下時鐘。"

    me "哭阿！這不是早上了嗎？？"

    think "得快點準備才行。"

    jump chap2_2

label chap1_doubt:

    stop music fadeout 1.0
    play music "audio/cheer.mp3"

    me "..."

    me "怎麼想都不太對阿..."

    me "等等老爸，說起來你不是常常說你的嬰兒時期都只喝酒的嗎？"

    father "怎了?"

    me "那我呢?我的嬰兒時期是不是也被你灌酒啊??"

    think "我開始為我父母的育嬰政策感到擔心"

    father "沒事啦~每次都有好好的被你母親阻止。"

    me "你倒是給我好好反省阿！"

    who "親愛的~你在幹嘛呢？"

    father "唉！..."

    think """
    
        父親臉色一下子就不好了，

        彷彿看見了暴龍的老鼠一樣。

        『啪！』的一聲，爸爸冷不防的站了起來，

        一股非常強大的壓迫感從爸爸背後傳來，

        無比沉重又輕盈的腳步聲緩緩靠近，

    """

    show shadow big
    with moveinright

    think "母親一手拿著菜刀，一手端著毛豆走出來。"

    father "春啊！妳...妳......妳聽我解釋！！"

    mother "不是說過了！不要亂餵妖怪吃的東西給松嗎？"

    father "咿！"

    think """一瞬間，老爸的尊嚴蕩然無存，

        即便平時於妖界再威風，

        只要在老媽面前便只有挨罵的份。

    """

    mother "你知道我每次要煮好一桌人類和妖怪都能吃的飯菜要花多少心力嗎？"

    father "等等阿春，有話好說，先把菜刀放下。"

    mother "要是松吃出什麼毛病要怎麼辦？"

    father "對不起！我知道錯了！"

    think "父親索性下跪了"

    father "不過你看嘛！是時候讓松他繼承家業了，"

    father "我也只是想加快流程...而已......。"

    mother "加快而已？！你是想加快我出刀的速度嗎？"

    think "看著這對恩愛的夫妻，不打算繼續打擾，我便溜回了房"

    stop music fadeout 1.0

    #轉場房間
    scene bg room
    with fade
        
    me "不過繼承家業阿，我的能力夠嗎?"

    think "說來慚愧....但除了用基本妖力增強體能以外，"

menu:

    think "我完全使不出妖術，感覺沒資格阿...。"

    "深究":

        think "之後去問老爸看看"
        
        $ask_to_be_strong = True

        jump room

    "不深究":
    
        think "算了，船到橋頭撞自然直"
        
        jump room
 
