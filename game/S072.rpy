#「優菜の『だいじょうぶ\001』」

label S072:
$ save_name = "◇優菜の『だいじょうぶ♪』"


#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


"沙雪さんに負けたくない……そんな思いがわたしを突き動かす。"
"勉強にもより一層、力が入った。"
"いつもなら、優菜お姉さまに指導して貰っているのだけれど。"
"放課後の教室で、わたしは一人で勉強をしていた。"
"この日は、自分で図書館や資料室から様々な資料を揃えて、独学中だった。"


show char tna08s2
with dis



voice "Nanami0421"
n "「えっと……あっ、これはこうで……うん」"
"資料はどれもこれも、わたしにはちょっぴり難しい。"
"だけど辞書を引いたり反芻したりして、自分なりに必死に学んでいく。"


show char tna03s2
with dis



voice "Nanami0422"
n "「う～ん……これ、難しいなぁ。でもわからないままにしてちゃ、いけないし……お姉さまに頼り切るのも、よくないし」"
"ペンを握る手にも、ギュッと力がこもり、汗ばんでしまっていた。"


show char tyu03p
with dis



voice "Yuuna_0227"
y "「ああ、七海～ぃ。くれぐれも、ムリして身体を壊さないでね……」"


#allClear:
hide char tyu03p
#lastBG:
#scene bg bg04a
with dis


"まるで愛しくてたまらないという視線で、ドアの向こうからわたしを見つめる、優菜お姉さま。"
"その存在にさっぱり気付かず、わたしは空が暗くなるまで、勉強を続けたのでした……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎廊下
scene bg bg05a
with Dis



#mes on
#system on


show char tna01s2
with dis



voice "Nanami0423"
n "「……あっ、六夏さん」"


show char tna01s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_1601"
rk "「な、七海さま……その……ごきげんよう……」"
"わたしは廊下でばったりと、六夏さんと出くわした。"
"六夏さんは明らかに、不安そうな表情を浮かべている。"
voice "Nanami0424"
n "（きっとこの間のことで、気まずくなっているのね……）"
"六夏さんもきっと、不安でたまらないのね。"
"気持ちは、手に取る様によくわかる。"
voice "Nanami0425"
n "「あの……この間の中庭でのことは、気にしないようにしましょう」"
voice "Rikka_1602"
rk "「えっ……」"
voice "Nanami0426"
n "「確かに、不安に思うことも多いけれど……でもお互い、自分ができる努力をしましょう」"


show char trk01s2 at right as r
with dis



voice "Rikka_1603"
rk "「七海……さま……」"


#★★★選択肢　ここから

"ワタシは六夏さんを励ますように、言った。"


#++選択肢（１）
#１．『お互いの恋人を信じましょう』○
#２．『もっと、頑張りましょう』×
menu:
 "お互いの恋人を信じましょう":
  jump select13_1
 "もっと、頑張りましょう":
  jump select13_2



#１．『お互いの恋人を信じましょう』
label select13_1:


voice "Nanami0427"
n "「優菜さまの恋人はわたしだし、沙雪さんの恋人は六夏さん……ねっ、そうでしょう？」"
voice "Rikka_1604"
rk "「そ、それは……はいっ！」"


show char tna02s2 at left
with dis



voice "Nanami0428"
n "「お互いの恋人を信じよう、ね」"
"わたしはニコッと、六夏さんに微笑みかけた。"
"緊張して強張った六夏さんの肩から、力がすっと抜けたのがわかる。"


show char trk02s2 at right as r
with dis



voice "Rikka_1605"
rk "「そうですよね、七海さま。愛しい人を信じられないなんて、恋人失格ですよね」"
"六夏さんは笑顔で、大きく頷いた。"
voice "Nanami0429"
n "「そうだね……そうだよ」"
"わたしも一緒に、うなづいてみせた……自分にも、言い聞かせるように。"


show char trk01s2 at right as r
with dis



voice "Rikka_1606"
rk "「ワタシも今できることを、精一杯頑張りますっ」"
voice "Nanami0430"
n "「うん、わたしも同じよ」"
voice "Rikka_1607"
rk "「それでは、失礼します……」"
voice "Nanami0431"
n "「うん……またね」"


hide char trk01s2 at right as r
with dis


"足取りも軽く、六夏さんはわたしの前から去っていった。"
"自分でできることを頑張りながら……恋人を信じる……"


#set f1 f1+1
jump select13_end


#２．『もっと、頑張りましょう』
label select13_2:


voice "Nanami0432"
n "「お互い、すごい恋人だから……ちょっと、不安になってしまうのよね」"


show char trk03s2 at right as r
with dis



voice "Rikka_1608"
rk "「はい……そうですね」"
voice "Nanami0433"
n "「だからこそ、わたし達がもっと頑張って、自分に自信を持てるようにならなくちゃ……ねっ？」"


show char trk01s2 at right as r
with dis



voice "Rikka_1609"
rk "「七海さま……そうですよね、もっと自信が持てる自分にならないと、いけないんですよね」"
"六夏さんは、うんうん頷いた。"


show char tna02s2 at left
with dis



voice "Nanami0434"
n "「そうよ……頑張りましょう！！」"
"わたしも一緒に、うなづいてみせた……自分にも、言い聞かせるように。"
voice "Rikka_1610"
rk "「ワタシも今できることを、精一杯頑張りますっ」"
voice "Nanami0435"
n "「うん、わたしも同じよ」"
voice "Rikka_1611"
rk "「それでは、失礼します……」"
voice "Nanami0436"
n "「うん……またね」"


hide char trk01s2 at right as r
with dis


"六夏さんはわたしの前から去っていった。"
"自分でできることを最大限、頑張る……"


#++選択肢終了
#★★★選択肢　ここまで
label select13_end:


"六夏さんに今言ったことは全部、自分に言い聞かせているの……うん。"


#allClear:
hide char tna02s2 at left
#lastBG:
#scene bg bg05a
show char tna08s2
with dis



voice "Nanami0437"
n "「……うん、大丈夫。頑張ろう」"
"わたしはこぶしをギュッと、握りしめたのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎教室・夕
scene bg bg04b
with Dis



#mes on
#system on


"わたしが沙雪さんより、優菜お姉さまの後継者にふさわしいところを、何とかして見せようと。"
"わたしは毎日、委員会で積極的に発言したり、行動したりした。"


show char tna01s2
with dis



voice "Nanami0438"
n "「文化祭の資料作成、わたしがしておきました。人数分コピーしてあります」"
voice "mobJyosiA0095"
mobA "「まあ、この量の資料を、ひとりでお作りになられたんですか？」"
voice "Nanami0439"
n "「ええ、なるべく分かりやすいように、図なども入れてみました」"
voice "mobJyosiB0056"
mobB "「とても見やすくまとまっていますね。良いんじゃないかしら」"


show char tna02s2
with dis



voice "Nanami0440"
n "「ありがとうございます、参考になれば幸いです」"
voice "mobJyosiC0028"
mobC "「七海さま、委員会で使う備品が、少し足りなくて……」"


show char tna01s2
with dis



voice "Nanami0441"
n "「それはわたしが、先ほど用意しておきました」"
voice "mobJyosiC0029"
mobC "「まあ、助かります。ありがとうございます」"
voice "Nanami0442"
n "「いいえ、大した手間じゃありませんから」"


show char tyu01s2 at left
show char tna01s2 at right as r
with dis



voice "Yuuna_0228"
y "「皆さん、お疲れ様です……もうこんな時間なので、本日は解散しましょう」"


show char tna03s2 at right as r
with dis



voice "Nanami0443"
n "「あっ……もう、こんなに……」"
"気が付けば、日はもう暮れていた。"
"仕事に夢中になりすぎて、全然気付かなかった。"
"外が暗くなるとさすがに帰りが危ないから、わたしは手早く後片付けをして、帰路に着こうとする。"


show char tna01s2 at right as r
with dis



voice "Nanami0444"
n "「お疲れ様でした。それでは優菜さま、また明日……」"
voice "Yuuna_0229"
y "「……あっ、七海さん」"
voice "Nanami0445"
n "「ふぇっ、優菜さまっ？」"
"お姉さまがわたしの鞄を、掴んで呼び止める。"
"思わず気の抜けた、いつもの声で返事をしてしまった。"
voice "Yuuna_0230"
y "「ね、今日は一緒に帰りましょう」"
voice "Nanami0446"
n "「えっ、あ……はい」"


show char tyu02s2 at left
with dis



voice "Yuuna_0231"
y "「最近はぜーんぜん、一緒に帰れてなかったからね♪」"
voice "Nanami0447"
n "「はぁ……はい……」"
"そのままわたしは久しぶりに、お姉さまと一緒に帰ることになった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**並木道・夕
scene bg bg18b
with Dis



#mes on
#system on


show char tyu01s2 at left
show char tna01s2 at right as r
with dis



voice "Yuuna_0232"
y "「こうして並んで歩くのも、久しぶりねぇ～」"
voice "Nanami0448"
n "「そうですね、最近はさっぱりでしたね」"


show char tyu06s2 at left
with dis



voice "Yuuna_0233"
y "「そうよぉ～、エッチなこともちょっと、ご無沙汰気味だし……ぐすん」"


show char tna04s2 at right as r
with dis



voice "Nanami0449"
n "「お、お姉さまっ……誰かにそんなこと聞かれでもしたら、どうするんですかっ」"
"唐突なお姉さまの発言に、わたしは慌てふためく。"



show char tna03s2 at right as r
with dis



"キョロキョロと周囲を見渡して、確認する。"
"ほっ……よかった、わたし達のほかには、誰も歩いていない。"


show char tyu01s2 at left
with dis



voice "Yuuna_0234"
y "「私は毎日、七海といーっぱいいーっぱいエッチなことをしたいんだけどなぁ」"


show char tna04s2 at right as r
with dis



voice "Nanami0450"
n "「そそそ、そんな。わ、わたしも、そうは思っていますけれども……」"
voice "Yuuna_0235"
y "「七海の可愛いアソコをグニュグニュってしたいし、可愛い仔猫みたいな舌もちゅうちゅう吸いたいしー」"


show char tna03s2 at right as r
with dis



voice "Nanami0451"
n "「も、もー、お姉さまったら、相変わらずのエロ乙女なんですから……」"
"呆れて見せるけれど、でも、全然いやな気はしない。"
"好きな人に体を求められるのって、とっても幸せなことだから。"
voice "Yuuna_0236"
y "「ね、七海……キスして、いい？」"
voice "Nanami0452"
n "「お、お姉さま、何もこんなところで……」"


show char tyu08s2 at left
with dis



voice "Yuuna_0237"
y "「欲求不満が爆発しそう。もうガマンできないの……いい？」"
voice "Nanami0453"
n "「お、お姉さまっ……」"
"真摯な顔をした、お姉さまの顔が近づいてくる。"
"ひどいわ、お姉さまったら……わたしが逆らえないの、わかってるくせに……"
"そしてお姉さまの麗しい顔が目の前に広がって、唇と唇が触れ合う……まさに、その瞬間。"
voice "Nanami0454"
n "「……えっ？」"
"頭の中が一瞬、真っ白になった。"


show char tyu04s2 at left
with dis



voice "Yuuna_0238"
y "「なっ、七海っ！？」"


#※EV041
#allClear:
hide char tyu04s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg18b
scene bg EV41
with Dis



"フラついたわたしの体を、お姉さまが抱きとめてくれていた。"
voice "Nanami0455"
n "「あっ……お姉さま、ありがとうございます……」"
voice "Yuuna_0239"
y "「もう……焦ったわよ。大丈夫、七海？」"
voice "Nanami0456"
n "「はい。あの……すみません」"
voice "Yuuna_0240"
y "「そう、よかった……でも七海、最近貴方、顔色が悪いわよ」"
"お姉さまが、そのすべすべとした柔らかな手で、わたしの頬を撫でる。"
voice "Nanami0457"
n "「えっ、そうですか？　自分では全然、気がつかなかったです」"
voice "Yuuna_0241"
y "「自分の体調に気が付かないくらい、頑張っていたんでしょう？」"
voice "Nanami0458"
n "「そ、それは……自己管理もできなくて、わたし……本当に、情けないです……」"
"なんだかシュンとして、落ち込んでしまう。"


#※EV041P1
scene bg EV41p1
with Dis



voice "Yuuna_0242"
y "「ふふっ……ね、七海、そんなに頑張らなくてもいいのよ」"
"お姉さまがわたしの頬を撫でながら、うんと優しい表情でわたしに語りかける。"
voice "Yuuna_0243"
y "「七海、貴方は十分頑張っているわ……無理しなくても、大丈夫よ」"
"そうしてわたしに微笑みかけるお姉さまの表情は、まるで聖母様のようで。"
"後光が射しているかのように眩しく見えた。"
voice "Nanami0459"
n "「ああ……お姉さま」"
voice "Yuuna_0244"
y "「で～も～ね～」"


#**並木道・夕
scene bg bg18b
with Dis



show char tyu08s2 at left
show char tna10s2 at right as r
with dis



voice "Nanami0460"
n "「ひゃあぁんっ、お姉さまっ、いたっ、痛いですっ」"
"頬を撫でていた手が、きゅっとほっぺをつねる。"
voice "Yuuna_0245"
y "「自分と沙雪ちゃんを、そんなに比べてはダメよ」"


show char tna04s2 at right as r
with dis



voice "Nanami0461"
n "「お、お姉さま……わかっていたんですか！？」"
"お姉さまのその言葉を聞いた瞬間、わたしは更に脱力してしまった。"


show char tyu02s2 at left
with dis



voice "Yuuna_0246"
y "「私は七海のことなら、なーんでもお見通しなのよ♪」"


show char tna01s2 at right as r
with dis



voice "Nanami0462"
n "「お姉さま……」"


show char tyu01s2 at left
with dis



voice "Yuuna_0247"
y "「七海が今、何を悩んでいるのかというのも、手に取る様にわかるし……ねっ」"


show char tna03s2 at right as r
with dis



voice "Nanami0463"
n "「そ、それは……」"
voice "Yuuna_0248"
y "「七海の感じちゃうところなんて、もう知りつくしちゃってるし、今日の七海のショーツの色だってわかるし……」"


show char tna04s2 at right as r
with dis



voice "Nanami0464"
n "「えっ、ええぇぇっ！？　そんなことまでわかるんですか！？」"


show char tyu02s2 at left
with dis



voice "Yuuna_0249"
y "「わかるわよ～♪　今日の七海のパンツの色はぁ……」"


show char tna09s2 at right as r
with dis



voice "Nanami0465"
n "「やっ、やだ、言わなくていいですからぁっ！！　あと、こんな街中で太股撫でるの、止めて下さい～っ！！」"
"頬を撫でていた筈のお姉さまの手は、気付けば今まさに、私の太股をイヤらしく撫でていた。"


show char tyu09s2 at left
with dis



voice "Yuuna_0250"
y "「もう、七海ってば、つれないんだから……」"


show char tna07s2 at right as r
with dis



voice "Nanami0466"
n "「ＴＰＯは大事ですっ！！　わきまえて下さいっ」"


show char tyu01s2 at left
with dis



voice "Yuuna_0251"
y "「はぁ～い。可愛い七海ちゃんにそう言われたら、しょうがないわよね～」"
"しぶしぶお姉さまは、わたしの太ももからそっと手を離す。"


show char tna03s2 at right as r
with dis



voice "Nanami0467"
n "（もう、油断も隙もないんだから……さすがエロ乙女なお姉さまだわ）"
voice "Yuuna_0252"
y "「さぁ、早く帰りましょう。今日は勉強はほどほどにして、ゆっくり寝るのよ？」"


show char tna01s2 at right as r
with dis



voice "Nanami0468"
n "「はい……お姉さま」"
"やっぱりお姉さまには全然、かなわないな。"
"お姉さまは私のことなんて、きっと全部お見通しだったんだわ。"
voice "Nanami0469"
n "（なるべくお姉さまには、心配をかけないようにしないとね……うん）"
"そして、わたし達はゆっくりと木々の間を歩いて帰った。"


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
jump S073



