#「沙雪の恋愛研究」

label S034:
$ save_name = "◇沙雪の恋愛研究"


#（ここは沙雪視点）

#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#♂MP24
play music "sound/BGM12.ogg"


voice "mobJyosiA0067"
mobA "「沙雪さん、ごきげんよう」"


show char tsy01s2
with dis



voice "Sayuki0326"
s "「ごきげんよう」"
"クラスメイトに別れのご挨拶をしてから、私は振り向いた。"
"愛しい六夏さんを、見つめるために。"


show char trk01s2
with dis



voice "Rikka_0764"
rk "「………………」"
"六夏さんはまだ帰り支度もせず、ぼんやりと座っていた。"
"何だか……お悩みのように見えてしまう。"
"気になった私は、近くまで歩み寄って、声をかけた。"


show char trk01s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0327"
s "「あの……六夏さん？」"
voice "Rikka_0765"
rk "「………………」"
voice "Sayuki0328"
s "「六夏さん……六夏さん？？」"


show char trk04s2 at left
with dis



voice "Rikka_0766"
rk "「あっ、沙雪さん！！」"
"私の姿を見て、六夏さんは明らかに驚いた様子だった。"
"やっぱり何か、悩んでいるような感じです。"


show char trk03s2 at left
with dis



voice "Rikka_0767"
rk "「はぁ～……もう放課後だったんですね」"
"いつものまぶしい笑みとは違い、どこか疲れたような、弱い笑いを浮かべている。"
voice "Sayuki0329"
s "「あの……差し出がましいようですが、どうかなさったのですか？」"
voice "Rikka_0768"
rk "「い、いいえ……何でもないです。美夜さまとの、追いかけっこの疲れかも……」"
voice "Sayuki0330"
s "「追いかけっこ……ですか？」"


show char trk04s2 at left
with dis



voice "Rikka_0769"
rk "「な、なんでもありません……気にしないで下さい」"
"慌てて、帰り支度を始める六夏さん。"

#♀SE067
play sound "sound/SE067.ogg"


"机の中のものをカバンに詰め込んでいると、パラッとプリントが床に落ちた。"


show char tsy01s2 at right as r
with dis



voice "Sayuki0331"
s "「これ、落ちましたよ」"


show char trk03s2 at left
with dis



voice "Rikka_0770"
rk "「ありがとう、沙雪さん。これ、なんだったっけ……あっ！」"
"大きな声をあげた後、気まずそうに私を見つめてきました。"


show char tsy03s2 at right as r
with dis



voice "Sayuki0332"
s "「あの……何かありましたか？」"
voice "Rikka_0771"
rk "「ごめんなさい、沙雪さん。今日は陸上部のミーティングの日でして」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0333"
s "「あら、そうだったのですか」"
voice "Rikka_0772"
rk "「クラブで配られたプリント、見るの忘れてました……あぁ、まったく」"
voice "Sayuki0334"
s "「そうでしたか……」"
"ということは、今日はご一緒に帰れないのですね。"


show char tsy03s2 at right as r
with dis



voice "Sayuki0335"
s "「……残念、です」"
voice "Rikka_0773"
rk "「す、すいません……」"
"六夏さんの御用が終わるまで、待っていてもかまわないのだけど。"
"それだと逆に、六夏さんに気を使わせてしまいそうだと思ったので、先に帰らせて頂くことにしました。"


show char tsy01s2 at right as r
with dis



voice "Sayuki0336"
s "「それでは六夏さん、クラブの方、頑張ってくださいね……ごきげんよう」"


show char trk01s2 at left
with dis



voice "Rikka_0774"
rk "「はい、ごきげんよう、沙雪さん」"
"名残惜しくはありますが、私は一人で教室を後にしました。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


voice "Miya_0422"
x "「あの……沙雪さん」"


show char tsy03s2
with dis



voice "Sayuki0337"
s "「はい……あっ」"


show char tmi01s2 at left
show char tsy03s2 at right as r
with dis



"急に誰かに呼び止められたので振り返ると、そこには美夜さまがいらっしゃいました。"
"『美夜さまは気配を消して近づいてくることがあります』って、六夏さんが教えてくれた時は、まさかと思いましたが……本当に、その通りでした。"
"さっきまでは人の気配なんて、微塵も感じていなかったのです。"


show char tsy01s2 at right as r
with dis



voice "Sayuki0338"
s "「美夜さま、私に何か御用でしょうか？」"
"そう問いかけると、美夜さまはキョロキョロと辺りを見まわしました。"


show char tmi03s2 at left
with dis



voice "Miya_0423"
m "「今、貴女一人だけ？　六夏さんはいないのかしら？」"
voice "Sayuki0339"
s "「はい。六夏さんにご用事でしたら、陸上部の部室にいらっしゃるはずです」"


show char tmi01s2 at left
with dis



voice "Miya_0424"
m "「いいえ、いいのよ。わたくしは貴女を探していたの……一人だけなら、好都合だわ」"
voice "Sayuki0340"
s "「はい……」"
"美夜さまが私に、一体何の御用でしょうか……"
voice "Miya_0425"
m "「時間、少しもらえるかしら？」"
voice "Sayuki0341"
s "「はい、かまいません」"
voice "Miya_0426"
m "「じゃあ、ついてきて」"


hide char tmi01s2 at left
with dis


"そのまま振り返りもせず、美夜さまは先に歩き出してしまいました。"


#allClear:
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg05a
show char tsy03s2
with dis



voice "Sayuki0342"
s "「美夜さま……思ったより、歩くのが速いです……はぁ、はぁ」"
"私は彼女の後を、遅れを取るまいと必死に着いていきました。"


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


"やがて到着したところは、中庭でした。"
"それも奥の方の、あまり人が寄ってこないような場所でした。"
"なんだか少しだけ……不安になります。"
"これってひょっとして、世に言うところの『上級生の呼び出し』でしょうか？"
"私、何か美夜さまのご機嫌を損ねるようなことをしてしまったのでしょうか？"


show char tmi01s2
with dis



voice "Miya_0427"
m "「ここでいいかしら……今日はね、貴女に聞きたいことがあったのよ」"


show char tmi01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0343"
s "「はい……どのようなお話でしょうか？」"
"美夜さまと二人っきりになるなんて、もちろん初めてのことです。"
"どんなことを言われるのか……ああ、想像もつきません。"
"私は五体満足で、ここから帰ることができるのでしょうか？"
voice "Miya_0428"
m "「あのね、沙雪さん……六夏さんとの関係について聞かせてもらいたいのよ」"
voice "Sayuki0344"
s "「は、はい……」"


show char tmi03s2 at left
with dis



voice "Miya_0429"
m "「貴女たち……恋人同士、なのよね？」"
"その普通の問いかけを聞いて、私は少しだけホッとした。"
"御用とは、恋愛のお話だったのですね。"


show char tsy02s2 at right as r
with dis



voice "Sayuki0345"
s "「六夏さんのことですね。はい……彼女は私の大事な方です{image=image/exch001.png}」"
"そう言葉にして発すると、私は自然に笑顔になってしまいます。"
"ああ……恋をするのがこんな素敵なことだなんて、知りませんでした。"


show char tmi01s2 at left
with dis



voice "Miya_0430"
m "「そう……ちゃんと付き合っているのね……」"
"美夜さまは先輩として、私たちのことを気にかけてくださったのですね。"
"それならちゃんとお話をして、安心して頂きましょう。"
voice "Sayuki0346"
s "「六夏さんの話なら、なんでも聞いてください。むしろ、させてもらいたいくらいです♪」"


show char tmi03s2 at left
with dis



voice "Miya_0431"
m "「そ、そう……ああ、なんか調子狂うわね」"
"一瞬、美夜さまがたじろいでるように見えた。"
"でも今の私は、六夏さんのことを聞いてもらいたい気持ちの方が強く、話し始めてしまった。"
voice "Sayuki0347"
s "「どのお話からいたしましょうか？　そうそう六夏さんって、辛いものがお好きなんですよ」"
voice "Miya_0432"
m "「えっ？」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0348"
s "「先日、すごく辛いカレーをあっと言う間に平らげてしまって……私びっくりしてしまいました」"
voice "Sayuki0349"
s "「他にも、六夏さんは……」"
voice "Miya_0433"
m "「ちょっと待って、わたくしが聞きたいのは、そういうことじゃなくて……」"
voice "Sayuki0350"
s "「あら……」"
"美夜さまは頭をかかえてしまいました……頭痛かしら？"
"やがてブンブンと頭を振った美夜さまは、一人で納得したようにうなづいた。"


show char tmi01s2 at left
with dis



voice "Miya_0434"
m "「……そうね、そんな話をしているくらいなんだから、お二人の仲は良好のようね」"


show char tsy02s2 at right as r
with dis



voice "Sayuki0351"
s "「ええ、おかげさまで」"
voice "Miya_0435"
m "「何の問題もなく……幸せなのね」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0352"
s "「………………」"
"そう言われて、少しだけ考え込んでしまう。"
"両思いになってから、校内で一緒にいる時間も増えて。"
"たくさんお喋りをして、ご飯も一緒に食べたり、そして手をつないだり……"
voice "Sayuki0353"
s "「……あっ……」"
"何だか……ちょっと、気づいてしまったことがありました。"
voice "Miya_0436"
m "「進展は……本当に、しているのかしら？」"
"まるで私の心を読んでいるかのように、美夜さまが切り込んできます。"
"確かに、幸せ……とっても幸せなのだけど……"


show char tsy03s2 at right as r
with dis



voice "Sayuki0354"
s "「キスは……していません」"


show char tmi04s2 at left
with dis



voice "Miya_0437"
m "「えっ！？」"
voice "Sayuki0355"
s "「あのバカンスの、最後の夜以来、一緒にいる時間はとても増えました。ですが二度めのキスは、まだしておりません……」"
"私、そのことに今、気づいてしまったのです。"


show char tmi08s2 at left
with dis



voice "Miya_0438"
m "「やっぱり……そんなことだと思ったわ」"
voice "Sayuki0356"
s "「美夜さま……」"
"再び、美夜さまの表情がけわしくなりました。"
voice "Miya_0439"
m "「貴女たちがちゃんとラヴラヴしてくれないと、わたくしと璃紗が迷惑なのよっ」"
voice "Sayuki0357"
s "「ご迷惑とは……璃紗さまが、どうかしましたか？」"
voice "Miya_0440"
m "「な、何でもないわ。とにかく沙雪さん、いいこと……待っているだけなんて、生ぬるいわよ」"
voice "Sayuki0358"
s "「では私は、どうすれば……」"
voice "Miya_0441"
m "「もっとガンガン責めるのよ……自分から、ね」"
voice "Sayuki0359"
s "「責める……とは、どういうことでしょうか？」"
voice "Miya_0442"
m "「だから、キスから先に進むために、責めるのよ」"
voice "Sayuki0360"
s "「キスの……先、ですか？」"
"美夜さまは一体、何の話をしているのでしょうか？"
"私には皆目、見当もつきません。"
voice "Sayuki0361"
s "「美夜さま、それは具体的に、どのようなことを指すのでしょうか？」"


show char tmi05s2 at left
with dis



voice "Miya_0443"
m "「な、何を聞くのよ……くっ、白河沙雪、恐ろしいコ……！？」"
voice "Sayuki0362"
s "「？？？」"
"珍しく美夜さまが、真っ赤になられました。"
"私、そんなに恥ずかしいことを言ってしまったのでしょうか？"


show char tmi03s2 at left
with dis



voice "Miya_0444"
m "「沙雪さん、貴女……本当に、何も知らないの？」"
voice "Sayuki0363"
s "「はい、存じ上げません」"
voice "Miya_0445"
m "「ううっ……この子、なんてピュアなのよ……なんか自分が恥ずかしいわ」"
voice "Sayuki0364"
s "「美夜さま……私の勉強不足、お許しください」"
voice "Miya_0446"
m "「謝られても……しょうがないし」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0365"
s "「では出来れば、私は六夏さんに何をすればいいのか、教えてください」"


show char tmi05s2 at left
with dis



voice "Miya_0447"
m "「そ、それくらい、自分で考えなさいよねっ！！」"


hide char tmi05s2 at left
show char tsy04s2 at right as r
with dis


voice "Sayuki0366"
s "「あっ、美夜さま！？」"
"気がつけば美夜さまは、風のように素早く、私の前から姿を消してしまっていた。"


#allClear:
hide char tsy04s2 at right as r
#lastBG:
#scene bg bg21a
show char tsy03s2
with dis



voice "Sayuki0367"
s "「ああ……キスより先のこととは一体、何なのでしょうか……」"
"その疑問が、私の頭の中でグルグル渦巻き続けました。"


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
jump S035


