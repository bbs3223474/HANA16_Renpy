#「まだまだ、新米カップル」

label S033:
$ save_name = "◇まだまだ、新米カップル"


#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP06
play music "sound/BGM06.ogg"


"付き合う前は、沙雪さんといつも一緒にいられたら、どんなに素敵なんだろう……って思っていた。"
"ずっとずっと、そうしたいと思っていた。"
"……なのに、それがいざ現実になると。"
"こんなにも、恥ずかしいことだったなんて……"


show char trk05s2
with dis



voice "Rikka_0729"
rk "「あ、あの……沙雪さん」"


show char trk05s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0310"
s "「なんですか、六夏さん{image=image/exch001.png}」"
voice "Rikka_0730"
rk "「校内で堂々と、手をつなぐというのは……」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0311"
s "「あら、いけないのですか？　私たち、恋人同士なんですから」"
"愛しい彼女にきっぱりそう言われては、ズキュンとするしかないよね。"
"でもまだ恋愛未熟なワタシは、沙雪さんの無垢な愛を直接受け取ることはできなかった。"


show char trk03s2 at left
with dis



voice "Rikka_0731"
rk "「なんていうか……ワタシ、手に汗かいちゃっているし、汚くないかなぁ……なんて」"
voice "Sayuki0312"
s "「そのようなこと、ありません。六夏さんの手を汚いだなんて、絶対に思いません」"


show char trk01s2 at left
with dis



voice "Rikka_0732"
rk "「沙雪……さん……」"


show char tsy03s2 at right as r
with dis



voice "Sayuki0313"
s "「ですがもし、六夏さんが嫌だとおっしゃるのでしたら……」"


show char trk04s2 at left
with dis



voice "Rikka_0733"
rk "「い、いえ、別に嫌なのではなくて、ですね……な、ななななっ！！」"


show char tsy02s2 at right as r
with dis



voice "Sayuki0314"
s "「ふふっ……んふふっ{image=image/exch001.png}」"
"今度はなんと、腕組みをしてしまった。"
voice "Sayuki0315"
s "「これでしたら、良いですよね？」"


show char trk05s2 at left
with dis



voice "Rikka_0734"
rk "「ううううっ……」"
"嬉しくないわけ、ない。"
"なんと言うか、もう……気絶しそう、今週の幸運を全部使い果たしたって感じ。"
"沙雪さんが近くにいるだけで、ドキドキするし……ふわっと、良い匂いもしてくるし。"
"でもでも、周りから向けられる目線が……ああ、もう耐えられないかも。"


show char tsy01s2 at right as r
with dis



voice "Sayuki0316"
s "「六夏さん、おでこの方にも汗をかいておりますわ。暑いのですか？」"


show char trk03s2 at left
with dis



voice "Rikka_0735"
rk "「あっ、うん……暑いよ、今日も暑いよね」"
"汗は汗でも、冷や汗の方なんだけど。"
"すると沙雪さんは、サッと白いレースのハンカチを出して、ワタシの汗をそっと拭おうとしてくれた。"


show char trk01s2 at left
with dis



voice "Rikka_0736"
rk "「沙雪さん……」"
##voice SAYUKI0317
#【沙　雪】「少しだけ屈んでいただけますか、六夏さん。ちょっと届かなくて」
"必死に背伸びしている姿が、どこか健気で。"
"ワタシはつい、彼女が拭きやすいように腰を落とした。"
"その瞬間、周りからため息が漏れた。"
voice "mobJyosiA0064"
mobA "「ああ……姫が騎士の汗を拭っていますわ。普段とは逆に、姫の方が献身的なのもいいですわね」"
voice "mobJyosiB0040"
mobB "「ええ、きっとこれが『萌え』というものなのかしら{image=image/exch001.png}」"
voice "mobJyosiA0065"
mobA "「とにかく本当に、素敵なお二人ですわ……目が放せません」"
"ただ、ちょっと汗を拭いてもらっているだけで、この言われよう。"
"ダメ、もう自分がいたたまれない。"


show char trk03s2 at left
with dis



voice "Rikka_0737"
rk "「さ、沙雪さん、もう汗はいいですよ」"
voice "Sayuki0318"
s "「いいえ、まだです。もう少しだけ、我慢してくださいね」"
"本当ならすぐ、この場から離れたかったけれど。"
"沙雪さんに諭すように言われたせいで、動くに動けなかった。"
voice "Rikka_0738"
rk "（もう、ダメかも……心労で倒れそう……あぁ）"


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


#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


"授業が終わり、昼休みになった。"
"今は特に注目もされておらず、一安心って感じ。"


show char trk01s2
with dis



voice "Rikka_0739"
rk "「今日もまた、学食の日替わりかな……あっ、でも売店でパンでもいいかも」"
voice "Rikka_0740"
rk "「どっちにしても、混み合う前に行ってこないと……んっ？」"
"沙雪さんの周りにまた、人が集まっていた。"


show char trk03s2
with dis



voice "Rikka_0741"
rk "「恥ずかしい話とか……してないよね？」"


#allClear:
hide char trk03s2
#lastBG:
#scene bg bg04a
with dis


"どうしても心配になって、近くに見に行ってしまう。"
"無関係ではいられない気がしたから。"
voice "mobJyosiC0017"
mobC "「沙雪さん、わたくし達、今日は天気が良いので、中庭でお昼を食べようと思っているんです」"
voice "mobJyosiD0004"
mobD "「もしよかったら、ご一緒しませんか？」"


show char trk01s2
with dis



voice "Rikka_0742"
rk "「なんだ、そういう話か……ホッ」"
"お昼に誘われていただけだった。"
"声をかけているのは比較的、沙雪さんと仲の良いグループの子たちだし。"
voice "Rikka_0743"
rk "「心配しすぎだったかも……」"
"ワタシも早いところ、お昼を買いに行かないと。"


show char tsy01s2
with dis



"教室を出ていこうとすると、不意に沙雪さんと目が合った。"


show char tsy02s2
with dis



"そして……ニッコリ微笑まれる。"


show char trk03s2
with dis



voice "Rikka_0744"
rk "「？？？」"


show char tsy01s2
with dis



voice "Sayuki0319"
s "「皆さん、申し訳ありません。私はこれからはいつも。六夏さんとお食事をとることにしたいと思いまして……」"


show char trk04s2
with dis



voice "Rikka_0745"
rk "「えええぇぇぇぇっ！！」"


#allClear:
hide char trk04s2
#lastBG:
#scene bg bg04a
with dis


"ワタシのその叫びは『きゃあー』という、黄色い声の連呼にかき消された。"
voice "mobJyosiC0018"
mobC "「そうですわね、お二人はカップルですものね」"
voice "mobJyosiD0005"
mobD "「お二人の時間を邪魔したりできませんわ……失礼しました」"
voice "mobJyosiC0019"
mobC "「あっ、六夏さんが沙雪さんを迎えに来ていますわ」"
"ワタシの前にいた子たちが、場所をあけてくれる。"
"まさにモーゼの十戒のごとく、ワタシと沙雪さんの間に１本の道が出来た。"
"沙雪さんはお弁当箱をかかえて、ゆっくりと立ち上がる。"


show char tsy01s2
with dis



voice "Sayuki0320"
s "「それでは、行きましょうか……六夏さん」"


show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Rikka_0746a"
rk "「は、はい……沙雪さん……」"
voice "mobJyosiA0066"
mobA "「いってらっしゃい」"
voice "mobJyosiB0041"
mobB "「素敵な午後をお過ごしくださいね、ふふふっ」"


#allClear:
hide char trk01s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"な、なんだろう、これ？"
"声援と見守るような視線の中で、ワタシと沙雪さんは教室を出ていった。"
"雰囲気的に、出ていかざるを得なかった。"


#**新校舎廊下・昼
scene bg bg05a
with Dis



show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0321"
s "「六夏さん、お弁当はお持ちですか？」"


show char trk03s2 at left
with dis



voice "Rikka_0746b"
rk "「今日は……実は、持ってきてなくて」"
"今更、学食や購買に付き合わせるのは悪いし……"
"ちょっと困り顔のワタシに、沙雪さんが嬉しそうに微笑んだ。"


show char tsy02s2 at right as r
with dis



voice "Sayuki0322"
s "「良かったです。無駄にならずにすみました」"
voice "Rikka_0747"
rk "「良かったって……どういうことですか？」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0323"
s "「そういうこともあると思いまして、実は……２人分持ってきたんです、お弁当を」"
voice "Rikka_0748a"
rk "「そ、そんな……悪いです」"
voice "Sayuki0324"
s "「遠慮せず、食べてくださいね」"
"ああ、もう……困っちゃうくらい、嬉しくてたまらない。"
"いつしか困惑や戸惑いが、喜びの感情で上書きされていく。"


show char trk01s2 at left
with dis



voice "Rikka_0748b"
rk "「ほ、本当にありがとうございます！　じゃあ飲み物だけでも、ワタシが買ってきますので」"
voice "Sayuki0325"
s "「そうですか……でしたら私、また学食の紙パックのジュースがいいです」"
voice "Rikka_0748c"
rk "「わかりました、すぐ買ってきますね！」"


#**青空
#allClear:
hide char trk01s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg05a
scene bg bg42a
with dis



"こうしてワタシ達は２人で一緒に、お昼を食べました。"
"愛しい彼女の作ってくれた、和風のおかずのお弁当。"
"あまりに緊張して、興奮して、夢見心地でもあって。"
"ワタシはきっと一生、この２人で初めて食べたランチのことは、忘れないと思った。"


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



voice "Rikka_0749"
rk "「ふぁ……ふぁぁ～」"
"午後の授業ってどうして、こんなに眠いのだろうか。"
"沙雪さんのお弁当はとても美味しくて、楽しいランチタイムを過ごせたけれど。"
"教室に戻ったら戻ったで、みんなからあれこれ聞かれたり、生暖かい視線を向けられたり。"
"それが、すごく恥ずかしくて……辛かった。"
voice "Rikka_0750"
rk "「ひょっとして、これがずっと続くのかな……はぁ～」"
"沙雪さんと恋人としてお付き合いする以上、今後もずっと、こんな目で見られていくのかな……"
voice "Rikka_0751"
rk "「すっごく幸せなのに……気が重いなぁ」"
"何事にもオープンな性格の沙雪さんに、ワタシはどうすれば良いのかわからなかった。"
"きっとこれ以上考えても、答えは出ないと思えてならない……このままでは。"
voice "Rikka_0752"
rk "「やっぱり……誰かに相談してみようかな」"
"と言っても、ワタシが相談出来る相手なんて、あの人しかいないのだけれど。"


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


show char trk10s2
with dis



voice "Rikka_0753"
rk "「リサ姉～」"


show char tri03s2 at left
show char trk10s2 at right as r
with dis

#voice RISA_0817
#voice RISA_0818
#voice RISA_0819

voice "Risa_0820"
r "「六夏……まったく」"


#allClear:
hide char tri03s2 at left
hide char trk10s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"ワタシはいつものように、リサ姉に泣きついていた。"
"きっと『やれやれ』って、思われているのだろう。"
"それでも今のワタシにとって、他の誰よりも頼れる人だから。"


show char tri01s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0821"
r "「恋愛相談はもう、終わったと思ったんだけど……まあ、いいわ」"
"人の良いリサ姉は、ワタシの話をちゃんと最後まで聞いてくれた。"


show char tri03s2 at left
with dis



voice "Risa_0822"
r "「うーん、そうね……」"
voice "Rikka_0754"
rk "「リサ姉……」"
"さすがのリサ姉も、今回は回答に戸惑っているように見えた。"
"それでもやがて、ワタシをたしなめるように言い聞かせた。"


show char tri01s2 at left
with dis



voice "Risa_0823"
r "「沙雪さんがみんなに話してしまうってことは、それだけ彼女が六夏を想っているって事じゃないの？」"


show char trk05s2 at right as r
with dis



voice "Rikka_0755"
rk "「そ、それは……まあ……」"
"その通りだとは思うし、嬉しくもあるんだけれど。"
voice "Risa_0824"
r "「ね、素直に喜んだら？」"
voice "Rikka_0756"
rk "「そ、そうだよね……うん」"
voice "Risa_0825"
r "「何にせよ、付き合い始めって一番楽しいじゃない？　もう少し六夏も、恋愛を楽しめばいいのよ」"


show char trk03s2 at right as r
with dis



voice "Rikka_0757"
rk "「うーん、だけど……っ！？」"

#//SE：ドアの開く音
#♀SE019
play sound "sound/SE019.ogg"


"突然、教室のドアが激しくバン、と開いた。"


show char tri03s2 at left
with dis



voice "Risa_0826"
r "「えっ？」"
voice "Rikka_0758"
rk "「み、みっ……美夜……さま……」"


#allClear:
hide char tri03s2 at left
hide char trk03s2 at right as r
#lastBG:
#scene bg bg04a
show char tmi08s2
with dis



voice "Miya_0416"
m "「………………」"
"振り返ると、そこにはものすごい形相の美夜さまが、仁王立ちしていた。"


show char tmi07s2
with dis



voice "Miya_0417"
m "「六夏さん……貴女また、わたくしの知らないところで、璃紗と……イチャイチャ逢瀬を！！」"


show char tmi07s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_0759"
rk "「こ、これは違います、そういうわけじゃなくて……」"
voice "Miya_0418"
m "「貴女と沙雪さんがデキているっていうの、やっぱりカモフラージュなのね。本命は美しくて可愛い璃紗なのね！？」"

hide char tmi07s2 at left
hide char trk03s2 at right as r
show char tri05s2 at sleft as l
show char tmi07s2
show char trk03s2 at sright as sr
with dis



voice "Risa_0827"
r "「も、もう……美夜ったら……」"
voice "Rikka_0760"
rk "「だから、もう……違いますぅ！！」"
"照れて喜び、赤くなったリサ姉とは対称的に、ワタシは血の気が引き、青くなっていた。"
"もう……どうしてこうなっちゃうんだろう。"
voice "Rikka_0761"
rk "「ワタシが好きなのは、沙雪さんだけです。でもそのことで悩んで、ついリサ姉に……」"
voice "Miya_0419"
m "「うるさい、問答無用よっ！！」"


#allClear:
hide char tri05s2 at sleft as l
hide char tmi07s2
hide char trk03s2 at sright as sr
#lastBG:
#scene bg bg04a
show char trk04s2
with dis



voice "Rikka_0762"
rk "「きゃ、きゃあぁん！」"
"いきなり美夜さまに飛びつかれそうになったワタシは、慌ててかわした。"


show char tri03s2
with dis



voice "Risa_0828"
r "「美夜、止めて。私だって、好きなのは美夜だけだし……」"


show char tmi07s2
with dis



voice "Miya_0420"
m "「ちょっと、待ちなさいっ！！」"


show char tri03s2
with dis



voice "Risa_0829"
r "「もう、美夜のバカ……私の言っていること、聞いてないし」"
"のろけるリサ姉の制止も聞かず、美夜さまがグングン、ワタシを追いかけてくる。"


show char tmi07s2
with dis



voice "Miya_0421"
m "「くっ……今日という今日は、許さないわよ」"


show char trk03s2
with dis



voice "Rikka_0763"
rk "「だから、誤解なんですよぉ～～～～」"


#allClear:
hide char trk03s2
#lastBG:
#scene bg bg04a
with dis


"その後、下校時間までの間。"
"ワタシは美夜さまに見つかる度に、追いかけまわされたのだった。"


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
jump S034



