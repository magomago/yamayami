label ayame4_A:
    
    #*aya_6a|６月２５日（ＭＯＮ）：あやめと鬼ごっこ
    
    scene bg school schoolyard
    with Fade(1, 0, 1)
    
    "なんとなく静かで広い場所が恋しくなったのでグラウンドにやって来た。"
    
    "ここなら誰にも邪魔されず心置きなく朝の空気と空を楽しむことが出来る。"
    
    "俺は校舎に続く階段の一段目に腰掛け、ぼー、っと広大な空を眺める。"
    
    scene bg bg_s00
    with Fade(1, 0, 1)
    
    "どこまでも続く空の世界で、いくつもの雲が果てしない旅を続けている。"
    
    "これを見たとき、雲と共に希望に満ちた旅をしているかのような気持ちになれる。"
    
    "それはちっぽけな枠にしがみついている俺たち人間には到底進むことの出来ない旅路だが、だからこそ空の旅を感じたときの喜びも大きい。"
    
    "若くしてこんな楽しみを知ることが出来たなんて、俺はなんて幸せ者なのだろう。"
    
    "と柄にもなく心の中で詩人を気取ってみた。実はそこまで大げさなことを想っているわけじゃない。"
    
    "だがこの景色を独り占めに出来て幸せなのは本当だ。"
    
    scene bg school schoolyard
    with Fade(1, 0, 1)
    
    show ayame aya_1_01
        
    ay "「あれあれ？センパイなにやってんスか？こんなとこで」"
    
    "突然、視界にあやめの顔のアップが映った。"
    
    #[qs]
    
    so "「うわっ」"
    
    "飛び上がって、反対向きで数歩階段を上り距離をとる。"
    
    so "「それはこっちのセリフだ。」"
    
    so "「なんでお前がここにいるんだよ」"
    
    ay "「あやめのクラスは体育ッスよ。」"
    
    ay "「でも今日はサボるつもりだったからあやめは着替えてないんスけどね」"
    
    so "「そうか。」"
    
    so "「俺のほうは授業が始まるまで一人の時間を過ごしに来ただけだ」"
    
    "そう説明している途中で、階段の上から足音や声が聞こえてくることに気がつく。"
    
    scene bg bg_a11
    with Fade(1, 0, 1)
    
    "振り返って階段を見上げる。"
    
    "体操服姿の女子が何人も階段を下りているところだった。"
    
    play sound "sound/se/se_002.ogg"
    
    scene bg school schoolyard
    with Fade(1, 0, 1)
    
    show ayame aya_1_02
    with dissolve
    
    ay "「またまた照れちゃって～！隠さなくてもいいッスよセンパイ～！」"
    
    so "「ぐえぇ！」"
    
    "背中を見せた隙を狙ってあやめがタックルを仕掛けて来た。"
    
    ay "{cps=*2}「ああ感激だなぁ！センパイがあやめの体操着姿を見たがっているなんて！それなら覗こうとせず最初から見たいと言ってくれれば二人っきりのときに{/cps}"
    
    ay "{cps=*2}「着替えてあげちゃうッスのに！でもセンパイは照れ屋だからあやめにはっきり言えないのもしょうがないかななんて思っちゃってだからセンパイが覗きに{/cps}"
    
    ay "{cps=*2}「走ったことは許してあげちゃおうと思ってむしろ逆に股とか胸のふくらみを楽しみに密かに悶々としているセンパイの姿を想像すると萌えちゃうッス！」{/cps}"
    
    so "「待て待て！そんな内容の妄想を大声で叫ぶなっ！」"
    
    "俺の頬に冷たい汗が流れた。"
    
    "今日の妄想はまずい。"
    
    "この場にとどまって会話をしていると、あやめのせいで俺の評判が非常に大変なことになってしまうかもしれない。"
    
    "万が一でも覗きと勘違いされてしまうと俺の楽しい高校生活が終了してしまう。"
    
    "それだけはなんとしても避けねばならない。"
    
    so "「俺を変態扱いするなっ！」"
    
    play sound "sound/se/se_003.ogg"
    
    hide ayame aya_1_02
    with dissolve
    
    "俺はあやめを突き飛ばすと即座に逃走を始めた。"
    
    ay "「センパ～イ！待ってくださいッス～！」"
    
    "その際に階段を上って校舎の方に逃げ込まなかったのは失敗だった。"
    
    play sound "sound/se/se_010.ogg"
    
    "あやめが追いかけて来た。"
    
    show ayame aya_1_02
    with dissolve
    
    ay "「何で逃げるんスか～？」"
    
    hide ayame aya_1_02
    with dissolve
    
    "全速力で走り続けているのに声と足音がぴたりと張り付いてくる。"
    
    "茂みに飛び込んで隠れる暇も今から階段を上る余裕もない。一瞬でも減速すれば捕まってしまうだろう。"
    
    "このままグラウンドを走り続けるしかない！"
    
    show ayame aya_1_02
    with dissolve
    
    play sound "sound/se/se_010.ogg"
    
    ay "「センパ～イ」"
    
    scene image "#000000"
    with Fade(1, 0, 1)
    
    "結局、一限目が始まるまでこの持久走は続き、俺は授業に遅刻して教室に戻ることになった。"
    
    jump main6_C # plo6.ks - *plo6_4

#;----------------------------------------------------------------------
label ayame4_B:

    #*aya_6b|６月２５日（ＭＯＮ）：にぎやかな昼食
    
    "まさか飲み物なしで弁当を食べるわけにはいかない。"
    
    "俺は食堂の自販機を目指して歩き出した。"
    
    scene bg bg_a09
    with Fade(1, 0, 1)
    
    "うちの高校の自販機は食堂に一台しか設置されていない。"
    
    "しかもそれは、今時珍しい当たりつきの自販機で、当たり外れの結果を待つ時間もかかることもあって、つまり昼休みになるといつも行列が出来てしまう。"
    
    "それはこの日も例外ではなく、俺はいつも通り待ち時間を食うことになった。"
    
    "行列に並び待つこと数分、ようやく俺の番が回ってきた。"
    
    play sound "sound/se/se_054.ogg"
    
    "お金を入れるとボタンが点灯。"
    
    "何を選ぶのか、などと考えている暇はない。お茶のボタンを押す。"
    
    "日本人ならばやはりお茶しかあるまい。"
    
    play sound "sound/se/se_052.ogg"
    
    "ゴトン、と取り出し口に缶が落ちて、直後にルーレットランプが回転を始める。"
    
    "結果が出る前にお茶の缶を取り出す。"
    
    "回転が徐々に減速していき……"
    
    "当たりの一つ手前で停止した。"
    
    "惜しいな。"
    
    "俺が表情に出さず悔しがっていると、背後に気配を感じた。"
    
    ay "「センパ～イ！あやめと一緒にお昼にしましょうッス～！」"
    
    "声が聞こえたときはもう遅かった。"
    
    #[quake time=500 hmax=20 vmax=20]
    
    play sound "sound/se/se_002.ogg"
    
    so "「うぐぉ！」"
    
    "背中に重たい衝撃を感じて、俺は自販機に体を叩きつけられていた。"
    
    "非常に派手でやかましい音が屋内に響き、食堂内に満ちた喧騒が一気に静まり返る。"
    
    show ayame aya_1_01
    with dissolve
    
    "俺は周囲を見回した。食堂内の人間が揃ってこちらを見ている。"
    
    "しかし音の発生源が俺とあやめだと確認すると、すぐに興味をなくした様子でおのおの元の会話と食事に戻っていく。"
    
    "首館あやめの存在は変わった女子の筆頭として校内中に知れ渡っている。多少おかしな行動をしていたとしても、ああまたこいつか。で済んでしまうのだ。"
    
    play sound "sound/se/se_052.ogg"
    
    "ゴトン、と自販機から缶が落ちた音がして、俺は振り返った。"
    
    "ランプが当たりの位置で停止していた。"
    
    "どうやら、俺がぶつかった衝撃で目盛りが一つ分ずれて当たりになったらしい。"
    
    show ayame aya_1_02
    
    #[quake time=500 hmax=20 vmax=20]
    
    play sound "sound/se/se_002.ogg"
    
    ay "「やったッスセンパイ～！あやめのおかげで当たりッス～！」"
    
    "あやめが俺の襟を掴んでがくがくと揺さぶる。"
    
    so "「お前と遭遇するというもっと大きなはずれくじを引いてしまったけどな」"
    
    ay "「さあ早くあやめと楽しいお昼ごはんッス！」"
    
    so "「わかったわかった、一緒に食べてやるから早く離れろ。待ってる人が迷惑だぞ」"
    
    "俺は自販機からもう一本のお茶を取り出して、あやめに手渡した。"
    
    scene bg bg_a16
    with Fade(1, 0, 1)
    
    "猫を掴むように首裏の襟を取られ、無理矢理引きずられて同じ食堂内のロングテーブルの前にやって来た。"
    
    "『雨宮センパイこんにちわぁ～！』"
    
    "そこで席に着いて食事中のあやめの友人三人組が一斉に挨拶してくれた。"
    
    so "「ああ、こんにちはＡＢＣさん、でいいのかな？」"
    
    "と友人ＡＢＣの向かい側の席に座り、弁当箱とお茶の缶を置いて挨拶を返す。"
    
    show ayame aya_1_07
    with dissolve
    
    ay "「ＡＢＣずるいッス！」"
    
    ay "「あやめが帰るまで待っててほしいって言ったはずッス！」"
    
    "あやめは俺の隣の椅子に座る。その椅子の前にはあやめの物らしき丸い弁当箱が最初から置かれている。"
    
    "友人Ａ" "「あはは、あやめお帰り～」"
    
    "友人Ｂ" "「早かったね～。自販機だとゼッタイ長くなると思ったから先に食べ始めちゃったよ～」"
    
    "友人Ｃ" "「センパイ誘って飲み物買ってくるの忘れたんじゃないの？」"
    
    show ayame aya_1_02
    
    ay "「ところがそうじゃないッス！」"
    
    ay "「センパイが当たりのジュースをあやめにプレゼントしてくれたんス！感激ッス！」"
    
    "あやめは嬉しそうにお茶の缶を両手で握り締め、ラテン音楽の楽器のように激しく振りまくる。"
    
    "友人Ａ" "「そういやさっき、当たりッス～。とか騒いでたね」"
    
    "友人Ｂ" "「ここまで聞こえてきたよ～、ばぁん、ってでっかい音までしてたし」"
    
    "友人Ｃ" "「そのうち迷惑行為とかで職員室に呼び出されちゃうかもよ～」"
    
    hide ayame aya_1_02
    with dissolve
    
    "俺はあやめとＡＢＣのやりとりを見物しながら、弁当の包みを外してふたを開ける。"
    
    "女の子四人に囲まれて食事をする。という状況は今までの人生の中ではこれが初めてだ。"
    
    "どう会話すればいいのかよくわからない。"
    
    "だからまずは、仲良しな女の子たちのやりとりでも見物して、静かに楽しんでおこう。"
    
    "と考えた矢先に、視界の端から、箸で掴まれた卵焼きが俺の口元まで運ばれて来た。"
    
    show ayame aya_1_02
    with dissolve
    
    ay "「はいセンパイ、あ～んしてほしいッス」"
    
    so "「……いやだ」"
    
    "と拒否するも、あやめはわずかに開いた俺の口のすき間から、卵焼きを強引にねじ込んで来た。"
    
    so "「……むぐっ」"
    
    "入ってしまった食べ物はしょうがないので、冷静によく噛んでから飲み込む。"
    
    "すると今度はウインナーを運んで来た。"
    
    "そんな様子を見て、ＡＢＣが笑う。"
    
    "友人Ａ" "「やっぱりあやめは強引だね～」"
    
    "友人Ｂ" "「雨宮センパイも落ち着いてますよね～、やっぱりずっとあやめにつきまとわれて平気な顔してるだけのことはありますよ」"
    
    "友人Ｃ" "「でもやりすぎちゃうとセンパイ怒っちゃうかもしれないよ～」"
    
    "談笑してないで止めてくれないかＡＢＣ。"
    
    show ayame aya_1_01
    
    ay "「どうッスかセンパイ？」"
    
    ay "「これあやめの手作りなんスよ。エンリョせずにもっと食べてほしいッス！」"
    
    "口を閉じたままにしても箸をどけてくれない。"
    
    "一緒に食べるとは約束したがお前の弁当を食べさせてくれとは言ってないからな。"

    "と思ったが説得しても聞いてくれないだろう。それ以前に、説得しようと口を開いた瞬間ウインナーを突っ込まれるのが目に見えている。"
    
    "仕方ない、最後の手段を使うか。"
    
    "俺はあえて口を開き、あやめの箸を迎え入れてウインナーをもぐもぐとする。"
    
    ay "「どうッスか？おいしいッスか？」"
    
    so "「ああ、美味い。お前意外と料理できたんだな」"
    
    show ayame aya_1_02
    
    "俺が褒めてやると、あやめは心底嬉しそうに満面の笑みを浮かべる。"
    
    so "「もっと食べたいな……あやめのお弁当」"
    
    "少しくさいセリフになってしまったが、あやめは何の疑問も持たずに早口で喋り始める。"
    
    ay "{cps=*2}「ああ感激だなぁ！センパイがあやめのお弁当をおいしいって言ってくれるなんて！いつものセンパイならきっと意地を張って口を開かなかったりするはず{/cps}"
    
    ay "{cps=*2}なのに今日はまるで恋人同士のように素直にあやめの作ったおかずを食べてくれてその上もっと食べたいなんて可愛くおねだりしてくるなんて！これはもはや{/cps}"
    
    ay "{cps=*2}恋人同士のようじゃなくって本当の恋人の関係にレベルアップしたって言うことッス！これからは毎日あやめの手作りのお弁当をセンパイに食べさせて{/cps}"
    
    ay "{cps=*2}あげられる至福の時間がやってきちゃうんスよねっ！」{/cps}"
    
    "あやめは妄想に浸り、次々と口の中におかずを突っ込んでいく。"
    
    "……それは俺の口じゃないけどな。"
    
    "様子を見ているＡＢＣが揃ってクスクスと声を出す。"
    
    "俺もその隣でにやにやしながら見物する。"
    
    show akira aki_1_02 at left
    show ayame aya_1_02 at right
    with dissolve
    
    ak "「いやいや～、あやめちゃん料理上手だったんだね～！嬉しいナァ～、これからは毎日俺のために手作り弁当を食べさせてくれるなんて～！」"
    
    "まるで十年も女の子と触れ合っていなかったかのように、幸せの絶頂を表した表情の明良がおかずをほおばり続けている。"
    
    "あやめはテンションが上がると何も見えなくなってしまう。"
    
    "それを利用して、いつの間にかＡＢＣの隣に座って非常にうらやましそうな目で俺を見つめている明良と入れ替わったのだ。"
    
    "飲み込むよりも早く次々とおかずが突っ込まれていき、口の中一杯におかずを詰め込まれて窒息寸前になりながらも、明良はまだ天国にいるみたいな顔をしている。"
    
    ay "「ああなんだかセンパイじゃないみたいッス！」"
    
    ay "「まるで顔や声も別人のような……ん？」"
    
    show akira aki_1_02 at left
    show ayame aya_1_02 at right
    
    ak "「女の子にフラレ続けた俺にもようやく春がやってきたんだなあ～！」"
    
    ay "「………………」"
    
    ak "「俺もセンパイとして男らしくならなくっちゃなあ～！」"
    
    show akira aki_1_02 at left
    show ayame aya_1_10 at right
    
    ay "「お前なんかセンパイじゃないッスー！」"
    
    #[quake time=500 hmax=20 vmax=20]
    
    hide akira aki_1_02
    hide ayame aya_1_10
    with dissolve
    
    play sound "sound/se/se_002.ogg"
    
    "ようやく気がついたあやめが明良の首を締めつける。"
    
    ak "「ぐええええええええっ！」"
    
    show ayame aya_1_03
    with dissolve
    
    ay "「吐き出せ～！」"
    
    ay "「せっかくセンパイのために用意したお弁当を返せッス～！」"
    
    "泣きそうな顔でがくがくと首を揺さぶる。"
    
    "『っぷ、あはははははははっ！』"
    
    "笑いをこらえて眺めていた俺とＡＢＣがついに耐え切れなくなって吹き出した。"
    
    "実に楽しい昼食になった。"
    
    jump ayame5 # a_01.ks - Top
