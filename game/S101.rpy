#「紗良……もう我慢できない」

label S101:
$ save_name = "◇紗良……もう我慢できない"


#**楓の部屋・昼
scene bg bg12c
with Dis



#mes on
#system on


#♂MP21
play music "sound/BGM21.ogg"


"毎日毎日、紗良のＣＭのお芝居の練習に、私は付き合った。"
"そしていつしか、紗良の演じる『新キャラ』に、本気で惹かれてしまっていた……"


show char tka05f2
with dis



voice "Kaede_0782"
k "「ああ……演技とは言え、そのツンとデレのバランスの良さ、そして恥じらい加減が絶妙なのよね、もう……」"
"ＣＭの練習とはいえ、愛しい人に魅力的な愛の告白をされ続けて。"
"この私でも、たまった欲求が体を熱くして、興奮はＭＡＸ状態だった。"
"もう、今日あたり危ないわ……我慢できない……かも……{image=image/exch001.png}"
voice "Kaede_0783"
k "「はぁ……はぁ、はぁ……紗良」"


show char tka05f2 at left
show char tsa08s2 at right as r
with dis



voice "Sara_0781"
sr "「もぉ……だから勘違いしないで、誰も好きだなんて……あっ、でもでも、嫌いとも言ってないわ！　ど、どちらかと言えば……す……」"
voice "Kaede_0784"
k "「……ダメ………………もう、ダメみたい……」"


show char tsa04s2 at right as r
with dis



voice "Sara_0782"
sr "「好き、かも…………って、か、楓ちゃん！？　なんかヘンだよ、汗びっしょりだし、熱があるみたいだよっ！？」"
voice "Kaede_0785"
k "「ぁぁ、ゴメンね……紗良……稽古中に悪いけど、もう私……あぁん、我慢できそうにないわ{image=image/exch001.png}{image=image/exch001.png}」"
voice "Sara_0783"
sr "「我慢できないって、一体何が………………ひゃっ！？　あああぁぁん！」"


#allClear:
hide char tka05f2 at left
hide char tsa04s2 at right as r
#lastBG:
#scene bg bg12c
with dis


"私は欲望に突き動かされるままに、紗良を押し倒してしまった……{image=image/exch001.png}"

"以下内容可能会导致部分人的不适，是否跳过？"
menu:
 "是":
  jump S102
 "否":
  jump hscene_sara3

label hscene_sara3:


#※EV063
scene bg EV63
with Dis


#if m==1
play music "sound/BGM21.ogg"
#mes on
#system on
#endif


voice "Sara_0784"
sr "「あああぁぁん、楓ちゃぁん……んふ、ちゅく、んぷっ……ぁん、すごいキス……あはぁ」"
voice "Kaede_0786"
k "「ちゅ、ちゅぱ、じゅる……ん、んん、ちゅる……紗良、さらぁ……あふぅん{image=image/exch001.png}」"
"なんだろう、止まらない、止められない、自分を抑えられない。"
"いつもと違う紗良、ツンデレの紗良、愛情に素直じゃない紗良。"
"それが演技だとわかっていても、その『新しい紗良』は、私を虜にして止まなかった。"
voice "Kaede_0787"
k "「ちゅ、んちゅる、れろ……んふぅ、好きよ、紗良……あぁん{image=image/exch001.png}」"
voice "Sara_0785"
sr "「ちゅぱ、あぁ、そんなに強く抱きしめられたら……んふ、それだけで感じちゃうよぉ{image=image/exch001.png}　楓ちゃん、なんで急にこんな……ん、ちゅるるっ」"
"何か言おうとしていた紗良の唇を、私は濃厚なキスで塞いでしまった。"
voice "Kaede_0788"
k "「好きよ、好き……ぁん、もうどうしうようもないくらい、紗良が好き……はぁ、ぁぁん、ちゅっ{image=image/exch001.png}」"
voice "Sara_0786"
sr "「んちゅ、楓ちゃぁん……あん、こんな強引な楓ちゃん、初めてかもぉ……一体、どうしちゃったの？」"
voice "Kaede_0789"
k "「はぁ、はぁ……紗良が、紗良が悪いのよ、あんな演技するから、見ている私を虜にしちゃうから……もぉ、可愛いすぎなのよぉ{image=image/exch001.png}」"
voice "Sara_0787"
sr "「そんなに、良かったんだ……んふふっ、じゃ、じゃあ……んっ{image=image/exch001.png}」"
"私に抱きしめられ、されるがままだった紗良。"
"そんな紗良が突然、私の体を押し退けようとした。"
voice "Sara_0788"
sr "「か、楓ちゃん、強引すぎるのはダメよ、私たち、まだそんな……ぁん、ダメぇぇ{image=image/exch001.png}」"
voice "Kaede_0790"
k "「はぁ、はぁ……紗良、あなた……ひょっとして、イヤ……なの？」"
voice "Sara_0789"
sr "「ち、違うわ……誰もイヤだなんて、言ってないでしょ……ばかぁ{image=image/exch001.png}」"
voice "Kaede_0791"
k "「紗良……アナタ……」"
"この状況で、演技を再開したっていうの！？"
"紗良……恐ろしい子。"
"でもそんな紗良の演技は、ますます私を虜にしていった……"
voice "Kaede_0792"
k "「紗良ぁ……可愛いわ、本当に可愛い……好きよ、あなたが好き、ちゅっ……もっと愛してあげるわ」"
voice "Sara_0790"
sr "「もう、強引なんだから……ぁん、でもイヤじゃない、んちゅ、キス……感じる、アナタの強引なキス、ゾクゾクするわ……ぁん{image=image/exch001.png}」"


#※EV063P1
scene bg EV63p1
with Dis



"あえぎ声が大きくなって、紗良の表情が蕩けてきた。"
voice "Sara_0791"
sr "「感じるぅ、感じちゃうの、でも……ぁん、でも恥ずかしい、やぁん、なんでこんなに感じちゃうのぉ………………くぅん、いいよぉ{image=image/exch001.png}」"
voice "Kaede_0793"
k "「さっ、紗良……恥じらいまでデレちゃって……はぁ、はぁ、もぉ、可愛い、可愛すぎて、めちゃくちゃにしたくなる……ちゅ{image=image/exch001.png}」"
"強く抱いて、紗良の唇に舌をすべり込ませて、絡ませて。"
"エッチなキスをしながら、私は紗良のおっぱいを、制服の上から揉みまわす。"
voice "Sara_0792"
sr "「ふぁあああぁっ、そんな、強引なの、だめぇ……わ、私たちまだ、そんな関係じゃ……ぁぁん{image=image/exch001.png}」"
voice "Kaede_0794"
k "「そんな関係でしょ……エッチに愛し合う、ラブラブな関係でしょう、紗良？」"
voice "Sara_0793"
sr "「違うわ、まだわたしたち、ただの腐れ縁で……やぁん、それなのに、胸揉まれて……ひぅん、服の上から乳首くりくりなんて、ダメなのぉ{image=image/exch001.png}」"
voice "Kaede_0795"
k "「ぁぁ、紗良……だったら今、恋人になりましょう……お互いの全てを晒しあう、恋人になりましょう……好きよ、ちゅっ{image=image/exch001.png}」"
"いつしか私も、紗良の演技に乗っかってしまった。"
"こういうの、イメージプレイっていうのかしら……なんかすごい、すごくゾクゾクしてきちゃう{image=image/exch001.png}"
voice "Sara_0794"
sr "「きゃぅ{image=image/exch001.png}　耳にキスなんて……ぁぁん、感じちゃう{image=image/exch001.png}　でも、まだ早いよ、エッチは……ぁん、エッチになんか溺れたら、わたし……私、アナタに溺れちゃう、好きになりすぎちゃうのぉぉっ{image=image/exch001.png}」"
voice "Kaede_0796"
k "「好きになって、溺れて……ううん、一緒に溺れましょう、紗良ぁ」"
voice "Sara_0795"
sr "「で、でもぉ……ぁんぁん、ダメよぉ、そんなのダメ、エッチになったらもう、元の関係に戻れないよぉ……あふ、あふぅゅん{image=image/exch001.png}」"
voice "Kaede_0797"
k "「戻る必要なんて、ないじゃない……溺れちゃえばいいのよ。私が紗良をもっともっと、とろとろにしてあげる、素直にしてあげる……すごくエッチな子にしてあげるんだから{image=image/exch001.png}」"
voice "Sara_0796"
sr "「やぁん、そんな、脱がしちゃだめぇ……ぁんああんっ{image=image/exch001.png}　恥ずかしいの、これ以上は……あああぁぁんっ{image=image/exch001.png}」"
"もはや演技かどうかわからなくなっていた、私と紗良のイメージプレイ。"
"でも確実に、私たちは興奮していた……私も紗良も、瞳は熱く潤んで、体も熱くほてっていて。"
"きっと……あそこももう、ぬるぬるになっているはず……"
voice "Sara_0797"
sr "「ああん{image=image/exch001.png}　脱がされちゃうぅ……やめてぇ、楓ちゃんのエッチぃ……あぁ、んふぅん」"
"演技かどうかわからない、微妙な抵抗を続ける紗良。"
"そんな紗良から、少し強引にショーツをずり降ろして。"
"更に邪魔な自分の服も半分脱ぎすて、私は紗良の丸くつややかなお尻に、思い切りキスをしていた。"


#※EV064
scene bg EV64
with Dis



voice "Sara_0798"
sr "「ひゃっ、ああん、そんな……ぁん、そこは、そんなところ、舐めちゃだめぇ……やぁん、ゾクゾクするぅ{image=image/exch001.png}」"
voice "Kaede_0798"
k "「あぁ、素敵……可愛いわ、とてもいいわ、紗良……ちゅる、ちゅ{image=image/exch001.png}　ぁぁ、こんなに濡らしちゃって……んふふっ{image=image/exch001.png}」"
"私は紗良の体を壁に押しつけて、手を突かせて。"
"グイッとお尻を突き出させるような、恥ずかしいポーズをさせた。"
"ショーツを脱がせた状態で、スカートをまくり上げているので秘密のスポットは無防備状態。"
"まさに私の好き放題、やり放題{image=image/exch001.png}"
"それでも紗良は、その白いお尻を左右に振って、微妙な抵抗を続けた。"
voice "Sara_0799"
sr "「やだぁ、そんな……だめ、そんなところ舐めないで、楓ちゃん、いやいやぁ……ぁん、ヘンな気持ちになるよぉ、あふぅ{image=image/exch001.png}」"
voice "Kaede_0799"
k "「ちゅる、れろ……{image=image/exch001.png}　んふふっ、変な気持ちになって当然よ。こんなエッチなお汁、可愛いおまんこいっぱいに溢れさせているんだもの……んちゅ{image=image/exch001.png}」"
"私はもっとねちっこく紗良を可愛がってあげたくて、柔らかな尻たぶをグイッと左右に開いて。"
"ますます晒された秘裂に、うっとりと唇を寄せた。"
voice "Kaede_0800"
k "「ちゅる、ちゅぱ………………じゅるるっ、甘くて美味しいわよ、紗良{image=image/exch001.png}　ちちゅ{image=image/exch001.png}　クリもぷっくりさせちゃって……ほぉら」"
voice "Sara_0800"
sr "「ひゃぅぅんっ{image=image/exch001.png}　やだやだぁ、そこは、そこだけはダメ、指で撫でたりしちゃ……きゃぅぅん{image=image/exch001.png}」"
voice "Kaede_0801"
k "「んふふっ、皮の上からでも、こんなに感じちゃうのね、紗良は……じゃあ、そっと剥いて……直接、指で撫でたら……{image=image/exch001.png}」"
voice "Sara_0801"
sr "「んあぁぁぁっ{image=image/exch001.png}{image=image/exch001.png}　それだめ、泣いちゃう、壊れちゃうぅぅ{image=image/exch001.png}　ぜったいおかしくなるよぉ、んぁぁっ{image=image/exch001.png}」"
voice "Kaede_0802"
k "「おかしくなっちゃえばいいのよ{image=image/exch001.png}　だったら今度は、吸ってあげるね……ちゅっ、はむ{image=image/exch001.png}　ちゅるる{image=image/exch001.png}」"


#※EV064P1
scene bg EV64p1
with Dis



voice "Sara_0802"
sr "「あひ、ひぅぅんっ、もぉ、あふ、もぉ……ふにゅぅぅ、泣いちゃうよぉ、気持ちいいんだもん、だめぇ……ぁふぅぅんっ{image=image/exch001.png}」"
"甘い声が更に甘くなって、紗良の抵抗が完全になくなった。"
"それどころかいつしか、紗良のお尻の方が、グッと私の顔に押しつけられていた。"
voice "Kaede_0803"
k "「ん{image=image/exch001.png}　んちゅ……さ、紗良……あなた……んむっ、くるしぃ」"
voice "Sara_0803"
sr "「ふぁぅん、もっとぉ……ぁん、もっと舐めて、ぺろぺろしてぇ{image=image/exch001.png}　クリも可愛がってぇ、楓ちゃん……ああん、お願いぃ{image=image/exch001.png}」"
voice "Kaede_0804"
k "「紗良ぁ……んぷっ、わかったわ、もっともっと、もっと可愛がってあげる……おまんこもクリも、とろとろにしてあげちゃう{image=image/exch001.png}　ちゅぅぅっ{image=image/exch001.png}」"
"淫らな紗良が本気で、私におねだりをして、甘えてくる。"
"そんな紗良の熱く潤んだおまんこを可愛がりながら、私はふと思ってしまった……"
voice "Kaede_0805"
k "（紗良……これってまだ、続きなのかしら……ツンな紗良が愛撫でとろけて、想い人に身も心も捧げる……そんなシチュのつもり？）"
voice "Kaede_0806"
k "（それとも私の愛撫に感じすぎて、演技どころじゃなくなって、いつものエッチな紗良に戻っちゃったの？）"
"どっちなのかは、不明だった……聞いてみたいけれど、今はそれどころじゃない。"
"完全にエッチなスイッチの入ってしまった紗良が、私の舌を求め、お尻ごとおまんこをギュウギュウ、押しつけてきたから。"
voice "Sara_0804"
sr "「くぅん{image=image/exch001.png}　楓ちゃぁん、もっとぉ……もっと舐めて、もっと紗良を可愛がってよぉ……あはぁぁん{image=image/exch001.png}」"
voice "Kaede_0807"
k "「ちゅる、ちゅ、あぁ、美味しい……ぁん、紗良のえっち、えっちな子……はぁ、はぁ……もぉ、んふゅ……ぁぁ、ぁぁんっ{image=image/exch001.png}」"
"こんな興奮、すごすぎ……愛撫している方の私も、すごくゾクゾクしてしまって。"
"そっと指を股間に忍ばせてみて、ビックリしてしまった。"
voice "Kaede_0808"
k "（やぁん、すごい……何もされていないのに、私……こんなにぬるぬる、熱く濡れちゃっているの……）"
"それを知って、ますます興奮は高まってしまって。"
"そのまま私の指は、自らの割れ目をなぞり始めてしまった。"


#※EV064P2
scene bg EV64p2
with Dis



voice "Kaede_0809"
k "「ぁぁ、やぁん……こんなに、ぬちゅぬちゅ……ふぅ、はぁ……ぁん、だめぇ……ぁぁ{image=image/exch001.png}」"
"ダメ……なんか興奮しすぎて、自分で自分を慰めてしまう。"
"紗良とのエッチ中に、こんな……今日の私、なんかおかしいよ……"
voice "Sara_0805"
sr "「ふぅん、あぁ、楓ちゃん……あっ、楓ちゃん、自分で……しちゃってるの？」"
voice "Kaede_0810"
k "「さ、紗良ぁ……ぁん、だってぇ、だって、熱くて……」"
voice "Kaede_0811"
k "「ツンデレな紗良を可愛がっていたら、どうしようもないくらい切なくなって……ぁぁん、指が止まらないのぉ{image=image/exch001.png}」"
voice "Sara_0806"
sr "「楓ちゃんのえっち{image=image/exch001.png}　でもダメ、紗良のおまんこも舐めて、紗良も最後まで、気持ちよくして欲しいのぉ{image=image/exch001.png}」"
voice "Kaede_0812"
k "「はぁ、ぁぁ……わかったわ、紗良……紗良も、イカせてあげる……ちゅっ、んちゅ、ちゅるっ{image=image/exch001.png}」"
voice "Sara_0807"
sr "「きゃふぅん{image=image/exch001.png}　またクリ、舐められてるぅ{image=image/exch001.png}　指も、楓ちゃんの指も、紗良の中をくちゅくちゅしてる、かき回してるぅぅ……ぁぁあん、すっごくいいよぉ{image=image/exch001.png}」"
voice "Kaede_0813"
k "「あぁ、んふぅ、紗良……ぁん、気持ち良くなってぇ……ぁぁっ{image=image/exch001.png}」"
"なんかこれ、めちゃくちゃヘンな……ううん、めちゃくちゃエッチな気分。"
"一方の手で、自分のおまんこを可愛がって。"
"そしてもう一方の手では、紗良の愛らしいおまんこを可愛がっているんだもの。"
"私一人で、二人を気持ち良くしちゃってる……本当に今日の私、すごくエッチかも……{image=image/exch001.png}"
"そんな淫らな事を考えていたら、ますますおまんこがうずいて、熱く濡れてしまった。"
"硬くなったクリトリスを弄って摘みながら、紗良のそれにも同じ愛撫をした。"
voice "Kaede_0814"
k "「あぁ、はぁん、いいよぉ……ぁん、イキそう、自分でしているのに、イッちゃいそう{image=image/exch001.png}　ちゅ……紗良は、紗良はどうなの？　イキそう？」"
voice "Sara_0808"
sr "「んぁ、んぁぁっ、イキそっ、すごいの、すごくイイよぉ……んはぁぁ、イキたいよぉ、楓ちゃんっ{image=image/exch001.png}」"
voice "Sara_0809"
sr "「好きなの、好き好き、だいすきぃ{image=image/exch001.png}　だからいこっ、一緒に、一緒にいこうよぉ………………あああぁぁんっ{image=image/exch001.png}」"


#※EV064P3
scene bg EV64p3
with Dis



voice "Kaede_0815"
k "「わた、私もよ、紗良っ、紗良が好き、愛しているわ……一緒にイキましょう、イクイクいくぅぅぅぅ…………んふぁああっ{image=image/exch001.png}{image=image/exch001.png}」"
voice "Sara_0810"
sr "「あふぅぅぅぅんっ{image=image/exch001.png}　楓ちゃん、紗良イクぅっ、いくいくいくぅ、いっちゃうぅうんっ{image=image/exch001.png}{image=image/exch001.png}」"
"ぴしゃぁっと、紗良の割れ目から大量の飛沫が飛び散った。"
"私がイッた直後、最後の気力を振り絞って、紗良のおまんこに激しくキスして、吸いついて、ヒダとキスでもするように唇を激しく絡ませて{image=image/exch001.png}"
voice "Sara_0811"
sr "「あぁ……はぁ、はぁ……楓ちゃん……あぁん、紗良……イッちゃったぁ{image=image/exch001.png}」"
voice "Kaede_0816"
k "「ふぅ、ふぁぁ……私も、自分でイッちゃった……エッチでゴメンね」"
"でもあまりに紗良が、今日の紗良が可愛かったんだから、しょうがない……よね？"
"キャラが違うだけで、こんなにエッチも違うなんて……なんだか、不思議。"


scene black
with dis


scene bg bg12c
with dis


show char tka01f2
with dis


voice "Kaede_0817"
k "「でも今日の紗良、いつもよりいっぱい濡れていたわね……そんなに、気持ちよかった？」"


show char tka01f2 at left
show char tsa05s2 at right as r
with dis


voice "Sara_0812"
sr "「………………」"


show char tka03f2 at left
with dis


voice "Kaede_0818"
k "「ん……紗良……？」"
voice "Sara_0813"
sr "「べ……別に、そんなに気持ちよく……なかった、わ」"


show char tka04f2 at left
with dis


voice "Kaede_0819"
k "「えぇぇっ！？」"
"う、ウソ……あんなに濡れていて、あんなに乱れて、あんなに求めてきたのに。"
"なのにどうして、紗良はそんなことを……？"


show char tka03f2 at left
with dis


voice "Kaede_0820"
k "「さ、紗良……本当に、よくなかったの？　全然、ダメだった？？」"


show char tsa03s2 at right as r
with dis


voice "Sara_0814"
sr "「だ、ダメじゃない、悪くは……なかったわ、ちょこっとだけ、気持ちよかったし……{image=image/exch001.png}」"


show char tka02f2 at left
with dis


voice "Kaede_0821"
k "「紗良………………ふっ、ふふふっ」"
"そっか……そうなのね、エッチの後でもまだ、紗良の演技は続いていたのね。"
"あれだけ感じて、濡れて、イッちゃったのに。"
"まだ、恋人との関係を認めない。"
"紗良は本当に、ツンデレキャラをマスターしたのね。"
voice "Kaede_0822"
k "「ふふっ……だーい好きよ、紗良……ん、ちゅっ{image=image/exch001.png}」"


show char tsa05s2 at right as r
with dis


voice "Sara_0815"
sr "「か、楓ちゃんなんか……す……好き、だぁい好きっ{image=image/exch001.png}{image=image/exch001.png}」"
"恥じらいながら微笑む紗良と、私は何度も甘いキスをかわしたのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with dis


#♂MS
stop music fadeout 1


#endscene
#setscene 15


#//END
jump S102



