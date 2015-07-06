#「玲緒、麻衣宅を訪問」

label S115:
$ save_name = "◇玲緒、麻衣宅を訪問"


#**玲緒の部屋・昼
scene bg bg33a
with Dis



#mes on
#system on


#♂MP13
play music "sound/BGM21.ogg"


show char tre03f2
with dis



voice "Reo_0764"
re "「麻衣……」"
"委員会を終えて、家に１人で戻って。"
"この後は、デパ地下で買ってきた惣菜で味気ない食事をして。"
"あとはただただ、ぼんやりとするだけで。"
"そしていつも考えてしまうのは、麻衣のことばかり。"


show char tre08f2
with dis



voice "Reo_0765"
re "「麻衣……もう、なんでワタシを放っておくのよぉー」"
"麻衣がいないのなら、エアコンも使い放題だし、お菓子だっていっぱい食べられる。"
"それってまさに、夢のような生活なのに。"


show char tre03f2
with dis



voice "Reo_0766"
re "「こんなの、つまんない……こんなの全然つまんないわよぉ」"
"麻衣に会いたい。"
"麻衣に会って、いっぱいわがまま言って甘やかしてもらいたい。"


show char tre10f2
with dis



voice "Reo_0767"
re "「うううっ……麻衣、まいぃっ！！」"

#//回想
show char moyan
show char tma03f2
with dis



voice "Mai_0722"
ma "「玲緒ったら、本当にわがままなんだから」"


show char tma08f2
with dis



voice "Mai_0723"
ma "「いーい、今度無駄遣いしたら、何も作ってあげないわよ」"


show char tma02f2
with dis



voice "Mai_0724"
ma "「あーもう、可愛い！　玲緒可愛すぎよぉー{image=image/exch001.png}」"

#//回想ここまで
#allClear:
hide char moyan
hide char tma02f2
#lastBG:
#scene bg bg33a
with dis


"麻衣の言葉がいっぱいいっぱい、頭の中に浮かんでくる。"


show char tre09f2
with dis



voice "Reo_0768"
re "「うーっ！　もうこんなのやだ、やだやだ、我慢できない」"
"もう直接、麻衣に会いに行ってしまおう。"
"そう考えたら、いてもたってもいられなくて。"
"ワタシは大急ぎで、出かける用意をする。"


show char tre03f2
with dis



voice "Reo_0769"
re "「何しに来たとか、言わないよね……麻衣」"
"事前にメールでもした方がいいのかな？"
"でも……また明日にしてとか、言われたらイヤだし。"
voice "Reo_0770"
re "「今すぐ、どうしても麻衣に会いたいんだもんっ」"
"だったら今よ、今行くしかないの。"
voice "Reo_0771"
re "「……あっ、そうだ」"
"カバンの中に、ノートをいれる。"


show char tre01f2
with dis



voice "Reo_0772"
re "「しゅ、宿題のわかんないとこ聞きに来たって、ことにしよう……本当にわかんないし♪」"


#allClear:
hide char tre01f2
#lastBG:
#scene bg bg33a
with dis


"待っててね、麻衣。"
"すぐに押しかけるから。"
"ワタシはそのまま部屋を飛びだしていった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**沢口家ダイニング・夜
scene bg bg15c
with Dis



#mes on
#system on


show char tre03f2
with dis



voice "Reo_0773"
re "「はぁ……はぁ、はぁ……麻衣……」"


show char tma04f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0725"
ma "「れっ、玲緒！？」"


#allClear:
hide char tma04f2 at left
hide char tre03f2 at right as r
#lastBG:
#scene bg bg15c
with dis


"麻衣の家に着くと、麻衣がすぐに出てきてくれた。"
"ワタシは用意していたノートを取りだして、麻衣に突きつけるつもりだったけど。"
"でも………………"

#//SE：バサッ（ノートの落ちる音）
#♀SE057
play sound "sound/SE057.ogg"


"麻衣の顔を見たら……"
"いっぱいいっぱい、涙が溢れてきて。"


stop music fadeout 1


#※EV074
scene bg EV74
with Dis


play music "sound/BGM14.ogg"


voice "Reo_0774"
re "「うわーん、まぁいー！」"
voice "Mai_0726"
ma "「ちょ、ちょっと玲緒……」"
"麻衣に抱きついて、そのまま泣き出してしまった。"
voice "Mai_0727"
ma "「……玲緒……」"
voice "Reo_0775"
re "「麻衣のばかぁー、ワタシを１人ぼっちにして～」"
voice "Mai_0728"
ma "「……ごめん、ごめんね、玲緒」"
"麻衣がワタシを抱きながら、背中をとんとん叩いてくれる。"
"でもワタシは、ぜんぜん涙が止まらなかった。"
voice "Reo_0776"
re "「麻衣が悪いんだから、責任とりなさいよねぇ……ううっ、うわあああん」"
voice "Mai_0729"
ma "「わかった、わかったわよ、玲緒」"


#※EV074P1
scene bg EV74p1
with Dis



voice "Mai_0730"
ma "「寂しい思いをさせて、ごめんね……玲緒」"
voice "Reo_0777"
re "「まい……ぅぅっ、くすん……」"
"ワタシが泣き止むまで、麻衣はずっとワタシを抱きしめてくれていた……"


stop music fadeout 1


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


play music "sound/BGM09.ogg"


#**麻衣の部屋・夜
scene bg bg14c
with Dis



#mes on
#system on


show char tma03f2
with dis



voice "Mai_0731"
ma "「少し落ち着いた？　何か飲む？」"


show char tma03f2 at left
show char tre01f2 at right as r
with dis



voice "Reo_0778"
re "「ジュース、オレンジのやつ」"


show char tma01f2 at left
with dis



voice "Mai_0732"
ma "「わかったわ、今持ってくるわね」"


#allClear:
hide char tma01f2 at left
hide char tre01f2 at right as r
#lastBG:
#scene bg bg14c
with dis


"麻衣のくれたジュースを飲む頃には、ワタシの涙もすっかり引っ込んでいた。"


show char tre03f2
with dis



voice "Reo_0779"
re "「あの、麻衣……」"


show char tma01f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0733"
ma "「うん？　なぁに」"
"ワタシは思い切って、聞いてみることにした。"
"ここのところ、ずっと引っかかっていたことを。"
voice "Reo_0780"
re "「麻衣はどうして、うちに来れなくなったの？」"


show char tma03f2 at left
with dis



voice "Mai_0734"
ma "「そ、それは……」"
"麻衣は少し、悩んでいるみたいだった。"
voice "Reo_0781"
re "「ねぇ、教えてよ。ワタシと一緒にいるの、イヤになったの？」"


show char tma01f2 at left
with dis



voice "Mai_0735"
ma "「バカねぇ、そんなことあるはずないでしょう」"
voice "Reo_0782"
re "「だったら……なんで？」"


show char tma03f2 at left
with dis



voice "Mai_0736"
ma "「だからね……玲緒に心配、かけたくなくて」"
voice "Reo_0783"
re "「心配……？」"
voice "Mai_0737"
ma "「でもその結果、玲緒を泣かしてしまったから、そうも言ってられなくなったわね」"
"そして麻衣は、ずっと隠していたことを、ワタシに打ち明けてくれた。"


show char tma08f2 at left
with dis



voice "Mai_0738"
ma "「実はね、うちのお母さんが今、入院しているのよね」"


show char tre04f2 at right as r
with dis



voice "Reo_0784"
re "「えっ、にゅういん？」"
voice "Mai_0739"
ma "「お母さんの実家の、近く……ウチから電車で２時間くらい掛かる所のね、病院に今いるのよ」"


show char tre03f2 at right as r
with dis



voice "Reo_0785"
re "「そんな、遠くに……」"
"ビックリした。"
"最近、麻衣の家には全然来てなかったから、麻衣のお母さんが具合悪いなんて、気づきもしなかった。"
"最後に麻衣のお母さんを見たのは、もうずいぶん前かもしれない。"
"あの時は、とても元気そうだったのに……"


show char tma01f2 at left
with dis



voice "Mai_0740"
ma "「週末は病院に行って、お母さんの世話をして、平日は弟や妹の面倒を見たりで……とにかく、忙しかったのよ」"
voice "Reo_0786"
re "「そう……だったんだ」"


show char tma03f2 at left
with dis



voice "Mai_0741"
ma "「そんなわけで、委員会や玲緒の家に顔が出せなかったのよ。ごめんね、玲緒」"
voice "Reo_0787"
re "「う、うん……」"
"なんだ、そんな理由だったんだ。"
"それだったら、早く言ってくれたら……"
"ワタシだって、こんなに悩んだりしなかったのに。"
voice "Reo_0788"
re "「ま、麻衣も、大変だったのね」"


show char tma02f2 at left
with dis



voice "Mai_0742"
ma "「ええ、でも……ふふふっ{image=image/exch001.png}」"
voice "Reo_0789"
re "「何にやついてるのよ……ヘンなの」"
voice "Mai_0743"
ma "「大変だったけど、まさか玲緒が寂しくなっちゃって、会いに来てくれるなんて」"
voice "Reo_0790"
re "「ち、違うもん、ほらノート、これ見てよ」"
voice "Mai_0744"
ma "「うんうん、ノートね。見たわよ」"
voice "Reo_0791"
re "「ワタシは宿題がわからなくて、仕方なく麻衣の家に……」"
voice "Mai_0745"
ma "「そういうベタな、ツンデレ発言はいいから」"


show char tre04f2 at right as r
with dis



voice "Reo_0792"
re "「うにゃぁぁっ！？」"
"麻衣がぐいぐい、迫ってくる。"
voice "Mai_0746"
ma "「はぁ、はぁ、玲緒可愛い{image=image/exch001.png}　わたしも玲緒に会えなくて、すごく寂しかったのよ」"


show char tre05f2 at right as r
with dis



voice "Reo_0793"
re "「近いちかい、顔が近いわよ、麻衣～」"
voice "Mai_0747"
ma "「わたしも、寂しくて……欲求不満なのよー」"
"と言いながら、麻衣がワタシを押し倒そうとしてくる。"
voice "Reo_0794"
re "「やめてー、麻衣のエロスっ！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#mes on
#system on


"……しかしその後、麻衣の弟や妹が部屋に入ってきてしまって。"
"麻衣の押し倒しは未遂に終わったのだった。"


stop music fadeout 1


play music "sound/BGM12.ogg"


#**麻衣の部屋・夜
scene bg bg14c
with Dis



#mes on
#system on


show char tma01f2
with dis



voice "Mai_0748"
ma "「玲緒、どうせなら今日、うちでご飯食べていきなさいよ。１人くらい増えても変わらないから」"


show char tma01f2 at left
show char tre03f2 at right as r
with dis



voice "Reo_0795"
re "「う……うん……」"


#allClear:
hide char tma01f2 at left
hide char tre03f2 at right as r
#lastBG:
#scene bg bg14c
with dis


"麻衣に言われて、ワタシはその後も、麻衣の家にいることにした。"
"ご飯ができるまでの間、ワタシは麻衣に言われて、宿題をしていたけれど。"


show char tre03f2
with dis



voice "Reo_0796"
re "「うううー、難しい……わかんないよ、こんなの……あっ！」"
"そうだわ。"
"こっそり麻衣のノート探して、そのまま丸写ししちゃえばいいわ。"
voice "Reo_0797"
re "「えっと、どこかな……」"
"うーん、見つからない。"
"麻衣、わざと隠したのかしら。"


show char tma09p
with dis



voice "Mai_0749"
ma "「もう、ダメでしょう、あなたたちはっ！」"


show char tre04f2
with dis



voice "Reo_0798"
re "「ひぃぃっ！」"
"麻衣の怒った声が聞こえてきて、思わず体が飛びあがった。"


#allClear:
hide char tre04f2
#lastBG:
#scene bg bg14c
with dis


voice "Mobmaibrz0000"
mao "「だって、こいつが」"
voice "Mobmaisis0000"
mai "「ちがうもん、おにいちゃんが」"


show char tma08p
with dis



voice "Mai_0750"
ma "「いつもいつも、ケンカばかりしないで、たまにはおとなしくしてなさい」"


show char tre03f2
with dis



voice "Reo_0799"
re "「な、なんだ……弟や妹に言ってたんだ、ほっ」"
"ワタシは部屋のドアを少し開けて、キッチンを覗き見る。"


#**沢口家ダイニングキッチン・夜
#allClear:
hide char tre03f2
#lastBG:
#scene bg bg14c
scene bg bg15c
with Dis



show char tma08f2
with dis



voice "Mai_0751"
ma "「いーい、ケンカするヒマがあるなら、お茶碗並べたりとか、お手伝いしてよ」"
voice "Mobmaisis0001"
mai "「えーっ、やだぁ」"
voice "Mobmaibrz0001"
mao "「それは、麻衣おねえちゃんの仕事だろ」"
voice "Mai_0752"
ma "「もうー」"


#allClear:
hide char tma08f2
#lastBG:
#scene bg bg15c
with dis


"学校と病院、そして弟と妹の世話。"
"麻衣はどこか、疲れているように見えた。"
"よく見ると、顔色もちょっと悪いし。"
"学校では決して見せない、イライラした感じだし。"


show char tre03p
with dis



voice "Reo_0800"
re "「麻衣……すごく大変そう」"
"ワタシ、麻衣に何かしてあげられないかな。"
"むくむくと、そんな気持ちが芽生えてくる。"


show char tma01f2
with dis



voice "Mai_0753"
ma "「じゃあ２人とも、ご飯ができるまで大人しくテレビでも見てなさい」"


#**麻衣の部屋・夜
#allClear:
hide char tma01f2
#lastBG:
#scene bg bg15c
scene bg bg14c
with Dis



show char tre03f2
with dis



voice "Reo_0801"
re "「あっ……」"
"麻衣がこっちの部屋に入ってくる。"
"ワタシは慌ててドアを閉めると、ちゃんと座ってノートに向かった。"


show char tma03f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0754"
ma "「玲緒、宿題しているところ悪いけど、テレビつけていいかしら？」"
voice "Reo_0802"
re "「う、うん……」"
voice "Mai_0755"
ma "「じゃあ、あなた達おとなしくしているのよ……はぁ」"
"大きくため息をつく、麻衣。"
"やっぱり疲れちゃってるんだわ。"
"よし、こうなったら……"


show char tre04f2 at right as r
with dis



voice "Reo_0803"
re "「ま、麻衣っ！！」"
voice "Mai_0756"
ma "「うん？　どうしたの、玲緒。もうお腹すいた？　あと少しだから……」"


show char tre01f2 at right as r
with dis



voice "Reo_0804"
re "「そうじゃなくて、ワタシも麻衣を手伝う」"
voice "Mai_0757"
ma "「玲緒……気持ちは嬉しいけれど、あなた料理はさっぱり……」"
voice "Reo_0805"
re "「うん、だからワタシ、この子たちの面倒、見てあげるっ！」"
"ワタシは麻衣の弟と妹を指差して、麻衣に宣言した。"
voice "Mai_0758"
ma "「玲緒が……うちの弟と妹を？」"


show char tre08f2 at right as r
with dis



voice "Reo_0806"
re "「ワタシだって、麻衣の力になるもん……できるもん！」"
voice "Mai_0759"
ma "「玲緒、本気で言ってるの？」"
voice "Reo_0807"
re "「もちろん本気よ、武士にニ言はないわ！」"


show char tma01f2 at left
with dis



voice "Mai_0760"
ma "「別に玲緒は、武士じゃないでしょう……ふふふっ」"
voice "Mai_0761"
ma "「でも、玲緒が面倒見てもらう側になりそうだけどね」"
voice "Reo_0808"
re "「な、なによ、ワタシだって、やるときはしっかりやるもんっ！」"
voice "Mai_0762"
ma "「うん、わかったわ。じゃあ２人とも、玲緒をよろしくね～」"


#allClear:
hide char tma01f2 at left
hide char tre08f2 at right as r
#lastBG:
#scene bg bg14c
with dis


"麻衣の言葉に、麻衣の弟たちはうんうん頷いた。"
"もう、ワタシは本気だっていうのに、麻衣ったらすぐからかうんだから。"
"とにかく、舐められないよう、最初にビシッと言っておかないとね。"


show char tre08f2
with dis



voice "Reo_0809"
re "「ちょっとアンタたち、これからはワタシが面倒見てあげるから、ワタシの言うことをちゃんと聞きなさいよ……って、聞いてるの！？」"
voice "Mobmaisis0002"
mai "「わーっ、あぶないーっ」"
voice "Mobmaibrz0002"
mao "「いけいけ、そこだーっ！」"
"２人はワタシの方など見向きもせず、テレビのアニメに夢中になっていた。"


show char tre03f2
with dis



voice "Reo_0810"
re "「ううっ……これだからお子様は……」"
"ああ、うまくやっていけるのかな、ワタシ……"


show char tma01f2
with dis



voice "Mai_0763"
ma "「玲緒」"
"すると麻衣が、困っていたワタシを呼んだ。"
voice "Mai_0764"
ma "「玲緒がこんなこと言ってくれるなんて、正直思わなかったわ……ありがとう、感謝しているわ」"


show char tre01f2
with dis



voice "Reo_0811"
re "「麻衣……任せて、頑張るからっ！！」"


#**夜空
#allClear:
hide char tre01f2
#lastBG:
#scene bg bg14c
scene bg bg42c
with Dis



"こうして麻衣のいない時間だけ、ワタシはこの家で、麻衣の弟と妹の世話をすることになったのだった。"


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
jump S116



