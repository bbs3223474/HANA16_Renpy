#「お茶会を見つめる、謎の集団」

label S104:
$ save_name = "◇お茶会を見つめる、謎の集団"


#**旧校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


#//SE：学校チャイム音
#♀SE001
play sound "sound/SE001.ogg"


show char tre01s2
with dis



voice "Reo_0237"
re "「ねぇ麻衣ー、早く早くー」"


show char tma01s2 at left
show char tre01s2 at right as r
with dis



voice "Mai_0362"
ma "「わかってるわよ、玲緒、ちょっと待ちなさいよ」"
"授業終了のチャイムが鳴った途端、一目散に教室を飛び出していった、玲緒。"
"廊下は走っちゃダメよと、何度も言い聞かせているのに……そんなルール、あの暴走特急の玲緒には通用しないみたい。"
"甘えん坊で、わがままで……だけど、実は寂しがりなわたしの恋人。"
"以前ならわたし以外には懐くことはなかったけれど。"
"最近は友達ができて、彼女たちとの触れ合いが嬉しくて、仕方ないみたい。"
voice "Mai_0363"
ma "「……まあ、本人に聞いてみても、絶対に認めないだろうけれどねー」"


show char tre08s2 at right as r
with dis



voice "Reo_0238"
re "「もぉ、麻衣遅いー！　エリスたちに先、越されるじゃないっ」"
voice "Mai_0364"
ma "「別にいいじゃない、一緒にお茶会するんだから」"
voice "Reo_0239"
re "「だめよ、ワタシの方が先に着いてなくちゃ……これはね、戦いなんだから」"
voice "Mai_0365"
ma "「はいはい、エリスさま相手だと、なんでも戦いにしちゃうんだからねぇ、玲緒は」"


show char tre03s2 at right as r
with dis



voice "Reo_0240"
re "「麻衣……今、なんか言った？」"
voice "Mai_0366"
ma "「そんなに遅い遅い言うなら、わたしの荷物、少し持ってくれてもいいんじゃないかしら」"


show char tre01s2 at right as r
with dis



voice "Reo_0241"
re "「………………」"
"お茶会で、みんなで食べるお菓子の袋を両手いっぱいに抱えているわたしと違って、玲緒は完全手ぶら状態。"
"玲緒はじいっと、わたしを見つめて……"
voice "Reo_0242"
re "「いいから麻衣、急いで行くわよ」"
"そのまま、また走り出した。"
voice "Mai_0367"
ma "「……わたしのを持ってくれる気は、まーったくないのね」"
voice "Reo_0243"
re "「だって麻衣の方が、ワタシより足が速いでしょ」"
voice "Mai_0368"
ma "「そんなに違わないと思うけれど……どういう根拠で、わたしの方が速いと思うのよ？」"


show char tre08s2 at right as r
with dis



voice "Reo_0244"
re "「だって……ワタシがどれだけ必死で逃げても、いつも麻衣が追いついてきて、捕まえるでしょ！」"
voice "Mai_0369"
ma "「……まあ、そうね。いつもわたしが勝っているわね」"


show char tre01s2 at right as r
with dis



voice "Reo_0245"
re "「ほらね、だから麻衣が荷物持つのよ。これくらいのハンデで、ちょうどいいのよ」"
voice "Mai_0370"
ma "「あー、はいはい、そうですか。ハンデ持ちますよ」"
"まったく……後で覚えてらっしゃい、玲緒。"
"こうして玲緒はハンデなしで、わたしより先に目的地に向かっていく。"


show char tre02s2 at right as r
with dis



voice "Reo_0246"
re "「ふふふっ、やっぱりエリス、まだ来てないみたいね……ワタシのかーちーっ♪」"
voice "Mai_0371"
ma "「もう、玲緒ったら……」"


#allClear:
hide char tma01s2 at left
hide char tre02s2 at right as r
#lastBG:
#scene bg bg05a
with dis


"中庭を指さしながら、玲緒が笑う。"
"その愛らしい笑顔に免じて、今日のわがままも許してあげようかしら。"
"なんだかんだ言いながら、わたしはこうして玲緒といるのが、楽しくて仕方ないのだから。"


#**中庭・昼
scene bg bg21a
with Dis



"放課後、玲緒の発案で、お菓子パーティをエリスさまたちと開くことになったけれど。"
"エリスさまたちはまだ、待ち合わせの中庭には来ていなかった。"


show char tre02s2
with dis



voice "Reo_0247"
re "「ふふふっ、やったわ……ワタシの勝ちね、エリスは遅刻だわ」"


show char tma03s2 at left
show char tre02s2 at right as r
with dis



voice "Mai_0372"
ma "「はぁ、ふうーっ、あれだけ急いでくれば、先に到着して当たり前よ……なんだか汗、かいちゃったわ」"
"南の島で過ごした夏休みが終わって、しばらく経ったけれど。"
"まだ外に出れば、日差しは容赦なくガンガン、照りつけてくる。"
"木陰の下にある野外テーブルを場所取りして、とりあえず先に、持ってきたお菓子を並べ始めた。"


show char tma01s2 at left
with dis



voice "Mai_0373"
ma "「ねっ、玲緒も手伝ってくれる？」"
voice "Reo_0248"
re "「はーい」"
voice "Mai_0374"
ma "「良いお返事ね。でも、つまみ食いは絶対だめよ」"


show char tre03s2 at right as r
with dis



voice "Reo_0249"
re "「りょ、りょうかい……でも、味見ならいいわよね？」"
voice "Mai_0375"
ma "「だぁめ」"


show char tre09s2 at right as r
with dis



voice "Reo_0250"
re "「もぉ、麻衣のけちっ！！」"


#allClear:
hide char tma01s2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg21a
with dis


"お茶は雫さまが用意をしてくださる予定だから、わたしたちはお菓子を出しちゃえば、それで終わり。"


show char tma02s2
with dis



voice "Mai_0376"
ma "「ふぅ……うん、これでいいわね」"


show char tma02s2 at left
show char tre01s2 at right as r
with dis



voice "Reo_0251"
re "「ごくっ……本当に美味しそうな、お菓子ばかり……じゅる」"


show char tma01s2 at left
with dis



voice "Mai_0377"
ma "「そうね……」"
"玲緒はどうにも落ち着きがなく、お菓子の方に見入っていた。"
"今すぐにでも、食べたいみたいね……本当にお菓子好きなんだから。"


show char tre03s2 at right as r
with dis



voice "Reo_0252"
re "「ねぇ、麻衣……」"


show char tma08s2 at left
with dis



voice "Mai_0378"
ma "「だめよ、食べちゃだめ」"
voice "Reo_0253"
re "「じゃあ、代わりにジュース飲んでいい？」"


show char tma03s2 at left
with dis



voice "Mai_0379"
ma "「雫さまがお茶を持ってくるまで待てないの」"
voice "Reo_0254"
re "「なんだか、のど乾いちゃったのよ……麻衣だって、汗かいたって言ってたじゃない」"
voice "Mai_0380"
ma "「それは、そうだけど……」"
voice "Reo_0255"
re "「こまめに水分取らないと、熱中症になるって、いつも麻衣が言ってるのにっ」"


#★★★選択肢　ここから


voice "Mai_0381"
ma "「まったく、玲緒ったら……へりくつばかり」"
"こんなときは……"


#++選択肢（１）
#１．『水を飲んでくるように言う』×
#２．『ジュースを飲ませてあげる』○
menu:
 "水を飲んでくるように言う":
  jump select19_1
 "ジュースを飲ませてあげる":
  jump select19_2



#１．『水を飲んでくるように言う』
label select19_1:


show char tma01s2 at left
with dis



voice "Mai_0382"
ma "「そんなに喉が渇いたなら、水のみ場でお水飲んでいらっしゃい」"


show char tre08s2 at right as r
with dis



voice "Reo_0256"
re "「ワタシ、買ってきた水以外は飲まないわ。家でも水道水は飲まないし」"


show char tma03s2 at left
with dis



voice "Mai_0383"
ma "「こ、この贅沢もの……」"


show char tma03s2 at left
with dis



voice "Reo_0257"
re "「麻衣のケチ、ワタシ、ジュースがいいのっ！」"


show char tma08s2 at left
with dis



voice "Mai_0384"
ma "「誰がケチよ！？　まったく……」"
"ここで言い争っても、玲緒は怒るかスネるだけよね……まあ、仕方ないけれどジュース、飲ませておきましょうか。"


jump select19_end


#２．『ジュースを飲ませてあげる』
label select19_2:


voice "Mai_0385"
ma "「はいはい、わかったわよ……お菓子はダメだけど、ジュースだけならいいわよ」"
"もう、仕方ないわね。"
"ちょっと甘いかもしれないけれど、喉が渇いているって言うんだもの。"
"やっぱり放っておけないわ。"
"先輩たちが来る前に、お茶会を始めるわけにはいかないけど、ジュースくらいならいいわよね。"


#set f1 f1+1


#++選択肢終了
#★★★選択肢　ここまで
label select19_end:


"ペットボトルのキャップを開けて、玲緒に手渡してあげた。"


show char tre02s2 at right as r
with dis



voice "Reo_0258"
re "「いただきまーす、んっ……ごくごく、美味しい～♪」"


show char tma01s2 at left
with dis



voice "Mai_0386"
ma "「本当に、幸せそうな顔しちゃって……玲緒ったら」"
"ジュースを美味しそうに飲む、玲緒を見ていると。"
"なんだかちょっと、イタズラしたくなってくる。"
voice "Mai_0387"
ma "「ねー、玲緒『熱中症』って、ゆっくり言ってみて」"


show char tre03s2 at right as r
with dis



voice "Reo_0259"
re "「ねっ、ちゅう、しょうー？」"


show char tma11s2 at left
with dis



voice "Mai_0388"
ma "「……はい、ちゅっ{image=image/exch001.png}」"


show char tre09s2 at right as r
with dis



voice "Reo_0260"
re "「ま、麻衣～、どうしてこんなとこで、キスするのよーっ！！」"


show char tma02s2 at left
with dis



voice "Mai_0389"
ma "「だって……今玲緒、自分で『ねぇ、チューしよう』って言ったじゃない」"


show char tre07s2 at right as r
with dis



voice "Reo_0261"
re "「ううっ……ち、ちがうもん！　麻衣、だましたわねっ」"
voice "Mai_0390"
ma "「まさか、玲緒からチューしようなんて言ってくれるなんて……んふふっ{image=image/exch001.png}」"


show char tre09s2 at right as r
with dis



voice "Reo_0262"
re "「ちちちっ、違うーっ！！」"


show char ter02f2 at left
show char tsi02f2 at right as r
with dis



voice "Erisu_0131"
e "「本当に玲緒ったら、大胆なんだね～♪」"
voice "Sizuku0103"
sk "「ええ……とても仲がよろしいですね」"


#allClear:
hide char ter02f2 at left
hide char tsi02f2 at right as r
#lastBG:
#scene bg bg21a
show char tre04s2
with dis



voice "Reo_0263"
re "「えっ、エリス！？　それに、霧島雫も……今の、見てたのね！？」"


show char tre04s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0132"
e "「もう、ばっちり見ちゃったよぉー、玲緒ったらエッチだね」"


show char tre09s2 at left
with dis



voice "Reo_0264"
re "「ワタシ、そんなんじゃないもんっ！」"


#allClear:
hide char tre09s2 at left
hide char ter01f2 at right as r
#lastBG:
#scene bg bg21a
with dis


"エリスさまに、思いっきりからかわれる玲緒。"
"でも怒りながらも、お待ちかねの２人の登場に、少し口が緩んでいた。"


show char tsi01f2
with dis



voice "Sizuku0104"
sk "「ごきげんよう、麻衣さん」"


show char tma01s2 at left
show char tsi01f2 at right as r
with dis



voice "Mai_0391"
ma "「ごきげんよう、雫さま。こちらにどうぞ」"


show char tsi02f2 at right as r
with dis



voice "Sizuku0105"
sk "「はい、ありがとうございます。これ、冷やし抹茶です」"


show char tma02s2 at left
with dis



voice "Mai_0392"
ma "「わぁ、美味しそうですね！」"
"雫さまから受け取ったボトルの中には、よく冷えた抹茶がたっぷりと入っていた。"


show char tsi01f2 at right as r
with dis



voice "Sizuku0106"
sk "「エリスの部屋の台所を借りて、作ってきたので、まだ入れたてですよ」"


show char tma01s2 at left
with dis



voice "Mai_0393"
ma "「それじゃあ、さっそくお茶会をはじめましょう。玲緒、こっちに……」"


#allClear:
hide char tma01s2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg21a
show char ter02f2
with dis



voice "Erisu_0133"
e "「わぁ～、美味しそうなお菓子がいっぱいだね」"


show char tre08s2 at left
show char ter02f2 at right as r
with dis



voice "Reo_0265"
re "「ふ、ふんっ。エリスは遅刻した罰で、お菓子抜きなんだから」"

hide char tre08s2 at left
hide char ter02f2 at right as r
show char tma03s2 at sleft as l
show char tre08s2
show char ter02f2 at sright as sr
with dis



voice "Mai_0394"
ma "「あなたはまた、何勝手なことを……」"
voice "Erisu_0134"
e "「いいよ、お菓子抜きでも{image=image/exch001.png}」"


show char tre03s2
with dis



voice "Reo_0266"
re "「えっ？　いいの」"
voice "Erisu_0135"
e "「そんなイジワルな玲緒には、シズクが焼いてきたクッキーあげないから」"
voice "Reo_0267"
re "「えっ……クッキーって……」"
voice "Erisu_0136"
e "「いいのかな？　ほらこれ、美味しそうでしょう～」"
voice "Reo_0268"
re "「うっ……いいもん、ワタシいらないもん」"


show char tma08s2 at sleft as l
with dis



voice "Mai_0395"
ma "「れーお、みんなで食べるために買ったお菓子よ。だから、イジワルしないの」"


show char tre03s2 at sleft as l
show char ter02f2
show char tsi08f2 at sright as sr
with dis



voice "Sizuku0107"
sk "「エリスもですよ。わたくしの作ったお菓子なら、いくらでもありますから、玲緒さんにもあげてください」"


#allClear:
hide char tre03s2 at sleft as l
hide char ter02f2
hide char tsi08f2 at sright as sr
#lastBG:
#scene bg bg21a
show char ter02f2
with dis



voice "Erisu_0137"
e "「ふふふっ、冗談に決まってるじゃない{image=image/exch001.png}」"


show char tre03s2 at left
show char ter02f2 at right as r
with dis



voice "Reo_0269"
re "「……えっ？」"
voice "Erisu_0138"
e "「シズクのお手製クッキー、たくさん食べてね。ワタシも手伝ったんだよ……玲緒に食べてもらいたくて」"


show char tre08s2 at left
with dis



voice "Reo_0270"
re "「エリス……ふ、ふん、わかったわ、食べてあげるわよ」"


show char ter01f2 at right as r
with dis



voice "Erisu_0139"
e "「ちなみにワタシが作ったのは、これとこれよ」"


show char tre03s2 at left
with dis



voice "Reo_0271"
re "「なにこれ？　ひょうたん形、ずいぶん小さいけど……ぱくぱく」"
voice "Erisu_0140"
e "「どう、美味しい？」"
voice "Reo_0272"
re "「……おっ」"
voice "Erisu_0141"
e "「お？」"


show char tre05s2 at left
with dis



voice "Reo_0273"
re "「まぁ、不味くはないわね」"


#allClear:
hide char tre05s2 at left
hide char ter01f2 at right as r
#lastBG:
#scene bg bg21a
with dis


"玲緒ったら、美味しいって言いかけてたくせに、言い直したりして。"
"本当に、素直じゃないんだから。"


show char tma01s2
with dis



voice "Mai_0396"
ma "「エリスさま、わたしも頂いていいですか？」"


show char tma01s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0142"
e "「どうぞ。シズクが作ったのは、この星形のやつだよ」"


show char tma02s2 at left
with dis



voice "Mai_0397"
ma "「これ、とっても可愛いですね」"

hide char tma02s2 at left
hide char ter01f2 at right as r
show char tma02s2 at sleft as l
show char ter01f2
show char tsi02f2 at sright as sr
with dis



voice "Sizuku0108"
sk "「ありがとうございます」"


#allClear:
hide char tma02s2 at sleft as l
hide char ter01f2
hide char tsi02f2 at sright as sr
#lastBG:
#scene bg bg21a
with dis


"星形のクッキーを、ひとつ頂く。"
"うん……甘すぎなくて、ちょうどいいお味。"
"星形クッキーの中に、何個か玲緒がひょうたん型と言っていた、エリスさまのクッキーが紛れている。"
"星と比べると、ずいぶん小さいわね。"


show char tma01s2
with dis



voice "Mai_0398"
ma "「エリスさま、こっちの型は小さいんですね」"


show char tma01s2 at left
show char ter02f2 at right as r
with dis



voice "Erisu_0143"
e "「そうだよ。だってそれは、玲緒のおっぱい型だからね」"


#allClear:
hide char tma01s2 at left
hide char ter02f2 at right as r
#lastBG:
#scene bg bg21a
show char tre04s2
with dis



voice "Reo_0274"
re "「なっ！！」"


show char tma02s2 at left
show char tre04s2 at right as r
with dis



voice "Mai_0399"
ma "「あーあ、なるほどなるほど」"


show char tre08s2 at right as r
with dis



voice "Reo_0275"
re "「なっ、なるほどじゃないわよ、なんでそんな型のクッキー、作るのよぉ」"

hide char tma02s2 at left
hide char tre08s2 at right as r
show char tma02s2 at sleft as l
show char tre08s2
show char ter01f2 at sright as sr
with dis



voice "Erisu_0144"
e "「玲緒のクッキー作ったら、玲緒が喜ぶかと思って」"


show char tre09s2
with dis



voice "Reo_0276"
re "「こんなんじゃ、喜ばないわよーっ！！」"


#allClear:
hide char tma02s2 at sleft as l
hide char tre09s2
hide char ter01f2 at sright as sr
#lastBG:
#scene bg bg21a
with dis


"ドタバタ騒ぎを始める、玲緒とエリスさま。"
"それを見つめる、わたしと雫さま。"


show char tma02s2
with dis



voice "Mai_0400"
ma "「ふふっ、なんだか……いつもの日常ですね」"


show char tma02s2 at left
show char tsi01f2 at right as r
with dis



voice "Sizuku0109"
sk "「そうですね。では、抹茶をどうぞ」"


show char tma01s2 at left
with dis



voice "Mai_0401"
ma "「はい、頂きます」"


#allClear:
hide char tma01s2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg21a
with dis


"しばらくすると、騒ぎ疲れた２人も雫さまに抹茶を頂いて。"
"後はのんびりとした、お茶会が始まった。"


#※EV067
scene bg EV67
with Dis



voice "Erisu_0145"
e "「おーっ、デリシャス！　このお菓子初めて食べるわ」"
voice "Sizuku0110"
sk "「ええ、とても美味しいですね」"
voice "Reo_0277"
re "「ふふふっ、わざわざデパ地下で買ってきたんだからねっ」"
voice "Mai_0402"
ma "「買いに行ったのは、わたしだけどね」"
voice "Erisu_0146"
e "「やっぱり、そんなことだと思ったよ」"
voice "Reo_0278"
re "「ワ、ワタシはその間、留守を守っていたのよ……しっかりと」"
voice "Mai_0403"
ma "「そうね、まさに自宅警備員ね～」"
voice "Reo_0279"
re "「そうそう、えっへん♪」"
voice "Erisu_0147"
e "「それ、ぜんぜん誉められていないよ、玲緒」"
voice "Reo_0280"
re "「えええっ！？」"
voice "Sizuku0111a"
sk "「あらっ、あそこにいるのは……」"
"向こうの方から、見覚えのある学生が一人でこっちに歩いてきた。"
voice "Mai_0404"
ma "「美夜ちゃんだわ。ねぇ、美夜ちゃ～ん」"
"手を振ると、美夜ちゃんも気づいて、こちらへ来る。"
voice "Mai_0405"
ma "「ごきげんよう、美夜ちゃん。こんなところでどうしたの？」"
voice "Miya_1065"
m "「今、ちょうど璃紗と、追いかけっこしている最中なんです」"
"追いかけっこ？"
"そういえば璃紗ちゃんって、よく中庭で美夜ちゃんを探し回ってる姿を目にするけれど。"
"あれって……本当に、追いかけっこなのかしら？？"
voice "Reo_0281"
re "「綾瀬美夜、よく来たわね。このお菓子、知ってるかしら？」"
"まるで玲緒が挑発するように、美夜ちゃんにそう言った。"
"玲緒の目が自慢げに、きらりと光る。"
"それはさっき、エリスさまたちも大絶賛していたお菓子だった。"
voice "Miya_1066"
m "「こ、これは……地域限定でありながらも、その形の崩れ易さから、お取り寄せさえしていない、幻のあのスイーツ！？」"
"気のせいか、美夜ちゃんの目も光っている。"
voice "Miya_1067"
m "「玲緒さま、一体どこで、これを？」"
voice "Reo_0282"
re "「あそこのデパ地下よ。今だけ出店しているの……良かったら、お一つどーぞ」"
voice "Miya_1068"
m "「ええ、ありがたくいただきます……ぱくっ」"
voice "Reo_0283"
re "「どう……かしら？」"
voice "Miya_1069"
m "「ああ……とても美味しい。ありがとうございます」"
voice "Reo_0284"
re "「うんうん、そうでしょうそうでしょう」"
"これまた自慢げに、そしてどこか偉そうに、玲緒が美夜ちゃんに笑いかける。"
"すると、美夜ちゃんは……"
voice "Miya_1070"
m "「ではわたくしも、これからこれを買いに行ってきます。璃紗にも食べさせたいので……ではっ！」"
voice "Reo_0285"
re "「いってらっしゃ……きゃああああっ！？」"

#//SE：ギャグ的に、美夜がダッシュで走り去る音（バビューン、的な）
#♀SE047
play sound "sound/SE047.ogg"


"びゅっと、大きな風が起きたかと思ったら、美夜ちゃんの姿はこの場から消えていた。"
voice "Sizuku0112"
sk "「すごいです……まるで風に乗って、消えていったみたいですね」"
voice "Mai_0406"
ma "「本当ね……あっちは例のデパートがある方角。よほど玲緒のあげたスイーツが気に入ったのね」"
"美夜ちゃんの話からすると、すごく珍しいお菓子だったみたいだし。"
"確か、わたしが買いに行った時も、個数制限されていたし。"
"それだけ、人気のあるやつだったのかもしれないわ。"
"そんな貴重なスイーツを、美夜ちゃんにあっさりあげちゃうなんて……玲緒も本当に、成長したのね。"
voice "Erisu_0148"
e "「後輩に優しくするのは良いことだよ、玲緒」"
"エリスさまも同じことを感じているみたいで、玲緒を誉めてくれた。"
voice "Reo_0286"
re "「うぅぅっ、だったらエリスももっと、後輩のワタシに優しくしなさいよねっ」"
voice "Erisu_0149"
e "「えー、優しくしているじゃない。愛しい玲緒のことを思いながら、この『ちんまいクッキー』を作ったのよ」"
voice "Reo_0287"
re "「ちがーう！　クッキーを作ったのは霧島雫で、エリスはそれをふざけてヘンな形にしただけじゃないっ！」"
voice "Erisu_0150"
e "「そうかなー」"
voice "Reo_0288"
re "「そうよっ」"
voice "Erisu_0151"
e "「大丈夫よ。大人になれば玲緒のおっぱいも大きくなるから、そしたら今度は、大きなクッキー型を用意してあげるわ」"
voice "Reo_0289"
re "「むきききーっ！」"
voice "Erisu_0152"
e "「また怒ってる……妹みたく可愛がってあげているのに」"
"そうね。"
"エリスさまの玲緒に対する愛情って、まさに姉妹って感じよね。"
voice "Sizuku0113"
sk "「んっ……」"
voice "Mai_0407"
ma "「雫さま……どうかしました？」"
voice "Sizuku0114"
sk "「いえ、今どこからか、じっと見つめられていたような気がしまして」"
voice "Mai_0408"
ma "「そう……ですか？」"
"言われて、あたりを見回してみる。"
"でも、誰もいなかった。"
voice "Mai_0409"
ma "「特に誰もいないようですが……」"
voice "Sizuku0115"
sk "「そうでしたか……うーん」"
voice "Mai_0410"
ma "「雫さまたちは、ミカ女にいた頃から人気がありましたから。在校生の誰かが通りかかって、たまたまこっちを見ていただけじゃないですか？」"
voice "Sizuku0116"
sk "「はぁ……それならば、良いのですが……」"


#**青空
scene bg bg42a
with Dis



"そしてわたしたちは何事もなかったかのように、そのままお茶会を続けた。"
"雫さまの言った通りに、こちらをじっと見つめている一団がいたことに、気づきもせず……"


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
jump S105



