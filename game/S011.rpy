#「カップル達の集い」

label S011:
$ save_name = "◇カップル達の集い"


#※ここは七海視点で

#**カフェ・昼
scene bg bg36a
with Dis


#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


show char tna01s2
with dis



voice "Nanami0082"
n "「じゃあ早速……ん、何から話そっか……」"
"ひょんなことから、２年生会緊急会議が始まった。"
"璃紗さんと六夏さんを尾行してきた、わたしと紗良さんも、何か六夏さんの力になりたいと思い、意見を出すことにした。"
"恋する乙女を応援するのは、大切なことですよね……そうですよね、優菜お姉さま！"
"ここにはいない恋人に、わたしはそう問いかけた。"
"返事はないけれど、Ｙｅｓに決まっているよね。"
"でも突然の事の成り行きに、六夏さんはまだついていけていない感じだった。"
"やっぱり、不安があるのかな……？"
"そんな六夏さんを、紗良さんが笑顔で励ます。"


show char tsa02s2 at left
show char tna01s2 at right as r
with dis



voice "Sara_0032"
sr "「六夏ちゃん大丈夫だよ、ここには恋愛のエキスパートが揃ってるんだから」"


show char tsa02s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami0083"
n "「璃紗さん、いつの間にそんな、すごい称号を？」"

hide char tsa02s2 at left
hide char tna03s2 at right as r
show char tsa02s2 at sleft as l
show char tna03s2
show char tri03s2 at sright as sr
with dis



voice "Risa_0313"
r "「私が……？？」"
voice "Sara_0033"
sr "「ううん、璃紗ちゃんじゃなくて、七海ちゃんのことなんだけど」"


show char tna04s2
with dis



voice "Nanami0084"
n "「ふぇぇぇっ」"
"わたし？　どうしてわたし！？"


show char tsa01s2 at sleft as l
with dis



voice "Sara_0034"
sr "「だってさぁ、一番カッコいいのは楓ちゃんで決まりだけど、優菜さまは学園のアイドルじゃない？」"


show char tna03s2
with dis



voice "Nanami0085"
n "「それは……そうですが……」"
voice "Sara_0035"
sr "「そのアイドルとつき合っている七海ちゃんが一番、六夏ちゃんに良いアドバイスをしてあげられるんじゃないかな？」"


show char tri01s2 at sright as sr
with dis



voice "Risa_0314"
r "「なるほど……美夜は確かに、ちょっと変わって……ううん、目立つ存在だけど、変わり者だし」"
voice "Risa_0315"
r "「学園内での立ち位置的には、沙雪さんは優菜さまに近いかも……」"
voice "Nanami0086"
n "「そ、そうかなぁ……」"
"確かにお姉さまは、素敵な方で。"
"わたしはそんなお姉さまに釣り合うのかどうか、未だに日々悩んでいる。"
"そういうところは、六夏さんと同じかもしれないけれど……"
voice "Nanami0087"
n "「でも、２人の時は……エロ乙女だなんて……」"
"みんな、お姉さまの本当の姿を知らないから……"


show char tna03s2 at sleft as l
show char tri01s2
show char trk03s2 at sright as sr
with dis



voice "Rikka_0204"
rk "「七海さま、今、なんて……？」"


show char tna04s2 at sleft as l
with dis



voice "Nanami0088"
n "「う、ううん、なんでもないです～」"
"ヤバい、口に出していたみたい。"
"気をつけなきゃ、わたしっ！"


show char tna01s2 at sleft as l
with dis



voice "Nanami0089"
n "「あの……わたしでアドバイス出来ることなら、もちろん個人的にはするけれど、とにかく今はベストカップルのみんなにこの話をする方が良いんじゃない？」"
voice "Rikka_0205"
rk "「で、でも……先輩方は皆さん、委員を掛け持ちしたりで、お忙しいと聞いていますが……」"
voice "Nanami0090"
n "「その点なら大丈夫だよ、ねっ？」"


show char tsa01s2 at sleft as l
show char tna01s2
show char trk03s2 at sright as sr
with dis



"紗良さんの顔を見ると、彼女もうんうんと頷く。"
"璃紗さんと六夏さんは、何だかわからないって顔をしていた。"


show char tna02s2
with dis



voice "Nanami0091"
n "「ふっふっふっ、実はね……」"
"わたしは２人に、少し前の出来事を語って聞かせた……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//回想

#**委員会室・昼
scene bg bg30a
with rr


#mes on
#system on


"ちょっと前……まだ璃紗さんと美夜さんが、誤解からとんでもない事になっていた時期。"
"この２人を抜きにして、ちょっとした話し合いが行われていた。"


show char tma03s2
with dis



voice "Mai_0039"
ma "「まさかベストカップルの顔合わせで、こんなことになっちゃうなんてね」"


show char tyu03s2 at left
show char tma03s2 at right as r
with dis



voice "Yuuna_0014"
y "「あんなに仲が良い２人だし、早くなんとかしてあげたいわね……」"


#allClear:
hide char tyu03s2 at left
hide char tma03s2 at right as r
#lastBG:
#scene bg bg30a
show char tka01s2
with dis



voice "Kaede_0011"
sk "「紗良から聞いたんだけれど、六夏さんと璃紗さんは、幼なじみだったんでしょう？」"


show char tka01s2 at left
show char tsa01s2 at right as r
with dis



voice "Sara_0036"
sr "「うん、そうだよ。数年ぶりの再会で嬉しいのはわかるけど、六夏ちゃん、もう少し周りの空気を読まないと……だよね～」"


show char tka03s2 at left
with dis



voice "Kaede_0012"
sk "「紗良、貴女がそれを言うの？　私と再会したとき、貴女は私を……」"


show char tsa02s2 at right as r
with dis



voice "Sara_0037"
sr "「私を？　なぁに、楓ちゃん{image=image/exch001.png}」"


show char tka05s2 at left
with dis



voice "Kaede_0013"
sk "「な、なんでもありません……コホン」"


#allClear:
hide char tka05s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg30a
show char tre03s2
with dis



voice "Reo_0036"
re "「ねぇ、今日はお茶とか出ないの？」"


show char tma08s2 at left
show char tre03s2 at right as r
with dis



voice "Mai_0040"
ma "「シッ、みんなで話してんだから、あなたは余計なこと言わないの、玲緒」"


show char tre08s2 at right as r
with dis



voice "Reo_0037"
re "「ぶうっ、もう早く、仲直りさせればいーんでしょう」"


#allClear:
hide char tma08s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu03s2
with dis



voice "Yuuna_0015"
y "「そうね……でもその方法が、なかなか見つからないのよね」"


show char tyu03s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami0092"
n "「美夜さん、わたし達の話、全然聞いてくれないから……」"


#allClear:
hide char tyu03s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg30a
show char tka03s2
with dis



voice "Kaede_0014"
sk "「ああ見えて、璃紗さんのこととなると、もろかったりするのね」"


show char tka03s2 at left
show char tsa02s2 at right as r
with dis



voice "Sara_0038"
sr "「はぁ～い、紗良も楓ちゃんのことになると、ガラスのハートになります♪」"
voice "Kaede_0015"
sk "「そ、そう……」"


#allClear:
hide char tka03s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0041"
ma "「玲緒はガラスのハートどころか、暴れてガラスを割って歩きそうね」"


show char tma01s2 at left
show char tre01s2 at right as r
with dis



voice "Reo_0038"
re "「そんなことないわよ、ワタシだって繊細だものっ」"
voice "Mai_0042"
ma "「ほうほう」"


show char tre09s2 at right as r
with dis



voice "Reo_0039"
re "「もうっ、麻衣ったらワタシのことばかにして～、むきーっ！」"


#allClear:
hide char tma01s2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"話がだんだんと、ずれていく。"
"その度に誰かが、軌道修正をするけれど。"
"気がつけば、また違う話になってしまっていた。"
"周りが何を言おうが、取り合ってくれない美夜さん……一体、どうすればいいのか。"
"どうしてもそこから、先が浮かんでこなかった。"
"すっかり、膠着状態。"
"わたしもここで素敵なアイディアをひねりだして、お姉さまの手前、良いところを見せたいんだけど……全くのお手上げ。"
"代わりに別なことが気になって、うずうずしていた。"
"いいかな、言っちゃっても？"
"……いいよね、うん。"
"一瞬、話が止まった隙に、さりげなく言ってしまった。"


show char tna03s2
with dis



voice "Nanami0093"
n "「ところで、六夏さんと沙雪さんの事なんですが……」"


show char tsa01s2 at left
show char tna03s2 at right as r
with dis



voice "Sara_0039"
sr "「あっ、それ！　紗良も気になっていた」"
"早速、紗良さんが食いついてきた。"


#allClear:
hide char tsa01s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu02s2
with dis



voice "Yuuna_0016"
y "「ふふふっ、あの２人って……」"


show char tyu02s2 at left
show char tma01s2 at right as r
with dis



voice "Mai_0043"
ma "「そうね、あの２人って……」"

hide char tyu02s2 at left
hide char tma01s2 at right as r
show char tyu02s2 at sleft as l
show char tma01s2
show char tka01s2 at sright as sr
with dis



voice "Kaede_0016"
sk "「まだ……よね、きっと」"
"なぁんだ。"
"みんなも気になっていたのね。"


#allClear:
hide char tyu02s2 at sleft as l
hide char tma01s2
hide char tka01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tre07s2
with dis



voice "Reo_0040"
re "「な、何よ、みんなして、にやにやしちゃって」"
"若干一名、気づいていない人もいたみたいだけれど。"


show char tyu01s2 at left
show char tre07s2 at right as r
with dis



voice "Yuuna_0017b"
y "「昨年の璃紗ちゃん、美夜ちゃん同様、あの２人はまだ、本当のカップルにはなっていないみたいね」"


show char tre04s2 at right as r
with dis



voice "Reo_0041"
re "「えっ……そうなの？？」"


#allClear:
hide char tyu01s2 at left
hide char tre04s2 at right as r
#lastBG:
#scene bg bg30a
show char tka01s2
with dis



voice "Kaede_0017"
sk "「ええ、そんな雰囲気ですよね」"


show char tma01s2 at left
show char tka01s2 at right as r
with dis



voice "Mai_0044"
ma "「２人並ぶと、良い感じには見えるけど……まだどこか、よそよそしいというか」"


#allClear:
hide char tma01s2 at left
hide char tka01s2 at right as r
#lastBG:
#scene bg bg30a
show char tna03s2
with dis



voice "Nanami0094"
n "「でも、本当のところは……どうなんでしょう？」"


show char tyu01s2 at left
show char tna03s2 at right as r
with dis



voice "Yuuna_0018"
y "「六夏ちゃんは沙雪ちゃんに、恋しているように見えるわ」"


show char tna04s2 at right as r
with dis



voice "Nanami0095"
n "「えっ？」"


show char tyu03s2 at left
with dis



voice "Yuuna_0019"
y "「七海、あなた気づかなかったの？　環境整備委員の時、校舎のまわりを走っていた六夏ちゃんが、沙雪ちゃんに気づいて、立ち止まって見ていたわ」"


show char tna03s2 at right as r
with dis



voice "Nanami0096"
n "「し、知らなかった……です」"
"委員の時は、仕事がいっぱいいっぱいで、そんな余裕はなかったから……"


show char tyu02s2 at left
with dis



voice "Yuuna_0020"
y "「あれは間違いなく、恋をしている目だわ～」"
"うっとりとお姉さまがそう言うと、他のみんなも同意してうんうん頷いた。"


#allClear:
hide char tyu02s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa01s2
with dis



voice "Sara_0040"
sr "「六夏ちゃんが沙雪ちゃんに惚れているのは、間違いないとして……沙雪ちゃんはどうなんだろうね」"


show char tsa01s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami0097"
n "「どうなのかな？　環境整備委員で一緒の時も、他愛ない話はするけれど、そこまで踏み込んだ話はしたことないし」"


#allClear:
hide char tsa01s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg30a
show char tma03s2
with dis



voice "Mai_0045"
ma "「誰に対しても、礼儀正しくて、気品あふれるお嬢様って感じだから……率先してコイバナとかするのは想像つかないわね」"


show char tka01s2 at left
show char tma03s2 at right as r
with dis



voice "Kaede_0018"
sk "「じゃあ……やっぱり、六夏さんの片思いってところかしら」"
"大体、みんな同じような意見みたい。"
"何か、他の意見はないのかしら……誰もがそう思い、発言を待っていると……"


#allClear:
hide char tka01s2 at left
hide char tma03s2 at right as r
#lastBG:
#scene bg bg30a
show char ter02f2
with dis



voice "Erisu_0005"
e "「なんだかみんな、楽しそうな話してるね～♪」"
"突然、乱入者が現れた。"


show char ter02f2 at left
show char tre04s2 at right as r
with dis



voice "Reo_0042"
re "「えっ、エリスっ！」"
voice "Erisu_0006"
e "「玲緒、久しぶり{image=image/exch001.png}　相変わらずちっこいわね」"


show char tre08s2 at right as r
with dis



voice "Reo_0043"
re "「くっ……ここで会ったが１０年目、今日こそ決着をつけてやってもいいのよ」"
voice "Erisu_0007"
e "「ふふふっ……どんな勝負だって、受けて立つわ」"
"いきなりエリスさまと玲緒さま、対決モード突入！？"


show char ter02f2 at sleft as l
show char tsi08f2
show char tre08s2 at sright as sr
with dis



voice "Sizuku0001"
sk "「ちょっと、エリス……いきなり何をしているんですか？」"
"エリスさまの後ろから雫さまが現れて、２人をいさめてくれた。"


show char ter01f2 at sleft as l
with dis



voice "Erisu_0008"
e "「もう、冗談だって、シズク。これはワタシと玲緒のコミュニケーションなんだから」"
voice "Sizuku0002"
sk "「はいはい、そういうことは外で、２人だけでしてください。皆さんは何か、真面目な話し合いをしているようですし」"


#allClear:
hide char ter01f2 at sleft as l
hide char tsi08f2
hide char tre08s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0046"
ma "「話し合いというか……乙女の雑談なんですけれど」"
"仲の良い雫さまに挨拶しながら、麻衣さまが苦笑いする。"


show char tyu01s2
with dis



voice "Yuuna_0021"
y "「エリスさま、雫さま……今日はどうなさったのですか？」"


show char ter01f2
with dis



voice "Erisu_0009"
e "「授業が休校になっちゃって、時間空いたから遊びに来ちゃった。そしたら面白そうな話が聞こえてきたんで……」"
"こういう話、エリスさまもどうやら興味津々のご様子。"
"空いている席に２人が座ると、それまでのことをみんなで説明した。"


show char ter01f2 at left
show char tsi01f2 at right as r
with dis



voice "Sizuku0003"
sk "「六夏さんと沙雪さんのかっぷるは、まだ本当のかっぷるじゃないんですか……」"
voice "Erisu_0010"
e "「それをワタシたちの力で、本物のカップルにするのね」"


#allClear:
hide char ter01f2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg30a
show char tka03s2
with dis



voice "Kaede_0019"
sk "「い、いえ、そういう話じゃ……本人の気持ちも大事ですし……」"


show char tyu01s2 at left
show char tka03s2 at right as r
with dis



voice "Yuuna_0022"
y "「あらっ、楓さん。私はそれ、良いアイディアだと思いますが」"


show char tna04s2 at right as r
with dis



voice "Nanami0098"
n "「ちょ、ちょっと、おね……優菜さまっ！」"
"おっとりと、お姉さまがとんでもないことを言い出した。"


#allClear:
hide char tyu01s2 at left
hide char tna04s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa02s2
with dis



voice "Sara_0041"
sr "「わぁ、紗良はそれ、いいと思いますー！」"


show char tma02s2 at left
show char tsa02s2 at right as r
with dis



voice "Mai_0047"
ma "「うん……悪くないわね」"
"みんなも次々と、賛同していく。"


#allClear:
hide char tma02s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0023"
y "「ねぇ、七海はどうなの？」"


show char tyu01s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami0099"
n "「えっ……その……」"
"お姉さまが小首をかしげながら聞いてくる。"
"そんなの……"


show char tna01s2 at right as r
with dis



voice "Nanami0100"
n "「さ……賛成です！　いいです」"
"賛成するに決まってるじゃないですか。"


#allClear:
hide char tyu01s2 at left
hide char tna01s2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0048"
ma "「とはいえ、２人の詳しい状況がまだわかっていないのよね……もっと詳しい情報が欲しいわ」"


show char tsi01f2 at left
show char tma01s2 at right as r
with dis



voice "Sizuku0004"
sk "「そうですね。ちゃんと話を聞いてみてから、手伝うなり応援するなりした方が良いと思います」"


show char ter01f2 at left
show char tsi01f2 at right as r
with dis



voice "Erisu_0011"
e "「シズク、すっごいやる気になってるね……こういうの好きなの？」"
voice "Sizuku0005"
sk "「いえ、ですがどうせやるなら、完璧にしたいからです」"


show char ter02f2 at left
show char tsi01f2 at right as r
with dis



voice "Erisu_0012"
e "「うんうん、シズクらしい意見だね」"


#allClear:
hide char ter02f2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg30a
show char tre01s2
with dis



voice "Reo_0044"
re "「ワタシは……どうでもいいわ」"


show char tma01s2 at left
show char tre01s2 at right as r
with dis



voice "Mai_0049"
ma "「そうね、玲緒はマスコットキャラ担当だから、そこにいるだけでいいよ。というか、玲緒に恋愛相談とかありえないし」"


show char tre08s2 at right as r
with dis



voice "Reo_0045"
re "「んっ？　なによ、ワタシだって人の相談くらい、しっかり聞けるわ」"
voice "Mai_0050"
ma "「そうね……じゃあ玲緒には、今晩のおかずを何にするかという、わたしの高尚な悩み相談にでも乗ってもらうわ」"


show char tre03s2 at right as r
with dis



voice "Reo_0046"
re "「ぅぅ……なんかバカにされてるような……でも今日は、目玉焼きのせハンバーグが良いと思うわ」"
voice "Mai_0051"
ma "「はい、ありがとう」"

hide char tma01s2 at left
hide char tre03s2 at right as r
show char ter02f2 at sleft as l
show char tma01s2
show char tre03s2 at sright as sr
with dis



voice "Erisu_0013"
e "「ぷぷっ……玲緒、可愛い♪」"


#allClear:
hide char ter02f2 at sleft as l
hide char tma01s2
hide char tre03s2 at sright as sr
#lastBG:
#scene bg bg30a
show char ter02f2 at left
show char tre09s2 at right as r
with dis



voice "Reo_0047"
re "「な、なによ～」"
"ああ、また話が脱線し始めた。"
"せっかく盛り上がってきたので、すかさずお姉さまが修正を入れる。"


#allClear:
hide char ter02f2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0024"
y "「とにかく、まずは璃紗ちゃんと美夜ちゃんよね……そっちの問題が収まってから、六夏ちゃんたちの話を聞いてみましょうよ」"


show char ter04f2
with dis



voice "Erisu_0014"
e "「えぇっ、あの２人……まだ揉めていたんだね」"


show char ter04f2 at left
show char tsi03f2 at right as r
with dis



voice "Sizuku0006"
sk "「早く仲直り出来ればいいですね……離れ離れは寂しいです」"


show char ter02f2 at left
with dis



voice "Erisu_0015"
e "「シズクとワタシはずーっとくっついているから、大丈夫だよ～」"


show char tsi05f2 at right as r
with dis



voice "Sizuku0007"
sk "「ひゃっ、だ、抱きつかないで下さい、エリス。皆さんが、見てますから……ぁん」"


#allClear:
hide char ter02f2 at left
hide char tsi05f2 at right as r
#lastBG:
#scene bg bg30a
with dis


"そんな感じで、最後はドタバタしてしまったけれど。"
"その場にいたメンバー全員、六夏さんの恋を応援しようということになったのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//回想終了

#**カフェ・昼
scene bg bg36a
with lr


#mes on
#system on


show char tna01s2
with dis



voice "Nanami0101"
n "「……というわけなの」"


show char tna01s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0316"
r "「そっか……私たちのことでみんな、そんな話し合いをしていたなんて……まったく知らなかったわ」"

hide char tna01s2 at left
hide char tri03s2 at right as r
show char tna01s2 at sleft as l
show char tri03s2
show char trk05s2 at sright as sr
with dis



voice "Rikka_0206"
rk "「環境整備委員の教室、覗いていたのバレていたなんて……うぅっ、なんかすごく恥ずかしい……」"
"六夏さん、思いっきりうつむいてしまったみたい。"
"やっぱりみんなに片思いがバレて、ショックだったのかしら？"


show char trk03s2 at sright as sr
with dis



voice "Rikka_0207"
rk "「それにしても、優菜さまって……何者なの？」"
"小声で何か呟いていたけれど、よく聞こえなかった。"
"多分、お姉さまに感謝しているのよね。"
"最初に六夏さんの恋の応援をしましょうって言ったのも、お姉さまだもの\001"


#allClear:
hide char tna01s2 at sleft as l
hide char tri03s2
hide char trk03s2 at sright as sr
#lastBG:
#scene bg bg36a
show char tsa02s2
with dis



voice "Sara_0042"
sr "「璃紗ちゃんたちが無事、仲直りした今、もう問題はないわけだし～♪」"


show char tsa02s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0102"
n "「みんなで、六夏さんの力になりますよ！！」"


#allClear:
hide char tsa02s2 at left
hide char tna01s2 at right as r
#lastBG:
#scene bg bg36a
show char trk04s2
with dis



voice "Rikka_0208"
rk "「歴代ベストカップルが、協力してくれるなんて……」"
"呆然としてる六夏さんの背中を、璃紗さんがパン、と叩いた。"


show char tri02s2 at left
show char trk04s2 at right as r
with dis



voice "Risa_0317"
r "「良かったね、六夏。皆さん良い人ばかりだから、きっと頼りになるわよ」"


show char trk01s2 at right as r
with dis



voice "Rikka_0209"
rk "「リサ姉……」"
"六夏さんは漠然と、不安を感じているようにも見えるけれど。"
"お姉さまをはじめとした、強力な仲間がついているのだもの……きっと、悪いことにはならないわ。"
"そうわたしは、強く確信したのだった。"


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
jump S012



