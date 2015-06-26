#「美夜はいつでも、負けず嫌い」

label S056:
$ save_name = "◇美夜はいつでも、負けず嫌い"


#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP06
play music "sound/BGM06.ogg"


show char tna01s2
with dis



voice "Nanami0269"
n "「あっ、璃紗さんちょうど良い所に！　良かったら、手伝ってもらえない？」"
"イベント実行委員に行こうとしてたら、大きな箱を２つ抱えた七海さんに声をかけられた。"


show char tri01s2 at left
show char tna01s2 at right as r
with dis



voice "Risa_1103"
r "「大変そうね、手伝うわ……はい」"
"とりあえず七海さんから、その箱を１つ受け取った。"
voice "Nanami0270"
n "「ありがとう、璃紗さん。いきなりごめんなさい」"
voice "Risa_1104"
r "「そんなに重くないから、大丈夫よ。ところでこれ、どこまで運べばいいのかしら？」"
voice "Nanami0271"
n "「いつもの委員会室まで、お願い」"
voice "Risa_1105"
r "「わかったわ。これ、文化祭の準備で使うもの？」"
voice "Nanami0272"
n "「うちの学校の文化祭招待券、さっき環境整備委員の方に届いてたんだけど、券と封筒が別だからセットにしないといけないから……」"
voice "Risa_1106"
r "「そう、それをイベント実行委員のみんなでやるのね」"
voice "Nanami0273"
n "「うん、そのつもり。こういう雑務って結構、多いんだよね～」"
voice "Risa_1107"
r "「そうね……でも、楽しいわよね」"


show char tna02s2 at right as r
with dis



voice "Nanami0274"
n "「ええ、こういうのが上がってくるたびに、わくわくしちゃう♪」"


show char tri02s2 at left
with dis



voice "Risa_1108"
r "「私もだわ……ふふっ」"
"２人で思わず、笑い合う。"
"忙しくはあるけれど、楽しみの方が大きいから。"
"それはやっぱり……美夜が一緒だからじゃないかと、今ははっきりと自覚していた。"
"準備もだけど、きっと当日だって、美夜と一緒に過ごすことになりそうな文化祭。"
"ああ……想像しただけでも、ドキドキしてきちゃう。"


show char tna01s2 at right as r
with dis



voice "Nanami0275"
n "「璃紗さん知ってる？　うちの学校の文化祭招待券、すっごい人気があるみたい」"


show char tri01s2 at left
with dis



voice "Risa_1109"
r "「へぇ～、そうなの？」"
voice "Nanami0276"
n "「世間ではなかなか手に入らない、レアアイテムなんだって」"
voice "Risa_1110"
r "「あっ……なんか、わかるような気がするわ」"
"他の学校はどうか、わからないけれど。"
"ウチの学校は文化祭とはいえ、校内に入れるのは在校生の身内か、卒業生くらい。"
"または、ミカ女の関係者だけ……って、聞いたことがある。"
voice "Nanami0277"
n "「楓さまや紗良さんみたいな有名人もいるから、今年は余計に人気みたい」"
voice "Risa_1111"
r "「なるほどね……」"
voice "Nanami0278"
n "「文化祭前になると、急に親戚が増えるなんて笑い話もあるぐらいだし」"


show char tri03s2 at left
with dis



voice "Risa_1112"
r "「それは……笑い話ではすまなさそうね」"
voice "Nanami0279"
n "「ところで璃紗さんは、誰を招待するか、決めた？」"
voice "Risa_1113"
r "「私は……うーん……」"
"やっぱり、ママかな？"
"それと。"
"ママの恋人も、呼んでみたいかも……来てくれるかしら？"
"２人ともミカ女の卒業生だから、懐かしいって思うかもしれないわよね。"


show char tri01s2 at left
with dis



voice "Risa_1114"
r "「２人が来てくれたら……ちょっと、嬉しいかも」"
voice "Nanami0280"
n "「えっ、２人って誰？　璃紗さんのお友達？？」"
voice "Risa_1115"
r "「もし来てもらえたら、七海さんにも紹介するわね」"
"そんな話をしているうちに、私たちは教室に到着した。"


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


show char trk01s2
with dis



voice "Rikka_1547"
rk "「リサ姉、ごきげんよう」"


show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0845"
s "「璃紗さま、ごきげんよう」"
"教室に入ると早速、六夏が駆け寄ってきて、私が持っていた箱を受け取ってくれる。"

hide char trk01s2 at left
hide char tsy01s2 at right as r
show char tri02s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Risa_1116"
r "（ふふっ……すぐにこういう風に体が動くのが、六夏の王子さまっぽいところなのよね）"
voice "Risa_1117"
r "「六夏、ありがとう。空いてるところに置いたら、中開けてくれる？」"
voice "Rikka_1548"
rk "「はい、リサ姉」"
"テキパキと働く六夏を、沙雪さんが熱いまなざしで見つめている。"


show char tsy02s2 at sright as sr
with dis



voice "Sayuki0846"
s "「六夏さん……六夏さんは本当に、仕事が早いですね{image=image/exch001.png}」"


show char trk05s2
with dis



voice "Rikka_1549"
rk "「い、いえ、そんなぁ、もう……んふ、んふふっ」"
voice "Risa_1118"
r "「あらあら、六夏ったら……照れちゃってるわ。可愛い」"


#allClear:
hide char tri02s2 at sleft as l
hide char trk05s2
hide char tsy02s2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"私は私で、七海さんの方の箱を開ける手伝いをする。"


show char tna02s2
with dis



voice "Nanami0281"
n "「六夏さんと沙雪さん、なんか良い感じだね～」"


show char tri02s2 at left
show char tna02s2 at right as r
with dis



voice "Risa_1119"
r "「そうね、かなり仲良くなったように見えるわね」"
"後輩カップルを暖かい目で見守る、私たち。"


#allClear:
hide char tri02s2 at left
hide char tna02s2 at right as r
#lastBG:
#scene bg bg30a
show char trk05s2
with dis



"その視線に気づいたのか、六夏がパッと赤くなった。"


show char trk05s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0847"
s "「六夏さん、どうかなさいました？」"


show char trk01s2 at left
with dis



voice "Rikka_1550"
rk "「な、なんでもないです……リサ姉、七海さま、この後どうすればいいんですか？」"

hide char trk01s2 at left
hide char tsy03s2 at right as r
show char tna01s2 at sleft as l
show char trk01s2
show char tsy03s2 at sright as sr
with dis



voice "Nanami0282"
n "「こっちの封筒の中に招待券を入れて、セットにしてください」"
voice "Rikka_1551"
rk "「はい、わかりました。それでは始めましょうか、沙雪さん」"


show char tsy01s2 at sright as sr
with dis



voice "Sayuki0848"
s "「はい」"


#allClear:
hide char tna01s2 at sleft as l
hide char trk01s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"２人で仲良く、てきぱきと作業を始める。"


show char tyu04s2
with dis



voice "Yuuna_0175"
y "「あら……招待状、もう来ていたのね？」"
"教室の中心でみんなに指示を出していた優菜さまが、私たちに気づいて、傍にやってきた。"


show char tyu04s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0283"
n "「はい。今、持ってきたところです」"


show char tyu01s2 at left
with dis



voice "Yuuna_0176"
y "「ご苦労様。六夏ちゃんと沙雪ちゃんも、頑張っているのね」"
"作業をする２人を見て、優菜さまも嬉しそうに微笑む。"


show char tyu02s2 at left
with dis



voice "Yuuna_0177"
y "「愛し合う２人の、共同作業ね……うふふ{image=image/exch001.png}」"


show char trk04s2 at right as r
with dis



voice "Rikka_1552"
rk "「ええっ？」"

hide char tyu02s2 at left
hide char trk04s2 at right as r
show char tyu02s2 at sleft as l
show char trk04s2
show char tsy02s2 at sright as sr
with dis



voice "Sayuki0849"
s "「はい。私と六夏さんはそれはもう、深く愛し合っておりますから{image=image/exch001.png}」"


show char trk05s2
with dis



voice "Rikka_1553"
rk "「さ、沙雪さんっ！？」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0175"
sr "「おやおやぁ、六夏ちゃん、表情が硬いよ～！　沙雪ちゃんみたいに堂々としないとね♪」"
"優菜さまにのっかるように、紗良さんが２人を冷やかすと、六夏はますます顔を赤くしてしまった。"


#allClear:
hide char tsa02s2 at sleft as l
hide char trk05s2
hide char tsy02s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0178"
y "「ふふふっ、六夏ちゃん手が止まってるわよ。こういうのは……こうやってやらなくちゃ」"

#しゅっ！
#♀SE029
play sound "sound/SE029.ogg"


show char tyu01s2 at left
show char tna02s2 at right as r
with dis



voice "Nanami0284"
n "「おね……じゃなくて、優菜さま、すごいです～」"
"ものすごい早業で、優菜さまが招待状のセットを作り上げていく。"

hide char tyu01s2 at left
hide char tna02s2 at right as r
show char tri02s2 at sleft as l
show char tyu01s2
show char tna02s2 at sright as sr
with dis



voice "Risa_1120"
r "「わぁ、本当にすごいわ」"


#allClear:
hide char tri02s2 at sleft as l
hide char tyu01s2
hide char tna02s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tmi01s2 at left
show char tri02s2 at right as r
with dis



voice "Miya_0693"
m "「ん……何がすごいのかしら、璃紗？」"


show char tri04s2 at right as r
with dis



voice "Risa_1121"
r "「えっ、美夜！？」"
"さっきまで向こうの方で、玲緒さまたちと別作業をしていたのに。"
"まるで瞬間移動でもしたかのように、美夜は私たちの輪の中に入ってきた。"
voice "Miya_0694"
m "「この招待状を、封筒に入れるだけでいいの？　それなら、わたくしだってできるわよ」"

#しゅしゅ！！
#♀SE030
play sound "sound/SE030.ogg"

hide char tmi01s2 at left
hide char tri04s2 at right as r
show char tmi01s2 at sleft as l
show char tri04s2
show char tna02s2 at sright as sr
with dis



voice "Nanami0285"
n "「わぁ、美夜さんもすごいですね」"


show char tri03s2
with dis



voice "Risa_1122"
r "「確かに、すごいけど……」"
"美夜ったら……別に張り合うことじゃないわよね、これって？"


#allClear:
hide char tmi01s2 at sleft as l
hide char tri03s2
hide char tna02s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tmi01s2 at left
show char tyu01s2 at right as r
with dis



voice "Yuuna_0179"
y "「美夜ちゃん、やるわね……さすがに速いわ」"
voice "Miya_0695"
m "「ええ……こんなの、簡単です」"


show char tyu02s2 at right as r
with dis



voice "Yuuna_0180"
y "「うふふ……私もあれが、最速ではなくってよ？」"
voice "Miya_0696"
m "「わたくしもです……今のは全力の２０％くらいですから」"

#しゅしゅしゅ！！
#♀SE031
play sound "sound/SE031.ogg"
pause 1
# 此处原对应代码"#se 0 wait"，但在sound文件夹内未找到wait.ogg，因此意图不明，暂以pause代替。
# Original script is "#se 0 wait", but I cannot find wait.ogg inside sound folder, so replace it with pause at this time.

#しゅしゅしゅしゅしゅっ！！
#♀SE032
play sound "sound/SE032.ogg"


"競い合うように、２人でどんどん作業が進んでいく。"
"その２人を六夏たちは呆然と、驚きの眼差しで見つめていた。"


#allClear:
hide char tmi01s2 at left
hide char tyu02s2 at right as r
#lastBG:
#scene bg bg30a
show char trk04s2
with dis



voice "Rikka_1554"
rk "「なっ、なんなんですか、これは？」"


show char trk04s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0850"
s "「素晴らしいですね{image=image/exch001.png}　六夏さんも先輩たちのように、やってみて下さい」"


show char trk03s2 at left
with dis



voice "Rikka_1555"
rk "「さすがにワタシでも、これは……」"


#allClear:
hide char trk03s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"いくら六夏でも、無理でしょうね。"
"だってこの２人は、本当に特別製なんだから。"


show char tsa01s2
with dis



voice "Sara_0176"
sr "「１年前の対決、思い出すねぇ～」"


show char tsa01s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0286"
n "「ええ、本当に……」"


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


"美夜と優菜さまの活躍により、招待状セットは一瞬ででき上がってしまった。"


show char tri04s2
with dis



voice "Risa_1123"
r "「あれだけの量があったのに、もう終わっちゃったわね」"


show char tri04s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0287"
n "「でもその分、他の仕事にまわせる時間ができて、良かったんじゃないですか？」"


show char tri01s2 at left
with dis



voice "Risa_1124"
r "「美夜の負けず嫌いが、仕事の効率を上げたわね……んっ？」"
"もしかして……ちょっと妙案、ひらめいたかも。"


#allClear:
hide char tri01s2 at left
hide char tna01s2 at right as r
#lastBG:
#scene bg bg30a
show char tri03s2
with dis



voice "Risa_1125"
r "「美夜のこの、負けず嫌いなところを利用して……ちゃんと授業に出させる方法、あるんじゃないかしら……」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Miya_0697"
m "「そんなの、考えるだけ無駄よ」"


show char tri08s2 at right as r
with dis



voice "Risa_1126"
r "「もう……すぐに否定しなくても」"
voice "Miya_0698"
m "「今のは余計な考えに囚われて、作業に集中出来なくなりそうな璃紗を止めるために教えてあげたのよ。効率的でしょう？」"


show char tri03s2 at right as r
with dis



voice "Risa_1127"
r "「うううっ……」"
"美夜ってああ言えば、こう言うなんだから……もう！"
hide char tmi01s2 at left
hide char tri03s2 at right as r
show char tyu01s2 at sleft as l
show char tmi01s2
show char tri03s2 at sright as sr
with dis



voice "Yuuna_0181"
y "「はいはい、お喋りはそこまでにして、それぞれの作業に戻ってね」"


show char tri01s2 at sright as sr
with dis



voice "Risa_1128"
r "「は、はいっ」"
voice "Miya_0699"
m "「………………」"


#allClear:
hide char tyu01s2 at sleft as l
hide char tmi01s2
hide char tri01s2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"優菜さまに注意されたと思ったら、美夜はまた一瞬で前の作業に戻っていた。"


show char tri01s2
with dis



voice "Risa_1129"
r "（なんだかんだで、要領がいいわよね、美夜って）"


#allClear:
hide char tri01s2
#lastBG:
#scene bg bg30a
with dis


"………………"
"その後は黙々と作業を続けて、少し疲れたと思い始めた頃。"


show char ter02f2
with dis



voice "Erisu_0111"
e "「失礼します～♪　みんな、お手伝いに来たよ」"


show char ter02f2 at left
show char tsi02f2 at right as r
with dis



voice "Sizuku0095"
sk "「ごきげんよう、皆さん」"
"差し入れを持ってエリスさまたちが、やって来てくれた。"


#allClear:
hide char ter02f2 at left
hide char tsi02f2 at right as r
#lastBG:
#scene bg bg30a
show char tre08s2
with dis



voice "Reo_0187"
re "「エリス、やっと来たわねー、最近全然、顔見せないじゃない」"


show char tre08s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0112"
e "「今のはツンデレ翻訳機にかけると『エリスに会えて嬉しい、ワタシずっと待ってたのよ』でいいのかしら？」"

hide char tre08s2 at left
hide char ter01f2 at right as r
show char tma02s2 at sleft as l
show char tre08s2
show char ter01f2 at sright as sr
with dis



voice "Mai_0244"
ma "「はい、正解です。エリスさまも玲緒のこと、わかってきましたね」"


#allClear:
hide char tma02s2 at sleft as l
hide char tre08s2
hide char ter01f2 at sright as sr
#lastBG:
#scene bg bg30a
show char tsi01f2
with dis



voice "Sizuku0096"
sk "「つんでれ翻訳機ですか？」"


#allClear:
hide char tsi01f2
#lastBG:
#scene bg bg30a
show char tre09s2
with dis



voice "Reo_0188"
re "「ワタシはそんなこと、一言も言ってなぁーーーーい！」"


#allClear:
hide char tre09s2
#lastBG:
#scene bg bg30a
with dis


"エリスさまたちが来ると、騒がしくなるけれど。"
"良いリフレッシュにもなるわね。"
"卒業した後でも、後輩たちの面倒を見たり様子を伺ってくれたり。"
"２人とも本当に、尊敬できる先輩たちだわ。"


show char tri01s2
with dis



voice "Risa_1130"
r "「私もいつか、あんな風になりたいなぁ～」"


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



voice "Miya_0700"
m "「ん……それは無理ね」"


show char tri03s2 at right as r
with dis



voice "Risa_1131"
r "「……な、なんでよ。というか私が何を考えてたのか、美夜わかっているの？」"
voice "Miya_0701"
m "「わかるわよ、璃紗の考えそうなことくらい」"
voice "Miya_0702"
m "「ちなみに卒業後の璃紗は後輩じゃなくて、わたくしの面倒だけを見ることになるから、エリスさまたちみたいな余裕はないわよ」"


show char tri05s2 at right as r
with dis



voice "Risa_1132"
r "「な、何言ってるの～」"

hide char tmi01s2 at left
hide char tri05s2 at right as r
show char tmi01s2 at sleft as l
show char tri05s2
show char tsa01s2 at sright as sr
with dis



voice "Sara_0177"
sr "「わわっ、何気なく美夜ちゃんが璃紗ちゃんと、ラブラブトークしてる」"


show char tri04s2
with dis



voice "Risa_1133"
r "「違う、違うわよ、紗良さん」"
voice "Miya_0703"
m "「いいえ、違わないわよ」"


#★★★選択肢　ここから


#美夜は勝手に、紗良さんの冷やかしを認めてしまっていた。
#でも、私は……


#++選択肢（２）
#１．『とにかく、はぐからす』○
#２．『とにかく、否定する』×
menu:
 "とにかく、はぐからす":
  jump select11_1
 "とにかく、否定する":
  jump select11_2



#１．『とにかく、はぐからす』
label select11_1:


show char tri03s2
with dis



voice "Risa_1134"
r "「ラブラブトークではなく、自分たちがどんな先輩になりたいか、美夜と相談を……」"


show char ter02f2 at sleft as l
show char tmi01s2
show char tri03s2 at sright as sr
with dis



voice "Erisu_0113"
e "「それだって立派な、ラブラブトークだよ{image=image/exch001.png}　ねっ、美夜さん？」"
voice "Miya_0704"
m "「はい、エリスさま」"
voice "Risa_1135"
r "「くぅぅっ、なんでそうなっちゃうのよぉ、もう……」"


#set f1 f1+1
jump select11_end


#２．『とにかく、否定する』
label select11_2:


show char tri07s2
with dis



voice "Risa_1136"
r "「とにかく私は、人前では恥ずかしい話は絶対にしませんっ！」"


show char ter02f2 at sleft as l
show char tmi01s2
show char tri07s2 at sright as sr
with dis



voice "Erisu_0114"
e "「人前では、しないのね……じゃあ２人きりの時は、美夜さんとどんな話をするのかな？」"
voice "Miya_0705"
m "「それはですね、エリスさま……こう見えて璃紗は、わたくしと２人きりだと……」"


show char tri04s2 at sright as sr
with dis



voice "Risa_1137"
r "「わーわーわーっ！！　もう余計なことは言わないで、美夜っ！！」"


#++選択肢終了
#★★★選択肢　ここまで
label select11_end:


voice "Erisu_0115"
e "「うんうん、玲緒も元気だけど、璃紗さんたちも元気だね♪」"


#allClear:
hide char ter02f2 at sleft as l
hide char tmi01s2
hide char tri04s2 at sright as sr
#lastBG:
#scene bg bg30a
show char ter02f2 at left
show char tsi02f2 at right as r
with dis



voice "Sizuku0097"
sk "「このお２人も相変わらずの仲の良さですわね」"


#allClear:
hide char ter02f2 at left
hide char tsi02f2 at right as r
#lastBG:
#scene bg bg30a
show char tri03s2
with dis



voice "Risa_1138"
r "「うううっ、もう、ああ……」"
"なんでいつも、こうなるのかしら。"
"イベント実行委員で、美夜がよく話すようになってきたのは、良い事だけど。"
"こういう話は、２人だけの時にしてもらいたいわね……本当に。"


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
jump S057



