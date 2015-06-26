#「ママとの話し合い……」

label S061:
$ save_name = "◇ママとの話し合い……"


#**璃紗の部屋・昼
scene bg bg01a
with Dis



#mes on
#system on


#♂MP09
play music "sound/BGM09.ogg"


#//SE：チャイム音
#ピンポーン♪
#♀SE024
play sound "sound/SE024.ogg"


"休日の朝。"
"私はいきなりの、チャイムの音で起こされた。"


show char tri03f2
with dis



voice "Risa_1333"
r "「もう……こんな早くに、一体誰かしら？」"
"急いで着替えてから、玄関に向かった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**安曇家ダイニング・昼
scene bg bg02a
with Dis



#mes on
#system on


show char tmi01f2
with dis



voice "Miya_0845"
m "「いきなりで悪かったわね、璃紗」"


show char tmi01f2 at left
show char tri03f2 at right as r
with dis



voice "Risa_1334"
r "「もう、びっくりしたわよ。寝起きの悪い美夜がこんな時間に、ウチに来るなんて……」"


show char tmi02f2 at left
with dis



voice "Miya_0846"
m "「ふふふっ、今朝はウチの会社の地方にある支店に、これから行くのよ」"
voice "Risa_1335"
r "「それじゃあ、もしかして……車？」"


show char tmi01f2 at left
with dis



voice "Miya_0847"
m "「ええ、玄関のところに止めてあるわ」"


show char tri01f2 at right as r
with dis



voice "Risa_1336"
r "「そう……」"
"だったら、早朝で良かったかも。"
"だって美夜の家の高級車、すごく目立つんだもの。"
voice "Risa_1337"
r "（近所の人が見たら……きっと、驚いてしまいそうだわ）"
voice "Miya_0848"
m "「それより今日、お母様が家にいらっしゃるんでしょう？」"
voice "Risa_1338"
r "「多分、来るのは昼過ぎくらいよ」"
"ママからメールがあった後。"
"ママの都合を聞いて、今日来てもらうことになっていたのは、美夜にも話したけれど。"
"それと今、美夜がウチに来たこととは、何の関係があるのかしら？"
voice "Miya_0849"
m "「これ……お母様に」"
"美夜が菓子折りをそっと差し出す。"
voice "Risa_1339"
r "「あっ……わざわざありがとう。このために来てくれたの？」"
voice "Miya_0850"
m "「それもあるけれど、璃紗の早朝ハプニングにも期待していたのよ」"


show char tri03f2 at right as r
with dis



voice "Risa_1340"
r "「……はい？」"


show char tmi03f2 at left
with dis



voice "Miya_0851"
m "「熟睡しているところを起こされて、パジャマ姿のまま無防備に現れる……レアキャラの『ぼんやり璃紗』が出てくるとばかり、思っていたのに……」"


show char tri01f2 at right as r
with dis



voice "Risa_1341"
r "「寝起きはいいのよ、私って」"
voice "Miya_0852"
m "「ふうううう～」"
"美夜は本当に残念そうに、深くため息をついた。"
"本気で早朝ハプニングなんて、あると思ったのかしら？"


show char tmi01f2 at left
with dis



voice "Miya_0853"
m "「じゃあわたくし、そろそろ行くわね」"


show char tri02f2 at right as r
with dis



voice "Risa_1342"
r "「うん。このお菓子、ありがとうね」"


show char tmi03f2 at left
with dis



voice "Miya_0854"
m "「急いでたから、１箱しか持ってこれなかったけど」"


show char tri03f2 at right as r
with dis



voice "Risa_1343"
r "「ひっ、１箱で十分だから……普通の人は」"


show char tmi01f2 at left
with dis



voice "Miya_0855"
m "「お母様も璃紗と同じで、小食なのね」"


show char tri01f2 at right as r
with dis



voice "Risa_1344"
r "「ま、まあね……うん、そういうことにしておくわ」"
voice "Miya_0856"
m "「それじゃ、ごきげんよう」"


show char tri08f2 at right as r
with dis



voice "Risa_1345"
r "「……と言いながら、その手に持っているのは何かしら？」"
voice "Miya_0857"
m "「早朝ハプニングは見れなかったけど、その代わりに璃紗のおぱんつをお土産に……」"


show char tri09f2 at right as r
with dis



voice "Risa_1346"
r "「そんなお土産、絶対にだめ！」"


#allClear:
hide char tmi01f2 at left
hide char tri09f2 at right as r
#lastBG:
#scene bg bg02a
with dis


"前もって美夜が来るのがわかってれば、隠しておくんだけど。"
"今日は突然だったから、油断していたわ。"
"美夜の手には、洗濯かごに入れられていた私の下着が、ちゃっかりと握られていた。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**安曇家ダイニング・昼
scene bg bg02a
with Dis



#mes on
#system on


"そして、お昼過ぎ。"
"約束通り、ママがやってきた。"
"美夜のくれたお菓子を出して、お茶を入れる。"
"おとり寄せマニアの美夜が選んだだけあって、お菓子はとても美味しかった。"
voice "Mobrie_0033"
rr "「とっても美味しかったわ～、美夜さんにお礼、ちゃんと言っておいてね」"


show char tri01f2
with dis



voice "Risa_1347"
r "「ええ、わかったわ」"


#※EV033
#allClear:
hide char tri01f2
#lastBG:
#scene bg bg02a
scene bg EV33
with Dis



voice "Mobrie_0034"
rr "「さてと……今日来たのは他でもないわ。璃紗にね、大事な話があるのよ」"
voice "Risa_1348"
r "「………………」"
"珍しい、ママの真剣な顔。"
"私は自然と、姿勢を正していた。"
voice "Mobrie_0035"
rr "「ママのパートナーの雪乃なんだけど……今度ね、ヨーロッパで起業することになったのよ」"
voice "Risa_1349"
r "「ヨーロッパ……なんか、すごいなぁ」"
"ミカ女のＯＧって麗奈先生を筆頭に、海外でもバリバリに働いている人が多いのね。"
"なんだかすごく、憧れてしまうわ。"
voice "Risa_1350"
r "「あっ……でも、雪乃さんがヨーロッパに行ってしまうってことは……」"
"ママは……どうするのかしら？"
voice "Mobrie_0036"
rr "「私ね……彼女に、着いてきて欲しいって言われたの」"
voice "Risa_1351"
r "「……っ！！」"
voice "Mobrie_0037"
rr "「仕事のスタッフとして、そしてもちろん生涯のパートナーとしても私が必要なんですって」"
voice "Risa_1352"
r "「それって、ほぼプロポーズじゃない？」"
voice "Mobrie_0038"
rr "「そう……なるわね」"
"恥ずかしそうに、ママは紅茶を一口飲む。"
"なんだかこれ、とても他人事とは思えない話だわ。"
voice "Risa_1353"
r "（ママの事だから当然、他人事ではないけれど……私と美夜にも近いかも）"
voice "Risa_1354"
r "「それで……ママは、どうするの？」"
voice "Mobrie_0039"
rr "「私は……もちろん、彼女に着いていくつもりよ」"
"私を見つめるその瞳に、もう迷いはなかった。"
"きっとママの中では、最初から決まっていたことで。"
"ううん……相当、悩んでいたのかも。"
"だからここ最近の様子が、おかしかったのね。"
voice "Risa_1355"
r "「ママ……正直、寂しいわ」"
voice "Mobrie_0040"
rr "「璃紗……」"
"せっかく、ママと仲直りもできて。"
"また新たな母娘関係が、結ばれてきたばかりなのに……でも。"
voice "Risa_1356"
r "「いいよ、ママ。ママの幸せの為だもの。これくらい我慢できるわ」"
voice "Mobrie_0041"
rr "「璃紗……ありがとう、あなたのことだけが、気がかりだったのよ」"
voice "Risa_1357"
r "「私は平気よ。こう見えても、ママよりずっとしっかりしているつもりだから」"
voice "Mobrie_0042"
rr "「うぅっ……ママ、そんなに頼りないかしら？」"
voice "Risa_1358"
r "「生活面においては、ね」"
voice "Mobrie_0043"
rr "「それを言われると、耳が痛いわね」"
voice "Risa_1359"
r "「ふふふっ、でも仕事の面では、すごく尊敬しているわ」"
voice "Mobrie_0044"
rr "「璃紗……」"
"一緒に暮らしていた頃、どんなに忙しくても、ママは仕事に手を抜くことはなかった。"
"だから多少、それ以外でだらしないところがあっても、私は仕方ないわね……と、許せていたんだわ。"
"少し前のことなのに、なんだか懐かしくなってしまう。"
"もう私とママが一緒に暮らすことは、ないのかもしれないわ……"
voice "Risa_1360"
r "「じゃあいよいよ、ママは恋人と一緒に暮らすことになるのね」"
voice "Mobrie_0045"
rr "「ええ、そうなりそうよ……ふふふっ」"
"なんだか、照れるママ。"
"でもすごく、幸せの真っ只中って感じが伝わってくる。"
"そんなママを、私は思いっきり祝福したくなった。"
voice "Risa_1361"
r "「ね、ママ……今度こそ絶対、幸せになってよね」"


#※EV033P1
scene bg EV33p1
with Dis



voice "Mobrie_0046"
rr "「璃紗、あなた……」"
voice "Risa_1362"
r "「今度こそ……きっと、ね」"
"私はママの幸せな未来を祈るように、その手をギュッと握りしめた。"
"ママは嬉しそうに微笑んで、私の手を握り返してくれる。"
voice "Mobrie_0047"
rr "「璃紗の為にも、幸せになるわ……本当にありがとう、璃紗」"
voice "Risa_1363"
r "「ママ……ぅっ、うぅっ……」"
"涙がにじみそうになるのをグッとこらえて、私はニッコリと微笑む。"
"だってママが、幸せになろうとしているんだもの。"
"笑顔で……最高の笑顔で、お祝いしてあげたいもの。"


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
jump S062



