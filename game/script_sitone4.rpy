label sitone4:
    jump sitone4_A

label sitone4_A:
    #*si_6a|６月２５日（ＭＯＮ）：しとね作成
    
    so "「まあ、やってみてもいいかな」"
    
    si "「本当！？じゃあこっち来てよ！」"
    
    "実にうれしそうだから、指を切り落とさない程度に頑張ろうという気になった。"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    so "「それで、俺に何をしろというんだ？俺は麺類なら作れるとか、そういう設定とは縁遠い存在だぞ」"
    
    show sitone si_2_01
    
    si "「何のこと？とりあえず簡単でもいいから自分で作ってみると美味しく感じられていいと思うんだよ」"
    
    so "「ほほう。そこまで言うならやってみよう。それで、何から手伝えばいいんだ？」"
    
    si "「じゃあとりあえず、その大根を全部桂剥きにしておいてくれるかな？」"
    
    so "「ちょ、山岡さん！」"
    
    show sitone si_2_02
    
    si "「ふふっ、もちろん冗談だからまずはそこに切ってある野菜をお皿に盛り付けてくれる？」"
    
    so "「そうします」"
    
    "ここで余計な軽口を叩いて桂剥きに挑むことになると、兄の威厳が粉砕！玉砕！大喝采ー！！しかねないので、波風立てないよう大人しく従う。"
    
    "……"
    
    so "「しとねさん、出来上がりましたが。というかよく考えると、これは弁当じゃなく朝食の手伝いですよね？」"
    
    show sitone si_2_01
    
    si "「うん、ひとまず一番簡単な手伝いからの方がいいかなと思ったから」"
    
    so "「まあそのとおりだ。だがしかし、このぐらいの事なら肉をウルトラ上手に焼くスキルが無くても余裕に過ぎますぜ」"
    
    si "「まあそうだよね。じゃあ次はそっちのソースに漬けてある豚肉を適当に焼いちゃってみて」"
    
    so "「いきなりハードルを上げてきたね。だがしかしこの俺も家庭科で４をもらっている以上、これくらいの事はやり遂げて見せましょう」"
    
    "そう言って俺は豚肉が並べられた皿を持ちフライパンと相対する。"
    
    "豚肉は程よくソースがなじんでいて、このままでも十分うまそうに見える。"
    
    "小さいのを摘んでみよう……パクッとな。"
    
    "少ししょっぱいかな。"
    
    show sitone si_2_05
    
    si "「お兄ちゃん！何してるの！？」"
    
    "それを目にしたしとねがすごい剣幕で飛んできた。"
    
    so "「いやちょっと味を見ようかと……」"
    
    show sitone si_2_04
    
    si "「生の豚肉には、寄生虫がいるかもしれないんだよ！？何でそんなものを考えもなしに食べちゃうの！」"
    
    so "「あー、そう言われればそんな話を聞いたことが……」"
    
    si "「最近の豚は安全管理をしっかりとしているから必ず危険だというわけではないかもしれないけど、生で食べるべきでないものを食べるなんて自分から危険に踏み込むような真似は百害あって一利無しだから絶対にやめてよね！」"
    
    so "「……はい、本当にすみません」"
    
    "その後もしとねに説教を受け、豚肉を焼く役割も解かれ皿を食卓に並べる単純作業に従事することにした。"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    "朝食を終えた後も、腹の調子に変わり映えは無かったので、これ以上しとねに説教されずに済むよう、少し早くはあったが学校へ向かうことにした。"
    
    jump main6_B # plo6.ks - *plo6_3

#;-------------------------------------------------------------
label sitone4_B:

    #*si_6b|６月２５日（ＭＯＮ）：しとねデリバリー
    
    "突然気付いたことがある。"
    
    "弁当がない。"
    
    "後から思うと今日のかばんはいつもより軽かったなーとか思うんだが、きっかけがない限りそうそう思い出すことはないぼくらがここにいるふしぎ。"
    
    "考えてても始まらないので、しとねに助けを求める。"
    
    play sound "sound/se/se_080.ogg" #[ws canskip=true]

    "ガチャ"
    
    play sound "sound/se/se_081.ogg"
    
    si "『おにいちゃん、どうしたのいきなり？』"
    
    so "『しとね、今どの辺にいる？』"
    
    si "『え？  家の前の通りだけど……』"
    
    so "『スパシーバ。実は弁当を忘れたので取りにいって高校に持ってきてくれると、狂いもだえます、喜びで』"
    
    si "『え～！珍しく早起きしたと思ったらなにやってんのおにいちゃん！』"
    
    so "『ええ、早起きとの因果関係は不明ですがおおむねそのような状況ですので、私も出来るだけそちらに向かいますから取りに戻っていただけないでしょうか』"
    
    si "『も～しょうがないな！遅刻したら責任とってもらうからね！』"
    
    "ガチャ"
    
    play sound "sound/se/se_081.ogg"
    
    "実に良く出来た妹だ。あれならこの先生きのこることもできるだろう。"
    
    "そしてこれ以上迷惑をかけないようにさっさと通学路を逆行しよう。"
    
    scene bg school staircase
    with Fade(1, 0, 1)
    
    scene bg school shoebox
    with Fade(1, 0, 1)
    
    scene bg school gate
    with Fade(1, 0, 1)
    
    scene bg bg_e00
    with Fade(1, 0, 1)
    
    "……ふう疲れた。"
    
    "さすがに流れに逆行して走るのはなかなか恥ずかしい。"
    
    "見知った人間を何度か見かけたような気がしたが、まあ特に問題はないだろう。"
    
    so "「お……？」"
    
    "僕と地平線の狭間にしとねらしきピンク色が。"
    
    "よく考えたら学校の位置は大して変わらないからここまで来る必要はあまりなかった気がするが、まあ誠実な対応というやつだ。"
    
    so "「お姉ちゃんありがとう！授業中に空腹を紛らわすために寝たりせずに済むよ！」"
    
    show sitone si_2_04
    with dissolve
    
    si "「も～、忘れ物はもっと早く気付いてよおにいちゃん」"
    
    so "「あー……本当にすまん」"
    
    show sitone si_2_02a
    
    si "「まあまだ間に合う頃合でよかったよ。それよりももうそろそろ急がないとＨＲに間に合わないよ？」"
    
    so "「そうだな、急ぐぞしとね！」"
    
    "そう言ってしとねの手をとって走り出した。当然ながらもう片方の手には弁当箱だ。"
    
    show sitone si_2_06
    
    si "「えっ！ちょちょっとおにいちゃん！！」"
    
    "当然しとねは慌てたが、結局諦めて揃って学校へと走ることになった。"
    
    "なぜこんなことをするようなテンションになったかは不明だが、たまにはこんなことをしてもいいんじゃないかという気分になったのは確かだ。"
    
    "しとねは当然ながらずっと顔を赤らめて走っていたが、まあ間に合ったのでよしとしよう。"
    
    $ f_sitone_6 = 1
    
    jump main6_C #plo6.ks - *plo6_4

#;-----------------------------------------------------------
label sitone4_C:

    #*si_6c|６月２５日（ＭＯＮ）：しとね電話
    
    "このところ梅雨ということで雨の降っていない日は珍しいから昼食は屋上で食べてみるか。"
    
    "明良に見つかると面倒なのでこっそりと弁当を持って出て行く。"
    
    scene bg school passage
    with Fade(1, 0, 1)
    
    "廊下に出ると、学食に向かう生徒が雨後の竹の子よろしく目に付く。"
    
    "こういうあたかも大衆は上り線でみっしりと敷き詰められてるのを尻目に下り線で優雅に座って登校するようなとき本当に幸せだと感じる。"
    
    "そりゃあ巨神兵も口からオプティックブラストを出すというものだ。"
    
    #[bg_cs sto=black]
    
    scene bg school staircase
    with Fade(1, 1, 1)
    
    play sound "sound/se/se_031.ogg"
    
    scene image "#FFFFFF"
    with Fade(0.5, 2, 1)
    
    #[wait time=500]
    
    scene bg bg_a14
    with Fade(0, 0, 1)
    
    "晴れた日は電波がよく届くそうだ。そしてあっという間にバッドエンドを迎えるそうだ。"
    
    "見たところまだ誰も屋上には見当たらない。"
    
    "せっかくだから赤いベンチを選んで座る。"
    
    "そして弁当箱を開ける前に携帯を確認する。ついでにしとねに謝罪しておくのがいいと思い、メールを送ることにした。"
    
    so "『朝は大変お世話になりました。これからもよろしくお願い申し上げます』"
    
    "弁当を食べながら返信を待つ。"
    
    "程なくして携帯が光る。"
    
    si "『本当だよ！せっかく作ったんだからしっかりしてよね！』"
    
    "そして返信を考える間もなくもう１通。"
    
    si "『しかも、あんな風に通学路を走ってるのを皆に見られちゃって本当に恥ずかしかったんだからね！！』"
    
    si "『それに急げば間に合わない時間でもなかったし、そもそも普通に走った方が速いでしょ！』"
    
    "まったくもってそのとおりだ。"
    
    so "『さあ……、そこんとこだが、おれにもようわからん』"
    
    "皆が見ていなかったら構わなかったのかと突っ込んでみたくもあったが、危ない橋を渡るのはよしておいた。"
    
    si "『まったくもう！見られたクラスの子にからかわれるし、すっごく不当な気分を味わってるんだよ！』"
    
    "うむ。今回はこれ以上ボケず取り成しに専念した方が身のためのようだ。"
    
    so "『いや本当にごめんなさい。今度アーバレスト買ってきますので、どうかご寛恕のほどを』"
    
    "反省の意味無し。どうしたものか俺。"
    
    si "『アーバレストって何？』"
    
    "そうですね。現在はレーバテインだとかそういう以前の根本的な認識の食い違いがありますよね。"
    
    so "『まあ言葉の綾だから気にするな。もしくは意識を逸らせて機嫌を直すよう働きかけたと思ってくれても構いません。というかそろそろ勘弁してください』"
    
    si "『まあ……今更騒いでどうこうなるものでもないから、別にいいんだけどね……』"
    
    "何とかなだめきれた。アーバレスト万歳。"
    
    so "『まあこの件で被った精神的苦痛についてはいずれ償うこともあろうと思うので、その方向でよろしく』"
    
    "さすがに繊細な作業中には食事をとる余裕がないために弁当がほぼ手付かずであるので、話に決着をつけようと試みる。"
    
    si "『本当？その場しのぎの口約束に見えるけど、一応期待しておくよ』"
    
    "そうして朝の件は決着に至り、俺は安心して昼食に取り掛かれるようになった。"
    
    "……とはいえ、しとねの言うとおりなんとなく勢いで言ったことなので、一体何をすれば埋め合わせになるかはさっぱり考えてない。"
    
    "とりあえず、次しとねと顔を合わせるまでに何らかの方向性を定めておく必要があるだろう。"
    
    so "「そういえば、祭りがあったか」"
    
    "今週の金曜日は、毎年雨に降られている気の毒な祭が催されることになっている。"
    
    "どうせ明良ぐらいしか一緒に行く当てがなかったから、それならばしとねと祭に行って何か買ってやることにすれば、実に有意義なことになるんじゃないだろうか。"
    
    "とりあえず帰ったらしとねにその辺りの事を聞いてみることにしよう。"
    
    "弁当を食べ終えたところに明良からどこにいるのか尋ねるメールがきたので、教室に戻ることにした。"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    mi "「あっ、聡介くん」"
    
    show misogi mi_1_06a
    with dissolve
    
    "教室に入るとみそぎがこちらに駆け寄ってきた。"
    
    mi "「お昼休みの間どこに行ってたの？授業終わってすぐに見当たらなかったから心配しちゃった」"
    
    "どうやらみそぎには早々とばれていたようだ。"
    
    so "「いや、久々に雨も降ってなかったし、屋上で弁当を食べてきたんだ」"
    
    mi "「そうだったんだ……、言っ――」"
    
    show akira aki_1_08 at left
    show misogi mi_1_06a at right
    with dissolve
    
    ak "「おいおい、この明良お兄さんに声もかけずにどっかへ行っちまうなんて冷てー男だな！」"
    
    "みそぎが何か言いかけてたが、明良の登場によってかき消された。"
    
    show akira aki_1_08 at left
    show misogi mi_1_03 at right
    
    so "「いやまあ、なんとなく屋上に行きたくてな。特に面白いことでもないから声はかけなかったんだ」"
    
    show akira aki_1_07 at left
    show misogi mi_1_03 at right
    
    ak "「全くこれだから最近の若いもんは……。お前みたいな友達甲斐のない奴がＱ３３ＮＹを世界貿易センタービルの住所だとか言い出すんだよ！」"
    
    so "「驚くほど無関係なたとえだな」"
    
    show akira aki_1_04 at left
    show misogi mi_1_03 at right
    
    ak "「それに見ろ！みそぎちゃんだってお前の振る舞いに困ってこんな憂い顔になっちまってるんだぞ！」"
    
    ak "「その憂いを帯びた表情も実に可愛いくて堪らないけど、みそぎちゃんも何か言いたいことがあるなら言ってやるといいさ！」"
    
    show akira aki_1_04 at left
    show misogi mi_1_01 at right
    
    mi "「ううん、明良君が早くどこか行って欲しいなと思ってただけだから、聡介くんは別に悪くないよ」"
    
    show akira aki_1_09 at left
    show misogi mi_1_01 at right
    
    play sound "sound/se/se_110.ogg"
    
    "冗談に聞こえないぐらい直球だった。"
    
    "まあこんな風に突然明るくなったみそぎと話すことは面白くもあったし、最初何を言いかけたのかも気にはなったが、午後の授業が始まるので席に戻ることにした。"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    so "「ふぁ～あ……」"
    
    "心地よい睡眠と共に授業とＨＲが終わった。"
    
    "しとねに祭の予定を聞く必要もあるし、今日はさっさと家に帰るとするか。"
    
    show akira aki_1_02
    with dissolve
    
    ak "「聡介ー、今日はゲーセンでも寄ってくか？」"
    
    "すぐさま明良が近づいてくる。"
    
    "ふと気付くと、俺は友達が少ないような気がしてきた。"
    
    "まあ、そんなことどうでもいいんですけどね。"
    
    so "「今日は気分が乗らないのでパスする。他にいい相手を見つけてくれ」"
    
    show akira aki_1_08
    
    ak "「なんだってんだよー、桃園の誓いを結んだ仲だってのに最近付き合い悪いじゃねーか」"
    
    so "「義兄弟になるには一人少ないと思うが、悪いが今日はちょっとやることがあるのでパスさせてもらう」"
    
    show akira aki_1_07
    
    ak "「ちぇっ、しょうがねえな。じゃあこっちはこっちで何とかするからとりあえず校門までは一緒に行こうぜ」"
    
    so "「ああ、じゃあ行くか」"
    
    "こういうときの引き際は心得たものなんだが、女子と接するときはどうしてあんなに三枚目なんだろうか。"
    
    #[tl sto= le=-120]
    #[wait time=200]
    #[tle]
    
    show misogi mi_1_03 at left
    with dissolve
    
    hide misogi mi_1_03
    with dissolve
    
    so "「ん？」"
    
    show akira aki_1_01
    
    ak "「ん？」"
    
    so "「いんや、なんでもない」"
    
    "みそぎがこっちを見てたような気がしたが、教室から出ていってしまったので、まあ用があったわけではないのだろう。"
    
    so "「じゃあ行くか」"
    
    scene bg school gate
    with Fade(1, 0, 1)
    
    "そうして無駄口を叩きつつ校門まで来たところで明良と別れて、俺は家路を辿ることとなった。"
    
    scene bg bg_b01
    with Fade(1, 0, 1)
    
    so "「ただいまー」"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    show sitone si_2_01
    with dissolve
    
    si "「あ、おかえり」"
    
    "しとねが普通に声をかけてきた。これこそ昼休みに行った根回しの所産というものだろう。"
    
    so "「ところでしとねさんや」"
    
    show sitone si_2_09
    
    si "「ん？」"
    
    so "「祭に俺と一緒に行くつもりがあったりしないか？」"
    
    "とりあえず単刀直入に聞いてみる。"
    
    si "「えっ？どうしたの藪から棒に？」"
    
    so "「まあ、昼に言った埋め合わせとして祭で何かするのがいいんじゃないかなと思ってさ」"
    
    show sitone si_2_05
    
    si "「うわ珍しい。おにいちゃんが約束を覚えてるなんて」"
    
    so "「おいおい、俺はちゃんと有言実行の男として各方面から高い評価を受けてますよ？」"
    
    show sitone si_2_07
    
    si "「うん、そう……だよね」"
    
    so "「？」"
    
    "ここは笑うところだったんだが、何か俯いてしまった。"
    
    show sitone si_2_01
    
    si "「あ、お祭は特に誰とも約束してないからおにいちゃんと一緒に行くよ」"
    
    so "「そ、そうか。分かった……」"
    
    show sitone si_2_09
    
    si "「？　どうかしたの？」"
    
    so "「ああ、いや何でもない」"
    
    "俯いたと思ったらごく普通の反応だったので、さっきのは特に気にする必要はないことなのだろう。"
    
    hide sitone si_2_09
    with dissolve
    
    "そんなこんなで祭をしとねと一緒に行く予定も決まり、何事もなく一日は終わりを告げた。"
    
    jump ToDo # s_01.ks - Top