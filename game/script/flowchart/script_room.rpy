
label room:

    scene bg room
    with fade

    stop music fadeout 1.0
    play music "audio/cheer.mp3"

menu:

    think "呼，那麼該做什麼呢?"

    "肝手游":
        
        jump room_playgame

    "讀書":

        jump room_read

    "向班上女同學發訊息":

        jump room_message

    "早早睡了":

        scene bg black
        with fade

        "算了，睡覺吧"

        jump chap2_1

##肝手遊
label room_playgame:

    think """
        
        也是呢，期間活動快結束了

        得趕快打完才行！
    
        ......

        ....

        ...

        ..

        .
        
        """

menu:

    think "體力用完了，怎麼辦？"

    "使用遊戲道具回復體力，繼續肝":

        me "果然，就是肝下去才稱得上是男人啊！"
        
        think "...."
        
        think "..."

        think ".."

        think "." 

        #表示隔天
        call splashscreen from _call_splashscreen_2
        
        scene bg room
        with fade

        me "哭阿！這不是早上了嗎？？"

        think "得快點準備才行。"

        jump chap2_2

    "算了，睡覺吧":

        think "算了，睡覺吧"

        scene bg black
        with fade

        think "..."

        jump chap2_1

##讀書
label room_read:

    think "恩！來讀點書吧！"

menu:

    think "看著書架上的書"

    "《神通及隱神通》":

        jump room_godtoon

    "《強者的故事，酒吞童子》":

        jump room_sake

    "《人類如何對抗妖怪》":

        jump room_huvsmo

label room_godtoon:

    think """
        
        《神通及隱神通》
        
        「隱神通，是由擁有神通力的妖怪們組成的組織」
        
        基本上能覺醒神通力的妖怪，通常代表其對前世的執念，
        
        然而執念與怨念會給予人魂無窮的力量，甚至獲得神通力，
        
        但即使是獲得神通力，也需要一定的修行方可運用自如。
        
        「隱神通也是不簡單吶…」

        神通力也包含了，
        
        能看透萬物的「{b}天眼通{/b}」，
        
        能以聽力探索世界的「{b}天耳通{/b}」，
        
        能準確判讀對方內心的「{b}他心通{/b}」，
        
        能在時空中穿梭的「{b}神足通{/b}」，
        
        能知曉因果業報的「{b}宿命通{/b}」，
        
        能解出所有疑惑的「{b}漏盡通{/b}」。
        
        ...
        
        這就是神通嗎？
        
        不管怎麼說，能力也太超規格了吧！
        
        但是能一個人壓制那些怪物的老爸也是不簡單吶...
        
    """

    me "差不多該睡覺了..."

    jump chap2_1

label room_sake:

    think """
    
        <<強者的故事，酒吞童子>>
        
        ...
        
        實在是對這本書沒什麼好感，
        
        但姑且還是讀一讀吧！
        
        「酒吞童子，妖界裡最強最帥氣的妖怪」
        
        「一個人擊退所有敵人」
        
        「登上妖界的寶座」
        
        「娶到世界上最漂亮的妻子」
        
        「走上世界的巔峰」
        
        後半段的內容幾乎都是跟老媽的愛情故事
        
        身為兩人孩子的我看得異常害臊
        
        這什麼鬼啊啊啊啊啊
        
        這什麼，這到底是什麼內容啊
        
        為什麼這種書可以出版？
        
        …
        
        「嗯…」
        
        大概就是某個極度仰慕我爸的傢伙寫的吧！
        
        從頭到尾被描述的異常帥氣啊！
        
        我突然好奇作者是誰
        
        翻到封面後
        
        「原來是老爸的自傳啊啊啊啊啊」
        
        「難怪可以出版，而且還意外暢銷」
        
        封面寫著第三次再版、動畫化、映畫化確定
        
        …這要我以後怎麼出去見人
    
    """

    me "差不多該睡覺了..."

    jump chap2_1

label room_huvsmo:

    think """

        感覺蠻實用的
        
        如果以後要繼承家業的話，戰鬥技能是必須的呢
        
        「人類在身體能力上是輸妖怪的」
        
        「但是人類在數量上有優勢，而且比起最自大的妖怪，人類很團結，並且會使用陷阱或武器」
        
        「所以對人類來說，會使用妖術和具有智慧的妖怪是最棘手的」
        
        「只有會使用氣功或手持法器的任人能夠與之抗衡」
        
        原來如此
        
        那我應該不用太擔心吧
        
        畢竟我應該是擁有智慧的
        
        嗯嗯
        
        不對啊，我的的妖力比一般妖怪弱很多誒
        
        一發功就頭痛
        
        可惡，這樣我不就是跟一般人差不多嗎？
    
    """

    if ask_to_be_strong:
        think "總之去問問老爸怎麼變強吧"
    
    me "差不多該睡覺了..."

    jump chap2_1

#打電話
label room_message:

    think "打開通訊錄"

    think "....."
    
menu:
    
    think "好了，要怎麼開頭呢？"

    "直接打電話過去":

        jump room_call

    "你覺得一個人的真心值多少錢":

        jump room_love

    "是我啦!我出車禍了，匯200萬給我":

        jump room_money


label room_call:

    think "「...」"

    me "好緊張啊..."

    think """
    
        根本沒跟女生講過多少次話，

        一上來就是高難度阿...。

        不知道我是著魔了還是怎樣，

        我還是硬著頭皮打過去。

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
        
        classmate "是被猴子的鬼魂詛咒了嗎？！"

        me "現在要我原諒妳，只要花699買下這個奇怪的壺"

        classmate "強迫推銷？"

        jump room_endcall

    "那我先掛了":

        me "..."

        jump room_endcall
    
label room_love:

    me "妳覺得一個人的真心值多少錢？"

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

    me "妳是惡魔吧！"

    jump room_end

label room_money:

    me "是我啦!我出車禍了，匯200萬給我"

    classmate "ㄟ？！真的嗎？我現在馬上匯！可以跟我說你的帳戶嗎？"

    me "ㄟ？！"

    think "我就如實跟她說吧"

    me "89346734"

    #轉場代表時間流逝
    with Fade(0.5, 1.0, 0.5, color="#000")

    classmate "好了"

    me "這種玩笑誰會......"

    think "一瞬間，我看到了手機的通知，看來我的帳戶裡有人匯了200萬給我"

    #獲得200萬(插入音效)
    $achievement.grant("獲得200萬")
    $renpy.notify("《獲得成就：獲得200萬》")

    me """
    
        耶！獲得兩桶金了！
    
        這兩桶就分別取名叫傑夫和約翰吧

        ...

        唉唉唉？？
    
    """

    classmate "你還好吧？"

    me "妳才還好吧？！"
    
    me "妳腦袋沒問題嗎？？！"

    classmate "真是失禮ㄟ！人家都資助你了！"

    me """
    
        ...

        總之我沒事，我只是鬧著玩的

        還有會這樣說的多半是詐騙啊！
        
    """

    classmate "那如果是真的怎麼辦？"

    me "嗚呃..."

    think "總覺得我的心像是被什麼東西狠狠的打穿了"

    me "我錢會還妳，還請妳不要這麼相信陌生人"

    #喪失200萬(插入音效)
    $achievement.grant("喪失200萬")
    $renpy.notify("《獲得成就：喪失200萬》")

    me "..."

    me "再見了傑夫...再見了約翰..."

    classmate "真搞不懂你到底在跟誰說話"

    jump room_end

label room_endcall:

    think "我受不了了，快找個藉口掛了吧！"

    me "抱歉吶！我突然想到我還沒洗澡，我先掛了"
    
    classmate "唉？那個......"

    jump room_end

label room_end:

    think "呼~真是累死我了跟女生講話原來這麼難啊，"

    think "差不多該睡覺了。"

    jump chap2_1
