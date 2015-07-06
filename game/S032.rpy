#「しゃべりたがりの沙雪さん」

label S032:
$ save_name = "◇しゃべりたがりの沙雪さん"


#**中庭・昼
scene bg bg21a
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


show char trk03s2
with dis



voice "Rikka_0670"
rk "「はぁ、はぁ……はぁ……」"


show char trk03s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0283"
s "「あ、あの……六夏さん……く、苦しい……です」"
voice "Rikka_0671"
rk "「えっ………………あっ、すみませんっ！！」"


#allClear:
hide char trk03s2 at left
hide char tsy03s2 at right as r
#lastBG:
#scene bg bg21a
with dis


"ワタシは慌てて急ブレーキ、立ち止まって沙雪さんの手を離す。"
"あの後、一斉にクラスメイトたちに周りを囲まれて、質問責めにあって。"
"沙雪さんも同じく、みんなに囲まれてしまって。"
"そのクラスメイトたちから逃げるように、ワタシは沙雪さんを連れ、この中庭まで逃げて来た。"
"教室を出ていく時、後ろから黄色い声で『素敵ですわ』『愛の逃避行かしら』『騎士が姫を連れて逃げたのよ……ああ、ロマンティック{image=image/exch001.png}』とか、勝手な言葉が聞こえていたけれど。"
"何故、沙雪さんを一緒に連れてきたか……それは彼女を助ける意味もあったが、それ以上に大事な意味があった。"
"沙雪さんの呼吸が整うのを待って、ワタシは彼女に一番聞きたかったことを言った。"


show char trk03s2 at left
show char tsy01s2 at right as r
with dis



voice "Rikka_0672"
rk "「あの……沙雪さん、どうしてクラスのみんなにワタシたちが付き合っていることを話しちゃったの？」"
"そう……ワタシと沙雪さんが相思相愛であることは、もうクラス中の知ることとなっていた。"
"そしてその原因は、なんと沙雪さんだったのだ。"
"今朝、嬉しそうにしているのを見られて、みんなに『夏休み、何か良いことでもあったのですか？』と聞かれて。"
"ワタシとの関係を、あっさりと話してしまっていたのだ。"
"困り果てたワタシを見て、沙雪さんは軽く首をかしげた。"


#※CU06
#allClear:
hide char trk03s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg21a
show char CU06
with dis



voice "Sayuki0284"
s "「あのぉ……ダメでしたか？」"
voice "Rikka_0673"
rk "「だ、ダメっていうか……困るというか、その……」"
voice "Sayuki0285"
s "「別に後ろめたいことでも、やましいことでもないと思ったもので……つい」"
voice "Rikka_0674"
rk "「それは、まあ……うぅ……」"
"沙雪さんの言うこともわかる。"
"別にワタシたち、悪いことをしているわけではないのだから。"
"ワタシだって今朝、誰かに話したい、聞いて欲しいかもって、ちょっと思っていたし。"
"でも冷静に考えれば、こんな事態になるのは、わかっていたはずなのに。"
voice "Rikka_0675"
rk "「あの……なんていえばいいのか……」"
voice "Sayuki0286"
s "「ひょっとして、六夏さん……困っているのですか？」"
"上目遣いに、じぃぃっと顔を見つめられる。"
"まるで『きゅる』って音が聞こえてきそうなその仕草に、ワタシの体温がグッと上がった。"


#★★★選択肢　ここから


"可愛らしい、可愛いすぎる{image=image/exch001.png}"
"こんな沙雪さんに、ワタシは……"



#++選択肢（１）
#１．『困っているなんて……言えない』○
#２．『困っているって……言わないと』×
menu:
 "困っているなんて……言えない":
  jump select07_1
 "困っているって……言わないと":
  jump select07_2



#１．『困っているなんて……言えない』
label select07_1:


voice "Rikka_0676"
rk "「い、いや……困るとか、そういうわけでは……」"
"ヘンなことを言って、沙雪さんを落ちこませたくなかった。"
"だから本当のことは、彼女には言えなかった。"


#set f1 f1+1
jump select07_end


#２．『困っているって……言わないと』
label select07_2:


voice "Rikka_0677"
rk "「ほ、本当は……その、困って……」"
voice "Sayuki0287"
s "「困って……いるの、ですか……？」"
"ああ、ちょっとウルウルしてきちゃったかも、沙雪さん……"
"やっぱりダメ、言えないよぉ。"
voice "Rikka_0678"
rk "「何でも、ないです……やっぱり」"
voice "Sayuki0288"
s "「そう、ですか……ほっ」"


#++選択肢終了
#★★★選択肢　ここまで
label select07_end:


voice "Sayuki0289"
s "「それなら良かったです。皆さん、私たちのことをとっても、祝福してくださいました」"
voice "Rikka_0679"
rk "「そ、そうなんだ……あは、あはははっ」"
"そんな嬉しそうに言われてしまったら『恥ずかしいから、みんなには知られたくない』なんて言い出せない。"
"しかし、それにしても……"
voice "Rikka_0680"
rk "「妄想の中の沙雪さんとは、ずいぶん違うなぁ」"
"あれはワタシが勝手に捏造した、沙雪さんだったけれど。"
"てっきり沙雪さんは、恥じらいが強かったり、秘密にしておきたい人だと思っていたのに。"
"ワタシの予想の斜め上をいくキャラだったんだ……意外だけど。"
"そんなことを考えていると、ふと沙雪さんが話しかけてきた。"
voice "Sayuki0290"
s "「六夏さん……ここの木陰は、とても涼しいですね」"
voice "Rikka_0681"
rk "「え、ええ。夏休みが終わったとはいえ、残暑厳しいし……そうだ、学食でジュース買って来てここで飲みませんか」"
voice "Rikka_0682"
rk "「沙雪さん、前に学食に行きたいって言ってましたよね？」"
voice "Sayuki0291"
s "「覚えていてくれたんですね、六夏さん。嬉しいです……行きましょう」"
"こんな小さなことでも、喜んでくれる。"
"みんなに知られてしまったのは、少し困るけど……２人の今の関係が変わるわけじゃない。"
"やっぱり、相思相愛って……嬉しいな。"
voice "Rikka_0683"
rk "「では行きましょうか、沙雪さん」"
"これから、お互いのことをもっと知って。"
"互いにどんな考えを持っているのか、話し合えばいいんだよね。"
"ワタシは、そう思っていた……でも。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


show char trk03s2
with dis



voice "Rikka_0684"
rk "「……んっ？」"
"翌日、教室に入るなり、またまた騒がしくて。"
"みんなきゃーきゃー、声を上げている。"
voice "Rikka_0685"
rk "「なんだろう……って、みんな沙雪さんの周りに……」"
"沙雪さんのところにクラスメイトたちが集まって、大騒ぎをしている。"
voice "Rikka_0686"
rk "「……イやな予感、するんですけど」"


#allClear:
hide char trk03s2
#lastBG:
#scene bg bg04a
with dis


"一体、どんな話題で盛り上がっているのか……知りたいけれど、知りたくないような。"
"それでも確認せずにはいられず、ワタシはゆっくりと近づいていった。"
"すると、聞こえてきた内容は……"
voice "mobJyosiA0060"
mobA "「まあ、南の島でご一緒に、バカンスをお過ごしになられたんですか！」"


show char tsy01s2
with dis



voice "Sayuki0292"
s "「ええ……六夏さんと２人、手をつないで岩場を登ったりしました」"
voice "mobJyosiB0036"
mobB "「手を、つないで……ああ、どんな感じでしたか？」"


show char tsy02s2
with dis



voice "Sayuki0293"
s "「とても暖かい手でした……思わず、強く握り返してしまいました」"


show char trk05s2
with dis



voice "Rikka_0687"
rk "「さ……沙雪さん……」"


#allClear:
hide char trk05s2
#lastBG:
#scene bg bg04a
with dis


"なんか聞いていると、こっちまで恥ずかしくなってしまう。"
"沙雪さんはクラスメイトに聞かれるまま、あのバカンスでの話をしていた。"
voice "mobJyosiC0015"
mobC "「そ、それで……あの、き……キスとか、されたのですか？」"


show char tsy05s2
with dis



voice "Sayuki0294"
s "「キス……ですか。それは……」"


show char trk09s2
with dis



voice "Rikka_0688"
rk "「な、なに聞いてるのよぉ！！」"


#allClear:
hide char trk09s2
#lastBG:
#scene bg bg04a
with dis


"いけない、話がエスカレートしてしまった……とめなくちゃ！！"
"ワタシはあわてて、沙雪さんの周りのクラスメイトたちをかき分けた。"
"その途端、場がワッと沸く。"
voice "mobJyosiA0061"
mobA "「六夏さんの乱入よ。姫をお守りにきたのね」"


show char trk05s2
with dis



voice "Rikka_0689"
rk "「守るとか、そういうのじゃないけれど……うぅぅっ」"
"沙雪さんが小さい声で『キスは……しました』というのが、聞こえたような気がした。"


show char trk03s2
with dis



voice "Rikka_0690"
rk "「沙雪さん、何もそこまで言わなくてもいいのに……」"


#allClear:
hide char trk03s2
#lastBG:
#scene bg bg04a
with dis


"ワタシがやってきても、好奇心に満ちた乙女たちの質問責めは終わらない。"
voice "mobJyosiB0037"
mobB "「沙雪さん、キスより先はどうなんですか？」"


show char tsy03s2
with dis



voice "Sayuki0295"
s "「………………えっ？」"


show char trk04s2
with dis



voice "Rikka_0691"
rk "「な、なななななな……っ」"


#allClear:
hide char trk04s2
#lastBG:
#scene bg bg04a
with dis


"なんてことを、沙雪さんに聞くんですか！！"
"やっと沙雪さんの前までたどりついたワタシは、みんなの視線を遮るように彼女の前に立った。"


show char trk03s2
with dis



voice "Rikka_0692"
rk "「はぁ、はぁ……沙雪さん……」"


show char trk03s2 at left
show char tsy05s2 at right as r
with dis



voice "Sayuki0296"
s "「り……六夏……さん……」"
"沙雪さんの顔が、明らかに赤い。"
"みんながこんな質問をするから、困っているんだ。"
"自分で言うのもなんだけど、普段はヘタレなワタシ。"
"だけどここはきっぱり、言ってやらないと。"


show char trk01s2 at left
with dis



voice "Rikka_0693"
rk "「みっ、皆さん、これ以上の質問は、止めてくれませんか？」"
"ワタシのその声と同時に、沙雪さんも言葉を発していた。"
voice "Sayuki0297"
s "「キス以上は、まだ……プラトニックな関係です」"


show char trk05s2 at left
with dis



voice "Rikka_0694"
rk "「っ！！」"
"なんでそこまで言ってしまうの、沙雪さぁん……ぅぅ、しくしく……"
"真っ赤になるしかできないワタシを、みんなの羨望の眼差しが見つめていた。"
voice "mobJyosiA0062"
mobA "「まぁ、そうでしたの」"
voice "mobJyosiB0038"
mobB "「さすが、白雪を守る騎士ですわ」"
voice "mobJyosiC0016"
mobC "「本当に……ストイックでいらっしゃいますわね」"


show char tsy02s2 at right as r
with dis



voice "Sayuki0298"
s "「はい、六夏さんはとても素敵な方です」"
voice "Rikka_0695"
rk "「……ぁぁ……沙雪、さん……」"
"そんなことを間近で言われたらワタシ、卒倒してしまいそうです。"
voice "mobJyosiA0063"
mobA "「ですが沙雪さん。まだ……ということは……」"
voice "mobJyosiB0039"
mobB "「それは、もしかして……これから……」"


show char trk04s2 at left
with dis



voice "Rikka_0696"
rk "「ちょ、ちょっと待って、もう止めてっ！！」"
"思わず大声をあげたワタシを、沙雪さんがきょとんと見つめた。"
voice "Sayuki0299"
s "「あら、六夏さん……どうかしましたか？」"
"ニッコリ可憐に微笑む沙雪さんは、いつもの可愛い沙雪さんだけど。"
"でも今の彼女の行動が、言動が、ワタシには信じられなかった。"
"なんで聞かれたこと全部、何でも人に話してしまうの！？"


show char trk03s2 at left
with dis



voice "Rikka_0697"
rk "「はぁぁぁ……もう、疲れたかも……」"
"ワタシは戸惑いが隠せなくて、そのままうなだれてしまった。"


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


show char trk03s2
with dis



voice "Rikka_0698"
rk "「………………はぁ～」"


show char tri03s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0807"
r "「六夏、元気ないのね……夏バテでもした？」"
"今日はイベント実行委員の集まりがあって、ワタシはいつもの教室に向かっていた。"
"途中、リサ姉に会ったので、そのまま並んで歩く事にした。"
voice "Rikka_0699"
rk "「リサ姉……ちょっと、聞いてくれる？」"


show char tri01s2 at left
with dis



voice "Risa_0808"
r "「いいわよ。どうしたの？」"
"『興味あり』って感じで、リサ姉が食いついてくれた。"
voice "Rikka_0700"
rk "「あの、ですね……沙雪さんの事なんだけど……」"
voice "Risa_0809"
r "「やっぱり沙雪さんのことね。それでどうしたの、オノロケしたいの？」"
voice "Rikka_0701"
rk "「そうじゃなくて……ワタシと沙雪さんがお付き合いを始めたこと、もうクラスのみんなにバレてちゃってたみたいで……」"


show char tri04s2 at left
with dis



voice "Risa_0810"
r "「は……早いわね。誰が言っちゃったのかしら……」"
voice "Rikka_0702"
rk "「それが……沙雪さんが喋っちゃったみたいで」"
"それを聞いたリサ姉の顔が一瞬だけ、小さな驚きに揺らいだ。"
"そういうの、他人に話しちゃうようなキャラには見えないもんね、沙雪さんって。"
voice "Rikka_0703"
rk "「それで毎日、みんなに冷やかされちゃって……それが辛くて」"


show char tri01s2 at left
with dis



voice "Risa_0811"
r "「そうだったのね……ふーん」"
voice "Rikka_0704"
rk "「ふーんって……なんか、もう……」"
"真剣に話しているのに、リサ姉はどこか真面目に取り合ってくれない。"


show char trk07s2 at right as r
with dis



voice "Rikka_0705"
rk "「ひどいよ、リサ姉！　リサ姉だけはワタシの気持ち、わかってくれると思ったのに……」"
voice "Risa_0812"
r "「だって……あのね、六夏。もし沙雪さんが喋らなくても、２人の関係が進展したのは、周囲にはバレバレだったんじゃないの？」"


show char trk03s2 at right as r
with dis



voice "Rikka_0706"
rk "「えっ？　どうして？？」"
voice "Risa_0813"
r "「だって……２人が一緒にいるときの雰囲気でわかるもの。六夏って私と同じで、すぐに顔に出るし」"
voice "Rikka_0707"
rk "「そ、そんなぁ～」"
voice "Risa_0814"
r "「それと沙雪さんは、クラスメイトだけにそういう話をしているんじゃないと思うわ」"
voice "Rikka_0708"
rk "「それって、どういう……」"
voice "Risa_0815"
r "「ほら、こういうことよ」"
"リサ姉が立ち止まって教室を指差した。"
"今向かっている、イベント実行委員会の教室を。"
"もうメンバーがそろっているのか、外にいても、楽しそうな笑い声が響いてきた。"
voice "Risa_0816"
r "「さてと……開けるわよ」"
"リサ姉がワタシの顔を見つめながら、ドアをガラッと開け放った。"


#♀SE003
play sound "sound/SE003.ogg"


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


show char tsa01s2
with dis



voice "Sara_0153"
sr "「へぇ～、それで沙雪ちゃんは初めて、学食に行ったんだ」"


show char tsa01s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0300"
s "「はい。そこで２人、同じジュースを買いました。紙のパックに入ってるジュース、初めて頂きました♪」"


show char tsa02s2 at left
with dis



voice "Sara_0154"
sr "「そっか……なんか、仲良しって感じだねー♪」"

hide char tsa02s2 at left
hide char tsy02s2 at right as r
show char tsa02s2 at sleft as l
show char tsy02s2
show char tna01s2 at sright as sr
with dis



voice "Nanami0260"
n "「じゃあ、一緒に帰ったりはしているの？」"


show char tsy01s2
with dis



voice "Sayuki0301"
s "「車の迎えがない日は、たまに……」"
voice "Nanami0261"
n "「じゃあじゃあ、手を繋いだりして？？」"


show char tsy02s2
with dis



voice "Sayuki0302"
s "「そういう時もあります。先日も教室から抜け出す時、ギュッと強く握られてしまいました{image=image/exch001.png}」"


show char tyu01s2 at sleft as l
with dis



voice "Yuuna_0149"
y "「なんか初々しくていいわ……別れ際、キスをしたりはしないのかしら？」"


show char tsy01s2
with dis



voice "Sayuki0303"
s "「それは……まだ、ないです」"


#allClear:
hide char tyu01s2 at sleft as l
hide char tsy01s2
hide char tna01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char trk04s2
with dis



voice "Rikka_0709"
rk "「さ……沙雪さんっ！！」"
"彼女の名前を大声で呼んだワタシに、一斉に注目が集まった。"


show char tsy01s2
with dis



voice "Sayuki0304"
s "「あら、六夏さんもいらっしゃいました」"


show char tma01s2
with dis



voice "Mai_0237"
ma "「璃紗ちゃんも来たし……これで全員そろったね」"


#allClear:
hide char tma01s2
#lastBG:
#scene bg bg30a
with dis


"そこでようやく、話は終わって。"
"それぞれが席に着いたけど、ワタシはこの事態についていけず、その場から動けなかった。"


show char tsy03s2
with dis



voice "Sayuki0305"
s "「六夏さん……どうかしました？」"


show char trk03s2 at left
show char tsy03s2 at right as r
with dis



voice "Rikka_0710"
rk "「沙雪さんこそ……今、皆さんで何の話をしていたの？」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0306"
s "「私たちのことです。バカンスの後、どうなったのかを聞きたいと言われまして、そのご説明を」"
voice "Rikka_0711"
rk "「ここでも……なんだね、はぁ～」"
"クラスだけではなく、ここでも沙雪さんは、聞かれたことに全て答えてしまったようだった。"
hide char trk03s2 at left
hide char tsy01s2 at right as r
show char tsa02s2 at sleft as l
show char trk03s2
show char tsy01s2 at sright as sr
with dis



voice "Sara_0155"
sr "「若いっていいなぁ、新米カップルって感じでお似合いだね、２人とも」"
voice "Rikka_0712"
rk "「紗良さま……」"


show char tyu02s2 at sleft as l
show char trk03s2
show char tsy01s2 at sright as sr
with dis



voice "Yuuna_0150"
y "「ええ、本当に可愛いわね{image=image/exch001.png}」"


show char trk05s2
with dis



voice "Rikka_0713"
rk "「うううっ……」"
"みんなから冷やかされて、ワタシはたじたじになってしまう。"


#allClear:
hide char tyu02s2 at sleft as l
hide char trk05s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tmi01s2
with dis



voice "Miya_0413"
m "「……六夏さん」"


show char tmi01s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_0714"
rk "「み、美夜さま、何でしょう？」"
"美夜さまには、たくさん迷惑かけてるけど。"
"ワタシと沙雪さんの恋の進行具合など聞かされては、またご迷惑をかけてしまうのでは……"
"どうしても考えが、ネガティブな方に行ってしまう。"
voice "Rikka_0715"
rk "「あの……ワタシは……」"
voice "Miya_0414"
m "「あなたたち、まだプラトニックだそうね」"
voice "Rikka_0716"
rk "「……へっ？」"
"沙雪さん、そんな話もしてしまったのね。"
"気が重くなってうつむくと、美夜さまはそんなワタシの耳元で囁いた。"


show char tmi02s2 at left
with dis



voice "Miya_0415"
m "「六夏さん、もっとガンガン行かなくてはダメよ……んふふっ{image=image/exch001.png}」"


show char trk04s2 at right as r
with dis



voice "Rikka_0717"
rk "「ええええっ！？」"
"美夜さまは嬉しそうに、とんでもないことを言い放った。"


show char trk05s2 at right as r
with dis



voice "Rikka_0718"
rk "「あうっ……もぉ、なんというか……」"
"ワタシは恥ずかしくて、なんて答えていいのかわからなかった。"
"こんなのもう、耐えられないかも。"
"話題を変えよう、この話はもう、終わりにしてもらおう。"


#allClear:
hide char tmi02s2 at left
hide char trk05s2 at right as r
#lastBG:
#scene bg bg30a
show char trk03s2
with dis



voice "Rikka_0719"
rk "「あの、優菜さま、今日はどの仕事から始めればいいんですか？」"
"とにかくもう、実行委員の仕事を始めさせてもらおう。"


show char tyu01s2 at left
show char trk03s2 at right as r
with dis



voice "Yuuna_0151"
y "「そうねぇ……今日は休み明けの、ただの顔合わせだから。特に急ぎの仕事はないわね」"


show char trk04s2 at right as r
with dis



voice "Rikka_0720"
rk "「えええっ？」"
voice "Yuuna_0152"
y "「六夏ちゃんって、熱心なのね～」"


show char trk03s2 at right as r
with dis



voice "Rikka_0721"
rk "「いえ、そういうわけじゃ……」"


show char tyu02s2 at left
with dis



voice "Yuuna_0153"
y "「でも大丈夫よ。すぐに忙しくなるんだから……今日ぐらいはゆっくりしましょうね、六夏ちゃん♪」"
"ということは……"


#allClear:
hide char tyu02s2 at left
hide char trk03s2 at right as r
#lastBG:
#scene bg bg30a
show char tre01s2
with dis



voice "Reo_0185"
re "「今日はお茶とお菓子、食べ放題ってことよね？」"


show char tma01s2 at left
show char tre01s2 at right as r
with dis



voice "Mai_0238"
ma "「んー？　そうなるのかしら。そうね、お茶でもいれてゆっくりみんなでお話しましょうか」"


#allClear:
hide char tma01s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0154"
y "「ええ、そんな感じでいいと思うわ」"


show char tka01s2
with dis



voice "Kaede_0124"
k "「じゃあ私も、お茶入れるのを手伝います」"


show char tsa02s2
with dis



voice "Sara_0156"
sr "「お茶会だねー、楽しみ♪　あっ、お菓子どうしよう」"


show char tsa02s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0262"
n "「では今から、買いに行ってきましょうか」"


#allClear:
hide char tsa02s2 at left
hide char tna01s2 at right as r
#lastBG:
#scene bg bg30a
show char trk03s2
with dis



voice "Rikka_0722"
rk "「お、お茶会って……」"
"そんなまったりしたことをしていたら、またいつ、ワタシと沙雪さんの話題になるかも知れない。"
voice "Rikka_0723"
rk "「そ、それだけは……もう勘弁して……」"


show char trk03s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0307"
s "「六夏……さん？」"


show char trk01s2 at left
with dis



voice "Rikka_0724"
rk "「い、行こう、沙雪さん！　今日は特に、仕事もないみたいですし」"
voice "Sayuki0308"
s "「六夏さんが、そういうのでしたら……私はかまいませんが」"
"みんながお茶会で騒いでる隙に、強引だけどワタシは沙雪さんの手をとって、この場を去ることにした。"
"でも、そんな企みもあっさり、紗良さまに見つかってしまった。"


#allClear:
hide char trk01s2 at left
hide char tsy03s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa02s2
with dis



voice "Sara_0157"
sr "「キャー、六夏ちゃんが沙雪ちゃんの手を握って、出て行こうとしてる～」"


show char tma02s2
with dis



voice "Mai_0239"
ma "「ふふふっ、きっと２人きりになりたいのね。気持ちはわかるわ～」"


show char tyu02s2
with dis



voice "Yuuna_0155"
y "「まぁ、だから六夏ちゃん、仕事があるかって聞いてたのね。早く終わらせて、２人で帰りたかったのね」"


show char trk05s2
with dis



voice "Rikka_0725"
rk "「ち、ちが……くっ」"
"ここで反論したら、それはそれで話しがややこしくなるかもしれない。"
"もうこうなったら、なるようになれ、だ。"


show char trk02s2
with dis



voice "Rikka_0726"
rk "「あ、あは……はははっ、そう言われると、困っちゃいます」"


show char trk02s2 at left
show char tsy05s2 at right as r
with dis



"苦笑いを浮かべて沙雪さんの方を見ると、彼女はわかりやすいほどに、頬をぽわっと赤らめていた。"


show char trk03s2 at left
with dis



voice "Rikka_0727"
rk "「沙雪……さん？」"
voice "Sayuki0309"
s "「皆さんの前から、私を連れ出すなんて……私、強引で情熱的な六夏さんも嫌いではありません{image=image/exch001.png}」"


show char trk04s2 at left
with dis



voice "Rikka_0728"
rk "「ええええっ！？」"
"なんかまた、勘違いされちゃっているし。"


show char trk03s2 at left
with dis



"どうしてワタシ、こうなっちゃうんだろう……ぅぅぅっ。"


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
jump S033



