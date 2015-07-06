# 此脚本为共通线结束，含有最终决定玩家将前往哪条路线的多个选项，需要使用判定条件。
# 我们选用if条件判定玩家是否选择了对应的选项，但因为if后接的判定名称事先未定义，
# 我们可以在label前使用default来预定义这些判定调教的名称并先设置为False。
# 待玩家选中相应路线的选项后，使用$来将变量设置为True，然后脚本末尾使用if判定。
# 我在这里研究了非常久，最终发现if与menu一样，对每个区块的空格数量要求非常严格。
# 具体请参见脚本内容。
# This is the end of the public route, which contains options to go to different route, so we need to use conditional statements.
# We chose "if" statement to judge whether player have choose the option or not, but because we did not define the name we use to judge,
# So we can use "default" to pre-define those name and set as "Fasle" at first.
# Then wait to the players choose one option, set the corresponding judgement as "True" by using "$". And use "if" at the end to judge what player have chosen.
# I was trapped here a long time, finally I noticed that not just the "menu" statement, "if" statement also have a strict requirement in numbers of spaces.
# For details, just look at this script.

#「本当の気持ち」
default risa_route = False
default nanami_route = False
default reo_route = False
default sara_route = False
default rikka_route = False
label S030:
$ save_name = "◇本当の気持ち"

#**ビーチ・夜
scene bg bg39c
with Dis



#mes on
#system on


#♂MP13
play music "sound/BGM13.ogg"


show char trn02m
with dis



voice "Rena_0076"
ren "「最後の夜よ。今日はめいいっぱい、盛り上がってね！」"


show char trk03m
with dis



voice "Rikka_0576"
rk "「………………」"
"ワタシはもやもやとした気持ちを抱えたまま、バカンスは最終日を迎えた。"
"初めての夜と同じように、麗奈先生がみんなをビーチに集めて、超ド級派手なバーベキューパーティが開催された。"


show char tre02m
with dis



voice "Reo_0172"
re "「肉だ～、肉だ～、焼き肉だ～！」"


show char tma08m at left
show char tre02m at right as r
with dis



voice "Mai_0223"
ma "「玲緒、もう少しゆっくり食べなさい」"


#allClear:
hide char tma08m at left
hide char tre02m at right as r
#lastBG:
#scene bg bg39c
show char tyu02m
with dis



voice "Yuuna_0138"
y "「このフルーツポンチ、七海の好きなイチゴもいっぱい入ってるわよ。よそってあげるわね～♪」"


show char tyu02m at left
show char tna01m at right as r
with dis



voice "Nanami0250"
n "「ありがとうございます～、甘くて美味しいです……でも、ちょっと変わった味が」"


#allClear:
hide char tyu02m at left
hide char tna01m at right as r
#lastBG:
#scene bg bg39c
show char tsa01m
with dis



voice "Sara_0142"
sr "「どれどれ……んっ、これリキュールが入ってるんだよ。食べ過ぎたら酔っ払うよ」"


show char tka08m at left
show char tsa01m at right as r
with dis



voice "Kaede_0114"
k "「と言いながら、紗良はたくさんよそらないの」"


show char tsa02m at right as r
with dis



voice "Sara_0143"
sr "「酔ったら、楓ちゃんがちゃーんと介抱してね{image=image/exch001.png}」"


show char tka04m at left
with dis



voice "Kaede_0115"
k "「えええっ？」"


#allClear:
hide char tka04m at left
hide char tsa02m at right as r
#lastBG:
#scene bg bg39c
show char tyu02m
with dis



voice "Yuuna_0139"
y "「私も七海を介抱して、あーんなことやこーんなことしてあげるから、安心してたくさん食べていいわよ{image=image/exch001.png}」"


show char tyu02m at left
show char tna03m at right as r
with dis



voice "Nanami0251"
n "「えっと……そろそろ、スペアリブが焼けた頃なんで、もらってきますー」"


hide char tna03m at right as r
show char tyu03m at left
with dis


voice "Yuuna_0140"
y "「あーん、七海ぃ～」"


show char trk03m
with dis



voice "Rikka_0577"
rk "「みんな、盛り上がっているけれど……」"
"ワタシはなんだか、食欲がわかなかった。"
"美味しそうな匂いはしているのに……"
voice "Rikka_0578"
rk "「バカンスも、終わりか。明日からは……」"
"沙雪さんとワタシは、きっと別々の生活が待っている。"
"もう決して、交わることはない……"


show char tri01m at left
show char trk03m at right as r
with dis



voice "Risa_0780"
r "「六夏、全然食べてないじゃない」"
voice "Rikka_0579"
rk "「あっ、なんか……お腹いっぱいで」"
"ワタシの皿の上では、分けてもらったお肉がすっかり冷めている。"


show char tri08m at left
with dis



voice "Risa_0781"
r "「食べ物を粗末にしちゃダメよ」"
"冷めた肉を、リサ姉が自分の皿の上に移しかえた。"
voice "Rikka_0580"
rk "「あっ……ごめんなさい」"


show char tri01m at left
with dis



voice "Risa_0782"
r "「謝らなくてもいいわ。六夏と同じく食欲ない子が、あそこにもう一人いるみたいだし」"


#allClear:
hide char tri01m at left
hide char trk03m at right as r
#lastBG:
#scene bg bg39c
show char tsy03m
with dis



voice "Sayuki0248"
s "「………………」"
"リサ姉が顔を向けた先には、沙雪さんがいた。"
"寂しそうに、みんなの輪からはずれて佇んでいる。"


show char tri03m at left
show char trk03m at right as r
with dis



voice "Risa_0783"
r "「彼女も全然、食べてないみたいよ」"
voice "Rikka_0581"
rk "「沙雪さん……」"


#allClear:
hide char tri03m at left
hide char trk03m at right as r
#lastBG:
#scene bg bg39c
show char tma01m
with dis



voice "Mai_0224"
ma "「璃紗ちゃん、ちょっとこっち手伝って～」"


show char tri01m at left
show char trk03m at right as r
with dis



voice "Risa_0784"
r "「はーい、今行きます！」"
"そう返事をしてから、リサ姉はワタシに向き直る。"
voice "Risa_0785"
r "「呼ばれてるから、私行くね。六夏、食欲なくてもせめて、フルーツくらいは食べなさいね……空腹じゃ、いざという時に気合入らないわよ」"


hide char tri01m at left
with dis


"世話好きのリサ姉らしい言葉を残し、行ってしまった。"


#allClear:
hide char trk03m at right as r
#lastBG:
#scene bg bg39c
show char trk03m
with dis



voice "Rikka_0582"
rk "「でも……気合なんてもう、入らなくていいよ……」"
"先日の告白と、沙雪さんの真実を受け止めるだけで、気力は使い果たしてしまったし。"
"気になってもう一度、沙雪さんの方を見ると……"
"彼女は優菜さまと七海さまと、３人で話をしていた。"
"でもやっぱり、寂しそうなのは変わらなかった。"
voice "Rikka_0583"
rk "「沙雪さん……一日も早く、元気になって欲しいな……」"


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
with dis



#mes on
#system on


"約１時間続いた、バーベキューの後。"
"麗奈先生がみんなに話があるという事で、全員を砂浜に呼び集めた。"


show char trn01m
with dis



voice "Rena_0077"
ren "「みんな、揃っているわね……最後の夜だし、今日はロマンチックな話、してあげるわね」"


show char trn01m at left
show char tsa01m at right as r
with dis



voice "Sara_0144"
sr "「どんな話なの、麗奈センセイ？」"


show char trn02m at left
with dis



voice "Rena_0078"
ren "「それはね……この島に伝わる、恋人同士の伝説よ♪」"


#allClear:
hide char trn02m at left
hide char tsa01m at right as r
#lastBG:
#scene bg bg39c
show char trk01m
with dis



voice "Rikka_0584"
rk "「恋人の……伝説……」"
"今まで先生がこんな風に話をしたことはなかったので、何だか唐突な感じがしたけれど。"
"みんな黙って聞いているので、ワタシもそのまま聞き入った。"


show char trn01m
with dis



voice "Rena_0079"
ren "「満月の夜、この砂浜で本当の気持ちを、本当の愛を伝え合って……口づけを交したカップルは、永遠に幸せになれるのよ」"


show char trk03m
with dis



voice "Rikka_0585"
rk "「……はぁ？」"
"何だか、どこかで聞いたことがあるような話だな。"
"よくあるというか、ありきたりというか……"


show char trn02m
with dis



voice "Rena_0080"
ren "「さあ、じゃあみんな、早速やってみましょ～{image=image/exch001.png}」"


show char trk04m
with dis



voice "Rikka_0586"
rk "「えぇっ！？」"


#allClear:
hide char trk04m
#lastBG:
#scene bg bg39c
with dis


"や、やるって？　何をするの？？"
"まわりを見ると、みんな……ううん、約半数の先輩たちがたじろいでいた。"
"当然だよね……こんな大勢の前で、そんな恥ずかしいこと、やるわけないよね。"
"いくらベストカップルに選ばれているとはいえ、ありえないって。"

# 此处已去除游戏强制二周目解锁其他角色路线的设定。
# Removed the limit of force goto Rika&Sayuki route at the first play.
#★★★選択肢関係の加筆　ここから
#//（１周目は、こっちのシナリオです）
#if s1==1 sentaku
menu:
 "璃紗と美夜の様子を見る":
  $ risa_route = True
  jump select06_1
 "七海と優菜の様子を見る":
  $ nanami_route = True
  jump select06_2
 "紗良と楓の様子を見る":
  $ sara_route = True
  jump select06_3
 "玲緒と麻衣の様子を見る":
  $ reo_route = True
  jump select06_4
 "ドキドキして、それどころではない":
  $ rikka_route = True
  jump select06_5


# 因为已经去去除强制一周目限制，以下直至label select06_1的台词均作废。
# Because I've removed the limit, all dialogues from now until "label select06_1" are useless.
"リサ姉だって、あんなに顔を赤くしているし……んっ？"


show char tri03m
with dis



voice "Risa_0786"
r "「み、美夜……行くわよ」"


show char tmi02m at left
show char tri03m at right as r
with dis



voice "Miya_0395"
m "「ええ{image=image/exch001.png}」"
"リサ姉が美夜さまの手を引いて、みんなの前に出た。"


#allClear:
hide char tmi02m at left
hide char tri03m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0587"
rk "「まっ、まさか、リサ姉……」"


#allClear:
hide char trk04m
#lastBG:
#scene bg bg39c
with dis


"ワタシとリサ姉の目が合う。"
"『六夏……よーく見ててね』"
"何故か、そう言われているように感じてしまった。"
"リサ姉は、美夜さまと向き合うと……いきなり、告白を始めた。"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0787"
r "「み、美夜……私は美夜が好きよ。すぐサボるところも、変態なところも、大食いなところも……全部、好き」"


show char tmi03m at left
with dis



voice "Miya_0396"
m "「ちょっと璃紗、それは褒めていないわよ」"


show char tri05m at right as r
with dis



voice "Risa_0788"
r "「うううっ……しょうがないでしょう、全部本当で、その通りなんだから」"
voice "Risa_0789"
r "「それとね、私にだけ見せてくれる、優しいところとか……そういうところが、好きよ……全部、好きだからね」"


show char tmi01m at left
with dis



voice "Miya_0397"
m "「……ありがとう、璃紗。今度はわたくしの番かしら」"
"美夜さまは真剣そのものの表情で、リサ姉を見つめながら言った。"


show char tmi08m at left
with dis



voice "Miya_0398"
m "「……わたくしも、璃紗が好きよ。他人にお節介なところも、まじめすぎるところや、変な趣味のところも……」"


show char tri04m at right as r
with dis



voice "Risa_0790"
r "「な、なななによ、変な趣味って！！」"
voice "Miya_0399"
m "「大丈夫、それはみんなには言わないわ。わたくしだけが知っている、璃紗の秘密も含めて、全部好き……わたくしはこの世で、璃紗しかいらないわ」"
"その告白に、見ていた周りのみんなから、邪魔にならない程度の小さな歓声がわいた。"
"お互いどれだけ、相手が好きか……しっかり言い合った２人はそのまま、なんと……"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0400"
m "「好きよ、璃紗……ちゅっ」"
voice "Risa_0791"
r "「んんっ、美夜……ちゅ{image=image/exch001.png}」"
"みんなの、そしてワタシの眼前で、濃厚なキスを始めてしまった。"
"再び、控えめな歓声が上がる。"


#allClear:
hide char tmi11m at left
hide char tri11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0588"
rk "「り、リサ姉が、みんなの前でこんな大胆なこと、するなんて……」"
"唖然としていると、麗奈先生がみんなに呼びかけた。"


show char trn02m
with dis



voice "Rena_0081"
ren "「さあ、みんなも２人に続いて、思いきって愛を告白しちゃいましょう{image=image/exch001.png}」"


show char trk04m
with dis



voice "Rikka_0589"
rk "「ええええっ！」"
"まだやるの、これ……"


#allClear:
hide char trk04m
#lastBG:
#scene bg bg39c
with dis


"リサ姉たちに触発されたのか、次々と他のカップル達も前に出てきた。"


show char tyu01m at left
show char tna01m at right as r
with dis



voice "Yuuna_0141"
y "「七海……好きよ。何があっても、ずっと一緒にいるわ」"
voice "Nanami0252"
n "「優菜お姉さま……わたしも大好きなお姉さまに置いていかれないよう、ずっと傍にいて追いかけます。だから一緒にいさせてください」"


show char tyu02m at left
with dis



voice "Yuuna_0142"
y "「ふふふっ、可愛いわ……ちゅっ{image=image/exch001.png}」"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Nanami0253"
n "「んんっ{image=image/exch001.png}　ちゅっ……くぅん{image=image/exch001.png}」"


show char tka01m at left
show char tsa01m at right as r
with dis



voice "Kaede_0116"
k "「紗良……私も、す、好きよ。あなたの事、これからもずっと守ってゆくわ。どんな時も離れないからね」"


show char tsa02m at right as r
with dis



voice "Sara_0145"
sr "「あぁ、楓ちゃん、かっこ良すぎ{image=image/exch001.png}　紗良も楓ちゃんを守るよ。そしてずっとずっと、楓ちゃんと一緒だよ……大好き、楓ちゃん{image=image/exch001.png}」"


show char tka04m at left
with dis



voice "Kaede_0117"
k "「ちょ、ちょっと、飛びついて来たら、危ないわ……んっ{image=image/exch001.png}」"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Sara_0146"
sr "「楓ちゃ～ん、ちゅっ、ちゅっ{image=image/exch001.png}」"


show char tma02m at left
show char tre05m at right as r
with dis



voice "Mai_0225"
ma "「みんな、本当にすごいわね。どれどれ、わたしたちも……玲緒、大好き{image=image/exch001.png}」"
voice "Reo_0173"
re "「………………」"


show char tma03m at left
with dis



voice "Mai_0226"
ma "「玲緒？　返事は？？」"
voice "Reo_0174"
re "「ワ、ワタシも……麻衣のこと、好きだもん……もう、これでいいでしょう」"


show char tma02m at left
with dis



voice "Mai_0227"
ma "「この期に及んでも、ツンデレを崩さないのは流石だわ。そういうところも可愛い～、大好き{image=image/exch001.png}」"


show char tre09m at right as r
with dis



voice "Reo_0175"
re "「うきゃあああ……強く抱きしめ過ぎ、麻衣～」"


show char tma11m at left
with dis



voice "Mai_0228"
ma "「んふふふっ……ちゅっ{image=image/exch001.png}」"


show char tre11m at right as r
with dis



voice "Reo_0176"
re "「あっ……ふぅ……ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tma11m at left
hide char tre11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0590"
rk "「み……皆さん、こんな……凄すぎだよ……」"


show char tsy05m
with dis



voice "Sayuki0249"
s "「………………」"
"３カップル連続の告白にワタシは驚き、沙雪さんは真っ赤になっていた。"


#allClear:
hide char tsy05m
#lastBG:
#scene bg bg39c
with dis

#//（ルート合流）へジャンプ
#set f2 0
#jump select06_end


#（２周目以降は、こっちのシナリオになります）
#label sentaku:


#++特別選択肢（２週目以降／ルート決定）
#１．『璃紗と美夜の様子を見る』
#２．『七海と優菜の様子を見る』
#３．『紗良と楓の様子を見る』
#４．『玲緒と麻衣の様子を見る』
#５．『ドキドキして、それどころではない』



#１．『璃紗と美夜の様子を見る』
label select06_1:
"リサ姉だって、あんなに顔を赤くしているし……んっ？"


show char tri03m
with dis



voice "Risa_0792"
r "「み、美夜……行くわよ」"


show char tmi02m at left
show char tri03m at right as r
with dis



voice "Miya_0401"
m "「ええ{image=image/exch001.png}」"
"リサ姉が美夜さまの手を引いて、みんなの前に出た。"


#allClear:
hide char tmi02m at left
hide char tri03m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0591"
rk "「まっ、まさか、リサ姉……」"


#allClear:
hide char trk04m
#lastBG:
#scene bg bg39c
with dis


"ワタシとリサ姉の目が合う。"
"『六夏……よーく見ててね』"
"何故か、そう言われているように感じてしまった。"
"リサ姉は、美夜さまと向き合うと……いきなり、告白を始めた。"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0793"
r "「み、美夜……私は美夜が好きよ。すぐサボるところも、変態なところも、大食いなところも……全部、好き」"


show char tmi03m at left
with dis



voice "Miya_0402"
m "「ちょっと璃紗、それは褒めていないわよ」"


show char tri05m at right as r
with dis



voice "Risa_0794"
r "「うううっ……しょうがないでしょう、全部本当で、その通りなんだから」"
voice "Risa_0795"
r "「それとね、私にだけ見せてくれる、優しいところとか……そういうところが、好きよ……全部、好きだからね」"


show char tmi01m at left
with dis



voice "Miya_0403"
m "「……ありがとう、璃紗。今度はわたくしの番かしら」"
"美夜さまは真剣そのものの表情で、リサ姉を見つめながら言った。"


show char tmi08m at left
with dis



voice "Miya_0404"
m "「……わたくしも、璃紗が好きよ。他人にお節介なところも、まじめすぎるところや、変な趣味のところも……」"


show char tri04m at right as r
with dis



voice "Risa_0796"
r "「な、なななによ、変な趣味って！！」"
voice "Miya_0405"
m "「大丈夫、それはみんなには言わないわ。わたくしだけが知っている、璃紗の秘密も含めて、全部好き……わたくしはこの世で、璃紗しかいらないわ」"
"その告白に、見ていた周りのみんなから、邪魔にならない程度の小さな歓声がわいた。"
"お互いどれだけ、相手が好きか……しっかり言い合った２人はそのまま、なんと……"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0406"
m "「好きよ、璃紗……ちゅっ」"
voice "Risa_0797"
r "「んんっ、美夜……ちゅ{image=image/exch001.png}」"
"みんなの、そしてワタシの眼前で、濃厚なキスを始めてしまった。"
"再び、控えめな歓声が上がる。"


#allClear:
hide char tmi11m at left
hide char tri11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0592"
rk "「り、リサ姉が、みんなの前でこんな大胆なこと、するなんて……」"
"唖然としていると、麗奈先生がみんなに呼びかけた。"


show char trn02m
with dis



voice "Rena_0082"
ren "「さあ、みんなも２人に続いて、思いきって愛を告白しちゃいましょう{image=image/exch001.png}」"


show char trk04m
with dis



voice "Rikka_0593"
rk "「ええええっ！」"
"まだやるの、これ……"


#allClear:
hide char trk04m
#lastBG:
#scene bg bg39c
with dis


"リサ姉たちに触発されたのか、次々と他のカップル達も前に出てきた。"
"七海さまと、優菜さまが……"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Yuuna_0143"
y "「七海……ずっと、ずっと、好きよ……これからも、ね。ちゅっ{image=image/exch001.png}」"
voice "Nanami0254"
n "「ちゅっ{image=image/exch001.png}　優菜お姉さま、わたしもずっと、お姉さまを愛します{image=image/exch001.png}」"


#allClear:
hide char tyu11m at left
hide char tna11m at right as r
#lastBG:
#scene bg bg39c
with dis


"紗良さまと、楓さまが……"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Sara_0147"
sr "「楓ちゃん、好き、好きすきっ{image=image/exch001.png}　ちゅっ{image=image/exch001.png}」"
voice "Kaede_0118"
k "「ちゅっ……もう、紗良ったら……でも、好きよ……ちゅっ」"


#allClear:
hide char tka11m at left
hide char tsa11m at right as r
#lastBG:
#scene bg bg39c
with dis


"玲緒さまと、麻衣さまが……"


show char tma01m at left
show char tre05m at right as r
with dis



voice "Mai_0229"
ma "「玲緒、ほら、わたしにキスして。わたしがいなくなったら玲緒、困るでしょう？」"


show char tma11m at left
show char tre11m at right as r
with dis



voice "Reo_0177"
re "「もぉ……でも、本当に困るわ……わかったわよ、ん……ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tma11m at left
hide char tre11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0594"
rk "「み……皆さん、こんな……凄すぎだよ……」"


show char trk04m at left
show char tsy05m at right as r
with dis


voice "Sayuki0250"
s "「………………」"
"４カップルの愛の告白とキスに、ワタシは驚き。"
"沙雪さんは、真っ赤になっていた。"


#allClear:
hide char trk04m at left
hide char tsy05m at right as r
#lastBG:
#scene bg bg39c
with dis


#//『璃紗＆美夜ルート』のフラグをＯＮにする
#set f2 1
jump select06_end


#２．『七海と優菜の様子を見る』
label select06_2:

"さすがに恥ずかしいのか、誰も前に出ない……すると麗奈先生が、みんなに呼びかけた。"


show char trn02m
with dis



voice "Rena_0083"
ren "「さあ、思いきって愛を告白しちゃいましょう{image=image/exch001.png}　最初にやったカップルが、一番幸せになれるかも？　んふふっ{image=image/exch001.png}」"


#allClear:
hide char trn02m
#lastBG:
#scene bg bg39c
with dis


"するとなんと、前に歩み出たのは……七海さまと、優菜さまだった。"
"ワタシは思わず、お二人に見入ってしまう。"


show char tyu01m at left
show char tna01m at right as r
with dis



voice "Yuuna_0144"
y "「七海……好きよ。何があっても、ずっと一緒にいるわ」"
voice "Nanami0255"
n "「優菜お姉さま……わたしも大好きなお姉さまに置いていかれないよう、ずっと傍にいて追いかけます。だから一緒にいさせてください」"


show char tyu02m at left
with dis



voice "Yuuna_0145"
y "「ふふふっ、可愛いわ……ちゅっ{image=image/exch001.png}」"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Nanami0256"
n "「んんっ{image=image/exch001.png}　ちゅっ……くぅん{image=image/exch001.png}」"


#allClear:
hide char tyu11m at left
hide char tna11m at right as r
#lastBG:
#scene bg bg39c
show char trk05m
with dis



voice "Rikka_0595"
rk "「あ、ああ……本当に、キス……している……はぁ、はぁ」"
"すると続いて、紗良さまと楓さま、玲緒さまと麻衣さま、リサ姉と美夜さまも、前に出てきた。"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Sara_0148"
sr "「楓ちゃん、好き、好きすきっ{image=image/exch001.png}　ちゅっ{image=image/exch001.png}」"
voice "Kaede_0119"
k "「ちゅっ……もう、紗良ったら……でも、好きよ……ちゅっ{image=image/exch001.png}」"


show char tma01m at left
show char tre05m at right as r
with dis



voice "Mai_0230"
ma "「玲緒、ほら、わたしにキスして。わたしがいなくなったら玲緒、困るでしょう？」"


show char tma11m at left
show char tre11m at right as r
with dis



voice "Reo_0178"
re "「もぉ……でも、本当に困るわ……わかったわよ、ん……ちゅっ{image=image/exch001.png}」"


show char tmi02m at left
show char tri02m at right as r
with dis



voice "Risa_0798"
r "「六夏、見ててね………………美夜、好きよ……キス、して{image=image/exch001.png}」"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0407"
m "「みんなの前で、告白してくれて……嬉しいわ、璃紗……ん、ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tmi11m at left
hide char tri11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0596"
rk "「み……皆さん、こんな……凄すぎだよ……」"


show char tsy05m
with dis



voice "Sayuki0251"
s "「………………」"
"４カップルの愛の告白とキスに、ワタシは驚き。"
"沙雪さんは、真っ赤になっていた。"


#allClear:
hide char tsy05m
#lastBG:
#scene bg bg39c
with dis


#//『七海＆優菜ルート』のフラグをＯＮにする
#set f2 2
jump select06_end


#３．『紗良と楓の様子を見る』
label select06_3:

"さすがに恥ずかしいのか、誰も前に出ない……すると麗奈先生が、みんなに呼びかけた。"


show char trn02m
with dis



voice "Rena_0084"
ren "「さあ、思いきって愛を告白しちゃいましょう{image=image/exch001.png}　最初にやったカップルが、一番幸せになれるかも？　んふふっ{image=image/exch001.png}」"
"するとなんと、前に歩み出たのは……紗良さまと、楓さまだった。"


show char tka01m at left
show char tsa01m at right as r
with dis



voice "Kaede_0120"
k "「紗良……私も、す、好きよ。あなたの事、これからもずっと守ってゆくわ。どんな時も離れないからね」"


show char tsa02m at right as r
with dis



voice "Sara_0149"
sr "「あぁ、楓ちゃん、かっこ良すぎ{image=image/exch001.png}　紗良も楓ちゃんを守るよ。そしてずっとずっと、楓ちゃんと一緒だよ……大好き、楓ちゃん{image=image/exch001.png}」"


show char tka04m at left
with dis



voice "Kaede_0121"
k "「ちょ、ちょっと、飛びついて来たら、危ないわ……んっ、ちゅっ」"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Sara_0150"
sr "「楓ちゃ～ん、ちゅっ、ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tka11m at left
hide char tsa11m at right as r
#lastBG:
#scene bg bg39c
show char trk05m
with dis



voice "Rikka_0597"
rk "「あ、ああ……本当に、キス……している……はぁ、はぁ」"
"すると続いて、七海さまと優菜さま、玲緒さまと麻衣さま、リサ姉と美夜さまも、前に出てきた。"


show char tyu02m at left
show char tna02m at right as r
with dis



voice "Yuuna_0146"
y "「七海……ずっと、ずっと、好きよ……これからも、ね。ちゅっ{image=image/exch001.png}」"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Nanami0257"
n "「ちゅっ{image=image/exch001.png}　優菜お姉さま、わたしもずっと、お姉さまを愛します{image=image/exch001.png}」"


show char tma01m at left
show char tre05m at right as r
with dis



voice "Mai_0231"
ma "「玲緒、ほら、わたしにキスして。わたしがいなくなったら玲緒、困るでしょう？」"


show char tma11m at left
show char tre11m at right as r
with dis



voice "Reo_0179"
re "「もぉ……でも、本当に困るわ……わかったわよ、ん……ちゅっ{image=image/exch001.png}」"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0799"
r "「六夏、見ててね………………美夜、好きよ……キス、して{image=image/exch001.png}」"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0408"
m "「みんなの前で、告白してくれて……嬉しいわ、璃紗……ん、ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tmi11m at left
hide char tri11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0598"
rk "「み……皆さん、こんな……凄すぎだよ……」"


show char tsy05m
with dis



voice "Sayuki0252"
s "「………………」"
"４カップルの愛の告白とキスに、ワタシは驚き。"
"沙雪さんは、真っ赤になっていた。"


#allClear:
hide char tsy05m
#lastBG:
#scene bg bg39c
with dis


#//『紗良＆楓ルート』のフラグをＯＮにする
#set f2 3
jump select06_end


#４．『玲緒と麻衣の様子を見る』
label select06_4:

"さすがに恥ずかしいのか、誰も前に出ない……すると麗奈先生が、みんなに呼びかけた。"


show char trn02m
with dis



voice "Rena_0085a"
ren "「さあ、思いきって愛を告白しちゃいましょう{image=image/exch001.png}　最初にやったカップルが、一番幸せになれるかも？　んふふっ{image=image/exch001.png}」"
"するとなんと、前に歩み出たのは……玲緒さまと、麻衣さまだった。"


show char tma02m at left
show char tre05m at right as r
with dis



voice "Mai_0232"
ma "「じゃあ一番は、わたしたちね……玲緒、大好き{image=image/exch001.png}」"
voice "Reo_0180"
re "「………………」"


show char tma03m at left
with dis



voice "Mai_0233"
ma "「玲緒？　返事は？？」"
voice "Reo_0181"
re "「ワ、ワタシも……麻衣のこと、好きだもん……もう、これでいいでしょう」"


show char tma02m at left
with dis



voice "Mai_0234"
ma "「この期に及んでも、ツンデレを崩さないのは流石だわ。そういうところも可愛い～、大好き{image=image/exch001.png}」"


show char tre09m at right as r
with dis



voice "Reo_0182"
re "「うきゃあああ……強く抱きしめ過ぎ、麻衣～」"


show char tma11m at left
with dis



voice "Mai_0235"
ma "「んふふふっ……ちゅっ{image=image/exch001.png}」"


show char tre11m at right as r
with dis



voice "Reo_0183"
re "「あっ……ふぅ……ちゅっ{image=image/exch001.png}」"
"すると続いて、七海さまと優菜さま、紗良さまと楓さま、リサ姉と美夜さまも、前に出てきた。"


show char tyu02m at left
show char tna02m at right as r
with dis



voice "Yuuna_0147"
y "「七海……ずっと、ずっと、好きよ……これからも、ね。ちゅっ{image=image/exch001.png}」"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Nanami0258"
n "「ちゅっ{image=image/exch001.png}　優菜お姉さま、わたしもずっと、お姉さまを愛します{image=image/exch001.png}」"


show char tka02m at left
show char tsa02m at right as r
with dis



voice "Sara_0151"
sr "「楓ちゃん、好き、好きすきっ{image=image/exch001.png}　ちゅっ{image=image/exch001.png}」"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Kaede_0122"
k "「ちゅっ……もう、紗良ったら……でも、好きよ……ちゅっ{image=image/exch001.png}」"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0800"
r "「六夏、見ててね………………美夜、好きよ……キス、して{image=image/exch001.png}」"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0409"
m "「みんなの前で、告白してくれて……嬉しいわ、璃紗……ん、ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tmi11m at left
hide char tri11m at right as r
#lastBG:
#scene bg bg39c
show char trk04m
with dis



voice "Rikka_0599"
rk "「み……皆さん、こんな……凄すぎだよ……」"


show char tsy05m
with dis



voice "Sayuki0253"
s "「………………」"
"４カップルの愛の告白とキスに、ワタシは驚き。"
"沙雪さんは、真っ赤になっていた。"


#allClear:
hide char tsy05m
#lastBG:
#scene bg bg39c
with dis


#//『玲緒＆麻衣ルート』のフラグをＯＮにする
#set f2 4
jump select06_end


#５．『ドキドキして、それどころではない』
label select06_5:

"ありえない……人前でキスなんて、ありえない！！"
"そう思っていたのに、なんと……"


show char tri01m
with dis



voice "Risa_0801"
r "「………………行きましょう、美夜」"


show char tmi02m at left
show char tri01m at right as r
with dis



voice "Miya_0410"
m "「ええ{image=image/exch001.png}」"
"ワタシをじっと見つめながら、リサ姉と美夜さまが前に出る。"
"それだけじゃない、七海さまと優菜さま、紗良さまと楓さま、玲緒さまと麻衣さままで……"
voice "Risa_0802"
r "「六夏、見ててね………………美夜、好きよ……キス、して{image=image/exch001.png}」"


show char tmi11m at left
show char tri11m at right as r
with dis



voice "Miya_0411"
m "「みんなの前で、告白してくれて……嬉しいわ、璃紗……ん、ちゅっ{image=image/exch001.png}」"


show char tyu02m at left
show char tna02m at right as r
with dis



voice "Yuuna_0148"
y "「七海……ずっと、ずっと、好きよ……これからも、ね。ちゅっ{image=image/exch001.png}」"


show char tyu11m at left
show char tna11m at right as r
with dis



voice "Nanami0259"
n "「ちゅっ{image=image/exch001.png}　優菜お姉さま、わたしもずっと、お姉さまを愛します{image=image/exch001.png}」"


show char tka02m at left
show char tsa02m at right as r
with dis



voice "Sara_0152"
sr "「楓ちゃん、好き、好きすきっ{image=image/exch001.png}　ちゅっ{image=image/exch001.png}」"


show char tka11m at left
show char tsa11m at right as r
with dis



voice "Kaede_0123"
k "「ちゅっ……もう、紗良ったら……でも、好きよ……ちゅっ{image=image/exch001.png}」"


show char tma01m at left
show char tre05m at right as r
with dis



voice "Mai_0236"
ma "「玲緒、ほら、わたしにキスして。わたしがいなくなったら玲緒、困るでしょう？」"


show char tma11m at left
show char tre11m at right as r
with dis



voice "Reo_0184"
re "「もぉ……でも、本当に困るわ……わかったわよ、ん……ちゅっ{image=image/exch001.png}」"


#allClear:
hide char tma11m at left
hide char tre11m at right as r
#lastBG:
#scene bg bg39c
show char tsy05m
with dis



voice "Sayuki0254"
s "「……み……皆さん……すごいです」"
"４カップルの愛の告白とキスを、沙雪さんは真っ赤になりながら見つめていた。"
"でもワタシは、ドキドキしすぎて、まともに見られなかった。"


show char trk05m
with dis



voice "Rikka_0600"
rk "（こんな、すごい……すごすぎて、ああ……）"
"ワタシと沙雪さんじゃ、こんなの……できないかも……"

#allClear:
hide char trk05m
#lastBG:
#scene bg bg39c
jump select06_end


#//フラグはそのまま（他ルートのフラグが立っていなければ、自動的に『六夏＆沙雪ルート』を判定します）
#set f2 0


#（ルート合流）１周目も、２周目も、ここからは共通
#★★★選択肢関係の加筆　ここまで
label select06_end:


"でもまだまだ、夜の大告白大会は終わらない。"


show char ter01m at left
show char tsi01m at right as r
with dis



voice "Erisu_0098"
e "「シズク、大好きだよ……シズクは？」"
voice "Sizuku0089"
sk "「もちろん……好きです」"
voice "Erisu_0099"
e "「生涯、好き……愛してるよ、シズク」"


show char tsi05m at right as r
with dis



voice "Sizuku0090"
sk "「わ、わたくしも……」"


show char ter02m at left
with dis



voice "Erisu_0100"
e "「本当に？　本当だね！　それじゃあここに、ワタシたちの婚約を発表しまーす{image=image/exch001.png}」"


show char tsi04m at right as r
with dis



voice "Sizuku0091"
sk "「えぇっ、エリスっ！！」"
voice "Erisu_0101"
e "「そして近い将来、結婚することを宣言します。式にはここにいるみんなを招待するよー」"


show char tsi03m at right as r
with dis



voice "Sizuku0092"
sk "「こ、困りますぅ……ぅぅっ」"


show char ter11m at left
with dis



voice "Erisu_0102"
e "「じゃあ、誓いのキスするね……ちゅっ」"


show char tsi11m at right as r
with dis



voice "Sizuku0093"
sk "「んんっ……ちゅっ……エリスったら……」"


#allClear:
hide char ter11m at left
hide char tsi11m at right as r
#lastBG:
#scene bg bg39c
show char tru01m
with dis



voice "Runa_0065"
rn "「……じゃあ、わたしたちもしようか、せんせい」"


show char tru01m at left
show char tta03m at right as r
with dis



voice "Takako0073"
t "「えっ、でも……」"


show char tru03m at left
with dis



voice "Runa_0066"
rn "「せんせいはわたしと、永遠の愛を誓わないの？」"
voice "Takako0074"
t "「それは……もう、わかったわ」"


show char tru01m at left
with dis



voice "Runa_0067"
rn "「せんせい、大好き。なにがあろうと、せんせいはわたしのものだからね」"


show char tta01m at right as r
with dis



voice "Takako0075"
t "「わかってるわ、瑠奈……可愛い瑠奈は、私にとって一番大事な人よ」"


show char tru11m at left
show char tta11m at right as r
with dis



voice "Runa_0068"
rn "「せんせい～、ちゅっ{image=image/exch001.png}」"


show char tta09m at right as r
with dis



voice "Takako0076"
t "「ちゅっ………………んんっ、長すぎよ、もう終わり、瑠奈離しなさいっ」"


show char tta09m at right as r
with dis



voice "Runa_0069"
rn "「だ・め・よ、もっとするのよ。ちゅうううっ{image=image/exch001.png}」"


#allClear:
hide char tru11m at left
hide char tta09m at right as r
#lastBG:
#scene bg bg39c
show char trk05m
with dis



voice "Rikka_0601"
rk "「あぁ……みんな、本当にすごい……」"
"こんなにたくさんの愛の告白とキスを見たのは、もちろん初めてだった。"
"エリスさまと雫さまなんて、婚約発表と結婚宣言までしてしまったし。"
"最初はビックリしたけれど。"
"みんなそれぞれ、相手のことを強く想っている気持ちが、こっちにも伝わって来て。"
"少し、羨ましく感じてしまった。"


show char trk03m
with dis



voice "Rikka_0602"
rk "（ああ……ワタシもあんな風に、沙雪さんに想いを伝えられたら……）"
"視線の先には……沙雪さんがいる。"
"ワタシたち２人だけが、この告白大会の中で取り残されていた。"


show char tri01m at left
show char trk03m at right as r
with dis



voice "Risa_0803"
r "「……六夏」"
"リサ姉が、ワタシの背中をそっと押していた。"
voice "Risa_0804"
r "「六夏、言いたい事を全部言わないまま、諦めたら……一生、後悔するわよ」"
voice "Rikka_0603"
rk "「リサ……姉……」"


#allClear:
hide char tri01m at left
hide char trk03m at right as r
#lastBG:
#scene bg bg39c
with dis


"ワタシはもう一度、沙雪さんを見つめる。"
"ああ……ダメ、やっぱり好き。"
"好きで好きでたまらない、絶対にこのまま、諦めたくなんてない！！"
"みんなの愛の告白を聞いて、胸も激しく高鳴っていた。"


show char trk08m
with dis



voice "Rikka_0604"
rk "「………………沙雪さんっ！！」"


show char trk08m at left
show char tsy03m at right as r
with dis



voice "Sayuki0255"
s "「えっ？　えぇぇっ！？」"


stop music fadeout 1


#※EV012
#allClear:
hide char trk08m at left
hide char tsy03m at right as r
#lastBG:
#scene bg bg39c
scene bg EV12
with Dis


play music "sound/BGM14.ogg"


"気がつくと、ワタシは沙雪さんの手を握って、そのままみんなの前に出ていった。"
"そして……もう一度、想いを告白する。"
"もう一度、自分の気持ちを思いっきり、残らず全部ぶつける。"
voice "Rikka_0605"
rk "「沙雪さん……ワタシ、沙雪さんが好き、大好きなの。どうしても諦め切れないよ」"
voice "Sayuki0256"
s "「り、りっ、六夏さん……ぅぅ……」"
"真っ赤になって、驚いている沙雪さん。"
"こんな時でさえ、こんな彼女でさえ、最高に可愛いと思ってしまう。"
"ここにいるみんな、誰もが素敵だけど……ワタシにはやっぱり、沙雪さん以上に惹かれる人はいなかった。"
voice "Rikka_0606"
rk "「沙雪さん、ワタシは……どうしても、このまま諦めたくないよ」"
voice "Sayuki0257"
s "「で、ですから……この前お話したように、私は祖母が決めて下さった方と、結婚を……」"
voice "Rikka_0607"
rk "「それは知っています、分かっています。でもワタシが今聞きたいのは、そういう事じゃないんです」"
voice "Rikka_0608"
rk "「ワタシは……沙雪さんの本当の気持ちが聞きたい、ワタシをどう思っているのか、ハッキリ聞かせて欲しいんです」"
voice "Sayuki0258"
s "「り……六夏……さん……」"


#※EV012P1
scene bg EV12p1
with Dis



"ワタシの告白を聞いていた沙雪さんの頬には、いつしか涙が伝っていた。"
"その涙の意味を、彼女は言葉にしてくれた。"
voice "Sayuki0259"
s "「うっ……六夏さん、私……本当は………………好き、です」"
voice "Rikka_0609"
rk "「……えっ……？」"
voice "Sayuki0260"
s "「本当は、私……貴女が好きなんです。ずっと惹かれておりました、六夏さん」"
voice "Rikka_0610"
rk "「う、ウソ……でしょう？」"
"ワタシが、好き？"
"沙雪さんが本当に、そう言ったの？？"
"ワタシと沙雪さんの周りでは、みんなニッコリ微笑みながら、うなづいていた。"
"沙雪さんの、この気持ち……気づいていたの？"
"ワタシは全然、気づかなかったのに。"
"未だに信じられないワタシに、沙雪さんは再び、真剣に言ってくれた。"
voice "Sayuki0261"
s "「六夏さん、ずっと一緒にいたい……私も六夏さんと、ずっと一緒にいたいです……」"
voice "Rikka_0611"
rk "「ほほほ、本当……に？　沙雪さん、本当にワタシを……」"
voice "Sayuki0262"
s "「はい、本当です……ちゅっ」"


#※EV012P1
scene bg EV12p2
with Dis



voice "Rikka_0612"
rk "「んんっ！？　んちゅ……んん……」"
"ワタシの唇に、沙雪さんの唇が……重なっていた。"
"なんと沙雪さんは感極まって、ワタシにキスしてきた。"
"ワタシは完全に固まってしまい、ピクリとも動けない。"
"でも……唇に感じる、この甘く柔らかい感触は、間違いなく本物で。"
"繋がれたそこから、あったかい幸せが溢れてくるのを、ハッキリ感じた。"

#//SE：拍手音×いっぱい
#♀SE017
play sound "sound/SE017.ogg"


voice "Risa_0805"
r "「おめでとう、六夏……本当に、良かったね」"
"ワタシと沙雪さんに向けられた、みんなの暖かい拍手。"
"リサ姉も涙を浮かべながら、めいっぱいの拍手を送ってくれていた。"
voice "Rena_0086"
ren "「うんうん、良かったわね……じゃあこれは、愛を誓い合ったみんなへ、私からのプレゼントよ{image=image/exch001.png}」"

#//SE：花火打ち上げ音
#♀SE018
play sound "sound/SE018.ogg"


voice "Risa_0806"
r "「こ、この音……また花火っ！？」"
voice "Miya_0412"
m "「去年のクリスマスの時みたいね……本当に派手な演出が好きよね、麗奈先生って」"
"花火のまぶしい光の下で、ワタシと沙雪さんはいつまでも、唇を重ねていた。"
"ああ……幸せ、もう死んでもいい……ううん、絶対死にたくない。"
"だって今、この瞬間から、やっと始まるんだから。"
"大好きな沙雪さんと、ワタシの……本当の、恋物語が。"
"熱い、本当に熱い夏が、こうして終わっていった……決して忘れられない想い出を、ワタシと沙雪さんの胸に残して。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



stop music fadeout 1

$ _skipping = False
$ _dismiss_pause = False

if risa_route:
     scene image "image/eyecatch02.png"
     with vs

     pause 3

     scene black
     with Dis
     $ _skipping = True
     $ _dismiss_pause = True
     jump S053

if nanami_route:
     scene image "image/eyecatch02.png"
     with vs

     pause 3

     scene black
     with Dis
     $ _skipping = True
     $ _dismiss_pause = True
     jump S070

if sara_route:
     scene image "image/eyecatch04.png"
     with vs

     pause 3

     scene black
     with Dis
     $ _skipping = True
     $ _dismiss_pause = True
     jump S087

if reo_route:
     scene image "image/eyecatch05.png"
     with vs

     pause 3

     scene black
     with Dis
     $ _skipping = True
     $ _dismiss_pause = True
     jump S104

if rikka_route:
     scene image "image/eyecatch01.png"
     with vs

     pause 3

     scene black
     with Dis
     $ _skipping = True
     $ _dismiss_pause = True
     jump S031
