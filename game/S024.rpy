#「美夜の寂しさ」

label S024:
$ save_name = "◇美夜の寂しさ"


#※ここは美夜視点です

#**ビーチ・昼
scene bg bg39a
with Dis



#mes on
#system on


#♂MP22
play music "sound/BGM22.ogg"


show char tmi01m
with dis



voice "Miya_0319"
m "「……あぁ、今日も太陽と海がまぶしいわね」"
"南の島に来てからというもの、毎日が楽しく、遊んでばかりで過ぎていく。"
"夏休みが終われば、学校と家の仕事でスケジュールはあっという間にうまっていくでしょうね。"
"だから、たまにはこんな休暇もいいと思う。"


show char tmi01m at left
show char tri02m at right as r
with dis



voice "Risa_0674"
r "「ねー、美夜、このトロピカルジュース美味しいわね{image=image/exch001.png}」"
"それに璃紗も、とても嬉しそうだし。"
"彼女の水着姿が見放題なのもたまらないわ。"


show char tmi01m at left
show char tri01m at right as r
with dis



voice "Risa_0675"
r "「美夜のって、私と同じジュースよね」"
voice "Miya_0320"
m "「ええ、パイナップルの味が特にきいていて美味しいわね」"
voice "Risa_0676"
r "「そうなのよね、でももう１個のマンゴーたっぷりなのも美味しそうで迷ったのよね」"

hide char tmi01m at left
hide char tri01m at right as r
show char tmi01m at sleft as l
show char tri01m
show char trk01m at sright as sr
with dis



voice "Rikka_0384"
rk "「あっ、リサ姉、だったらワタシの、味見する？」"
voice "Risa_0677"
r "「えっ、いいの？」"
"横にいた六夏さんが、璃紗にジュースを差し出す。"
"六夏さんが飲んでいたのは、璃紗が今し方飲みたいと言った、マンゴーメインのジュース。"


show char trk02m at sright as sr
with dis



voice "Rikka_0385"
rk "「こっちも美味しいよ」"


show char tri02m
with dis



voice "Risa_0678"
r "「それじゃあ、ひとくち……んっ、美味しい」"


show char tmi03m at sleft as l
with dis



voice "Miya_0321"
m "「………………」"
"この２人……やっぱり仲が良いわよね。"
"もう、疑ってはいないものの、なんとなく面白くないわ。"
"２人の様子をじっと見ていると、六夏さんが何を勘違いしたのか、わたくしにもジュースを差し出してきた。"


show char trk01m at sright as sr
with dis



voice "Rikka_0386"
rk "「あの……よかったら、美夜さまも味見しませんか？」"
voice "Miya_0322"
m "「………………」"
"黙ってるわたくしを、六夏さんが子犬のような目で見つめる。"
"下級生からは騎士なんて呼ばれているけれど、わたくしたち前では、甘えたがりのヘタレな子でしかない。"
"そんな子を拒否しても、仕方ないわね……"


show char tmi01m at sleft as l
with dis



voice "Miya_0323"
m "「じゃあ、いただくわ……ごくごく、ごく……」"


show char tri03m
with dis



voice "Risa_0679"
r "「美夜……ちょっと、飲み過ぎなんじゃ……」"
voice "Miya_0324"
m "「ごちそうさま、マンゴー味の方が少し甘めね。でも美味しかったわ」"


show char trk03m at sright as sr
with dis



voice "Rikka_0387"
rk "「美夜さま、のど乾いていたんですね……」"
"気がつけば、グラスがカラになっていた。"


show char tri01m
with dis



voice "Risa_0680"
r "「もう美夜ったら、全部飲んじゃうなんて……六夏、今私がお代わりもらってくるわ」"
"立ち上がる璃紗を、グッと引きとめる。"
voice "Miya_0325"
m "「わたくしがもらってくるから、２人はここにいていいわ」"
voice "Rikka_0388"
rk "「そんな、ワタシが行きますから」"
voice "Miya_0326"
m "「いいのよ……」"


#allClear:
hide char tmi01m at sleft as l
hide char tri01m
hide char trk03m at sright as sr
#lastBG:
#scene bg bg39a
with dis


"２人から離れて、蓬莱泉家専用『海の家』に行く。"
"麗奈先生がここでの飲み食いはフリーだと、初日に言われたので。"
"わたくしや玲緒さまなどは、スイーツや果物を好きなだけ、ここで調達することにしていた。"
"店員……おそらく蓬莱泉家の使用人……にジュースを頼むと、それが用意できるまでの間、ぼんやりと海を眺めた。"


show char tmi01m
with dis



voice "Miya_0327"
m "「璃紗と一緒に、南の島でバカンス……部屋もきれいだし、食べ放題に飲み放題、ここは何もかも満たされているわ」"
"満たされているというのに、それでもわたくしの中では、何かが足りない。"


show char tmi03m
with dis



voice "Miya_0328"
m "「これ以上、わたくしは何を望んでいるというの……」"
"ようやく、ジュースが出来上がり。"
"それを持って、璃紗たちの元へと戻る。"
"六夏さんとお喋りしながら、わたくしを待っている璃紗の姿が目に入った。"
"たまに海に向かって、手を振っているのは。"
"海で遊んでいる、七海さんや紗良さんに向かって……なんだと思う。"
"可愛い笑顔を振りまいてる、璃紗。"
"途端に胸が、チクッと痛んだ。"
voice "Miya_0329"
m "「……あっ、わたくしは……ぅぅっ」"
"唐突に、気づいてしまった。"
"自分が何に悩んで、何を欲しがっていたのか。"
"璃紗が、わたくしの方を向く。"
"そしてそのまま、驚いたように走ってきた。"


show char tmi03m at left
show char tri04m at right as r
with dis



voice "Risa_0681"
r "「み、美夜……それ、何？」"


show char tmi01m at left
with dis



voice "Miya_0330"
m "「なにって……ジュースよ」"
"両手にそれぞれ抱えていた、お盆。"
"その上にはトロピカルジュースが載っている。"
voice "Risa_0682"
r "「それはわかるけど……量が……」"
voice "Miya_0331"
m "「食べ物じゃないから、璃紗と六夏さんで３杯ずつくらい飲めるわよね。わたくしは残りをいただくわ」"


show char tri03m at right as r
with dis



voice "Risa_0683"
r "「お腹ごぼごぼになるわよ」"
voice "Miya_0332"
m "「大丈夫よ。暑いんだから、これくらい」"
voice "Risa_0684"
r "「………………」"

hide char tmi01m at left
hide char tri03m at right as r
show char tmi01m at sleft as l
show char tri03m
show char trk03m at sright as sr
with dis



voice "Rikka_0389"
rk "「………………」"


#allClear:
hide char tmi01m at sleft as l
hide char tri03m
hide char trk03m at sright as sr
#lastBG:
#scene bg bg39a
with dis


"璃紗も六夏さんも遠慮しているのか、ジュースを２杯までしか飲まなくて、後は七海さんたちにあげてしまった。"


show char tmi01m
with dis



voice "Miya_0333"
m "「……ごく……ごく、ごく……」"
"わたくしは残りのジュースを飲みながら。"
"自分で気付いてしまった、その望みについて考えていた。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


"翌日。"
"朝食をすませた後、部屋にこもっていたわたくしを、璃紗が誘いに来た。"


show char tri02f2
with dis



voice "Risa_0685"
r "「ねぇ、美夜。今日はみんなで沖にクルーズ行って、釣りするんだって……楽しみね」"
"声がうきうきしている。"
"よっぽど、そのクルーズが楽しみなようね。"
voice "Risa_0686"
r "「美夜も準備して、早く行きましょう」"


show char tmi03f2 at left
show char tri02f2 at right as r
with dis



voice "Miya_0334"
m "「今日は、ちょっと……」"


show char tri01f2 at right as r
with dis



voice "Risa_0687"
r "「ちょっと……何？？」"
voice "Miya_0335"
m "「えっと、その……具合が、悪いのよ……」"


show char tri04f2 at right as r
with dis



voice "Risa_0688"
r "「えっ、大丈夫！？　もしかして、風邪でもひいた？」"


show char tmi01f2 at left
with dis



voice "Miya_0336"
m "「ちょっと疲れているだけよ。今日は一日、部屋で寝ているわ」"


show char tri03f2 at right as r
with dis



voice "Risa_0689"
r "「そ、そう……」"
voice "Miya_0337"
m "「わたくしは行けないけど、璃紗はクルーズ楽しんできてね」"
voice "Risa_0690"
r "「……わかったわ、じゃあ……」"


#allClear:
hide char tmi01f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg37a
with dis


"そう言いながらも、璃紗はすごく残念そう。"
"寂しげに一人、行ってしまった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・昼
scene bg bg37a
with dis



#mes on
#system on


show char tmi01f2
with dis



voice "Miya_0338"
m "「………………さてと」"
"部屋に１人になったわたくしは、小声で呟いた。"


show char tmi03f2
with dis



voice "Miya_0339"
m "「……璃紗……ごめんなさい」"
"去り際の寂しそうな璃紗を思い出すと、罪悪感はあったけれど。"
voice "Miya_0340"
m "「こうするしかなかったのよ……」"
"そう、自分に言い聞かせる。"
"本当は具合なんて、悪くはなかった。"
"仮病を装っただけ。"
"あるものを、手に入れる為に。"
voice "Miya_0341"
m "「仮病とはいえ、一応は布団の中にいないとね……」"


#allClear:
hide char tmi03f2
#lastBG:
#scene bg bg37a
with dis


"ベッドの中に体をすべりこませて、横になる。"
"そして、そこでこれから起きるであろう『ある事』を、信じて待つ。"
voice "Miya_0342"
m "「………………」"
"さっきまでは部屋の外で、たくさんの人の出入りする音が聞こえてきたけれど。"
"みんなもうビーチに行ってしまったので、今は静かだ。"
"たまにホテルの従業員が、ドアの外を行き来するのが聞こえるけど。"
voice "Miya_0343"
m "「本当に……静かだわ……」"
"そのまま耳をすまして、じっとしている。"
"自分が思い描いたことを、ひたすらに信じて。"
voice "Miya_0344"
m "「………………ん……？」"
"遠くから聞こえてくる、走ってくる足音……"
voice "Miya_0345"
m "「……きたわ」"
"その音は、この部屋の前で止まり、そしてゆっくりとドアが開く。"

#//SE：ドアの開く音
#♀SE015
play sound "sound/SE015.ogg"


show char tri03m
with dis



voice "Risa_0691"
r "「はぁ、はぁ……美夜、具合どう？」"
voice "Miya_0346"
m "「………………」"
"そこには、わたくしが心配で戻ってきた、璃紗の姿があった。"
"信じていた通り……だったわ。"


show char tmi03p at left
show char tri03m at right as r
with dis



voice "Miya_0347"
m "「璃紗……クルーズは？」"


show char tri01m at right as r
with dis



voice "Risa_0692"
r "「みんなには、私も行けなくなったって言ってあるわ」"
"そう言うなり、璃紗はベッドの近くに腰掛けて、わたくしの額に触れる。"


show char tri03m at right as r
with dis



voice "Risa_0693"
r "「熱とかはない？　美夜は無理すると、すぐに体調を崩すから……」"
voice "Miya_0348"
m "「………………」"


show char tri01m at right as r
with dis



voice "Risa_0694"
r "「熱はないみたいね……下に行って薬もらってこようかしら。病状、詳しく聞かせて？」"
"璃紗はあれこれと、気を使ってくれる。"
"本当にわたくしが、病気だと思っている。"
"これ以上、嘘をつき続けても……意味はないわね。"
"わたくしは本当のことを、璃紗に告白した。"
voice "Miya_0349"
m "「あの……ごめんなさい、璃紗」"


show char tri03m at right as r
with dis



voice "Risa_0695"
r "「美夜……？」"
voice "Miya_0350"
m "「具合悪いなんて、実は嘘なのよ」"
voice "Risa_0696"
r "「えっ？」"
voice "Miya_0351"
m "「仮病なの」"
voice "Risa_0697"
r "「な、なぁーんだ……はぁ～」"
"安心して、力が抜けたようにその場に座り込む。"
"でも、すぐに理由を聞かれた。"
voice "Risa_0698"
r "「もう、美夜ったら……なんでそんな嘘ついたの？」"
voice "Miya_0352"
m "「みんなといるのも楽しいけど、本当は……」"
voice "Risa_0699"
r "「本当は……何なの？？」"
voice "Miya_0353"
m "「本当はね、もっと……璃紗と、２人きりでいたいのよ……」"


show char tri04m at right as r
with dis



voice "Risa_0700"
r "「えええっ！　もう、美夜ったら……」"
voice "Miya_0354"
m "「……怒った、璃紗？」"


show char tri08m at right as r
with dis



voice "Risa_0701"
r "「もちろんよ、他のみんなも美夜の事、とっても心配していたのよ」"
voice "Miya_0355"
m "「そう……」"


show char tri03m at right as r
with dis



voice "Risa_0702"
r "「私だって……すっごく、心配したんだから……」"
voice "Miya_0356"
m "「悪かったわ、ごめんなさい」"
voice "Risa_0703"
r "「もう、もう、もう……ぷっ」"
"最初は怒っていた璃紗だけど、そのうち吹き出してしまった。"
voice "Miya_0357"
m "「璃紗……？」"


show char tri01m at right as r
with dis



voice "Risa_0704"
r "「私もね、実はちょっとだけ同じ気持ちだったのよ……美夜と」"


show char tmi04p at left
with dis



voice "Miya_0358"
m "「えっ、璃紗も？」"
voice "Risa_0705"
r "「ええ。みんなと一緒も楽しいけれど、今ここに美夜と２人っきりだったら素敵なのに……って思ったこと、何度かあったの」"


show char tmi01p at left
with dis



voice "Miya_0359"
m "「璃紗……ぁぁ」"
"璃紗もわたくしと、同じ気持ちでいてくれたんだわ。"
"それが今、すごく嬉しい。"
voice "Risa_0706"
r "「今日だけはずっと、一緒にいようね……美夜」"
voice "Miya_0360"
m "「璃紗……」"


#allClear:
hide char tmi01p at left
hide char tri01m at right as r
#lastBG:
#scene bg bg37a
scene black
with Dis


#※EV010
scene bg EV10
with Dis


voice "Risa_0707"
r "「もう、美夜ったら……甘えんぼうね」"
voice "Miya_0361"
m "「……たまには、いいでしょう？」"
voice "Risa_0708"
r "「そうね……なんか、嬉しい{image=image/exch001.png}」"
"わたくしはベッドの上で寝そべりながら、璃紗の膝の上に頭を乗せて、うっとりしていた。"
"行けなかったクルージング気分を取り戻そうという璃紗の提案に乗って、水着にまで着替えてしまった。"
"こういうの、初めてかも……すごく気恥ずかしいけれど、ドキドキしてきた。"
"でも何だか無性に、璃紗に甘えたかった。"
voice "Miya_0362"
m "「璃紗……本当にごめんなさい」"
voice "Risa_0709"
r "「もう謝らないで、美夜。私、本当に嬉しいのよ……」"
"そう言いながら、璃紗がわたくしの黒髪を、そっと手で撫でてくれた。"
"ああ……なんか、とっても心地良い。"
"愛しい璃紗と、こんな幸せな時間を与えてもらえるのは、この世でわたくしだけなのよね……"


#※EV010P1
scene bg EV10p1
with Dis



voice "Risa_0710"
r "「美夜、たまには私に甘えてね……なんかこういうの、嬉しいわ」"
voice "Miya_0363"
m "「璃紗ったら……いつもは璃紗の方が、わたくしに甘えている感じだものね」"
voice "Risa_0711"
r "「そ、そんな事は………………ある、かも……」"
voice "Miya_0364"
m "「わたくし、こうやって貰えて、幸せよ……ありがとう、璃紗」"
"ちょっとだけ、嬉し涙が浮かんでしまった。"
"そんなわたくしを見つめて、璃紗は優しく穏やかに微笑んでいた。"
"嬉しい……嬉しすぎて、思わず璃紗の腰に抱きついてしまった。"
voice "Risa_0712"
r "「あんっ、もう……美夜ったら……」"
voice "Miya_0365"
m "「ありがとう、璃紗……んちゅっ」"
"璃紗の可愛い太股に、唇をつける。"
"それだけで璃紗は、可愛い声をもらした。"
voice "Risa_0713"
r "「んんっ……いきなりなんだから、美夜は……」"
voice "Miya_0366"
m "「今日はずっと……一緒ね」"
voice "Risa_0714a"
r "「ええ……一緒よ」"
"満たされなかったものを、埋めるように。"
"わたくしは璃紗の体を抱きしめて、愛撫のようなキスを続けた。"
"今日一日、愛しい璃紗を独り占め出来る幸福に酔いながら……"


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

scene image eyecatch05
#wipe vshutter#############################

#wait 3000

scene black
with Dis

#log on
#waitcancel enabled
#wipecancel enabled


#//END
jump S025


