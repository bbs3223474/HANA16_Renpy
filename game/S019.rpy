#「再会を祝して」

label S019:
$ save_name = "◇再会を祝して"


#**ビーチテラス・昼
scene bg bg40a
with Dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


show char tri01m
with dis



voice "Risa_0606"
r "「ふぅ～、リゾート地のビーチって、なんか違うわね……ん、あれは？」"
"一休みしようと、ビーチのテラスに戻ってきた私が見たものは、何ともゴージャスな、美しい姉妹だった。"


#※EV005
#allClear:
hide char tri01m
#lastBG:
#scene bg bg40a
scene bg EV05
with Dis



"大胆で美しい水着の麗奈先生が、デッキチェアでくつろいでいて。"
"その膝の上には、何とも愛らしい女の子がじゃれついていた。"
voice "Runa_0024"
rn "「んふふっ、ねえさま……いつまでお休みなの？　またすぐ、お仕事に……戻られるの？」"
voice "Rena_0023"
ren "「いいえ、今回は最後まで、みんなと一緒に楽しむつもりよ。もちろん、瑠奈とも……ね{image=image/exch001.png}」"
voice "Runa_0025"
rn "「それほんと、ねえさま！？　ずっと一緒なの？？」"
voice "Rena_0024"
ren "「ええ、一緒よ……だからって、甘えすぎちゃダメよ、瑠奈」"
voice "Runa_0026"
rn "「ちっ、違うわ、これは甘えているんじゃなくて………………そう、じゃれているだけよ。久々に会えたねえさまを、癒しているの」"
voice "Rena_0025"
ren "「ふぅん……なんかネコみたいね。本当に可愛い仔ネコちゃん……ほら、撫で撫でしてあげるわね{image=image/exch001.png}」"


#※EV005P1
scene bg EV05p1
with Dis



voice "Runa_0027"
rn "「ひゃっ、ぁん、もう……そこはくすぐったいの、ねえさま……ぁん」"
voice "Rena_0026"
ren "「あら、そうだったの……瑠奈の性感帯、一つ発見ね{image=image/exch001.png}」"
voice "Runa_0028"
rn "「もう、そんなのじゃないわ、ただくすぐったいだけよ……もぉ、そこはダメなのぉ」"
voice "Rena_0027"
ren "「後で貴子にも、教えてあげなくちゃね……んふっ{image=image/exch001.png}」"
voice "Runa_0029"
rn "「そんなのダメ、言っちゃダメぇ……はぅぅ、力が抜けちゃうぅ……くぅん」"
voice "Rena_0028"
ren "「本当に、可愛いわ……瑠奈、んふふっ{image=image/exch001.png}」"
voice "Risa_0607"
r "「あぁ………………なんか、すごいもの見ちゃったかも」"
"いつもは大人ぶっている……ううん、大人っぽい瑠奈ちゃんも、あの麗奈先生の前では仔ネコみたくなっちゃうのね。"
voice "Risa_0608"
r "「仲良し姉妹って感じ……なんかうらやましいな」"


#**ビーチテラス・昼
scene bg bg40a
with Dis



show char tmi01m
with dis



voice "Miya_0297"
m "「ちょっと璃紗、何やってるの？　早くこっちにいらっしゃいよ」"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0609"
r "「うん、今行くわね」"
"何とも和んだ気分を感じながら、私は美夜の元へと走り出していった……"


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
with Dis



#mes on
#system on


show char trn01f2
with dis



voice "Rena_0029"
ren "「今日はみんな、集まってくれてありがとう。じゃあ、再会を祝して……乾杯～」"


#allClear:
hide char trn01f2
#lastBG:
#scene bg bg39c
with dis


voice "mobAll_0000"
a "「カンパ～イ」"
"南の島での１日目の夜は、砂浜でバーベキューになった。"
"みんなで夕方から準備を始めて、わいわい言いながら、材料を切り分けたりして。"
"本当に、去年の合宿の時みたいだった。"


show char tma03f2
with dis



voice "Mai_0135"
ma "「ん～……このジュース、お酒っぽいけど？」"


show char tma03f2 at left
show char tmi01f2 at right as r
with dis



voice "Miya_0298"
m "「大丈夫です、ノンアルコールだから」"

hide char tma03f2 at left
hide char tmi01f2 at right as r
show char tma03f2 at sleft as l
show char tmi01f2
show char ter01f2 at sright as sr
with dis



voice "Erisu_0047"
e "「美夜さんってなんか、ノンアルコールのジュース好きだよね。もしかして、自分で用意したの？」"
voice "Miya_0299"
m "「ホテルにいくらでもあったわ。本物のお酒も一応、あちらにあるけれど」"


#allClear:
hide char tma03f2 at sleft as l
hide char tmi01f2
hide char ter01f2 at sright as sr
#lastBG:
#scene bg bg39c
with dis


"美夜が指さした先では、麗奈先生が景気よく瓶を開けていた。"


show char trn02f2
with dis



voice "Rena_0030"
ren "「貴子、おかわり～♪」"


show char trn02f2 at left
show char tta03f2 at right as r
with dis



voice "Takako0033"
t "「せ、先輩、飲み過ぎなんじゃ……」"
voice "Rena_0031"
ren "「いいのよ、せっかくのお祝いなんだから」"

hide char trn02f2 at left
hide char tta03f2 at right as r
show char tru01f2 at sleft as l
show char trn02f2
show char tta03f2 at sright as sr
with dis



voice "Runa_0030"
rn "「そうよ……はい、ねえさま」"
voice "Rena_0032"
ren "「あら、気が利くわね、瑠奈」"
voice "Runa_0031"
rn "「ねえさま、それ飲み終わったら、あっちの方に散歩に行きましょうよ」"
voice "Rena_0033"
ren "「そうねー、いいわねー」"


show char tru02f2 at sleft as l
with dis



voice "Runa_0032"
rn "「ふふふっ{image=image/exch001.png}」"
"瑠奈さんはお姉さんにベタベタして、かまってオーラ全開に見えた。"


#allClear:
hide char tru02f2 at sleft as l
hide char trn02f2
hide char tta03f2 at sright as sr
#lastBG:
#scene bg bg39c
show char tri02f2
with dis



voice "Risa_0610"
r "「ふふふっ……ああいうところを見ると、年相応で可愛いのにね」"
"少し大人びた口を利いて、いつも堂々としている瑠奈ちゃんだけど。"
"今日は普通の、お姉さんが大好きな女の子に見えてきた。"
"なんだか、微笑ましいわね。"


show char tna01f2 at left
show char tri02f2 at right as r
with dis



voice "Nanami0159"
n "「璃紗さん、お肉焼けたわよ」"


show char tri01f2 at right as r
with dis



voice "Risa_0611"
r "「あっ、ありがとう」"
"バーベキューグリルの上で炙っていたお肉がジュージュー、いい感じに焼けてきた。"
"七海さんがそれを、取り皿に分けてくれた。"

hide char tna01f2 at left
hide char tri01f2 at right as r
show char tsa01f2 at sleft as l
show char tna01f2
show char tri01f2 at sright as sr
with dis



voice "Sara_0082"
sr "「ほらほら、ぼーっとしてると無くなっちゃうよ、璃紗ちゃん」"
voice "Risa_0612"
r "「そうだね、いただきます」"
"いけないいけない。"
"せっかくのバーベキューだもの。"
"温かいうちに、頂かなきゃ。"


show char tri02f2 at sright as sr
with dis



voice "Risa_0613"
r "「パクッ……もぐもぐ……ああ、美味しいっ」"


show char tsa02f2 at sleft as l
with dis



voice "Sara_0083"
sr "「うんうん、すっごく美味しいよね{image=image/exch001.png}」"
"肉も野菜も、炭火でこんがりと焼けていて、とても美味しかった。"


show char tna02f2
with dis



voice "Nanami0160"
n "「こんな風に海を見ながら、食事出来るっていいですよね」"
voice "Risa_0614"
r "「うん、いくらでも食べれちゃいそう」"


show char tsa01f2 at sleft as l
with dis



voice "Sara_0084"
sr "「ホントホント。でも、食べすぎは注意だよ」"


show char tna03f2
with dis



voice "Nanami0161"
n "「うううっ……そうでした」"
voice "Risa_0615"
r "「ふふふっ」"


#allClear:
hide char tsa01f2 at sleft as l
hide char tna03f2
hide char tri02f2 at sright as sr
#lastBG:
#scene bg bg39c
with dis


"しばらく食事に専念していると、どこからか言い争う声が聞こえてきた。"


show char tre09f2
with dis



voice "Reo_0114"
re "「ちょっと綾瀬美夜、焼いてるそばから、すぐに食べないでよ！　それはワタシの肉なのよ～！」"


show char tre09f2 at left
show char tmi01f2 at right as r
with dis



voice "Miya_0300"
m "「………………」"
voice "Reo_0115"
re "「なによなによ！　無言で食べ続けないでよぉ」"
"向こうの方で、玲緒さまが騒いでいるけれど。"


#allClear:
hide char tre09f2 at left
hide char tmi01f2 at right as r
#lastBG:
#scene bg bg39c
show char tri03f2
with dis



voice "Risa_0616"
r "「うーん……申し訳ないけれど、関わらない方がいいわね」"
"美夜の食欲に関しては、私でも止めるのは難しいから……"


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
with Dis



#mes on
#system on


show char tri01f2
with dis



voice "Risa_0617"
r "「……ん……麗奈先生……」"
"お腹も満腹になったところで、海を見ながら少しのんびりしていると。"
"足早に駆けまわる、麗奈先生が見えた。"
"どうやらそれぞれのカップルのところに行って、近況を聞いて周っているみたい。"
"楽しそうな声が、あちらこちらで聞こえてきた。"
"もう、私たちの先生ではないけれど。"
"やっぱりこういうところは、前と変わらないんだわ……ふふっ。"


show char trn01f2
with dis



voice "Rena_0034"
ren "「……そうなの、織田さんは松原さんの後を引き継ぐ為に、頑張っているのね」"


show char tna05f2 at left
show char trn01f2 at right as r
with dis



voice "Nanami0162"
n "「わたしなんて、まだまだですけど……」"

hide char tna05f2 at left
hide char trn01f2 at right as r
show char tyu02f2 at sleft as l
show char tna05f2
show char trn01f2 at sright as sr
with dis



voice "Yuuna_0060"
y "「ふふふっ、そんなことないわ。七海は一生懸命、やれているわよ」"
voice "Nanami0163"
n "「お、お姉さま……」"
voice "Rena_0035"
ren "「そう……それで松原さん、あっちの方はどうなの？」"


#allClear:
hide char tyu02f2 at sleft as l
hide char tna05f2
hide char trn01f2 at sright as sr
#lastBG:
#scene bg bg39c
show char tri03f2
with dis



voice "Risa_0618"
r "「んっ……あっちって、何かしら？」"
"麗奈先生は優菜さまの耳元で、こしょこしょ何かを言っている。"


show char trn01f2 at sleft as l
show char tyu02f2
show char tna05f2 at sright as sr
with dis



voice "Yuuna_0061"
y "「それは……もちろん、七海は……」"
"波の音に消されてしまって、優菜さまの返事は聞こえない。"
"でもすぐ隣にいた七海さんには聞こえていたみたいで、真っ赤になってその場にうずくまってしまった。"


#allClear:
hide char trn01f2 at sleft as l
hide char tyu02f2
hide char tna05f2 at sright as sr
#lastBG:
#scene bg bg39c
show char tri03f2
with dis



voice "Risa_0619"
r "「何の話をしているのかしら……？」"
"疑問に感じているうちに、麗奈先生は今度は、紗良さんと楓さまのところへ移動する。"


show char trn02f2
with dis



voice "Rena_0036"
ren "「２人とも大活躍ね。海外にいても、ネットで２人の姿を見ているわ～」"


show char tka05f2 at sleft as l
show char tsa02f2
show char trn02f2 at sright as sr
with dis



voice "Kaede_0054"
k "「あ、ありがとうございます。でも……恥ずかしいです」"
voice "Sara_0085"
sr "「そうなんです♪　楓ちゃんの歌のプロモなんて、ニッコリ動画で再生回数がどんどん伸びていってるんですよー」"
voice "Kaede_0055"
k "「さ、紗良ったら……もう」"
voice "Rena_0037"
ren "「わかるわ～、教師をしていた時から、楓さんには磨けば光る原石を感じていたから」"
voice "Sara_0086"
sr "「そうですよねー{image=image/exch001.png}」"
voice "Kaede_0056"
k "「２人とも、もうやめて……ぅぅっ」"
"今度は、楓さまが恥ずかしそうにしている。"


#allClear:
hide char tka05f2 at sleft as l
hide char tsa02f2
hide char trn02f2 at sright as sr
#lastBG:
#scene bg bg39c
with dis


"麗奈先生の進撃は止まらず、次は麻衣さまと玲緒さまのところへ。"


show char trn01f2
with dis



voice "Rena_0038"
ren "「お久しぶり、川村さん」"


show char tre08f2 at left
show char trn01f2 at right as r
with dis



voice "Reo_0116"
re "「………………」"

hide char tre08f2 at left
hide char trn01f2 at right as r
show char tma03f2 at sleft as l
show char tre08f2
show char trn01f2 at sright as sr
with dis



voice "Mai_0136"
ma "「玲緒、麗奈先生よ。もう忘れちゃったかしら？」"
voice "Reo_0117"
re "「忘れてないわよ……こ、こんにちは……」"
voice "Rena_0039"
ren "「もうこんばんは、の時間よ。あなたたちは、沢口さんがしっかりしているから、大丈夫そうね」"


show char tma02f2 at sleft as l
with dis



voice "Mai_0137"
ma "「はい。玲緒はわたしがいないと何も出来ない子ですが、わたしがちゃんとついてますから」"


show char trn02f2 at sright as sr
with dis



voice "Rena_0040"
ren "「ふふふっ、頼もしい恋人がいて良かったわね、川村さん」"
voice "Mai_0138"
ma "「良かったわね、玲緒」"


show char tre09f2
with dis



voice "Reo_0118"
re "「ふっ、２人して、そんな生暖かい目でワタシを見ないでっ！」"


show char tma01f2 at sleft as l
with dis



voice "Mai_0139"
ma "「はいはい、これ以上いじると、猛獣のごとく暴れますので、この辺で勘弁してあげてください」"


show char trn01f2 at sright as sr
with dis



voice "Rena_0041"
ren "「わかってるわ、それじゃあ」"


#allClear:
hide char tma01f2 at sleft as l
hide char tre09f2
hide char trn01f2 at sright as sr
#lastBG:
#scene bg bg39c
with dis


"逃げ出すように、麗奈先生は玲緒さまから離れて、続いてエリスさまたちの方へ向かった。"


show char trn01f2
with dis



voice "Rena_0042"
ren "「短大の方、もう慣れた？」"


show char ter03f2 at sleft as l
show char tsi01f2
show char trn01f2 at sright as sr
with dis



voice "Sizuku0040"
sk "「ええ、エリスも一緒ですし、高等部からの知り合いも多いので、思ったより早く順応出来ています」"
voice "Erisu_0048"
e "「講義はちょっと、眠いけど……」"


show char tsi08f2
with dis



voice "Sizuku0041"
sk "「エリスっ、あなたはまた……」"
voice "Erisu_0049"
e "「えー、だって」"


show char trn02f2 at sright as sr
with dis



voice "Rena_0043"
ren "「ふふふっ、たしかに大学の講義って、退屈よね」"


show char ter01f2 at sleft as l
with dis



voice "Erisu_0050"
e "「麗奈先生、わかってくれてますね」"


show char trn01f2 at sright as sr
with dis



voice "Rena_0044"
ren "「一時、短大の講師をやってくれないかって話もあったのよね」"


show char ter02f2 at sleft as l
with dis



voice "Erisu_0051"
e "「わっ、それ実現したら面白かったかも。麗奈先生の授業、聞きたかったー」"
voice "Rena_0045"
ren "「そう？　それじゃあ今から、粢さんだけに特別レクチャーしようかしら」"


show char ter03f2 at sleft as l
with dis



voice "Erisu_0052"
e "「えっ？」"
voice "Rena_0046b"
ren "「えっと……について、とか」"


#allClear:
hide char ter03f2 at sleft as l
hide char tsi08f2
hide char trn01f2 at sright as sr
#lastBG:
#scene bg bg39c
show char tri03f2
with dis



voice "Risa_0620"
r "「んん……何かしら……？」"
"肝心なところになると、波の音に邪魔にされてしまうのよね。"


show char ter02f2 at sleft as l
show char tsi07f2
show char trn01f2 at sright as sr
with dis



voice "Erisu_0053"
e "「……それ聞きたい、是非、聞きたいですっ！！」"
voice "Sizuku0042"
sk "「い、いけません、そんなのだめ……絶対だめですっ！」"
"エリスさまは大喜びだけど、雫さまは怒っているみたい。"
"一体、何だったんだろう……とっても気になるわ。"


#allClear:
hide char ter02f2 at sleft as l
hide char tsi07f2
hide char trn01f2 at sright as sr
#lastBG:
#scene bg bg39c
show char tmi03f2
with dis



voice "Miya_0301"
m "「……璃紗、さっきから落ち着かないけど、何か悩みでもあるの？」"


show char tmi03f2 at left
show char tri03f2 at right as r
with dis



voice "Risa_0621"
r "「えっ！？　えーと……」"
"他人にあまり関心のない美夜には『麗奈先生と他カップルの会話が気になっているの』と言っても、わかってもらえそうにない。"
voice "Risa_0622"
r "「悩みってほどじゃ……って、何食べてるの？」"


show char tmi01f2 at left
with dis



voice "Miya_0302"
m "「これ？　食後だから、フルーツよ」"
"美夜の前には山盛りの、パイナップルやらマンゴーなどの果物が積まれていた。"
voice "Miya_0303"
m "「肉ばかりで飽きたから、フルーツをもらって来たの。璃紗も食べる？」"
voice "Risa_0623"
r "「も、もらおうかな……」"
voice "Miya_0304"
m "「パイナップルとマンゴー、何個づつ食べる？」"
voice "Risa_0624"
r "「一切れでいいわ」"
"なんで美夜、１個単位で渡そうとするのかしら。"
"常人の私が、そんなに食べられるわけないじゃない。"

hide char tmi01f2 at left
hide char tri03f2 at right as r
show char tmi01f2 at sleft as l
show char tri03f2
show char trn02f2 at sright as sr
with dis



voice "Rena_0047"
ren "「あら、美味しそうね」"


show char tri04f2
with dis



voice "Risa_0625"
r "「れ、麗奈先生っ！」"
"後ろからにゅっと不意打ちで、麗奈先生が私たちをのぞき込んできた。"
"少し前まで、エリスさまたちのところにいたのに……本当に素早いわ。"
voice "Miya_0305"
m "「……先生も、フルーツ食べますか」"
voice "Rena_0048"
ren "「綾瀬さん、ありがとう」"
voice "Miya_0306"
m "「では、何個ずつ……」"


show char tri01f2
with dis



voice "Risa_0626"
r "「ここに切り分けてあるパイナップル、どうぞ」"


show char trn01f2 at sright as sr
with dis



voice "Rena_0049"
ren "「それじゃあ、一切れいただくわね」"
"美夜ったら……普通の人は個数単位では食べないっていうのに……"
"ジロッと美夜を睨むと、まったく気にせずに、マンゴーを次々と飲み込んでいた。"
voice "Rena_0050"
ren "「ああ、美味しかったわ。それにしてもあなたたち、もうしっかりと、恋人同士が板についたって感じね」"


show char tmi02f2 at sleft as l
with dis



voice "Miya_0307"
m "「はい……麗奈先生が言った通りになりましたね{image=image/exch001.png}」"


show char trn02f2 at sright as sr
with dis



voice "Rena_0051"
ren "「でしょう……んふふっ」"


show char tri03f2
with dis



voice "Risa_0627"
r "「？？？」"
"麗奈先生と美夜が、ニヤリと笑う。"
"この笑い、明らかに悪人の笑みだわ。"
"この２人……かつて一体、何を話していたっていうの！？"
voice "Risa_0628"
r "「あの……麗奈先生、美夜……」"
voice "Rena_0052"
ren "「それじゃあ、これからも２人、仲良くね」"


show char tri04f2
with dis



voice "Risa_0629"
r "「ちょ、ちょっと麗奈センセイっ！」"

hide char trn02f2 at sright as sr
with dis


"私に尋ねる暇も与えずに、麗奈先生はサッと行ってしまった。"

hide char tmi02f2 at sleft as l
show char tmi02f2 at left
show char tri03f2 at right as r
with dis



voice "Risa_0630"
r "「美夜、今の話って……」"


show char tmi01f2 at left
with dis



voice "Miya_0308"
m "「……さあ？」"
voice "Risa_0631"
r "「ちょっとぉー、気になるじゃない、教えてよ」"
voice "Miya_0309"
m "「それより璃紗、お友達が来たわよ」"
voice "Risa_0632"
r "「えっ……？」"
"いつの間にか、２年生会の２人がやってきていた。"


show char tsa01f2 at left
show char tna01f2 at right as r
with dis



voice "Sara_0087"
sr "「わぁ、すごいフルーツの量だね。美夜ちゃん、これ全部食べるの？」"

hide char tsa01f2 at left
hide char tna01f2 at right as r
show char tmi01f2 at sleft as l
show char tsa01f2
show char tna01f2 at sright as sr
with dis



voice "Miya_0310"
m "「ええ、頂くわ……もっと食べるつもりだけど」"
voice "Nanami0164"
n "「本当にすごいわ……美味しそう」"
"紗良さんと七海さんが感心したように、美夜の前のフルーツの山を眺めていた。"


show char tri03f2 at sleft as l
show char tsa01f2
show char tna01f2 at sright as sr
with dis



voice "Risa_0633"
r "「２人とも、どうしたの？」"


show char tsa08f2
with dis



voice "Sara_0088"
sr "「……しっ、尾行中だよ」"
voice "Risa_0634"
r "「尾行？　一体誰を？」"


show char tna08f2 at sright as sr
with dis



voice "Nanami0165"
n "「麗奈先生です。みんなに話を聞きに、回っているじゃないですか。ですから、この後は……」"
"当然、六夏たちのところ……でしょうね。"
voice "Sara_0089"
sr "「１年生カップルの２人と麗奈先生、どんな会話するか……気にならない？」"


show char tri08f2 at sleft as l
with dis



voice "Risa_0635"
r "「……気になる、すっごく気になるわ」"
"まだカップルになってない２人。"
"麗奈先生と、どんな会話で盛り上がるのかしら……"


show char tna01f2 at sright as sr
with dis



voice "Nanami0166"
n "「だからね、後をつけているの」"


show char tsa01f2
with dis



voice "Sara_0090"
sr "「ねーねー、璃紗ちゃんも行かない？」"


show char tri03f2 at sleft as l
with dis



voice "Risa_0636"
r "「え、えっと……」"
"美夜の方を見ると、呆れたように『好きにすれば』という表情だった。"
voice "Risa_0637"
r "「じゃ、じゃあ……ちょっと行ってくるわね」"


#allClear:
hide char tri03f2 at sleft as l
hide char tsa01f2
hide char tna01f2 at sright as sr
#lastBG:
#scene bg bg39c
with dis


"美夜と麗奈先生とのことも、問いつめたかったけど。"
"ここは尾行でしょう！"
"私たち３人はソロソロと、先生の後を追っていった……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**岩場・夜
scene bg bg41c
with Dis



#mes on
#system on


show char tsa02f2
with dis



voice "Sara_0091"
sr "「……おっ、ハッケン～♪」"


show char tsa02f2 at left
show char tna01f2 at right as r
with dis



voice "Nanami0167"
n "「ちょうどここに岩場があって、よかったですね。向こうからは見えないはずです」"

hide char tsa02f2 at left
hide char tna01f2 at right as r
show char tsa02f2 at sleft as l
show char tna01f2
show char tri01f2 at sright as sr
with dis



voice "Risa_0638"
r "「ええ……」"
"私たち３人は岩場の陰に隠れて、麗奈先生と六夏たちの会話を盗み聞きすることにした。"


#allClear:
hide char tsa02f2 at sleft as l
hide char tna01f2
hide char tri01f2 at sright as sr
#lastBG:
#scene bg bg41c
show char trn02f2
with dis



voice "Rena_0053b"
ren "「新しいベストカップルさん、こんばんわ」"


show char trn02f2 at left
show char tsy01f2 at right as r
with dis



voice "Sayuki0140"
s "「麗奈さま……祖母からいつも、お噂は伺っております」"


show char trn01f2 at left
with dis



voice "Rena_0054"
ren "「おばあ様は、お元気かしら？」"
voice "Sayuki0141"
s "「ええ、とても。先日は名門会の集まりに参加していたようで……」"
"……そして、その後。"
"２人は私たちの知らない人たちの話や、蓬莱泉家や白河家でのことなんかを話し始めてしまった。"


#allClear:
hide char trn01f2 at left
hide char tsy01f2 at right as r
#lastBG:
#scene bg bg41c
show char tsa03f2
with dis



voice "Sara_0092"
sr "「うーっ、何の話してるのか、さっぱりわからないね」"


show char tsa03f2 at left
show char tna03f2 at right as r
with dis



voice "Nanami0168"
n "「共に究極の淑女と呼ばれている、お二人だけのことはありますね……なんだかオーラが違います」"

hide char tsa03f2 at left
hide char tna03f2 at right as r
show char tsa03f2 at sleft as l
show char tna03f2
show char tri03f2 at sright as sr
with dis



voice "Risa_0639"
r "「あそこだけ、別世界みたいだわ」"
"社交界みたいなところで、会話してるみたい。"
voice "Sara_0093"
sr "「六夏ちゃん、思いっきり困っているね……」"
"２人の会話に入れず、おろおろしてる六夏に、こっちまでドキドキしてしまう。"
voice "Risa_0640"
r "「六夏……大丈夫かしら？」"


show char tna01f2
with dis



voice "Nanami0169"
n "「あっ、２人の会話が終わったみたいです」"
"良かった、今度は麗奈先生、六夏に話しかけているわ。"


#allClear:
hide char tsa03f2 at sleft as l
hide char tna01f2
hide char tri03f2 at sright as sr
#lastBG:
#scene bg bg41c
show char trn01f2
with dis



voice "Rena_0055"
ren "「ね、篠崎さん……他の先輩カップル達とは、うまく行っているの？」"


show char trn01f2 at left
show char trk01f2 at right as r
with dis



voice "Rikka_0350"
rk "「はい、皆さんとても、親切にしてくださるので……」"
voice "Rena_0056"
ren "「そう、良かったわね。ところで貴女は『白雪の騎士』って呼ばれているそうね」"


show char trk05f2 at right as r
with dis



voice "Rikka_0351"
rk "「は、はい……お恥ずかしいですが……」"


show char trn02f2 at left
with dis



voice "Rena_0057"
ren "「そんなことないわ……白雪姫を守る、騎士……貴女達って、本当にお似合いよ」"


#allClear:
hide char trn02f2 at left
hide char trk05f2 at right as r
#lastBG:
#scene bg bg41c
show char tri01f2
with dis



voice "Risa_0641"
r "「麗奈先生……」"
"さっき自慢していた情報網とやらが、本当にあるのなら。"
"２人は本物のカップルじゃないって、知っているはずなのに。"
"六夏は驚いたように顔を上げて、何かを言おうとした。"


show char trn02f2 at left
show char trk03f2 at right as r
with dis



voice "Rikka_0352"
rk "「あ、あの……実は……」"
"六夏は偉大なるＯＢに嘘はつけないと思ったのか、本当のことを言おうとしていた。"
"まさに、その時だった。"


#allClear:
hide char trn02f2 at left
hide char trk03f2 at right as r
#lastBG:
#scene bg bg41c
show char tri04f2
with dis



voice "Risa_0642"
r "「あっ……沙雪さん……」"
"なんと沙雪さんが、六夏の手を取り、ぎゅっと握った。"
"まるで『何も言わなくても良いです』とでも、言わんばかりに……"


show char trn02f2 at sleft as l
show char trk03f2
show char tsy01f2 at sright as sr
with dis



voice "Sayuki0142"
s "「……ありがとうございます、麗奈さま」"
"それだけ言って、穏やかに微笑んでみせる。"
voice "Rena_0058"
ren "「ふふふっ……本当に、お似合いね」"


#allClear:
hide char trn02f2 at sleft as l
hide char trk03f2
hide char tsy01f2 at sright as sr
#lastBG:
#scene bg bg41c
with dis


"麗奈先生はそれだけで何かを察したのか、２人から離れて行った。"


show char tsa03f2
with dis



voice "Sara_0094"
sr "「あっ、やばいよ、先生こっち来ちゃう」"


show char tsa03f2 at left
show char tna03f2 at right as r
with dis



voice "Nanami0170"
n "「とにかく隠れよう、暗いし、何とかごまかせるかも」"


#allClear:
hide char tsa03f2 at left
hide char tna03f2 at right as r
#lastBG:
#scene bg bg41c
with dis


"私たち３人は息を潜めて、先生をやり過ごそうとした……"


show char trn08f2
with dis



voice "Rena_0059"
ren "「……そこの先輩たち、盗み見はだめよ」"


show char trn08f2 at left
show char tri04f2 at right as r
with dis



voice "Risa_0643"
r "「っっ！！」"
"あっけなく見つかり、ポンポンと頭を軽くたたかれて。"


hide char trn08f2 at left
with dis


"先生はそのまま、ホテルの方へと帰っていった。"


show char tna03f2 at left
show char tri03f2 at right as r
with dis



voice "Nanami0171"
n "「もしかして……最初から、バレていたのかしら」"

hide char tna03f2 at left
hide char tri03f2 at right as r
show char tsa01f2 at sleft as l
show char tna03f2
show char tri03f2 at sright as sr
with dis



voice "Sara_0095"
sr "「あの先生のことだもんね。六夏ちゃん達にはバレないよう、慎重に帰ろうっと」"
voice "Risa_0644"
r "「………………」"


show char tna01f2
with dis



voice "Nanami0172"
n "「行きましょう、璃紗さん」"


show char tri01f2 at sright as sr
with dis



voice "Risa_0645"
r "「あっ、そうね……行きましょう」"
"静かに立ち上がり、歩き出す。"


show char tsa02f2 at sleft as l
with dis



voice "Sara_0096"
sr "「なんかドキドキしたねー」"


show char tna02f2
with dis



voice "Nanami0173"
n "「先生には見つかっちゃったけど、面白かったね」"


#allClear:
hide char tsa02f2 at sleft as l
hide char tna02f2
hide char tri01f2 at sright as sr
#lastBG:
#scene bg bg41c
with dis


"２人は特に、気にしていないみたいだけど。"
"私は、麗奈先生に本当の事を話そうとしていた六夏を、沙雪さんが止めたことが、心に引っかかっていた。"


show char tri03f2
with dis



voice "Risa_0646"
r "「なんで止めたのかしら……沙雪さん」"


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


#wipecancel disabled
#waitcancel disabled
#log off

scene image "image/eyecatch04.png"
#wipe vshutter##########################

pause 3

scene black
with Dis

#log on
#waitcancel enabled
#wipecancel enabled


#//END
jump S020



