#「みんなから、祝福されて」

label S044:
$ save_name = "◇みんなから、祝福されて"

#（六夏視点に戻す）

#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP13
play music "sound/BGM13.ogg"


show char trk02s2
with dis



voice "Rikka_1149"
rk "「さぁ、今日も委員会、頑張っていきましょうね、沙雪さん」"


show char trk02s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0613"
s "「ええ……そうですね、六夏さん」"
"なんだか委員会に行くだけでも、今までよりずっと楽しい。"
"ううん、きっと沙雪さんさえ一緒にいてくれたら、そこが地獄だとしても、ワタシはきっと幸せなんだ。"
"２人きりだし、手を繋ぎたい……でもここは校内だし、廊下だし。"
"その願望は、今はグッと堪えた。"
"委員会が終わって、帰る時に繋げばいいよね、うん。"
voice "Risa_0872"
r "「ねぇ、六夏」"
"不意に呼びかけてきたその声は、リサ姉のものだった。"

hide char trk02s2 at left
hide char tsy01s2 at right as r
show char tmi01s2 at sleft as l
show char tri01s2
show char trk03s2 at sright as sr
with dis



voice "Rikka_1150"
rk "「なぁに、リサ姉………………と、美夜……さま」"
voice "Miya_0503"
m "「ごきげんよう、六夏さん、沙雪さん」"
voice "Rikka_1151"
rk "「ご、ごきげん……よう……」"
"リサ姉だけだと思ったら、なんと美夜さまも一緒だった。"
"なんかワタシ、どうも苦手なの……美夜さまって。"
"きっと例の『浮気疑惑』の時、その怖さをたっぷり思い知らされたからだと思うけれど。"


show char trk03s2
show char tsy02s2 at sright as sr
with dis



voice "Sayuki0614"
s "「ごきげんよう、璃紗さま、美夜さま……ふふっ{image=image/exch001.png}」"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0504"
m "「ふふふっ{image=image/exch001.png}」"
voice "Rikka_1152"
rk "「………………？？」"


#allClear:
hide char tmi02s2 at sleft as l
hide char trk03s2
hide char tsy02s2 at sright as sr
#lastBG:
#scene bg bg05a
with dis


"何なの、今の？"
"沙雪さんと美夜さま、なんかこれまでと雰囲気が違う……どこか親しげに見えてしまう。"
"ワタシは苦手なのに、沙雪さんはそうでもないどころか、明らかに距離が縮まっているし。"
"一体、二人の間に何があったっていうの……？？"
"その疑問を考える時間も、沙雪さんに問いかける時間も、ワタシは与えてもらえなかった。"


show char tri02s2
with dis



voice "Risa_0873"
r "「ねっ、六夏。ちょっと付き合って欲しいんだけど」"


show char tri02s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_1153"
rk "「えっ、ワタシ？」"

hide char tri02s2 at left
hide char trk03s2 at right as r
show char tmi02s2 at sleft as l
show char tri02s2
show char trk03s2 at sright as sr
with dis



voice "Miya_0505"
m "「そう、六夏さんよ。ちょっと話したい事があるの……一緒に来て」"
voice "Rikka_1154"
rk "「そ……それは……ぅぅ……」"
"ワタシを手招きする、リサ姉と美夜さまの笑顔が、何だか怖い。"
"嫌な予感がする……ワタシの野生的な本能がビンビンに、それを感じていた。"
"危ない、危険信号が点滅している。"
"逃げなくちゃ、着いていってはダメ……"
voice "Rikka_1155"
rk "「あ、あの……今から委員会ですし、用事ならまた後で……ねぇ、沙雪さん？」"
voice "Miya_0506"
m "「沙雪さん、ちょっとだけ六夏さんをお借りするわね」"


show char trk03s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0615"
s "「はい、わかりました……それでは六夏さん、また後ほど」"


show char trk04s2
with dis



voice "Rikka_1156"
rk "「えっ、えぇっ、さ、沙雪さぁん……ぅぅ……」"


#allClear:
hide char tmi02s2 at sleft as l
hide char trk04s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg05a
with dis


"不安が募る、ドンドン大きくなっていく。"
"沙雪さんはワタシを見捨てるように、一人行ってしまった。"


show char tri02s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0874"
r "「さぁ、行きましょうか……六夏、んふふっ{image=image/exch001.png}」"
"ワタシはリサ姉と美夜さまに、連行されていった……"


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


show char tmi01s2
with dis



voice "Miya_0507"
m "「うん、ここならいいわね。誰もいないし」"


show char trk03s2
with dis



voice "Rikka_1157"
rk "「だ……誰もいない、教室……」"
"なんでこんな場所に連れてこられたのか、心当たりはまったくなかった。"
"リサ姉も一緒で、楽しそうな顔をしているってコトは、もう浮気疑惑は関係なさそうだし。"
"この２人に、こんな風にされる理由が、ワタシにはサッパリだった。"


show char tri01s2 at left
show char trk03s2 at right as r
with dis



voice "Risa_0875"
r "「六夏……優菜さまから、聞いたわよ」"


show char trk04s2 at right as r
with dis



voice "Rikka_1158"
rk "「ゆ、優菜さまから……あぁっ！！」"
"その名前を聞いた瞬間、ちょっとだけ分かったような気がした。"
"何故ワタシが、人気のないこの教室に、連れてこられたのか？"
"それは……"
hide char tri01s2 at left
hide char trk04s2 at right as r
show char tmi01s2 at sleft as l
show char tri01s2
show char trk04s2 at sright as sr
with dis



voice "Miya_0508"
m "「六夏さん、貴女、委員会が終わった後、優菜さまに鍵を借りて、残ったそうね……沙雪さんと一緒に」"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1159"
rk "「どうして美夜さまが、そんな事を……」"
"……って、優菜さまに聞いたからに決まっている。"
"ああ、優菜さまって思っていた以上に、おしゃべりな方なのかも……"
voice "Risa_0876"
r "「でもね、六夏。優菜さまはみんなに言ったのよ。『六夏さんと沙雪さんに何があったか……気にはなるけれど、野暮な事はしないでおきましょう』って」"


show char trk01s2 at sright as sr
with dis



voice "Rikka_1160"
rk "「優菜、さま……良い方ですね。だったら……」"
voice "Risa_0877"
r "「でもね、六夏……やっぱり、気になるじゃない？」"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1161"
rk "「えっ？」"
voice "Miya_0509"
m "「ずっと貴女を近くで見守ってきた、わたくしたちだもの……どうなっているのか、すっごく気になるわ」"


show char trk04s2 at sright as sr
with dis



voice "Rikka_1162"
rk "「えぇぇっ！？」"
"だからこうして人気のないところに連れてきて、聞き出そうとしていたのね。"


show char tri02s2
with dis



voice "Risa_0878"
r "「さあ……さあさあ、聞かせてもらおうかしら、六夏と沙雪さんの事を♪」"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0510"
m "「一体どこまで、進んだのかしら……ああ、気になるわ♪」"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1163"
rk "「そ、そんな……ぅぅっ、どうして話さなくちゃいけないんですか……？」"
voice "Risa_0879"
r "「そんなの、決まってるじゃない。聞きたいからよ、人の恋バナってすっごく楽しいの{image=image/exch001.png}」"


show char tmi01s2 at sleft as l
with dis



voice "Miya_0511"
m "「ほらほら、しっかりと聞かせてちょうだい。さもないと……」"
voice "Rikka_1164"
rk "「さ、さもないと……？」"
voice "Miya_0512"
m "「六夏さんをそこの椅子に縛りつけて、沙雪さんをここに呼ぶわよ」"
voice "Risa_0880"
r "「沙雪さんだったらきっと、喜んで話してくれそうね……二人がどこまで進んだか」"


show char trk04s2 at sright as sr
with dis



voice "Rikka_1165"
rk "「ひぃぃぃっ！！　そっ、それだけは許してください、ダメぇぇっ！！」"
"沙雪さんだったら本当に、全部話してしまいそうで、すごく怖い。"
"全部話されてしまったら、ワタシ……もう恥ずかしくて委員会に顔を出せない、ううん、生きていけないかも。"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1166"
rk "（そんなコトになるくらいなら……ここは、自分で……）"
"全部、１００％、話す必要はないんだから。"
"適当にはぐらかしつつ、７０％くらいの報告で……"
voice "Rikka_1167"
rk "「わ……わかりました、言います、言いますから……沙雪さんは、呼ばないで下さい。お願いします」"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0513"
m "「そうそう、最初からそうやって、聞き分けよくしてくれれば良かったのよ{image=image/exch001.png}」"
voice "Risa_0881"
r "「さあ、聞かせて、六夏……貴女と沙雪さんの、恋の進展を」"
voice "Rikka_1168"
rk "「うぅっ、は、はい……」"


#**青空
#allClear:
hide char tmi02s2 at sleft as l
hide char tri02s2
hide char trk03s2 at sright as sr
#lastBG:
#scene bg bg04a
scene bg bg42a
with Dis



"ああ、ごまかすにしても、どこまで話せばいいのか。"
"ウソを言ったら、バレてしまいそうだし……特に、眼光鋭い美夜さまに。"
"仕方なく、ちょっとずつかいつまんで、ワタシは２人に報告をした。"
"沙雪さんとデートして以来、他の事が考えられなくなるほど、彼女の事で頭がいっぱいになって。"
"このままじゃ、おかしくなってしまいそうで……だからその想いを、沙雪さんに告げたくなって。"
"どうしても二人きりで、他の誰にも邪魔されないように言いたかったから、優菜さまに鍵を借りて。"
"そこで沙雪さんに、自分の想いの全てをぶつけた……と。"


#**新校舎教室・昼
scene bg bg04a
with Dis



show char tmi08s2 at sleft as l
show char tri08s2
show char trk03s2 at sright as sr
with dis



voice "Rikka_1169"
rk "「………………」"
"そこまで話し終えたワタシを、リサ姉と美夜さまはじっと見つめていた。"
"でも二人のその表情は、明らかに不満たっぷりだった。"
voice "Miya_0514"
m "「それで……どうなったわけ？」"
voice "Rikka_1170"
rk "「そ、それでって……もう、終わりですが……」"
voice "Miya_0515"
m "「それはおかしいわね、六夏さん。だって貴女は二人きりになって、自分の想いを告白したのでしょう？」"
voice "Rikka_1171"
rk "「は、はい……しました、沙雪さんに……」"
"そこに今度は、リサ姉が割り込んできた。"
voice "Risa_0882"
r "「だったら沙雪さん、返事をしてくれたわよね？　どんな返事をくれたの？？」"
voice "Rikka_1172"
rk "「それは……ワタシも、嬉しいと……言ってくれました」"


show char tri02s2
with dis



voice "Risa_0883"
r "「良かったじゃない、六夏！　だったらすぐ、沙雪さんにキスしたわよね？　抱きしめたわよね？」"


show char trk05s2 at sright as sr
with dis



voice "Rikka_1173"
rk "「そ、そんな事まで、言わなくちゃ……ダメ、なの？」"
"今度はしびれを切らした美夜さまが、また割り込んできた。"
voice "Miya_0516"
m "「言わなきゃダメに決まってるじゃない。どうなの？　ギュッと抱きしめたの？　熱いキスを交わしたの？」"
"目が血走ってみえたこの二人に、もうワタシは抗えそうになかった。"
"完全に、気迫負けしてしまったのだ。"
voice "Rikka_1174"
rk "「し、しました……沙雪さんをギュッと抱きしめて、キスして……ひゃんっ{image=image/exch001.png}」"
"そう告白したワタシを、リサ姉が強くつよく、抱きしめてくれた。"
voice "Rikka_1175"
rk "「りっ、リサ姉、どうして……ぁん{image=image/exch001.png}」"
voice "Risa_0884"
r "「六夏、良かったね。本当に良かったね……なんか私、自分の事のように嬉しいわ♪」"


show char trk02s2 at sright as sr
with dis



voice "Rikka_1176"
rk "「リサ姉……ありがとう。ワタシが沙雪さんと結ばれるコトができたのは、リサ姉のおかげだよ」"
"思わずワタシも、リサ姉に抱きついてしまった。"
"嬉しくて、嬉しくてたまらなくて、つい……でも、気づいてしまった。"
"リサ姉に抱きしめられているワタシを見つめる……ううん、睨んでいる視線に。"


show char tmi09s2 at sleft as l
with dis



voice "Miya_0517"
m "「り、六夏さん……やっぱり貴女、本当は璃紗の事を……」"


show char trk04s2 at sright as sr
with dis



voice "Rikka_1177"
rk "「ひっ、ち、ちちっ、違いますぅっ！！」"
"ワタシは慌てて、リサ姉から体を離した。"
"このまま抱き合っていたら、命の危険を感じたからだった。"


show char trk03s2 at sright as sr
with dis



voice "Rikka_1178"
rk "「み、美夜さま、信じてください。ワタシが愛しているのは、沙雪さんだけなんです、本当ですっ！！」"


show char tmi08s2 at sleft as l
with dis



voice "Miya_0518"
m "「六夏さん……さっき貴女、言ったわね。『沙雪さんと結ばれるコトができた』って」"
voice "Rikka_1179"
rk "「は、はい……言いました……けど」"


show char tmi02s2 at sleft as l
with dis



voice "Miya_0519"
m "「それって、つまり………………したって事よね、エッチを{image=image/exch001.png}」"


show char trk05s2 at sright as sr
with dis



voice "Rikka_1180"
rk "「っっ！！」"
"そんな……全部分かっちゃったの！？"
"ワタシ、口を滑らせてしまったの？"
"でも『結ばれるコトができた』って言っただけ、心と心が結ばれたって意味もあるし……"
voice "Risa_0885"
r "「ああ、六夏……ついにそこまで……本当に、おめでとう♪」"
"再び、ワタシに抱きつきそうになったリサ姉から身を引き、慌てて手を振った。"
voice "Rikka_1181"
rk "「だ、だからワタシ、そんなコトは……心と心が、結ばれたっていうか……」"


show char tmi09s2 at sleft as l
with dis



voice "Miya_0520"
m "「ゴチャゴチャ言ってないで、ハッキリしなさいっ！　エッチしたの、してないのっ！？」"


show char trk04s2 at sright as sr
with dis



voice "Rikka_1182"
rk "「ひっ、し、しました、エッチしましたぁぁっ」"


#allClear:
hide char tmi09s2 at sleft as l
hide char tri02s2
hide char trk04s2 at sright as sr
#lastBG:
#scene bg bg04a
with dis


"ああ、ワタシのバカ……美夜さまの押しに、迫力に負けて、言っちゃったよぉ。"
"どうしよう、沙雪さんに呆れられるかも。"
"リサ姉と、美夜さまに知られてしまうなんて……"

#♀SE003
play sound "sound/SE003.ogg"


show char tyu02s2
with dis



#//SE：拍手喝采
#♀SE017
play sound "sound/SE017.ogg"


voice "Yuuna_0171"
y "「おめでとう、六夏ちゃん{image=image/exch001.png}」"


show char trk04s2
with dis



voice "Rikka_1183"
rk "「ええええぇぇっ！？」"
"教室のドアが開け放たれ、いきなり入ってきたのは、優菜さまだった。"
"ううん、優菜さまだけじゃない。"
"七海さまも、麻衣さまも、玲緒さまも。"
"今日はお仕事がないのか、楓さまや紗良さまも。"
"なんとなんと、沙雪さんまでも、一緒に入ってきたのだった。"


show char trk03s2
with dis



voice "Rikka_1184"
rk "「さ、沙雪さん……ぅぅ、その、こ、これは……」"


show char trk03s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0616"
s "「……いいんです、六夏さん。皆さんに話して下さって、私……嬉しいです{image=image/exch001.png}」"
"頬を赤らめながら、ニッコリと。"
"ちょっと泣きそうな、でも嬉しそうに、沙雪さんが微笑んでいた。"

#//SE：拍手喝采
#♀SE017
play sound "sound/SE017.ogg"


"再び、大きな拍手が、ワタシと沙雪さんを包んだ。"


#allClear:
hide char trk03s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg04a
show char tma02s2
with dis



voice "Mai_0242"
ma "「本当におめでとう、六夏ちゃん、沙雪ちゃん。良かった良かった」"


show char tma02s2 at left
show char tre03s2 at right as r
with dis



voice "Reo_0186"
re "「まあ……良かったんじゃないの」"


show char tma08s2 at left
with dis



voice "Mai_0243"
ma "「ちょっと玲緒、もっとちゃんと祝福しなさいよね……」"


show char trk05s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0617"
s "「ありがとうございます、麻衣さま、玲緒さま」"
voice "Rikka_1185"
rk "「あ、ありがとう……ございます……」"


#allClear:
hide char trk05s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg04a
show char tna02s2
with dis



voice "Nanami0263"
n "「これでやっと、本当の意味で『ベストカップル』ですね」"


show char tsa02s2 at left
show char tna02s2 at right as r
with dis



voice "Sara_0158"
sr "「うんうん、二人ともすっごく幸せでしょう、ね、ねっ？」"

hide char tsa02s2 at left
hide char tna02s2 at right as r
show char tka02s2 at sleft as l
show char tsa02s2
show char tna02s2 at sright as sr
with dis



voice "Kaede_0126"
# "【　楓　】「紗良、そんな事、聞かなくても分かるでしょう……本当に、良かったわね」"


#allClear:
hide char tka02s2 at sleft as l
hide char tsa02s2
hide char tna02s2 at sright as sr
#lastBG:
#scene bg bg04a
show char tsy02s2
with dis



voice "Sayuki0618"
s "「はい、楓さま、紗良さま、七海さま……私、皆さんに祝福されて、本当に幸せです」"


show char trk01s2 at left
show char tsy02s2 at right as r
with dis



voice "Rikka_1186"
rk "「沙雪さん……」"
"なんかちょっとだけ、沙雪さんの気持ちが分かったような気がした。"
"自分が幸せになって、その幸せがドンドン膨らんでいくと。"
"自分の中だけに収まり切れなくなって、周りに広がっていく。"
"沙雪さんは、本当にたくさんの幸せを感じてくれていて。"
"だからワタシとのコトを、みんなに話してしまうんだ……幸せすぎるから。"


show char trk02s2 at left
with dis



voice "Rikka_1187"
rk "「沙雪さん、ワタシ……すごく恥ずかしいけれど、皆さんに祝福されるのって……とっても、嬉しいですね」"
voice "Sayuki0619"
s "「はい、嬉しいです……とっても、幸せです{image=image/exch001.png}」"
"微笑みあう、ワタシと沙雪さん。"
"ワタシの肩をリサ姉が、沙雪さんの肩を美夜さまが、軽く叩いて笑顔をくれた。"


show char tri02s2 at left
show char trk01s2 at right as r
with dis



voice "Risa_0886"
r "「本当におめでとう、六夏。貴女と沙雪さんが幸せになってくれて、自分の事のように、嬉しいわ」"
voice "Rikka_1188"
rk "「リサ姉……」"


show char tmi02s2 at left
show char tsy02s2 at right as r
with dis



voice "Miya_0521"
m "「沙雪さん、貴女の幸せを心から祝福するわ……お互いにね」"
voice "Sayuki0620"
s "「そうですね、お互いに……ふふふっ{image=image/exch001.png}」"
"やっぱり、この２人の間に何かあったような気がしてならない、ワタシ……"
"でも、祝福してくれている気持ちは、本物だから……嬉しいです、美夜さま。"


#allClear:
hide char tmi02s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"優菜さまは、ワタシと沙雪さん、そしてリサ姉と美夜さまを見ながら言った。"


show char tyu02s2
with dis



voice "Yuuna_0172"
y "「本当におめでとう、六夏ちゃん、沙雪ちゃん。二人がどうなるか、ずっと心配だったわ」"


show char tyu01s2
with dis



voice "Yuuna_0173"
y "「半年前、璃紗ちゃんと美夜ちゃんを見守っていた時以上に、ハラハラしていたのよ」"


show char tri05s2
with dis



voice "Risa_0887"
r "「ちょ、ちょっと優菜さま、もう……止めてください、恥ずかしい……」"


show char tmi01s2 at left
show char tri05s2 at right as r
with dis



voice "Miya_0522"
m "「応援、ありがとうございました。わたくしと璃紗はもう大丈夫ですから……これからは皆さん、沙雪さんと六夏さんを温かく見守ってあげて下さいね」"
"照れまくりのリサ姉、余裕の美夜さま。"
"こんなに仲の良い二人も、半年前は大変だったのね……でも今は、どこからどう見ても、ラブラブ度２５０％超の無敵カップル。"


#allClear:
hide char tmi01s2 at left
hide char tri05s2 at right as r
#lastBG:
#scene bg bg04a
show char trk02s2
with dis



voice "Rikka_1189"
rk "「ワタシと沙雪さんも、もっともっと仲良くなって……もっともっと……んふふっ{image=image/exch001.png}」"


show char tmi01s2 at left
show char trk02s2 at right as r
with dis



voice "Miya_0523"
m "「あらあら、何だか嬉しそうね、六夏さん……ところで初エッチは、どんなプレイだったのかしら？」"


show char trk03s2 at right as r
with dis



voice "Rikka_1190"
rk "「………………へっ？」"
voice "Miya_0524"
m "「もちろん貴女が、沙雪さんを愛してあげたのよね？　どこをどんな風に愛してあげたのかしら？」"


show char trk04s2 at right as r
with dis



voice "Rikka_1191"
rk "「そそそっ、そんなコト、絶対言えませんっ！！」"


#allClear:
hide char tmi01s2 at left
hide char trk04s2 at right as r
#lastBG:
#scene bg bg04a
show char tsy05s2
with dis



voice "Sayuki0621"
s "「六夏さんは……情熱的なキスをして、私の体をそっと抱き寄せて下さいました。そして私の……花びらを、そっと指で……{image=image/exch001.png}」"


show char trk04s2 at left
show char tsy05s2 at right as r
with dis



voice "Rikka_1192"
rk "「さっ、沙雪さん、お願い、止めてぇぇ～っ！！」"


#**青空
#allClear:
hide char trk04s2 at left
hide char tsy05s2 at right as r
#lastBG:
#scene bg bg04a
scene bg bg42a
with Dis



"美夜さまやみんなに問い詰められ、冷やかされ、超恥ずかしくて。"
"でも………………やっぱり、嬉しくて。"
"沙雪さんだけじゃない、ここにいる皆さんと出会えて、本当に良かったです。"


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


$ _skipping = False
$ _dismiss_pause = False
#log off

scene image "image/eyecatch01.png"
with vs

pause 3

scene black
with Dis

#log on
$ _skipping = True
$ _dismiss_pause = True


#//END
jump S045



