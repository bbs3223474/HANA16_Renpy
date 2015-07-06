#「秘密は、ヒミツのままで」

label S112:
$ save_name = "◇秘密は、ヒミツのままで"


#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


"こうして『黒髪会』の調査は、明日も続けて行われることになった。"
voice "Reo_0583"
re "「明日こそきっと、尻尾をつかんで……あっ、あれは！？」"
"綾瀬美夜……こんな時間にどうして、こんなところを……"
"気になったワタシは、後を追いかけて声をかけた。"


#**商店街・昼
scene bg bg16a
with Dis



show char tre08s2
with dis



voice "Reo_0584"
re "「ちょ、ちょっと綾瀬美夜っ！」"


show char tre08s2 at left
show char tmi03s2 at right as r
with dis



voice "Miya_1113"
m "「あっ、玲緒、さま……ごきげんよう」"
"何か様子がおかしいような、ボーッとしているような……"


show char tre03s2 at left
with dis



voice "Reo_0585"
re "「アンタ結局、調査の方、どうなったのよ？」"
voice "Miya_1114"
m "「調査、って……一体、何の事でしょうか？」"


show char tre07s2 at left
with dis



voice "Reo_0586"
re "「ちょっと、とぼけないで！　『黒髪会』のことよっ！！」"
voice "Miya_1115"
m "「ああ、はい。『黒髪会』の事は……結局、何もわからなかったんです。ゴメンなさい」"


show char tre03s2 at left
with dis



voice "Reo_0587"
re "「えっ……何も？」"
voice "Miya_1116"
m "「ええ、何も」"
"そんなぁ～。"
"あれだけ、自信ありげだったくせに。"
voice "Reo_0588"
re "「もぉ……綾瀬美夜も案外、大したことないのね」"


show char tmi02s2 at right as r
with dis



voice "Miya_1117"
m "「ふふふっ」"
voice "Reo_0589"
re "「？？？」"
"ちょっと、なんでそこで笑うのよ。"


show char tmi01s2 at right as r
with dis



voice "Miya_1118"
m "「先輩のご期待に添えず、本当に申し訳ありません。『黒髪会』はかなり、謎の組織のようですね」"
voice "Reo_0590"
re "「うぅっ……なによぉ、すごく気になる、気になるぅ」"


show char tmi02s2 at right as r
with dis



voice "Miya_1119"
m "「………………ニヤリ」"
voice "Reo_0591"
re "「えっ？」"


show char tmi01s2 at right as r
with dis



voice "Miya_1120"
m "「それでは、わたくし……失礼いたします」"


hide char tmi01s2 at right as r
with dis


voice "Reo_0592"
re "「ちょ、ちょっと、待ちなさいよぉ～」"
"いつの間にか、綾瀬美夜はいなくなっていた。"


show char tre09s2
with dis



voice "Reo_0593"
re "「う、うぅぅっ……ワタシは、諦めない……絶対に秘密、暴いてみせるわっ！！」"


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


"でも……捜査を続けて、３日目。"
"ワタシはある決断を下すことにした。"


#**委員会室・昼
scene bg bg30a
with Dis



show char tre01s2
with dis



voice "Reo_0594"
re "「みんな、この３日間、本当にありがとう……尽力に感謝するわ」"


show char tna03s2
with dis



voice "Nanami1205"
n "「ほ、本当に……疲れた……はぁ～」"


#allClear:
hide char tna03s2
#lastBG:
#scene bg bg30a
with dis


"みんな、本当に憔悴していた。"
"よくやってくれた…………そんなみんなに、ワタシはハッキリと告げた。"


show char tre08s2
with dis



voice "Reo_0595"
re "「『黒髪会』の捜査本部は……本日をもって、解散よ！！」"
"………………"
voice "Reo_0596"
re "「アンタたちが納得いかないのはわかるけれど、これ以上の調査は飽きた……っていうか、ムダなのよ。それほどまで『黒髪会』の存在は謎なのよ」"
voice "Reo_0597"
re "「無念とは思う、でも……捜査はこれで終わりよっ！！」"
"次の瞬間、みんなの悔し泣きが教室に響いた……ワケではなく、安堵のため息がもれた。"


show char tru01s2
with dis



voice "Runa_0136"
rn "「やれやれ、やっと探偵ごっこも終わったわね～」"


show char trk01s2
with dis



voice "Rikka_1640"
rk "「玲緒さま、お疲れ様でした。ワタシ、明日からは陸上部の練習に戻ります」"


show char tre01s2
with dis



voice "Reo_0598"
re "「コホン。今日、これからワタシの部屋で『捜査本部解散パーティ』やるから。お菓子やジュース、デパ地下グルメもたくさんあるわよ。大いに盛り上がって」"
voice "Moball_0004"
a "「はーいっ！！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**玲緒の部屋
scene bg bg33a
with Dis



show char tma04s2
with dis


#mes on
#system on


voice "Mai_0632"
ma "「ただいま～……って、何よ、この部屋は！？」"


show char tma04s2 at left
show char tre02s2 at right as r
with dis



voice "Reo_0599"
re "「麻衣、おかえり～♪　みんなでね、打ち上げやってたんだ～」"


show char tma03s2 at left
with dis



voice "Mai_0633"
ma "「そ、そう……ビックリしたわ。これ、玲緒が一人で全部、食べ散らかしたかと思ったわよ」"


show char tre08s2 at right as r
with dis



voice "Reo_0600"
re "「そんなわけないでしょ！　それより聞いてよ、麻衣。ワタシね、みんなと一緒にくろか──とある組織の秘密を暴こうって、捜査本部を作ったの」"
voice "Mai_0634"
ma "「えっ……そ、そんなことを……それで、何か……わかったの？」"


show char tre01s2 at right as r
with dis



voice "Reo_0601"
re "「ううん、全然わかんない。だからもー、疲れちゃって……捜査はやめたわ」"


show char tma01s2 at left
with dis



voice "Mai_0635"
ma "「そう、なんだ……お疲れ様」"


show char tre02s2 at right as r
with dis



voice "Reo_0602"
re "「でもねでもね、すごく疲れたけど、すっごく楽しかった♪　みんなワタシの為に頑張ってくれたし……」"
voice "Mai_0636"
ma "「………………」"
"……その後、ワタシはこの３日間の武勇伝を、麻衣に聞かせてあげた。"
"麻衣は最初ニコニコしながら、話を聞いてくれていたけれど……だんだん、つまらなそうな顔になっていった。"


show char tre03s2 at right as r
with dis



voice "Reo_0603"
re "「麻衣……ワタシの話、面白くない？」"


show char tma02s2 at left
with dis



voice "Mai_0637"
ma "「ううん、面白いわよ……っていうか、本当に楽しかったのね、玲緒」"


show char tre02s2 at right as r
with dis



voice "Reo_0604"
re "「うん、楽しかった♪」"


show char tma01s2 at left
with dis



voice "Mai_0638"
ma "「みんなとも、仲良くなったみたいだし……」"


show char tre01s2 at right as r
with dis



voice "Reo_0605"
re "「そう、かもね。みんなこのワタシの人望に惹かれて、一生懸命捜査してくれたわ」"


show char tma03s2 at left
with dis



voice "Mai_0639"
ma "「……ただ、庇護欲で放っておけなかっただけじゃないかしら……」"


show char tre03s2 at right as r
with dis



voice "Reo_0606"
re "「なんか言った、麻衣？」"


show char tma01s2 at left
with dis



voice "Mai_0640"
ma "「ううん、なーんにも。でも玲緒、みんなとそんなに楽しいことしていたのに……どうしてわたしは、誘ってくれなかったの？」"


show char tre04s2 at right as r
with dis



voice "Reo_0607"
re "「えっ！？　そ、それは……」"
"麻衣が『黒髪会』の一員だと思っていたから……なんて言ったら、怒るかな……？"


show char tma03s2 at left
with dis



voice "Mai_0641"
ma "「あの『黒髪パーティ』のお返しで、わたしを仲間はずれにしたの、玲緒？」"


show char tre03s2 at right as r
with dis



voice "Reo_0608"
re "「そ、そんなつもりじゃ……ワタシは……」"
voice "Mai_0642"
ma "「みんなとばっかり、仲良くしちゃって……わたしとは遊んでくれないのね、玲緒は」"


show char tre04s2 at right as r
with dis



voice "Reo_0609"
re "「そんな、そんなことないもん！　ワタシが一番、一緒に遊びたいのは、麻衣……だから……」"
voice "Mai_0643"
ma "「ほんと？　本当にそう思っている！？」"


show char tre05s2 at right as r
with dis



voice "Reo_0610"
re "「うん、本当に……思ってる、わよ……」"


show char tma02s2 at left
with dis



voice "Mai_0644"
ma "「そう、だったら……わたしと遊びましょう♪」"


show char tre01s2 at right as r
with dis



voice "Reo_0611"
re "「うん、いいけど……どんな遊び？」"
voice "Mai_0645"
ma "「それはね……玲緒がわたしを、エッチに可愛がってイカせてくれる遊び{image=image/exch001.png}」"


show char tre09s2 at right as r
with dis



voice "Reo_0612"
re "「ワ、ワタシからって、麻衣のエロス～～～！！」"


show char tma03s2 at left
with dis



voice "Mai_0646"
ma "「イヤなの？　みんなとは打ち上げパーティするほど仲良しになったのに、わたしとは仲良しエッチしてくれないの？」"


show char tre03s2 at right as r
with dis



voice "Reo_0613"
re "「だから、それとこれとは……」"
voice "Mai_0647"
ma "「するの……しない、の？」"
"瞳をうるうるさせて、どこか泣きそうな麻衣。"
"そんな麻衣に、ワタシもいつしかドキドキしちゃって……"


show char tre05s2 at right as r
with dis



voice "Reo_0614"
re "「わ、わかったわよ……」"
"こうしてワタシは、いきなりエロスに突入することになってしまった……"


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

"以下内容可能会导致部分人的不适，是否跳过？"
menu:
 "是":
  jump reo2
 "否":
  jump hscene_reo2

label hscene_reo2:


#※EV071
scene bg EV71
with Dis


#mes on
#system on


#♂MP11
play music "sound/BGM11.ogg"


voice "Reo_0615"
re "「ま、麻衣……ちゅっ{image=image/exch001.png}」"
"麻衣を押し倒すというより、ワタシが覆いかぶさるようにして、キスをした。"
"でも……なんか自分からのキスって、とっても恥ずかしい。"
voice "Mai_0648"
ma "「ん……玲緒……んっ、ちゅっ」"
voice "Reo_0616"
re "「ん、ふ……ちゅっ……ああ、麻衣……ちゅ{image=image/exch001.png}」"
"いつも麻衣がしてくれるようなキスを、真似してみる。"
"ちろっと舌を入れて、麻衣の口腔をかきまわす……ああ、にゅるにゅるであったかい。"
voice "Mai_0649"
ma "「あん、あんっ……玲緒のキス、すごいわ……はぁ{image=image/exch001.png}」"
"麻衣のその言葉が、なんか嬉しくて。"
"今度はキスをしながら、麻衣の胸元に手を伸ばしてみた。"
"少しだけ制服をはだけさせて、ワタシとは違う大きい膨らみに触ってみる。"
voice "Reo_0617"
re "「んっ……麻衣のおっぱい、とっても柔らか……」"
voice "Mai_0650"
ma "「あっ、はぅん……気持ち良いわ、玲緒……くぅん{image=image/exch001.png}」"
voice "Reo_0618"
re "「麻衣の乳首……なんかもう、コリコリしてる……」"
voice "Mai_0651"
ma "「だって、玲緒に……愛しい玲緒に押し倒されてると思うと、すっごく感じちゃうの……ぁぁ{image=image/exch001.png}」"
voice "Reo_0619"
re "「そ、そうなの……？」"
voice "Mai_0652"
ma "「ええ、そうよ。だからもっと、キスをちょうだい、玲緒{image=image/exch001.png}」"
voice "Reo_0620"
re "「う、うん、わかった……ちゅ、ちゅっ……んん」"
voice "Mai_0653"
ma "「ん、ふ……ぁぁう……ちゅ、れろ……玲緒、いいよぉ、もっといっぱい触ってぇ」"
voice "Reo_0621"
re "「んっ……でも、麻衣とキスしてると……あぁん、ワタシも何か、変になっちゃう」"
"ワタシのキスや胸への愛撫で、麻衣が感じてくれると思うと。"
"すっごくドキドキして、体中が熱くなってきて。"
"なんか、ガマンできなくなりそう……"
voice "Mai_0654"
ma "「いいわよ……おかしくなって。頭の中、わたしでいっぱいになって、玲緒……あんっ、んあああっ{image=image/exch001.png}」"
voice "Mai_0655"
ma "「すごいの、玲緒のちっちゃい指が、わたしのおっぱいをもみもみ揉んでいるわ……んふぅ、すごく気持ちいいの」"
voice "Reo_0622"
re "「麻衣のおっぱい……すごい、ふわふわしてる……」"
voice "Mai_0656"
ma "「ひぁ……んっ、ちゅう……ちゅるる、キスも……もっと{image=image/exch001.png}」"
voice "Reo_0623"
re "「んっ、ちゅう……{image=image/exch001.png}　ちゅぱ、れろっ」"
"舌と唇を絡めるようなキスをすると、麻衣の体がびくびく震えだした。"
voice "Mai_0657"
ma "「きっ、キスだけなのに……ああん、体がとろけちゃう……あっ、んっ{image=image/exch001.png}」"


#※EV071P1
scene bg EV71p1
with Dis



voice "Mai_0658"
ma "「あああっ、だめぇ、イクぅぅ……ひゃっ、ひぁぁうんっ{image=image/exch001.png}」"
voice "Reo_0624"
re "「う、ウソ……麻衣、キスだけでイッちゃったの？　本当に？？」"
"ビックリして麻衣を見ると、そこにはうっとりとワタシを見つめる、うるうるした瞳があった。"


#※EV071P2
scene bg EV71p2
with Dis


voice "Mai_0659"
ma "「はぁ、はぁ……ありがとう、玲緒……玲緒のエッチなキス、すごくドキドキしちゃった{image=image/exch001.png}」"
voice "Reo_0625"
re "「そ、そう……なの……」"
"なんか……一生懸命やってみて、良かったかも。"
"エッチで麻衣に誉められるなんて、なかなかない事だもん。"
voice "Mai_0660"
ma "「たどたどしくも、イヤらしく舌を絡ませる、玲緒の姿……あれはもう、たまらないわ」"
voice "Reo_0626"
re "「やっ、やだぁ……恥ずかしいこと言わないでよ、麻衣っ」"
voice "Mai_0661"
ma "「なんで？　だってわたしを気持ちよくさせようとして、頑張ってくれたんでしょう、玲緒は？」"
voice "Reo_0627"
re "「そそっ、それは……」"
"それは、そう……だけど。"
"なんかいちいち、麻衣の言い方はイヤらしい。"
"とゆーより、エロスよ、エロスっ！"
"でも……"
voice "Reo_0628"
re "「でもでも、これだけで終わりじゃないんだからね、麻衣っ！！」"
voice "Mai_0662"
ma "「えぇぇっ？　ちょ、ちょっと玲緒！？」"


#※EV072
scene bg EV72
with Dis



"ワタシはベッドから下りて制服を脱ぎ、裸になる。"
"同じく麻衣の服も脱がせちゃって。"
"その片脚をつかみ、ぐいっと高く持ち上げた。"
"そしてそのまま、麻衣の濡れているおまんこに、ワタシのおまんこをグイッと押しつけた。"
voice "Reo_0629"
re "（あっ、くちゅっとエッチな音……ワタシも麻衣とエッチしてて、濡れちゃっていたんだわ……くぅ、恥ずかしい……）"
voice "Mai_0663"
ma "「はぁ、はぁ……ちょっと玲緒、今日のあなた……なんかすごくない？　かなりエロスじゃない？」"
voice "Reo_0630"
re "「いちいち『エロス』言わないで、もう……エッチしてるんだもん、エロスでふつーなのよっ！！」"
"もっともっと、麻衣を感じさせて、もっともっと麻衣と繋がるんだから。"
"そして『気持ちよかったわ』って、言ってもらうんだから。"
voice "Mai_0664"
ma "「あっ、あんっ……玲緒のおまんこも、すごいわ……すっごく熱くなっているの」"
voice "Reo_0631"
re "「だったら、麻衣のだってドロドロのぐちゅぐちゅじゃない」"
"ワタシと麻衣の割れ目をぴったりとくっつける度に、なんかイヤらしい音が聞こえてきちゃう。"
"でも麻衣、ワタシのキスと愛撫で、こんなに濡れちゃっていたんだ……なんか嬉しいっていうか、ゾクゾクしちゃうっていうか。"
"いつもとは逆の立場になって、麻衣を責めているんだと思うと、なんだかとっても不思議な気分だった。"
voice "Reo_0632"
re "「はぁ、はぁ……いつも麻衣は、こんな気持ちで……ワタシと、エッチしてたの？」"
voice "Mai_0665"
ma "「えっ……？　玲緒、今なんて……？」"
voice "Reo_0633"
re "「な、なんでもないわよっ」"
"どうしてかな？"
"なんだかすごく、興奮してきちゃった。"
"もっといっぱい、麻衣とエッチなこと……してみたい。"
"そしてまた、麻衣を気持ち良くして。"
"さっきよりもっと激しく、イカせてあげたいって思っちゃう。"
"麻衣が好きだから……だーい好きだから{image=image/exch001.png}"
voice "Reo_0634"
re "「ま、麻衣……やっ、あうっ、んふっ、ああっ{image=image/exch001.png}」"


#※EV072P1
scene bg EV72p1
with Dis



voice "Mai_0666"
ma "「ぁんぁん、玲緒の腰の動き、なんかすごいわ……あぁ、感じるの、とっても気持ちいいよぉ{image=image/exch001.png}」"
voice "Reo_0635"
re "「ワ、ワタシも……いいっ{image=image/exch001.png}　あっ、そこ、すごくいい……あん、気持ちいいいのぉ{image=image/exch001.png}」"
voice "Mai_0667"
ma "「ふふふっ……なんかこれじゃ、どっちが責めているのかわからないわね」"
voice "Reo_0636"
re "「んっ、あっ、あっ……だめぇ、おかしくなりそう……ううううっ」"
"麻衣の言葉も耳に入らないくらい、ワタシは感じていた。"
"こっちが責めていたつもりなのに、今じゃお互いに……ううん、どっちかと言えば、ワタシが麻衣に責められているみたい。"
voice "Reo_0637a"
re "「ちょっと麻衣、だめぇ、ワタシが動くの、麻衣は動いちゃだめーっ」"
voice "Mai_0668"
ma "「はぁ、はぁ……どうしてよ？　一緒に動いたほうが、気持ちいいでしょ？」"
voice "Reo_0638"
re "「だって……だって今日は、ワタシが麻衣を気持ち良くしてあげるんだもんっ」"
voice "Mai_0669"
ma "「もう……可愛いこと言ってくれるのね、玲緒。キュンときちゃった……ちゅっ{image=image/exch001.png}」"
"ワタシに軽いキスをしてから、麻衣はチロッと赤い舌を出した。"
voice "Mai_0670"
ma "「でも………………だーめ、わたしも動いちゃうんだから」"
voice "Reo_0639"
re "「なんで、どーしてよぉ！？」"
voice "Mai_0671"
ma "「だって……わたしだってもう、気持ちよすぎて我慢できないのぉ{image=image/exch001.png}　ああ、あぁんっ{image=image/exch001.png}」"
voice "Reo_0640"
re "「ひゃうぅっ、激しいの、激しすぎよぉ、まーいーっ{image=image/exch001.png}{image=image/exch001.png}」"
"お互いの腰の動きは、どんどん激しくなっていって。"
"２人で動く分、快感も２倍、ううん、何倍も高まっちゃう。"
voice "Reo_0641"
re "「んっ、やっ、はぁぁっ……麻衣っ、すっごい気持ちいいよぉ……はうん」"
voice "Mai_0672"
ma "「玲緒、わたしだってすごいわ、こんなに濡れちゃうなんて……あんっ、んあぁぁっ{image=image/exch001.png}」"
"２人で夢中になって、擦り上げる。"
"濡れまくって、気持ち良すぎて……もう、限界。"


#※EV072P2
scene bg EV72p2
with Dis



voice "Reo_0642"
re "「麻衣、ワタシ、もう……いっぱい感じちゃって、ああん、ああああんっ{image=image/exch001.png}{image=image/exch001.png}」"
voice "Mai_0673"
ma "「ふあっ、玲緒、わたしもよ、またイクぅぅっ、イクぅぅん……んうううううっ{image=image/exch001.png}{image=image/exch001.png}」"
"そして……ワタシと麻衣は、一緒にイッちゃったのでした。"
voice "Reo_0643"
re "「あふ、あふぅん……すごいのぉ、麻衣ぃ……すっごく、気持ちよくって……あぁ、ぷしゅぅぅ……」"
voice "Mai_0674"
ma "「はぁ、はぁ……今日の玲緒、とってもエッチに頑張ったわね……ありがとう{image=image/exch001.png}　んふふっ」"
"麻衣は本当に、嬉しそうに笑ってくれた。"
"よかった……もうスネてないよね、麻衣。"


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


#endscene
#setscene 17
label reo2:

#**並木道・昼
scene bg bg18a
with dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


show char tma01s2
with dis



voice "Mai_0675"
ma "「ほらほら玲緒、そんなにゆっくり歩いていると、遅刻するわよ」"


show char tma01s2 at left
show char tre03s2 at right as r
with dis



voice "Reo_0644"
re "「うううっ、麻衣、ワタシ捜査で疲れて筋肉痛だから、休みたい……」"
voice "Mai_0676"
ma "「ダメよ、歩いた歩いた～」"
voice "Reo_0645"
re "「もう麻衣、押さないでよぉ～、ちゃんと歩くから」"

#//SE：メール着信音
#♀SE012
play sound "sound/SE012.ogg"


voice "Reo_0646"
re "「うぅっ、こんなタイミングで、誰よ……エリス？」"
"エリスからきたメールを、ワタシはその場で読み上げた。"
voice "Reo_0647"
re "「玲緒へ。例の『黒髪会』のこと、またネットで調べたら、最近メンバーが増えたらしいよ……と」"
voice "Reo_0648"
re "「でもでも、詳しくはわからなかったよ。このまま増殖を続けるのかな……かっこ笑い、だって」"


show char tre09s2 at right as r
with dis



voice "Reo_0649"
re "「んもぉ～、何がかっこ笑い、よ！　もうエリスったらっ！」"
"こんなの、もうどうでもいい情報だわ。"
"メンバーが増えようが減ろうが、もうワタシには『黒髪会』なんて、関係ないから。"


show char tre03s2 at right as r
with dis



voice "Reo_0650"
re "「とにかく、今日は……ああ、休みたい」"
voice "Mai_0677"
ma "「ダメだったら、玲緒。今日も放課後は、委員会が……ん？」"
"麻衣の背中を押す手が、急に緩む。"
"どうしたのかしら？"

hide char tma01s2 at left
hide char tre03s2 at right as r
show char tmi01s2 at sleft as l
show char tma01s2
show char tre03s2 at sright as sr
with dis



voice "Miya_1121"
m "「麻衣さま……ごきげんよう」"
voice "Mai_0678"
ma "「美夜ちゃん、ごきげんよう」"
voice "Reo_0651"
re "「綾瀬……美夜……」"
"綾瀬美夜の方から、麻衣に挨拶するなんて。"
"これ、なんだか怪しいわ。"


show char tmi02s2 at sleft as l
with dis



voice "Miya_1122"
m "「ふふふっ{image=image/exch001.png}」"


show char tma02s2
with dis



voice "Mai_0679"
ma "「ふふふっ{image=image/exch001.png}」"


#allClear:
hide char tmi02s2 at sleft as l
hide char tma02s2
hide char tre03s2 at sright as sr
#lastBG:
#scene bg bg18a
show char tre03s2
with dis



voice "Reo_0652"
re "「んんっ？？？」"
"２人ともすれ違いざま、小さくにやりと笑った……ように見えた。"
"ううん、確かに笑ったわ、気のせいじゃない！！"
voice "Reo_0653"
re "「な、なに？　２人の間に、一体なにが？？」"
voice "Reo_0654"
re "「ああ……なんか、気になるよぉ」"


show char tma01s2 at left
show char tre03s2 at right as r
with dis



voice "Mai_0680"
ma "「ほーら玲緒、教室行くわよ～」"
"今度は腕を取られて、そのままひきずるように、教室まで連れて行かれたのだった。"
voice "Reo_0655"
re "「もう……またみんなを集めて、今度は麻衣と綾瀬美夜の素行調査でもしようかしら……」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//※以下『黒髪会』の秘密パート

#※美夜視点で

#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


show char tmi03s2
with dis



voice "Miya_1123"
m "「玲緒さま……申し訳ありません、何も教えてあげられなくて」"
"実はわたくし……たどりついていたのです、『黒髪会』の秘密に。"
"あの時………………"


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



#※CU19
show char CU19
with dis



#mes on
#system on


voice "Sizuku0162"
sk "「知ったからには、もう…………このままでは済ませませんわね、５０代目」"
voice "Mai_0681"
ma "「そうですね……４９代目、ふふっ、ふふふっ」"
voice "Miya_1124"
m "「やっ、やぁぁ、わたくし……消されてしまう……ぅぅっ」"
voice "Sizuku0163"
sk "「知ったからには……仲間、ね」"
voice "Mai_0682"
ma "「ええ、そうね♪」"
voice "Miya_1125"
m "「………………へっ！？」"
"わたくしの両肩に手を置いて、にっこりと微笑む麻衣さま。"
"もしかして、このわたくしを『黒髪会』に引き入れて、秘密を守らせようって魂胆なの？"
voice "Mai_0683"
ma "「新会員が増えて嬉しいですね、雫さま{image=image/exch001.png}」"
voice "Sizuku0164"
sk "「ええ{image=image/exch001.png}」"
voice "Miya_1126"
m "「い、いえ……わたくしが、先輩お２人の仲間になるなんて……」"
voice "Mai_0684"
ma "「そんなの、気にしなくていいわよ」"
voice "Sizuku0165"
sk "「年齢関係なく、美夜さんはとても綺麗な黒髪の持ち主なんですから」"
"２人に詰め寄られて……これはもう、断れそうにない。"
voice "Miya_1127"
m "「は、はい……」"
voice "Mai_0685"
ma "「ではこの件は、３人だけの秘密って事で……ね、ふふふっ」"
voice "Sizuku0166"
sk "「ふふふっ」"
voice "Mai_0686"
ma "「ちなみに現会長は、５０代目のわたし。前の会長は……」"
voice "Sizuku0167"
sk "「４９代目のわたくしです。黒髪美しい美夜さんにはいずれ、５１代目の会長になっていただけたら……嬉しいわ」"
voice "Miya_1128"
m "「ご、５１代目……ですか……」"
"結構、長く続いているのね……"
voice "Mai_0687"
ma "「美夜ちゃん、これからよろしくね」"
voice "Sizuku0168"
sk "「よろしくお願いします。たまに定例会もありますので」"
voice "Miya_1129"
m "「は、はい……」"
"何だかわからないうちに、わたくしもその『黒髪会』に入ることになってしまった。"


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


"こうしてわたくしは、おかしなことに巻き込まれたのだった……"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


show char tma03s2
with dis



voice "Mai_0688"
ma "「だから、なんでもないったら～」"


show char tma03s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0656"
re "「怪しい……麻衣と綾瀬美夜、さっき『ふふっ{image=image/exch001.png}』って笑い合って……関係怪しすぎよっ」"


#allClear:
hide char tma03s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg18a
show char tmi02s2
with dis



voice "Miya_1130"
m "「まだ、ケンカしているわ……ふふ」"
"そんな先輩２人の背中を見ながら、わたくしはまた小さく微笑んだ。"


show char tmi01s2
with dis



voice "Miya_1131"
m "「でも……なんか、悪くないわね……こういうの」"
"初めての、グループ所属だし。"
"この２人なら、そんなに騒がしくもないから、良いかもしれないわ。"
"それに『黒髪会』。"
"ミカ女一、黒髪が美しいわたくしにふさわしいグループ名。"
"その５１代目会長になるという事は……わたくしこそがミカ女黒髪キャラの頂点となったも同じだもの。"


show char tmi02s2
with dis



voice "Miya_1132"
m "「璃紗……喜んで、これで名実共に、貴女の恋人の髪は世界一よ{image=image/exch001.png}　んふ、んふふっ{image=image/exch001.png}」"


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



#//※※自動分岐
#//玲緒＆麻衣ルートに入ってからの選択肢（１）～（３）で
#//２つ以上○を選んでいれば、S113にジャンプ
#//それ以外なら、下記の『途中ＥＮＤ』へ。
#if f1<2 badend

$ _skipping = False
$ _dismiss_pause = False
#log off

scene image "image/eyecatch05.png"
with vs

pause 3

scene black
with Dis

#log on
$ _skipping = True
$ _dismiss_pause = True

jump S113



