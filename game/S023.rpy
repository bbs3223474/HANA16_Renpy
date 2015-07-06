#「麻衣、ついに暴走」

label S023:
$ save_name = "◇麻衣、ついに暴走"


#※ここは麻衣視点です
#※このシーン、全員水着姿で


#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


#♂MP13
play music "sound/BGM13.ogg"


"夏休みの玲緒といえば。"
"わたしが見張ってないと、一日中クーラーの利いた部屋から出てこないで、だらだらだらだら。"
"宿題もせずに、ひたすらだらだらしてるだけなんだから。"
"今回のバカンスの誘いは、本当に助かったかも。"
"こうして――"


show char tma02m
with dis



voice "Mai_0155"
ma "「バカンスのおかげで、玲緒はひきこもりにならずにすんだのでした、おしまい♪」"


show char tma02m at left
show char tre03m at right as r
with dis



voice "Reo_0125"
re "「麻衣、何言ってるのよ？」"
voice "Mai_0156"
ma "「ひと夏の玲緒物語よ」"
voice "Reo_0126"
re "「はぁ？」"


show char tma01m at left
with dis



voice "Mai_0157"
ma "「ひきこもりの玲緒が、少しずつ外に世界に飛び出していく……」"
voice "Reo_0127"
re "「成長物語とかいうんでしょう？」"
voice "Mai_0158"
ma "「残念！　それはないわ、玲緒のお胸が成長するわけないじゃない」"


show char tre07m at right as r
with dis



voice "Reo_0128"
re "「まーい、今、胸の話なんてしてないわっ」"
voice "Mai_0159"
ma "「そうだっけ」"


show char tre08m at right as r
with dis



voice "Reo_0129"
re "「もう、適当なんだから」"
"バンッと、テーブルの上に乱暴に玲緒がお盆を置く。"

#♀SE065
play sound "sound/SE065.ogg"


"そこにはスイーツやフルーツなど、玲緒の好きなものがたくさん乗っている。"


show char tma03m at left
with dis



voice "Mai_0160"
ma "「こんなにたくさん、どうしたの？」"
voice "Reo_0130"
re "「ホテルの人に頼んだのよ」"
voice "Mai_0161"
ma "「そうじゃなくて……」"
"玲緒はソファーに座ると、早速ジュースを飲んだりお菓子を食べ始めた。"


show char tre02m at right as r
with dis



voice "Reo_0131"
re "「あー美味しい♪　ここのホテルのスイーツって、どれも美味しいわよね。帰ったらお取り寄せしてもらおうかしら……もぐもぐ」"
voice "Mai_0162"
ma "「なんかこれって、玲緒のマンションでよく見る光景なんだけど……玲緒、今日はビーチに行かないの？」"
"毎日、陽が落ちるまで、遊びまくっているのに。"
"今日はなんだか、のんびりしてるわね。"


show char tre03m at right as r
with dis



voice "Reo_0132"
re "「んー、なんか疲れちゃったのよね……」"


show char tma01m at left
with dis



voice "Mai_0163"
ma "「あれだけ全力全開で遊んでいれば、疲れもするわね」"


show char tre02m at right as r
with dis



voice "Reo_0133"
re "「だから、今日は部屋でまったり過ごす日に決めたの♪」"
voice "Mai_0164"
ma "「……そう」"
"毎日、はしゃぎすぎではあったからね。"
"普通は、自分の体力も考えてセーブするところだけど。"
voice "Mai_0165"
ma "「……玲緒はその辺何も考えていなさそうだものね。こうなるのも仕方ない事ね」"
voice "Mai_0166"
ma "「それが玲緒イズムってヤツね」"


show char tre08m at right as r
with dis



voice "Reo_0134"
re "「麻衣、考えてること全部、口に出さないでよ」"
voice "Mai_0167"
ma "「えっ？　わたしとしたことが、体力のない玲緒をこのまま押し倒して、わたしの言いなりにさせてあげようとか」"


show char tre04m at right as r
with dis



voice "Reo_0135"
re "「ほわっ！？」"
voice "Mai_0168"
ma "「もう疲れたからやだーとか、泣きそうな顔の玲緒をさらに気持ち良くさせちゃったりとか……そんなことまで口にしてた？」"


show char tre09m at right as r
with dis



voice "Reo_0136"
re "「ま、麻衣のエロス～、何言ってるのよ！！」"
"ふぎーと、毛を逆立たせる猫のようにこっちを警戒してくる玲緒。"


show char tma02m at left
with dis



voice "Mai_0169"
ma "「ふふふっ、冗談よ、そんなことするわけないじゃない♪」"


show char tre08m at right as r
with dis



voice "Reo_0137"
re "「もう、麻衣はワタシの隣りでおとなしくしてなさい」"


show char tma01m at left
with dis



voice "Mai_0170"
ma "「わかったわよ、玲緒」"
"今日は玲緒に一日、つきあいますか。"
"たまには、部屋でのんびりするのも、悪くないわね。"
"バカンスの過ごし方なんて、人それぞれなんだから……"


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


#――コンコンッ
#♀SE013
play sound "sound/SE013.ogg"


#//SE：ドアノック音

"玲緒と一緒にお茶やお菓子を食べながら過ごしていると、ドアがノックされた。"


show char tma03m
with dis



voice "Mai_0171"
ma "「……誰かしら？」"


show char tma03m at left
show char tre01m at right as r
with dis



voice "Reo_0138"
re "「ホテルの人が気を利かせて、お菓子の追加分を持ってきてくれたのよ」"
voice "Mai_0172"
ma "「それはないと思うわよ」"


show char tre03m at right as r
with dis



voice "Reo_0139"
re "「ええー」"


#allClear:
hide char tma03m at left
hide char tre03m at right as r
#lastBG:
#scene bg bg37a
with dis


"玲緒のことは放っておいて扉を開けると、そこには……"


show char ter02m at left
show char tsi01m at right as r
with dis



voice "Erisu_0067"
e "「玲緒、こんにちはー♪」"
voice "Sizuku0054"
sk "「ごきげんよう」"

hide char ter02m at left
hide char tsi01m at right as r
show char tma01m at sleft as l
show char ter02m
show char tsi01m at sright as sr
with dis



voice "Mai_0173"
ma "「エリスさま、雫さま」"
"先輩たち２人の姿があった。"


#allClear:
hide char tma01m at sleft as l
hide char ter02m
hide char tsi01m at sright as sr
#lastBG:
#scene bg bg37a
show char tre04m
with dis



voice "Reo_0140"
re "「えっ？　エリス？」"


show char tre04m at left
show char ter02m at right as r
with dis



voice "Erisu_0068"
e "「ハァ～イ！　玲緒、遊びに来たよ」"


show char tre01m at left
with dis



voice "Reo_0141"
re "「ず、ずうずうしいわね、ワタシのお菓子たかりにきたんでしょう」"
"エリスさまに文句を言いつつも、玲緒の口調は嬉しそうで、顔がすでに笑ってる。"
voice "Erisu_0069"
e "「そうよ、玲緒のお菓子全部食べちゃおうかな～」"


show char tre08m at left
with dis



voice "Reo_0142"
re "「だめだからねっ」"
"２人がじゃれてる横では、雫さまがいきなり来てすいませんと謝る。"


show char tma02m at left
show char tsi03m at right as r
with dis



voice "Mai_0174"
ma "「いいんですよ、２人でだらだらしてるだけだったから」"


show char tsi01m at right as r
with dis



voice "Sizuku0055"
sk "「ありがとうございます、麻衣さんたちがビーチに出てこないので、エリスが寂しかったみたいで、部屋に行こうって言いだしたんです」"
voice "Mai_0175"
ma "「そうなんですね……わたしたちならいつでも大歓迎だから、遠慮なく遊びに来てください」"
"これは本音。"
"バカンスだからこそ、なかなか会えないこの２人とも、一緒にいる時間があるんだもの。"
"特に玲緒はエリスさまと仲良しだから、今のうちにたくさん話をさせてあげたいのよね。"


show char tma01m at left
with dis



voice "Mai_0176"
ma "「雫さま、短大の話、じっくり聞かせてもらえませんか。来年の参考にしたいので」"
voice "Sizuku0056"
sk "「もちろんです。麻衣さんたちも来年は、卒業ですからね」"
voice "Mai_0177"
ma "「一応は、受験生なんですよね……ミカ女にいるとそんな感じしないけど」"
voice "Sizuku0057"
sk "「わたくしも、同じことを一年前に思いましたわ。おかげで進路がぎりぎりまで決まらなくて……」"
voice "Mai_0178"
ma "「そうでしたね……」"
"２人でおしゃべりをしていると、いつの間にか玲緒が部屋から出ていった。"


show char tma03m at left
with dis



voice "Mai_0179"
ma "「ん……トイレかしら？」"
"気にせず話を続けていると、しばらくして戻ってきた。"
"その手には、美味しそうなトロピカルジュースを２つ、持っていた。"


#allClear:
hide char tma03m at left
hide char tsi01m at right as r
#lastBG:
#scene bg bg37a
show char tre02m
with dis



voice "Reo_0143"
re "「このジュース、すっごく美味しいの！」"
"そう言って玲緒は、エリスさまと雫さまに差し出した。"


show char tre02m at sleft as l
show char ter02m
show char tsi02m at sright as sr
with dis



voice "Sizuku0058"
sk "「ありがとうございます、玲緒さん」"
voice "Erisu_0070"
e "「ふふふ、ありがとう♪　玲緒にしては気がきいてるわね」"


#allClear:
hide char tre02m at sleft as l
hide char ter02m
hide char tsi02m at sright as sr
#lastBG:
#scene bg bg37a
show char tma10m
with dis



voice "Mai_0180"
ma "「本当に……胸は成長しなくても、人間的中身はちんまり成長してるのね」"


show char tma10m at left
show char tre09m at right as r
with dis



voice "Reo_0144"
re "「うう、うるさい、麻衣……もう」"


#allClear:
hide char tma10m at left
hide char tre09m at right as r
#lastBG:
#scene bg bg37a
with dis


"いつも自分のことばかりの玲緒が、２人に気を使ってジュースをもらってくるなんて。"
"珍しいこともあるものね。"
"エリスさまたちのこと、本当に好きなのね……玲緒は。"


show char tsi02m
with dis



voice "Sizuku0059"
sk "「んっ……これ、美味しいです。玲緒さんの言うとおり、とても美味しいですね」"
"雫さまはそれを気に入ったのか、ごくごく飲んでいる。"


show char tre02m at left
show char tsi02m at right as r
with dis



voice "Reo_0145"
re "「当然だわ、ワタシが選んだんだもの」"


show char ter02m at left
show char tre02m at right as r
with dis



voice "Erisu_0071"
e "「ありがとう、玲緒。感謝の気持ちをこめて、ぎゅーってしてあげる」"


show char tre03m at right as r
with dis



voice "Reo_0146"
re "「いっ、いらないわよ……」"
voice "Erisu_0072"
e "「照れなくていいのよ、さあワタシの胸に飛び込んでおいで……ぷっ」"


show char tre08m at right as r
with dis



voice "Reo_0147"
re "「自分で言って、なに吹き出しているのよ」"


show char ter01m at left
with dis



voice "Erisu_0073"
e "「いや、玲緒には飛び込む胸がないなーって」"


show char tre09m at right as r
with dis



voice "Reo_0148"
re "「むきーーーーっ、ばっかじゃないの」"
voice "Erisu_0074"
e "「いや待って、少しはあるのかも、是非これは確かめてみないと」"
voice "Reo_0149"
re "「みなくていいのぉー、ちょっと」"
voice "Erisu_0075"
e "「玲緒だって、ワタシの胸をすぐさわるくせに」"
voice "Reo_0150"
re "「あんたが無駄ちちだからよ」"


show char ter02m at left
with dis



voice "Erisu_0076"
e "「ええええっー、ひどいなぁ♪」"
"相変わらずの２人ね。"


#allClear:
hide char ter02m at left
hide char tre09m at right as r
#lastBG:
#scene bg bg37a
show char tma01m
with dis



voice "Mai_0181"
ma "「玲緒ったらすっかり、エリスさまの妹分ね」"


show char tma01m at left
show char tsi05m at right as r
with dis



voice "Sizuku0060"
sk "「………………」"


show char tma03m at left
with dis



voice "Mai_0182"
ma "「雫さま？」"
"雫さまは赤い顔をして、ぼーっとしたままエリスさまたちを見つめている。"
voice "Mai_0183"
ma "「あの、どうかしました」"


show char tsi02m at right as r
with dis



voice "Sizuku0061"
sk "「いいえ……ごくごく……これ本当に美味しいですよ、麻衣さん」"
voice "Mai_0184"
ma "「そうですか……」"
"なんかいつもと、様子が違うような……"
"普段の雫さまだったら、こんな風にジュースをカブ飲みとか、ありえないんだけど。"
voice "Mai_0185"
ma "「もしかして、どこか具合が悪いんじゃないですか」"
"ますます顔も、赤くなっているし。"
"ひょっとして、夏風邪じゃないかしら？"


show char tsi08m at right as r
with dis



voice "Sizuku0062"
sk "「いいえ、大丈夫ですからっ」"
"雫さまが急に大声を出されて、一瞬ドキっとしてしまった。"
"異変を感じたエリスさまが、慌ててすぐに飛んできた。"

hide char tma03m at left
hide char tsi08m at right as r
show char tma03m at sleft as l
show char tsi08m
show char ter03m at sright as sr
with dis



voice "Erisu_0077"
e "「ねぇシズク、急に大きな声をだして、どうしたの？」"


show char tsi02m
with dis



voice "Sizuku0063"
sk "「なんでもありませんよぉー、ふふふっ{image=image/exch001.png}」"
"何もおかしいことはないのに、今度は笑いだしている。"
voice "Erisu_0078"
e "「どうしちゃったのシズク～、麻衣さん、何か思い当たることある？」"
voice "Mai_0186"
ma "「うーん……といっても、ジュース飲んでいただけだし」"
voice "Erisu_0079"
e "「ジュース？」"
"エリスさまが、雫さまの飲んでいたジュースを確認する。"
voice "Erisu_0080"
e "「これ………………カクテルだわ」"


show char tma04m at sleft as l
with dis



voice "Mai_0187"
ma "「ええぇぇーっ！」"
"玲緒がジュースと間違えて、持ってきてしまったのね。"


#allClear:
hide char tma04m at sleft as l
hide char tsi02m
hide char ter03m at sright as sr
#lastBG:
#scene bg bg37a
show char tre03m
with dis



voice "Reo_0151"
re "「んっ、なに騒いでいるの？」"


show char tma03m at left
show char tre03m at right as r
with dis



voice "Mai_0188"
ma "「雫さまが飲んでいたのジュースじゃなくて、お酒だったって」"


show char tre04m at right as r
with dis



voice "Reo_0152"
re "「……あっ！」"


show char tma08m at left
with dis



voice "Mai_0189"
ma "「あっ、じゃないでしょう、もう、玲緒のおバカ」"


show char tre03m at right as r
with dis



voice "Reo_0153"
re "「だって、似ていたから、それに雫も一口飲んで、どうしてすぐに気が付かないのよ」"


show char tma09m at left
with dis



voice "Mai_0190"
ma "「そうやって、人のせいにしないのっ！」"

hide char tma09m at left
hide char tre03m at right as r
show char tsi03m at sleft as l
show char tma09m
show char tre03m at sright as sr
with dis



voice "Sizuku0064"
sk "「あの……わたくしは、大丈夫ですから」"


show char tma03m
with dis



voice "Mai_0191"
ma "「雫さま、本当に平気ですか」"


show char ter03m at sleft as l
show char tsi03m
show char tma03m at sright as sr
with dis



voice "Erisu_0081"
e "「シズク、気持ち悪くない？　少し横になっていた方が、酔いが醒めるんじゃない？」"
"介抱しようとする、エリスさまの手を雫さまはふりほどいた。"
voice "Sizuku0065"
sk "「……平気ですから……ヒック」"


show char tsi02m
with dis



voice "Sizuku0066"
sk "「わたくしはぁ～、平気なんですよぉ……んふっ」"
"ああ……目が完全にすわっていた。"
"その場にいた全員が、雫さまが全く平気でないことを確信した。"
voice "Mai_0192"
ma "「なんだかやばい雰囲気になってきたわね……」"


show char ter01m at sleft as l
with dis



voice "Erisu_0082"
e "「でも、気持ち悪いとかはないみたいだから、良かったよ」"


show char tma01m at sright as sr
with dis



voice "Mai_0193"
ma "「そうね……」"
"それは良いことだけど……なんか、やっかいなことになりそうな。"


#allClear:
hide char ter01m at sleft as l
hide char tsi02m
hide char tma01m at sright as sr
#lastBG:
#scene bg bg37a
show char tsi08m
with dis



voice "Sizuku0067"
sk "「……麻衣さん」"


show char tsi08m at left
show char tma03m at right as r
with dis



voice "Mai_0194"
ma "「はい？」"
"突然、わたしの名前が呼ばれた。"
"これ、きちゃったかも……"
voice "Sizuku0068"
sk "「さっき短大の話が聞きたいって言いましたね。だから、いっぱいしてさしあげますわ」"
voice "Mai_0195"
ma "「え、ええ……はい」"
"できれば酔ってない時に、お聞きしたかったんだけど……"
"まぁ、しょうがないわね。"


show char tsi02m at left
with dis



voice "Sizuku0069"
sk "「短大でも、わたくしはエリスと一緒で、とっても仲が良いんですよ{image=image/exch001.png}」"
voice "Mai_0196"
ma "「は、はぁ……そうみたいですね」"
voice "Sizuku0070"
sk "「わたくし……エリスが好きなんです{image=image/exch001.png}」"
voice "Mai_0197"
ma "「えっ？」"
voice "Sizuku0071"
sk "「とぉーても好きなんです、大好きなんです{image=image/exch001.png}」"
voice "Mai_0198"
ma "「そ、そうですか……」"
"普段の雫さまなら決してしないような、ノロケ話。"
"これって間違いなく、お酒のせいよね？"
"それでもエリスさまは、すごく嬉しそうだった。"


show char ter02m at left
show char tsi02m at right as r
with dis



voice "Erisu_0083"
e "「シズク～、ああシズクの口からこんな言葉が聞けるなんて、なんてラッキーな日よ♪」"
"エリスさまは雫さまの心配をするどころか、喜んでいる。"
voice "Sizuku0072"
sk "「短大でも、家でもエリスと一緒、これからもずっとエリスと一緒にいたいと思っているのです」"
voice "Erisu_0084"
e "「シズク～、ワタシもだよ♪」"
voice "Sizuku0073"
sk "「わたくしはエリスがいないと、生きていけません……エリスがそばにいてくれれば、それだけでいいのです{image=image/exch001.png}」"
voice "Erisu_0085"
e "「シズクって普段、そういうコト言ってくれないから……嬉しい{image=image/exch001.png}」"
"嬉しさのあまり、エリスさまは雫さまに抱きついてしまった。"
"人前でこんなことをしようものなら、驚いて怒ってしまう雫さまなのに。"


#allClear:
hide char ter02m at left
hide char tsi02m at right as r
#lastBG:
#scene bg bg37a
show char tma03m
with dis



voice "Mai_0199"
ma "「話に夢中になって、気にならないみたいだわ……はぁ～」"
"エリスさまに抱きつかれたまま、今度は玲緒にもお説教を始めた。"


show char tsi09m
with dis



voice "Sizuku0074"
sk "「ですから、エリスはわたくしのものです……玲緒さんには、ぜぇーったいに渡しません」"


show char tsi09m at left
show char tre03m at right as r
with dis



voice "Reo_0154"
re "「べっ、別に、ワタシは……」"
voice "Sizuku0075"
sk "「いいえ、玲緒さんはぜーったい、エリスの事が好きなんです」"
"もう、言ってることがめちゃくちゃです、雫さま。"
"すると玲緒はムキになって、反論する。"


show char tre08m at right as r
with dis



voice "Reo_0155"
re "「ワタシとエリスは、ただの喧嘩仲間なの」"
voice "Sizuku0076"
sk "「いいえ、そんなことはありません。玲緒さんとエリスが本気で喧嘩したら、玲緒さんなど消し飛んでしまいますわ」"


#allClear:
hide char tsi09m at left
hide char tre08m at right as r
#lastBG:
#scene bg bg37a
show char tma02m
with dis



voice "Mai_0200"
ma "「ぷぷっ」"
"け、消し飛ぶって……笑っちゃだめ。"
"笑っちゃだめよ、わたし。"


show char tsi09m at left
show char tre08m at right as r
with dis



voice "Reo_0156"
re "「だから、そういう意味じゃなくて……」"

hide char tsi09m at left
hide char tre08m at right as r
show char ter02m at sleft as l
show char tsi09m
show char tre08m at sright as sr
with dis



voice "Erisu_0086"
e "「ふふふ♪　シズク、またワタシを好きだって言ってよ」"
"エリスさまは雫さまに抱きついたまま、にやにやしている。"
"ここはもう……わたしが止めに入るしかないわね。"


#allClear:
hide char ter02m at sleft as l
hide char tsi09m
hide char tre08m at sright as sr
#lastBG:
#scene bg bg37a
show char tma08m
with dis



voice "Mai_0201"
ma "「はいそこまで、玲緒もムキにならない。元はといえばあなたがジュースを間違えたのが、いけないんだから」"


show char tma08m at left
show char tre08m at right as r
with dis



voice "Reo_0157"
re "「ぶー、ぶー」"


show char tma01m at left
with dis



voice "Mai_0202"
ma "「雫さまも、今お水もらってきますから、少し酔いをさまして下さいね」"


show char tsi09m at left
show char tma01m at right as r
with dis



voice "Sizuku0077"
sk "「だいたい麻衣さんがしっかり、玲緒さんを管理しておかないからいけないんですよ」"


show char tma04m at right as r
with dis



voice "Mai_0203"
ma "「わっ、わたし？」"
"話の矛先がいきなり、わたしに向けられた。"


show char tsi08m at left
with dis



voice "Sizuku0078"
sk "「ああいう子には、ちゃんと首輪でもつけておいたほうが……ヒック」"


show char tma03m at right as r
with dis



voice "Mai_0204"
ma "「は、はぁ……」"
"酔った上の言動なので、わたしはあまり気にはならないけど。"
"わたしの後ろで、玲緒が明らかにイライラしている気配がする。"
"このままだと、爆発しかねない……ああ。"
"どうか雫さま、これ以上玲緒を挑発しないで。"
voice "Sizuku0079"
sk "「だから、玲緒さんはエリスを好きになっても無駄ですよ」"

"ぷつん。"
#♀SE014
##se 0 SE014


"玲緒のなかで、何かが切れる音がした。"


#allClear:
hide char tsi08m at left
hide char tma03m at right as r
#lastBG:
#scene bg bg37a
show char tre09m
with dis



voice "Reo_0158"
re "「もうもう！　ワタシは麻衣が好きなの、麻衣が一番なのぉぉぉっ！！」"


show char tma04m at left
show char tre09m at right as r
with dis



voice "Mai_0205"
ma "「っっ！！」"


#**青空
#allClear:
hide char tma04m at left
hide char tre09m at right as r
#lastBG:
#scene bg bg37a
scene bg bg42a
with Dis



"玲緒の叫びは、部屋の外まで響いてしまい。"
"どうかなさないましたか？　と、ホテルの人が心配そうにドアをノックしてきたり……とにかく、大変だった。"
"でも……玲緒、あんなに大声で……"


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


"雫さまは言いたいことだけ言うと、こてんと眠りについてしまった。"


show char ter03m
with dis



voice "Erisu_0087"
e "「ゴメンね、玲緒、麻衣さん」"


#allClear:
hide char ter03m
#lastBG:
#scene bg bg37a
with dis


"エリスさまが珍しく、雫さまの代わりに謝ってきた。"
"なんかいつもと、立場逆転って感じよね。"
"まだ半分眠っている雫さまをかかえるようにして、帰っていった。"
"２人を見送り、いなくなったところで……わたしは玲緒の方を見て、小さく笑う。"


show char tma02m at left
show char tre08m at right as r
with dis



voice "Reo_0159"
re "「な、なによ、にやにやして……お説教なら聞かないわよ、今回の件は雫にだって問題があるんだから」"
voice "Mai_0206"
ma "「お説教なんてしないわ……わたしはね、素直に嬉しいのよ」"


show char tre03m at right as r
with dis



voice "Reo_0160"
re "「？？？」"
voice "Mai_0207"
ma "「玲緒……やっぱり玲緒は、わたしが一番なのね{image=image/exch001.png}」"


show char tre05m at right as r
with dis



voice "Reo_0161"
re "「あ、あれは……言葉のアヤで……」"
voice "Mai_0208"
ma "「あんなに大声で叫んでたじゃない、もぉ、素直じゃないんだから。玲緒、カワイすぎるわぁ{image=image/exch001.png}」"


#※EV009
#allClear:
hide char tma02m at left
hide char tre05m at right as r
#lastBG:
#scene bg bg37a
scene bg EV09
with Dis



voice "Reo_0162"
re "「ひゃん！　ちょ、ちょっと麻衣っ、なにしてるの」"
voice "Mai_0209"
ma "「だめ、我慢出来ないわ、抱かせて、触らせて、キスさせなさーい{image=image/exch001.png}」"
voice "Reo_0163"
re "「きゃっ、あぁん、止めてぇ、どうしてこうなるのよぉ」"
voice "Mai_0210"
ma "「ぜーんぶ、玲緒が悪いのよ。あんな愛の告白をされて、このわたしが黙っていられると思ってるの！？」"
voice "Reo_0164"
re "「だ、だからあれは、たまたま言っちゃっただけで……もう止めてぇ、麻衣のエロス～」"


#※EV009P1
scene bg EV09p1
with Dis



voice "Mai_0211"
ma "「今日のわたしは愛の暴走列車なの、ブレーキの壊れたラヴトレインよ！　とことん可愛がっちゃうんだから、玲緒っ{image=image/exch001.png}{image=image/exch001.png}」"
"あんな可愛らしい告白を聞かされて、我慢しろっていうのが無理な話なのよね。"
voice "Reo_0165"
re "「あぁん、ひゃぅん{image=image/exch001.png}　いつもより早すぎ、まだ脱がしちゃ……きゃんっ」"
voice "Mai_0212"
ma "「さあ、一気に脱ぎ脱ぎしましょうね、玲緒……んふふっ{image=image/exch001.png}」"


#**青空
scene bg bg42a
with Dis



"わたしはそのまま、玲緒をベッドに押し倒してしまって。"
"夕ご飯の時間までたーっぷりと、可愛がってあげたのでした{image=image/exch001.png}"
voice "Mai_0213"
ma "「はぁ、はぁ……今日の玲緒は『食後のデザート』ならぬ『食前酒』だったみたいね{image=image/exch001.png}」"
voice "Reo_0166"
re "「ま、麻衣の………………エロエロ、エロスぅぅ……むきゅ～」"


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
jump S024



