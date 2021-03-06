label main4:
    jump main4_A

label main4_A:
    
    #*plo4|６月１７日（ＳＵＮ）：休日の過ごし方
    
    #@day nowday='６月１７日（ＳＵＮ）'
    
    play music "sound/bgm/bgm_003.ogg"
    
    scene bg bg_b00
    with Fade(1, 0, 1)
    
    play sound "sound/se/se_061.ogg"
    
    "ジリリリリリリリリリリ！！！"
    
    "けたたましいベルの音が鳴り、俺は目を覚ます。"
    
    "その音を止めようと、手探りで時計を探す。"
    
    "俺の朝は、よくあるラブコメみたいに幼なじみとか妹とかが起こしに来てくれるような展開ではない。"
    
    "ごくごく普通の、五月蠅い目覚ましが鳴るだけである。"
    
    "時計を引っ掴み、アラームを切り、時間を確認する。"
    
    "時計の針は、いつも学校へ行くために設定しているのと同じ時間。"
    
    "あれ？昨日は土曜日だったよな……。"
    
    "嗚呼、こんな休日に限ってアラーム設定を消し忘れるとは……。"
    
    "俺は、昨日ちゃんと確認せず寝たことを後悔しながら、ベルを止めてもう一度枕に顔を埋める。"
    
    "しかし、しばらくそうしていても寝られない。"
    
    "窓の外からは雨の音だけが静かに響き、曇天であるために寝やすい環境ではあるのだが、どうにも二度寝出来ない。"
    
    "こんな日に限って、何となく目が覚めてしまったり、下らぬ思考を巡らせてしまったりして、脳が活性化してしまう。"
    
    "まぁ、良くあることなのだが。"
    
    "仕方なく、俺は布団から出ることにした。といっても、別段やることもないので、放ってあった漫画のページを捲る程度の活動しかしない。"
    
    "まだしとねも起きていないらしく、家の中は至って静かだ。"
    
    "雨の音だけが、静かに鼓膜を打つ。"
    
    "さて、これからどうしようか。"
    
    menu:
        "しとねを起こしてみる":
            $ loveSi += 1
            jump sitone2
            
        "雨だが散歩してみる":
            $ loveMi += 1
            jump misogi2
            
        "めんどくさいので何もしない":
            jump main4_A_1

label main4_A_1:
    
    "……とりあえずあれこれ思考を廻らせてみたが、結構時間も早いので、空いてる店も少なく、行く宛も無いという結論に辿りつく。"
    
    "そういうことで、俺はもう一度ベッドに横になり布団をかぶった。"
    
    scene bg bg_b00
    with Fade(1, 1, .8)
    
    "…………"
    
    "朝食を摂っていない栄養不足の脳で思考を巡らせた所為か、また睡魔が襲ってきて、結局昼まで寝てしまった。"
    
    "とりあえず、それ以上寝ると時間が勿体無いので、起きることにする。"
    
    "さぁ、最初に何をするかな。"
    
    menu:
        "携帯の電源をつける":
            $ loveAy += 1
            jump ayame2 # aya_4.ks - Top
            
        "テレビをつける":
            $ loveKi += 1
            jump kiriko2_A # ki_4.ks - Top

label main4_B:
    
    #*plo4_3|６月１７日（ＳＵＮ）：休日の過ごし方（２）
    
    play music "sound/bgm/bgm_001.ogg"
    
    scene bg bg_b00
    with Fade(1, 0, 1)
    
    "明日からまた学校か。１週間も学業に勤しまねばならんとは苦痛だ。"
    
    so "「テレビでもつけてみるか」"
    
    "別段やることも無く、徐にテレビをつけるが、やはり面白いものはない。"
    
    "あ、予習してないな。"
    
    so "「うぁ……こりゃ結構な量だな」"
    
    "今の今まで宿題などを忘れていた。これは今晩きつくなりそうだ。"
    
    "と言うわけで、俺は宿題に追われ、結局眠りについたのは日付が変わってからだった。"
    
    if f_kiriko_4==1:
        jump kiriko2_B # ki_4.ks - *ki_4z
    
    jump main5 # plo5.ks - Top
