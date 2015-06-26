#「美夜のヨーロッパ行きは……？」

label S068:
$ save_name = "◇美夜のヨーロッパ行きは……？"


#**璃紗の部屋・夜
scene bg bg01c
with Dis



#mes on
#system on


#♂MP08
play music "sound/BGM08.ogg"


show char tmi01z
with dis



voice "Miya_0973"
m "「ね、璃紗。これもらっていいかしら」"
"事後、美夜が机の上に置いてあったペットボトルを手に取る。"


show char tmi01z at left
show char tri01z at right as r
with dis



voice "Risa_1696"
r "「冷たいのが冷蔵庫に入ってるから、それを取ってくるわよ」"
voice "Miya_0974"
m "「いいわ、これで十分よ……ゴクゴクッ」"
voice "Risa_1697"
r "「………………」"


show char tmi03z at left
with dis



voice "Miya_0975"
m "「ん……どうしたのかしら？　そんなに見つめて、璃紗も飲みたいの？」"
voice "Risa_1698"
r "「……飲ませて、美夜」"
voice "Miya_0976"
m "「えっ……？」"
voice "Risa_1699"
r "「私に飲ませて……くれるかしら？」"


show char tmi05z at left
with dis



voice "Miya_0977"
m "「な、なによ、その甘えモード……ぅぅっ」"
"めずらしく、美夜がうろたえている。"
voice "Risa_1700"
r "「ね、早くちょうだい、美夜」"
voice "Miya_0978"
m "「わかったわ、今、あげるから……ごくっ、んっ」"
"美夜はペットボトルの中身を口に含み、そのまま私に口移しで飲ませてくれた。"


show char tmi11z at left
show char tri11z at right as r
with dis



voice "Miya_0979"
m "「ちゅ……ん、んっ……」"
voice "Risa_1701"
r "「んぐ、ごくっ……ふう……んっ、ごくん」"
"すっかり温くなったアイスティーが、喉を通っていく。"


show char tmi01z at left
show char tri02z at right as r
with dis



voice "Risa_1702"
r "「ありがとう、美夜……ごちそうさま{image=image/exch001.png}」"

"以下内容可能会导致部分人的不适，是否跳过？"
menu:
 "是":
  jump risa4
 "否":
  jump hscene_risa4

label hscene_risa4:


#※EV039
#allClear:
hide char tmi01z at left
hide char tri02z at right as r
#lastBG:
#scene bg bg01c
scene bg EV39
with Dis

play music "sound/BGM08.ogg"
#mes on
#system on
#endif


"お礼を言ってから、ほてった美夜の体にそっと寄り添う。"
"あれだけ愛し合った後なのに、もっともっと美夜と触れていたい……そう思ってしまう。"
voice "Miya_0980"
m "「あの璃紗が、こんなに甘えるなんて……これは夢じゃないの？」"
voice "Risa_1703"
r "「ううん、夢じゃないわよ」"
voice "Miya_0981"
m "「それじゃ……まさか、罠！？」"
voice "Risa_1704"
r "「ちょっと美夜、どうしてそうなるのよぉ？」"
voice "Miya_0982"
m "「わたくしが完全に安心したところで、盛大なオチが待っているとか……」"
voice "Risa_1705"
r "「もう、違うわよ……疑り深いのね、美夜って」"
voice "Miya_0983"
m "「だって……今夜は幸せすぎて、かえって落ち着かないのよ」"
"どうやらそれは、美夜の本心らしく。"
"さっきから美夜は、そわそわしっぱなしだった。"
"しかも、心臓の音がどきんどきん鳴り止まなくて、それが私にも伝わってくる。"
voice "Miya_0984"
m "「い、今ならもしかして、あれとかこれとか……お願いしても、聞いてくれるのかもしれないわ」"
voice "Risa_1706"
r "「………………」"
"私はしっかり、美夜の体温を感じながら。"
"先日皆さんと話した後の決意について、どう美夜に伝えていこうか、考えをめぐらせていた。"
voice "Miya_0985"
m "「うーん、どんなことをしてもらおうかしら……いや待って、それよりも下着、璃紗の使用済み下着コレクションの充実を……」"
voice "Risa_1707"
r "「………………」"
"美夜が気持ちよく、ヨーロッパに旅立てるために。"
"しっかりと、自分の気持ちを伝えておかなくちゃ。"
voice "Miya_0986"
m "「あー、でもでも、コスプレプレイも捨てがたいわ……悩むわ、もう！」"
voice "Risa_1708"
r "「………………」"
"うん、だいたい頭の中でまとまって来たわ。"
"よし……言おう、ちゃんと言うわ。"
voice "Risa_1709"
r "「あのね、美夜……」"
voice "Miya_0987"
m "「やっぱり、コレクションだわっ！」"
voice "Risa_1710"
r "「？？？」"
"美夜はブツブツ言っていたと思ったら、いきなり意味不明の叫び声を上げた。"
voice "Risa_1711"
r "「美夜……さっきからヘンよ、どうかしたの？」"
voice "Miya_0988"
m "「あ、あの、璃紗……お願いが、あって……」"
voice "Risa_1712"
r "「お願い？　いいけど……私も美夜に話したいことがあるんだけど」"
voice "Miya_0989"
m "「それなら、璃紗からどうぞ。わたくしは後でいいから」"
voice "Risa_1713"
r "「う、うん……」"
"なんとなく、美夜の息づかいが荒い。"
"室内が暑いのかしら？"
"とにかく、言わなくちゃ……ちゃんと、気持ちを込めて。"
voice "Risa_1714"
r "「あのね、私……美夜を信じて、日本で待っているから……」"
voice "Miya_0990"
m "「えっ……？　日本って、ここだけど……」"


#※EV039P1
scene bg EV39p1
with Dis



voice "Risa_1715"
r "「私もしっかり成長して、いつかは美夜の力になるからね」"
voice "Miya_0991"
m "「？？？」"
voice "Risa_1716"
r "「もう……私、知っているのよ。美夜がヨーロッパに行っちゃうって事」"
voice "Miya_0992"
m "「それ……誰から聞いたの？」"
voice "Risa_1717"
r "「ええ、ママからよ」"
voice "Miya_0993"
m "「………………」"
"私の言葉を、否定しない美夜。"
"やっぱり、行くのね。"
"わかっていたけれど、本人の口から聞くと……少し辛い。"
"でもここで、泣いたりなんかしちゃだめよ。"
voice "Risa_1718"
r "「私は、日本に残るわ。ここで待っているわ」"
voice "Miya_0994"
m "「………………」"
voice "Risa_1719"
r "「そして今よりももっともっと勉学に励んで、美夜の立派なパートナーになったら、私もヨーロッパに行くから……」"
voice "Risa_1720"
r "「だから……それまで、待っていてね……」"
voice "Miya_0995"
m "「………………」"
"涙が溢れそうになるのをこらえながら、何とか言葉を紡ぐ。"
"本当は笑顔で、言いたかったけれど。"
"そこまで私は、強くはないみたい。"
voice "Miya_0996"
m "「あら……そう」"
voice "Risa_1721"
r "「ぐすっ………………えっ？」"
"私が考えに考え抜いた決意に対しての、美夜の反応は……淡白だった。"
"そして……"


#※EV039P2
scene bg EV39p2
with Dis



voice "Miya_0997"
m "「じゃあ来週の一週間、璃紗はお留守番ね」"
voice "Risa_1722"
r "「……へっ！？」"
"一週間っ！"
"今、一週間って言ったの！？"
voice "Miya_0998"
m "「そうよ、一週間よ？」"
voice "Risa_1723"
r "「い、一週間～～～～～っ！！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


#endscene
#setscene 8

label risa4:
#**璃紗の部屋・夜
scene bg bg01c
with Dis



#mes on
#system on


show char tri10z
with dis



voice "Risa_1724"
r "「ぅぅっ……ママの、バカ……」"


show char tmi02z at left
show char tri10z at right as r
with dis



voice "Miya_0999"
m "「……くすくすっ、少し落ち着いたかしら」"


show char tri03z at right as r
with dis



voice "Risa_1725"
r "「え、ええ……」"
"あの後、私はパニックに陥って。"
"もうなにがなんだかわからないのと恥ずかしいので、部屋から逃げだしてしまって。"
"家のトイレに１時間、籠城してしまった。"
"トイレの外で、美夜から一連の説明を受けて。"
"しぶしぶ、またこの部屋に戻ってきたわけだけど……"


show char tri05z at right as r
with dis



voice "Risa_1726"
r "「もう……やだ、恥ずかしすぎる」"


show char tmi03z at left
with dis



voice "Miya_1000"
m "「ちゃんと話さなかった、わたくしも悪かったけれど……忙しかったのよ」"


show char tri03z at right as r
with dis



voice "Risa_1727"
r "「それは、わかるけど……」"
"美夜はあの日の食事会で意気投合した雪乃さんと、会社の事業の一環で、合同でビジネスを始めることに決めたのだと話してくれた。"


show char tmi01z at left
with dis



voice "Miya_1001"
m "「その準備が忙しくて、学校にもなかなか顔をだせなかったのよ」"
voice "Miya_1002"
m "「そしてその最後の仕上げを、ヨーロッパですることになっただけよ」"
voice "Risa_1728"
r "「それが……一週間、ってことね」"
voice "Miya_1003"
m "「ええ、帰ってきたら今まで通り、委員会のお仕事も手伝うつもりよ」"


show char tri07z at right as r
with dis



voice "Risa_1729"
r "「ママったら、勝手に早合点して……勘違いしたのね、もう！」"


show char tmi02z at left
with dis



voice "Miya_1004"
m "「自分だって同じでしょう。さすが親子ね……ふふふっ」"


show char tri03z at right as r
with dis



voice "Risa_1730"
r "「はぁぁ～」"
"なんだか、ドッと疲れたわ。"
"ここ数日の私の悩みは一体、なんだったのかしら。"
"しかも……"
voice "Risa_1731"
r "「今回の美夜のヨーロッパの件、イベント委員のみんなにも相談しちゃったのよ」"
voice "Miya_1005"
m "「それはそれは……うふふっ、おもしろいことになっていたのね」"
voice "Risa_1732"
r "「うううっ、もう、話したらみんなに絶対、からかわれるわ」"


show char tmi01z at left
with dis



voice "Miya_1006"
m "「仕方ないわよ。それともこのまま、わたくしがずっとヨーロッパへ行ってしまう方がいいかしら？」"


show char tri09z at right as r
with dis



voice "Risa_1733"
r "「それはないわ、絶対っ！！」"


show char tmi02z at left
with dis



voice "Miya_1007"
m "「ふふふっ、でもそんなことを考えていたから、今夜の璃紗はあんなに激しかったのね……んふ、んふふっ{image=image/exch001.png}」"


show char tri05z at right as r
with dis



voice "Risa_1734"
r "「あっ……ぅぅ……」"
"さっきまでの自分と美夜の行為が、頭の中に次々と浮かんでくる。"
voice "Miya_1008b"
m "「今日の璃紗……とっても、萌え萌えだったわ{image=image/exch001.png}」"
voice "Risa_1735"
r "「もうっ、その話はいいから……忘れて、お願い」"
voice "Miya_1009"
m "「ずっと情熱的で、わたくしを求めて……エッチの後だって、あーんなに甘えてくるし{image=image/exch001.png}」"
voice "Risa_1736"
r "「だ、だから……それは……」"
"今ここに、美夜の記憶を消せる装置が売っていたら、言い値で買うのに。"
"どれだけ借金しても、絶対に買うのに！！"
voice "Miya_1010"
m "「ああ……またいつか、こんなプレイがしたいわ」"


show char tri09z at right as r
with dis



voice "Risa_1737"
r "「冗談いわないで！！　これが最初で最後よっ」"


show char tmi03z at left
with dis



voice "Miya_1011"
m "「あら、それは残念ね……でもこんな璃紗が見られるのなら、本当にヨーロッパに行っちゃおうかしら？」"


show char tri08z at right as r
with dis



voice "Risa_1738"
r "「もうっ……それより、聞かせてよ」"
voice "Miya_1012"
m "「えっ……何を？？」"


show char tri01z at right as r
with dis



voice "Risa_1739"
r "「だってさっき、美夜は私に何かお願いがあるって言っていたわよね？」"


show char tmi01z at left
with dis



voice "Miya_1013"
m "「あぁ、あれね……今日の璃紗ならなんでも聞いてくれそうだったから、脱ぎたての下着を５枚ほど……」"


show char tri07z at right as r
with dis



voice "Risa_1740"
r "「……死んでも、美夜にはあげないわっ！」"


show char tmi03z at left
with dis



voice "Miya_1014"
m "「もう、つまらないわね……ネタバレ前に、言っておけばよかったかしら」"
"ネタバレって……"
"なんだか今回の件、後々までからかいのネタにされてしまいそうだわ。"


show char tmi01z at left
with dis



voice "Miya_1015"
m "「まぁ、いいわ。さっきの情熱的な璃紗を忘れないうちに……」"


show char tri04z at right as r
with dis



voice "Risa_1741"
r "「へっ？　ちょちょっと……きゃぅん{image=image/exch001.png}」"


show char tmi02z at left
with dis



voice "Miya_1016"
m "「朝までどころか、一日中エッチしましょう♪」"


#**夜空
#allClear:
hide char tmi02z at left
hide char tri04z at right as r
#lastBG:
#scene bg bg01c
scene bg bg42c
with Dis



"そう言って美夜は、私を押し倒してしまって。"
"何度も何度も、愛されてしまったのでした……\001"


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

scene image "image/eyecatch02.png"
#wipe vshutter

pause

scene black
with Dis

#log on
#waitcancel enabled
#wipecancel enabled


#//END
jump S069



