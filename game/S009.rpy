#「二人の仲直り」

label S009:
$ save_name = "◇二人の仲直り"


#※璃紗視点に戻ります

#**新校舎廊下・昼
scene bg bg05a
with dis



#mes on
#system on


#♂MP08
play music "sound/BGM08.ogg"


show char tri03s2
with dis



voice "Risa_0209"
r "「………………ふうっ、もう……」"
"美夜はいつまでたっても、怒ったまま。"
"もうこれ以上、私に何が出来るのかしら？"
voice "Risa_0210"
r "「何とか理解してもらうよう、努力は続けるけど……今の美夜、あまりにポンコツすぎるし」"
"七海さんは言い過ぎだって言うけれど。"
"ここ数日の美夜は、どう見たってポンコツとしか言いようがない。"


show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Rikka_0169"
rk "「リサ姉～！」"

hide char trk01s2 at left
hide char tsy01s2 at right as r
show char tri01s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Risa_0211"
r "「あれは……六夏と沙雪さん？」"
"２人一緒にいるところなんて、ベストカップルの顔合わせ以来だわ。"
"ずっと沈みがちだった六夏の顔が、今日はなんか明るい……それだけじゃなくて、なんか赤らんでも見えるけれど。"
"一体、何があったのかしら……？"
voice "Sayuki0062"
s "「璃紗さま、ごきげんよう」"
voice "Risa_0212"
r "「ごきげんよう。今日は２人で、どうしたの？」"


show char trk02s2
with dis



voice "Rikka_0170"
rk "「今まで迷惑かけたお詫びと、報告をしに来たんです」"
voice "Risa_0213"
r "「報告、って……」"
"六夏は本当に嬉しそうに、私に言った。"


show char trk03s2
with dis



voice "Rikka_0171"
rk "「今回はいっぱい、ご迷惑をおかけして……ゴメンなさい」"
voice "Sayuki0063"
s "「美夜さまの件に関しまして、おそらくもう、誤解は解けたと思います」"


show char tri04s2 at sleft as l
with dis



voice "Risa_0214"
r "「えっ……本当に？」"


show char trk05s2
with dis



voice "Rikka_0172"
rk "「はい。ワタシ……というか、沙雪さんのおかげで、わかってもらえました」"
"ちょっと恥ずかしそうに、そして小さく、六夏は微笑んだ。"
"こんな表情の六夏、初めて見たかもしれない……"
"まるで、恋する少女の……"


show char trk03s2
with dis



voice "Rikka_0173"
rk "「……リサ姉？」"


show char tri01s2 at sleft as l
with dis



voice "Risa_0215"
r "「あっ、うん……そうなの、美夜がわかってくれたのね……ありがとう、２人とも」"
"それを聞いたら、ボーっとなんかしていられないわ。"
"すぐにでも、美夜に会いたい……"
voice "Risa_0216"
r "「本当にありがとう、じゃあまたね」"


#allClear:
hide char tri01s2 at sleft as l
hide char trk03s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg05a
with dis


"私はすぐさま、美夜のいる所へ――アトリエへと向かった。"


#**暗転
#allClear:
#lastBG:
#scene bg bg05a
scene black
with Dis


voice "Risa_0217"
r "「はぁ、はぁ……美夜、入るわよ」"
"最近、美夜はずっと、アトリエに姿を見せなかったけれど。"
"今日は必ずいると、確信していた。"


#**アトリエ・昼
scene bg bg29a
with dis



"ドアを開けると、そこには静かに外を見てたたずむ、美夜がいた。"


show char tri01s2
with dis


voice "Risa_0218"
r "「美夜……ここで会うの久しぶりね」"


show char tmi03s2 at left
show char tri01s2 at right as r
with dis



voice "Miya_0136"
m "「………………」"
voice "Risa_0219"
r "「あの、六夏から聞いたわよ……もう分かってくれたのよね、怒ってないんでしょ？」"
voice "Miya_0137"
m "「………………」"
"今までのことが照れくさいのか、美夜は私の顔を見てくれず、そっぽを向いたままだった。"
"でも……昨日までとは違って、ちゃんと私の話を聞いてくれているのはわかる。"
"だから返事がなくても、私は喋り続けた。"
"すると美夜はようやく、その重い口を開いた。"
voice "Miya_0138"
m "「……ごめんなさい、璃紗」"
voice "Risa_0220"
r "「んっ？　なんて言ったの、美夜」"
voice "Miya_0139"
m "「だから、その……ずっと勘違いしていて、ごめんなさい」"


show char tri02s2 at right as r
with dis



voice "Risa_0221"
r "「そうね……ふふふっ、本当にものすごい勘違いだったわよ」"
voice "Miya_0140"
m "「今回ばかりは、わたくしも反省しているわ」"
"殊勝な態度の美夜って、なんだかすごく珍しいかも。"
voice "Miya_0141"
m "「そうね……自分への自信のなさが、こんな結果を招いてしまったのね」"


show char tri03s2 at right as r
with dis



voice "Risa_0222"
r "「そ、そうなの？？」"
voice "Miya_0142"
m "「璃紗……どうしたの、震えているの？」"
voice "Risa_0223"
r "「それは……ククッ、今日は、ちょっと寒くて……」"
voice "Miya_0143"
m "「もう、初夏なのに……」"
"私は必死に、震えるのを堪えていた……笑ってしまわないように。"
"だって超自信家な美夜が、こんなことを言うんだもの。"
"笑いを堪えるのに、とにかく必死だった。"
voice "Miya_0144"
m "「わたくし、これからはもっと璃紗を信じて、みんなの話にも耳を傾けるわ」"


show char tri01s2 at right as r
with dis



voice "Risa_0224"
r "「美夜……」"
"今回の件は、さすがの美夜も、かなり堪えたのね。"
"美夜の悪いクセ……周りに興味を持たなかったり、人の話を聞かなかったり……が、これで直ってくれるなら。"
"それはすごく、いいことだと思う。"
"ああ……人ってこうやって、成長していくのね。"
voice "Risa_0225"
r "「それじゃ美夜、これで私たち……無事、仲直りよね？」"


show char tmi08s2 at left
with dis



voice "Miya_0145"
m "「……いいえ、まだよ！！」"


show char tri04s2 at right as r
with dis



voice "Risa_0226"
r "「えぇっ！？」"
"び、びっくりした……急に大声だすんだもの。"


show char tri03s2 at right as r
with dis



voice "Risa_0227"
r "「どうしたの、美夜？」"
voice "Miya_0146"
m "「今回は確かに、わたくしが悪かったわ」"
voice "Risa_0228"
r "「じゃ、じゃあ……」"
voice "Miya_0147"
m "「それはよーくわかっているけど、璃紗にだって責任の一端があるわ」"
voice "Risa_0229"
r "「わ、私にも……？」"
"そんな……私は別に、何もしてないじゃない。"
voice "Risa_0230"
r "「ちょっと、理由を教えてよ」"
voice "Miya_0148"
m "「理由……そうね、じゃあ言ってあげるわ」"
"さっきまでおとなしかった、美夜……負けず嫌いな彼女の反撃が、始まろうとしていた。"


show char tmi01s2 at left
with dis



voice "Miya_0149"
m "「今年の春休み、本当に充実していたわよね」"
voice "Risa_0231"
r "「う、うん……」"
voice "Miya_0150"
m "「一緒に遊園地に行ったり、一緒にスカイシティに行って泳いだり」"


show char tri01s2 at right as r
with dis



voice "Risa_0232"
r "「そうね……楽しかったわ」"


show char tmi02s2 at left
with dis



voice "Miya_0151"
m "「プールでは璃紗、お約束のポロリもやってくれたわ{image=image/exch001.png}」"


show char tri05s2 at right as r
with dis



voice "Risa_0233"
r "「うううっ……変なこと、思い出さないでよ」"
voice "Miya_0152"
m "「その後……シャワー室で、激しく愛し合ったり……ね」"
voice "Risa_0234"
r "「わわわっ……それは、もういいから……」"
voice "Miya_0153"
m "「わたくしが予約しておいた、ホテルでも……璃紗は大胆にイブニングドレスを脱いで……」"
voice "Risa_0235"
r "「だから……ああ、もういいって……恥ずかしい」"
"いくら周りに誰もいないアトリエだからって、美夜の発言は大胆過ぎる。"
voice "Risa_0236"
r "「とにかく、楽しい春休みだったわよね……」"


show char tmi01s2 at left
with dis



voice "Miya_0154"
m "「そして、この間のＧＷ……」"


show char tri01s2 at right as r
with dis



voice "Risa_0237"
r "「美夜の別荘に行った時ね」"
"今年のＧＷは、別荘で過ごすって言っていた美夜に、私が着いて行っちゃったのよね。"
"美夜はまったり、読書を楽しんで。"
"私はそんな美夜の身の周りの世話をしたりして、穏やかな時間が過ごせたわ。"
"美夜の子供の頃の話も聞けたりして、新たな美夜の魅力を知ったのよね……"
"あれで何だか、ますます２人の距離が近づいたような。"
"そんな素敵なＧＷだったわ。"


show char tri02s2 at right as r
with dis



voice "Risa_0238"
r "「全部、本当に楽しかった……」"
"楽しい思い出が、次から次へと溢れてくる。"
"しかしほのぼの感慨に浸っていた私とは対照的に、美夜は何故かギラギラと燃え上がっていた。"


show char tmi08s2 at left
with dis



voice "Miya_0155"
m "「そうよ……あんなにも、ラブラブな日々を過ごしたのに……」"


show char tri03s2 at right as r
with dis



voice "Risa_0239"
r "「……えっ？」"
voice "Miya_0156"
m "「最近の璃紗といえば……」"
voice "Risa_0240c"
r "「ど、どういうことよ？　別に今だって……らららら～♪」"
voice "Miya_0157"
m "「こんな時に、のんきに歌なんて……」"


show char tri05s2 at right as r
with dis



voice "Risa_0241b"
r "「違うわよ……ららら～♪　ラブラブな日々じゃない」"
"自分たちのことラブラブだなんて……真面目な顔で言えっこない、だからつい、歌ってしまったわ。"
voice "Miya_0158"
m "「いいえ、ダメよ。こんなのラブラブじゃないわ」"


show char tri03s2 at right as r
with dis



voice "Risa_0242"
r "「美夜……」"
"私は何があっても、ずっと美夜が好きなのに……もしかして。"
"やっぱり、まだ言葉が足りないのかしら。"
"言葉でもっと『好き』とか『愛している』とか……言わないといけないってことなの？"

#//（以下妄想）
show char moyan as c
show char tmi01s2 at left
show char tri02s2 at right as r
with Dis



voice "Risa_0243"
r "「美夜……好き好き大好き、世界で一番愛してる{image=image/exch001.png}」"
voice "Miya_0159"
m "「璃紗、ありがとう……でももっと、言ってほしいわ」"
voice "Risa_0244"
r "「ええ、何度だって言うわよ……好き、好きっ」"
voice "Miya_0160"
m "「あと１００万回、言って」"
voice "Risa_0245"
r "「わかったわ、１００万回でも１０００万回でも言うわ。美夜が好き好き～～～っ」"

#//（妄想終了）
#allClear:
hide char moyan as c
hide char tmi01s2 at left
hide char tri02s2 at right as r
with dis
#lastBG:
#scene bg bg29a
show char tmi08s2 at left
show char tri05s2 at right as r
with dis



voice "Risa_0246"
r "「……って、ないわ。これは恥ずかしすぎる」"
"だいたい１００万回って、いちいち数えられないじゃない。"
voice "Risa_0247"
r "「頑張って、１０回かなぁ……でも、それでもかなり恥ずかしい」"
voice "Miya_0161"
m "「何をブツブツ言ってるの、璃紗？」"


show char tri03s2 at right as r
with dis



voice "Risa_0248b"
r "「な、なんでもないわよ……コホン」"
voice "Miya_0162"
m "「そう……だったら話の続きよ。最近の璃紗ときたら……」"
"言葉で愛を表現しない……とか、言うのかな？"
voice "Miya_0163"
m "「委員会が忙しい、とか……」"
voice "Risa_0249"
r "「へっ？」"
voice "Miya_0164"
m "「テスト勉強が忙しい、とか……」"
voice "Risa_0250"
r "「それは、その……いつものことじゃない」"
voice "Miya_0165"
m "「違うわよ。そんな理由で、エッチが週にたった３回しかないじゃない」"


show char tri04s2 at right as r
with dis



voice "Risa_0251"
r "「ええええっ！」"
voice "Miya_0166"
m "「こんなに少ないなんて……恋人として、ありえないわよ」"


show char tri09s2 at right as r
with dis



voice "Risa_0252"
r "「じゅ、十分に多いわよ！」"
"美夜ったら、もう……それが理由だったの？"
voice "Miya_0167"
m "「少ないわ……絶対、少ないわよ」"


show char tri03s2 at right as r
with dis



voice "Risa_0253"
r "「そんなこと言ったって……忙しいから、なかなか難しいというか……」"


show char tri05s2 at right as r
with dis



voice "Risa_0254"
r "「でもでも、私は美夜のこと、すごく、す、好きだし、ら……ラブラブだと思っているし……」"


show char tmi02s2 at left
with dis



voice "Miya_0168"
m "「……言ってて、顔が赤くなってるわよ、璃紗」"
voice "Risa_0255"
r "「もぉ……わかってるわよ」"
"うううっ……恥ずかしいこと、言っちゃったわ。"
"美夜ったら、ニヤニヤしちゃっているし。"
voice "Miya_0169"
m "「璃紗がそんなにわたくしのこと、好きなら……もっと愛を実感させて」"


show char tri03s2 at right as r
with dis



voice "Risa_0256"
r "「実感って……何をすればいいの？」"


show char tmi01s2 at left
with dis



voice "Miya_0170"
m "「それはね……璃紗からわたくしに、キスをするの」"


show char tri04s2 at right as r
with dis



voice "Risa_0257"
r "「ふぇぇっ、そんな……」"
voice "Miya_0171"
m "「あら、出来ないのかしら？」"
"恥ずかしいに決まっている……でも美夜は、キスをねだる。"
"委員会や勉強は、私にとってとっても大事。"
"でもそのせいで、私が美夜を寂しくさせているのなら……自分から、キスするくらい……"


show char tri05s2 at right as r
with dis



voice "Risa_0258"
r "「や、やるわよ……」"


show char tmi11s2 at left
with dis



voice "Miya_0172"
m "「じゃあ……来て、璃紗……」"
"美夜が静かに目を閉じて、私を待っている。"
"私は少しずつ、彼女に近づき、その唇に……"


show char tri11s2 at right as r
with dis



voice "Risa_0259"
r "「……んっ、ん……ちゅう{image=image/exch001.png}」"
voice "Miya_0173"
m "「んんっ、あっ……ちゅっ……」"
"軽く触れて、そして離れる。"


show char tri05s2 at right as r
with dis



voice "Risa_0260"
r "「ほら……キス、したからね……」"
voice "Miya_0174"
m "「……もっと、よ」"
"美夜はまだ、瞳を閉じたままだった。"
"もう、美夜ったら……"


show char tri11s2 at right as r
with dis



voice "Risa_0261"
r "「ちゅっ{image=image/exch001.png}」"
voice "Miya_0175"
m "「んんっ……もっとよ」"
voice "Risa_0262"
r "「ちゅる、んちゅ……美夜ぁ」"
voice "Miya_0176"
m "「まだよ……わたくし、まだ不安よ……」"
voice "Risa_0263"
r "「わかったわよ……んちゅ、ちゅう{image=image/exch001.png}」"
"美夜の要求は、なかなか終わらない。"
"と言うよりも、よりいっそうエスカレートしていく。"


show char tmi05s2 at left
show char tri05s2 at right as r
with dis



voice "Miya_0177"
m "「もう、１回……ね」"
voice "Risa_0264"
r "「えっ……なんか、おかしくなりそう……はぁ、はぁ……」"
voice "Miya_0178"
m "「だったら、もう１０回っ！！」"


show char tmi11s2 at left
show char tri11s2 at right as r
with dis



voice "Risa_0265"
r "「ちゅるる、ちゅぱ……あんっ、もう……何回しているか、もうわからないわ……はぁ、はぁ……んちゅ」"
voice "Miya_0179"
m "「ちゅうううっ……もっと、もっとよ{image=image/exch001.png}」"
"私からしているのか、美夜から仕掛けてるのか、わからないくらい。"
"２人で何度も、激しいキスを繰り返す。"


show char tmi05s2 at left
show char tri05s2 at right as r
with dis



voice "Risa_0266"
r "「あぁん……美夜ぁ、まだキスするのぉ{image=image/exch001.png}」"
voice "Miya_0180"
m "「璃紗ったら……そんな甘えた声を出して、エッチね……もうわたくし、我慢の限界かも」"


show char tri03s2 at right as r
with dis



voice "Risa_0267"
r "「……えっ？」"
voice "Miya_0181"
m "「もうダメ、璃紗が欲しいのよ……エッチな璃紗が！！」"


show char tri05s2 at right as r
with dis



voice "Risa_0268"
r "「そんなぁ、エッチだなんて、美夜が迫るから……ひゃ、あぁん……だめぇ{image=image/exch001.png}」"
"結局私は、いつものようにソファに押し倒されて。"
"そのまま、美夜が満足するまで、可愛がられてしまったのでした。"


#**青空
#allClear:
hide char tmi05s2 at left
hide char tri05s2 at right as r
#lastBG:
#scene bg bg29a
scene bg bg42a
with Dis



voice "Risa_0269"
r "「あぁ、はぁん……もぉ、美夜のエッチぃぃっ……やぁぁん{image=image/exch001.png}\001」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with dis


#♂MS
stop music fadeout 1


#wipecancel disabled
#waitcancel disabled
#log off

scene image eyecatch01
#wipe vshutter

#wait 3000

scene black
with Dis

#log on
#waitcancel enabled
#wipecancel enabled


#//END
jump S010


