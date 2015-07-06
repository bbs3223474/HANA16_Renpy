#「離れるどころか……ずっと一緒！？」

label S069:
$ save_name = "◇離れるどころか……ずっと一緒！？"


#**暗転


#mes on
#system on


#♂MP18
play music "sound/BGM18.ogg"


"そして、その後……二人は朝まで愛し合ってしまい……"
"仕事がまだ残っているからと、美夜は家に戻っていった。"
"私は恥ずかしながら、午後から一人で登校して。"
"そして放課後、皆さんに事の顛末を報告した。"


#**委員会室
scene bg bg30a
with Dis



show char tri05s2
with dis



voice "Risa_1742"
r "「――そんなわけで、美夜がヨーロッパに行くのはたったの一週間で、私とママの勘違いでした」"
"………………"
"さすがにすぐには、ツッコミをしてくる人はいなかった。"
"いつもポジティブな紗良さんですら、絶句中なのだから。"
"い、今のうちに、早めに……"


show char tri03s2
with dis



voice "Risa_1743"
r "「今回の件では、皆さんをいっぱいお騒がせしてしまい、本当にごめんなさいっ！」"
"深々と頭を下げて、謝罪をする。"
"あんなに大騒ぎした結果が、こんなことだなんて……本当に恥ずかしい。"
"皆さん絶対、呆れているわよね？"
"おそるおそる顔を上げてみると……みんな、穏やかに微笑んでいた。"


show char tsa02s2 at left
show char tri03s2 at right as r
with dis



voice "Sara_0221"
sr "「よかったね……美夜ちゃんがいなくならなくて、本当に良かったね、璃紗ちゃん♪」"


show char tri01s2 at right as r
with dis



voice "Risa_1744"
r "「さ、紗良……さん……」"


show char tka01s2 at left
with dis



voice "Kaede_0135"
k "「でも今度からは、早合点しないようにしましょうね、璃紗さん」"
voice "Risa_1745"
r "「は、はい、楓さま……それはもう、十分に気をつけます」"


show char tri01s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0127"
e "「ヨーロッパ一週間だけなら、着いていっても大丈夫なんじゃない？」"

hide char tri01s2 at left
hide char ter01f2 at right as r
show char tri01s2 at sleft as l
show char ter01f2
show char tsi03f2 at sright as sr
with dis



voice "Sizuku0102"
sk "「だめですよ、エリス。その間の学校はどうするんですか？」"
voice "Erisu_0128"
e "「秋休みにすればいいんじゃないかなぁ……どう？」"


show char tri03s2 at sleft as l
with dis



voice "Risa_1746"
r "「……それは無理です、エリスさま」"
"私も一週間くらいなら、美夜に着いていってみたい気もするけれど……"
"仕事の邪魔に、なっちゃいそうだものね。"


#allClear:
hide char tri03s2 at sleft as l
hide char ter01f2
hide char tsi03f2 at sright as sr
#lastBG:
#scene bg bg30a
show char tre08s2 at left
show char tri03s2 at right as r
with dis



voice "Reo_0203"
re "「まったく……安曇璃紗って、人騒がせよね」"
voice "Risa_1747"
r "「ぅぅ……すみません、玲緒さま」"


show char tma01s2 at left
show char tre08s2 at right as r
with dis



voice "Mai_0266"
ma "「ふふふっ、そう言いながら玲緒は、美夜ちゃんがいなくならなくて、ホッとしているんじゃないのかしら？」"


show char tre03s2 at right as r
with dis



voice "Reo_0204"
re "「ど、どうしてワタシが、綾瀬美夜のことを……」"
voice "Mai_0267"
ma "「だって大事な大事な、メル友でしょう？」"


show char tre08s2 at right as r
with dis



voice "Reo_0205"
re "「す、スイーツ情報交換担当なだけよ……お互いの、り、利害が一致している間柄なのよっ！」"
voice "Mai_0268"
ma "「ほうほう……」"


#allClear:
hide char tma01s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0199"
y "「スイーツといえば、皆さんにって、差し入れでケーキもらっていたんだわ」"


show char tyu01s2 at left
show char tna02s2 at right as r
with dis



voice "Nanami0322"
n "「わっ、美味しそうですね♪　みんなで頂きましょう」"


#allClear:
hide char tyu01s2 at left
hide char tna02s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa01s2
with dis



voice "Sara_0222"
sr "「それなら『美夜ちゃんが、ミカ女に残って良かったね記念』の、お茶会を開こうよ」"


show char tma01s2 at left
show char tsa01s2 at right as r
with dis



voice "Mai_0269"
ma "「美夜ちゃん本人がいないのは残念だけど……それいいわね。どうかしら、優菜さん？」"


#allClear:
hide char tma01s2 at left
hide char tsa01s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0200"
y "「そうね、まだ文化祭の準備は残ってるけれど、少しくらいならいいわね」"


show char tyu01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_1748"
r "「優菜……さま……」"
voice "Yuuna_0201"
y "「璃紗ちゃんここのところ悩んでいて、ゆっくりお茶をする余裕もなかったんじゃないかしら？」"


show char tri03s2 at right as r
with dis



voice "Risa_1749"
r "「ええ……それは、まあ……」"


show char tri03s2 at left
show char trk02s2 at right as r
with dis



voice "Rikka_1599"
rk "「じゃあワタシ、お茶入れてくるね。リサ姉のために美味しいの入れてくるからね」"


show char tri01s2 at left
with dis



voice "Risa_1750"
r "「六夏……うん、ありがとう」"


show char trk02s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0864"
s "「では私もお手伝いしますわ、六夏さん」"


#allClear:
hide char trk02s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"こうしてその後、突如としてお茶会が始まった。"
"文化祭の準備途中だったため、短い時間だったけれど。"
"気持ちに余裕があったせいか、すごくリラックスできて。"
"ここ数日、自分の気持ちがすごく張っていたんだなってことに気付かされた。"
"仲間がいるって、本当に……心強いね。"


show char tsa01s2
with dis



voice "Sara_0223"
sr "「美夜ちゃんが戻ってきたら、お帰りのお茶会を開こうよ」"


show char tka03s2 at left
show char tsa01s2 at right as r
with dis



voice "Kaede_0136"
k "「それはいいけど、そんなにケーキばかり食べて大丈夫なの、紗良？」"


show char tsa03s2 at right as r
with dis



voice "Sara_0224"
sr "「あっ、明日からしっかりダイエットだから、今日はいいの」"


#allClear:
hide char tka03s2 at left
hide char tsa03s2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0270"
ma "「美夜ちゃん帰国記念お茶会は、玲緒がお菓子を用意してあげたら？」"


show char ter02f2 at left
show char tma01s2 at right as r
with dis



voice "Erisu_0129"
e "「うんうん、玲緒に相応しい仕事だね♪」"

hide char ter02f2 at left
hide char tma01s2 at right as r
show char ter02f2 at sleft as l
show char tma01s2
show char tre08s2 at sright as sr
with dis



voice "Reo_0206"
re "「ふんっ、綾瀬美夜がぎゃふんと言いそうなお菓子、いーっぱい用意してみせるわ」"
voice "Erisu_0130"
e "「お菓子でぎゃふんは、言わないと思うなぁー」"


show char tma02s2
with dis



voice "Mai_0271"
ma "「でも……見てみたい気はするけどね、ふふっ」"
"いつの間にか、美夜を囲んでのお茶会の開催まで決まっていた。"


#allClear:
hide char ter02f2 at sleft as l
hide char tma02s2
hide char tre08s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tri02s2
with dis



voice "Risa_1751"
r "（美夜に話したら、どんな顔するかしら……ふふっ）"


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


show char tsa01s2 at sleft as l
show char tri01s2
show char tna01s2 at sright as sr
with dis



voice "Sara_0225"
sr "「璃紗ちゃん、ごきげんよう」"
voice "Nanami0323"
n "「ごきげんよう、璃紗さん」"
voice "Risa_1752"
r "「ごきげんよう。２人とも、今帰り？」"
voice "Nanami0324"
n "「はい。わたしはこのまま、家だけど……」"


show char tsa10s2 at sleft as l
with dis



voice "Sara_0226"
sr "「うううっ、紗良はこの後仕事だよ～！　また楓ちゃんとすれ違い生活だよー」"


show char tri03s2
with dis



voice "Risa_1753"
r "「そ、そうなの？」"


show char tsa03s2 at sleft as l
with dis



voice "Sara_0227"
sr "「昨日も一昨日も仕事の時間が合わなくて、楓ちゃんとちっとも一緒にいられないんだよぉ～」"
voice "Nanami0325"
n "「まぁまぁ、でも今の仕事終わればしばらくは休みになるって、さっき言ってたじゃない」"
"グチる紗良さんを、七海さんがなだめる。"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0228"
sr "「そうなんだ。そしたら楓ちゃんといーっぱい、甘い時間が過ごせる……うふふ{image=image/exch001.png}」"


show char tri01s2
with dis



"遠い目をしている紗良さん。"
"すっかりご機嫌な様子ね。"
voice "Nanami0326"
n "「美夜さんはもう、日本出ちゃったんだよね？」"
voice "Risa_1754"
r "「ええ、今頃はむこうで忙しく動き回っているんじゃないかしら」"


show char tsa01s2 at sleft as l
with dis



voice "Sara_0229"
sr "「うわー、美夜ちゃんってそういうの、すごく似合いそうだね」"


show char tna02s2 at sright as sr
with dis



voice "Nanami0327"
n "「一週間の、遠距離恋愛だね……ちょっと素敵{image=image/exch001.png}」"


show char tri03s2
with dis



voice "Risa_1755"
r "「そうなるのかしら……？」"
"本当なら、美夜を見送りにも行きたかったのに。"
"美夜ったらいきなり空港から『今から行くから』とメールを送ってきて。"
"出発日も、帰国する日すら、私に教えてくれないんだもの。"
"まともに話ができたのも、ウチに訪ねてきた時くらいなのよね。"
voice "Risa_1756"
r "「美夜が何も教えてくれないから、全然スケジュールがわからないのよ」"
voice "Sara_0230"
sr "「それは……美夜ちゃんも璃紗ちゃんが見送りに来たら、さすがに行くの迷っちゃうんじゃないかな？」"
voice "Risa_1757"
r "「そんなこと……うん、あるかもしれない」"


show char tna01s2 at sright as sr
with dis



voice "Nanami0328"
n "「じゃなかったら『やっぱり璃紗を連れていく～』とか、なっちゃいそうだからじゃない？」"
voice "Risa_1758"
r "「飛行機で、それはちょっと……」"
"強引に私をさらって、ヨーロッパまで連れて行っちゃう美夜を想像したら、カッコいいけれど。"
"そんなことしたら、いろいろなところに迷惑をかけるどころじゃ済まなそうだわ。"

#//SE：携帯の音
#♀SE012
play sound "sound/SE012.ogg"


show char tri01s2
with dis



voice "Risa_1759"
r "「あっ、メールだわ」"
voice "Sara_0231"
sr "「噂をすれば……美夜ちゃんからじゃないの？」"
voice "Risa_1760"
r "「うん……そうみたい」"


show char tna02s2 at sright as sr
with dis



voice "Nanami0329"
n "「わたしたちには遠慮せずに、早く見てあげて♪」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0232"
sr "「どうぞ、どうぞー♪」"


show char tri05s2
with dis



voice "Risa_1761"
r "「え、ええ……」"
"２人に気を使われて、少し恥ずかしいけれど、中身が気になって。"
"私はすぐに、メールに目を通した。"
voice "Risa_1762"
r "「みっ……美夜ったら……もう……」"


show char tna01s2 at sright as sr
with dis



voice "Nanami0330"
n "「璃紗さん、顔がすごく赤くなってるよ」"
voice "Sara_0233"
sr "「うふふ、ラブラブメールなんだね、ねー？　なんて書いてあったの？？」"
voice "Risa_1763"
r "「な、内緒……よ」"


show char tsa03s2 at sleft as l
with dis



voice "Sara_0234"
sr "「えええっ～、そんなぁ」"


show char tna03s2 at sright as sr
with dis



voice "Nanami0331"
n "「なんか、気になっちゃいますね～」"
"２人は残念そうだけど……このメールは、私だけのものにしたい。"
"というか、そうじゃないと、またからかわれてしまいそうだから。"
voice "Sara_0235"
sr "「じゃあ、ちょっとだけでいいから」"
voice "Nanami0332"
n "「簡単な内容だけでも、ねっ？」"


show char tri09s2
with dis



voice "Risa_1764"
r "「だ、だめっ！！」"
"私は２人の質問責めから逃げながら、美夜からもらったメールの中身を頭で反芻していた。"


#**青空
#allClear:
hide char tsa03s2 at sleft as l
hide char tri09s2
hide char tna03s2 at sright as sr
#lastBG:
#scene bg bg18a
scene bg bg42a
with Dis



voice "Miya_1017"
m "『璃紗、元気にしているかしら？　それともみんなに今回の件を報告して、からかわれている頃かしら？』"
voice "Miya_1018"
m "『まったく……璃紗を置いていくワケないじゃない。わたくしは璃紗にベタ惚れなんだから{image=image/exch001.png}』"
voice "Miya_1019"
m "『海外では、妻はビジネスパートナーとして、常に伴侶と共にあるものよ。憶えておいてね』"


#**並木道・昼
scene bg bg18a
with Dis



show char tri02s2
with dis



voice "Risa_1765"
r "「もう……本当に美夜ったら、恥ずかしいこと書いてくるんだから」"


show char tsa01s2 at left
show char tri02s2 at right as r
with dis



voice "Sara_0236"
sr "「あー、またニヤニヤしちゃって。璃紗ちゃん思いだし笑いしてる」"

hide char tsa01s2 at left
hide char tri02s2 at right as r
show char tsa01s2 at sleft as l
show char tri02s2
show char tna01s2 at sright as sr
with dis



voice "Nanami0333"
n "「璃紗さんが幸せそうなら、それでいいんだけどね……もう、そっとしておきましょうか、紗良さん」"
voice "Sara_0236b"
sr "「ん、だね、だね♪」"
"恥ずかしいけれど、とっても嬉しい。"
"美夜からもらった今回のメールがなくならないように、そっと保護機能をかけたのでした。"


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


"そしてそれから、また数日後……"


#**住宅街・昼
scene bg bg08a
with Dis



show char tri03s2
with dis


##voice RISA_1766
voice "Risa_1767"
r "「美夜が戻るまで、あと何日あるのかしら……」"
"普段なら一週間なんて、あっと言う間なのに……今回はなんか、とても長く感じてしまった。"


show char tri01s2
with dis



voice "Risa_1768"
r "「……ふう、ただいま～」"
"誰もいない、寂しい我が家に到着。"
"家の鍵を差し込んだ瞬間、私は妙な違和感を覚えた。"


show char tri03s2
with dis



voice "Risa_1769"
r "「あれっ、ひょっとして……開いてる？」"
"ママが何か、忘れ物を取りに来た？"
"そんなわけないわよね、ママもヨーロッパだし。"
"それに何かしら、連絡があるはずだし。"
voice "Risa_1770"
r "「もしかして……私、今朝鍵をかけ忘れたんじゃ……」"
"今までそんなボケをしたこと、ただの一度もないのに。"
voice "Risa_1771"
r "「じゃあ、泥棒が……ピッキングで開けたのかしら？」"
"何にしても、これはただ事ではないわ。"
voice "Risa_1772"
r "「ぅぅ……ぅぅっ………………」"
"私はおそるおそる、ドアを開ける……"


#**安曇家ダイニング・昼
#allClear:
hide char tri03s2
#lastBG:
#scene bg bg08a
scene bg bg02a
with Dis



#//このシーン、美夜は顔ウインドウの表示で（スーツの立ち絵が無いので）
show char tri04s2
with dis



voice "Risa_1773"
r "「はぁ、はぁ……誰か………………あぁっ！？」"


show char tmi01p at hleft
show char tri04s2 at right as r
with dis



voice "Miya_1020"
m "「あら……おかえりなさい、璃紗」"
voice "Risa_1774"
r "「美夜……どうして日本にいるの？　帰国、もっと後じゃないの？？」"
voice "Miya_1021"
m "「だって……愛しい璃紗に会いたくて、早く帰ってきてしまったわ」"
voice "Risa_1775"
r "「び、びびっ」"


show char tmi03p at hleft
with dis



voice "Miya_1022"
m "「びびびっ？　なにか電波でも感じたの？」"
voice "Risa_1776"
r "「びっ、びっくりしたのよぉ～」"


show char tmi01p at hleft
with dis



voice "Miya_1023"
m "「そう……でもこれくらいで、驚いていてはダメよ」"


show char tri03s2 at right as r
with dis



voice "Risa_1777"
r "「えっ……？」"
"それは実に、意味ありげな言葉だった。"
"これ以上のサプライズなんて、あるとは思えないんだけれど……"
voice "Miya_1024"
m "「以前、お母様が使われていたお部屋、あるわよね？」"
voice "Risa_1778"
r "「ええ……この間ママが荷物を運び出したから、今は物置代わりになっているけど」"
voice "Miya_1025"
m "「そこ、見てきたらどうかしら」"
voice "Risa_1779"
r "「ママの……部屋を？」"
"美夜の言っていることは、なんだかワケがわからない。"
voice "Miya_1026"
m "「ほらほら、早く行ってみて、ねっ？」"
voice "Risa_1780"
r "「わ、わかったわよ……もう」"


#allClear:
hide char tmi01p at hleft
hide char tri03s2 at right as r
#lastBG:
#scene bg bg02a
with dis


"美夜に急かされて、私はママの部屋を覗いてくることにした。"
"そして……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**安曇家ダイニング
scene bg bg02a
with Dis



#mes on
#system on


show char tri08s2
with dis



voice "Risa_1781"
r "「………………」"


show char tmi01p at hleft
show char tri08s2 at right as r
with dis



voice "Miya_1027"
m "「あら、戻ってきたわね。どうだったかしら？」"


show char tri09s2 at right as r
with dis



voice "Risa_1782"
r "「どうだったって……何よあれ、こっちが聞きたいわよ！！」"
"私はガマンできず、美夜を問い詰める。"
voice "Risa_1783"
r "「一体全体、どうなってるのよ！　ママの部屋が、あんなに……」"
voice "Miya_1028"
m "「そうよ……わたくしの部屋になったのよ」"


show char tri03s2 at right as r
with dis



voice "Risa_1784"
r "「や、やっぱり……そうなのね」"
"物もなく、ガランとしていたはずの、ママの部屋。"
"そこに見知らぬ高級家具と、大量の本が運び込まれていた。"
voice "Risa_1785"
r "「どうしてこんなこと、しちゃったの？」"
voice "Miya_1029"
m "「だって、わたくし……今日からここで暮らすから」"


show char tri04s2 at right as r
with dis



voice "Risa_1786"
r "「えええぇっっ！！」"
"何それ、何なのよ、それって！？"
"私、聞いてないし、何も知らないし。"
"この私を完全無視して、ママと美夜で勝手に決めちゃったっていうの？？"


show char tri03s2 at right as r
with dis



voice "Risa_1787"
r "「どうしてよ、いつ、こんなことが決まったの？」"
voice "Miya_1030"
m "「だってほら、会食の時にお母様から、璃紗の事を頼まれたでしょう？」"
voice "Risa_1788"
r "「そ、それは……そんな話、していたけれど……」"


show char tmi02p at hleft
with dis



voice "Miya_1031"
m "「お母様から、この部屋も好きに使って良いって言われたのよ{image=image/exch001.png}」"


show char tri04s2 at right as r
with dis



voice "Risa_1789"
r "「そ、そんな……もう、驚かせすぎよぉぉっ！！」"
voice "Miya_1032"
m "「うんうん、璃紗のその顔が見たかったのよ、驚いたでしょ？　嬉しいでしょ？」"
voice "Risa_1790"
r "「それは、確かに嬉しいような……あっ！？」"


#※EV040
#allClear:
hide char tmi02p at hleft
hide char tri04s2 at right as r
#lastBG:
#scene bg bg02a
scene bg EV40
with Dis



voice "Miya_1033"
m "「驚く璃紗って、とっても可愛いわ……ちゅっ{image=image/exch001.png}」"
voice "Risa_1791"
r "「んんっ！？　もぉ……ん、ちゅ{image=image/exch001.png}」"
"いきなりの、久しぶりのキス……でもそれが、なんだかすごく嬉しい。"
"私はそっと目を閉じて、そのキスを堪能した。"


#※EV040P1
scene bg EV40p1
with Dis



voice "Risa_1792"
r "「んん、んんっ……美夜……{image=image/exch001.png}」"
voice "Miya_1034"
m "「璃紗……ん、ちゅ……ん{image=image/exch001.png}」"
"何度も何度も、互いの存在を確認するような、キスを繰り返す。"
voice "Miya_1035"
m "「んふふ……これからはいつでも一緒ね、璃紗{image=image/exch001.png}」"
voice "Risa_1793"
r "「う、うん……そう、みたい……ちゅっ{image=image/exch001.png}」"
voice "Miya_1036"
m "「ちゅぱ、んふ……これってもう、新婚生活ね{image=image/exch001.png}」"
"そう言って、美夜は優しく微笑んで。"
"こうして私たちの新しい２人暮らしが今、いきなりスタートしたのでした{image=image/exch001.png}"

"璃紗＆美夜　ＨＡＰＰＹ　ＥＮＤ{image=image/exch001.png}"


#mes off
#mes clear
#system off


$ _skipping = False
$ _dismiss_pause = False
#log off


scene image "image/end02.png"
with Dis


pause 5


#log on
$ _skipping = True
$ _dismiss_pause = True


#**暗転
scene black
with Dis


#♂MS
stop music fadeout 1


#//END
#set f2 2
jump staffroll



