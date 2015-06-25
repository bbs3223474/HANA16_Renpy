#「天国から、地獄へ」

label S046:
$ save_name = "◇天国から、地獄へ"


#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#♂MP16
play music "sound/BGM16.ogg"


show char trk03s2
with dis



voice "Rikka_1253"
rk "「………………」"
"こんなにも、近くにいるのに。"
"沙雪さんの存在は、夢でも妄想でもなかったのに。"
"ワタシは同じ教室内にいる彼女に、声をかけられずにいた。"
"翌日、思わず彼女を問い詰めてしまった時。"
"とても辛そうな沙雪さんをより、悲しませてしまったから……"


#（ちょっと回想）
#**並木道・昼
scene bg bg18a
with lr


show char trk08s2
with dis



voice "Rikka_1254"
rk "「沙雪さん……昨日の『最後かも』って一体、どういうことなんですか！？」"


show char trk08s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0666"
s "「それは……ごめんなさい。私の、私自身の問題なんです」"


show char trk03s2 at left
with dis



voice "Rikka_1255"
rk "「それじゃ納得できません、もっとちゃんと、分かるように……」"
voice "Sayuki0667"
s "「………………」"
"あまりに焦ってしまい、キツく問い詰める様な口調になった事は、自覚していた。"
"だけど、止められなかった。"
"だって……昨日は、あんなに激しく愛を確かめ合っていたのに。"
"愛し合えた喜びに奮えていたのは、ワタシだけだったのだろうか。"
"そんなひとりよがり……惨め過ぎるよ。"
voice "Sayuki0668"
s "「六夏、さん……」"
voice "Rikka_1256"
rk "「沙雪、さん……」"
"見つめ合う事……数秒。"


show char tsy06s2 at right as r
with dis



"やがて沙雪さんの瞳に涙が溜まり、ポトリと零れ落ちた。"
voice "Rikka_1257"
rk "「さ、沙雪さん……すみません、責めるつもりは無かったんですけれど……」"
"慌てるワタシに、沙雪さんは涙を拭った。"
voice "Sayuki0669"
s "「本当に、ごめんなさい。でも、こればかりは……自分で解決しないと、ダメな事なのです。ですから、しばらく会えません」"
voice "Rikka_1258"
rk "「会えないって……そんな……」"
voice "Sayuki0670"
s "「私を愛して下さって、本当にありがとうございます……ぅぅっ」"


hide char tsy06s2 at right as r
show char trk04s2 at left
with dis


voice "Rikka_1259"
rk "「あっ……」"
"沙雪さんは、ワタシに謝って、走り去っていった。"
"ワタシはその姿を追えずに、ただ見送ることしかできなかった……"

#（回想終了）

#**新校舎教室・昼
scene bg bg04a
with rr


show char trk03s2
with dis



voice "Rikka_1260"
rk "「沙雪さん……どうして謝るの？　一体何が、彼女に起こっているの？」"
"しばらく会えないことに対して、謝ったのか。"
"それとも……もうワタシと、別れたいという意味なのか。"
voice "Rikka_1261"
rk "「やだ、イヤだよ、そんなの……でも、どうすれば……ぅぅっ」"
"混乱したワタシの頭の中はグルグルして、軽い吐き気がしてきた。"
"沙雪さんと心も体も結ばれて、全てがわかり合えたと思っていたのに。"
"沙雪さんの、あの態度……すっかりワタシは困り果ててしまった。"
"こう言う時、頼ってばかりは悪いと思いつつも、一人の顔が脳裏に思い浮かぶ。"


show char trk08s2
with dis



voice "Rikka_1262"
rk "「やっぱり……リサ姉に、相談してみよう」"


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


show char tri01s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0888"
r "「あら、六夏。今日はまだ、学校に残っていたの？」"


show char trk06s2 at right as r
with dis



voice "Rikka_1263"
rk "「リサ姉……」"
"見つけたリサ姉の顔を見た途端、安堵と悲しみが一気に溢れ出してきた。"


show char tri03s2 at left
with dis



voice "Risa_0889"
r "「どうしたのよ、六夏……アナタ、泣いているの？」"
"気遣わしげに、リサ姉がワタシの顔を覗きこんでくる。"
"そう……リサ姉の指摘通り、ワタシは泣いていた。"
"いつの間にかぽろぽろと、大粒の雫が目からとめどなく落ちてしまう。"
voice "Rikka_1264a"
rk "「あ、あれ、やだなぁ、ワタシ……どうしたんだろ？　ダメ、止まんないよぉ……ぅぅっ」"
"拭っても拭っても、涙は溢れて頬を伝っていく。"
"自分の気持ちがコントロールできない、どうしよう。"
voice "Risa_0890"
r "「ね、六夏……何か辛いことがあったの？」"
"リサ姉はワタシをいたわるように、ハンカチを差し出してくれた。"
"ワタシはそれを受け取って、自分の目にあてる。"
"やがてリサ姉の顔が滲んで、曇っていく。"
voice "Rikka_1265"
rk "「り、リサ姉……うわぁぁぁんっ！！」"
voice "Risa_0891"
r "「六夏……」"
"気付けばワタシは、その場に泣き崩れていた。"
"子どものように泣きじゃくるワタシはさぞ、みっともないことだろう。"
"でも今のワタシは、そんな事を気にする余裕なんて無かった。"
"ただただ、泣きたかった。"


show char tri01s2 at left
with dis



voice "Risa_0892"
r "「最近は調子良く見えていたけど……こういうところ昔と変わらないわね」"
"泣き続けるワタシに、リサ姉は優しく背中をさすってくれた。"
"子供の頃と同じように……"


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



#mes on
#system on


show char tmi01s2
with dis



voice "Miya_0525"
m "「ふぅん……それで、わたくしを呼んだってワケ？」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0893"
r "「ええ、どうしたら良いか、もうわからなくて……とっさに、美夜を呼んじゃったの」"
voice "Miya_0526"
m "「まあ、愛しい璃紗に頼りにされるのは、悪くないけれど……ね」"

hide char tmi01s2 at left
hide char tri03s2 at right as r
show char tmi01s2 at sleft as l
show char tri03s2
show char trk06s2 at sright as sr
with dis



voice "Rikka_1266"
rk "「ぅぅっ……ぅっ、ひっく……」"
"ああ、ものすごく怒っているように見える、美夜さま……ちょっと怖い。"
voice "Risa_0894"
r "「もう、どうしたらいいかしら……私」"
voice "Miya_0527"
m "「ねぇ、六夏さん。一体どうしたの？　泣いても構わないけれど、璃紗が困っているのよ」"
voice "Rikka_1267"
rk "「ひっく……ぐすっ……」"


show char tmi07s2 at sleft as l
with dis



voice "Miya_0528"
m "「もう、泣いているだけじゃわからないわ。しっかりしなさいっ！！」"
voice "Risa_0895"
r "「ちょっと美夜、そんな言い方は……」"


show char tmi08s2 at sleft as l
with dis



voice "Miya_0529"
m "「いい？　恋愛の悩みは、誰かに話せば大体、スッキリするはずよ。ほら、聞いてあげるから、話してごらんなさい」"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1268"
rk "「み、美夜さま……」"
"ワタシは涙に濡れた顔を上げて、美夜さまを見つめた。"
"美夜さまは美しすぎる顔で、小さく優しく微笑んでいた。"
"普段はキツい事を言っているようでも、本当は美夜さまって、リサ姉と同じく優しい人なんだよね……口は悪いけれど。"
voice "Rikka_1269"
rk "「あの……ごめんなさい、美夜さま、リサ姉」"
voice "Risa_0896"
r "「ううん、もう平気？」"
voice "Rikka_1270"
rk "「……うん、涙、止まった」"
voice "Risa_0897a"
r "「それは良かったわ。今までも六夏の悩みは聞いてきたけど、まさか泣くまでとは思わなかったから」"
voice "Rikka_1271"
rk "「心配かけて、ゴメンなさい……」"
"リサ姉はそっと、ワタシの頭を撫でてくれた。"
voice "Risa_0898"
r "「でも、よっぽどの事があったのね……」"
voice "Rikka_1272"
rk "「うん……本当に、ごめんなさい……」"
voice "Miya_0530"
m "「もう謝らなくてもいいわ。何があったのか、ちゃんと話してごらんなさい」"
voice "Rikka_1273"
rk "「はい、それが……」"
"ワタシは事のいきさつを、２人に話した。"
"２人は静かに、だけど真剣に、ワタシの話を聞いてくれた。"
voice "Risa_0899"
r "「それは……気になるわね」"
voice "Miya_0531"
m "「そうね。単純に、別れの言葉とも取れるけど……」"
voice "Rikka_1274"
rk "「わ……別れ、って……」"
"美夜さまのその言葉に、ワタシはショックを受けた。"
"ううっ、やっと落ち着いた涙腺が、また決壊しそう……"


show char tri08s2
with dis



voice "Risa_0900"
r "「ちょっと、美夜！　そんな事言わないでよ……まだわからないわよ、六夏。諦めちゃダメ、ねっ？」"
"気を使って明るい表情で励ましてくれる、リサ姉。"
"やっぱりワタシにとってのリサ姉は、優しいお姉さんだった。"
voice "Rikka_1275"
rk "「うん……でもワタシ、どうしたらいいのか……」"


show char tri03s2
with dis



voice "Risa_0901"
r "「うーん……今は沙雪さんを信じて、待つしかないんじゃない？」"
voice "Rikka_1276"
rk "「待つ……」"


show char tri01s2
with dis



voice "Risa_0902"
r "「そうそう。その内、沙雪さんから歩み寄ってくれると思うわ」"
voice "Rikka_1277"
rk "「そっか……リサ姉がそういうなら、そうした方が……」"
voice "Miya_0532"
m "「……フッ、甘い、甘いわ、駅前の文学堂のはちみつロール並に甘いわよ、璃紗っ！！」"


show char tri03s2
with dis



voice "Risa_0903"
r "「どういうたとえよ、美夜？」"
voice "Miya_0533"
m "「恋愛事はね、ただ待つだけじゃダメ……ガンガン攻めなければ、逃げていってしまうものなのよ」"
voice "Risa_0904"
r "「どういう……こと？」"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0534"
m "「簡単な事よ。沙雪さんの事が気になるなら、調べてみればいいのよ♪」"
"ニッコリと笑う美夜さんの表情は、まさしく……肉食系女子の、それだった。"


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
jump S047



