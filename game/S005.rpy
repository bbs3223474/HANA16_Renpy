# S005基本没有可圈可点的地方，所有的东西在S002都碰到过。
# 在这里非常感谢仙儿制作的krkr2转Ren'py代码html脚本，
# 使得在定义明确的情况下，我能够轻松地通过复制粘贴，
# 就能瞬间将原花吻16的代码转成Ren'py的语言，减少一半以上的工作量。
# 有条件的同学可以去找会写正则替换法代码的好基友帮忙做一个哦。
# 
# 当然，我也说了时定义明确的情况下，因此这个html代码是不能通用的，
# 也不能分享给大家直接使用。所有的转换都必须要在专属定义的情况下进行，否则就算转换出来了也没法运行。


#「璃紗と六夏の、大スキャンダル」

label S005:


$ save_name = "◇璃紗と六夏の、大スキャンダル"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP12
play music "sound/BGM12.ogg"


show char tri03s2
with dis



voice "Risa_0164"
r "「ううぅ……憂鬱だわ」"
"いつも通りの、初夏の香りを感じる爽やかな朝。"
"だけど私を取り巻く環境は、昨日から激変してしまった。"
voice "mobJyosiA0011"
mobA "「見て、璃紗さんだわ。あの方が１年の、六夏さんと……」"
voice "mobJyosiB0010"
mobB "「ええ、ビックリしましたわね」"
voice "mobJyosiA0012"
mobA "「美夜さんは一体、どうなさるのでしょう？」"
voice "Risa_0165"
r "「ああ……皆さん、聞こえているんですけれど……」"
"歩いているだけで、人の視線と噂話がついてまわる。"
"ああ、いたたまれないわ。"


show char tna01s2 at left
show char tri03s2 at right as r
with dis



voice "Nanami0062"
n "「璃紗さん、ごきげんよう」"


show char tri01s2 at right as r
with dis



voice "Risa_0166"
r "「あっ、七海さん……ごきげんよう」"
"後ろから七海さんに声をかけられる。"
"知ってる人がそばにいるだけで、少しほっとした。"


show char tna03s2 at left
with dis



voice "Nanami0063"
n "「璃紗さん……疲れてるみたいだね、大丈夫？」"
voice "Risa_0167"
r "「ええ、なんとか……」"
"でも正直、答える声に気力はなくて。"
"心配そうに七海さんは、私を見ていた。"
"そうしている間にも、私の周りからヒソヒソ話は聞こえてきて。"
"璃紗さんが、六夏さんが、美夜さんが……といった名前が、飛び交っていた。"
voice "Nanami0064"
n "「あの場にいたのは、ベストカップルのメンバーだけなのに……何故か噂になっちゃってるね」"


show char tri03s2 at right as r
with dis



voice "Risa_0168"
r "「そうなのよね……はぁ～」"
"１年生の六夏が、私に突然抱きついて来た件はいつの間にか、翌日には学園中には知れ渡っていて。"
"『ベストカップル安曇璃紗に、新恋人発覚！？』なんていう、どこかのゴシップ誌並みのスキャンダルで今、ミカ女は騒然としていた。"
voice "Risa_0169"
r "「委員会室の前をたまたま、通りがかった人がいたのかもしれないわ……それに大騒ぎだったから、外にも聞こえたのかも」"
voice "Nanami0065"
n "「そうだね……美夜さん、ものすごかったもんねー」"
"あの時の状況を思い出して、七海さんがぶるっと震えた。"
voice "Nanami0066"
n "「それで……美夜さんの方はどうなの？」"
voice "Risa_0170"
r "「それがね、ちょっと困ったことになっちゃったの……全然、私の話を聞いてくれなくて」"
"あの場は仕方ないけれど、ちゃんと説明すれば、いつものようにわかってくれると思っていたのに。"
"勝手に流されたスキャンダルな噂に呆然としちゃって、聞く耳を持ってくれないのよね。"
voice "Risa_0171"
r "「こんなこと、初めてだから……ああ、どうしたらいいのかしら」"
voice "Nanami0067"
n "「わたしもあんな感情的な美夜さんを見たの、初めて」"
"人前では常にクールで、ポーカーフェイス……その美夜の姿は、もうなかった。"
voice "Risa_0172"
r "「とにかく、もう１回ちゃんと説明してくるわ。六夏は幼なじみで、妹のようなものだって」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**アトリエ・昼
scene bg bg29a
with Dis



#mes on
#system on


show char tri03s2
with dis



voice "Risa_0173"
r "「美夜……ねぇ美夜、いるんでしょう？」"
"すっかりふさぎ込んでいる美夜は、学校に来ても、ほぼ一日中アトリエにこもっていた。"
"昼休み、ようやく時間を見つけて、私は彼女に会いに来た。"


show char tmi03s2
with dis



voice "Miya_0060"
m "「………………」"
"ドアを開けると、ソファに座ってぼんやりしている美夜の姿があった。"
"いつもなら読書をしていたり、お茶を楽しんだりしているのに……ただ、ボーっとしているだけ。"
"今回のことは相当、堪えているのがわかった。"
"だからこそ、ちゃんと話を聞いて欲しい。"


show char tmi03s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0174"
r "「あのね、美夜……六夏のことだけど」"


show char tmi08s2 at left
with dis



voice "Miya_0061"
m "「……その方の話なら、何も聞きたくないわ」"
voice "Risa_0175"
r "「そんなこと言わないで、聞いてったら。彼女とは以前、ご近所で幼なじみだったのよ」"
voice "Miya_0062"
m "「………………」"
voice "Risa_0176"
r "「六夏は、一学年上の私を、姉のように慕ってくれていたの」"
voice "Miya_0063"
m "「ふん……そのころから、璃紗を狙っていたのね」"
voice "Risa_0177"
r "「違うわよ、もう……その後は前にも話したけれど、ウチは母が離婚して、今の家に引っ越したから……転校して、六夏と離れちゃったのよ」"
"六夏の家もお父様がいなかったから、あの時は私の気持ちに共感してくれて、すごく救われたっけ。"
"だから別れる時は、とっても悲しかったのを、今でも覚えている。"
voice "Risa_0178"
r "「それがまさか、こんなところで再会するなんて……六夏は感きわまって、抱きついてしまっただけなのよ」"
voice "Miya_0064"
m "「良かったわね……素敵な恋人との再会じゃない」"
voice "Risa_0179"
r "「だから、もうっ」"
"なんで、わかってくれないのかしら。"
"美夜はツンと横を向いて、私の目すら見てくれない。"
"それだけ美夜には、あの場面がショックだったのね。"
"確かに……私の目の前で、美夜が他の子にぎゅっと抱きつかれる場面を想像すると……泣きたくなるけれど。"
voice "Risa_0180"
r "「美夜……ああ、もう……」"


#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


voice "Miya_0065"
m "「……授業が始まるわよ、戻らなくてもいいの、委員長さん？」"
voice "Risa_0181"
r "「うっ……わかったわ。でも、また来るから……」"


#allClear:
hide char tmi08s2 at left
hide char tri03s2 at right as r
#lastBG:
#scene bg bg29a
with dis


"ここで授業をさぼったとしても、美夜の気持ちが変わるわけじゃない。"
"後ろ髪ひかれる思いのまま、私はアトリエを出ていった……。"


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
show char alpha
with Dis



#mes on
#system on


"授業が終わり、すぐにアトリエに向かったけれど……もう美夜はどこかに行ってしまったらしく、もぬけの空だった。"


show char tri03s2
with dis



voice "Risa_0182"
r "「まだ、家に帰ってはいないはずよね……？」"
"カバンはアトリエに置きっぱなしだったから、どこかその辺りにいるはず。"
"校内を探していると、前から麻衣さまが歩いてきた。"


show char tma01s2 at left
show char tri03s2 at right as r
with dis



voice "Mai_0020"
ma "「あっ、璃紗ちゃん。探していたのよ」"
voice "Risa_0183"
r "「麻衣さまが……私を？」"
voice "Mai_0021"
ma "「ええ。１年の六夏ちゃんだっけ？　さっきわたしと玲緒の所に、謝りに来たのよ」"
voice "Risa_0184"
r "「六夏が、３年の教室に？」"
voice "Mai_0022"
ma "「今はただでさえ、周りの注目を浴びているのに……緊張しながらやって来て『この間はお騒がせして、すいません』って」"
voice "Risa_0185"
r "「そう……なんですか」"
voice "Mai_0023"
ma "「幼なじみなんだってね、２人は。ちゃんと説明していったよ。おそらく他のメンバーのところにも、行っているみたいよ」"
"六夏……１人でそんなこと、していたのね。"
voice "Mai_0024"
ma "「あの子も今回の件では随分と、責任を感じてるみたいだったわよ」"
voice "Risa_0186"
r "「そう……ですか……」"


show char tma03s2 at left
with dis



voice "Mai_0025"
ma "「それでね、その……」"
"麻衣さまが言いにくそうに、言葉を切った。"
voice "Mai_0026"
ma "「多分あの子、美夜ちゃんの所にも行っていると思うのよ」"


show char tri04s2 at right as r
with dis



voice "Risa_0187"
r "「……えっ？　美夜のところにも」"
voice "Mai_0027"
ma "「うん、ほら、この間の美夜ちゃん、ちょっとおかしかったでしょう？　心配していたから」"


show char tri01s2 at right as r
with dis



voice "Risa_0188"
r "「わ、わかりました！　ちょっと見てきます、麻衣さまありがとうございました」"


show char tma01s2 at left
with dis



voice "Mai_0028"
ma "「うん、頑張ってね！」"


hide char tma01s2 at left
with dis


"麻衣さまにお礼を言って、私は廊下を早歩きで進んでいく。"
voice "Risa_0189"
r "「美夜……六夏……」"
"私の話ですら、まともに聞いてくれなかった美夜が、六夏を相手にしてくれるわけない。"
"なんか、大変なことにならなければいいけれど……"


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
show char alpha
with Dis



#mes on
#system on


show char tri03s2
with dis



voice "Risa_0190"
r "「はぁ、はぁ……六夏、いたっ！」"
"しばらく校内を探し回って、私はようやく六夏を見つけることができた。"


show char trk03s2 at left
show char tri03s2 at right as r
with dis



voice "Rikka_0003"
rk "「リサ姉……どうしたの？　そんなに息を切らせて」"
voice "Risa_0191"
r "「はぁはぁ……六夏、アナタ、美夜の所へ行くつもりなんでしょう」"
voice "Rikka_0004"
rk "「えっ、うん。ワタシのせいで、美夜さまが色々、誤解しているみたいだったから……ちゃんと説明しようかと」"
voice "Risa_0192"
r "「あのね、六夏……それ、今はやめておいた方が……」"


hide char trk03s2 at left
hide char tri03s2 at right as r
show char tmi08s2 at sleft as l
show char trk03s2
show char tri03s2 at sright as sr
with dis



voice "Miya_0066"
m "「……何だか、騒がしいわね」"


show char tri04s2 at sright as sr
with dis



voice "Risa_0193"
r "「み、美夜……」"
"私と六夏の前に突然、美夜が現れた。"


show char tri03s2 at sright as sr
with dis



"その手には、校内で売られている紙パックのジュースを持っていた。"
"いつもならきっと、アトリエでお茶をしているところだけど……今日は私を避けようとして、ここでこっそりお茶をしていたんだわ。"
"その美夜に、六夏はいきなり話しかけた。"
voice "Rikka_0005"
rk "「あ、あの、美夜さま、今回はワタシの軽率な行動で、お二人に迷惑をかけてしまい、本当にすいませんでした」"
"長身の六夏が、ぺこっと深く頭を下げる。"
"でも美夜は……眉間にシワを寄せて、そんな六夏を冷ややかに見つめているだけだった。"
voice "Risa_0194"
r "「み、美夜……六夏も謝っているし、もうこの件は……ねっ？」"
voice "Miya_0067"
m "「………………」"
voice "Risa_0195"
r "「ねぇ、美夜ったら」"
voice "Rikka_0006"
rk "「すいませんでした、美夜さま」"
voice "Miya_0068"
m "「………………」"
voice "Risa_0196"
r "「美夜……ちょっと、聞いてるの？」"
voice "Rikka_0007"
rk "「美夜さま……？」"


show char tmi09s2 at sleft as l
with dis



voice "Miya_0069"
m "「も、もぉ、なんなのよぉ～っ！！」"


show char trk04s2
with dis



voice "Rikka_0008"
rk "「えっ？」"
voice "Miya_0070"
m "「そんな風に２人して仲良くしているから、噂になったりするんじゃないのかしら」"
voice "Risa_0197"
r "「えっ、だって今は、そういうことじゃ……」"
voice "Miya_0071"
m "「もうわたくし、何も聞こえないわ、わぁー、わぁー！　わぁぁっー！」"
"耳をふさいで、大声を出す美夜。"
"そんな、子供じゃないんだから……"


show char tmi08s2 at sleft as l
with dis



voice "Miya_0072"
m "「もういいでしょう、わたくしはここで失礼するわ」"


hide char tmi08s2 at sleft as l
with dis


voice "Risa_0198"
r "「待ってよ、美夜……あっ」"
"追いかけようとしたのに、美夜はサッとその場から姿を消した。"
voice "Risa_0199"
r "「ちょっと……もう、こんなところで逃げ足の速さを発揮しなくてもいいじゃないのぉ」"
"はぁ～……もうだめだわ。"
"全く、話を聞いてくれないし。"
"困っちゃうなぁ……もう。"


#allClear:
hide char trk04s2
hide char tri03s2 at sright as sr
#lastBG:
#scene bg bg21a
show char trk03s2 at left
show char tri03s2 at right as r
with dis



voice "Rikka_0009"
rk "「リサ姉……ごめんなさい、ワタシのせいで……」"
voice "Risa_0200"
r "「六夏……」"
voice "Rikka_0010"
rk "「本当に、ごめんなさい……」"
"落ち込む六夏に、何か優しい言葉をかけてあげたかったけれど。"
"私は美夜のことが気がかりで、もやもやして、何も言ってあげられなかった。"


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
jump S006



