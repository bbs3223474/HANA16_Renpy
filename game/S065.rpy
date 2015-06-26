#「美夜がいないと……寂しいよ」

label S065:
$ save_name = "◇美夜がいないと……寂しいよ"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP22
play music "sound/BGM22.ogg"


voice "mobJyosiA0087"
mobA "「ごきげんよう」"
voice "mobJyosiB0049"
mobB "「ごきげんよう、今日も良いお天気ですね」"
voice "mobJyosiA0088"
mobA "「ええ、晴れて良かったですわ～」"
"いつもと変わらぬ、ミカ女の朝の風景。"
"学校へと向かう人波を眺めながら、私もその流れに乗っていた。"
voice "mobJyosiC0022"
mobC "「璃紗さん、ごきげんよう」"


show char tri02s2
with dis



voice "Risa_1560"
r "「……ええ、ごきげんよう」"
"朝から憂鬱な気持ちでいっぱいながらも、知り合いに挨拶されたら笑顔で返す。"
"もう、条件反射のようなものになっていた。"
"だけど……心の中は、雨模様。"
"雨も雨、どしゃ降り状態。"
"力を入れないと、今にも泣き出しそうだった。"


show char tri03s2
with dis



voice "Risa_1561"
r "「美夜……メール、見てないのかしら？」"


#allClear:
hide char tri03s2
#lastBG:
#scene bg bg18a
scene bg bg42a
with dis



"呟いて、空を見上げると。"
"悲しいくらいの、見事な晴天で。"
"それが余計に、私を悲しくさせてしまう。"


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


#//SE：ドアを開ける音
#♀SE003
play sound "sound/SE003.ogg"


show char tri03s2
with dis



voice "Risa_1562"
r "「………………」"
"最後の望みとばかりに、教室に入り。"
"もう習慣になっているように、美夜の席を見つめる。"
"だけどそこは、変わらず空席だった。"
voice "Risa_1563"
r "「やっぱり……休みなのね、美夜は」"


#allClear:
hide char tri03s2
#lastBG:
#scene bg bg04a
with dis


"やがて先生が入って来て、授業が始まる。"
"私はいるはずもない空席を、何度もチラ見してしまった。"
"そして心の中で、何度も祈る。"
"美夜……お願いだから今すぐ、学校に来て……"


show char tri04s2
with dis



voice "Risa_1564"
r "「……あっ」"
"祈りが通じたのかしら？"
"いつでも見れるように、制服のポケットに入れておいた携帯が震えていた。"
"私は先生に見つからないようにそっと、机の下で携帯を開く。"


show char tri01s2
with dis



voice "Risa_1565"
r "「メール……だわ」"
"待ちに待った、美夜からのメール。"
"深呼吸をしてから、それを開封する。"

#ガタッ！
#♀SE036
play sound "sound/SE036.ogg"


voice "Mobkyosi_0007"
j "「ん……安曇さん、どうかしましたか？」"


show char tri03s2
with dis



voice "Risa_1566"
r "「いえ……その、ちょっと具合が悪くて……保健室行って来ても、よろしいでしょうか？」"
voice "Mobkyosi_0008"
j "「あらっ、確かに顔色が悪いですね。このクラスの保健委員は……」"
voice "Risa_1567"
r "「私ひとりで大丈夫ですから、そのまま授業を続けてください」"


#allClear:
hide char tri03s2
#lastBG:
#scene bg bg04a
with dis


"付き添いはつけず、私はよろよろと教室から退出していった……"


#**新校舎廊下・昼
scene bg bg05a
with Dis


show char tri03s2
with dis



voice "Risa_1568"
r "「ああ、美夜……どうして……」"
"美夜からのメールには、こう書かれていた。"
"『今、本当に忙しいから、何かあったらメールか電話にして』"
"私と会う時間は、作れないということらしい。"


show char tri06s2
with dis



voice "Risa_1569"
r "「どうしても、会いたいのに……会って、ちゃんと聞きたいのに……ぐすっ」"
"昨日から我慢してたものが、一気に溢れ出してくる。"
"みんなの中で、何事もなかったように、真面目に授業を聞いていることなんて、できそうにない。"
"励ましてくれた友達や後輩の言葉も、今は何の慰めにもなっていなかった。"
voice "Risa_1570"
r "「美夜……もう、こんなに会いたいのに……ぅぅっ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#mes on
#system on


"私はそのまま、保健室に飛び込んだ。"
"そして放課後までの時間、誰とも顔を会わさずに、ずっとベッドの中で過ごしたのだった。"


#**璃紗の部屋・昼
scene bg bg01a
with Dis



show char tri03f2
with dis



voice "Risa_1571"
r "「………………あっ、ちょっと美夜、いつの間に来ていたの？」"


show char tmi01f2 at left
show char tri03f2 at right as r
with dis



voice "Miya_0916"
m "「あら、さっきからいたじゃないの。璃紗が部屋の大掃除をするから、手伝いにきてっていったんでしょう？」"


show char tri01f2 at right as r
with dis



voice "Risa_1572"
r "「そうだったかしら……ゴメン、ありがとね。じゃあ美夜には、キッチンの掃除を……って、なんでゴミ袋を漁っているのよ！？」"
voice "Miya_0917"
m "「だってここに、捨ててはいけないお宝が混ざっているかも知れないじゃないの」"


show char tri08f2 at right as r
with dis



voice "Risa_1573"
r "「そこはちゃんと、ゴミだけを……あぁっ、もう！　私が捨てようとしている古い下着、こっそり拾わないでよ！」"
voice "Miya_0918"
m "「こっそり捨てたの？　堂々と捨てれば良いのに」"
voice "Risa_1574b"
r "「そういうのは、あまり目立たないように捨てるのが、マナーなのよ。どこかの困った変質者が、持っていかないように……って、ここにも一人いたわ」"
voice "Miya_0919"
m "「あら、このわたくしを変質者呼ばわりするの、璃紗？」"
voice "Risa_1575"
r "「ええ、呼ぶわ。ド変態と呼ばせていただくわ」"
voice "Miya_0920"
m "「そんな、ひどい……こう見えてもわたくし、エコ主義者なのよ」"


show char tri03f2 at right as r
with dis



voice "Risa_1576"
r "「美夜が？　エコ主義？？　そんなの初耳だわ」"
voice "Miya_0921"
m "「いいえ、わたくしほどのエコ主義者はいないわよ。璃紗が着なくなった、服や下着を集めて、再利用しているんですもの」"
voice "Risa_1577"
r "「う、うわぁ……そんなエコ主義、聞きたくないわー」"
voice "Miya_0922"
m "「璃紗はものを大切にしなさすぎよ。これからは、璃紗の使用済みアイテムは全て、わたくしに回収させてね{image=image/exch001.png}」"


show char tri09f2 at right as r
with dis



voice "Risa_1578"
r "「おことわりよっ！！　私よりも、私の下着を優先するなんて……くぅぅっ」"
voice "Miya_0923"
m "「それは違うわ、璃紗。そんなものをいくら集めても、本物の魅力にはかなわないわよ」"


show char tri03f2 at right as r
with dis



voice "Risa_1579"
r "「どういう比べ方よ、もう……やっぱり美夜って変態だわ」"
voice "Miya_0924"
m "「そうね、璃紗がそう言うのなら、わたくしは変態なのね……そんな変態な恋人、もう嫌いになったかしら？」"


show char tri08f2 at right as r
with dis



voice "Risa_1580"
r "「きっ、嫌いになるなんて……そんなことない、たとえ変態だって、美夜は美夜だものっ！！」"


show char tmi02f2 at left
with dis



voice "Miya_0925"
m "「そんな風に言ってくれるのね、璃紗……嬉しいわ」"


show char tri03f2 at right as r
with dis



voice "Risa_1581"
r "「だって……だって私、美夜がいてくれないと……ずっとずっと、美夜に傍にいて欲しいのよ」"


show char tmi01f2 at left
with dis



voice "Miya_0926"
m "「だったら璃紗、こう言って……『美夜、ずっと私の傍にいてね』って」"


show char tri05f2 at right as r
with dis



voice "Risa_1582"
r "「えぇっ、そんな恥ずかしいこと、言わなくちゃいけないの！？」"
voice "Miya_0927"
m "「そうよ……そうしないとわたくし、いなくなってしまうかも……」"


show char tri09f2 at right as r
with dis



voice "Risa_1583"
r "「そんな、それはイヤ、そんなの絶対にイヤよっ！！」"


show char tmi02f2 at left
with dis



voice "Miya_0928"
m "「じゃあ………………言って{image=image/exch001.png}」"


show char tri05f2 at right as r
with dis



voice "Risa_1584"
r "「わ、わかったわ……言うわ、言えばいいんでしょう……もう……」"
voice "Risa_1585"
r "「み……美夜、その……ずっと、私の傍に……ぃ、ぃて……ね……」"


show char tmi01f2 at left
with dis



voice "Miya_0929"
m "「もっと大きな声で、はっきり、はいっ」"


show char tri09f2 at right as r
with dis



voice "Risa_1586"
r "「くぅぅっ、美夜、これからもずっと、ずっとずっと、私のそばにいて、いてほしいのっ！！」"


show char tmi02f2 at left
with dis



voice "Miya_0930"
m "「いいわ、その調子よ！　じゃあもう一回」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**保健室・昼
scene bg bg06a
with Dis



#mes on
#system on


show char tri04p
with dis



voice "Risa_1587a"
r "「み……美夜……ずっと、私のそばに……そば……えっ！？」"
"なんか、ヘンな気分……なんだろう、これ？"
"私、何かに包まって………………はっ！？"


show char tri03s2
with dis



voice "Risa_1588"
r "「ここ……保健室の、ベッド……」"
"そっか……私はいつの間にか、眠りこんでしまったのね。"
voice "Risa_1589"
r "「……昨日、寝てなかったから……」"
"悲しくて辛いのに、熟睡してしまって。"
voice "Risa_1590"
r "「あんな夢……見ちゃったのね、もう……」"
"目が覚めると、私は保健室に１人だった。"
"先生は席をはずしていて『目が覚めたら、そのまま帰宅して結構です』と、メモが残されていた。"
voice "Risa_1591"
r "「一眠りしたから、少しは落ち着いたかな……」"
"最初に保健室に来た時。"
"先生には、落ち込んでいる私が、よほどやつれているように見えたようで。"
"早退をするよう、進められたのだけど。"
voice "Risa_1592"
r "「ダメよ……この時期に、そんなことできないわ」"
"文化祭の準備も、いよいよ大詰め。"
"美夜の分も、私がしっかり働かなくちゃ……"
"私の気持ちの問題で、皆さんに迷惑はかけられない。"


show char tri08s2
with dis



voice "Risa_1593"
r "「辛くたって……頑張らないと！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**委員会室・昼
scene bg bg30a
with Dis


#mes on
#system on


show char tri03s2
with dis



voice "Risa_1594"
r "「………………」"


show char tsa03s2 at left
show char tri03s2 at right as r
with dis



voice "Sara_0208"
sr "「璃紗ちゃん、それ、色が違ってるよ？」"
voice "Risa_1595"
r "「………………」"


show char tsa08s2 at left
with dis



voice "Sara_0209"
sr "「ねぇ、璃紗ちゃんってば」"
voice "Risa_1596"
r "「あっ……ごめん。紗良さん、何かしら？」"


show char tsa03s2 at left
with dis



voice "Sara_0210"
sr "「璃紗ちゃん、今塗ってるの、木だよね」"
voice "Risa_1597"
r "「え、ええ……そうね」"
voice "Sara_0211"
sr "「ブルーになってるよ」"


show char tri04s2 at right as r
with dis



voice "Risa_1598"
r "「はうっ！　ごめん、すぐ塗り直すからっ」"
"私は慌てて、違う色の絵の具を取り出した。"

hide char tsa03s2 at left
hide char tri04s2 at right as r
show char tsa03s2 at sleft as l
show char tri04s2
show char tna04s2 at sright as sr
with dis



voice "Nanami0315"
n "「待って待って、璃紗さん！　乾いてからじゃないと、色が混ざるから……」"


show char tri03s2
with dis



voice "Risa_1599"
r "「あっ……あーあ……」"


show char tna03s2 at sright as sr
with dis



voice "Nanami0316"
n "「……遅かった、ね」"
voice "Sara_0212"
sr "「うーん……見事なまだら模様だね」"
voice "Risa_1600"
r "「ご、ごめんなさい……」"
"森の木が１本だけ、茶色とブルーの混ざった、なんともシュールな色になってしまった。"


show char tna01s2 at sright as sr
with dis



voice "Nanami0317"
n "「ここはわたしたちで何とかするから、璃紗さんはちょっと休んでいて」"
voice "Risa_1601"
r "「で、でも……」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0213"
sr "「大丈夫だよ。紗良たちにバーン、と任せて♪」"


#allClear:
hide char tsa02s2 at sleft as l
hide char tri03s2
hide char tna01s2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"失敗した以上、無理にやらせてもらうわけにもいかず、私はその場から離れた。"
"こんな忙しい時に、余計な仕事を増やしちゃった。"


show char tri03s2
with dis



voice "Risa_1602"
r "「はぁぁ……ダメだな、今日の私……」"
"私を心配して、さっきから六夏がちらちらと、こっちを見てるのも気づいているけれど。"
"大丈夫だからと、気丈に振舞う余裕すらない。"


show char tsy03s2
with dis



voice "Sayuki0858"
s "「六夏さん、どうかなさいましたか？　さっきから集中力が落ちてますよ」"


show char trk03s2 at left
show char tsy03s2 at right as r
with dis



voice "Rikka_1589"
rk "「だって、リサ姉が……ううん、ゴメンね。なんでもない」"
voice "Sayuki0859"
s "「………………」"
"沙雪さんの視線も、一瞬だけ感じた。"


#allClear:
hide char trk03s2 at left
hide char tsy03s2 at right as r
#lastBG:
#scene bg bg30a
show char tma03s2
with dis



voice "Mai_0259"
ma "「璃紗ちゃん、今回はずいぶんと、落ち込んでいるわね……」"


show char tma03s2 at left
show char tre01s2 at right as r
with dis



voice "Reo_0194"
re "「きっとお腹でも空いてるんじゃないの？　なんかお菓子分けてあげようかしら」"

hide char tma03s2 at left
hide char tre01s2 at right as r
show char tma03s2 at sleft as l
show char tre01s2
show char ter03f2 at sright as sr
with dis



voice "Erisu_0119"
e "「そういう玲緒が、スイーツ食べたいだけなんじゃないの？」"


show char tre04s2
with dis



voice "Reo_0195"
re "「ち、違うわよ、むううううっ」"


show char tre04s2 at sleft as l
show char ter03f2
show char tsi03f2 at sright as sr
with dis



voice "Sizuku0099"
sk "「だけど本当に、元気がないですね……璃紗さん」"


#allClear:
hide char tre04s2 at sleft as l
hide char ter03f2
hide char tsi03f2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"皆さまが私の方を見て、何か言っているみたいだけど。"
"その声は、私の耳には入ってこなかった。"


show char tri03s2
with dis



voice "Risa_1603"
r "「ぁぁ……美夜ぁ……ぅぅっ」"
"仕事をはずされて、１人でぼんやりしていると。"
"頭の中は美夜のことしか、考えられなくなっていく。"
"シャボン玉のように、美夜の姿がぽんぽんと、私のまわりに浮かんでくる。"
voice "Yuuna_0187"
y "「……璃紗ちゃん～{image=image/exch001.png}」"


show char tri04s2
with dis



voice "Risa_1604"
r "「っ！！」"
"突然、後ろから無邪気な声が聞こえてきて、私の思考はストップ。"
"美夜の姿が次々と、消えていった。"


show char tyu02s2 at left
show char tri08s2 at right as r
with dis



voice "Risa_1605"
r "「だ、誰ですか、いきなり？　あうっ……優菜さま……」"
"忙しいのに、ぼうっと１人の世界に入っていた私。"
"もしかして……お叱りを受けるかもしれないわ。"


show char tri03s2 at right as r
with dis



voice "Risa_1606"
r "「その……すいません、今すぐ作業始めますから」"
"辺りを見回して、何か仕事を探す。"
voice "Risa_1607"
r "（何でもいい、とにかく何か、何かやらなくちゃ……）"


show char tyu01s2 at left
with dis



voice "Yuuna_0188"
y "「ちょっと待って、璃紗ちゃん」"
voice "Risa_1608"
r "「っ！！」"
"優菜さまの手が、そんな私を止める。"
voice "Yuuna_0189"
y "「璃紗ちゃん……何か大きな悩み、あるのよね？」"
voice "Risa_1609"
r "「そ、それは……」"
"瞳の奥の奥まで、見透かすような。"
"そんな優菜さまの瞳に見つめられてしまい、私はたじろいだ。"
voice "Yuuna_0190"
y "「璃紗ちゃんがそんな様子では、みんな気になってしまって、仕事にならないわ」"
voice "Risa_1610"
r "「そんな……皆さんにまで、迷惑をかけてしまって……申し訳、ありません……」"
"落ち込む私の肩をそっと撫でながら、優菜さまは教室内のみんなに呼びかけた。"
voice "Yuuna_0191"
y "「今日は文化祭の準備を中止にして、璃紗さんの悩みをみんなで聞きましょう」"
voice "Risa_1611"
r "「優菜……さま……」"
voice "Yuuna_0192"
y "「私たち、もう何でも話せる関係でしょう……ね？」"

hide char tyu01s2 at left
hide char tri03s2 at right as r
show char tyu01s2 at sleft as l
show char tri03s2
show char tka01s2 at sright as sr
with dis



voice "Kaede_0131"
k "「そうよ、１人だけで悩まないで」"


show char tsa01s2 at sleft as l
with dis



voice "Sara_0214"
sr "「２年生会の仲間じゃない、何でも話してよ」"


show char trk01s2 at sright as sr
with dis



voice "Rikka_1590"
rk "「リサ姉、水くさいよ。ワタシだってたくさん、相談乗ってもらったんだから……ちょっとは恩返しさせてよ」"


show char tri03s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0860"
s "「微力ながら、私にできることでしたら、協力しますわ」"


show char tre01s2 at sleft as l
show char tri03s2
show char trk01s2 at sright as sr
with dis



voice "Reo_0196"
re "「うじうじするくらいなら、わーって話しちゃえばいいのよ」"


show char ter02f2 at sleft as l
show char tre01s2
show char tri03s2 at sright as sr
with dis



voice "Erisu_0120"
e "「玲緒の言う通りだよ、璃紗さん♪」"


#allClear:
hide char ter02f2 at sleft as l
hide char tre01s2
hide char tri03s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tri01s2
with dis



voice "Risa_1612"
r "「み……みんな……ぁぁ……」"
"いつの間にか、私の周りには皆さんが集まってきて。"
"次々に、優しい言葉をかけてくれていた。"
voice "Risa_1613"
r "「皆さん……ありがとう、本当にありがとうございます」"
"嬉しくて、泣きそうになるのを堪えながら、私は自分の置かれた事情を説明することにした。"


show char tri03s2
with dis



voice "Risa_1614"
r "「実は、その……美夜が……」"


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
jump S066



