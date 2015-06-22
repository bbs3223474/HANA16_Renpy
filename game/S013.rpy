#「私の知らない世界」

label S013:
$ save_name = "◇私の知らない世界"


#※ここは沙雪視点で

#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP12
play music "sound/BGM12.ogg"


voice "mobJyosiA0040"
mobA "「沙雪さん、ごきげんよう」"


show char tsy02s2
with dis



voice "Sayuki0075"
s "「ごきげんよう」"
voice "mobJyosiB0027"
mobB "「白雪姫、今日もお美しいですわ」"
voice "Sayuki0076"
s "「うふふ、ありがとうございます」"
"朝、校門に近づくにつれ、たくさんの方が挨拶をしてくれます。"
"ベストカップルに選ばれてからは、他のクラスの方や、先輩達にも声をかけられることが多くなって。"
"なんだか、たくさんの人とお知り合いになれたみたいで、嬉しく思っています。"


show char tsy01s2
with dis



voice "Sayuki0077"
s "「あっ、あれは……」"
"優菜さまと、七海さまだわ。"
"お二人は朝も、ご一緒に登校なさるのね。"
"挨拶をする為に、私は２人に近づいていきました。"


show char tna03s2
with dis



voice "Nanami0112"
n "「うーん……」"


show char tyu03s2 at left
show char tna03s2 at right as r
with dis



voice "Yuuna_0025"
y "「七海ったら、朝からそんな難しい顔して……どうしたの？」"


show char tna01s2 at right as r
with dis



voice "Nanami0113"
n "「いえ、例のことだけど、なかなか進展しませんね」"


show char tyu02s2 at left
with dis



voice "Yuuna_0026"
y "「ふふふっ、七海は後輩想いで、優しいのね」"
voice "Nanami0114"
n "「そんなぁ、わたしなんてお姉さまに比べたら、大したことないです」"
voice "Yuuna_0027"
y "「私は後輩想いではなくて、七海想いなだけよ」"


show char tna05s2 at right as r
with dis



voice "Nanami0115"
n "「お、お姉さまったら……もう」"


#allClear:
hide char tyu02s2 at left
hide char tna05s2 at right as r
#lastBG:
#scene bg bg18a
show char tsy03s2
with dis



voice "Sayuki0078"
s "「？？？」"
"何の話を、しているのかしら？"
"私がここで話しかけては、お邪魔になってしまうかしら。"
"でも、こうして後ろで立ち聞きしているのも、はしたないことですし……"
"私はさりげなくお二人の横に並んで、挨拶をしました。"


show char tsy02s2
with dis



voice "Sayuki0079"
s "「優菜さま、七海さま、ごきげんよう」"


show char tna04s2 at left
show char tsy02s2 at right as r
with dis



voice "Nanami0116"
n "「さ、沙雪さん……」"

hide char tna04s2 at left
hide char tsy02s2 at right as r
show char tyu02s2 at sleft as l
show char tna04s2
show char tsy02s2 at sright as sr
with dis



voice "Yuuna_0028"
y "「あら、沙雪ちゃん、ごきげんよう」"
"七海さんは体が少し、飛び上がったように見えましたが。"
"優菜さまは普段通り、笑顔で挨拶を返してくれました。"


show char tna03s2
with dis



voice "Nanami0117"
n "「あの、沙雪さん……いつから、わたしたちの後ろに？」"


show char tsy03s2 at sright as sr
with dis



voice "Sayuki0080"
s "「えっ、少し前ですが、何か不都合な事でも？」"
voice "Yuuna_0029"
y "「ふふふっ、七海ったら……おねしょした話を聞かれたかと思ったのよね」"


show char tna04s2
with dis



voice "Nanami0118"
n "「ちょ、ちょっと、おねしょなんてしてませんっ」"


show char tyu01s2 at sleft as l
with dis



voice "Yuuna_0030"
y "「あら、したことあるでしょう、子供の頃に」"


show char tna05s2
with dis



voice "Nanami0119"
n "「あっ……もう、優菜さまったら」"
"七海さんは怒ったり、真っ赤になったり、コロコロと表情が変わっていく。"
"環境整備委員でご一緒している時とは、また違う印象を受けました。"
"それはきっと、優菜さまが隣りにいるからなのかしら……"
voice "Yuuna_0031"
y "「そんな他愛もない話をしていただけだから、沙雪ちゃんは気にしないでね」"


show char tsy01s2 at sright as sr
with dis



voice "Sayuki0081"
s "「ええ、わかりました」"


#allClear:
hide char tyu01s2 at sleft as l
hide char tna05s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg18a
with dis


"そのまま会釈をして、お二人とお別れしました。"


show char tsy03s2
with dis



voice "Sayuki0082"
s "「でも……なんだか、おかしいです」"
"おねしょ、だなんて……さっき少し聞こえて来たお話とは、違う気がします。"
voice "Sayuki0083"
s "「先輩方を疑うなんて、いけないこと。でも……」"
"最近、こういうことが多い気がしてなりません。"
"私が近づくと、皆さんは急に会話を止めてしまうのです。"
voice "Sayuki0084"
s "「気のせいでは、ないような……」"


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


"ベストカップルに選ばれた後、イベント実行委員の仕事をすることになる。"
"それは最初に聞いていたので、その点ももちろん承知の上で。"
"できるだけ、皆さんの期待に添えるつもりではあるけれど……"


show char tsy03s2
with dis



voice "Sayuki0085"
s "「私にはお仕事、全然まわって来ませんね」"
"同じく選ばれた六夏さんは、璃紗さまと一緒に、昨年活躍された先輩に話を聞いたり、書類整理を手伝ったりしているというのに。"
"私にはまったく、声がかからない。"
voice "Sayuki0086"
s "「璃紗さまと旧知の仲である、六夏さんの方が……頼りやすいのでしょうか」"
"それとも、他に何か理由が……"
voice "Sayuki0087"
s "「気になります。思い切って、尋ねてみた方が……」"
"そこへちょうど、先輩たちが現れました。"


show char tka01s2 at left
show char tsa02s2 at right as r
with dis



"紗良さまと楓さまだわ。"
"お２人とも芸能活動をされているから、お揃いでお姿を見る機会は、とても少なくなっているけれど。"
"今日はお２人とも、登校していたようでした。"
voice "Sara_0043"
sr "「久しぶりのオフだねぇ～、放課後どっか行こうよ、楓ちゃん{image=image/exch001.png}」"
"ふにゃあ～と、紗良さまが楓さまに寄りかかる。"
"お二人は従姉妹だと聞きましたが……とても仲がよろしいのですね。"
voice "Kaede_0028"
k "「んー、でもここのところ忙しかったし、今日くらいは家でゆっくりしていた方がいいんじゃないかしら」"


show char tsa03s2 at right as r
with dis



voice "Sara_0044"
sr "「ええ～、遊ぼうよ、じゃあカフェ行こうよ。それなら疲れないでしょう？」"
voice "Kaede_0029"
k "「そうね……そのくらいなら……」"


show char tsa02s2 at right as r
with dis



voice "Sara_0045"
sr "「あっ、六夏ちゃんも誘ってみようよ。そして色々と、作戦考えてあげるの♪」"


#allClear:
hide char tka01s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg05a
show char tsy03s2
with dis



voice "Sayuki0088"
s "「……六夏さん？　作戦？？」"
"一体、何のことでしょうか。"


show char tka01s2 at left
show char tsy03s2 at right as r
with dis



voice "Kaede_0030"
k "「もう、面白がっているでしょう、紗良は……あらっ、沙雪さん」"

hide char tka01s2 at left
hide char tsy03s2 at right as r
show char tka01s2 at sleft as l
show char tsa04s2
show char tsy03s2 at sright as sr
with dis



voice "Sara_0046"
sr "「えぇっ？　わっ、沙雪ちゃん」"
voice "Sayuki0089"
s "「………………」"
"どうして私が現れると、こんなにも驚かれるんでしょうか？"


show char tsy01s2 at sright as sr
with dis



voice "Sayuki0090"
s "「ごきげんよう、楓さま、紗良さま」"


show char tsa01s2
with dis



voice "Sara_0047"
sr "「え、ええ……ごきげんよう」"
voice "Sayuki0091"
s "「あの、紗良さま。今、六夏さんのお話をしていませんでしたか？」"


show char tsa03s2
with dis



voice "Sara_0048"
sr "「えっ！？　そ、そうだったかな……あっ、楓ちゃん、メールだよ」"
"紗良さまは携帯を取り出すと、慌てて何か操作し始めました。"


show char tsa04s2
with dis



voice "Sara_0049"
sr "「わっ、マネージャーからだよ、すぐに行かなくちゃ……沙雪ちゃん、またね」"


hide char tsa04s2
show char tka03s2 at sleft as l
with dis


voice "Kaede_0031"
k "「待ってよ、紗良。今日は休みだったんじゃ……」"
voice "Sara_0050"
sr "「急な仕事なんだよ～」"
voice "Kaede_0032"
k "「もう、紗良ったら……それでは沙雪さん、また」"


hide char tka03s2 at sleft as l
with dis


"廊下を走らない代わりに、早歩きでお二人はいなくなってしまった。"


#allClear:
hide char tka03s2 at sleft as l
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg05a
show char tsy03s2
with dis



voice "Sayuki0092"
s "「残念です……もう少し、お話がしたかったのに」"
"結局、何もお聞きすることが出来ませんでした。"
voice "Sayuki0093"
s "「仕方ありません……では別の方に、お話を伺いましょうか」"
"紗良さまの態度に、不自然さを感じてはいましたが。"
"いつまでも、引きずっていられません。"


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


"そして、放課後。"
"イベント実行委員が集まる、教室へとやってきました。"


show char tsy01s2
with dis



voice "Sayuki0094"
s "「あら、早く来すぎてしまいました。まだ、誰もいらっしゃらないなんて……」"
"ベストカップルに選ばれて、初の大きな仕事は、２学期明けに始まる文化祭だと聞いています。"
"その頃になればきっと、お忙しくもなるはず……ですが今はまだ皆さん、のんびりしているようです。"


show char tsy03s2
with dis



voice "Sayuki0095"
s "「早く誰か、来て頂けたら……」"
"イスに座り、ぼんやりと待ちます。"
"しばらくすると、廊下の方から話し声が聞こえてきました。"
"室内が静かなので、余計にその声はここまで響いてきます。"
"この声の感じからして……麻衣さまと玲緒さまに違いないです。"
voice "Reo_0056"
re "「だからぁー、みんなで美味しいものでも食べにいけば、仲良くなれるんじゃないの？」"
voice "Mai_0070"
ma "「美味しいものはともかく、みんなで出かけてみるのもいいかもね。うーん……でもあの２人の好きそうなところって、どこかしら」"
voice "Reo_0057"
re "「デパ地下っ！」"
voice "Mai_0071"
ma "「それはないわ」"
voice "Reo_0058"
re "「どうしてよぉー」"
"２つの足音が、ドアの前で止まりました。"

#//SE：ドアを開ける音

#♀SE003
play sound "sound/SE003.ogg"


show char tma03s2
with dis



voice "Mai_0072"
ma "「六夏ちゃんならともかく、もう片方は超お嬢様だから……あっ」"


show char tsy01s2 at left
show char tma03s2 at right as r
with dis



voice "Sayuki0096"
s "「………………」"
"教室に入ってきた麻衣さまと、私の目が合いました。"
"麻衣さまはまるで凍り付いたように、その場で動きを止めてしまい。"
"後ろからついてきた玲緒さまが、その背中にぶつかってしまいました。"

hide char tsy01s2 at left
hide char tma03s2 at right as r
show char tsy01s2 at sleft as l
show char tma03s2
show char tre08s2 at sright as sr
with dis



voice "Reo_0059"
re "「痛っ、ちょっと麻衣、急に立ち止まらないでよ」"
voice "Mai_0073"
ma "「あっ、ごめんね。玲緒の鼻が、お胸と同じようにへこんじゃったわね」"


show char tre09s2 at sright as sr
with dis



voice "Reo_0060"
re "「ぶーっ、さらっとワタシを不快にさせる一言、つけ加えないで」"


show char tsy03s2 at sleft as l
with dis



voice "Sayuki0097"
s "「申し訳ありません。私が麻衣さまを驚かせてしまったみたいで……」"


show char tre03s2 at sright as sr
with dis



voice "Reo_0061"
re "「あっ、白河沙雪。アンタ、なんでここに？」"


show char tma01s2
with dis



voice "Mai_0074"
ma "「沙雪ちゃんもイベント実行委員なんだから、いてもおかしくないでしょう？　今日は早いのね」"


show char tsy01s2 at sleft as l
with dis



voice "Sayuki0098"
s "「ええ……たまたま、時間がありましたから」"
voice "Mai_0075"
ma "「そう。じゃあお茶でもいれて来ましょうか。簡単なお茶会が出来るくらいのセットは揃っているのよ」"
voice "Sayuki0099"
s "「まだ喉は渇いておりませんから、おかまいなく」"
voice "Mai_0076"
ma "「そう……」"


show char tsy03s2 at sleft as l
with dis



voice "Sayuki0100"
s "「あの……今『でぱちか』と聞こえたのですが、それは一体何ですか？」"
voice "Mai_0077"
ma "「でぱちか………………あっ、デパ地下ね。聞こえていたのね」"
voice "Sayuki0101"
s "「そこに、皆さんで行くと……」"
voice "Mai_0078"
ma "「ああ、ただの例え話よ。ちなみに沙雪ちゃんはどこのデパ地下によく行くの？」"
voice "Sayuki0102"
s "「私、そのでぱちかという場所には、行ったことがありません……どんなところなんでしょうか？」"


show char tre02s2 at sright as sr
with dis



voice "Reo_0062"
re "「そ、そうなの！？　未経験だったんだ……すごい所よ。美味しいものがたくさんあるの{image=image/exch001.png}」"
voice "Sayuki0103"
s "「美味しいもの……レストランみたいなところですか？」"


show char tre01s2 at sright as sr
with dis



voice "Reo_0063"
re "「そういうのとは違って、お店がたくさん並んでいて……って、麻衣なによぉ」"
voice "Mai_0079"
ma "「今日は、学期末試験の勉強をしに来たんでしょう。遊んでいていいの、玲緒？」"


show char tre03s2 at sright as sr
with dis



voice "Reo_0064"
re "「ううっー、わかってるわよ。少しくらいいいじゃない、麻衣のけちっ」"
voice "Sayuki0104"
s "「でぱ……ちか……」"
"会話は中断されてしまい、でぱちかとは何なのか、結局わかりませんでした。"
voice "Sayuki0105"
s "「勉強をしにこられたんですか？」"
voice "Mai_0080"
ma "「ええ、せっかく来てくれたけれど、今は特にイベント実行委員の仕事はないのよ」"
voice "Mai_0081"
ma "「家で勉強すると、この子がすぐに飽きて遊んじゃうから……ここだとちょうどいいかと思って」"
voice "Sayuki0106"
s "「あの……それでは私、ここにいてはお邪魔でしょうか？」"
voice "Mai_0082"
ma "「ううん、そんなことないわ。こっちのことは気にしないでね」"
"そう言って、麻衣さまはカバンからテキストを取り出して、玲緒さまの勉強を見始めました。"


#allClear:
hide char tsy03s2 at sleft as l
hide char tma01s2
hide char tre03s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tma08s2 at left
show char tre03s2 at right as r
with dis



voice "Mai_0083"
ma "「今日は最低でも、この２ページは終わらせるわよ」"
voice "Reo_0065"
re "「えぇっ、無理よ、こんなにたくさん」"


show char tma01s2 at left
with dis



voice "Mai_0084"
ma "「あら、そう……今晩は玲緒の好きな煮込みハンバーグにしてあげようと思ったのに」"


show char tre02s2 at right as r
with dis



voice "Reo_0066"
re "「は、ハンバーグ！　あのトマト味のヤツね、あれワタシ大好き{image=image/exch001.png}」"
voice "Mai_0085"
ma "「じゃあお勉強、頑張りなさい」"


show char tre08s2 at right as r
with dis



voice "Reo_0067"
re "「くぅぅっ……わかったわよ、やればいいんでしょ、やれば！」"


#allClear:
hide char tma01s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"これ以上このお２人からは、話を聞けそうにありません。"
"聞けないけれど、ここ数日の皆さん態度を見ていると、私の疑問が確信に変わっていきます。"
"ベストカップルの皆さんは、集まって何かをしている。"
"でも私が近づくと、驚いて止めてしまいます。"
"そして、それにはおそらく……六夏さんも関わっている。"
"さっきも麻衣さまは『六夏さん』の事を話していたけれど、多分聞いてみても、これまでの経験上、お答えになっては頂けないでしょう。"


show char tsy03s2
with dis



voice "Sayuki0107"
s "「ああ……どうすればいいのでしょうか」"
"ぼんやりと私は、目の前の先輩たちを見つめていました。"


show char tma08s2 at left
show char tre02s2 at right as r
with dis



voice "Reo_0068"
re "「よーし、できた！　これで終わりでしょう、麻衣」"
voice "Mai_0086"
ma "「また適当に、勘で答えを書いたでしょう、玲緒」"


show char tre03s2 at right as r
with dis



voice "Reo_0069"
re "「うっ……」"
voice "Mai_0087"
ma "「玲緒はやれば出来る子なんだから、まじめにしっかりやりなさい」"


show char tre08s2 at right as r
with dis



voice "Reo_0070"
re "「ごほうびくれるなら、やるわ」"
voice "Mai_0088"
ma "「だーかーらー、ハンバーグ作ってあげるって言ったでしょう」"
voice "Reo_0071"
re "「それだけじゃ、足りないわよ」"


show char tma01s2 at left
with dis



voice "Mai_0089"
ma "「もう、玲緒はわがままなんだから」"
"そう言いながら、麻衣さまは玲緒さまの髪の毛をクシャクシャと触ります。"


show char tre01s2 at right as r
with dis



voice "Reo_0072"
re "「んっ……やだぁ～」"
"文句を言いながらも、玲緒さまは微笑んでいるようです。"


#allClear:
hide char tma01s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg30a
show char tsy03s2
with dis



voice "Sayuki0108"
s "「あっ……これって……」"
"自分が仲間外れにされているような、そんな疎外感を覚えて、ここのところ先輩たちの様子を眺めていることが多かったけれど。"
"今になって、私はある事に気づきました。"
voice "Sayuki0109"
s "「もしかして、本当に……」"
"ベストカップルの皆さんは、本当に『恋人』として、お付き合いしているんではないでしょうか。"
"私と六夏さんのような、カップルのフリではなくて、本当に恋人として……"


#//SE：ドアを開ける音
#♀SE003
play sound "sound/SE003.ogg"


show char trk01s2
with dis



voice "Rikka_0241"
rk "「失礼します……あっ」"


show char tsy01s2 at left
show char trk01s2 at right as r
with dis



voice "Sayuki0110"
s "「ごきげんよう、六夏さん」"
voice "Rikka_0242"
rk "「ごきげんよう……沙雪さん」"
"六夏さん、落ちつこうとしているみたいだけれど、私を見た瞬間、ちょっと焦りを感じたように見えました。"
"同じ学年なのに……何故でしょうか。"


#allClear:
hide char tsy01s2 at left
hide char trk01s2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0090"
ma "「あら、六夏ちゃん……今日は一人」"


show char tma01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_0243"
rk "「はい。麻衣さま、玲緒さまごきげんよう」"

hide char tma01s2 at left
hide char trk01s2 at right as r
show char tma01s2 at sleft as l
show char tre01s2
show char trk01s2 at sright as sr
with dis



voice "Reo_0073"
re "「よく来たわね。早速だけど、お茶をいれてきなさいよ」"


show char tma08s2 at sleft as l
with dis



voice "Mai_0091"
ma "「なんで命令口調なのよ、玲緒」"
voice "Rikka_0244"
rk "「いいですよ、すぐいれてきますね……沙雪さんも飲みますか？」"


#allClear:
hide char tma08s2 at sleft as l
hide char tre01s2
hide char trk01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tsy01s2
with dis



voice "Sayuki0111"
s "「いいえ、私も手伝います」"


show char tsy01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_0245"
rk "「大丈夫です。そんなに大人数じゃありませんから……すぐいれてきますね」"


#allClear:
hide char tsy01s2 at left
hide char trk01s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"てきぱきと、お茶の支度をして。"
"本当にあっと言う間に、六夏さんは人数分のお茶をいれてきて下さいました。"
"勉強は一休み……と、玲緒さまはポーチの中から何かを取り出しました。"


show char tre01s2
with dis



voice "Reo_0074"
re "「お茶といえば、やっぱりお菓子よね。篠崎六夏と白河沙雪にも、少しならあげるわよ」"
"私と六夏さんにお菓子を配って下さる、玲緒さま。"
"その玲緒さまを、麻衣さまはどこか優しい目で見つめています。"


show char tma01s2 at left
show char tre01s2 at right as r
with dis



voice "Mai_0092"
ma "「玲緒、そのポーチ、ずっと使っててくれてるのね」"


show char tre05s2 at right as r
with dis



voice "Reo_0075"
re "「当たり前じゃない……まっ、麻衣が選んでくれたものだし……」"


show char tma02s2 at left
with dis



voice "Mai_0093"
ma "「ふふふっ、ありがとう」"


show char tre08s2 at right as r
with dis



voice "Reo_0076"
re "「お菓子を入れるのに、他にちょうどいいのがないからよっ」"
voice "Mai_0094"
ma "「はいはい、わかっているわ」"
"優しく見守るような瞳で、玲緒さまを見つめ続ける麻衣さま。"
"私はこんな風に、誰かを見つめたことがあったかしら？"
"ちょっと……うらやましい、です。"
"私には、そのようなお相手が……"


#allClear:
hide char tma02s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg30a
show char trk03s2
with dis



voice "Rikka_0246"
rk "「あ、あの……何か悩みでもあるの、沙雪さん？」"
"不意に、六夏さんが心配そうに声をかけてきました。"


show char tsy01s2 at left
show char trk03s2 at right as r
with dis



voice "Sayuki0112"
s "「六夏さん……いいえ、何もありませんわ」"
"こうやって私を気づかってくれる、六夏さんの気持ちが嬉しい。"
"六夏さんは私だけではなく、他のクラスメイトも……いいえ、誰に対しても、このように気を使っています。"


#★★★選択肢　ここから



voice "Sayuki0113"
s "（私だけに対して、特別というわけではない……）"
"きっとそうなんです。"
"でも……もし、私と六夏さんが普通とは違う、特別な関係だったなら……"



#++選択肢（３）
#１．『六夏さんと、本当のカップルだったら……』○
#２．『私は……特別、ですか……？』×
menu:
    "六夏さんと、本当のカップルだったら……":
     jump select03_1
    "私は……特別、ですか……？":
     jump select03_2



#１．『六夏さんと、本当のカップルだったら……』
label select03_1:


show char tsy03s2 at left
with dis



voice "Sayuki0114"
s "「私と六夏さんも、他の皆さんのように……本当のカップルだったら……」"
voice "Rikka_0247"
rk "「さ、沙雪さん……今、なんて……？？」"


show char tsy05s2 at left
with dis



voice "Sayuki0115"
s "「い……いいえ、何でもありません」"
"ああ、私ったら……なんてとんでもない事を、口走ってしまったのでしょう。"
"私はそんな夢を見てはいけないのに、抱いてはいけないのに……"


#set f1 f1+1
jump select03_end


#２．『私は……特別、ですか……？』×
label select03_2:


show char tsy03s2 at left
with dis



voice "Sayuki0116"
s "「私は……特別、ですか……？」"
voice "Rikka_0248"
rk "「えっ？　沙雪さん、今、なんて……？？」"


show char tsy05s2 at left
with dis



voice "Sayuki0117"
s "「い、いえ、その……自分でも、よくわかりません……申し訳ありません」"
"私ったら、よく意味のわからない事を言ってしまったでしょうか。"
"ああ、恥ずかしいです……"


#++選択肢終了
#★★★選択肢　ここまで
label select03_end:


voice "Rikka_0249"
rk "「あ、あの……沙雪さん……」"


show char tsy01s2 at left
with dis



voice "Sayuki0118"
s "「六夏さん、お茶ごちそうさまでした。たいへん美味しかったです」"
voice "Rikka_0250"
rk "「あっ……うん……」"
voice "Sayuki0119"
s "「今日は特にお仕事もないみたいですし、私はこれで失礼します」"
voice "Rikka_0251"
rk "「……うん、それじゃ……ごきげんよう……」"


hide char tsy01s2 at left
with dis


"私は、六夏さんからそっと、離れていきました。"
"これ以上、おかしな事を考えずに済むように。"
"決して言ってはいけない事を、言わないためにも……"


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
jump S014


