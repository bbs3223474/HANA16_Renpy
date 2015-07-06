#「またあそびにきてね」

label S119:
$ save_name = "◇またあそびにきてね"


#※ここは麻衣視点で

#♂MP22
play music "sound/BGM22.ogg"


#**青空
scene bg bg42a
with Dis



#mes on
#system on


"この連休中、母の出産の為にずっと群馬に泊まり込みで、残していった弟や妹たちのことは気になっていたけれど。"
"家に戻って、２人と玲緒の様子を見ていたら、意外とうまくいっていたんだな……って、正直驚いた。"
"でも本当に、玲緒には感謝しないとね。"
"そして……玲緒と弟たちの、別れの朝が来た。"


#**麻衣の部屋・昼
scene bg bg14a
with Dis



show char tma03f2
with dis



voice "Mai_0836"
ma "「玲緒、ほら玲緒、起きなさいよ～」"


show char tma03f2 at left
show char tre03p at right as r
with dis



voice "Reo_0987"
re "「うぅーん、麻衣、もう少し……ふぁぁ～」"


show char tma08f2 at left
with dis



voice "Mai_0837"
ma "「だめよ、連休はおしまい。今日からまた、学校でしょう」"
"休みが終わったから、学校に行かなくてはならない。"
"いつもより少し早めに、玲緒を起こしたんだけど……なかなか起きてくれない。"
voice "Mai_0838"
ma "「ほーら、１回マンションに戻らないといけないんだから、もう起きなさいよ」"
voice "Reo_0988"
re "「やだ……今日は麻衣の家から、登校する～」"


show char tma09f2 at left
with dis



voice "Mai_0839"
ma "「そんなこと言って、制服もカバンも持ってきてないでしょ、玲緒っ！」"
"シーツを一気に持ち上げて、床の上に玲緒をゴロゴロと転がす。"
voice "Reo_0989"
re "「うにゅゅゅ～、麻衣ひどい～」"


show char tma08f2 at left
with dis



voice "Mai_0840"
ma "「ほら、荷物はまとめておいてあげたから、早く用意しなさい」"


show char tre03f2 at right as r
with dis



voice "Reo_0990"
re "「うううぅー、まだ眠いのにぃ……」"
"なんだかすごく辛そうに、起き上がる玲緒。"
"ずっと弟たちと一緒だったから、やっぱり疲れちゃったのかしら。"
voice "Reo_0991"
re "「あーあ……帰りたくないなぁ」"
"ぽつりと小さい声で、玲緒が何かを呟く。"


show char tma03f2 at left
with dis



voice "Mai_0841"
ma "「んっ……なぁに？」"


show char tre01f2 at right as r
with dis



voice "Reo_0992"
re "「ううん、なんでもない……今、準備するから」"
"ようやく玲緒は、のそのそと立ち上がって。"
"ここを出て行く準備を始めた。"


show char tre03f2 at right as r
with dis



voice "Reo_0993"
re "「……お別れ……なのね……」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**沢口家ダイニングキッチン・昼
scene bg bg15a
with Dis



#mes on
#system on


show char tma01f2
with dis



voice "Mai_0842"
ma "「ほら、玲緒」"


show char tma01f2 at left
show char tre03f2 at right as r
with dis



voice "Reo_0994"
re "「……う、うん……」"
"わたしは玄関先で、玲緒を見送る。"
"マンションまで送っていきたいけれど、これからウチの朝食やお弁当も作らないといけないので、そうも言ってられない。"
"すると……すやすや寝ていたはずの、弟と妹が姿を見せた。"
voice "Mobmaibrz0043"
mao "「ふぁぁぁ……麻衣おねえちゃん、おはよう」"
voice "Mobmaisis0037"
mai "「……おはよう、おねえちゃん」"
voice "Mai_0843"
ma "「あなたたち、もう起きちゃったの？　いつもなら、ギリギリまで寝ているのに……」"
"めずらしいこともあるものね。"
"寝坊が好きな弟たちがきちんと起きて来たのは、きっと……玲緒を見送ろうとしているのね。"


show char tre01f2 at right as r
with dis



voice "Reo_0995"
re "「………………」"
voice "Mobmaibrz0044"
mao "「………………」"
voice "Mobmaisis0038"
mai "「………………」"
"だけど３人とも、何故か無言のままだった。"
"一体、どうしたのかしら……？"
voice "Mai_0844"
ma "「玲緒、忘れ物はないわよね」"
voice "Reo_0996"
re "「ぅ……うん、ないわ……」"
"返事はしているけど、なんだか上の空な様子。"


show char tma03f2 at left
with dis



voice "Mai_0845"
ma "「玲緒ったら……まだ眠いの？」"


show char tre03f2 at right as r
with dis



voice "Reo_0997"
re "「ち、ちがうわよ、そうじゃなくて……」"
"玲緒はわたしの後ろにいる、弟たちの方をじっと見つめていた。"
voice "Mai_0846"
ma "「玲緒、本当にどうしちゃったの？」"


show char tre08f2 at right as r
with dis



voice "Reo_0998"
re "「別に……正直、子供たちの世話なんて、もうコリゴリだわ」"


show char tma04f2 at left
with dis



voice "Mai_0847"
ma "「えっ！？」"
"いきなり最後になって、急に文句を言い出すなんて……どうしちゃったのよ、玲緒は。"
"するとそれがきっかけとなって、ずっと黙っていた弟たちも喋り始めた。"
voice "Mobmaibrz0045"
mao "「う、うるさい、バカれおっ！！」"
voice "Mobmaisis0039"
mai "「ふんだ、れおちゃんのちーびっ！」"


show char tma03f2 at left
with dis



voice "Mai_0848"
ma "「ちょ、ちょっとあなたたち、朝からケンカなんて止めてよぉ」"
"だけど玲緒と弟たちは、ぐっと顔を突き合わせて、罵倒しあう。"


show char tre09f2 at right as r
with dis



voice "Reo_0999"
re "「う、うるさいわね、このガキっ」"
voice "Mobmaibrz0046"
mao "「ちーび！　ちーび！」"
voice "Mobmaisis0040"
mai "「ぺったんこ、れおちゃん」"
voice "Mai_0849"
ma "「ああ……もう、なんなのよぉ」"


#allClear:
hide char tma03f2 at left
hide char tre09f2 at right as r
#lastBG:
#scene bg bg15a
with dis


"なんか子供相手に、本気でケンカをしている玲緒。"
"最初は『子供相手に、本気で口ゲンカして……』と呆れていたけれど、いつもの玲緒とは何か違うことに気づいた。"
"悪口を言ってケンカしているのに、玲緒も、そして弟たちも、なんだか嬉しそうに見えたから。"
"そして、どっちも疲れるまで、しばらく言い合いを続けた後……"
voice "Mobmaibrz0047"
mao "「はぁ、はぁ……また、遊びにこいよな、れおっ！」"


show char tre01f2
with dis



voice "Reo_1000"
re "「『れおお姉ちゃん』って呼んでくれるなら、来てあげるわよ」"
voice "Mobmaibrz0048"
mao "「そんなの、やだよーだ！　でもぜったい、またこいよな！」"


stop music fadeout 1


#※EV076P1
#allClear:
hide char tre01f2
#lastBG:
#scene bg bg15a
scene bg EV76p1
with Dis


play music "sound/BGM14.ogg"


"そう言って、弟はがしっと玲緒にしがみついた。"
"その弟に続き、妹も玲緒に抱きつく。"
voice "Mobmaisis0041"
mai "「こんどはもっと、たくさん遊ぼうね……れおちゃん」"
voice "Reo_1001"
re "「た、たまになら、いいわ、よ……ううっ」"
voice "Mai_0850"
ma "「玲緒……」"
"玲緒の瞳はいつしか、涙で潤んでいた。"
"弟や妹との別れが寂しくて、思わず泣いてしまったみたい。"
voice "Mai_0851"
ma "「そっか……たった数日だったけど、いろんな意味で成長したのね……玲緒」"
"わたしもそんな玲緒の姿を見ているだけで、もらい泣きしてしまいそうになる。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・昼
scene bg bg08a
with Dis



#mes on
#system on


show char tma01f2
with dis



voice "Mai_0852"
ma "「ほら、あなたたちはもう部屋に戻って。ちゃんと顔、洗ってきなさい」"
"わたしは弟たちの背中を、家の中に押しやった。"


#※EV079
#allClear:
hide char tma01f2
#lastBG:
#scene bg bg08a
scene bg EV79
with Dis



voice "Reo_1002"
re "「あっ……」"
voice "Mobmaibrz0049"
mao "「じゃあね……れお……おねえちゃん」"
voice "Mobmaisis0042"
mai "「れおおねえちゃん……ぜったい、またあそんでね」"
"別れを惜しむように、ぶんぶん手を振る２人に、玲緒は悲しそうに背を向けていた。"
voice "Mai_0853"
ma "「玲緒、この数日間、本当にありがとうね」"


#※EV079P1
scene bg EV79p1
with Dis



voice "Reo_1003"
re "「ま、麻衣……うううっ……ぐすっ」"
"玲緒はついに、大粒の涙をぼろぼろと流した。"
voice "Mai_0854"
ma "「うんうん、玲緒、えらかったわよ」"
voice "Reo_1004"
re "「ま、まいぃ……ひっく、ぅぅぅ……ぐずっ、うぅぅっ……」"
"頭をなでなでしてあげながら、わたしは自分の涙をそっと拭った。"
"あんまりのんびりしていると、学校には遅刻してしまいそうだけど。"
"玲緒のこの涙が止まるまでは、こうやっていてあげたかった。"


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

scene image "image/eyecatch05.png"
with vs

pause 3

scene black
with Dis

#log on
$ _skipping = True
$ _dismiss_pause = True


#//END
jump S120



