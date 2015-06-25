#「家出、してしまいました」

label S048:
$ save_name = "◇家出、してしまいました"


#**六夏の部屋・夜
scene bg bg34c
with Dis



#mes on
#system on


#♂MP01
play music "sound/BGM01.ogg"


show char trk03f2
with dis



voice "Rikka_1299"
rk "「………………はぁ～」"
"ワタシは一人、見慣れた天井を見上げて、深いため息をついた。"
"沙雪さんとのコトは、自分で何とかしよう、解決しよう。"
"そう強く決意をしたのは良いが、どうすれば良いのかサッパリ分からなかった。"
voice "Rikka_1300"
rk "「まずは沙雪さんを説得して、２人で一緒に、彼女のおばあ様に……ぅぅっ」"
"想像しただけで緊張して、足が震えてきた。"
"相手はこの国でも屈指の、名家の当主なんだ。"
voice "Rikka_1301"
rk "「ワタシが、ワタシなんかが何か言ったって、聞いてもらえないかも……ううん、きっと聞いてくれない」"
"自分で呟いていて、軽く絶望的な気持ちになってきた。"
voice "Rikka_1302"
rk "「ああ、やっぱりリサ姉や美夜さまに、力を借りた方が……ううん、ダメ！　ダメだよ、それは」"
"沙雪さんに告白する為に、すごく力を貸してもらったんだもの。"
"これ以上はきっと、迷惑なはず。"
voice "Rikka_1303"
rk "「それに……これはあくまで、ワタシと沙雪さんの問題なんだから……」"

#//SE：チャイム音
#♀SE024
play sound "sound/SE024.ogg"


voice "Rikka_1304"
rk "「ん……誰だろう、こんな時に……」"
"１人でゆっくり、考えたかったのに……正直、出るのが面倒だった。"
voice "Rikka_1305"
rk "「どうせ、新聞の勧誘かなんかだろうし。無視していれば……」"

#//SE：チャイム音
#♀SE024
play sound "sound/SE024.ogg"


voice "Rikka_1306"
rk "「２度目か、しつこいなぁ、もう……」"
"それでもワタシは、無視し続けた。"
"本当に今は、余計なコトをしたくなかった。"

#//SE：チャイム音
#♀SE024
play sound "sound/SE024.ogg"


show char trk09f2
with dis



voice "Rikka_1307"
rk "「くぅぅっ、もう、ワタシは静かにして欲しいだけなのにっ！！」"
"これ以上、イライラさせられてはたまらない。"
"ワタシは立ち上がって、インターホンのボタンを押した。"


show char trk07f2
with dis



voice "Rikka_1308"
rk "「いい加減にして下さい、新聞なら間に合って……えぇっ！？」"


show char trk07f2 at left
show char tsy03p at right as r
with dis



voice "Sayuki0671"
s "『申し訳ありません、新聞は持ってきておりませんが……』"


show char trk04f2 at left
with dis



voice "Rikka_1309"
rk "「さ、ささっ、沙雪さん！？　今開けます、すぐ開けますから、ちょっと待ってて下さいっ！！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**六夏の部屋・夜
scene bg bg34c
with Dis



#mes on
#system on


show char tsy01f2
with dis



voice "Sayuki0672"
s "「ここが、六夏さんのお部屋……」"


show char trk03f2 at left
show char tsy01f2 at right as r
with dis



voice "Rikka_1310"
rk "「………………」"
"どうして……こんなコトになっているの？"
"なんで沙雪さんが、ワタシの部屋にいるの？？"
"ひょっとしたら、もう会えないかも……そんな不安さえ、抱いていたのに。"
"沙雪さんは自分の方から、ワタシに会いに来てくれた。"
"この驚きの状況に、ワタシは喜びながらも、どこか呆然としてしまって。"
"一方の沙雪さんはキョロキョロと、この普通すぎる部屋を見回していた。"


show char tsy03f2 at right as r
with dis



voice "Sayuki0673"
s "「とてもシンプルで、清潔なお部屋ですね……ですが少々、手狭ではありませんか？」"
voice "Rikka_1311"
rk "「へっ？　そ、そんなコトはないですよ。ワタシには、これで十分で……」"
voice "Sayuki0674"
s "「そう……ですか」"
voice "Rikka_1312"
rk "「ちなみに沙雪さんの部屋は、どのくらい広いんですか？」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0675"
s "「私の部屋ですか？　大体、ここの５倍くらい……と思います」"
voice "Rikka_1313"
rk "「そ、そうですか……あは、あははっ……」"
"広いとは思っていたけれど、まさかそこまで違うとは思わなかった。"
"お風呂とトイレを合わせても、ここ全部よりも沙雪さんの部屋の方が広そうだ。"
voice "Rikka_1314"
rk "「狭くてすみません……沙雪さん」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0676"
s "「いいえ、そのような事は……私の方こそ、いきなり来てしまいまして、申し訳ありませんでした」"


show char trk01f2 at left
with dis



voice "Rikka_1315"
rk "「い、いえ……沙雪さんなら、大歓迎です……」"
"一応、ここの住所は前に教えておいたけれど。"
"まさか来てもらえるなんて、思ってもいなかった。"
voice "Rikka_1316"
rk "「ところで、その……今日は、どうして？」"
voice "Sayuki0677"
s "「そ……それは……その……」"
"思わず聞いてしまったが、理由なんてあんまり考える必要はなかった。"
"ワタシと沙雪さんは、恋人なんだから……会いたいから、会いに来てくれた。"
"それだけだと思った。"


show char trk05f2 at left
with dis



voice "Rikka_1317"
rk "（でももし、沙雪さんから『六夏さんに会いたくなって、来てしまいました{image=image/exch001.png}』なんて言われたら……ああ、想像しただけでクラクラしちゃいそう）"
voice "Sayuki0678"
s "「あの、実は……私、家を出てきました」"


show char trk03f2 at left
with dis



voice "Rikka_1318"
rk "「そんな、ワタシに会いに来てくれたなんて……えっ！？　沙雪さん、今なんて……？」"


show char tsy08f2 at right as r
with dis



voice "Sayuki0679"
s "「ですから、私……家出して、しまいました」"


show char trk04f2 at left
with dis



voice "Rikka_1319"
rk "「えぇぇぇっ！？」"


#allClear:
hide char trk04f2 at left
hide char tsy08f2 at right as r
#lastBG:
#scene bg bg34c
with dis


"沙雪さんのその言葉に、ワタシはただただ呆然としてしまった。"
"あの沙雪さんが、家出？"
"それも、ワタシのところに？？"
"一体、何がどうなっているのか、ワタシにはさっぱりわからなかった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**六夏の部屋・夜
scene bg bg34c
with dis



#mes on
#system on


"とりあえず沙雪さんには、荷物を……と言っても、小さなバッグ一つだけど……を、置いてもらって。"
"座ってもらい、すぐにお茶を用意した。"


show char tsy02f2
with dis



voice "Sayuki0680"
s "「ありがとうございます、六夏さん」"


show char trk01f2 at left
show char tsy02f2 at right as r
with dis



voice "Rikka_1320"
rk "「いえ、このくらいは……ところでどうして、いきなり家出なんて……」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0681"
s "「それは……ぅぅ……」"
"ものすごく言いづらそうに、うつむいてしまう沙雪さん。"
"でも、いつまでも黙っていられないと思ったのか、やがて静かに口を開いた。"
voice "Sayuki0682"
s "「実は、祖母……おばあ様が……早急に、私の結婚話を進めているのです」"


show char trk03f2 at left
with dis



voice "Rikka_1321"
rk "「そ、そう……なんですか……」"
"驚きはしたものの、それほどでもなかった。"
"だってその事は、美夜さまから聞いていたから。"
"この驚きは、やっぱり美夜さまの情報が本当だったんだ……というショックからだった。"
voice "Sayuki0683"
s "「結婚なんて、ミカ女を卒業してからの話だと思っていたのに……来週、顔合わせをするなんて……」"


show char trk04f2 at left
with dis



voice "Rikka_1322"
rk "「らっ、来週！？」"
"そんなに急ぎだとは、夢にも思わなかった。"
"あまりに焦り過ぎて、もう絶句などしていられなかった。"
"これじゃあ、一人でゆっくりと対策を考えている余裕なんてなくなってしまった。"


show char trk03f2 at left
with dis



voice "Rikka_1323"
rk "「ど、どうしてそんな、急な話になったんですか！？」"
voice "Sayuki0684"
s "「私も、よく分かりません……ですが、おばあ様は本当に急いでおられて……」"
"泣きそうになりながらも、沙雪さんは話を続けた。"
voice "Sayuki0685"
s "「私は断って下さいと頼みました。ですがおばあ様は『これはお前の幸せの為だ、いいから従いなさい』と言うだけで、私の話を聞いてもらえなくて……」"
voice "Rikka_1324"
rk "「そんな、一方的な……」"


show char tsy08f2 at right as r
with dis



voice "Sayuki0686"
s "「ですから、私……どうしても、おばあ様が許せなくて……それなら私にも考えがあります、と」"
"あの沙雪さんが珍しく、感情的になっていた。"
"いつもの穏やかで、おしとやかなしゃべり方ではなくなっていた。"
voice "Rikka_1325"
rk "「だから、家出してきてしまった……と」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0687"
s "「はい、そうです。私、他に行く場所が思いつかず……ご迷惑をかけてしまうと思いましたが、私……私……」"


show char trk08f2 at left
with dis



voice "Rikka_1326"
rk "「迷惑だなんて、そんなコトありません、まったくありませんっ！！」"
"もう今すぐ、沙雪さんを抱きしめたかった。"
"ワタシを頼ってくれた、ここに来てくれた事が、本当に嬉しかった。"
"そんな沙雪さんを守りたい、彼女の期待に応えたい。"
"そう思っているのに……一方で、どこか怖じ気づいているワタシもいた。"
"だって彼女をここに置くという事は、沙雪さんのおばあ様を怒らせるという事で。"
"そんな偉い人を本気で怒らせてしまったら、もう沙雪さんとは、二度と……"


show char trk03f2 at left
with dis



voice "Rikka_1327"
rk "（それに、沙雪さん……家出にしては、随分小さいバッグだったよね）"
voice "Rikka_1328"
rk "「あの……沙雪さん、家出の経験は……？」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0688"
s "「はい、もちろん……初めて、ですが」"
voice "Rikka_1329"
rk "「やっぱり、ね……」"
"きっと、勢いだけで出てきてしまったんだ。"
"本音を言えば、困っている沙雪さんを帰したくない、一緒にいたい。"
"でも……だけど……"
"ワタシは沙雪さんから一歩退いて、静かに告げた。"
voice "Rikka_1330"
rk "「沙雪さん……やっぱり、いきなり家出はダメだよ。家の人が心配するよ」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0689"
s "「そ、それは……分かってます、分かっております、でも……」"
voice "Rikka_1331"
rk "「やっぱりさ、帰った方がいいよ。ワタシ、近くまで送っていくから」"


show char tsy07f2 at right as r
with dis



voice "Sayuki0690"
s "「いいえ、ダメです。そうはいきませんっ！！」"
voice "Rikka_1332"
rk "「沙雪……さん……」"
"こんな沙雪さんを見るのは、初めてだった。"
"さっきまで泣きそうだったのに、そのまま崩れ落ちてしまいそうだったのに。"
"今、彼女は潤んだ瞳でまっすぐに、ワタシを見つめていた。"
voice "Rikka_1333"
rk "「沙雪さん、どうしてそこまで……」"
voice "Sayuki0691"
s "「私、本気です。本気で六夏さんの事を、愛しております。ですから……他の方に嫁ぐなど、もう考えられません」"
voice "Rikka_1334"
rk "「沙雪さん……うぅっ、そんなコト言われたら……」"
"ますます帰したくなくなっちゃう、抱きしめたくなっちゃう。"
"このまま、彼女を受け入れてしまいたくなる。"
"それでもワタシはしばらく、グッと気持ちを抑えて説得を続けた。"


show char tsy08f2 at right as r
with dis



voice "Sayuki0692"
s "「六夏さんが何を言っても、家には戻りません。ここに置いて頂けないのなら、どこかのホテルに部屋を取ります」"
voice "Rikka_1335"
rk "「そんな……ああ、もう……」"
voice "Rikka_1336"
rk "（ここまで沙雪さんが頑固だなんて、思いもしなかったよ。今の興奮状態にある彼女を説得するのは、難しいかも……）"
"もし追い返してしまったら、どこに行ってしまうか分からない。"
"だったら……ここにいてもらった方が良いかも。"
"とりあえず、彼女が落ち着くまで待って、それからあらためて話をしよう……"


show char trk01f2 at left
with dis



voice "Rikka_1337"
rk "「沙雪さん、沙雪さんの気持ちはよくわかりました。そこまでワタシを想って頂いて、本当に嬉しいです」"


show char tsy03f2 at right as r
with dis



voice "Sayuki0693"
s "「六夏、さん……それでは……？？」"
voice "Rikka_1338"
rk "「はい。しばらくはここにいてくれていいです」"


show char tsy06f2 at right as r
with dis



voice "Sayuki0694"
s "「あっ、ありがとうございますっ！！　う、うぅぅ、ぅぅっ……」"
"まるで緊張の糸が切れたように、沙雪さんはうなだれ、泣き出してしまった。"
"そんな彼女をそっと抱きしめて、ワタシはあらためて言った。"
voice "Rikka_1339"
rk "「でも、しばらくですよ……落ち着いたらちゃんと、これからのコトを考えましょう」"
voice "Sayuki0695"
s "「ぅ、ぅぅ……ひっく……六夏さん……」"
voice "Rikka_1340"
rk "「ワタシも一緒に考えますから、だから……ね？」"
voice "Sayuki0696"
s "「……はい、わかりました。ありがとうございます、六夏さん」"
"涙を拭って、はにかみながら、お礼を言ってくれた。"
"怒ったり、乱れたり、泣いたり、でも笑ったり。"


show char trk02f2 at left
with dis



voice "Rikka_1341"
rk "（なんか、こういう感情的な沙雪さんも可愛いなぁ……ふふっ{image=image/exch001.png}）"


#allClear:
hide char trk02f2 at left
hide char tsy06f2 at right as r
#lastBG:
#scene bg bg34c
with dis


"ちょっとだけ力を込めて、沙雪さんを強く抱きしめる。"
"一緒って事は、いつでもこうして抱き合えるって事で……ああ、なんて素敵なんだろう。"
"不安は残るけれど、今だけはこの幸せな気持ちに流されたいと、思ってしまったのだった。"


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
jump S049



