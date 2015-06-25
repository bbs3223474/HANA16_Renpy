#「いきなりリゾート？」

label S017:
$ save_name = "◇いきなりリゾート？"


#**璃紗の部屋・夜
scene bg bg01c
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


show char tri01f2
with dis



voice "Risa_0519"
r "「うーん、今日もたくさん勉強したわね」"


show char tmi01f2 at left
show char tri01f2 at right as r
with dis



voice "Miya_0256"
m "「短期集中の夏期講習だけのことはあったわね。璃紗たち、一般人にはかなりの量だったんじゃない」"


show char tri03f2 at right as r
with dis



voice "Risa_0520"
r "「また、そんな言い方を……」"
"私たちは夏休みに入ってすぐに夏期講習に通いはじめて。"
"今日は、その最終日だった。"


show char tri01f2 at right as r
with dis



voice "Risa_0521"
r "「美夜だって、熱心にノートとっていたじゃない」"
voice "Miya_0257"
m "「あれは……璃紗の観察ノートよ」"


show char tri03f2 at right as r
with dis



voice "Risa_0522"
r "「へっ？　なんかデ○ノート以上にいやな響きがするわ」"
voice "Miya_0258"
m "「ここだけの話だけど、優菜さまはデ○ノート以上のすごいノートを所有しているそうよ」"
"あの、優菜さまが……そんなの初耳だわ。"
voice "Miya_0259"
m "「その名も『七海ちゃん手帳』」"


show char tri04f2 at right as r
with dis



voice "Risa_0523"
r "「はぁぁぁ？」"
voice "Miya_0260"
m "「そこには、なんと……七海さんのあらゆる秘密が記述されているそうよ」"


show char tri03f2 at right as r
with dis



voice "Risa_0524"
r "「あの七海さんに、どんな秘密があるのかしら」"
voice "Miya_0261"
m "「彼女の性感帯とか、彼女の感じる時の仕草とか……その一冊ですべて、網羅されているそうよ」"
voice "Risa_0525"
r "「秘密って、そっちのこと？」"
"意外というか、呆れるというか……優菜さまってみんなの前では完璧キャラに見えるから、どうしてもそういう印象を持てないのよね。"
voice "Miya_0262"
m "「偉大なる先人の所行、わたくしも見習うべきよね」"
voice "Risa_0526"
r "「み、見習わなくていいわよ～！　もう、美夜ったら……」"
"夏期講習の間、そんなことばかり考えていたのね、まったく。"
"何の為にお金を払ってまで、講習に行ってると思ってるのかしら。"


show char tri08f2 at right as r
with dis



voice "Risa_0527"
r "「夏期講習は終わったけれど、まだまだ勉強はやるわよ！」"
voice "Miya_0263"
m "「ええ、わたくしも更に、この『リサノート』を完璧にするわ」"


show char tri09f2 at right as r
with dis



voice "Risa_0528"
r "「その勉強じゃないわよ。それにノートに変な名前をつけないで！」"
"もう……相変わらず、変態なんだから。"


show char tri01f2 at right as r
with dis



voice "Risa_0529"
r "「勉強は十分、するとしても……まだどこにも遊びに行ってないし、そっちの計画も立てないとね」"
voice "Miya_0264"
m "「そうね……プールでの璃紗の水着姿、また見てみたいし」"


show char tri03f2 at right as r
with dis



voice "Risa_0530"
r "「あれは……プールでは、もう着ないわよ」"
voice "Miya_0265"
m "「だったら、海では？」"
voice "Risa_0531"
r "「海に行くのは良いけれど、あの恥ずかしい水着はもう着ないわよ」"
voice "Miya_0266"
m "「あれがそんなにイヤなら、新しい水着また買いに行きましょうか？」"
voice "Risa_0532"
r "「美夜……もっとすごいの、買うつもりでしょう」"
voice "Miya_0267"
m "「璃紗、察しがよくなる……メモメモっと」"


show char tri09f2 at right as r
with dis



voice "Risa_0533"
r "「もぉ、ノートに変なこと書き込まないの～！」"
"こうして騒ぎながら、結構楽しく、夏の計画を立てていると……"

#//SE：携帯の音
#♀SE007
play sound "sound/SE007.ogg"


voice "Miya_0268"
m "「璃紗、メールよ。また六夏さんじゃないの？」"


show char tri03f2 at right as r
with dis



voice "Risa_0534"
r "「ううん、電話みたい……誰かしら？　知らない番号だわ」"
"もしかしてママがまた、番号を変えたのかしら……"
"ママはだらしないところがあるから、よく携帯をなくしたりするのよね。"
"とりあえず、出てみるしかないわ。"


#allClear:
hide char tmi01f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg01c
show char tri01f2
with dis



voice "Risa_0535"
r "「……はい」"
voice "Rena_0000"
x "『もしもし、安曇さん？』"
voice "Risa_0536"
r "「は、はい……」"
"何だか懐かしい声に思えた。"
"この声って……"
voice "Risa_0537"
r "「……もしかして、麗奈先生ですか？」"


show char trn02p at hleft
show char tri01f2 at right as r
with dis



voice "Rena_0001"
ren "『正解♪』"
"麗奈先生という名前を聞いて、隣りにいた美夜も驚いている。"
"麗奈先生は去年、私や美夜の担任だった先生で。"
"つい『先生』って呼んでいるけれど、厳密にはもう教師じゃなくて、かなりの事業家だったりする。"
"ミカ女のＯＢで、在学中は『究極の淑女』と呼ばれていたり……って、今は沙雪さんがその、究極の淑女の再来とかって呼ばれているわね。"
"附属部の瑠奈さんのお姉さんだったり、貴子先生とも交流があったりと、ミカ女とかなり付き合いの深いキャラクターで。"
"とにかく、究極完璧超人というか……ものすごい人なのよね。"
"海外で新しい事業を始めたはずの麗奈先生から、まさか電話がかかってくるなんて……"
voice "Rena_0002"
ren "『久しぶりね～、綾瀬さんとはうまくいってる？』"
voice "Risa_0538"
r "「え、ええ……まあ」"
"チラッと、美夜の方を見る。"
"あれから色々あったけど、こうして一緒に過ごすくらい、うまくいっているわ。"
voice "Risa_0539"
r "「先生は今、どちらにいらっしゃるんですか？」"


show char trn01p at hleft
with dis



voice "Rena_0003"
ren "『私？　私はね……先日、結構大きな仕事を成功させたんで、長期休暇中よ』"
voice "Risa_0540"
r "「そう、なんですか……」"
"日本を離れて、また３ヶ月ちょっと……それでやりとげてしまったなんて。"
"相変わらず、すごい事をやっているみたいね。"
voice "Rena_0004"
ren "『でね、実は今、日本にいるのよ』"


show char tri04f2 at right as r
with dis



voice "Risa_0541"
r "「えぇぇぇっ！？」"
"行動力ありすぎよ、先生……"
"きっとその仕事内容だって、私なんかには計り知れないものなんだろうなぁ。"
voice "Rena_0005"
ren "『それでね、せっかくだから、みんなに会おうと思って連絡したのよ……私の泊まっている、リゾートホテルに来ない？』"


show char tri01f2 at right as r
with dis



voice "Risa_0542"
r "「もう、いきなりですね……」"
"こういうところも全然、変わってないわ。"
"麗奈先生のことだから、そのホテルもきっと、ものすごくゴージャスなんでしょうね。"
"楽しそうではあるけれど……私一人では、決められないわ。"
voice "Risa_0543"
r "「美夜……じゃなくて、綾瀬さんと一度相談してから、お返事させ──」"
voice "Rena_0006"
ren "『ダメ』"
"まだ話してる途中なのに、思いっきり否定されてしまったわ。"
voice "Rena_0007"
ren "『ベストカップルは、強制参加だから……あなたたちだけ、例外は認めないわ』"


show char tri03f2 at right as r
with dis



voice "Risa_0544"
r "「そ、そうなんですか？」"
voice "Rena_0008"
ren "『ええ。綾瀬さんも今、一緒にいるのかしら？』"


show char tri01f2 at right as r
with dis



voice "Risa_0545"
r "「まあ……はい」"
voice "Rena_0009"
ren "『ちょうど良いわ。じゃあ、貴女の家にそのまま、迎えをよこすから』"


show char tri04f2 at right as r
with dis



voice "Risa_0546"
r "「えっ！？　ちょ、ちょっと先生」"

#♀SE059
play sound "sound/SE059.ogg"

hide char trn01p at hleft
#wipe flash#################################


"そのままプツッと、携帯は切れた。"


#allClear:
hide char tri04f2 at right as r
#lastBG:
#scene bg bg01c
show char tri03f2
with dis



voice "Risa_0547"
r "「もう、なんて慌ただしいのかしら……」"
"このこと、美夜になんて説明しよう。"
"夏休みは２人だけで過ごすって、決めたばかりなのに……"
voice "Risa_0548"
r "「美夜、あのね……」"


show char tmi01f2 at left
show char tri03f2 at right as r
with dis



voice "Miya_0269"
m "「麗奈先生から、リゾートホテルへ招待されたのね」"
voice "Risa_0549"
r "「あっ……聞こえていた？」"
voice "Miya_0270"
m "「ええ、先生の声、とても大きかったし……相変わらずよね」"


show char tmi02f2 at left
show char tri02f2 at right as r
with dis



"２人して、失笑してしまう。"
voice "Risa_0550"
r "「本当に困った先生よね。私たちの都合なんて、おかまいなしなんだから」"
"でも……これはこれで、楽しそうかも。"
"他のベストカップルの人たちも呼ばれているみたいだし、以前麗奈先生のマンションで合宿したときのように、面白いことがありそうだし。"
voice "Miya_0271"
m "「璃紗と２人きりの方が、本当はいいんだけど……これはこれでありかもね」"
"どうやら美夜も、同意見みたいだわ。"


#**夜空
#allClear:
hide char tmi02f2 at left
hide char tri02f2 at right as r
#lastBG:
#scene bg bg01c
scene bg bg42c
with dis



"こうして私たちは、麗奈先生の待つ南国の島にサマーバカンスに行く事になりました。"
voice "Miya_0272"
m "「ああ、まぶしい海に躍る、水着姿の璃紗……やっぱり今から、水着買いにいきましょうよ」"
voice "Risa_0551"
r "「だから、それはもういいって！」"


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
jump S018



