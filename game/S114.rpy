#「麻衣、あまり来なくなる……」

label S114:
$ save_name = "◇麻衣、あまり来なくなる……"


#**旧校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#♂MP08
play music "sound/BGM08.ogg"


show char tre03s2
with dis



voice "Reo_0723"
re "「ふにゅー、ギリギリセーフ、間に合ったぁ～」"
"昨日は変なＤＶＤを見てしまったせいか、なんだか寝付かれなくて。"
"すっかり、寝坊してしまった。"
"のんびり来ても良かったけれど……麻衣にお説教されるのもイヤだし。"
"だから走って、急いで教室まで来た。"
voice "mobJyosiA0106"
mobA "「玲緒さん、ごきげんよう」"
voice "Reo_0724"
re "「ご、ごきげんよう……はぁ、はぁ」"
voice "mobJyosiB0068"
mobB "「あら玲緒さん、汗びっしょりですわ」"
voice "mobJyosiA0107"
mobA "「大変ですわ、拭いてさしあげますわ」"
voice "Reo_0725"
re "「い、いいわよ～」"
voice "mobJyosiA0108"
mobA "「そんな、ご遠慮などなさらずに」"
"レースのハンカチがのびてきて、ごしごし拭かれてしまう。"
"うううっ……たくさんの人に囲まれて、麻衣の姿が見えないわ。"
"麻衣に昨日のこと、早く聞きたいのに……"
voice "mobJyosiC0038"
mobC "「玲緒さま、髪の毛が乱れてますわ。今、梳いてさしあげます」"
voice "Reo_0726"
re "「いいの、いらないって」"
voice "mobJyosiA0109"
mobB "「よかったら、キャンディをどうぞ」"
voice "Reo_0727"
re "「えっ？」"
"口の中に、飴が放り込まれる。"
"はちみつの味と甘さが、ふんわり広がった。"
"うん、美味しい♪"


show char tre02s2
with dis



voice "Reo_0728"
re "「はぁ～……」"
voice "mobJyosiA0110"
mobA "「まぁ、なんて幸せそうなお顔」"
voice "mobJyosiC0039B"
mobC "「本当に、玲緒さまは可愛いですわ。わたくしも飴をさしあげます、はい」"
voice "mobJyosiB0069"
mobB "「私も美味しい飴、あげますね。どうぞ」"
voice "mobJyosiA0111"
mobA "「わたしもまだまだ、たくさん持っていますわ。どうぞ」"

#ぽいぽい、ぽいぽいぽいぽいっ
#♀SE056
play sound "sound/SE056.ogg"


show char tre01s2
with dis



voice "Reo_0729"
re "「んじゅ、うんうん、どの飴も、美味しい……じゃないわ、人の口にいくつ、飴を入れるつもりなの、もごもごっ」"


show char tre09s2
with dis



voice "Reo_0730"
re "「もうアンタたち、邪魔よぉ、うきーっ！！」"
"両手をあげて、大声で叫ぶと。"
"蜘蛛の子を散らしたように、みんないなくなってしまった。"
voice "mobJyosiA0112"
mobA "「ふふふっ、楽しかったです……今朝はここまで」"
voice "mobJyosiB0070"
mobB "「玲緒さん、ごきげんよう～」"
"みんなにこにこしちゃって……ワタシ、いつの間にかクラスメイトのおもちゃにされてるような……"


show char tre08s2
with dis



voice "Reo_0731"
re "「そんなことより麻衣よ、麻衣っ！」"
"ワタシが大変な目に遭っているのに、全然助けにもこないんだから……薄情モノ！"


show char tma03s2
with dis



voice "Mai_0715"
ma "「………………」"
"麻衣の方を見ると、席についてぼんやりと教壇の方を眺めている。"


show char tre08s2
with dis



voice "Reo_0732"
re "「ちょっと麻衣、昨日のことだけど……」"

#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


show char tre03s2
with dis



voice "Reo_0733"
re "「うっ……」"
"授業が始まってしまう。"
"ワタシは麻衣のところへ行くのをあきらめて、自分の席に着いたのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**旧校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


show char tre03s2
with dis



voice "Reo_0734"
re "「まーい、どこに行ったのよ？」"
"休み時間になったのに、麻衣はワタシのところへ来るどころか、教室から消えていた。"
voice "Reo_0735"
re "「もう、どこにいるのかしら」"
"しばらく歩いていると、やっと麻衣を発見した。"
voice "Reo_0736"
re "「……えっ？　ここって……」"
"なんと麻衣は、職員室から出てきたところだった。"
"こんなところで一体、何しているのかしら。"


show char tma01s2 at left
show char tre03s2 at right as r
with dis



voice "Mai_0716"
ma "「あら、玲緒……どうしたの？」"
voice "Reo_0737"
re "「どうしたって、麻衣を探してたのよ」"
voice "Mai_0717"
ma "「わたしを？　なになに一人で教室にいたら、寂しくなっちゃったの？」"


show char tre08s2 at right as r
with dis



voice "Reo_0738"
re "「ち、違うわよ！　それより職員室で、何してたのよ」"


show char tma03s2 at left
with dis



voice "Mai_0718"
ma "「ちょっと担任の先生に、家のことでね……」"


show char tre03s2 at right as r
with dis



voice "Reo_0739"
re "「おうちのこと？」"


show char tma01s2 at left
with dis



voice "Mai_0719"
ma "「別に、大した話じゃないわ。早く教室に戻りましょう、もうすぐチャイム鳴るわよ」"
voice "Reo_0740"
re "「う、うん……」"


#allClear:
hide char tma01s2 at left
hide char tre03s2 at right as r
#lastBG:
#scene bg bg05a
with dis


"なんか怪しい、麻衣。"
"麻衣の言うところの、ワタシの野生のカンが、ぴくぴくそう告げていた。"


#**青空
scene bg bg42a
with Dis



"そして見事に、ワタシのカンは当たってしまった。"
"その日から、麻衣は学校には来ていても、ワタシの部屋や委員会にはあまり、顔を出さなくなってしまった……。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**旧校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#//SE：チャイムの音
#♀SE001
play sound "sound/SE001.ogg"


voice "mobJyosiA0113"
mobA "「皆さん、ごきげんよう」"
voice "mobJyosiB0071"
mobB "「ごきげんよう、また明日」"
"授業が終わり、みんなそれぞれに、別れの挨拶をしている。"
"今日もイベント実行委員会はあるけれど、麻衣は慌ただしく帰り支度をしていた。"


show char tre03s2
with dis



voice "Reo_0741"
re "「麻衣……今日も委員会、でないの？」"


show char tma03s2 at left
show char tre03s2 at right as r
with dis



voice "Mai_0720"
ma "「うん、ごめんね。ちょっとね……みんなにもよろしく伝えておいてね」"
voice "Reo_0742"
re "「ここんとこずっとじゃない、何か理由があるの？」"
voice "Mai_0721"
ma "「急いでいるの、ゴメンね、玲緒」"


hide char tma03s2 at left
with dis


voice "Reo_0743"
re "「あっ……」"
"麻衣はそのまま、帰ってしまった。"


#allClear:
hide char tre03s2 at right as r
#lastBG:
#scene bg bg04a
show char tre03s2
with dis



voice "Reo_0744"
re "「麻衣……もう、ばか……」"
"『黒髪会』のことを教えてくれなかった時も、なんかイヤだったけど。"
voice "Reo_0745"
re "「……今の方が、もっとイヤだわ」"
"なんで麻衣は、ワタシに何も話してくれないんだろう。"
voice "Reo_0746"
re "「麻衣、何があったのよぉー」"


#**委員会室・昼
#allClear:
hide char tre03s2
#lastBG:
#scene bg bg04a
scene bg bg30a
with Dis



show char tna01s2
with dis



voice "Nanami1206"
n "「優菜さま、こっち塗り終わりました」"


show char tyu01s2 at left
show char tna01s2 at right as r
with dis



voice "Yuuna_0904"
y "「あらっ、綺麗に仕上がったわね。じゃあ、この空いてるところに乾かしておきましょうね」"


show char tna02s2 at right as r
with dis



voice "Nanami1207"
n "「はいっ{image=image/exch001.png}」"


show char tyu02s2 at left
with dis



voice "Yuuna_0905"
y "「良い返事ね。七海もずいぶんしっかりしてきたわね」"
voice "Nanami1208"
n "「ありがとうございます、ふふふっ」"


#allClear:
hide char tyu02s2 at left
hide char tna02s2 at right as r
#lastBG:
#scene bg bg30a
show char tre03s2
with dis



voice "Reo_0747"
re "「………………」"


show char tri01s2
with dis



voice "Risa_1932"
r "「美夜、書類チェックお願いできるかしら」"


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



voice "Miya_1133"
m "「ええ、もうやっておいたわ」"


show char tri02s2 at right as r
with dis



voice "Risa_1933"
r "「わぁ、さすが仕事が早いわね」"


show char tmi02s2 at left
with dis



voice "Miya_1134"
m "「当然よ。そのかわり、後でたっぷりとごほうびを……」"


#allClear:
hide char tmi02s2 at left
hide char tri02s2 at right as r
#lastBG:
#scene bg bg30a
show char tri01s2
with dis



voice "Risa_1934"
r "「あっー、六夏、こっち手伝ってくれる？」"


show char tri01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_1641"
rk "「はい、リサ姉」"

hide char tri01s2 at left
hide char trk01s2 at right as r
show char tri01s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0914"
s "「私も、手伝います」"


#allClear:
hide char tri01s2 at sleft as l
hide char trk01s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tmi02s2
with dis



voice "Miya_1135"
m "「……ふふふっ、すぐ照れるんだから、璃紗ったら」"


show char tmi02s2 at left
show char tri05s2 at right as r
with dis



voice "Risa_1935"
r "「てっ、照れてないわよ、もうっ」"


#allClear:
hide char tmi02s2 at left
hide char tri05s2 at right as r
#lastBG:
#scene bg bg30a
show char tre03s2
with dis



voice "Reo_0748"
re "「……なんだかな～」"
"みんな楽しそうに、仕事しているみたい。"
"ワタシは委員のみんなの仕事っぷりを、ただただ眺めていた。"


show char tsa03s2
with dis



voice "Sara_0876"
sr "「玲緒さま……静かですね」"


show char tka03s2 at left
show char tsa03s2 at right as r
with dis



voice "Kaede_0885"
k "「きっと麻衣さんがいないから、寂しいのね」"
voice "Sara_0877"
sr "「麻衣さまのこと、楓ちゃん聞いてる？」"
voice "Kaede_0886"
k "「私は、何も……ただ家の事情だってことくらいしか知らないわ」"


#allClear:
hide char tka03s2 at left
hide char tsa03s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"そう。"
"麻衣は家の事情とだけ言って、委員会をずっと休んでいた。"
"具体的な理由は言わず、いつまで休むかも言わず。"
"理由は、ぜんぜんわからない。"


show char tre03s2
with dis



voice "Reo_0749"
re "「うううっ……」"
"思い切って、麻衣の家に行ってみたいけど。"
"委員会の終わりまでいると、結構遅くなってしまうから、そんな時間に尋ねるのが非常識だってことは、さすがにワタシでもわかる。"
"本当なら、今すぐにでも帰りたい。"
"でも目の前には、やらなきゃいけない仕事がたくさんあるから、それもできない。"


show char tre08s2
with dis



voice "Reo_0750"
re "「麻衣が来れないんだもの……麻衣の分まで、ワタシが……頑張らなくちゃ……えっ？？」"


stop music fadeout 1


#※EV073
#allClear:
hide char tre08s2
#lastBG:
#scene bg bg30a
scene bg EV73
with Dis


play music "sound/BGM20.ogg"


voice "Miya_1136"
m "「玲緒さま……」"
voice "Reo_0751"
re "「……えっ？　綾瀬美夜、いつの間に……いったい何の用？」"
voice "Miya_1137"
m "「はい……これ、どうぞ」"
"綾瀬美夜は、ワタシの手になにかを握らせた。"
voice "Reo_0752"
re "「これは……お取り寄せで半年待ちって言われてる、幻のラスクじゃない」"
"テレビでたびたび、紹介されているけれど。"
"本物を見るのは、これが初めてだわ。"
voice "Reo_0753"
re "「も、もらっていいの？　後で返してって言っても知らないからねっ」"
voice "Miya_1138"
m "「いいわ。玲緒さまがお好きなだけ、どうぞ」"
voice "Reo_0754"
re "「あ、ありがとう……」"
voice "Yuuna_0906"
y "「あら、美味しそうね♪」"
voice "Reo_0755"
re "「……松原優菜」"
voice "Yuuna_0907"
y "「そうだわ、私も美味しいお菓子持ってるのよ、今あげるから待ってて」"
voice "Reo_0756"
re "「う、うん……ありがと……」"
"そう言って、優菜は自分の仕事を一時中断させて、カバンの中からお菓子の包みを取り出しワタシにくれた。"
voice "Reo_0757"
re "「………………」"
voice "Yuuna_0908"
y "「お菓子ばかりじゃ、喉が渇くわよね。待ってて、今お茶でも入れてきましょう」"
voice "Reo_0758"
re "「あっ……大丈夫」"
voice "Yuuna_0909"
y "「そう。じゃあどうぞ」"
voice "Reo_0759"
re "「い……いただきます」"
"ワタシは袋からラスクを取り出し、ぱくっと１枚口にいれる。"
"それは今まで食べたどのラスクよりも、美味しかった。"
voice "Reo_0760"
re "「はむはむ……んっ、美味しい」"
"続いて、優菜からもらったお菓子も開けようとして……その手が止まる。"
voice "Reo_0761"
re "「うううっ……」"
"いくら、美味しいお菓子を食べても。"
"ワタシの気持ちは全然、晴れなかった。"
"心の中は麻衣のことでいっぱいで、寂しさは拭えなかった。"
voice "Reo_0762"
re "「うぅっ、うぅぅっ……ま……麻衣ぃ……ひっく」"


#※EV073P1
scene bg EV73p1
with Dis



"我慢しようと、ぎゅっと目を閉じても、溢れてくる涙を止めることができない……何故なの？"
voice "Yuuna_0910"
y "「……玲緒さん」"
voice "Miya_1139"
m "「……玲緒さま」"
"横では２人が、心配そうにワタシをみていたけど……"
"泣いているのを見られて、ちょっと恥ずかしいけれど。"
voice "Reo_0763"
re "「うううっ……ひっく……麻衣ぃ」"
"涙はどんどん溢れて、止まりそうになかった……。"


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
jump S115



