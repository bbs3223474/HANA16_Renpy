#「玲緒のお姉さんＤＡＹＳ」

label S116:
$ save_name = "◇玲緒のお姉さんＤＡＹＳ"


#**玲緒の部屋・夜
scene bg bg33c
with Dis



#mes on
#system on


#♂MP01
play music "sound/BGM01.ogg"


show char tre03f2
with dis



voice "Reo_0812"
re "「ただいまー、ふうー、疲れたわ」"
"麻衣のお手伝いをすると決めた日から。"
"ワタシは放課後になると、麻衣の家に行って。"
"麻衣がお家のことをしている間、弟や妹の面倒を見ることになった。"
"そして夜になると、麻衣の作った美味しいご飯を食べて。"
"それからこうやって、自分のマンションに帰ることにしていた。"
voice "Reo_0813"
re "「ああ、簡単に引き受けたけど……誰かの世話をするって、こんなに大変だったのね」"
"ついつい、グチが出てしまう。"


show char tre08f2
with dis



voice "Reo_0814"
re "「ぅぅっ……だめだめだめ、ワタシはあの子たちから見たら、大きなお姉さんなんだからっ」"


show char tre01f2
with dis



voice "Reo_0815"
re "「これくらいで、音をあげないもん……んっ、電話だ、えっ？　麻衣？」"
"今別れたばかりなのに、麻衣から電話がかかってきた。"
voice "Reo_0816"
re "「もしもし……ほんとに麻衣？」"


show char tma03p at left
show char tre01f2 at right as r
with dis



voice "Mai_0765"
ma "『あっ、玲緒？　もう家に着いた？』"
voice "Reo_0817"
re "「ええ、家よ。それがどうかしたの」"


show char tma01p at left
with dis



voice "Mai_0766"
ma "『あー……実は今週末って、連休じゃない？』"
voice "Reo_0818"
re "「うーん……」"
"ワタシは部屋の中のカレンダーを見る。"
"確かに、週末は連休になっている。"
"いつもならどこかに遊びに行くか、部屋でごろごろして過ごすけど。"
"今回はもちろん、麻衣の家で麻衣のお手伝いしないとね。"
voice "Reo_0819"
re "「大丈夫、ちゃんと麻衣の家に行くから！」"
voice "Mai_0767"
ma "『ありがとう。わたしは朝から、お母さんの病院に行って、色々やらないといけないことがあるのよ』"
"『色々』っていうのが何なのかは、わからないけれど……"
"麻衣の声は、とても真剣だった。"
"もしかして……検査とか手術とか、そういう重大なことなんじゃ……"
voice "Reo_0820"
re "「……うん、わかったわ！」"


show char tma03p at left
with dis



voice "Mai_0768"
ma "『玲緒？』"
voice "Reo_0821"
re "「ワタシにどーんと任せておいて！　麻衣はしっかりお母さんについてあげて」"


show char tma01p at left
with dis



voice "Mai_0769"
ma "『本当にいいの？　ありがとう玲緒。ごはんは一日分、ちゃんと作っておくから』"
voice "Reo_0822"
re "「ええ」"


show char tma02p at left
with dis



voice "Mai_0770"
ma "『ふふふっ、玲緒も本当に成長したわね』"


show char tre02f2 at right as r
with dis



voice "Reo_0823"
re "「当然よ。ワタシはあの子たちの、立派なお姉さんになるんだから」"
voice "Mai_0771"
ma "『そうね……玲緒の『お姉さんっぽい日々』が始まったんだもんね』"


show char tre01f2 at right as r
with dis



voice "Reo_0824"
re "「麻衣のお母さんが戻ってくるまで、しっかり続けるわ」"
voice "Mai_0772"
ma "『うん、頼りにしているわよ、お姉さん{image=image/exch001.png}』"


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


"こうして今週末は朝から、麻衣の家に行くことになったのだけれど……"


#**沢口家ダイニングキッチン
scene bg bg15a
with Dis



show char tre03f2
with dis



voice "Reo_0825"
re "「どーんと任せろなんて、言ったけど……ぅぅっ」"

#//SE：食器の音
#♀SE058
play sound "sound/SE058.ogg"


show char tre08f2
with dis



voice "Reo_0826"
re "「ちょっとアンタたち、なんでお茶碗ひっくり返すのよ」"


show char tre03f2
with dis



voice "Reo_0827"
re "「あーあ、こんなに食べ散らかして……もっときれいに食べなさいよ」"
"麻衣がいないせいか、お子さまたちは大暴れの大騒ぎ。"
"食事させるだけで、一苦労だった。"
voice "Mobmaibrz0003"
mao "「おまえがお茶碗ひっくりかえしたんだろう、あやまれよ」"
voice "Mobmaisis0003"
mai "「おにいちゃんが、押したからー」"
voice "Mobmaibrz0004"
mao "「ちがうよー」"
voice "Reo_0828"
re "「もう……いいから早く、残りを食べちゃいなさいよ」"
"ワタシだって、まだ全然食べてないんだから。"
"麻衣の作ってくれた、おおきなエビフライ。"
"冷めないうちに、早く食べちゃいたいんだから。"


show char tre01f2
with dis



voice "Reo_0829"
re "「いただきまぁ～す……あーん」"
voice "Mobmaibrz0005"
mao "「れおのそれ、いただきっ！」"


show char tre04f2
with dis



voice "Reo_0830"
re "「えっ……わぁぁっ！！」"
"横から小さな手が伸びてきて、エビフライが奪われて。"
"麻衣の弟は手づかみのまま、ワタシのおかずを食べてしまった。"
voice "Mobmaisis0004"
mai "「あっ、おにいちゃんずるーい」"
voice "Mobmaibrz0006"
mao "「へへーん、トロトロしてるのが悪いんだよ」"


show char tre03f2
with dis



voice "Reo_0831"
re "「わ、ワタシのエビフライ……くっ、うぅぅ……」"
"今日、お世話をしてくれるお礼ってことで、麻衣はわざわざワタシの好きなものを作っておいてくれたのに。"
voice "Mobmaibrz0007"
mao "「エビフライ、うめー♪」"
voice "Mobmaisis0005"
mai "「もー、おにいちゃん、ずるいずるいっ」"
"２人はさっきから何度も注意しているのに、テーブルの周りで追いかけっこを始めてしまった。"


show char tre09f2
with dis



voice "Reo_0832"
re "「う、うぅぅ、アンタたちぃ……むきぃ！！」"
"ワタシのイライラは最高潮に達していた。"
voice "Reo_0833"
re "「ばかぁぁぁ～、アンタたち、なんてことをしてくれるのよぉ！！」"
voice "Reo_0834"
re "「もう好きにしなさい、ごはんもなにも、ワタシ面倒みないわよ！！」"
"気がつくと、子供相手に大声で怒鳴りつけてしまった。"
voice "Mobmaisis0006"
mai "「ふぇ、ふぇぇぇ………………ふぇぇぇ～ん！！」"


show char tre03f2
with dis



voice "Reo_0835"
re "「ちょ、ちょっと、なんで泣くのよ、もう！」"
voice "Mobmaisis0007"
mai "「だって、だってぇ……ふぇぇぇ～、怒られたぁ、おにいちゃんのせいだぁ～」"
voice "Mobmaibrz0008"
mao "「うわぁぁん、ボク、ボク悪くないもん～」"
"２人はビクっと体を震わせながら、ワタシの怒り声に驚いて、泣き出してしまった。"
voice "Reo_0836"
re "「も、もう……泣かないでよ、もう……泣きたいのは、ワタシの方なんだからね……エビフライ……」"
"なんだか、もう……麻衣には悪いけど、この子たちの面倒をみるのがイヤになってきた。"


show char tre08f2
with dis



voice "Reo_0837"
re "「もう、さっさと泣き止みなさいよ。アンタたちが悪いんでしょう！」"
voice "Mobmaibrz0009"
mao "「ひっく、う、うるさい……ちびっ」"
voice "Reo_0838"
re "「ち、ちびって……失礼ね、アンタよりおっきいわよ！」"
voice "Mobmaibrz0010"
mao "「だってれおは、麻衣おねえちゃんよりぜんぜん、ちびじゃないか、お胸だってぺったんこだし」"
voice "Mobmaisis0008"
mai "「あっ、ほんとだ。れおちゃん、あたしとおんなじ、ぺったんこだね」"


show char tre03f2
with dis



voice "Reo_0839"
re "「うきゅゅ……コイツら、ワタシが気にしていることを」"
voice "Mobmaibrz0011"
mao "「なんだ、やるのか、れお？」"


show char tre09f2
with dis



voice "Reo_0840"
re "「の、のぞむところよっ！！」"


#allClear:
hide char tre09f2
#lastBG:
#scene bg bg15a
with dis


"ああ、もう……ちゃんと面倒みるっていったのに。"
"いつしかワタシは、子供相手に本気でケンカをしてしまったのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**麻衣の部屋・夜
scene bg bg14c
with Dis



#mes on
#system on


show char tre03f2
with dis



voice "Reo_0841"
re "「ああ……麻衣、遅いなぁー」"
"夕飯の後かたづけを終えて、ぶつぶつ文句を言いながらも、なんとかあの２人をお風呂に入れるまではできた。"
"お風呂に入る入りたくないで、また大ゲンカになっちゃったけど。"
"もう、いいや。"
"しっかりした、優しいお姉さんなんて、ワタシにはぜったい無理だもん。"
"やっぱりワタシは人の面倒をみるより、みてもらう方が楽で好きだわ。"


show char tre01f2
with dis



voice "Reo_0842"
re "「はやく、麻衣と会いたいなぁー」"
"明日も休みだし、少しくらい家に帰るのが遅くなってもいいわ。"


show char tre02f2
with dis



voice "Reo_0843"
re "「その分、帰ってきた麻衣と、たぁ～くさんおしゃべりしよう{image=image/exch001.png}」"

#//SE：携帯の音
#♀SE007
play sound "sound/SE007.ogg"


voice "Reo_0844"
re "「んっ、やっと麻衣から連絡ね♪　もうこっちに戻ってきてるのかな～……はい、もしもし！」"


show char tma01p at left
show char tre02f2 at right as r
with dis



voice "Mai_0773"
ma "『玲緒、そっちの様子はどうかしら？』"


show char tre01f2 at right as r
with dis



voice "Reo_0845"
re "「２人ともお風呂から出て、ジュース飲んでるところ。麻衣は、今どこなの？」"


show char tma03p at left
with dis



voice "Mai_0774"
ma "『実は……まだ、病院なのよ』"


show char tre04f2 at right as r
with dis



voice "Reo_0846"
re "「えぇっ！？」"
voice "Mai_0775"
ma "『今夜はなんか、帰れそうにないの。だから……玲緒、泊まっていって欲しいんだけど』"


show char tre03f2 at right as r
with dis



voice "Reo_0847"
re "「そ、そんなぁー」"
voice "Mai_0776"
ma "『お願いよ、玲緒……あの子たち２人だけにしてはおけないから』"
voice "Reo_0848"
re "「……うん、わかったわ」"
"そうよね、麻衣の言う通り……憎らしいけれど、あの２人だけ放っておくわけにはいかないもんね。"


show char tma01p at left
with dis



voice "Mai_0777"
ma "『ありがとう、本当に助かるわ。もし何かあったら、連絡ちょうだいね』"


show char tre01f2 at right as r
with dis



voice "Reo_0849"
re "「うん……それじゃあ麻衣、おやすみ」"
voice "Mai_0778"
ma "『おやすみ、玲緒……』"


hide char tma01p at left
with dis


#//SE：携帯の切れる音
#♀SE059
play sound "sound/SE059.ogg"


voice "Reo_0850"
re "「………………ふうー」"
"麻衣に言われたから、しぶしぶ泊まることにしたけれど。"
"麻衣が帰ってこないこと……あの子たちにうまく伝えられるかな。"


#allClear:
hide char tre01f2 at right as r
#lastBG:
#scene bg bg14c
show char tre03f2
with dis



voice "Reo_0851"
re "「もしまた、泣かれたりしたら……どうしよう」"
"それでも、言わないわけにはいかなくて。"
"ワタシは２人に、麻衣が今夜は病院に泊まることを伝えた……"


show char tre01f2
with dis



voice "Reo_0852"
re "「……ということなのよ。ワタシが泊まるけど、アンタたちはさっさと寝てちょうだいね」"
voice "Mobmaisis0009"
mai "「………………」"
voice "Mobmaibrz0012"
mao "「………………」"


show char tre03f2
with dis



voice "Reo_0853"
re "「ちょっと、わかったの？」"
voice "Mobmaibrz0013"
mao "「う……うん、わかった、れお……おやすみ」"
voice "Mobmaisis0010"
mai "「れおちゃん……」"
"不安そうな顔のまま、弟が妹の手をひいて、布団の中に入っていった。"
voice "Reo_0854"
re "「やれやれ、また泣かれたりするかと思ったけど……助かったわ」"


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


#**沢口家ダイニングキッチン・夜
scene bg bg15c
with Dis



#♂MP02
play music "sound/BGM02.ogg"


show char tre01f2
with dis


#mes on
#system on


voice "Reo_0855"
re "「……ふー、シャワーでやっと、さっぱりしたわ」"
"あの２人はもう寝てるだろうし、やっとのんびりできるわ。"


show char tre02f2
with dis



voice "Reo_0856"
re "「寝る前に、アイスくらい食べてもいいよね……んふふっ{image=image/exch001.png}」"
"お子さまたちに見つかるとちょーだいちょーだいうるさいから、今日はぜんぜんお菓子も食べてなかったのよね～"
voice "Reo_0857"
re "「ふふふっ、あったあった！　シャワーの後のアイスキャンディは、また格別……」"
"それを食べようとして、ふと部屋で寝ている２人のことが、気になった。"


show char tre03f2
with dis



voice "Reo_0858"
re "「もうちゃんと、寝ているわよね……」"
"さっきも『わかった』って言っていたし、問題はないはず……"


show char tre01f2
with dis



voice "Reo_0859"
re "「……うん、やっぱり一応、様子みてこようっと。麻衣に頼まれたんだもの……」"
"熟睡しているのを確認したら、あとでゆっくりアイス食べればいいのよ。"
voice "Reo_0860"
re "「別に、心配とかじゃなくて……これは義務、お姉さんとしての義務よ」"


#♂MS
stop music fadeout 1


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


#♂MP14
play music "sound/BGM14.ogg"


#mes on
#system on


"あの子たちの部屋の電気は、消えていたけれど。"
"話し声はボソボソと、聞こえていた。"
"どうやらまだ２人とも、起きているみたいだった。"
voice "Reo_0861"
re "「……んっ　これって……泣き声？」"
"すすり泣くような声が、かすかに聞こえてきた。"
voice "Mobmaibrz0014"
mao "「……な、泣くなよ……」"
voice "Mobmaisis0011"
mai "「うううっ……だって、だって……おかあさん、だいじょうぶなのかなぁ。だいじょうぶだよね、おにいちゃん」"
voice "Mobmaibrz0015"
mao "「そんなの、ボクだってわからないよぉ……ううううっ」"
voice "Mobmaisis0012"
mai "「なによぉ、おにいちゃんも泣いてるじゃない」"
voice "Mobmaibrz0016"
mao "「だって、おまえが変なこというから……ぅぅっ、ひっく……お母さん」"
voice "Reo_0862"
re "「アンタたち……」"
"やっぱりお母さんのこと、子供なりに不安になっていたんだ。"
"そんなことにワタシは、今更ながらに気がついた。"
voice "Reo_0863"
re "「もう、しょうがないわね……よいしょっと」"
"ワタシはパジャマに着替え、２人の間に寝転がった。"


#※EV075
scene bg EV75
with Dis



voice "Mobmaibrz0017"
mao "「なっ、なんだよ、れおっ！」"
voice "Reo_0864"
re "「別に……ワタシも一緒に、寝てあげるわ」"
voice "Mobmaibrz0018"
mao "「くるなよ、れお……はいってくんなっ！」"
"必死に涙を拭って、怒る麻衣の弟。"
"ワタシはそっと、その頭を撫でてやった。"
voice "Reo_0865"
re "「お母さんなら、大丈夫よ……麻衣がついてるんだもの」"
voice "Mobmaibrz0019"
mao "「れ、れお……うううっ、うわぁーん」"
voice "Mobmaisis0013"
mai "「ううううっ、おかあさん、だいじょうぶだよね、だいじょうぶだよね、れおちゃん」"
voice "Reo_0866"
re "「うん……大丈夫、だいじょうぶよ」"
"２人の頭を、そっと撫でて。"
"そして何度も『だいじょうぶ』と繰り返し言ってるうちに、いつしか２人は泣き止んでいた。"
voice "Reo_0867"
re "「あれっ……寝ちゃったわ、この子たち」"
"２人の、穏やかな寝顔。"
"さっきはあんなにも、憎らしかったのに。"
voice "Reo_0868"
re "「なんか……すっごく、可愛く見えるかも」"
"ワタシは初めて、子供が可愛いと思った。"


#※EV075P1
scene bg EV75p1
with Dis



voice "Reo_0869"
re "「ずっとこんな感じなら、いいのにね……ふぁ、ふわぁぁ～」"
voice "Reo_0870"
re "「うにゅ……ワタシも、もう……眠くなっちゃったぁ……」"
"今日は一日、子供たちの世話をしていたから、疲れもすっごくたまってて。"
"ワタシもそのまま、眠りに落ちていった。"


#**夜空
scene bg bg42c
with Dis



voice "Reo_0871"
re "「まいぃ……おやす……みぃ……」"


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
jump S117



