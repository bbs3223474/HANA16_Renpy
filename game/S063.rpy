#「美夜の様子が……おかしい？」

label S063:
$ save_name = "◇美夜の様子が……おかしい？"


#**璃紗の部屋・夜
scene bg bg01c
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


show char tri02f2
with dis



voice "Risa_1455"
r "「ふうー、みんなで食事会、すっごく楽しかったなぁ～」"
"ママがヨーロッパに行く前に、いい思い出になったと思うわ。"
voice "Risa_1456"
r "「ママも雪乃さんも、すごく仲が良さそうだし……きっと２人とも、うまくいきそうよね」"
"学校が休みになったら、美夜と２人でむこうの家に訪ねに行く約束もしたし。"
"本当にすべてが、順風満帆に思えていた……"


show char tri01f2
with dis



voice "Risa_1457"
r "「でも……」"
"私は、自分の携帯を眺める。"


show char tri03f2
with dis



voice "Risa_1458"
r "「てっきり美夜のことだから、今日はうちに泊まるのかと……」"
"ちょこっと、期待しちゃったのよね……私。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//以下、璃紗の妄想

#**璃紗の部屋・昼
scene bg bg01c
show char moyan
show char tri01f2
with Dis


#mes on
#system on


voice "Risa_1459"
r "「……はぁ～、やっと終わったわ。これから後片づけね。美夜もちょっと、手伝って……美夜？」"


show char tmi05f2 at left
show char tri01f2 at right as r
with dis



voice "Miya_0896"
m "「う、うーん……なんか、わたくし……いい気分……かも」"


show char tri04f2 at right as r
with dis



voice "Risa_1460"
r "「どうしたの、美夜！？　顔も赤いし、ふらふらしているし……あっ、ひょっとしてまた、風邪でもひいたの？」"
voice "Miya_0897"
m "「かぜ……じゃないわ、きっと……ひっく」"


show char tri03f2 at right as r
with dis



voice "Risa_1461"
r "「でもなんかちょっと、様子がヘンよ」"
voice "Miya_0898"
m "「璃紗ぁ、なんか足がもつれちゃうの……きゃっ」"
voice "Risa_1462"
r "「みっ、美夜！？　急に抱きつかれたりしたら……ひょっとして美夜、お酒飲んじゃったの？」"


show char tmi09f2 at left
with dis



voice "Miya_0899"
m "「だっ、誰が酔っ払いですって！？」"


show char tri09f2 at right as r
with dis



voice "Risa_1463"
r "「そうじゃなくて……もう、美夜が飲んいでたのはノンアルコールのシャンパンでしょう！」"

#//※下記の美夜のセリフ、急にシラフ＆クールにしてください


show char tmi01f2 at left
with dis



voice "Miya_0900"
m "「……ええ、そうよ。キッチリ、学生に優しいノンアルコールよ」"


show char tri03f2 at right as r
with dis



voice "Risa_1464"
r "「もぉ、酔ったフリとかしないでよ、片付け大変なんだから」"
voice "Miya_0901"
m "「フリなんかじゃないわ……本当に酔っているのよ、わたくし」"


show char tri04f2 at right as r
with dis



voice "Risa_1465"
r "「だーかーらー、あのシャンパンには、お酒なんて……んっ！？」"


show char tmi11f2 at left
with dis



voice "Miya_0902"
m "「ちゅっ{image=image/exch001.png}　んちゅ、ちゅる………………ペロッ」"


show char tri05f2 at right as r
with dis



voice "Risa_1466"
r "「ひゃん、ちょっと美夜、いきなりキスしたり……首とか、舐めたりしちゃ……ダメよぉ」"


show char tmi02f2 at left
with dis



voice "Miya_0903"
m "「んふ、だってわたくし、ベロベロに酔っているんですもの……可愛い璃紗に」"


show char tri03f2 at right as r
with dis



voice "Risa_1467"
r "「ま、またそんなこと、言っちゃって……どうして私に酔うのよ？」"


show char tmi01f2 at left
with dis



voice "Miya_0904"
m "「だって璃紗、あんなに一生懸命、お母様や雪乃さんに、わたくしのことを自慢して……あんなにも、わたくしが好きなのよね？」"


show char tri02f2 at right as r
with dis



voice "Risa_1468"
r "「え、ええ……好きよ…………大好き、よ{image=image/exch001.png}」"


show char tmi02f2 at left
with dis



voice "Miya_0905"
m "「嬉しい……じゃあ今から、璃紗にお礼をしないと……ちゅぱ、んふ……さあ、脱ぎ脱ぎしましょうね{image=image/exch001.png}」"


show char tri05f2 at right as r
with dis



voice "Risa_1469"
r "「で、でもまだ、片づけが……ぁん{image=image/exch001.png}」"


show char tmi01f2 at left
with dis



voice "Miya_0906"
m "「片づけなら後で、一緒にしてあげるわよ。だから、今は……ね？」"
voice "Risa_1470"
r "「そ、それなら……うん、いいわ……ぁっ、はぁん{image=image/exch001.png}」"


show char tmi02f2 at left
with dis



voice "Miya_0907"
m "「可愛いわ、璃紗……わたくし、今夜は璃紗に泥酔しちゃいそう……んふふっ{image=image/exch001.png}」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//（璃紗の妄想ここまで）

#**璃紗の部屋・昼
scene bg bg01c
with Dis



#mes on
#system on


show char tri03f2
with dis



voice "Risa_1471"
r "「……とかとか、美夜ならあってもおかしくないのにぃ～」"
"食事会の終了後、ママと雪乃さんを送り出したら、美夜は部屋に残るのかと思ったけど。"
"結局ママたちと一緒に、帰ってしまった。"
voice "Risa_1472"
r "「雪乃さんとの話が盛り上がっていたし、まだ話足りない様子だったものね……美夜」"
"美夜の家の車で、２人を送っていくって言ったけど……"
"多分……車の中でも、雪乃さんとの話は続いていたんでしょうね。"
voice "Risa_1473"
r "「それにしても……家に着いたら着いたで、メールくらいしてくれてもいいのに」"
"携帯は、うんともすんとも言わない。"


show char tri08f2
with dis



voice "Risa_1474"
r "「まるで私ばっかりが、美夜と２人きりになりたかったみたいじゃない……もう」"
"美夜が泊まる約束をしていたわけじゃないけれど……"


show char tri03f2
with dis



voice "Risa_1475"
r "「なんだか……ガッカリだわ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


voice "mobJyosiA0084"
mobA "「璃紗さん、ごきげんよう」"


show char tri01s2
with dis



voice "Risa_1476"
r "「ええ、ごきげんよう」"
voice "mobJyosiA0085"
mobA "「少しお顔の色がすぐれませんが、どうかなさいましたか？」"


show char tri03s2
with dis



voice "Risa_1477"
r "「あっ……昨日夢中で小説を読んでいて、その……寝不足気味なんですっ」"
voice "mobJyosiA0086"
mobA "「まぁ……でも、璃紗さんがそれほど夢中になる本でしたら、わたくしも是非今度読んでみたいですわ{image=image/exch001.png}」"


show char tri01s2
with dis



voice "Risa_1478"
r "「それなら読み終わったら、持って来ますね」"
"愛想良く、クラスメイトに答えながら。"
"そんなに顔色が悪かったのかしら……と、ちょっと不安になる。"
"寝不足は寝不足でも、美夜のメール待ちだったのよね。"


show char tri03s2
with dis



voice "Risa_1479"
r "「もしかしたら、ママたちを送り届けた後、また戻ってくるかも……なんて勝手に思いこんでいたから」"
"なかなか落ち着かなくて、明け方まで寝付けなくて。"
"でも結局、美夜からはなんの連絡もなかった。"
voice "Risa_1480"
r "「まぁ、こういう日もあるわね……」"
"私じゃ、美夜の仕事の話なんてついていけないもの。"
"せっかくわかりあえる人に会えたんだもの、思う存分、語り合いたいわよね。"


show char tri01s2
with dis



voice "Risa_1481"
r "「そうよね、うん……そうだわ」"
"学校にいる間は、美夜は私と同じ学生だから。"
"そのあたりは、対等でいられる。"
voice "Risa_1482"
r "「昨日話せなかった分、今日たくさん話せばいいんだわ」"


#allClear:
hide char tri01s2
#lastBG:
#scene bg bg18a
with dis


"足取りも軽く、私は教室に向かった。"


#**新校舎教室・昼
scene bg bg04a
with Dis



show char tri08s2
with dis



voice "Risa_1483"
r "「もう……美夜ったら……」"
"授業が始まっても、美夜の姿はなかった。"
"またサボりのようで。"
voice "Risa_1484"
r "「アトリエにでも行ってるのかしら？　昼休みに見に行ってこなくちゃ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


#**アトリエ・昼
scene bg bg29a
with Dis



#mes on
#system on


"昼休みのチャイムが鳴り、急いでアトリエに向かったけれど。"
"しかしそこにも、美夜の姿はなかった。"


show char tri03s2
with dis



voice "Risa_1485"
r "「もしかして今日、休み？　そんなことないわよね……私、何も聞いてないし」"
"とりあえずソファに座り、お弁当箱を広げる。"


show char tri01s2
with dis



voice "Risa_1486"
r "「お弁当箱持ったまま、移動するのも面倒だから、ここで食べながら……美夜を待とうかしら」"


#allClear:
hide char tri01s2
#lastBG:
#scene bg bg29a
with dis


"そのまま、一人で黙々とお弁当を食べて。"
"食べ終わった後、いつも美夜がしているように、ヤカンに火をかけ、お茶を入れた。"


show char tri03s2
with dis



voice "Risa_1487"
r "「まだ来ないの？　美夜ったら、本当にどうしちゃったのかしら」"
"やっぱり他の場所も、探した方が良かったのかしら？"
"悩んでいると、ゆっくりとドアが開いて。"
"ようやく、お目当ての人が現れた。"


show char tmi04s2
with dis



voice "Miya_0908"
m "「璃紗！？　来ていたの？」"


show char tmi04s2 at left
show char tri08s2 at right as r
with dis



voice "Risa_1488"
r "「美夜、遅いわよ～、どこに行ってたのよ」"


show char tmi03s2 at left
with dis



voice "Miya_0909"
m "「ちょっと、家の仕事が長引いてて……」"


show char tri03s2 at right as r
with dis



voice "Risa_1489"
r "「もしかして今、来たところなの？」"


show char tmi01s2 at left
with dis



voice "Miya_0910"
m "「ええ、少し前にメールしたけれど」"


show char tri04s2 at right as r
with dis



voice "Risa_1490"
r "「ええっ？」"
"携帯を取り出すと、ちょうどお昼を食べている時間くらいに、美夜から『今日は昼過ぎに行きます』と入っていた。"


show char tri03s2 at right as r
with dis



voice "Risa_1491"
r "「ごめん、見てなかったわ」"
voice "Miya_0911"
m "「かまわないわ。本当なら朝、連絡すれば良かったんだけど、忙しくて」"
voice "Risa_1492"
r "「仕事なら仕方ないわね、それで美夜……」"


#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


show char tri01s2 at right as r
with dis



voice "Risa_1493"
r "「あっ……もうこんな時間なのね」"
"せっかく美夜と会えたのに、もう昼休みが終わってしまう。"
voice "Risa_1494"
r "「教室戻らなくちゃ……美夜も行くでしょう？」"
voice "Miya_0912"
m "「わたくしは今、着いたところだから、せめてお茶くらい飲んでからにしたいわ」"


show char tri08s2 at right as r
with dis



voice "Risa_1495"
r "「だめよっ！　そんな時間ないわよ」"
voice "Miya_0913"
m "「だったら璃紗も一緒に、お茶していけばいいじゃない」"


hide char tmi01s2 at left
with dis


voice "Risa_1496"
r "「私はもう飲んだもの、さあ行くわよ……って、美夜？」"
"目の前から、美夜の姿は消えていた。"
voice "Risa_1497"
r "「もう～」"
"その日、美夜は午後の授業を一時間だけ顔をだして、帰っていったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



"……美夜の様子が少し変わったと気付いたのは、これが最初だった。"


#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


show char tri03s2
with dis



voice "Risa_1498"
r "「ねぇ美夜、文化祭の準備は？」"


show char tmi03s2 at left
show char tri03s2 at right as r
with dis



voice "Miya_0914"
m "「ごめんなさい、今日はどうしてもはずせない用があるの。皆さんにも謝っておいてくれるかしら」"
voice "Risa_1499"
r "「え、ええ……わかったわ」"


show char tmi01s2 at left
with dis



voice "Miya_0915"
m "「ありがとう、それじゃごきげんよう」"


show char tri01s2 at right as r
with dis



voice "Risa_1500"
r "「ごきげんよう……」"


#allClear:
hide char tmi01s2 at left
hide char tri01s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"慌ただしく出かけていく後ろ姿。"
"このところずっと、美夜は忙しい。"
"２人で一緒にいる時間も、どんどん減っていた。"


show char tri03s2
with dis



voice "Risa_1501"
r "「……こんなのたまたまよね。私も早く行って、準備手伝わないと」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


show char tri03s2
with dis



voice "Risa_1502"
r "「えっ……美夜、今日も休みなの？」"
"朝学校に来ると、美夜からメールが来ていて。"
"そこには『今日も学校を休むから』とだけ、書いてあった。"
voice "Risa_1503"
r "「２人でいる時間も減ったけど、美夜が学校を休むことも多くなったのよね……」"
"休んだ日はちゃんとメールが来るので、そんなに心配はしていない。"
"メールにもしっかりと『今、大事な仕事をやっていて、しばらく会えないわ、ゴメンね』と書いてあるし、不安になる要素もない。"
voice "Risa_1504"
r "「なのに……ちょっと寂しいって、感じてしまうのよね」"


#allClear:
hide char tri03s2
#lastBG:
#scene bg bg04a
with dis


"早く美夜の仕事が終わり、また前みたいに戻れたら……こんな気持ちにならなくていいのに。"


#**新校舎廊下・昼
scene bg bg05a
with Dis



#//SE：走ってくる音
#♀SE035
play sound "sound/SE035.ogg"


voice "Rikka_1581"
rk "「リサ姉～」"
"いつものように、イベント実行委員の教室に向かおうとすると、六夏が走ってやってきた。"


show char tri08s2
with dis



voice "Risa_1505"
r "「六夏、廊下は走っちゃだめでしょう」"


show char tri08s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_1582"
rk "「ごめん、リサ姉を見かけたもので、つい……」"
voice "Sayuki0852"
s "「六夏さん、待ってください」"
"後ろから必死に、沙雪さんがやってきた。"

hide char tri08s2 at left
hide char trk03s2 at right as r
show char tri08s2 at sleft as l
show char trk03s2
show char tsy03s2 at sright as sr
with dis



voice "Sayuki0853"
s "「はぁ、はぁ、やっと追いつきました……六夏さんは本当に、璃紗さまがお好きなんですから」"
voice "Rikka_1583"
rk "「あっ……すいません、今はわざとおいていったわけじゃなくて」"


show char tsy02s2 at sright as sr
with dis



voice "Sayuki0854"
s "「ふふふ、わかっております。ちょっと拗ねてみただけです」"
"沙雪さんの言動に、おろおろする六夏。"
"いろいろあったけれど、この２人はうまくいっているみたいね。"


show char tri01s2 at sleft as l
with dis



voice "Risa_1506"
r "「２人ともこれから、委員会に行くの？」"


show char trk01s2
with dis



voice "Rikka_1584"
rk "「ええ……でもせっかくだし、３人でお茶でもしてきませんか？」"


show char tri03s2 at sleft as l
with dis



voice "Risa_1507"
r "「お茶……？」"
"六夏は学食の方を指さした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**中庭・昼
scene bg bg21a
with Dis



#mes on
#system on


show char tri01s2
with dis



voice "Risa_1508"
r "「ごちそうさまでした、でも本当にご馳走になっていいのかしら？」"


show char tri01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_1585"
rk "「リサ姉にはお世話になったんだから、これくらい大したことないよ」"


show char tri02s2 at left
with dis



voice "Risa_1509"
r "「そう……ありがとう」"
"六夏は学食で紙パックのジュースを買って来て、それを私にくれた。"
"もちろん自分でお金は出すつもりだったけれど、やんわりと断られてしまった。"
voice "Risa_1510"
r "「ここ、とっても風が気持ちいいわね～」"

hide char tri02s2 at left
hide char trk01s2 at right as r
show char tri02s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0855"
s "「ええ、六夏さんと私も、よく一緒にここに来るんです。良い気分転換になりますよ」"
voice "Risa_1511"
r "「本当に、いい場所よね～」"
"文化祭の準備が忙しい中、こんなにのんびりしている場合じゃないけれど。"
"たまには……こういうのもいいかもしれないわね。"
voice "Rikka_1586"
rk "「美夜さまも早く、委員の方に復活してくれるといいね」"
voice "Sayuki0856"
s "「きっとすぐに、戻って来ますわ」"
"ここのところ、ずっとイベント実行委員の仕事を休んでいる美夜のことを、２人はぽつりと言い出した。"


show char tri03s2 at sleft as l
with dis



voice "Risa_1512"
r "「あ、あの……」"
voice "Rikka_1587"
rk "「休んでいる間にワタシ達だけで沢山進めておいて、驚かせるのもいいんじゃないかなぁ」"
voice "Sayuki0857"
s "「驚いた顔の、美夜さま……拝見してみたいですね」"
voice "Risa_1513"
r "「………………」"
voice "Rikka_1588"
rk "「それじゃ、そろそろ教室に行きましょうか」"
voice "Risa_1514"
r "「そうね……」"
"そのまま３人で、教室へと向かった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・昼
scene bg bg08a
with Dis



#mes on
#system on


show char tsa01s2
with dis



voice "Sara_0203"
sr "「七海ちゃん、買い出しリスト、ちゃんと持ってきたよね？」"


show char tsa01s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0312"
n "「はい。優菜さまからしっかり、預かって来ましたよ」"
voice "Sara_0204"
sr "「最初は、どの店にしようか……」"
"教室に戻ったら、優菜さまから足りない資材を買い足しして欲しいと言われて。"
"２年生会のみんなと、買い出しに行くことになった。"

hide char tsa01s2 at left
hide char tna01s2 at right as r
show char tri03s2 at sleft as l
show char tsa01s2
show char tna01s2 at sright as sr
with dis



voice "Risa_1515"
r "「………………」"


show char tsa03s2
with dis



voice "Sara_0205"
sr "「璃紗ちゃん、疲れてる？」"


show char tri01s2 at sleft as l
with dis



voice "Risa_1516"
r "「あっ……ううん、平気よ」"
voice "Nanami0313"
n "「無理しないでね、また帰りにカフェ寄っていこうか？」"


show char tri03s2 at sleft as l
with dis



voice "Risa_1517"
r "「えっ、でも……」"
"さっき、六夏たちとジュースを飲んだから、喉は渇いていないんだけど……"


show char tsa01s2
with dis



voice "Sara_0206"
sr "「遠慮しないで。話したいこととか、グチとかたまってない？」"
voice "Risa_1518"
r "「それは……」"
voice "Nanami0314"
n "「行きましょうよ、璃紗さん。たくさんおしゃべりしましょう」"


show char tri01s2 at sleft as l
with dis



voice "Risa_1519"
r "「そうね……ええ、そうするわ」"
"六夏と沙雪さん。"
"そして２年生会の、七海さん、紗良さん。"
"きっとみんな、私が美夜のことで元気ないの知っていて、気にかけてくれているんだわ。"
voice "Risa_1520"
r "「……ありがとう」"
voice "Sara_0207"
sr "「んっ？　何」"
voice "Risa_1521"
r "「……えっと、最初はかさばらないものから、買い物して行きましょう」"


#allClear:
hide char tri01s2 at sleft as l
hide char tsa01s2
hide char tna01s2 at sright as sr
#lastBG:
#scene bg bg08a
with dis


"少し照れくさくて、ちゃんと言えなかったけれど。"
"私は本当に、良い友達や後輩を持ったなぁ……って、思ったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#♂MS
stop music fadeout 1


#//END
jump S064



