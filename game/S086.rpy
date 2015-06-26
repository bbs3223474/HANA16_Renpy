#「今度は七海の番ね……んふふっ」

label S086:
$ save_name = "◇今度は七海の番ね……んふふっ"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP18
play music "sound/BGM18.ogg"


voice "mobJyosiA0101"
mobA "「七海さん、ごきげんよう」"


show char tna02s2
with dis



voice "Nanami1151"
n "「ごきげんよう」"
"放課後……クラスメイトに挨拶をしながら、わたしはのんびりと歩いていた。"
voice "Nanami1152"
n "「今日も、とってもいい天気だなぁ～」"
"なんだかわたしの心と同じくらい、からっと晴れている。"


show char tna01s2
with dis



voice "Nanami1153"
n "「思えば……ここ最近、色々なことがあったなぁ」"
"お姉さまが環境整備委員会を引退して、わたしが委員長を引き継いで。"
"お姉さまが住み慣れた思い出の家を引き払うにあたって、２人でプチ同棲をして。"


show char tna02s2
with dis



voice "Nanami1154"
n "「お姉さまが、ウチの両親と食事会をしたと思ったら……うふふっ{image=image/exch001.png}」"
"両親に結婚の許しを貰うという、まさかの展開にも発展した。"
"今回もバタバタしたけれど、全て丸く収まって、一段落。"
voice "Nanami1155"
n "「これからも色々あるだろうけど……こんな風に、お姉さまと仲良くやっていきたいな」"
"お姉さまも、きっと同じ気持ちだと思う。"
"わたしの両親に向き合うお姉さまは、とても格好よかった。"
"真剣な話をしているのに、お姉さまにドキドキして、心臓がはちきれそうになっていたくらい。"


show char tna05s2
with dis



voice "Nanami1156"
n "「もうこれ以上、お姉さまを好きにさせないで欲しいわ」"
voice "Nanami1157"
n "「ああ、わたしのハートが持たないよぉ～」"
voice "mobJyosiB0062"
mobB "「七海さん……あの、どうかされました？」"


show char tna03s2
with dis



voice "Nanami1158"
n "「えっ？　あっ……」"
"目の前ではクラスメイトが、きょとんとした顔でわたしを見つめている。"
"いけないいけない、まだこの辺りには知り合いがいるのよね。"
"自分の世界に入ってしまうには、早すぎる。"


show char tna01s2
with dis



voice "Nanami1159"
n "「ご、ごきげんよう～」"
voice "mobJyosiB0063"
mobB "「ええ、ごきげんよう」"


#allClear:
hide char tna01s2
#lastBG:
#scene bg bg18a
with dis


"ぴゅっと、その場から逃げ出した。"
"お姉さまのことを考えると、本当に周りが見えなくなってしまうわ、わたしって。"
"それだけお姉さまのことで、わたしはいつも頭がいっぱいだから……"


show char tna01s2
with dis



voice "Nanami1160"
n "「また誰かに声をかけられないうちに、さっさとカフェに行こう」"
"わたしは、カフェまでの道を急いだ。"
"今日はこの後、恒例の２年生会があるのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**カフェ・昼
scene bg bg36a
with Dis



#mes on
#system on


"いつものカフェに早く着き過ぎたわたしは、席に座って、２人を待った。"


show char tna02s2
with dis



voice "Nanami1161"
n "「ふんふんふーん♪」"
"少し待つくらいなら、全然苦にはならない。"
"鼻歌を歌う程、今日のわたしは気分が良かった。"
voice "Nanami1162"
n "「えへへっ……あの時のことを思い返すと、頬が緩んじゃうなぁ」"
"両親と公認の仲になった。"
"それが嬉しくて、今はもう何をしていても楽しい気持ちになっていた。"
"やがてカフェのドアの入口が開き、２人がやってきた。"


show char tsa02s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_1863"
r "「お待たせ、七海さん、随分早いわね」"
voice "Sara_0282"
sr "「ほんとだ～、やっほー、七海ちゃん」"


#allClear:
hide char tsa02s2 at left
hide char tri01s2 at right as r
#lastBG:
#scene bg bg36a
show char tna01s2
with dis



voice "Nanami1163"
n "「璃紗さん、紗良さん、お疲れー」"


#allClear:
hide char tna01s2
#lastBG:
#scene bg bg36a
with dis


"それぞれ席に着いて、好きなメニューを注文する。"
"やがて注文したメニューが運ばれてくると、それぞれ飲み始めた。"
"わたしは、アイスミルクティー………………うん、美味しい\001"


show char tri01s2
with dis



voice "Risa_1864"
r "「七海さん……何か良いこと、あった？」"


show char tna03s2 at left
show char tri01s2 at right as r
with dis



voice "Nanami1164"
n "「えっ？　そう見えるかな？」"
voice "Risa_1865"
r "「誰が見てもそう思うわ。表情が、すっごく明るいもの」"


show char tna04s2 at left
with dis



voice "Nanami1165"
n "「ふええっ……そ、そぉ？」"

hide char tna04s2 at left
hide char tri01s2 at right as r
show char tsa02s2 at sleft as l
show char tna04s2
show char tri01s2 at sright as sr
with dis



voice "Sara_0283"
sr "「七海ちゃん、お肌つるつる……光り輝いてるよ」"
voice "Nanami1166"
n "「ひゃあっ」"
"突然、紗良さんに顔を掴まれて、頬を撫でられる。"
voice "Sara_0284"
sr "「あーん、滑らかで……まるで絹のようっ。羨ましい～っ」"


show char tna03s2
with dis



voice "Nanami1167"
n "「いやいや、紗良さんにはぜんっぜん、そんな……芸能人の足元にも及ばないよ」"
voice "Sara_0285"
sr "「そんなことないよ～。紗良よりずっとピチピチした肌だもん。美肌の秘訣教えてよぉ」"


show char tna01s2
with dis



voice "Nanami1168"
n "「いやぁ、それがね……」"
"わたしはつい、先日の食事会であったことの顛末を、２人に話してしまった。"


show char tri04s2 at sright as sr
with dis



voice "Risa_1866"
r "「ええっ……それ、本当！？」"
voice "Sara_0286"
sr "「キャ～っ！！　す、すごぉ～いっ！！　優菜さまカッコいい～！！」"
"２人は興奮を隠しきれない様子で、きゃあきゃあ騒ぐ。"


show char tna03s2
with dis



voice "Nanami1169"
n "「ちょ、ちょっと２人とも……声が大きいよぉ」"
"そわそわと辺りを見回すけれど……よかった、誰もこちらを気にしていない。"


show char tri03s2 at sright as sr
with dis



voice "Risa_1867"
r "「だだだだって、これが興奮しないではいられないわっ」"


show char tsa01s2 at sleft as l
with dis



voice "Sara_0287"
sr "「そうだよ～っ！！　なになに、これでもう将来は安泰って感じっ？」"
voice "Nanami1170"
n "「そ、そこまでは……」"


show char tri01s2 at sright as sr
with dis



voice "Risa_1868"
r "「それでも、それってとても、すごいことよ！　ねっ、紗良さん？」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0288"
sr "「だねだねっ♪　おめでとう、七海ちゃん」"


show char tri02s2 at sright as sr
with dis



voice "Risa_1869"
r "「おめでとう、七海さん」"
voice "Nanami1171"
n "「あっ……でも、まだ優菜さまのご両親は、このことは知らないかも……」"
"そうだ、すっかり舞い上がって忘れていた。"
"両親公認と言っても、それはあくまで、わたしの両親に限ってだということを。"
"ウチの両親は、割とあっさり認めてくれたけれど。"
"お姉さまのご両親は、とても素敵な方達なのだろうと、想像しているけれど……"
voice "Nanami1172"
n "「もしかしたら……結婚どころか、お付き合いも反対されるかもしれないわ」"
"だってお姉さまと比べたら、わたしはごく普通の庶民だもん。"
"お姉さまは可愛いと言ってくれるけど、顔だって普通だし、ちよっとぽっちゃりしているし……"
voice "Nanami1173"
n "「ううううっ、なんだか不安になってきたかも」"
voice "Sara_0289"
sr "「大丈夫だよ、七海ちゃん、いい子だもん」"
voice "Risa_1870"
r "「そうよ。環境整備委員の委員長を努めているくらい、優秀じゃない」"
voice "Nanami1174"
n "「でもぉ……」"


#allClear:
hide char tsa02s2 at sleft as l
hide char tna03s2
hide char tri02s2 at sright as sr
#lastBG:
#scene bg bg36a
with dis


"２人は、そう言ってくれるけれど。"
"わたしには、不安しかない。"
"今までの浮足立った気持ちが、急に盛り下がってしまった。"
"ああ、どうしよう、そんなことになったら……わたしは、どうすればいいの～！？"


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


"先日の２年生会で思ったそのことを、お姉さまに伝えてみると……"


show char tyu03s2
with dis



voice "Yuuna_0841"
y "「七海……心配性過ぎない？」"
"あっさりと、一蹴されてしまった。"


show char tyu03s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami1175"
n "「はぅぅ……そうですか？」"


show char tyu01s2 at left
with dis



voice "Yuuna_0842"
y "「そうよ。七海はなんでもマイナス方向に捉え過ぎなの。もうちょっとポジティブに物事を捉えなさい」"
voice "Nanami1176"
n "「いや……この間の食事会の時のお姉さまも、相当ネガティブ思考に走っていたと思うんですけれど」"


show char tyu09s2 at left
with dis



voice "Yuuna_0843"
y "「な～に、何か言った？」"
voice "Nanami1177"
n "「い、いえっ、なんでもないです！！」"


show char tyu01s2 at left
with dis



voice "Yuuna_0844"
y "「じゃあ次は七海が、ウチの両親に挨拶する番ね」"


show char tna04s2 at right as r
with dis



voice "Nanami1178"
n "「ひぃぃっ！！」"
"お姉さまのご両親にご挨拶だなんて……そんな難易度の高いミッション、わたしにクリアできるの！？"
"何しろお姉さまのお家は、とーっても格式高い、由緒正しきお家だし。"
"そんなセレブなご両親に、庶民のわたしが『お嬢さんをわたしにください』だなんて、切り出せるだろうか……？"


show char tna03s2 at right as r
with dis



voice "Nanami1179"
n "「考えただけで、身震いするよぉ……ぅぅっ」"


show char tyu02s2 at left
with dis



voice "Yuuna_0845"
y "「七海なら、絶対に大丈夫よ。それに万が一、ウチの両親が反対したら、勘当してあげるから{image=image/exch001.png}」"
voice "Nanami1180"
n "「お姉さま……そんな、勘当だなんて」"
"わたしはお姉さまのその発言を不安に思い、思わず制服の裾をきゅっと握り締めた。"
"お姉さまは、そのわたしの手を上からそっと握り締める。"
voice "Yuuna_0846"
y "「そのくらい、私は七海が大切なのよ……ふふっ、ちゅっ{image=image/exch001.png}」"
"いきなり不意打ちで、お姉さまのキスがきた。"


show char tna04s2 at right as r
with dis



voice "Nanami1181"
n "「おおおっ……お姉さまっ！！」"
voice "Yuuna_0847"
y "「まあ、七海ったら、いつまで経ってもウブなんだから……」"


show char tna05s2 at right as r
with dis



voice "Nanami1182"
n "「そ、それはぁ……そうですけどぉ……」"
voice "Yuuna_0848"
y "「あーんなところをこねこねしたり、指を入れちゃったり……色々しているのにね？」"


show char tna04s2 at right as r
with dis



voice "Nanami1183"
n "「お姉さまったらっ！？」"
voice "Yuuna_0849"
y "「お互いのキモチイイ場所なんかも、知り尽くしているのにね～」"


show char tna09s2 at right as r
with dis



voice "Nanami1184"
n "「あぁぁ、学校でエッチなことを言うのは禁止ですっ、お口チャックですっ！！」"
"わたしはエロいことばかりを口にするお姉さまの口を、思わず両手で押さえた。"
voice "Yuuna_0850"
y "「もがっ……もがもがもが……」"


show char tna08s2 at right as r
with dis



voice "Nanami1185"
n "「エロ発言……もうしませんか？」"


show char tyu01s2 at left
with dis



voice "Yuuna_0851"
y "「もがっ……コクコクっ」"


show char tna01s2 at right as r
with dis



voice "Nanami1186"
n "「じゃあ、離してあげます」"
"わたしが手を外すと、自由になったお姉さまの口は、すーはーすーはーと思いっきり息をした。"
voice "Yuuna_0852"
y "「はぁはぁ……強くなったわね、七海。出会った時に比べたら、別人のようだわ」"
voice "Nanami1187"
n "「それはそーですっ。お姉さまのようなエロ乙女と付き合っていたら、たくましくもなりますよっ」"


show char tyu02s2 at left
with dis



voice "Yuuna_0853"
y "「うふふ……まあウブな七海も、たくましい七海も、イヤらしい七海も、ぜーんぶひっくるめて好きなんだけど{image=image/exch001.png}」"
"お姉さまのにこやかな顔に、わたしも自然と笑みが生まれた。"


show char tna02s2 at right as r
with dis



voice "Nanami1188"
n "「わたしも、凛々しいお姉さまも、この間のちょっとおどおどしたお姉さまも、エロ乙女なお姉さまも、大好きですっ{image=image/exch001.png}」"
voice "Yuuna_0854"
y "「うふふ……っ」"
voice "Nanami1189"
n "「あはははっ」"
"笑い合いながら、お姉さまがわたしの頬を撫でる。"
voice "Yuuna_0855"
y "「ね、七海……もう一回、キスしてもいい？」"
voice "Nanami1190"
n "「どうぞ、何度でも。わたしの唇は、お姉さまのものですっ」"
voice "Yuuna_0856"
y "「私の心も体だって全部、七海のものよ……返品は永久に不可能なんだから」"
"美しい顔が近付いて、小鳥のような口づけが降ってくる。"
voice "Nanami1191"
n "「もちろん、大事にします……だからわたしのことも全部、貰って下さいね、お姉さま{image=image/exch001.png}」"


#※EV053
#allClear:
hide char tyu02s2 at left
hide char tna02s2 at right as r
#lastBG:
#scene bg bg30a
scene bg EV53
with Dis



"今度はわたしの方から、少し高い位置にあるピンクの唇にキスをした。"
voice "Yuuna_0857"
y "「髪の毛一本から、足の指の先まで、一生愛してあげるから、覚悟してね……ちゅっ{image=image/exch001.png}」"
"更にお姉さまから、キスが落ちてくる。"
voice "Nanami1192"
n "「んちゅ……望むところです。わたしなんて、死んでもお姉さまのことを離さないんですから……ん、はぅん……んちゅ{image=image/exch001.png}」"


#※EV053P1
scene bg EV53p1
with Dis



"わたしも負けじと、またキスを返してしまった……熱く濃厚なキスを。"
voice "Yuuna_0858"
y "「んちゅ、ぅぅん……七海ぃ……」"
voice "Nanami1193"
n "「ぁぁ……優菜お姉さま……」"
"激しいキスはやがて、もっと深いものに変わり……"
voice "Yuuna_0859"
y "「ちゅぱ、んじゅ……ぁぁ、愛しているわ、七海{image=image/exch001.png}」"
"こうして愛の言葉を囁かれたり、キスをして貰ったりするのは、すごく嬉しい。"
voice "Nanami1194"
n "「わたしもいっぱい、愛しています……優菜お姉さま{image=image/exch001.png}」"
"これからもずっとずっと、わたしはお姉さまを愛していきたい。"
"そしてお姉さまに愛され続けたいと、強く願うのでした。"

"七海＆優菜　ＨＡＰＰＹ　ＥＮＤ{image=image/exch001.png}"


#mes off
#mes clear
#system off


#wipecancel disabled
#waitcancel disabled
#log off


scene image "image/end03.png"
with Dis


pause 5


#log on
#waitcancel enabled
#wipecancel enabled


#**暗転
scene black
with Dis


#♂MS
stop music fadeout 1


#//END
#set f2 3
jump staffroll



