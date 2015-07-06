#「お姉さまとまったりゆっくり」

label S021:
$ save_name = "◇お姉さまとまったりゆっくり"


#※ここは七海視点で

#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


#♂MP12
play music "sound/BGM12.ogg"


show char tyu01f2
with dis



voice "Yuuna_0083"
y "「七海、七海……起きて」"

#♀SE063
play sound "sound/SE063.ogg"


voice "Nanami0184"
n "「ん……んんっ」"
"ブラインドの開く音と、眩しい光。"
"見慣れない天井に一瞬自分がどこにいるのか、忘れてしまいそうになる。"
voice "Yuuna_0084"
y "「七海ったら、お寝坊さんね。早く起きなさい」"


show char tyu01f2 at left
show char tna03f2 at right as r
with dis



voice "Nanami0185"
n "「……お姉さま」"
voice "Yuuna_0085"
y "「あらあら、髪がはねているわよ。後で梳かしてあげるから、まず顔を洗っていらっしゃい」"
"優しいお姉さまの声と、笑顔でここが南の島だったことを思い出す。"


show char tna01f2 at right as r
with dis



voice "Nanami0186"
n "「おはようございます、お姉さま」"


show char tyu02f2 at left
with dis



voice "Yuuna_0086"
y "「ええ……七海、今日も可愛いわね{image=image/exch001.png}」"
"眠い目をこすりながら起きると、頭がだんだんはっきりしてくる。"
"そうだ……わたし、お姉さまに聞きたいコトがあったんだわ。"
"今日こそは、ちゃんと言わないと……"


show char tna03f2 at right as r
with dis



voice "Nanami0187"
n "「あの、お姉さま……」"


show char tyu01f2 at left
with dis



voice "Yuuna_0087"
y "「早く準備していらっしゃい、七海。今日はみんなでスキューバーをする約束でしょう」"
voice "Nanami0188"
n "「あ、あの……」"
"有無を言わせず、洗面所の方に連れていかれてしまう。"
voice "Nanami0189"
n "「はぁ～……仕方ないわ、朝の準備が終ってからにしようっと」"


#allClear:
hide char tyu01f2 at left
hide char tna03f2 at right as r
#lastBG:
#scene bg bg37a
with dis


"ところが――"
"朝ごはんを食べ終わり、お姉さまと話をしようとした途端。"
"みんなが迎えに来て、すぐにスキューバーに出かけることになり。"
"あっという間に、一日が終ってしまった……"


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


show char tna10f2
with dis



voice "Nanami0190"
n "「ううっ、今日もお姉さまと一日遊んでしまったわ」"


#allClear:
hide char tna10f2
#lastBG:
#scene bg bg38a
with dis


"南の島に来てからというもの、毎日遊んでばかり。"
"お姉さまは楽しそうだけど、本当はわたしは……"


show char tri03f2
with dis



voice "Risa_0662"
r "「七海さん、１人でどうしたの？」"


show char tri03f2 at left
show char tna01f2 at right as r
with dis



voice "Nanami0191"
n "「あっ……璃紗さん……」"
"わたしは友達の顔をじっと見つめる。"
"クラス委員を毎回務めて、しっかりもので、頭だって良い璃紗さん。"
"彼女もわたしと同じく、遊んでばかりだけれど……それでいいのかしら？"


show char tna03f2 at right as r
with dis



voice "Nanami0192"
n "「あの……璃紗さん、璃紗さんは夏休みの前半、何をしていたの？」"


show char tri01f2 at left
with dis



voice "Risa_0663"
r "「私？　私は美夜と一緒に、夏期講習に行っていたわ」"
"そう言って、璃紗さんが教えてくれた名前は。"
"短期集中型の厳しくて有名なカリキュラムの講習会だった。"


show char tna04f2 at right as r
with dis



voice "Nanami0193"
n "「す、すごいね……」"
voice "Risa_0664"
r "「そんなことないわよ。もともと前半は勉強に力をいれて、後半はどこか遊びに行こうかって計画、立てていたところだったから」"
voice "Nanami0194"
n "「ふぇ、ふぇぇ……」"
"やっぱり璃紗さんはこういうところ、しっかりとしているのね。"
voice "Risa_0665"
r "「七海さんは？　やっぱり優菜さまと一緒だったの？？」"


show char tna01f2 at right as r
with dis



voice "Nanami0195"
n "「うん、優菜さまの別荘に行っていたの」"


show char tri02f2 at left
with dis



voice "Risa_0666"
r "「そう、素敵ね……」"
voice "Nanami0196"
n "「ううん、遊びというより、優菜さまに環境整備委員会での後継者教育を受けていたんだけど」"


show char tri01f2 at left
with dis



voice "Risa_0667"
r "「あっ、そういうことだったの。それじゃ、こっちに来てからはいい息抜きになったんじゃないの？」"
voice "Nanami0197"
n "「あ……うん……」"
"息抜きというより、遊んでばっかりだわ。"
"前半はあんなにみっちり毎日、勉強していたのに……"
"ここに来ても、その勉強は続くんじゃないかと、ドキドキしていたのに……"
"そんな様子はまるでなかった。"
"何だか逆に、不安になってきた。"
voice "Nanami0198"
n "「明日こそは……お姉さまに聞いてみましょう」"
"じゃないと安心して、遊んでいられないわ。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチテラス・昼
scene bg bg40a
with Dis



#mes on
#system on


show char tyu01m
with dis



voice "Yuuna_0088"
y "「七海、今日はどこに行く？　泳ぎに行く？　それともこのままのんびりビーチでお昼寝でもする？」"


show char tyu01m at left
show char tna01m at right as r
with dis



voice "Nanami0199"
n "「いいえ、その前にちよっと……」"
voice "Yuuna_0089"
y "「あら、出かけないの？　それじゃあホテルでまったりかしら」"
voice "Nanami0200"
n "「そうじゃなくて、お姉さまに聞きたいことがありまして……」"
voice "Yuuna_0090"
y "「何かしら？」"


show char tna03m at right as r
with dis



voice "Nanami0201"
n "「あの……後継者教育のお勉強、もうしなくていいのですか？」"


show char tyu04m at left
with dis



voice "Yuuna_0091"
y "「七海、あなた……」"
"お姉さま、吃驚してる。"
"でも今のままでは、わたしも不安で仕方ない。"
"元々、自分に自信がなかったんだけど、優秀な後輩の沙雪さんの登場で、わたしはますます不安になっていたから。"
"勉強をするならする、しないならしないで、お姉さまの考えがちゃんと聞きたかった。"


show char tyu01m at left
with dis



voice "Yuuna_0092"
y "「七海ったら……そんなこと、気にしていたの？」"
"わたしの不安を吹き飛ばすように、お姉さまはニッコリと笑う。"


show char tyu02m at left
with dis



voice "Yuuna_0093"
y "「せっかくのバカンスよ。ゆっくりまったり楽しみましょうよ{image=image/exch001.png}」"


show char tna02m at right as r
with dis



voice "Nanami0202"
n "「は、はい{image=image/exch001.png}」"
"良かった～。"
"お姉さまの言葉に、なんかホッとする。"
"絶対的に信頼しているお姉さまが、穏やかに微笑みながら、そう言ってくれたんだもの。"
"いいんだよね、安心してもいいんだよね、わたし。"
"ここにいる間は、バカンスを楽しんでいいんだわ。"
voice "Nanami0203"
n "「そうと決まれば、わたし、たくさん楽しみます」"


show char tyu03m at left
with dis



voice "Yuuna_0094"
y "「朝から元気がないから、どうしたのかと思ったわ。私はてっきり……」"


show char tna03m at right as r
with dis



voice "Nanami0204"
n "「なんです？」"


show char tyu02m at left
with dis



voice "Yuuna_0095"
y "「昨日のエッチが物足りないのかと思って{image=image/exch001.png}」"


show char tna09m at right as r
with dis



voice "Nanami0205"
n "「ち、違いますっ！　朝からそんなこと考えません」"
voice "Yuuna_0096"
y "「あら？　私は朝から七海の寝顔を見るだけで、ムラムラって♪」"


show char tna08m at right as r
with dis



voice "Nanami0206"
n "「はうううっ！　と、とにかく今日からは思いっきり、バカンスを満喫するんで」"
"あれっ？"


show char tna03m at right as r
with dis



voice "Nanami0207"
n "「でも、バカンスって具体的に何をすればいいんでしょうか？」"
"ここ最近、とっても忙しくて。"
"勉強してるか、寝てるか、お姉さまとえっちするか……"
"それしかしていなかった気がする。"
"南の島に来てからも、みんなと一緒に行動していただけで、自分で何かをしていたわけではない。"
"自由になったのはいいけれど、何からしたらいいかわからないなんて……"
"わたしって、間抜けすぎるわ。"
"お姉さまに素直に相談すると、さっきのように優しく微笑みながら、言ってくれた。"
voice "Yuuna_0097"
y "「じゃあ私が七海に、バカンスというものを教えてあげるわ」"


show char tna02m at right as r
with dis



voice "Nanami0208"
n "「お姉さま……はいっ」"
"お姉さまは本当に、何でも知っているのよね。"
"きっと、素敵なバカンスになるに違いないわ。"


show char tyu01m at left
with dis



voice "Yuuna_0098"
y "「でもその前に、昨日のエッチが物足りなかった七海ちゃんに、サービスを……」"


show char tna05m at right as r
with dis



voice "Nanami0209"
n "「だから、そんなこと言ってません……あっ、胸触らないでください、あぁん」"


show char tyu02m at left
with dis



voice "Yuuna_0099"
y "「だーめ、うふふ{image=image/exch001.png}」"
"お姉さまは朝からしっかりと、エロ乙女でした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#※EV007
scene bg EV07
with Dis




#mes on
#system on


voice "Nanami0210"
n "「あ、あの……お姉さま」"
voice "Yuuna_0100"
y "「なぁに？　七海」"
voice "Nanami0211"
n "「わたし達、今何をしているんでしょうか」"
"バカンスを教えてくれると言われたけれど。"
"２人してぼんやりと、ビーチに寝そべっているだけのような……"
voice "Yuuna_0101"
y "「まったり日光浴よ。七海、もう飽きたのかしら？」"
voice "Nanami0212"
n "「いえ、そんなことはありません。お姉さまと一緒にいられるんですから……飽きるわけがありません」"
voice "Yuuna_0102"
y "「ふふふっ、可愛いこと言ってくれるのね、ちゅっ{image=image/exch001.png}」"
voice "Nanami0213"
n "「はうっ、お姉さま！」"
"軽くだけど、キスされてしまった。"
voice "Nanami0214"
n "「だっ、誰かに見られちゃいますよ」"
voice "Yuuna_0103"
y "「別に、かまわないわ……ふあぁぁ」"
"のんびりと欠伸をして、何でもないことのように言う。"
voice "Nanami0215"
n "「で、でも……」"
voice "Yuuna_0104"
y "「もう、ごちゃごちゃ考えないの、ほら」"
"今度は軽く抱きしめられる。"
voice "Nanami0216"
n "「わわわっ……」"
voice "Yuuna_0105"
y "「七海、柔らかい～！　ふふふっ」"
voice "Nanami0217"
n "「お、お姉さま」"
voice "Yuuna_0106"
y "「しっ、少しだけ黙って……」"
"お姉さまに止められて、口を閉じると。"
"波の音だけが、静かにわたし達の耳に響く。"
voice "Yuuna_0107"
y "「七海と抱き合って、こうして波の音を聞くのって……いいわね」"
voice "Nanami0218"
n "「……そうですね」"
"お姉さまにソフトに抱きしめられて、こうしていると、何だか落ち着いてくる。"
voice "Yuuna_0108"
y "「………………」"
voice "Nanami0219"
n "「………………」"
"……どのくらい、そのままでいたのか。"
"お姉さまはゆっくりと立ち上がって、わたしに手を差し伸べる。"
voice "Yuuna_0109"
y "「少し暑くなってきたわね。ちょっとだけ泳ぎましょうか」"
voice "Nanami0220"
n "「はい」"


#**青空
scene bg bg42a
with Dis



"立ち上がり、海に入る。"
"そしてお姉さまの言葉通り、少しだけ泳いでから、また一休み。"
"２人で寝そべって波の音を聞きながら、キスをしたり、抱き合ったり。"
"美味しいフルーツを食べたり、ジュースを飲んだり。"
"そこにはゆったりとした時間が流れていた。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#※EV007
scene bg EV07
with Dis



#mes on
#system on


voice "Nanami0221"
n "「……これはすごく、楽しいけれど」"
"ゆったりしすぎな気がしないでもない。"
"この間までの、忙しさがウソのようで、逆にまた不安になる。"
voice "Nanami0222"
n "「お、お姉さま……」"
"何度目かの日光浴の最中、わたしはまた、お姉さまに聞いてみた。"
voice "Nanami0223"
n "「これ、ゆったりしすぎじゃないでしょうか？」"
voice "Yuuna_0110"
y "「七海……」"
voice "Nanami0224"
n "「どうせここでのんびりするなら、資料を持ってきて、それを読みながらでもいいんじゃ……」"
voice "Yuuna_0111"
y "「もう、七海ったら……私とのんびりするのがつまらないの？」"
voice "Nanami0225"
n "「そ、そんなわけは……ただわたしはなかなか物覚えも悪いから、こうしてる間にも、以前教えてもらったことを忘れてしまいそうで」"
voice "Yuuna_0112"
y "「馬鹿ね、七海は。七海はちゃんとできているわ。だから私が後継者に選んだんじゃない」"
"諭すように、そう言われる。"
voice "Nanami0226"
n "「お姉さま……」"
"お姉さまはわたしのこと、信じてくださっているんだわ。"
"だったらわたしも、自分にもっと自信をもたないといけないのかもしれない。"
"お姉さまが信じてくれているのに、自分が自分を信じないって、ある意味お姉さまを信じていないってことになってしまうもの。"
voice "Yuuna_0113"
y "「休むときは休む、楽しむときは楽しむ。そうしないと、立派なリーダーにはなれないわよ」"
voice "Nanami0227"
n "「……はい、お姉さま」"
voice "Yuuna_0114"
y "「うふふ、そういうわけで、バカンスの続きしましょう～♪」"
voice "Nanami0228"
n "「ええ！　わっ、お姉さま……」"
voice "Yuuna_0115"
y "「逃げても、だめよ。バカンスを教わりたいって言ったのは、七海なんですからねっ」"
"ごろごろと猫のように、お姉さまが甘えてくる。"
voice "Nanami0229"
n "「それはわかりますけど……いつものお姉さまらしからぬ、ゆったりぷりじゃないですか」"
voice "Yuuna_0116"
y "「それは……七海がいるからよ」"
voice "Nanami0230"
n "「ええっ！」"
voice "Yuuna_0117"
y "「いくらまったりなバカンスでも、傍に七海がいてくれなくちゃ、私はつまらないわ」"
"わたしが……いるから？"
"もしかしてわたしの為に、こんなにのんびり過ごしてくれているの？"
voice "Yuuna_0118"
y "「別荘にいる間……ずっと厳しくしてしまって、ゴメンね」"
voice "Yuuna_0119"
y "「でも、このバカンス中だけは、思いっきり私に甘えていいわよ{image=image/exch001.png}」"
voice "Nanami0231"
n "「お姉さまっ！」"
"わたしは高ぶる気持ちのまま、お姉さまに抱きついた。"
voice "Yuuna_0120"
y "「あんっ♪　七海」"
"お姉さまが愛しくて、嬉しくて仕方ない。"
voice "Nanami0232"
n "「お姉さま、大好きです」"


#※EV007P1
scene bg EV07p1
with Dis



voice "Yuuna_0121"
y "「私もよ、七海……だめ、可愛すぎるわ{image=image/exch001.png}　ここでこのまま、七海と……んふふっ」"
voice "Nanami0233"
n "「ダメ、ダメダメダメダメダメ～ダメです！」"
"それだけは、いくらなんでも……"
voice "Yuuna_0122"
y "「そんなに嫌がらなくてもいいのに」"
voice "Nanami0234"
n "「部屋に帰ったら、いくらでも……しますから」"
voice "Yuuna_0123"
y "「そう、いくらでも……なのね。七海のエッチ{image=image/exch001.png}」"
voice "Nanami0235"
n "「どうして、そうなるんですかっ！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチテラス・昼
scene bg bg40a
with Dis



#mes on
#system on


show char tna03m
with dis



voice "Nanami0236"
n "「もう、お姉さまったら……可愛がってもらえるのは嬉しいけど、どうしてすぐにエッチな話にしてしまうんですか？」"


show char tyu02m at left
show char tna03m at right as r
with dis



voice "Yuuna_0124"
y "「だって……愛しい人とはいつだってしたいでしょう、エッチって{image=image/exch001.png}」"
voice "Nanami0237"
n "「お姉さまのエロ乙女はもう、不治の病ですね。一生治らないかも」"


show char tyu03m at left
with dis



voice "Yuuna_0125"
y "「治す必要、あるの……七海？」"
voice "Nanami0238"
n "「そ、それは……ぅぅ……」"


show char tyu01m at left
with dis



voice "Yuuna_0126"
y "「完全に治してしまって、エロさ０％、まともさ１００％の私になって欲しいのかしら？」"
voice "Nanami0239"
n "「そんな、極端な……ちょうど良いバランスは選べないんですか？」"


show char tyu08m at left
with dis



voice "Yuuna_0127"
y "「それは………………無理ね。デッド・オア・アライブ、二つに一つよ」"


show char tna05m at right as r
with dis



voice "Nanami0240"
n "「はうぅぅっ、だ、だったら……エロ乙女の、方が……きゃんっ{image=image/exch001.png}」"


show char tyu02m at left
with dis



voice "Yuuna_0128"
y "「そうよ、そっちが正解よ、七海{image=image/exch001.png}　じゃあ早速、お部屋に戻りましょう。そこでめいっぱい、私に甘えてね{image=image/exch001.png}」"
voice "Nanami0241"
n "「は……はい、じゃあ……甘え、ます……ね」"
"エッチな事って恥ずかしいけど、でも……嫌いじゃない。"
"お姉さまにだけなら、甘えさせて欲しい……可愛がって欲しいもの。"


#**青空
#allClear:
hide char tyu02m at left
hide char tna05m at right as r
#lastBG:
#scene bg bg40a
scene bg bg42a
with Dis



voice "Nanami0242"
n "「あぁぁんっ{image=image/exch001.png}　でもでもぉ、お姉さまエッチすぎますぅぅ、はぁん{image=image/exch001.png}」"
"相変わらずのエロ乙女全開な、お姉さまでした。"
"その後も、２人でまったりゴロゴロしながら。"
"たくさんたくさん、甘えさせてもらったのでした{image=image/exch001.png}"


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
jump S022


