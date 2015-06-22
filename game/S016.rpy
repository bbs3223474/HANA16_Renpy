#「夏休み突入」

label S016:
$ save_name = "◇夏休み突入"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP18
play music "sound/BGM18.ogg"


voice "mobJyosiA0043"
mobA "「璃紗さん、ごきげんよう」"


show char tri02s2
with dis



voice "Risa_0467"
r "「ええ、ごきげんよう」"
voice "mobJyosiA0044"
mobA "「夏のバカンスの予定、お決まりですか？」"


show char tri03s2
with dis



voice "Risa_0468"
r "「バ、バカンスねぇ。えっと……多分講習は、行くかしら」"
voice "mobJyosiA0045"
mobA "「まぁ、璃紗さんも休みの間は、家で勉学に励まれるんですね？」"
voice "Risa_0469"
r "「まぁ、そうね……」"
"１００％、そうとは言いきれないけれど。"
voice "mobJyosiA0046"
mobA "「よかったら、ウチの別荘に来ませんか？　涼しくて勉強もはかどりますわよ」"
voice "Risa_0470"
r "「それって……もちろん海外ですよね」"
voice "mobJyosiA0047"
mobA "「ええ、もちろん{image=image/exch001.png}」"
voice "Risa_0471"
r "「あははははっ……」"
"海外の別荘持ちなところをサラッと言えちゃうところが、お嬢様なのよね。"
"明日から夏休みということで、こんな誘いをいくつか受けたけれど、私は適当に受け流していた。"
voice "Risa_0472"
r "「ちょっと駅前までみたいに、みんな誘ってくるんだもの……とまどってしまうわ」"
"声をかけてきたクラスメイトと別れ、校門の方へ歩いて行くと。"
"そこはちょっとした騒ぎになっていた。"


#allClear:
hide char tri03s2
#lastBG:
#scene bg bg18a
with dis


voice "mobJyosiB0030"
mobB "「六夏さん、夏休みは是非わたくしと一緒に」"
voice "mobJyosiC0013"
mobC "「いいえ、私の別荘へ。近くに陸上競技場もありますので」"
voice "mobJyosiA0048"
mobA "「ウチだって、スポーツジム完備ですわ」"


show char trk03s2
with dis



voice "Rikka_0303"
rk "「あ、ありがとうございます。でも夏休み中は、クラブの合宿もありますし……」"
"ファンの子たちに囲まれているのは、六夏だった。"
"私と同じように、こっちもお誘いがたくさんみたい。"


show char tri01s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0473"
r "「六夏、ごきげんよう」"


show char trk01s2 at right as r
with dis



voice "Rikka_0304"
rk "「あっ、リサ姉～」"
"ホッとしたように、六夏がこっちに来る。"
"先輩に呼ばれたとあっては、しつこく追いかけ回すわけにもいかず。"
"彼女たちはその場から撤退していった。"
voice "Risa_0474"
r "「相変わらず、大変そうね」"


show char trk03s2 at right as r
with dis



voice "Rikka_0305"
rk "「うん。誘ってくれるのは嬉しいけど、何だか息がつまりそうで……」"
voice "Risa_0475"
r "「わかるわ、それより陸上部の合宿、参加するの？」"


show char trk01s2 at right as r
with dis



voice "Rikka_0306"
rk "「あれは……その場のウソ。ミカ女の体育系の部活って、それほど熱心な活動はしてないし」"
voice "Risa_0476"
r "「……そうよね」"
"仮にあったとしても……"
"避暑地でのんびりお茶の休憩を挟みながら、まったりしてそうなイメージだわ。"
voice "Rikka_0307"
rk "「夏休みは、自主トレをするつもりだけど……」"
voice "Risa_0477"
r "「頑張ってね。明日からしばらく、会えなくなるけど」"


show char trk03s2 at right as r
with dis



voice "Rikka_0308"
rk "「あっ、そうか……ここのところリサ姉とずっと一緒だったから、寂しいなぁ……」"
"本気で寂しそうな六夏は、瞳を潤ませて私を見つめた。"
voice "Rikka_0309"
rk "「リサ姉、夏休み中、家に遊びに行っても……いい？」"


show char tri03s2 at left
with dis



voice "Risa_0478"
r "「う、ウチに……来たいの？」"
"ツツっと、冷や汗が流れる。"
"昔住んでた家には、六夏はよく遊びに来てたけど。"
"あの時と今とは、事情が違うのよね……"
voice "Risa_0479"
r "「わ、私の方が、六夏の家に行くわよ」"
voice "Rikka_0310"
rk "「えっ、ワタシの部屋に？　別にかまわないけど……」"
"『どうしてダメなの？』とでも、聞きたげな表情だった。"
"私はすかさず、話題を切りかえる。"


show char tri08s2 at left
with dis



voice "Risa_0480"
r "「そ、それとね、六夏……文化祭は、告白のチャンスよ」"
voice "Rikka_0311"
rk "「えっ？」"
voice "Risa_0481"
r "「だからね、夏休みの間に心身をよーく、鍛えておくように」"
voice "Rikka_0312"
rk "「告白の……チャンス……」"

hide char tri08s2 at left
hide char trk03s2 at right as r
show char tsa02s2 at sleft as l
show char tri08s2
show char trk03s2 at sright as sr
with dis



voice "Sara_0064"
sr "「そうそう、その通り～、璃紗ちゃん良いこと言うね～！」"


show char tri03s2
with dis



voice "Risa_0482"
r "「紗良さん？」"
"後ろからいきなり、紗良さんがやってきた。"
"もちろん、楓さまも一緒に。"
voice "Sara_0065"
sr "「文化祭の準備で一緒にいる時間は増えるし、そこで親密度をアップさせて当日告白……いい流れだよ～」"
voice "Rikka_0313"
rk "「で、でも……」"
voice "Sara_0066"
sr "「大丈夫だよ。ねっ、楓ちゃん」"


show char tka01s2 at sleft as l
show char tsa02s2
show char trk03s2 at sright as sr
with dis



voice "Kaede_0045"
k "「一緒に何かを作り上げていくうちに、仲良くなれると思うわ。だから六夏さん、頑張って」"
"先輩２人に応援されて、六夏はうんうん頷いた。"


#allClear:
hide char tka01s2 at sleft as l
hide char tsa02s2
hide char trk03s2 at sright as sr
#lastBG:
#scene bg bg18a
show char tsa01s2 at left
show char tri01s2 at right as r
with dis



voice "Sara_0067"
sr "「でね、璃紗ちゃん」"
"紗良さんが、耳元で囁く。"


show char tsa03s2 at left
with dis



voice "Sara_0068"
sr "「紗良と楓ちゃんは、仕事が忙しい時はあまり、お手伝いいけないと思うの」"
voice "Risa_0483"
r "「その辺なら……私たちがしっかり、お二人の分まで頑張ります」"


show char tsa01s2 at left
with dis



voice "Sara_0069"
sr "「璃紗ちゃん、マジメだね……でも、そうじゃなくて」"


show char tri03s2 at right as r
with dis



voice "Risa_0484"
r "「？？？」"


show char tsa02s2 at left
with dis



voice "Sara_0070"
sr "「六夏ちゃんと沙雪ちゃんの間に何かあったら、すぐにメールで教えてね♪」"
"そういうことね。"


show char tri01s2 at right as r
with dis



voice "Risa_0485"
r "「わかったわ……気になるものね」"
voice "Sara_0071"
sr "「そうそう、気になってお仕事に集中できないから……じゃあ、またね～！」"

hide char tsa02s2 at left
hide char tri01s2 at right as r
show char tka02s2
with dis



voice "Kaede_0046"
k "「璃紗さん、六夏さん、素敵な夏休みを過ごしてくださいね」"


show char tka02s2 at sleft as l
show char tri01s2
show char trk01s2 at sright as sr
with dis



voice "Rikka_0314"
rk "「あ、ありがとう……ございます」"
voice "Risa_0486"
r "「楓さまたちも、素敵な夏休みをお過ごしください」"


#allClear:
hide char tka02s2 at sleft as l
hide char tri01s2
hide char trk01s2 at sright as sr
#lastBG:
#scene bg bg18a
with dis


"２人を見送って、私たちも校舎へ入っていった。"


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


show char trk01s2
with dis



voice "Rikka_0315"
rk "「リサ姉、それじゃワタシはここで……」"
"六夏が１年の校舎へと向かおうとしたけれど……急に、その動きがとまった。"


show char tri03s2 at left
show char trk01s2 at right as r
with dis



voice "Risa_0487"
r "「どうかしたの？」"


show char trk03s2 at right as r
with dis



voice "Rikka_0316"
rk "「あ、あの美夜さま……ごきげんよう」"
voice "Risa_0488"
r "「美夜？　あっ……」"

hide char tri03s2 at left
hide char trk03s2 at right as r
show char tmi01s2 at sleft as l
show char tri03s2
show char trk03s2 at sright as sr
with dis



voice "Miya_0228"
m "「………………」"
"全然気がつかなかったけど、私たちの後ろにはいつしか、ピッタリと美夜がついていた。"
voice "Risa_0489"
r "「い、いつから……いたの？」"
voice "Miya_0229"
m "「文化祭は告白のチャンスよ……のあたりから、よ」"


show char tri08s2
with dis



voice "Risa_0490"
r "「ひゃあ、ほぼ最初っからじゃない！　もう、どうして声をかけてくれないのよ」"
"忍びじゃないんだから、気配消してついてこられても困るわ。"
voice "Rikka_0317"
rk "「美夜さま、まるで忍者みたいですね」"


show char tri04s2
with dis



voice "Risa_0491"
r "「ちょ、ちょっと六夏っ」"
"六夏も思ったこと、すぐに言わないの……もう。"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0230"
m "「ふっ……」"
"美夜ったら、鼻で笑ったりして。"
"この２人ってまだ、仲が良くないのかしら？"
"このままだと夏休みに入ってしまうし、今日、少しでも修復出来るのなら……"


show char tri01s2
with dis



voice "Risa_0492"
r "「み、美夜、美夜からも六夏に何か、アドバイスないかしら？」"
"ダメもとで聞いてみる。"
"ここで『六夏が好きなのは沙雪さんですよ』っていうアピールも込みで。"


show char tmi01s2 at sleft as l
with dis



voice "Miya_0231"
m "「そうねぇ……」"
"考えている。"
"美夜が六夏の為に、何か考えてくれているわ。"
voice "Miya_0232"
m "「……当たって砕けてみれば？」"


show char tri04s2
with dis



voice "Risa_0493"
r "「なっ！？」"
"砕けちゃダメじゃない！"


show char trk02s2 at sright as sr
with dis



voice "Rikka_0318"
rk "「わ、わかりました、意気込みが大事ってことですよね、ありがとうございます～」"
"でも本人、喜んでいるし……"


hide char trk02s2 at sright as sr
with dis


"美夜にお礼を言って、六夏は行ってしまった。"


show char tmi01s2 at left
show char tri08s2 at right as r
with dis



voice "Risa_0494"
r "「もう、六夏ったら……」"
voice "Miya_0233"
m "「わたくしたちも早く教室に行きましょう、璃紗」"


show char tri03s2 at right as r
with dis



voice "Risa_0495"
r "「う、うん……」"
"やっぱりまだ美夜は、六夏に対してクールに見えた。"
"当分、仲良くなりそうもないわね……はぁ～"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・夕
scene bg bg08c
with Dis



#mes on
#system on


"明日から夏休みということで、アトリエの掃除を軽くしてから。"
"私は美夜と２人、一緒に帰った。"


show char tmi03s2
with dis



voice "Miya_0234"
m "「まさか、掃除をさせられるとは思ってなかったわ」"


show char tmi03s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0496"
r "「一応、しておかないと……もしかして何か用事があって、学校くることはあるかもしれないけれど、一ヶ月くらい閉めっきりにするんだもの」"
voice "Risa_0497"
r "「茶葉だって、しけってしまうかもしれないじゃない」"
"お茶のセットやお菓子やら、美夜が持ち込んだ食べ物類は特に、要チェックだわ。"


show char tmi01s2 at left
with dis



voice "Miya_0235"
m "「そんなの、心配ないのに……ミニ冷蔵庫があるから」"


show char tri03s2 at right as r
with dis



voice "Risa_0498"
r "「えっ？　いつの間にそんなの買ったの？」"
voice "Miya_0236"
m "「もらったのよ、玲緒さまに」"
voice "Risa_0499"
r "「玲緒さまに？」"
voice "Miya_0237"
m "「教室でいつでもアイスが食べれるように……って持ち込もうとして、麻衣さまに怒られたって言うから、わたくしが引き取ったの」"
voice "Risa_0500"
r "「そ、そう……」"
"教室でアイス……玲緒さまなら、あり得そうなことね。"


show char tri02s2 at right as r
with dis



voice "Risa_0501"
r "「それはともかくとして、掃除するって気持ちいいよね」"


show char tmi03s2 at left
with dis



voice "Miya_0238"
m "「………………」"
"美夜の家はほとんどお手伝いさんがやってくれるから、そういった達成感はわかってもらえないみたい。"
voice "Risa_0502"
r "「でも、明日から夏休みよ……なんか嬉しいわ」"


show char tmi01s2 at left
with dis



voice "Miya_0239"
m "「そうね……学校に行って、くだらない授業を受けなくていいのは嬉しいわ」"


show char tri08s2 at right as r
with dis



voice "Risa_0503"
r "「くだらなくないわよ。今学期もろくに受けてないくせに」"
voice "Miya_0240"
m "「あら、そうだったかしら」"
"そうよ。"
"一体何度、美夜を呼びに行ったか、わからないほどだわ。"


show char tri03s2 at right as r
with dis



voice "Risa_0504"
r "「留年にならないのが不思議なくらいよ」"
voice "Miya_0241"
m "「そうやって、またわたくしに説教するの？」"
voice "Risa_0505"
r "「だから……って、違うわ」"
"明日からの休みのことについて、話したかったのに。"
"美夜といるとついつい、お説教口調になっちゃう。"


show char tri01s2 at right as r
with dis



voice "Risa_0506a"
r "「コホン……いい、よく聞いて」"
voice "Miya_0242"
m "「何かしら？」"
voice "Risa_0507"
r "「私ね……夏休み中はずっと、美夜と二人きりで過ごすわ」"
voice "Miya_0243"
m "「璃紗……」"
voice "Risa_0508"
r "「昨年みたいに、夏季講習も一緒にいくし、できればまた美夜の別荘にも行きたいって思っているの」"
voice "Miya_0244"
m "「………………」"


show char tri02s2 at right as r
with dis



voice "Risa_0509"
r "「あとは……夏だし、海もいいわね～」"
voice "Miya_0245"
m "「………………」"


show char tri01s2 at right as r
with dis



voice "Risa_0510"
r "「美夜はどこか行きたいところ、リクエストあるかしら？」"
voice "Miya_0246"
m "「……ったわ」"


show char tri03s2 at right as r
with dis



voice "Risa_0511"
r "「へっ？」"


show char tmi03s2 at left
with dis



voice "Miya_0247"
m "「わたくしが……悪かったわ」"
"いきなり美夜が謝罪をしたので、私の目は丸くなった。"
voice "Miya_0248"
m "「璃紗がまさか、そんなにわたくしのことを考えているなんて……」"
voice "Risa_0512"
r "「そ……それは、まあ……」"
"最近の美夜ったら、思いっきりスネていたんだもの。"
voice "Miya_0249"
m "「それなのに……わたくしはいつまでも、六夏さんに冷たくして」"
"六夏のことを話す美夜の口調はどこか、ぎこちなさが残っているけれど。"
"もう六夏のことも、私のことも、許してくれている……そんな風に感じられた。"
voice "Miya_0250"
m "「わたくしの方が、先輩なのに……大人げないわよね」"


show char tri01s2 at right as r
with dis



voice "Risa_0513"
r "「美夜……謝らなくていいわよ」"


show char tmi04s2 at left
with dis



voice "Miya_0251"
m "「えっ？」"
voice "Risa_0514"
r "「立場が逆なら、きっと私だって嫉妬しちゃうし……嫉妬してくれる美夜の気持ちが嬉しいの」"


show char tmi01s2 at left
with dis



voice "Miya_0252"
m "「璃紗……」"


show char tri02s2 at right as r
with dis



voice "Risa_0515"
r "「六夏には可哀想だけど、私、心のどこかで美夜に嫉妬されていて、喜んでいたのよ」"


show char tmi02s2 at left
with dis



voice "Miya_0253"
m "「ふふふっ……悪いリサ姉だったのね」"


show char tri05s2 at right as r
with dis



voice "Risa_0516"
r "「もう、その呼び方、やめて……恥ずかしいわ」"
voice "Miya_0254"
m "「ふふふっ」"


show char tri02s2 at right as r
with dis



voice "Risa_0517"
r "「ふふっ……ふふふっ」"
"２人、微笑み合う。"
voice "Miya_0255"
m "「明日から、ずっと一緒ね……璃紗」"
voice "Risa_0518"
r "「ええ、２人で過ごしましょう」"
"恋人になってからの、初めての夏。"
"きっと楽しいことがいっぱい、待ち受けているわ……そんな気がする。"


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
jump S017


