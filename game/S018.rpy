#「水着だよ全員集合！！」

label S018:
$ save_name = "◇水着だよ全員集合！！"


#**海岸通り・昼
scene bg bg38a
with Dis


#mes on
#system on


#♂MP08
play music "sound/BGM08.ogg"


show char tri02f2
with dis



voice "Risa_0552"
r "「うわぁー、綺麗な海ね、美夜」"


show char tmi01f2 at left
show char tri02f2 at right as r
with dis



voice "Miya_0273"
m "「……そうね」"


show char tri01f2 at right as r
with dis



voice "Risa_0553"
r "「あれが私たちの泊まる、リゾートホテルね……どんな部屋なのかしら」"
voice "Miya_0274"
m "「……そうね」"
voice "Risa_0554"
r "「まだ私たちの他に、来ている人はいないのかしら」"
voice "Miya_0275"
m "「……そうね」"


show char tri03f2 at right as r
with dis



voice "Risa_0555"
r "「美夜……もしかして、寝ぼけている？」"
voice "Miya_0276"
m "「………………ええ」"
"麗奈先生からの迎えの車が来て、連れて行かれた先は、空港だった。"
"そこから飛行機に乗って、いきなりこの南の島まで来たけれど。"
"その間、美夜はずっと眠っていたから、まだ頭が覚醒していないみたいだった。"
voice "Risa_0556"
r "「美夜、先にホテルに行く？　多分、先生がいると思うし」"
voice "Miya_0277"
m "「ん……そうしようかしら……あれっ、ねぇ璃紗、あれ何かしら？」"
"美夜が目を細めて、海を見つめる。"
"その視線の先を追うと、何かがこっちに向かってくるのが見えた。"
voice "Risa_0557"
r "「あれ、船かしら……んっ、誰か手を振っているわ」"
voice "Miya_0278"
m "「多分、七海さんじゃないかしら」"


show char tri04f2 at right as r
with dis



voice "Risa_0558"
r "「えっ、七海さん？」"
"船はだんだんと近づいてきて、甲板に立つ七海さんの姿が確認出来た。"


#allClear:
hide char tmi01f2 at left
hide char tri04f2 at right as r
#lastBG:
#scene bg bg38a
show char tna02p
with dis



voice "Nanami0148"
n "「璃紗さーん、美夜さーん！」"


show char tmi01f2 at left
show char tri01f2 at right as r
with dis



voice "Risa_0559"
r "「やっぱり七海さんだわ、七海さぁーん！」"
"やがて船が到着して、そこから七海さんと優菜さまが降りてきた。"

hide char tmi01f2 at left
hide char tri01f2 at right as r
show char tna01f2 at sleft as l
show char tmi01f2
show char tri01f2 at sright as sr
with dis



voice "Nanami0149"
n "「ごきげんよう」"
voice "Risa_0560"
r "「ごきげんよう。でもびっくりしたわ、まさか船で来るなんて」"


show char tna02f2 at sleft as l
with dis



voice "Nanami0150"
n "「ふふっ、これ、優菜さまの家の船なんです」"


show char tri04f2 at sright as sr
with dis



voice "Risa_0561"
r "「えぇっ？　優菜さまの家の所有物なの！？」"
"まったく、これだからブルジョアは……あぁ、やっぱり庶民連合に入りたいわ、私も。"


#allClear:
hide char tna02f2 at sleft as l
hide char tmi01f2
hide char tri04f2 at sright as sr
#lastBG:
#scene bg bg38a
show char tyu02f2
with dis



voice "Yuuna_0051"
y "「ごきげんよう、璃紗ちゃん、美夜ちゃん」"


show char tyu02f2 at sleft as l
show char tmi01f2
show char tri01f2 at sright as sr
with dis



voice "Miya_0279"
m "「……ごきげんよう」"
voice "Yuuna_0052"
y "「突然、麗奈先生に呼び出されたから、ウチの船で来ちゃった……ふふふ{image=image/exch001.png}」"


show char tri03f2 at sright as sr
with dis



voice "Risa_0562"
r "「ウチの、船……」"
"はぁ……なんていうか、もう次元が違うわね。"


#allClear:
hide char tyu02f2 at sleft as l
hide char tmi01f2
hide char tri03f2 at sright as sr
#lastBG:
#scene bg bg38a
show char tmi01f2 at left
show char tri03f2 at right as r
with dis



voice "Miya_0280"
m "「……ウチの会社にも、船はあるわ」"


show char tri04f2 at right as r
with dis



voice "Risa_0563"
r "「そうなの？　すごいのね」"
"別に優菜さまを羨んだわけじゃないのに……美夜はこういう時、すぐに対抗したがるんだから。"
voice "Miya_0281"
m "「なんだったらこの島に呼んで、帰りは船にする？」"
voice "Risa_0564"
r "「い、いいわよ……そんな贅沢しなくても」"
voice "Miya_0282"
m "「だったら、自家用飛行機の方が、いいかしら？」"
voice "Risa_0565"
r "「ひっ、飛行機もあるの！？」"
voice "Miya_0283"
m "「ほら、ちょうどあれみたいに……」"
voice "Risa_0566"
r "「っ！！」"


#//SE：飛行機着陸音
#♀SE008
play sound "sound/SE008.ogg"


"さっき私たちが降りてきた場所に、自家用と思われる飛行機が降り立った。"
"そして、そこから出てきたのは……"


#allClear:
hide char tmi01f2 at left
hide char tri04f2 at right as r
#lastBG:
#scene bg bg38a
show char tyu01f2
with dis



voice "Yuuna_0053"
y "「あら……エリスさまと雫さまだわ」"


show char tyu01f2 at left
show char tna01f2 at right as r
with dis



voice "Nanami0151"
n "「わっ、本当だ。なんだか二人とも、疲れているのかしら……ふらふらしているみたい」"
"足元がおぼついてないわ、本当に疲れているみたいね。。"


show char tmi01f2 at left
show char tri03f2 at right as r
with dis



voice "Miya_0284"
m "「璃紗、あれを見て」"
voice "Risa_0567"
r "「今度は……何？」"
"美夜が空を指さすと、ヘリがこちらに向かってきていた。"


#allClear:
hide char tmi01f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg38a
show char tna01f2
with dis



voice "Nanami0152"
n "「なんか中にいる人、こっちを見て手を振っているわ」"
"じゃああれも、もしかして……ベストカップルの誰かかしら？"
"そんな感じで、続々とリゾートビーチに、ベストカップルのメンバーが集まってきたのだった。"


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


show char tsa03f2
with dis



voice "Sara_0072"
sr "「今日はなんか、強制召喚されたって感じだよねー」"
"雑誌のグラビア撮影をしていた紗良さんと楓さまは、仕事が終わった途端、麗奈先生の迎えが来て。"
"そのままヘリに乗せられた、と。"


show char ter03f2
with dis



voice "Erisu_0043"
e "「ワタシたちもだよ。シズクがワタシの実家に、遊びに来ていたのに……」"


show char tka04f2 at left
show char ter03f2 at right as r
with dis



voice "Kaede_0047"
# "【　楓　】「えぇっ、エリスさまの実家って……じゃあ海外から、この島まで来たんですか？」"

hide char tka04f2 at left
hide char ter03f2 at right as r
show char tka04f2 at sleft as l
show char ter03f2
show char tsi03f2 at sright as sr
with dis



voice "Sizuku0038"
# "【　雫　】「ええ、最初は何が起きているのか、よくわかりませんでした」"
"それじゃあエリスさまたち、疲れていて当然だわ。"
"移動時間、どれくらいかかったのかしら……？"


#allClear:
hide char tka04f2 at sleft as l
hide char ter03f2
hide char tsi03f2 at sright as sr
#lastBG:
#scene bg bg39a
show char tre03f2
with dis



voice "Reo_0108"
re "「ワタシはもっと、クーラーの効いた部屋でごろごろしていたかったのに……」"


show char tma02f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0130"
ma "「玲緒は無理矢理でも、外に出た方がいいのよ。ちょうど良かったわね♪」"


show char tre08f2 at right as r
with dis



voice "Reo_0109"
re "「むうううっ」"

hide char tma02f2 at left
hide char tre08f2 at right as r
show char tyu02f2 at sleft as l
show char tma02f2
show char tre08f2 at sright as sr
with dis



voice "Yuuna_0054"
y "「いきなり連れてこられたことには、みんなびっくりしたと思うけれど、こうして会えたのは嬉しいわ」"
voice "Mai_0131"
ma "「本当ですね……一年前の合宿を思い出すわ」"
"連れてこられた経緯は、それぞれ違うけれど。"
"みんなと一緒にバカンスが過ごせるのは、単純に嬉しかった。"


#allClear:
hide char tyu02f2 at sleft as l
hide char tma02f2
hide char tre08f2 at sright as sr
#lastBG:
#scene bg bg39a
show char tyu01f2
with dis



voice "Yuuna_0055"
y "「それじゃあ皆さんで、麗奈先生に挨拶してきましょうか」"


show char tyu01f2 at left
show char tna02f2 at right as r
with dis



voice "Nanami0153"
n "「先生に会うのも、久しぶりですね」"
"ワクワクした気持ちを抱えながら、私たちはホテルへと移動した。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


show char trn02f2
with dis



voice "Rena_0010"
ren "「みんな、よく来たわね～、さあどうぞ」"


show char trn02f2 at left
show char tta02f2 at right as r
with dis



voice "Takako0020"
t "「みんな、いらっしゃい」"

hide char trn02f2 at left
hide char tta02f2 at right as r
show char trn02f2 at sleft as l
show char tta02f2
show char tru03f2 at sright as sr
with dis


##voice RUNA_0014
voice "Runa_0015"
rn "「……いらっしゃい」"
"ホテルに着いた私たちを出迎えてくれたのは、麗奈先生だけではなかった。"
"貴子先生や瑠奈さんも、一緒にいた。"


#allClear:
hide char trn02f2 at sleft as l
hide char tta02f2
hide char tru03f2 at sright as sr
#lastBG:
#scene bg bg37a
show char tre08f2 at left
show char tru03f2 at right as r
with dis



voice "Reo_0110"
re "「蓬莱泉瑠奈……アンタもここに来ていたのね」"


show char tru02f2 at right as r
with dis



voice "Runa_0016"
rn "「ええ。ねえさまに先に招待されていたのよ……ふふっ」"
"何だか、誇らしげ……というか、偉そうな様子だった。"
"でも笑顔が見られるのは、久しぶりにお姉さんに会えて、嬉しいってことね。"

hide char tre08f2 at left
hide char tru02f2 at right as r
show char ter02f2 at sleft as l
show char tre08f2
show char tru02f2 at sright as sr
with dis



voice "Erisu_0044"
e "「わぁっ、数ヶ月ぶりのちびっこ対決だね～」"
voice "Reo_0111"
re "「むうっ、ワタシの方がお姉さんなんだから、こんな子供と一緒にしないで」"
voice "Runa_0017"
rn "「ふふふっ、そうやってムキになるなんて、お姉さんっぽくないわよ」"


show char tre09f2
with dis



voice "Reo_0112"
re "「ななっ、なんですって～」"


#allClear:
hide char ter02f2 at sleft as l
hide char tre09f2
hide char tru02f2 at sright as sr
#lastBG:
#scene bg bg37a
show char tta03f2
with dis



voice "Takako0021"
t "「瑠奈、いけないわ。来て早々、絡むなんて」"


show char trn02f2 at left
show char tta03f2 at right as r
with dis



voice "Rena_0011"
ren "「まあまあ、いいじゃないの。賑やかで楽しいわ～」"


#allClear:
hide char trn02f2 at left
hide char tta03f2 at right as r
#lastBG:
#scene bg bg37a
show char tma01f2
with dis



voice "Mai_0132"
ma "「玲緒、あなたも少しは自重しなさい……麗奈先生、今回はお招き、ありがとうございます」"


show char tri01f2
with dis



voice "Risa_0568"
r "「あ、ありがとう……ございます」"
"麻衣さまの言葉で、まだ先生にお礼を言っていないことに気が付いた。"


#allClear:
hide char tri01f2
#lastBG:
#scene bg bg37a
with dis


"続いてみんなも同じく、お礼を言った。"
"強制連行とはいえ、こんな素敵なリゾート地に呼んでくださったんだもの。"
"そこはしっかりと、感謝の意を表さないと。"


show char trn02f2
with dis



voice "Rena_0012"
ren "「もう私も先生じゃないんだし、硬い挨拶はいいわ。しばらくはここでみんな、思いっきり楽しんでね」"


show char tsa02f2
with dis



voice "Sara_0073"
sr "「は～い{image=image/exch001.png}　仕事抜きでのバカンスなんて、滅多にないから嬉しいね、楓ちゃん」"


show char tka02f2 at left
show char tsa02f2 at right as r
with dis



voice "Kaede_0048"
# "【　楓　】「ふふふっ……そうね」"


#allClear:
hide char tka02f2 at left
hide char tsa02f2 at right as r
#lastBG:
#scene bg bg37a
show char tsi01f2
with dis



voice "Sizuku0039"
# "【　雫　】「エリスの実家に行く機会は、これからも何度だってありそうですし……今回はたくさん楽しみますわ」"


show char ter02f2 at left
show char tsi01f2 at right as r
with dis



voice "Erisu_0045"
e "「ウチはいつでもシズクなら、大歓迎だからね♪　また次の機会を待ってるよ」"


#allClear:
hide char ter02f2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg37a
show char tyu02f2
with dis



voice "Yuuna_0056"
y "「せっかくだから、素敵なバカンスを過ごしましょうね、七海」"


show char tyu02f2 at left
show char tna02f2 at right as r
with dis



voice "Nanami0154"
n "「はい、お姉さま」"


#allClear:
hide char tyu02f2 at left
hide char tna02f2 at right as r
#lastBG:
#scene bg bg37a
show char tmi01f2
with dis



voice "Miya_0285"
m "「………………」"
"美夜は何も言わないけれど、どこか楽しそうに見えた。"
"やっぱりこのメンバーでいるのが、私たちにはすごく居心地が良いみたい。"


show char tta01f2
with dis



voice "Takako0022"
t "「先輩、これでメンバー全員そろったみたいですね。皆さんをお部屋の方に案内しましょうか？」"


show char trn08f2 at left
show char tta01f2 at right as r
with dis



voice "Rena_0013"
ren "「いいえ、まだよ……まだ、全員じゃないわ」"


#allClear:
hide char trn08f2 at left
hide char tta01f2 at right as r
#lastBG:
#scene bg bg37a
show char tri03f2
with dis



voice "Risa_0569"
r "「全員……じゃない？？」"
"ベストカップルのメンバーはもう、ここにそろっているはずだけど。"
"他に誰か、麗奈先生の知り合いでも呼んでいるのかしら？"


show char trn01f2
with dis



voice "Rena_0014"
ren "「……あっ、来たわ。こっちよ～」"
"ホテルの入り口の方に向かって、麗奈先生が声をかける。"
"その場にいた、全員がそちらを向いた。"
"そこに現れたのは……"


show char tri01f2
with dis



voice "Risa_0570"
r "「りっ、六夏……と、沙雪さん」"
"六夏はきょろきょろと、落ち着かない様子で。"
"沙雪さんはどこか慣れたように従業員に荷物を預けて、私たちの方にやってきた。"


show char tka01f2
with dis



voice "Kaede_0049"
# "【　楓　】「あの２人も、呼ばれていたんですね」"


show char trn02f2 at left
show char tka01f2 at right as r
with dis



voice "Rena_0015"
ren "「今回、一番興味あるカップルなのよねぇ……ふふっ{image=image/exch001.png}」"


#allClear:
hide char trn02f2 at left
hide char tka01f2 at right as r
#lastBG:
#scene bg bg37a
show char tri03f2
with dis



voice "Risa_0571"
r "「う、ううっ……」"


show char tmi03f2 at left
show char tri03f2 at right as r
with dis



voice "Miya_0286"
m "「どうしたの、璃紗？」"
voice "Risa_0572"
r "「昨年のことをちょっと、思い出していたのよ……」"
"美夜とベストカップルに選ばれた直後。"
"なんとか取り下げてもらおうと、麗奈先生に直談判に行ったのだけれど。"
"今みたいな感じで、先生は面白がっていたのよね。"
voice "Risa_0573"
r "「先生は２人のこと、知っていたんですか？」"


show char trn01f2 at left
with dis



voice "Rena_0016"
ren "「もちろんよ。私の情報網をあなどらないでね」"
voice "Risa_0574"
r "「そ、そうですか……」"
"しっかりと、ご存知だったのね……"
"そしてやっぱり、面白がっているんだわ。"


#allClear:
hide char trn01f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg37a
show char tta03f2
with dis



voice "Takako0023"
t "「あら……あの２人って……」"
"おそらく２人に会うのは初めての貴子先生が、どこか戸惑っていた。"


show char tka01f2 at left
show char tta03f2 at right as r
with dis



voice "Kaede_0050"
# "【　楓　】「あの２人は今年選ばれた、ベストカップルの１年生です」"
voice "Takako0024"
t "「ベストカップル？　あの子が……そうなのね」"


#allClear:
hide char tka01f2 at left
hide char tta03f2 at right as r
#lastBG:
#scene bg bg37a
with dis


"そうこう言ってるうちに、六夏が先生に挨拶する。"


show char trn02f2 at left
show char trk03f2 at right as r
with dis



voice "Rikka_0319"
rk "「は、はじめまして、篠崎六夏です。今回はこんな素敵な場所にご招待してくださり、ありがとうございます」"
voice "Rena_0017"
ren "「はじめまして、篠崎さん。ゆっくり楽しんでいってね♪」"
voice "Rikka_0320"
rk "「はっ、はい……」"
"六夏は予想通り、ガチガチの緊張モードだった。"
"私と同じ庶民だもの、なかなかこういう場は、慣れないわよね。"
voice "Rena_0018"
ren "「白河さんも、いらっしゃい」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0130"
s "「お招きありがとうございます。今回は色々と、お手数をおかけしました」"


show char trn01f2 at left
with dis



voice "Rena_0019"
ren "「いいえ、たいした手間ではないわ。学生のうちにこういうことは、一度くらいは経験しておかないとね」"
voice "Sayuki0131"
s "「はい……ありがとうございます」"
voice "Rena_0020"
ren "「おばあ様にも、よろしく伝えておいてください」"
voice "Sayuki0132"
s "「はい、わかりました」"


#allClear:
hide char trn01f2 at left
hide char tsy01f2 at right as r
#lastBG:
#scene bg bg37a
show char tri03f2
with dis



voice "Risa_0575"
r "「んっ……おばあさま？？」"
"麗奈先生と沙雪さんってひょっとして、お知り合いなのかしら。"


show char tna03f2 at left
show char tri03f2 at right as r
with dis



voice "Nanami0155"
n "「沙雪さんと、麗奈先生って……初対面じゃないのかしら……」"
"七海さんも、その疑問を口にする。"

hide char tna03f2 at left
hide char tri03f2 at right as r
show char tyu01f2 at sleft as l
show char tna03f2
show char tri03f2 at sright as sr
with dis



voice "Yuuna_0057"
y "「多分、だけどね……」"
"優菜さまが小声で、そっと教えてくださった。"
voice "Yuuna_0058"
y "「沙雪さんはお家の関係上、そんなに簡単に外泊など出来る身分じゃないのよ」"
voice "Risa_0576"
r "「そ、そうなんですか？」"
"沙雪さんはお嬢様の中のお嬢様だと、聞いてはいたけれど。"
"あんまり具体的には、他の方とどう違うのか、わかってはいなかった。"
"お友達とお泊りするだけでも、大変なんだ……"
voice "Yuuna_0059"
y "「麗奈先生は蓬莱泉家もバックにあるし、先生ご自身もたくさんの繋がりがあるから、そこから白河家に直接、許諾を取ったんじゃないかしら」"
voice "Nanami0156"
n "「なるほど～、庶民には別世界の話ですね」"
"まったくだわ。"
"でもこれで、やっと全員揃ったわけね。"


#allClear:
hide char tyu01f2 at sleft as l
hide char tna03f2
hide char tri03f2 at sright as sr
#lastBG:
#scene bg bg37a
show char trn08f2
with dis



voice "Rena_0021"
ren "「とにかく……まずは全員、水着よっ！！」"


show char tri03f2
with dis



voice "Risa_0577"
r "「えっ？」"


show char trk03f2
with dis



voice "Rikka_0321"
rk "「ワタシ、水着持ってきてませんが……」"


show char trn02f2
with dis



voice "Rena_0022"
ren "「大丈夫よ、私がちゃんと用意してあるから、好きなのを選んでね」"


#allClear:
hide char trn02f2
#lastBG:
#scene bg bg37a
with dis


"麗奈先生は私たちを、ロビーの奥へと案内してくれた。"
"そこには信じられないくらい大量の水着が、まるでデパートの水着売り場のように並んでいた。"


show char tsa01f2
with dis



voice "Sara_0074"
sr "「うわぁ～、すごく迷っちゃうね、楓ちゃん」"


show char tka03f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0051"
# "【　楓　】「ええ……でもなんか、派手なのが多い気がするわ」"
voice "Sara_0075"
sr "「せっかくだから、うんと派手なのにしようよ」"
voice "Kaede_0052"
# "【　楓　】「そ、それは、ちょっと……」"


#allClear:
hide char tka03f2 at left
hide char tsa01f2 at right as r
#lastBG:
#scene bg bg37a
show char tma02f2
with dis



voice "Mai_0133"
ma "「はぁ、はぁ……玲緒の水着はぜったい、わたしが選んであげるわ{image=image/exch001.png}」"


show char tma02f2 at left
show char tre03f2 at right as r
with dis



voice "Reo_0113"
re "「麻衣……もう、興奮しすぎよ」"


#allClear:
hide char tma02f2 at left
hide char tre03f2 at right as r
#lastBG:
#scene bg bg37a
show char tri01f2
with dis



voice "Risa_0578"
r "「私は……どれにしようかしら……」"


show char tmi01f2 at left
show char tri01f2 at right as r
with dis



voice "Miya_0287"
m "「璃紗は水着持ってきてるでしょう？　わたくしが以前買ってあげたヤツ」"


show char tri03f2 at right as r
with dis



voice "Risa_0579"
r "「あ、あれね……」"
"美夜があんまりしつこく言うから、一応荷物の中に入れてきたけど。"
voice "Miya_0288"
m "「そうよ。あれを着ればいいでしょう？」"
voice "Risa_0580"
r "「で、でも……」"
voice "Miya_0289"
m "「さあ、着替えて来ましょう」"
voice "Risa_0581"
r "「ちょっと、美夜～」"


#allClear:
hide char tmi01f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg37a
with dis


"私は選ぶ時間を与えられず、美夜に更衣室に押し込まれてしまった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


"私が無理矢理、美夜に更衣室に連れて行かれた頃。"
"六夏はある人と、再会を果たしていた……"


show char tsy01f2
with dis



voice "Sayuki0133"
s "「六夏さん、私、水着はどれが似合うと思いますか？」"


show char trk01f2 at left
show char tsy01f2 at right as r
with dis



voice "Rikka_0322"
rk "「えええっ、ワ、ワタシが選ぶんですか……そうですね、じゃあ……このピンクとか白とかどうですか」"
voice "Sayuki0134"
s "「とても可愛いデザインですね」"


show char trk03f2 at left
with dis



voice "Rikka_0323"
rk "「あっ、でもこのフリルのついたのも、沙雪さんには似合いそうかも……」"


show char tta02f2 at left
show char trk03f2 at right as r
with dis



voice "Takako0025"
t "「ふふふっ、こんにちは。楽しそうですね」"


show char trk04f2 at right as r
with dis



voice "Rikka_0324"
rk "「こんにちは？　えっ……えええええーっ！？」"

hide char tta02f2 at left
hide char trk04f2 at right as r
show char tru08f2 at sleft as l
show char tta02f2
show char trk04f2 at sright as sr
with dis



voice "Runa_0018"
rn "「もう、驚きすぎよ……」"
voice "Rikka_0325"
rk "「お、お姉さん、なんでアナタがここに……」"
voice "Runa_0019"
rn "「だれがアナタのお姉さんよ、ずうずうしいわ」"


show char tta01f2
with dis



voice "Takako0026"
t "「瑠奈は、また……そんなこと言わないの。そういえば、自己紹介が遅れたわね」"
voice "Takako0027"
t "「私は墨廼江貴子。ミカ女附属で、教師をしています」"


show char trk03f2 at sright as sr
with dis



voice "Rikka_0326"
rk "「は、はぁ……先生だったんですか。それもミカ女の……」"
voice "Takako0028"
t "「そしてこの子は、蓬莱泉瑠奈。麗奈先生の妹で、ミカ女の中等科に通っているわ」"


show char tru09f2 at sleft as l
with dis



voice "Runa_0020"
rn "「それだけじゃないわ、せんせいの恋人よ！」"
voice "Rikka_0327"
rk "「えっ？　こ、恋人って……」"


show char tta04f2
with dis



voice "Takako0029"
t "「ちょ、ちょっと瑠奈、なんてこと言うの～」"


show char tru01f2 at sleft as l
with dis



voice "Runa_0021"
rn "「でも正直、わたしも驚いたわ。ご近所のアナタが、ベストカップルのメンバーだったなんて」"
voice "Rikka_0328"
rk "「は、はぁ……」"
voice "Runa_0022"
rn "「こっちのふわふわのお嬢様はまだしも、アナタみたいな庶民キャラが選ばれるなんてね」"


show char tta08f2
with dis



voice "Takako0030"
t "「なんて失礼なこと言うの、瑠奈！　篠崎さん、だったわね……ごめんなさいね」"
voice "Rikka_0329"
rk "「い、いえ……庶民なのは、本当ですし」"


show char tta07f2
with dis



voice "Takako0031"
t "「瑠奈、あなたもちゃんと謝りなさい」"
voice "Runa_0023"
rn "「いやよー、そんなことよりさっさと水着に着替えるわよ」"


hide char tru01f2 at sleft as l
with dis


voice "Takako0032"
t "「ちょっと、待ちなさい……あっ、それじゃ、また後ほど……」"


#allClear:
hide char tta07f2
hide char trk03f2 at sright as sr
#lastBG:
#scene bg bg37a
show char trk03f2 at left
show char tsy01f2 at right as r
with dis



voice "Sayuki0135"
s "「あらあら、行ってしまわれましたね」"
voice "Rikka_0330"
rk "「あの子、おねえさ……ううん、貴子先生の子供でも妹でもなかったんだ」"
voice "Rikka_0331"
rk "「恋人、って言っていたけれど……本当に？？」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0136"
s "「六夏さん、どうかしましたか？」"


show char trk01f2 at left
with dis



voice "Rikka_0332"
rk "「な、なんでもないです……水着、早く決めちゃいましょうね」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**海岸通り・昼
scene bg bg38a
with Dis



#mes on
#system on


show char trk01m
with dis



voice "Rikka_0333"
rk "「リサ姉っ！」"


show char tri01m at left
show char trk01m at right as r
with dis



voice "Risa_0582"
r "「六夏、やっぱりスポーティな水着を選んだのね」"


show char trk05m at right as r
with dis



voice "Rikka_0334"
rk "「リサ姉は……結構、大胆なヤツだね……」"


show char tri05m at left
with dis



voice "Risa_0583"
r "「でしょ？　もう、恥ずかしいわ……これ、美夜が選んだのよ」"

hide char tri05m at left
hide char trk05m at right as r
show char tmi01m at sleft as l
show char tri05m
show char trk05m at sright as sr
with dis



voice "Miya_0290"
m "「いいでしょう、それ。璃紗くらいのエロカワイイ子には、こういう水着が似合うのよ」"


show char trk03m at sright as sr
with dis



voice "Rikka_0335"
rk "「た、確かに……ちょっとエッチな感じもするけど、似合ってる……ような」"


show char tri01m
with dis



voice "Risa_0584"
r "「六夏、美夜の言う事は鵜呑みにしなくてもいいの。それより沙雪さんは？」"


show char trk01m at sright as sr
with dis



voice "Rikka_0336"
rk "「沙雪さんはまだ、水着を選んでるよ。悩んでいたから、モデルの紗良さまのアドバイスを受けていたみたい」"


show char tri08m
with dis



voice "Risa_0585"
r "「もう……六夏、こういう時こそ『ワタシが選んであげる』とか言って、自己ＰＲしなくちゃ！！」"


show char trk08m at sright as sr
with dis



voice "Rikka_0337"
rk "「無理ムリ、ワタシ、そういうセンスないし……」"
voice "Miya_0291"
m "「あら、どうやら決まったようよ、沙雪さん」"


#allClear:
hide char tmi01m at sleft as l
hide char tri08m
hide char trk08m at sright as sr
#lastBG:
#scene bg bg38a
show char tsa02m
with dis



voice "Sara_0076"
sr "「六夏ちゃん、お待たせ。沙雪ちゃん連れてきたよ」"


show char trk04m
with dis



voice "Rikka_0338"
rk "「沙雪さん………………っ！！」"


#※EV004
#allClear:
hide char trk04m
#lastBG:
#scene bg bg38a
scene bg EV04
with Dis



voice "Sayuki0137"
s "「うぅっ……なんだかこれ、とても恥ずかしいです。私は普通のワンピースか、スクール水着で良いのですが……」"
voice "Miya_0292"
m "「ワンピースはともかく、スク水はアブないわ。マニアが食いつくわよ」"
voice "Sayuki0138"
s "「このビキニとかいう水着、初めてです。肌の露出も多いですし……本当に、似合っているのでしょうか？」"
voice "Sara_0077"
sr "「うんうん、すっごく似合ってるよ。六夏ちゃんもそう思うよね？」"
voice "Rikka_0339"
rk "「………………」"
voice "Sara_0078"
sr "「あれっ……六夏ちゃん？」"


#※EV004P1
scene bg EV04p1
with Dis



voice "Rikka_0340"
rk "「沙雪さん……ああ、沙雪さんのビキニ……いい、すごくいい……です……」"
voice "Risa_0586"
r "「あらあら、完全に見とれちゃって……放心しているわ」"
voice "Sara_0079"
sr "「そのくらい、バッチリ似合ってるってことだよ。良かったね、沙雪ちゃん♪」"
voice "Sayuki0139"
s "「……はい、六夏さんが良いと思って下さるのなら……恥ずかしいですが、これで……お願いします」"
"結局、沙雪さんがビキニを着てくれたのはその日だけだったけど、ワタシは天にも昇る幸せな気持ちでした。"


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


show char tsa02m
with dis



voice "Sara_0080"
sr "「わぁ～、海だ海だぁ♪」"
"水着に着替え終わった私たちは早速、ビーチに飛び出していった。"


show char tri01m
with dis



voice "Risa_0587"
r "「さすがに全員水着だと、迫力あるわね～」"


show char tna03m at left
show char tri01m at right as r
with dis



voice "Nanami0157"
n "「……迫力、ありすぎです」"
voice "Risa_0588"
r "「ん、どうしたの、七海さん。その水着、すごく可愛いわよ」"
voice "Nanami0158"
n "「そんな慰めは、いりません……今のわたしには、すべてが目の毒です」"


show char tri03m at right as r
with dis



voice "Risa_0589"
r "「……はぁ？」"
"最初はちょっと恥ずかしいかと思った、この水着だけど。"
"麗奈先生セレクトの水着も結構セクシーなのが多いので、そんなに気にならなくなってきた。"


#allClear:
hide char tna03m at left
hide char tri03m at right as r
#lastBG:
#scene bg bg39a
show char tma01m
with dis



voice "Mai_0134"
ma "「これだけ人数いると、ビーチバレーとかやりたくなるわね」"


show char ter02m at left
show char tma01m at right as r
with dis



voice "Erisu_0046"
e "「わぁ、面白そう～」"


#allClear:
hide char ter02m at left
hide char tma01m at right as r
#lastBG:
#scene bg bg39a
show char tmi02m
with dis



voice "Miya_0293"
m "「ビーチバレー……ふふっ、いいわね」"


show char tmi02m at left
show char tri01m at right as r
with dis



voice "Risa_0590"
r "「美夜、めずらしく協力的ね。麗奈先生に言えば、ボールとか一通り用意はしてくれそうだけど」"


show char tmi01m at left
with dis



voice "Miya_0294"
m "「璃紗も一緒にやるのよ」"


show char tri03m at right as r
with dis



voice "Risa_0591"
r "「私も？　そんなに得意じゃないから……」"


show char tmi08m at left
with dis



voice "Miya_0295"
m "「いいえ、璃紗にはとても重要な役割があるから」"
voice "Risa_0592"
r "「重要、って……審判でもやれってこと？」"
voice "Miya_0296"
m "「そうじゃなくて、アタックを決めようとして、お約束のポロリを決める為のキャラクター……ずばり、ポロリ要員よっ！」"


show char tri09m at right as r
with dis



voice "Risa_0593"
r "「ぜぇ～ったい、しないからっ！」"

hide char tmi08m at left
hide char tri09m at right as r
show char tsa02m at sleft as l
show char tmi08m
show char tri09m at sright as sr
with dis



voice "Sara_0081"
sr "「それなら楓ちゃんも、同じくポロリ要員だよ」"


#allClear:
hide char tsa02m at sleft as l
hide char tmi08m
hide char tri09m at sright as sr
#lastBG:
#scene bg bg39a
show char tka09m at left
show char tsa02m at right as r
with dis



voice "Kaede_0053"
# "【　楓　】「それはありませんっ！」"


show char tsa02m at left
show char tmi02m at right as r
with dis



"美夜と紗良さんが２人で親指を突きあわせて、ニヤッと笑っていた。"
"もう、なんなのよ、２人とも。"
"変なところで、わかりあっちゃっているんだから。"


#allClear:
hide char tsa02m at left
hide char tmi02m at right as r
#lastBG:
#scene bg bg39a
with dis


"でも本当に、このメンバーでスポーツをした場合……やっぱり六夏が一番、上手い気がするわね。"


show char tri03m
with dis



voice "Risa_0594"
r "「そういえば六夏は、どこにいるんだろう？」"


show char tri01m
with dis



voice "Risa_0595"
r "「……あっ、いたいた……」"
"浜辺で１人だけど……何しているのかしら。"
voice "Risa_0596"
r "「……ねぇ、六夏」"


#※CU03
show char CU03
with dis



voice "Rikka_0341"
rk "「……んっ、はぁ～」"
"顔が赤いわ……もしかして、日射病。"
voice "Risa_0597"
r "「ちょっと六夏、アナタ大丈夫？」"
voice "Rikka_0342"
rk "「………………はぁ～、ああ、可愛いなぁ、沙雪さん{image=image/exch001.png}」"
voice "Risa_0598"
r "「えっ？」"
"六夏の視線の先を辿っていくと……水着姿の沙雪さんがいた。"
"本当に気に入ったのね、彼女のあの水着が。"
"ひたすら見とれているみたい。"
voice "Rikka_0343"
rk "「……あっ、リサ姉。リサ姉も来ていたんだね」"
voice "Risa_0599"
r "「今頃気づいたのね。でも六夏、こんなところに一人でいないで、沙雪さんのところに行ったら？」"
voice "Rikka_0344"
rk "「そ、そんなの、出来るわけない……無理だよ」"
voice "Risa_0600"
r "「でも、せっかくのバカンスじゃない」"
voice "Rikka_0345"
rk "「だって……あの水着姿を見ていたら、ドキドキが止まらなくて」"
voice "Risa_0601"
r "「まぁ、確かに……綺麗よね、うん」"
"どこかのご令嬢オーラ１２０％って感じだわ。"
voice "Rikka_0346"
rk "「見ているだけでも、鼻血が出そうだし……」"
voice "Risa_0602"
r "「………………はぁ～」"
"相変わらずの、ヘタレっぷりだわ。"
"休み前にアドバイスしたこと、もう覚えてないのかしら。"
voice "Risa_0603"
r "「もう、こうなったら……」"
voice "Rikka_0347"
rk "「ちょ、ちょっとリサ姉、なんで引っ張るの？」"


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


"私は六夏を、沙雪さんやその他のメンバーに気づかれないように、物陰に連れていった。"


#**岩場・昼
scene bg bg41a
with Dis



show char tri01m
with dis



voice "Risa_0604"
r "「……うん、ここなら平気ね」"


show char tri01m at left
show char trk03m at right as r
with dis



voice "Rikka_0348"
rk "「な、何なの？」"


show char tri08m at left
with dis



voice "Risa_0605"
r "「六夏、予定変更よ……このバカンス中に絶対、沙雪さんに告白するわよっ！！」"


show char trk04m at right as r
with dis



voice "Rikka_0349"
rk "「えぇぇぇっ！？」"
"そうよ……こんなビックチャンス、逃すわけにはいかないわ！！"
"私は六夏に、思いっきりハッパをかけたのだった。"


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
jump S019



