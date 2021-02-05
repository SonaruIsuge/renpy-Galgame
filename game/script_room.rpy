
label room:

    scene bg tree
    with fade

menu:

    think "呼，那麼該做什麼呢?"

    "肝手游":
        
        jump room_playgame

    "讀書":

        jump room_read

    "向班上曖昧的女同學發訊息":

        jump room_message

    "早早睡了":

        scene bg black
        with fade

        "算了，睡覺吧"

        jump chap2_2

##肝手遊
label room_playgame:

    think """
        
        也是呢，期間活動快結束了

        得趕快打完才行
    
        ......

        ....

        ...

        ..

        .
        
        """

menu:

    think "體力用完了，怎麼辦？"

    "使用遊戲道具回復體力，繼續":

        think """
        ....

        ...

        ..

        .
        
        """
        
        jump chap2_1

    "算了，睡覺吧":

        think "算了，睡覺吧"

        scene bg black
        with fade

        think "..."

        jump chap2_2

##讀書
label room_read:

    think "恩!來讀點書吧"

menu:

    think "看著書架上的書"

    "《罪人或英雄?隱神通》":

        return

    "《強者的故事，酒吞童子》":

        return

    "《人類如何對抗妖怪》":

        return

#打電話
label room_message:

    think "....."
    
menu:
    
    think "好了，要怎麼開頭呢？"

    "直接打電話過去":

        jump room_call

    "你覺得一個人的愛值多少錢":

        jump room_love

    "是我啦!我出車禍了，匯200萬給我":

        jump room_money


label room_call:

    think "「...」"

    me "好緊張啊..."

    think """
    
        根本沒跟女生講過多少次話，

        一上來就是高難度阿...

        不知道我是著魔了還是怎樣

        我還是硬著頭皮打過去

        「 嘟...嘟...嘟...嘟...」

        「 嘟...嘟...嘟...嘟...」

        「 嘟...嘟...嘟...嘟...」

        「 嘟...嘟...嘟...嘟...」

        唉呀！看來是不想接的樣子，

        我的心瞬間安定了下來，也不壞，

    """

    classmate "喂~"

    me "啊啊啊啊啊啊啊啊！！！" with vpunch

    classmate "啊啊啊！"

    classmate "為什麼叫出來了阿？？"

    me "被你嚇到了...妳...妳找我有什麼事嗎？"

    classmate "是你打過來的吧！"

    me "......"

menu:

    think "可惡，愣住了阿...現在該怎麼辦？"

    "今天天氣真好呢！":

        me "今天天氣真好呢！"

        classmate "嗯？ㄟ？天氣？"

        think "看來她一副不知所措的樣子"

        jump room_endcall

    "開始模仿幽靈的叫聲":

        me "嗚嗚！..."

        classmate "ㄟ？是猴子嗎？"
        
        me "嗚嗚嗚！我好恨阿..."
        
        classmate "難道是猴子的鬼魂嗎？"

        me "現在要我原諒妳，只要花699買下這個奇怪的壺"

        classmate "強迫推銷？"

        jump room_endcall

    "那我先掛了":

        me "..."

        jump room_endcall
    
label room_love:

    me "妳覺得一個人的愛值多少錢？"

    classmate "..."

    me "喔喔喔！！！我在幹嘛阿！！" with vpunch

    think """
    
        別鬧了，快收回吧！

        ㄟ？她已讀了阿...

        在那一瞬間，我有種想出門裸奔的衝動

        她似乎回了一些什麼
        
    """

    classmate "ㄟ？沒買過啊。不過如果是指心臟，夠漂亮的話我可以花個500萬收購喔"

    me "500萬？！求之不得！！！"

    think "Bad End"

    think "為了避免變成這樣，所以還是先算了"

    classmate "所以你有要賣嗎？"

    me "..."

    me "你是惡魔吧！"

    jump room_end

label room_money:

    return

label room_endcall:

    think "我受不了了，快找個藉口掛了吧！"

    me "抱歉吶！我突然想到我還沒洗澡，我先掛了"
    
    classmate "唉？這不是通常是我的台詞嗎?"

    classmate "算了，五步同學真是有趣的人"

    jump room_end

label room_end:

    think "呼~真是累死我了跟女生講話原來這麼難啊"

    think "差不多該睡覺了"

    scene bg black
    with fade

    think "..."

    jump chap2_2




