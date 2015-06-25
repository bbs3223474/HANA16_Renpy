#「究極の淑女トークバトル」

label S020:
$ save_name = "◇究極の淑女トークバトル"


#**ビーチテラス・昼
scene bg bg40a
with Dis



#mes on
#system on


#♂MP01
play music "sound/BGM01.ogg"


"麗奈先生に招待された南国のバカンス……滞在日数はなんと、夏休み最終日まで！！"
"つまりあと２週間も、ここでたっぷりと遊べるということだった。"


show char tma01f2
with dis



voice "Mai_0140"
ma "「麗奈先生、太っ腹よね。これだけの人数、ツアーで行ったとしても、結構かかるわね」"


show char tma01f2 at left
show char tna03f2 at right as r
with dis



voice "Nanami0174"
n "「夏休みが終わったら……わたし、しばらく現実に帰れなくなりそう」"

hide char tma01f2 at left
hide char tna03f2 at right as r
show char tma01f2 at sleft as l
show char tna03f2
show char trk03f2 at sright as sr
with dis



voice "Rikka_0353"
rk "「その通り……ですね」"


#allClear:
hide char tma01f2 at sleft as l
hide char tna03f2
hide char trk03f2 at sright as sr
#lastBG:
#scene bg bg40a
show char tma03f2
with dis



voice "Mai_0141"
ma "「……うーん」"


show char tma03f2 at left
show char tri03f2 at right as r
with dis



voice "Risa_0647"
r "「どうしたんですか、麻衣さま」"


show char tma01f2 at left
with dis



voice "Mai_0142"
ma "「みんなだめよ、こういう時は思いっきり楽しまなくちゃ！　スーパーのタイムセールとか、現実的なことは忘れるのよ、ねっ？」"


show char trk03f2 at right as r
with dis



voice "Rikka_0354"
rk "「タイムセール！」"


show char tna02f2 at right as r
with dis



voice "Nanami0175"
n "「そうですね……こうなったら、現実を忘れて楽しみましょう～」"


#allClear:
hide char tma01f2 at left
hide char tna02f2 at right as r
#lastBG:
#scene bg bg40a
show char tre03f2
with dis



voice "Reo_0119"
re "「麻衣たち、何を騒いでいるのかしら……」"


show char tyu02f2
with dis



voice "Yuuna_0062"
y "「ふふふっ、七海ったらあんなにはしゃいじゃって、可愛い～{image=image/exch001.png}」"


show char tsy02f2
with dis



voice "Sayuki0143"
s "「六夏さん、先輩の皆さまと本当に仲が良いですね」"


#allClear:
hide char tsy02f2
#lastBG:
#scene bg bg40a
with dis


"『庶民連合』と、そのパートナー達の温度差を、ひしひしと感じるわ。"
"私も夏休みの終わりまで、ここにいて良いって言われた時には、かなり驚いたけれど。"
"だけど……あまり難しいことは考えずに。"
"このバカンスを、私たちは大いに楽しむことにした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチ・昼
scene bg bg39a
with Dis

#mes on
#system on


"海で泳ぐのは、もちろんだけど。"
"夏の海といえば……"


show char tsa01m
with dis



voice "Sara_0097"
sr "「スイカ割り、だよね？」"


show char tka01m at left
show char tsa01m at right as r
with dis



voice "Kaede_0057"
k "「紗良、スイカ割りなんてやったことあるのかしら？」"
voice "Sara_0098"
sr "「ないけど、一度やってみたかったんだよね。みんな、やってみない？」"

hide char tka01m at left
hide char tsa01m at right as r
show char tka01m at sleft as l
show char tsa01m
show char ter02m at sright as sr
with dis



voice "Erisu_0054"
e "「わぁ、やるやる、ワタシやってみたい{image=image/exch001.png}」"


show char tsa02m
with dis



voice "Sara_0099"
sr "「やりましょう、エリスさま♪」"


#allClear:
hide char tka01m at sleft as l
hide char tsa02m
hide char ter02m at sright as sr
#lastBG:
#scene bg bg39a
with dis


"紗良さんの一言に、エリスさまはすっかり乗り気になって。"
"今日はみんなで、スイカ割りをすることになった。"
"ほとんどの人が初体験ってことで、最初はやる気満々なエリスさまから始めることになったのだけど……"


show char tsi03m
with dis



voice "Sizuku0043"
sk "「エリス……気をつけてくださいね」"


show char ter01p at hleft
show char tsi03m at right as r
with dis



voice "Erisu_0055"
e "「平気だよ。あっ、シズクもう少し固めにしばって」"
"雫さまがタオルで、エリスさまに目隠しをする。"


show char tsi08m at right as r
with dis



voice "Sizuku0044"
sk "「後はこのまま、くるくると回せばいいんですよね……いきますよ、それっ！」"
voice "Erisu_0056"
e "「あーれー」"
"両手をあげて回りながら、エリスさまはよれよれと雫さまに寄りかかる。"
"そのまま、わかりやすいくらいのセクハラ行為が始まった。"


show char tsi07m at right as r
with dis



voice "Sizuku0045"
sk "「もう！　エリス、ふざけないでください」"


#※CU04
#allClear:
hide char ter01p at hleft
hide char tsi07m at right as r
#lastBG:
#scene bg bg39a
show char CU04
with dis



voice "Erisu_0057"
e "「だって、見えないんだもん{image=image/exch001.png}　ふふふっ～」"
voice "Sizuku0046"
sk "「ちょ、ちょっと、エリス重たいですぅ」"
"何だかエリスさま、ただ雫さまとふざけあってるだけにしか見えない。"
voice "Yuuna_0063"
y "「エリスさまと雫さまったら、楽しそうね」"
voice "Sara_0100"
sr "「はうっ、エリスさまったら公衆の面前で、いちゃいちゃしてる……次は紗良も、あれやる～」"
"紗良さん……それは何だか、目的が違っているような……"
"その後、エリスさまはお顔を真っ赤にされた雫さまに怒られて、普通にスイカ割りを始めることにした。"
"周りの私たちは、エリスさまをスイカのあるところまで誘導するために声を上げる。"
voice "Risa_0648"
r "「エリスさま、こっちです、こっち」"
voice "Sizuku0047"
sk "「エリス、もっと右ですよ」"
voice "Erisu_0058"
e "「えーっ、こっちの方かなー」"
voice "Reo_0120"
re "「……全然違うわよ」"
"スイカ割り初体験のエリスさまは要領がつかめず、あっちにふらふら、こっちにふらふら。"
"棒を振り回してみるも、あと一歩のところでスイカに当たらない。"
voice "Risa_0649"
r "「ああ、惜しい～……ねぇ、美夜は応援しないの？」"
voice "Miya_0311"
m "「あまり興味がないわ……もぐもぐ」"
voice "Risa_0650"
r "「どうして、もうスイカ食べてるのよ、美夜」"
voice "Miya_0312"
m "「割るの待ちきれないから、貰ってきたのよ……璃紗もどう？」"
voice "Risa_0651"
r "「エリスさまが割ってからにするわ」"
voice "Miya_0313"
m "「でも……エリスさま、ズルしてるわよ」"
voice "Risa_0652"
r "「えっ？」"
voice "Reo_0121"
re "「きゃあああ！　エリス、なんでこっちにくるのよー」"
voice "Erisu_0059"
e "「だって、このまままっすぐなんでしょう？」"
voice "Reo_0122"
re "「違うわよ、通り過ぎてるわよ、戻りなさいっ」"
"棒をブンブン振り回しながら、エリスさまは玲緒さまを追いかけまわしている。"
"それも随分、しっかりとした足取りで……"
voice "Sizuku0048"
sk "「もう、エリスったら……またふざけて」"
voice "Mai_0143"
ma "「途中で玲緒をからかう方が面白いことに、気づいてしまったのね……エリスさま」"
voice "Sayuki0144"
s "「六夏さん……これがスイカ割りなのですか？　私、初めて拝見しました」"
voice "Rikka_0355"
rk "「いえ……これは多分、ただの追いかけっこです」"
voice "Sayuki0145"
s "「そうなのですか？　それではスイカ割りというものは？」"
voice "Rikka_0356"
rk "「ワ、ワタシが……後で、やってみせますから」"
"確かに運動神経の良い六夏なら、見事に割ってくれそうね。"
voice "Risa_0653"
r "「でも、エリスさま……悪ふざけしすぎですよ、これじゃ」"
"そしてこの悪ふざけが、とんでもない事態を招く事に……"
voice "Erisu_0060"
e "「スイカはどこー？　玲緒みたいなスイカはどこー？？」"
voice "Reo_0123"
re "「うにゃぁぁ、ワタシスイカじゃない、助けてぇ～！！」"
"さすがに玲緒さまを見かねたのか、雫さまが声を上げた。"
voice "Sizuku0049"
sk "「エリス、もう止めてあげて下さい、玲緒さんが可哀想ですっ！」"
voice "Erisu_0061"
e "「玲緒スイカ、みーつけた！　えーいっ！！」"
voice "Sizuku0050"
sk "「止めてください、エリス～っ！！」"

#//SE：ドサッと激しく抱きつくような音
#♀SE009
play sound "sound/SE009.ogg"


#※EV006
#allClear:
hide char CU04
#lastBG:
#scene bg bg39a
scene bg EV06
with Dis



voice "Sizuku0051"
sk "「きゃっ、ぶつかってしまいました……大丈夫ですか、エリス？」"
voice "Erisu_0062"
e "「うん、ワタシは全然大丈夫だよ」"
voice "Risa_0654"
r "「だっ、大丈夫じゃないです、エリスさま……お胸がその……」"
voice "Miya_0314"
m "「見事に……ポロリ、ね」"
voice "Erisu_0063"
e "「キャッ、もう……シズクの、エッチ{image=image/exch001.png}」"
"エリスさまを止めようとして、つまづいて。"
"背後から抱きつくように、しがみついた雫さま。"
"そのせいで、なんとエリスさまの水着がズリ落ち、はだけてしまったのだった。"
voice "Miya_0315"
m "「まさかね……璃紗だと思っていたのに、エリスさまだったなんて」"
voice "Risa_0655"
r "「それって何のこと、美夜？」"
voice "Miya_0316"
m "「このリゾートビーチツアーの、ポロリ担当よ」"
voice "Risa_0656"
r "「勝手に決めないでよぉ～」"
"でも本当に、絶妙な感じで水着が残っている。"
"大きな胸はほとんど丸見えなのに、肝心なところが微妙な感じで。"
voice "Risa_0657"
r "「それでも、私だったら……恥ずかしくて、泣いちゃいそうだわ」"
voice "Erisu_0064"
e "「もぉ、いやん……シズク、こんなハプニングをこっそり、狙っていたのね{image=image/exch001.png}」"


#※EV006P1
scene bg EV06p1
with Dis



voice "Sizuku0052"
sk "「ちちちっ、違います、ただの偶然ですっ！！　そんなつもりでやったのでは……ひぃん」"
"慌てまくって、涙まで浮かべている、雫さま。"
"なのに脱がされた当人の方は、照れながらも笑っていた。"
voice "Erisu_0065"
e "「シズクのせいで、みんなにサービスしちゃったよ、もう。こうなったらシズクも一緒に、サービスしとく？」"
voice "Sizuku0053"
sk "「わ、わたくしは遠慮します、許してくださいぃ、ひぃんんっ！！」"
voice "Risa_0658"
r "「雫さまも、エリスさまも……ふふっ、ふふふっ」"
"仲が良いというか、面白いというか。"
voice "Risa_0659"
r "「このバカンスの楽しい想い出が、また一つ増えたわ」"
voice "Miya_0317"
m "「あら、そう……だったら璃紗もポロリしちゃって、わたくしの美しい想い出を増やして欲しいわね{image=image/exch001.png}」"
voice "Risa_0660"
r "「それは……いやぁぁっ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**青空
scene bg bg42a
with Dis



#mes on
#system on


"……こうして、エリスさまと雫さまは、退場して。"
"そのエリスさまの代わりに、スイカ割りは六夏が引き継いで。"
"見事にスイカは割れたのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチ・昼
scene bg bg39a
with Dis



#mes on
#system on

#※ここから、六夏視点。

show char tna02m at sleft as l
show char trk05m
show char tsy02m at sright as sr
with dis



voice "Sayuki0146"
s "「六夏さんのスイカ割り、本当にすごかったです」"
voice "Nanami0176"
n "「本当に、見事に割れてたよね～」"
voice "Rikka_0357"
rk "「たまたまです、みんながうまく誘導してくれたから……」"


show char tyu01m at sleft as l
show char tna02m
show char trk05m at sright as sr
with dis



voice "Yuuna_0064"
y "「さすが、騎士と呼ばれるだけのことはあるわね」"
voice "Rikka_0358"
rk "「い、いえ、そんな……ぅぅっ、恥ずかしい……」"


#allClear:
hide char tyu01m at sleft as l
hide char tna02m
hide char trk05m at sright as sr
#lastBG:
#scene bg bg39a
with dis


"みんなでビーチで遊んでいたはずなのに、いつの間にかワタシの周りには、環境整備委員のメンバーが揃っていた。"
"この３人は、仲が良いみたいだけど。"
"ワタシは一体、何を話せばいいんだろう……ああ、ちょっと困る。"
"いつも恋愛相談に乗ってもらっていたけれど、今は沙雪さんがいるから、その話は出来ないし……"


show char tsy02m
with dis



voice "Sayuki0147"
s "「ここに来てからは、初めての経験ばかりでとても楽しいです」"


show char tyu02m at left
show char tsy02m at right as r
with dis



voice "Yuuna_0065"
y "「そうねー、私もこんな大人数でバカンスを楽しむのは、初めてよ」"
voice "Sayuki0148"
s "「優菜さまも、ですか？」"
voice "Yuuna_0066"
y "「ええ」"


#allClear:
hide char tyu02m at left
hide char tsy02m at right as r
#lastBG:
#scene bg bg39a
show char trk01m
with dis



voice "Rikka_0359"
rk "「………………」"
"ワタシは楽しげに話す沙雪さんを、ぼんやりと眺めていることにした。"


show char tyu01m at left
show char tsy01m at right as r
with dis



voice "Sayuki0149"
s "「優菜さまは普段の夏休みは、どんな風にお過ごしになっているのですか？」"
voice "Yuuna_0067"
y "「私、１人の時は、海外の別荘に行っているわね」"


#allClear:
hide char tyu01m at left
hide char tsy01m at right as r
#lastBG:
#scene bg bg39a
show char trk04m
with dis



voice "Rikka_0360"
rk "「べっ、別荘！？」"
"クラスメイトたちも話していたことだけど、こういうのはミカ女では当たり前のことらしい。"
"でも、やっぱり直接聞くと、驚いてしまう。"
voice "Yuuna_0068"
y "「どうかしたの、六夏ちゃん？」"


show char tyu01m at left
show char trk03m at right as r
with dis



voice "Rikka_0361"
rk "「あっ……その、海外に別荘があるなんて、すごいですね」"
voice "Yuuna_0069"
y "「国内にもいくつかあるけれど、長期休暇の時は海外の方に行くことが多いわね」"


show char trk04m at right as r
with dis



voice "Rikka_0362"
rk "「わっ、ほっ、他にもあるんですか！？」"
voice "Yuuna_0070"
y "「ええ……そのうちの一つは先日まで、七海も遊びに来てたのよね？」"

hide char tyu01m at left
hide char trk04m at right as r
show char tna02m at sleft as l
show char tyu01m
show char trk04m at sright as sr
with dis



voice "Nanami0177"
n "「はいっ、管理人さんの飼っていた犬が、とっても可愛かったです{image=image/exch001.png}」"
"七海さんが嬉しそうに答える。"
voice "Yuuna_0071"
y "「七海は動物、好きなのね。ウチも普段から家に誰かいれば、ペットを飼ったり出来たんだけど」"
voice "Nanami0178"
n "「仕方ありませんよ、おね……優菜さまのお家は、ご両親がいつもお忙しいんですから」"


show char trk03m at sright as sr
with dis



voice "Rikka_0363"
rk "「優菜さまの家って、何をしているんですか？」"
voice "Yuuna_0072"
y "「病院の経営よ」"
"びょ、病院！！"
"それも日本全国に開業している、大病院グループと同じ苗字ってことは……"
voice "Rikka_0364"
rk "「はぁ～、優菜さまってやっぱり、すごいんですね」"
"成績も常にトップクラスだって聞いているし、家柄も良いし。"
"何だかもう、庶民の憧れだわ。"


#allClear:
hide char tna02m at sleft as l
hide char tyu01m
hide char trk03m at sright as sr
#lastBG:
#scene bg bg39a
show char tsy03m
with dis



voice "Sayuki0150"
s "「………………」"


show char tna03m at left
show char tsy03m at right as r
with dis



voice "Nanami0179"
n "「あら、沙雪さん。少し顔色が悪いけれど、どうかしましたか？」"

hide char tna03m at left
hide char tsy03m at right as r
show char tna03m at sleft as l
show char tsy03m
show char trk03m at sright as sr
with dis



voice "Rikka_0365"
rk "「えっ？」"
"優菜さまの話に夢中になっていたけれど、そういえばさっきから、沙雪さんが一言も喋っていない。"
"よく見ると、下唇を小さく噛んで、ふるふる震えているようにも見えた。"
"海で少し、冷えてしまったのかな？"
"ワタシは思わず、自分の上着を沙雪さんに羽織ってもらおうとした。"
voice "Rikka_0366"
rk "「あの……沙雪さん、これ、良かったら……」"
voice "Sayuki0151"
s "「私の家も、海外に別荘がいくつかあります」"
voice "Rikka_0367"
rk "「えっ、沙雪さん？？」"
"寒いんじゃなかったの？　ひょっとして、優菜さまに負けたくないって思っていたの？"
"本心はよく分からないけれど。"


#allClear:
hide char tna03m at sleft as l
hide char tsy03m
hide char trk03m at sright as sr
#lastBG:
#scene bg bg39a
with dis


"沙雪さんは突然、自分の家のことについて話り始めた。"
"別荘がいくつあるかとか、自宅の広さはどれくらいだとか……確かにその内容は、ものすごいものだった。"
"私たち学生をバーンと、南の島にご招待してしまう麗奈先生もすごいけれど……沙雪さんの家も同じくらい、もしくはそれ以上かもしれないってこと？"


show char tna02m
with dis



voice "Nanami0180"
n "「ふわー、沙雪さんの家も、とってもすごいんですね」"
"今度は七海さんが、沙雪さんを憧れの眼差しで見つめた。"


show char tyu03m
with dis



voice "Yuuna_0073"
y "「な、七海……そんなキラキラした顔で、沙雪ちゃんを……くっ！」"


#allClear:
hide char tyu03m
#lastBG:
#scene bg bg39a
with dis


"何故か優菜さまは、倒れ込むようにうつむいた。"
"どこか、具合でも悪いのかな……"
voice "Yuuna_0074"
y "「ううううっ、でもこんなことで、落ち込んでいられないわ」"

#シャキン！
#♀SE010
play sound "sound/SE010.ogg"


show char trk01m
with dis



voice "Rikka_0368"
rk "「あっ、起き上がった」"


#※CU05
show char CU05
with dis



voice "Yuuna_0075"
y "「沙雪ちゃん……あなた、１年の間では『究極の淑女』って呼ばれているそうね」"
voice "Sayuki0152"
s "「淑女なんて、とんでもありません。私なんて……」"
voice "Sayuki0153"
s "「それより優菜さまこそ『学園のアイドル』と、皆様から慕われていらっしゃいますよね」"
voice "Yuuna_0076"
y "「私こそ、とんでもないわ……」"
voice "Sayuki0154"
s "「本当に、すごいですね」"
voice "Yuuna_0077"
y "「そちらこそ……」"
"なんだろう、これ……表向きは褒めあっているけれど、どこか不穏な空気を感じてしまう。"
"そして何故かそこから、松原家ＶＳ白河家のＰＲ合戦が始まってしまった。"
voice "Yuuna_0078"
y "「両親が大病院の院長とは言っても、そんな大したことはありませんしー」"
voice "Sayuki0155a"
s "「当家も山城を所有してるとはいえ、さほど大きなものではありませんし……」"
"いやいや、２人とも大したこと、ありすぎだし……"
voice "Yuuna_0079"
y "「最近、新しいクルーザーを買ったのですが、意外に使わないものねー。ムダな買い物だったかも知れないわー」"
voice "Sayuki0156"
s "「そうですね。個人所有の孤島をいくつか買って、ようやく最近、クルーザーの使い道が出てきました」"
voice "Yuuna_0080"
y "「まぁ、すごいわ{image=image/exch001.png}　我が家も是非、大きな島を買って、クルーザーでレジャーに行きたいわねー」"
voice "Sayuki0157"
s "「それは素敵ですね。優菜さまのお買いになる島は、さぞ大きいのでしょうね」"
"２人とも、メチャクチャ言っているわりに、笑顔なんですけど……"
"ゴゴゴゴッと、バックに竜と虎が争っている映像が見えるような気がした。"
voice "Rikka_0369"
rk "「な、何なの、これ……」"
voice "Nanami0181"
n "「もうわたしたちには、理解不可能な争いになっているわ」"
"この騒ぎを聞きつけて、みんなが集まってきた。"
voice "Mai_0144"
ma "「ねぇ、何しているの？」"
voice "Sayuki0158"
s "「ウチの自家用ジェットはせいぜい、２０名程度しか乗れませんし」"
voice "Yuuna_0081"
y "「すごいじゃなーい、沙雪ちゃん。我が家の自家用機は、定員はたったの１０名だから……でも軽い分、音速出るんだけどねー」"
voice "Mai_0145"
ma "「ひぃぃぃっ！！」"
"庶民連合仲間である麻衣さまは、あまりにセレブな対決内容にガクブルになっている。"
voice "Risa_0661"
r "「麻衣さま、一体何が……ひやぁぁ、何なのよ、この戦いは……」"
"リサ姉まで……あれ？"
"リサ姉もああ見えて、ワタシたちと同じ庶民感覚なのかな？"
"だったら、嬉しいけれど……ちょっと。"
voice "Miya_0318"
m "「璃紗、何を驚いているの……あれくらいの自慢合戦、みんなやっていることよ」"
"普通じゃないですよ、美夜さま！"
"思わずツッコミを入れたかったけど、今、美夜さまとは波風立てたくないし……"
voice "Erisu_0066"
e "「何やってるの、みんな？　ワタシも入れてよ」"
voice "Reo_0124"
re "「ふふふっ、じゃあエリス、勝負よ！　これならワタシだって勝てるわ」"
voice "Runa_0033"
rn "「家柄対決？　お金持ち対決？　それならわたしとねえさまの圧勝よ{image=image/exch001.png}」"
voice "Rena_0060"
ren "「そうね……確かにみんなすごいけれど、ウチは負ける気がしないわよ～」"
"こ、これって……もうメチャクチャ……"
voice "Rikka_0370"
rk "「場外乱戦？」"
"いつの間にか、そこはいかに自分の家がすごいかの、トークバトルの場になっていた。"
voice "Nanami0182"
n "「り、六夏さん……どうしようか？」"
"先輩である七海さんでさえ、心細そうな声を上げていた。"
voice "Rikka_0371"
rk "「どうしますかね……」"
"ワタシも不安でたまらず、まともな返事が出来ない。"


#**青空
#allClear:
hide char CU05
#lastBG:
#scene bg bg39a
scene bg bg42a
with Dis



"そうしてる間も、沙雪さんと優菜さまの対決は続いていって……"
"２人とも声を荒げることなく上品に、美しくかつ淡々とに舌戦を繰り広げた。"
"そして……いいかげん疲れたのか、先に音をあげたのは、優菜さまだった。"


#**ビーチ・昼
scene bg bg39a
with Dis


show char tyu01m
with dis



voice "Yuuna_0082"
y "「沙雪ちゃん……貴女は本当に素敵な人だわ。まさに究極の淑女にふさわしいと思うわ」"


show char tyu01m at left
show char tsy01m at right as r
with dis



voice "Sayuki0159"
s "「優菜さまこそ……学園のアイドルを地でゆく、立派な方だと思います」"


#allClear:
hide char tyu01m at left
hide char tsy01m at right as r
#lastBG:
#scene bg bg39a
show char trk04m
with dis



voice "Rikka_0372"
rk "「わ、わぁぁぁっ！！」"

#//SE：拍手の音
#♀SE011
play sound "sound/SE011.ogg"


"このチャンスに、ワタシは大きく拍手をした。"
"こうしてお互いを称えあい、対決は何とか終了した。"


show char tna03m at left
show char trk04m at right as r
with dis



voice "Nanami0183"
n "「お、終わったね……六夏さん」"


show char trk03m at right as r
with dis



voice "Rikka_0373"
rk "「やっと、終わりましたね……七海さま」"
"当の２人以上に、ワタシと七海さまはヒヤヒヤさせられてしまったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチ・夜
scene bg bg39c
with Dis



#mes on
#system on


show char tsy01f2
with dis



"戦いが終わって、宵闇時。"
"沙雪さんは１人、砂浜にたたずんでいた。"
"考え事の邪魔になるかもしれないけれど、どうしても話がしたくて……"
"ワタシは声がうわずらないように気をつけながら、彼女に話しかけた。"


show char trk01f2 at left
show char tsy01f2 at right as r
with dis



voice "Rikka_0374"
rk "「沙雪さん、お疲れ様」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0160"
s "「六夏……さん……」"
"ワタシの顔を見るなり、沙雪さんは顔をそらすようにうつむいてしまった。"
voice "Rikka_0375"
rk "「どうしたんですか……元気なさそうですよ」"
voice "Sayuki0161"
s "「先ほどの、優菜さまとのこと……反省していたのです」"
voice "Rikka_0376"
rk "「反省って……沙雪さん、負けていないじゃないですか」"
voice "Sayuki0162"
s "「いいえ、今回の件で、自分の未熟さを知りました……上には上がいる、と言うことを」"
"沙雪さんは、どこか遠い目をしてみせる。"
voice "Sayuki0163"
s "「ついムキになって、張り合ってしまいました……」"
voice "Rikka_0377"
rk "「沙雪さんって案外、負けず嫌いなんですね」"
voice "Sayuki0164"
s "「そ、それは……六夏さんが、見ていたから……」"


show char trk03f2 at left
with dis



voice "Rikka_0378"
rk "「……えっ？」"
"それって、どういうこと？"
"ワタシがいたから？"
"戸惑いながら、ワタシは今、思っていることをそのまま伝えた。"


show char trk01f2 at left
with dis



voice "Rikka_0379"
rk "「お金持ちのことは、よくわからないけど……ワタシは沙雪さんが一番、素敵だと思うよ……」"
voice "Sayuki0165"
s "「………………」"
"わぁぁっ、何とも言えない気まずい空気になってしまった。"
"なんて恥ずかしいことを言ってしまったの、ワタシ。"
"こんなことを突然言われて、沙雪さんが引いてしまわないかな……"
"しかし沙雪さんは半分だけ顔を上げて、穏やか微笑んでくれた。"


show char tsy02f2 at right as r
with dis



voice "Sayuki0166"
s "「六夏さん……嬉しいです、ありがとう」"


show char trk05f2 at left
with dis



voice "Rikka_0380"
rk "「さ……沙雪……さん……」"
"頭の中で、何かがプツンと切れたような音がした。"
"ああ……可愛い、可愛すぎる！"
"なんなの、今まで見せたことのない、その可愛さは。"
"そのままぎゅっと、抱きついてしまいたい。"
"そうできたら、どんなに嬉しくて……幸せで……"


show char tsy03f2 at right as r
with dis



voice "Sayuki0167"
s "「……六夏さん？」"


show char trk03f2 at left
with dis



voice "Rikka_0381"
rk "「そ……そろそろ、部屋に戻りましょうか……」"


#allClear:
hide char trk03f2 at left
hide char tsy03f2 at right as r
#lastBG:
#scene bg bg39c
with dis


"だけど……無理だよ、できないよ。"
"そんなこと、ワタシにできるワケないよ。"
"こんな素敵すぎる沙雪さんに、告白なんて無理だよ………………リサ姉。"


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
jump S021



