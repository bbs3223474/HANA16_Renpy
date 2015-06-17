# 此脚本开始出现多个同屏立绘数量变化的场景。
# 经过实践，发现当屏幕上的立绘由两个变成三个，三个变成两个、一个，两个变成一个时，
# 必须要用hide命令将原来显示的所有立绘隐藏。
# 否则会出现立绘重叠现象。
# 例如，上个场景如果用过show char xx at left和at right as r，
# 那么下个场景如果要变成一个或者三个立绘，那么必须用hide将两个都隐藏，
# 再执行新的show命令。
# 如果是三个立绘变少，则用hide隐藏at sleft as l和at sright as sr的两个立绘。
# 

#「璃紗、三角関係発覚！？」

label S004:


$ save_name = "◇璃紗、三角関係発覚！？"


#**新校舎教室・昼
scene bg bg04a
show char alpha
with dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


voice "mobJyosiA0007"
mobA "「璃紗さん、ごきげんよう」"


show char tri01s2
with dis



voice "Risa_0118"
r "「ええ、ごきげんよう」"
voice "mobJyosiB0005"
mobB "「璃紗さん、お聞きになりました？」"


show char tri03s2
with dis



voice "Risa_0119"
r "「？？？」"
"教室に入った途端、私はクラスメイトたちに囲まれてしまった。"
"あれっ……私、何かしたかしら？"
"それともまた、美夜のこと？"
"私はとっさに、美夜の席の方を見てみた……けど、その姿は見えない。"
"どうやら今日も、サボりを決め込んでいるようだった。"


show char tri01s2
with dis



voice "Risa_0120"
r "「まったく、美夜ったら……ところで、何の話かしら？」"
voice "mobJyosiB0006"
mobB "「もちろん、１年生のベストカップルですわ」"
voice "Risa_0121"
r "「ああ、その話ね……」"
"七海さんの言うとおり、上級生の間でも話題になっているのね。"
voice "Risa_0122"
r "「下級生の間ではずいぶんと、盛り上がっているみたいですね」"
"私の返答に、クラスメイトたちは顔を見合わせる。"
"ちょっと残念な反応をされてしまったわ……違うのかしら？"
voice "mobJyosiC0002"
mobC "「ベストカップルに選ばれた璃紗さんなら、もっと詳しい話をご存知かと思いましたが……」"
voice "mobJyosiB0007"
mobB "「どうやらまだ、そこまで話は進んでいないようですね」"


show char tri03s2
with dis



voice "Risa_0123"
r "「えっ？？」"
"どういうことなのかわからず、ますますきょとんとなってしまう。"
voice "mobJyosiA0008"
mobA "「そんな言い方をされては、璃紗さんも困惑してしまいますわ。ちゃんと説明しないと……」"
voice "mobJyosiC0003"
mobC "「あっ……璃紗さん失礼しました」"
voice "Risa_0124"
r "「いえ、お気になさらず。それよりベストカップルが、どうしたのかしら？」"
voice "mobJyosiB0008"
mobB "「ええ、１年生たちの強い要望で正式に『新１年ベストカップル』投票開催が決まったんですのよ」"


show char tri04s2
with dis



voice "Risa_0125"
r "「えええっ！？」"
"これにはビックリした。"
"あれっててっきり、遊びのようなものだと思っていたのに……"
"確かに今も麗奈先生がいたら、すぐ実行されそうな内容だけど、まさか本当に開催されるなんて。"
voice "mobJyosiA0009"
mobA "「昨年のベストカップル投票が盛り上がりましたから、学校側からもあっさり承諾が得られたそうですわ」"


show char tri03s2
with dis



voice "Risa_0126"
r "「な、なるほど……ね」"
voice "mobJyosiB0009"
mobB "「そうなると、新しく選ばれたペアは、璃紗さんたちと同じくイベント委員会の新メンバーになるのかしら？」"
voice "Risa_0127"
r "「それは……私はまだ、よく知らないわ」"
"そうだったのね……みんなこのことが気になって、私のところに集まって来たのね。"
"でも私だって、カップル投票が決まったのを今、知ったくらいだから。"
"わかるはずないわ。"
voice "mobJyosiC0004"
mobC "「でも、今のメンバーに白雪姫と騎士が加わったら……ああ、なんて素敵なんでしょう」"
voice "mobJyosiA0010"
mobA "「ええ、とても絵になる、お２人ですわ」"
voice "Risa_0128"
r "「………………」"
"まだ投票は始まっていないのに……"
"彼女たちもどうやら、七海さんから聞いたあの２人が選ばれると確信してるようだった。"


show char tri01s2
with dis



voice "Risa_0129"
r "「……あっ、美夜」"


show char tmi01s2
with dis



voice "Miya_0037"
m "「………………」"
"教室に入ってきた美夜と、フッと目が合う。"
"クラスメイトたちに囲まれてる私を、美夜はじっと見つめていた。"
"私はその場から抜け出て、美夜の席へと向かった。"


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0130"
r "「美夜、おはよう。遅刻ギリギリだけど、今朝はちゃんと来たのね」"


show char tmi03s2 at left
with dis



voice "Miya_0038"
m "「ええ……でも何だか、教室内が騒がしいわ。こんなことなら、もっとゆっくり来れば良かったわ」"
voice "Risa_0131"
r "「もう、そんなこと言わないの。ほら、前に話した１年生のベストカップル投票、あれ正式に開催されるんですって」"


show char tmi01s2 at left
with dis



voice "Miya_0039"
m "「ふーん、なるほど……それで皆さん、ざわついてるのね」"
voice "Risa_0132"
r "「そ、そうね……」"
"相変わらず美夜は、この手の話題には興味がないみたい。"
"逆にこの教室の雰囲気のせいで、不機嫌になっているようだった。"
voice "Miya_0040"
m "「こんな浮き足だっている場所にいるのは、我慢出来ないわ……今日は１日、アトリエにこもることにするわ」"


show char tri03s2 at right as r
with dis



voice "Risa_0133"
r "「だ、だめよっ」"
"せっかく教室に来たのに、どうしてすぐ出ていこうとするのよ、美夜は。"
voice "Risa_0134"
r "「ね、お願いだから、ちゃんと授業受けましょうよ」"
voice "Miya_0041"
m "「……必要ないわ」"


show char tri08s2 at right as r
with dis



voice "Risa_0135"
r "「いいえ、必要だわ。集団生活の勉強よ」"
voice "Miya_0042"
m "「……璃紗がここでキスしてくれるのなら、考えてもいいわ」"


show char tri04s2 at right as r
with dis



voice "Risa_0136"
r "「ひゃああああ！　変なこと言わないのっ！」"
"ひそひそ声ではなく、普通にそう言われたものだから、私は周りに聞かれていないかドキドキしてしまった。"
voice "Miya_0043"
m "「じゃあ、わたくしの手の甲にキスをして……それならいいでしょう」"


show char tri03s2 at right as r
with dis



voice "Risa_0137"
r "「そ、それは……」"
"私は再び、周りを見る。"
"どうやらみんな、さっきの話に夢中で、こっちを見ている人は誰もいない。"
"ある意味、チャンスよね……手の甲に軽く、ちゅっとキスして。"
"それだけでいいのよね、それくらいなら。"
"私は美夜が差し出した手に、そっと顔を寄せていく。"
"そして……"
voice "Risa_0138"
r "「うっ……ううううっ」"
"ダメ、心臓が暴れるように高鳴っちゃう。"
"アトリエで普通にキスするより、こっちの方が恥ずかしい。"
"緊張で、体が震えてしまう。"
"美夜はそんな私の様子を、ただ見つめている。"
voice "Miya_0044"
m "「璃紗……ね、早く」"
voice "Risa_0139"
r "「わ、わかってるわよ……」"
"こんなの、一瞬なんだから。"
"さっさと済まして……"

#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


show char tri04s2 at right as r
with dis



voice "Risa_0140"
r "「っ！！」"
"チャイムの音に、体がびくっと反応して、固まってしまって。"
"私は美夜の手から、離れてしまった。"
voice "Miya_0045"
m "「ふっ……タイムリミットね、璃紗」"


show char tri03s2 at right as r
with dis



voice "Risa_0141"
r "「はうっ……」"
"あれだけ恥ずかしい思いをしたくせに、結局私からはキスは出来なかった。"
voice "Miya_0046"
m "「仕方ないわね……でも璃紗の努力に免じて、午前中だけは我慢して授業を受けてあげるわ」"
voice "Risa_0142"
r "「ほ……本当に？」"


show char tmi02s2 at left
with dis



voice "Miya_0047"
m "「ええ、今の恥ずかしそうな璃紗の顔、ちゃんと写メに残せたし」"


show char tri04s2 at right as r
with dis



voice "Risa_0143"
r "「えっ？　ええええっ」"
"よく見ると、私が握っていた手と反対の手にはしっかり、携帯が握られていた。"
voice "Miya_0048"
m "「教室であんなにエロ恥ずかしい顔をする璃紗なんて、滅多にみれないから、いいコレクションになったわ」"


show char tri03s2 at right as r
with dis



voice "Risa_0144"
r "「そそ、そんな……写メの撮影音、しなかったわよ」"
voice "Miya_0049"
m "「わたくしのは、特別製なのよ……ふふっ」"
"酷いわ、そんなの悪事よ、犯罪よ～"
voice "Risa_0145"
r "「と、とにかく美夜、その写真見せて」"
voice "Miya_0050"
m "「そうねぇ……あら、もう先生が来たわよ。席に戻らなくていいのかしら、委員長さん？」"
voice "Risa_0146"
r "「くっ、くぅぅぅ……」"
"美夜ったら、もう……最初からそれが目的だったのね。"


#**青空
scene bg bg42a
with dis



"その後、美夜は有言実行してくれて、午前の授業はちゃんと出てくれたけれど。"
"私のあの写真が、美夜の手にずっと残るのかと思うと……ちょっと割に合わないんじゃないかと思えてしまった。"

scene black
with dis



"それから、数日後。"
"１年生のベストカップル投票は、本当に行われた。"
"噂通りに、選ばれたのは白河沙雪さんと篠崎六夏さんだった。"
"そして……ベストカップルメンバーでの緊急の話し合いが早速、放課後に行われることとなったのだった。"


#**委員会室・昼
scene bg bg30a
show char alpha
with dis



show char tyu01s2
with dis


voice "Yuuna_0000"
y "「１年生のベストカップルに、沙雪さんと六夏さんが選ばれたことは、皆さんご存じですね」"
"司会進行は昨年に引き続き、優菜さま。"
"リーダーとして今日もしっかり、皆さんをまとめあげていた。"
voice "Yuuna_0001"
y "「今日はその新ペアを、正式なベストカップルのメンバーとして、迎え入れてはどうかしら……ということを話し合いたいと思います」"


show char tyu01s2 at left
show char tka01s2 at right as r
with dis


voice "Kaede_0000"
k "「では、皆さんの意見をお聞かせください」"
"サブリーダーであり、進行役でもある楓さまが、みんなに聞いてきた。"

hide char tyu01s2 at left
hide char tka01s2 at right as r
show char tsa01s2
with dis



voice "Sara_0008"
sr "「はぁ～い、はいはいっ」"
"すると早速、紗良さんが元気に高く手を挙げた。"
"今日は仕事がオフってことで、楓さまと揃って参加していたのだった。"


show char tka01s2 at left
show char tsa01s2 at right as r
with dis



voice "Kaede_0001"
k "「はい、紗良」"


show char tsa02s2 at right as r
with dis



voice "Sara_0009"
sr "「紗良は賛成でーす。雫さまとエリスさまが卒業されて、メンバーも減ったことですし、今年もクリスマスのようなイベントをする場合、人手は必要だと思います」"


hide char tka01s2 at left
hide char tsa02s2 at right as r
show char tyu01s2
with dis



voice "Yuuna_0002"
y "「そうね、紗良ちゃんの言う通りね。今のところは、大きなイベントはないけれど、もし何かあった場合、ちょっと人手不足になりそうだし」"


show char tyu01s2 at left
show char tna01s2 at right as r
with dis



voice "Nanami0053"
n "「おねえ……じゃなくて、優菜さまの環境整備委員を始めとして、みんな他にも掛け持ちしてる仕事があって、今のメンバーだけでやるのは大変だと思います」"


show char tyu02s2 at left
with dis



voice "Yuuna_0003"
y "「そうね。七海も次期『環境整備委員会』委員長になるし{image=image/exch001.png}」"


show char tna05s2 at right as r
with dis



voice "Nanami0054"
n "「わ、わたしのことは……いいんです」"
"七海さんがポッと、顔を赤くする。"


show char tna05s2 at right as r
show char tma02s2 at left
with dis



voice "Mai_0000"
ma "「でもなんか、新しい仲間が増えるっていうのは楽しみよね～」"


hide char tma02s2 at left
hide char tna05s2 at right as r
with dis


"麻衣さまの意見に、みんなうんうん頷く。"
"まだベストカップルに選ばれた２人を見てはいないけれど、その話題性だけで十分、楽しみになってきた。"

show char alpha
with dis
show char tka02s2
with dis



voice "Kaede_0002"
k "「なかなか他の学年の方と知り合える機会もないから、紗良たちに後輩が出来るのも、良いことだと思います」"


show char tka02s2 at left
show char tsa02s2 at right as r
with dis



voice "Sara_0010"
sr "「楓ちゃん{image=image/exch001.png}　わぁ、こんな時にまで紗良のことを考えてくれてるんだね～、愛を感じるよぉ～」"


show char tka08s2 at left
with dis



voice "Kaede_0003"
k "「ちょっと、じゃれついてこないの。“紗良たち”って、言ってたでしょう」"
voice "Sara_0011"
sr "「もぉ、照れない照れない～」"


hide char tsa02s2 at right as r
hide char tka08s2 at leftf
show char tri02s2
with dis



voice "Risa_0147"
r "「……ふふふっ」"
"相変わらず、紗良さんと楓さまって仲良いなぁ。"
"こっちまで、ほほえましくなってくる。"

show char alpha
with dis
show char tyu01s2
with dis



voice "Yuuna_0004"
y "「では皆さん、概ね賛成みたいですわね……玲緒さんはどうなのかしら？」"


show char tyu01s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0000"
r "「………………」"
"まだ何も意見をだしてない玲緒さまに、優菜さまが尋ねた。"
"すると玲緒さまは、ぷうっと頬を膨らませていた。"

hide char tyu01s2 at left
hide char tre08s2 at right as r
show char tyu01s2 at sleft as l
show char tre08s2
show char tma03s2 at sright as sr
with dis



voice "Mai_0001"
ma "「ちょっと、玲緒。あなたはどうかって聞かれてるわよ？」"


show char tre09s2
with dis



voice "Reo_0001"
re "「ぶうっ……麻衣のばかぁ」"


show char tma04s2 at sright as sr
with dis



voice "Mai_0002"
ma "「どっ、どうしてここで、わたしがバカになるのよ？」"


show char tre07s2 
with dis



voice "Reo_0002"
re "「何が『新しい仲間が増えて嬉しい』よ。そんなのワタシ、ちっとも嬉しくないわ」"
voice "Yuuna_0005"
y "「玲緒さんは……反対ってことなのかしら？」"
voice "Reo_0003"
re "「ええ、反対よ。これ以上のメンバー、ここにはいらないわ」"


show char tma02s2 at sright as sr
with dis



voice "Mai_0003"
m "「ああっ、ひょっとしてまた、玲緒の人見知りが発動しちゃったの？　もう、玲緒ったら……わがまま言わないの」"


show char tre09s2
with dis



voice "Reo_0004"
re "「わがままじゃないわ！　エリスと雫だって……たまに手伝いに来てくれるって、言ってるし……だから、今のままでいいじゃない」"


show char tyu03s2 at sleft as l
with dis



voice "Yuuna_0006"
y "「玲緒さん……」"
"優菜さま、困った顔をしているわ。"
"このまま、うまくまとまると思ったのに……"


hide char tyu03s2 at sleft as l
hide char tma02s2 at sright as sr
show char tna03s2
with dis



voice "Nanami0055"
n "「あ、あの……」"
"七海さんが、何か言おうとする……が、その前に玲緒さまが大声を上げた。"


show char tna03s2 at left
show char tre07s2 at right as r
with dis



voice "Reo_0005"
re "「何かしら、織田七海？　ワタシはこう見えても、先輩なんですからね……敬意を払いなさい」"
voice "Nanami0056"
n "「ううううっ、そんなぁ……」"


#ゴツンッ！！
#♀SE002
play sound "sound/SE002.ogg"

hide char tna03s2 at left
hide char tre07s2 at right as r
show char tre09s2
with dis



voice "Reo_0006"
re "「痛たたたっ、麻衣、なんでいきなり殴るのよっ」"


show char tre09s2 at left
show char tma09s2 at right as r
with dis



voice "Mai_0004"
ma "「玲緒のおばかっ、そんなとこで先輩風吹かせてどうするの！　もう……七海ちゃん、ごめんね」"


hide char tre09s2 at left
hide char tma09s2 at right as r
show char tna03s2 at sleft as l
show char tre09s2
show char tma09s2 at sright as sr
with dis



voice "Nanami0057"
n "「いえ、その……平気ですから」"
"でも明らかに、しょぼんとしてしまう七海さん。"
"その七海さんを見て、優菜さまの瞳がキラリと光った。"


hide char tna03s2 at sleft as l
hide char tma09s2 at sright as sr
show char tyu02s2
with dis



voice "Yuuna_0007"
y "「……ああ、嬉しいわ。七海が私の為に、先輩に口答えするなんて……うふふふ{image=image/exch001.png}」"
"んっ？　何か優菜さま、笑っているみたいだけど。"
"こんな話し合いの最中に、そんなわけないわよね。"
"でもここに来ての、反対意見。"
"優菜さま、どうするつもりなのかしら？"
"成り行きをハラハラと見守っていると……"


show char tka01s2
with dis



voice "Kaede_0004"
k "「……玲緒さん」"
"そこに凛とした声が響いた。"


show char tka01s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0007"
re "「北島楓……な、何よ、アンタも文句あるの？」"


hide char tka01s2 at left
hide char tre08s2 at right as r
show char tka01s2 at sleft as l
show char tre08s2
show char tma08s2 at sright as sr
with dis



voice "Mai_0005"
ma "「もう、玲緒ったら……あなたはどうして、そういう口のきき方なの？」"
voice "Kaede_0005"
k "「いえ、いいんです、麻衣さん。ちょっと聞いてくれますか、玲緒さん」"
voice "Reo_0008"
re "「……いいわよ」"


hide char tma08s2 at sright as sr
hide char tka01s2 at sleft as l
show char tna03s2
with dis



voice "Nanami0058"
n "「楓……さま……」"


show char tsa03s2
with dis



voice "Sara_0012"
sr "「楓ちゃん……ハラハラ」"
"緊迫した空気の中、ジッと楓さまを見守る、七海さんと紗良さん。"
"明らかに不機嫌そうな玲緒さまに、楓さまは静かに話し始めた。"


show char tka01s2 at left
show char tre08s2 at right as r
with dis



voice "Kaede_0006"
k "「今のメンバーは優秀な方も多いですし、璃紗さんのように頑張り屋な人もいます。ですからこのままでも、ここの仕事は何とかこなせるとは思います」"


hide char tka01s2 at left
hide char tre08s2 at right as r
show char tri04s2
with dis



voice "Risa_0148"
r "「か……楓さま……」"
"いきなり自分の名前が出てきたから、ビックリしてしまう。"


show char tri02s2
with dis



"でも楓さま、私のことをそんな風に思ってくれていたんだ……嬉しい、かなり嬉しい。"


show char tmi03s2 at left
show char tri02s2 at right as r
with dis



voice "Miya_0051"
m "「……わかりやすいくらい、ニヤついてるわよ、璃紗？」"


show char tri03s2 at right as r
with dis



voice "Risa_0149"
r "「わ、悪かったわね……」"


show char tka01s2 at left
show char tre08s2 at right as r
with dis



voice "Kaede_0007"
k "「ですが、みんな優秀だからって、エリスさまや雫さまは毎回来られるわけではありませんよね」"


show char tre03s2 at right as r
with dis



voice "Reo_0009"
re "「そ……それは……」"


show char tka03s2 at left
with dis



voice "Kaede_0008"
k "「それに私と紗良も、仕事で出られないこともあったりで……その分、皆さんの負担を大きくしていると思うと、申し訳なくて」"


hide char tka03s2 at left
hide char tre03s2 at right as r
show char tka03s2 at sleft as l
show char tre03s2
show char tma01s2 at sright as sr
with dis



voice "Mai_0006"
ma "「楓さん……」"
"仕事で集まりに来られないこと、楓さまは私たちが思うよりずっと気にしてらしたのね。"
"その言葉から、私はあらためて、楓さまの想いを知った。"


show char tka01s2 at sleft as l
with dis



voice "Kaede_0009"
k "「だから……私は新しいペアを迎えいれたいと思います」"
"楓さまのその言葉に、室内が静まった。"
voice "Mai_0007"
ma "「玲緒、どうなの？　楓さんの話を聞いても、まだイヤだっていうの？」"
voice "Reo_0010"
re "「べ、別に……もう、そんなに入れたいのなら、入れたらいいじゃない」"
"ぷいっと、ぶっきらぼうに言葉を紡ぐ玲緒さま。"


show char tma02s2 at sright as sr
with dis



voice "Mai_0008"
ma "「ふふふっ、玲緒も入れてもいいそうですよ♪」"
"その言葉に、その場の雰囲気が和らぐ。"


hide char tka01s2 at sleft as l
hide char tma02s2 at sright as sr
show char tsa02s2
with dis



voice "Sara_0013"
sr "「楓ちゃん、かっこいい～、やっぱり楓ちゃんは王子様だね{image=image/exch001.png}」"


show char tka03s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0010"
k "「さ、紗良……」"
"普段はどちらかといえば、裏方に回っていることの多い楓さまだけど、こう言う時はすごく頼りがいがあるのね。"
"紗良さんが、王子様だって言うのもわかる気がする。"

hide char tka03s2 at left
hide char tsa02s2 at right as r
show char tyu01s2
with dis



voice "Yuuna_0008"
y "「それじゃあ、これで決まりかしら……あらっ、璃紗ちゃんと美夜ちゃんはどうなの？」"


show char tri04s2
with dis



voice "Risa_0150"
r "「あっ……」"
"そういえば私も美夜もまだ、全然意見を言ってなかったわ。"


show char tre02s2
with dis



voice "Reo_0011"
re "「そうよ、綾瀬美夜。アンタはどうなの？　人付き合いのヘタなアンタが、新しいメンバーと仲良く出来るの？」"


show char tre02s2 at left
show char tma03s2 at right as r
with dis



voice "Mai_0009"
ma "「……美夜ちゃんも、玲緒にだけは言われたくないわよね」"
"玲緒さまはまるで、同志でも見つけたように、嬉しそうに言った。"

hide char tre02s2 at left
hide char tma03s2 at right as r
show char tmi01s2
with dis



voice "Miya_0052"
m "「………………」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0151"
r "「美夜……」"
"確かに美夜は基本、他人にはあまり興味ないし、関わりたがらない。"
"新しく来た子たちと、うまくやってくれるとは思えないわ……"
voice "Miya_0053"
m "「わたくしは……」"
"そこにいた全員の視線が、美夜に集まる。"
voice "Miya_0054"
m "「わたくしは……璃紗と同じ意見です」"


show char tri04s2 at right as r
with dis



voice "Risa_0152"
r "「ちょ、ちょっと、美夜っ！」"
"何よ、その答えは。"

hide char tmi01s2 at left
hide char tri04s2 at right as r
show char tna02s2
with dis



voice "Nanami0059"
n "「ふふふっ、美夜さんって、璃紗さんと本当に仲良しなんだね」"
"七海さん、それは何か違うわ。"


show char tyu01s2
with dis



voice "Yuuna_0009"
y "「そうね……では、璃紗ちゃんの意見は？」"


show char tyu01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0153"
r "「私は……皆さんと同じく、賛成です……」"


show char tyu02s2 at left
with dis



voice "Yuuna_0010"
y "「はい、じゃあこれで決まりね」"
"こうして、１年生新カップルをメンバーとして迎え入れることが決まったのだった。"

hide char tyu02s2 at left
hide char tri01s2 at right as r
show char tri03s2
with dis



voice "Risa_0154"
r "「ちょっと、美夜。さっきの面倒くさくて、私に投げたんでしょう？」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Miya_0055"
m "「ええ……新しいメンバーなんてどうでもいいけれど、あそこまで決まっているところで、わざわざ反論するのも変でしょう？」"
voice "Risa_0155"
r "「もう……」"
"どんな時でも美夜は、マイペースなんだから……"


#**暗転
#mes off
#mes clear
#system off
scene black
with Dis



#**新校舎廊下・昼
scene bg bg05a
show char alpha
with Dis



#mes on
#system on


show char tre07s2
with dis



voice "Reo_0012"
re "「……ぶぅ……ぶぅ……」"


show char tre07s2 at left
show char tma02s2 at right as r
with dis



voice "Mai_0010"
ma "「あら、可愛いブタさんの真似が上手くなったのね、玲緒」"


show char tre09s2 at left
with dis



voice "Reo_0013"
re "「ちがーうっ！！　ワタシ、怒ってるんだから……麻衣の薄情ものっ！！」"


show char tma08s2 at right as r
with dis



voice "Mai_0011"
ma "「どうしてわたしが薄情ものなのよ？　それを言うなら、玲緒だって……どうしてさっき、委員会の新メンバーに反対したの？」"


show char tre03s2 at left
with dis



voice "Reo_0014"
re "「そ……それは……だから……」"


show char tma03s2 at right as r
with dis



voice "Mai_0012"
ma "「玲緒も委員会に入って、人間的にも成長したって思っていたのに、実はまだまだダメっ子問題児だったって事？」"
voice "Reo_0015"
re "「違う、ワタシは……ただ、新メンバーなんかいなくても……エリスや、霧島シズクが手伝ってくれるから……」"


show char tma01s2 at right as r
with dis



voice "Mai_0013"
ma "「………………あっ、そっか」"
"ダメなのはわたしの方だったみたい。"
"恋人なのに、玲緒の優しい思いやりに、気づいてあげられなかったなんて……反省ね。"


show char tma02s2 at right as r
with dis



voice "Mai_0014"
ma "「玲緒……ああ、やっぱり玲緒って、カワイイっ{image=image/exch001.png}」"


show char tre09s2 at left
with dis



voice "Reo_0016"
re "「ちょ、ちょっと麻衣っ、廊下で抱きつくなぁ、エロスーっ！！」"


show char tma01s2 at right as r
with dis



voice "Mai_0015"
ma "「だって……玲緒、新メンバーが入っちゃったら、エリスさまと雫さまの居場所がなくなるんじゃないかと思って、反対したんでしょ？」"


show char tre03s2 at left
with dis



voice "Reo_0017"
re "「そ、それは……だって、そのぉ……」"
"ああ……本当に、愛しい玲緒。"
"わたしは玲緒を更に強く抱きしめながら、そっと囁いた。"
voice "Mai_0016"
ma "「大丈夫よ、玲緒……あなたもわたしも、そして他のメンバーだって絶対、エリスさまと雫さまの事は忘れたりしないから、ね？」"
voice "Reo_0018"
re "「麻衣……うん、そう……だよね」"
"うつむく玲緒の美しい金髪をくしゃくしゃしながら、わたしはニッコリ微笑んだ。"
voice "Mai_0017"
ma "「だからね、ほら。ラヴラヴカップルの先輩として、新しい１年生カップルを迎えてあげましょう、玲緒？」"
voice "Reo_0019"
re "「……麻衣が、そう言うなら……」"


show char tma02s2 at right as r
with dis



voice "Mai_0018"
ma "「そして自分たちが、まだまだ未熟な青いカップルだって思えるほど、見せつけてあげましょう……わたしと玲緒のあつーい愛の抱擁を{image=image/exch001.png}」"


show char tre09s2 at left
with dis



voice "Reo_0020"
re "「だ、だから麻衣、こんなところで……ひゃぅぅん！　おっぱい触るなぁ、麻衣のエロスーっ！！」"


#**暗転
#mes off
#mes clear
#system off
scene black
with dis



#**委員会室・昼
scene bg bg30a
show char alpha
with dis



#mes on
#system on


"そしてついに、ベストカップルの顔合わせが行われた。"
"初めてということで、今回はなんと、雫さまとエリスさまも来てくれた。"


show char tsi01f2
with dis



voice "Sizuku0000"
sk "「１年生のかっぷる、どんな方たちなのかしら……楽しみですね、エリス」"


show char ter02f2 at left
show char tsi01f2 at right as r
with dis



voice "Erisu_0000"
e "「そうだね～♪　ふふふっ、ところで聞いたよ～、玲緒、最初反対してたんだって？」"


show char tre03s2 at right as r
with dis



voice "Reo_0021"
re "「うにゅ～、誰がそんなこと言ったのよ」"


show char ter01f2 at left
with dis



voice "Erisu_0001"
e "「玲緒の気持ち……ワタシ、よーくわかるわ」"


show char tre04s2 at right as r
with dis



voice "Reo_0022"
re "「えっ……ほ、本当に？」"


show char ter02f2 at left
with dis



voice "Erisu_0002"
e "「もちろんよ。玲緒は後輩に、ワタシがとられると思ったのね」"


show char tre03s2 at right as r
with dis



voice "Reo_0023"
re "「はぁぁぁ？」"
voice "Erisu_0003"
e "「大丈夫だよ。玲緒はいつまでも、ワタシの可愛い友達だから～」"


show char tre09s2 at right as r
with dis



voice "Reo_0024"
re "「にやぁぁ～、エリス苦しい、その無駄に大きいおっぱい押しつけるなぁ～」"

hide char ter02f2 at left
hide char tre09s2 at right as r
show char ter02f2 at sleft as l
show char tre03s2
show char tma02s2 at sright as sr
with dis



voice "Mai_0019"
ma "「玲緒、これからもエリスさまに遊んでもらえそうで、良かったわね♪」"
voice "Reo_0025"
re "「良くない～、麻衣助けなさいよ」"


hide char ter02f2 at sleft as l
hide char tma02s2 at sright as sr
show char tyu02s2
with dis



voice "Yuuna_0011"
y "「ふふふっ、仲良しなのはいいけど、私たちが騒いでいると、彼女たちが入りずらそうよ」"
"教室のドアの外にはもう、２人ともスタンバっていた。"
"どうやら、入ってくるタイミングを計りかねているみたい。"


show char ter03f2
with dis



voice "Erisu_0004"
e "「あっ、ゴメンね……じゃあこの続きは、また後でね、玲緒{image=image/exch001.png}」"


show char ter03f2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0026"
re "「続きなんて、永久にないからねっ」"

hide char ter03f2 at left
hide char tre08s2 at right as r
with dis


"エリスさまが、玲緒さまから離れていくと、優菜さまがドアに向かって呼びかけた。"


show char tyu01s2
with dis



voice "Yuuna_0012"
y "「それでは……お二人とも、どうぞ」"


hide char tyu01s2
with dis


#♀SE003
play sound "sound/SE003.ogg"


"２人が教室に入ってきた……いよいよだわ。"
"どういう子たちなんだろう。"


show char tmi01s2
with dis



voice "Miya_0056"
m "「………………」"
"美夜はただぼんやりと、外の景色を眺めていた。"
"まったく……どれだけ興味がないのかしら。"


show char tsy01s2
with dis


voice "Sayuki0000"
x "「失礼……します」"
"まず、先に入ってきたのは。"
"物静かで、上品なたたずまいの子だった。"
"もう自己紹介するまでもなく、彼女が『白河沙雪さん』であることは明白だった。"


show char tri04s2
with dis



voice "Risa_0156"
r "「わ……とっても、綺麗……」"
"小声だけど、思わずそんな声が出てしまった。"


show char tri01s2
with dis



"まさに白雪姫というあだ名、そのものだった。"
"ついつい、見とれてしまう。"
"ベストカップルに選ばれた人たちは、美夜を含めてみんな、綺麗な人が多いけれど。"
"その中でも沙雪さんは、どこか違ったオーラを放っていた。"
"さすが『究極の淑女の再来』と呼ばれるだけのことはあるわ。"
"私以外のメンバーもみんな、驚いたように彼女を見つめていた。"
"彼女に続いて、もう１人……『白雪の騎士』と呼ばれている子が入ってくる。"


show char trk03s2
with dis



voice "Rikka_0000"
x "「し、失礼しますぅ……」"
"あら……緊張でガチガチみたい。"
"手と足が、同時に出ているわ。"


show char tri03s2
with dis



voice "Risa_0157"
r "「この子……大丈夫なのかしら」"
"他人のことながら、心配になってくる。"
"『白雪の騎士』って呼ばれているって、本当なのかしら。"
"どこか頼りないっていうか、放っておけない感じというか……"
"彼女は少し俯きがちに、沙雪さんの隣に並んだ。"
"彼女が、六夏さん……ってことよね？"
"明らかに緊張ＭＡＸの彼女に、優菜さまが優しく微笑みかける。"


show char tyu02s2
with dis



voice "Yuuna_0013"
y "「そんなに硬くならないで、六夏さん。みんな、あなたたちを歓迎しているのよ」"
"その優菜さまの声に、六夏さんが顔を上げる。"


show char tri04s2
with dis



voice "Risa_0158"
r "「あっ……この顔……」"


show char tri03s2
with dis



"どこか、見覚えがあるわ……やっぱり、知っている子なのかしら……"
"そう思った時、六夏さんの目が、私と合った。"
"その瞬間……思いもかけないことが起こった。"


show char tri03s2 at left
show char trk04s2 at right as r
with dis



voice "Rikka_0001"
rk "「りっ、リサ姉っ！！」"
voice "Risa_0159"
r "「へっ？？」"


stop music fadeout 1


#※EV001
scene bg EV01
with Dis


play music "sound/BGM22.ogg"


"六夏さんはいきなり、大きな声で私の名を呼んで。"
"そのまま飛びつくように、ギュッと抱きついてきたのだ。"
voice "Risa_0160"
r "「ちょ、ちょっと、これ、どういうこと！？」"
"驚いている私の周りで、同じくビックリしてるベストカップルの皆さん。"
voice "Sara_0014"
sr "「ちょっと、璃紗ちゃん、これって……」"
voice "Nanami0060"
n "「六夏さんと、知り合いなの？」"
"２年生会の２人も目を丸くしている。"
"そして……さっきまで、新カップルにはまったく興味を寄せてなかった、美夜は……"


#※EV001P1
scene bg EV01p1
with dis



voice "Miya_0057"
m "「りりりっ、璃紗ぁ……その女は一体、誰なのよぉぉっ！！」"
"いつものクールがどこかに飛んで行ってしまったように、動揺していた。"
voice "Risa_0161"
r "「み、美夜、あのその、この子は……えっと……」"
voice "Miya_0058"
m "「うそ、ウソウソ、ウソよ……この世で璃紗を抱いてもいいのは、わたくしだけなのに……そんな璃紗が別の女に、どこの誰とも分からない、ふしだらな女に……くうううっ、くわぁぁぁっ！！」"
voice "Nanami0061"
n "「美夜さん……こんなに動揺した美夜さん見るの、初めてだよぉ……」"
voice "Risa_0162"
r "「ちょ、ちょっと美夜、違うのっ！　私はこの子の事、知らないわ！　きっと誰かと勘違いしているだけ……」"
voice "Rikka_0002"
rk "「そんな、忘れたなんて言わないで、リサ姉っ！　あんなに仲良かったじゃない！？」"
voice "Miya_0059"
m "「あ、あんなに仲が良かった、って……わたくしに抱かれる前に、璃紗はこの子と、あんな事やこんな事を、もうやっていたのね……もうもう、もうっ！！」"
voice "Risa_0163"
r "「美夜、だから誤解だって言っているのに……ぅぅっ、なんか……」"
"なんだかものすごい、嵐の予感がする……とんでもなく、ヤバい予感が。"


#**暗転
#mes off
#mes clear
#system off
scene black
with Dis


#♂MS
stop music fadeout 1

jump S005


