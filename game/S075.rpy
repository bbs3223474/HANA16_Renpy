#「後継者、ついに決定！？」

label S075:
$ save_name = "◇後継者、ついに決定！？"


#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


#♂MP13
play music "sound/BGM13.ogg"


show char tna03s2
with dis



voice "Nanami0539"
n "「ああ……ついに、この日が来たのね……」"
"昨夜は、全然眠れなかった。"
"緊張しすぎて、もう既にお腹が痛くなってきたし。"
voice "Nanami0540"
n "「わたしって、こんなにプレッシャーに弱い性質だったかなぁ……」"
"ついに行われる『環境整備委員会』次期会長（後継者）信任投票。"
"委員のみんなの１票が、お姉さまの後継者を決める。"


show char tyu01s2 at left
show char tna03s2 at right as r
with dis



voice "Yuuna_0294"
y "「七海さん、ずいぶん緊張しているようね」"
voice "Nanami0541"
n "「おねえ……いえ、優菜さま、だ、だって～……こんなの緊張せずにはいられませんっ」"
voice "Yuuna_0295"
y "「そんなの、七海さんに決まっているわ」"
voice "Nanami0542"
n "「優菜さまはそう言って下さいますけど……結局は、投票ですから……」"
"ああ、不安で胸がドキドキする……！！"
"緊張で、内臓が口から出てしまいそう……って、ちょっと下品な例えだったかな。"
"でも、それくらいわたしは今、未だかつてない緊張感を味わっていた。"
voice "Yuuna_0296"
y "「ほら、七海さんも早く投票なさい」"
voice "Nanami0543"
n "「は、はい……」"
"投票箱に、自分の名前を書いた紙を投票した。"
voice "Yuuna_0297"
y "「これで、委員のみんなの全ての投票が終わりました。それでは開票します」"
voice "Nanami0544"
n "「い、いよいよだぁ～……」"


#allClear:
hide char tyu01s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"投票が締め切られ、投票箱が開けられる。"
"わたしは、緊張の面持ちでその瞬間を待った。"
"お姉さまが、無造作に畳まれた投票用紙を１枚、取って広げる。"


show char tyu01s2
with dis



voice "Yuuna_0298"
y "「織田七海さん」"


show char tna04s2
with dis



voice "Nanami0545"
n "「わ……！」"


#allClear:
hide char tna04s2
#lastBG:
#scene bg bg04a
with dis


"お姉さまの軽やかな声が教室中に響いたと同時に、黒板にわたしの名前が書かれる。"
"わたしに投票してくれている人がいる事実が、とても嬉しい。"
"嬉しいのだけれど、あと何票入るか……"
"そんなわたしの不安をよそに、お姉さまはどんどん開票していく。"


show char tyu01s2
with dis



voice "Yuuna_0299"
y "「織田七海さん……織田七海さん……」"


show char tna04s2
with dis



voice "Nanami0546"
n "「わ、わ……」"


#allClear:
hide char tna04s2
#lastBG:
#scene bg bg04a
with dis


"お姉さまが、わたしの名前を何度も何度も連呼する。"
"その度に、黒板に書かれたわたしの名前の下に、正の字が増えていく。"
"そして……"


show char tyu02s2
with dis



voice "Yuuna_0300"
y "「これで全ての開票が終わりました。次期委員長は満場一致で、２年の織田七海さんに決定しました」"

#//SE：拍手の音
#♀SE040
play sound "sound/SE040.ogg"


"教室中に、拍手と共に『わあっ』と歓声が上がった。"


show char tna01s2
with dis



voice "Nanami0547"
n "「よ、よかったぁ……」"


#allClear:
hide char tna01s2
#lastBG:
#scene bg bg04a
with dis


"わたしは、誰にも気付かれないよう、そっと安堵の息を吐いた。"
"今まで不安で不安でたまらなくて、妙な対抗心を燃やしたり、みんなに心配を掛けちゃったりしたけれど……"
"お姉さまの言う通り、まったくの杞憂だったんだわ。"


show char tyu01s2
with dis



voice "Yuuna_0301"
y "「それでは、早速新委員長に挨拶をお願いします……七海さん、前に出てきて」"


show char tna01s2
with dis



voice "Nanami0548"
n "「は、はい……」"
"わたしは、先ほどとは違う緊張感を持って、教壇の上に立った。"
"お姉さまを含め、みんなの視線がわたしに集中する。"
"前に立つと、委員ひとりひとりの顔がよく見える。"
"お姉さまはいつもずっと、ここからみんなを見守っていたのね。"
"それを引き継いで、今度からはわたしがいつも見る景色になるんだわ。"
"わたしはスッと息を吸って、大きく吐いてから、挨拶を始めた。"
voice "Nanami0549"
n "「皆さん、投票ありがとうございます。新委員長を務める事になりました、織田七海です」"
"わたしは、まず投票のお礼を口にした。"
voice "Nanami0550"
n "「優菜さまに比べたら、わたしは至らない点が多々あると思いますが、精一杯頑張りますので、どうぞ宜しくお願いします」"
"ここまで言い終わってから深々と礼をする。"
"すると、あちこちから宜しくお願いします、と言葉が返ってきた。"
voice "Nanami0551"
n "「皆さんにお願いがあります。まずは、これからも未熟なわたしに力を貸して下さい。それと……」"
"わたしは、沙雪さんに顔を向けた。"
voice "Nanami0552"
n "「わたしは、白河沙雪さんに、副委員長になって頂きたいと思います」"


show char tna01s2 at left
show char tsy03s2 at right as r
with dis



voice "Sayuki0890"
s "「七海さま……？　私でいいのでしょうか？」"
voice "Nanami0553"
n "「沙雪さんに、お願いしたいんです。どうでしょう、皆さん？」"
voice "mobJyosiA0096"
mobA "「いいと思いますわ。沙雪さんはとても優秀な方ですし」"
voice "mobJyosiB0057"
mobB "「きっと新委員長のサポートも、的確にこなして下さるでしょう」"
voice "mobJyosiC0030"
mobC "「素敵ですわ……黄金コンビの誕生ですね」"

#//SE：拍手の音
#♀SE041
play sound "sound/SE041.ogg"


"パチパチと、みんなが拍手をしてくれた。"
voice "Nanami0554"
n "「異論はないみたいですね……沙雪さん、どうぞ宜しくお願いします」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0891"
s "「……はい。私でよろしければ、一生懸命頑張らせて頂きます」"


#allClear:
hide char tna01s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"より、拍手の音が大きくなった。"
"壇上からお姉さまを見ると、優しく微笑んでくれていた。"
"お姉さま……わたし、貴方の大事にしてきたものを受け継いで、一生懸命頑張らせて頂きますから！"


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


"そして数日後……次の環境整備委員会。"
voice "mobJyosiA0097"
mobA "「新委員長、文化祭当日の視聴覚室の使用予定が、ダブルブッキングしておりましたわ」"


show char tna01s2
with dis



voice "Nanami0555"
n "「そうですか。その件については、わたしが直接、話に行ってきます」"
voice "mobJyosiB0058"
mobB "「備品購入をお願いしたいのですけれど」"
voice "Nanami0556"
n "「はい、購入予定物を書きだしておいてくれれば、わたしが先生方に交渉してきます」"


show char tna01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0892"
s "「七海さま、当日の役割分担とタイムスケジュールをリスト化しましたが、これで宜しいでしょうか」"


show char tna02s2 at left
with dis



voice "Nanami0557"
n "「沙雪さん、ありがとう……うん、よくできていると思います。これでいきましょう」"
voice "Sayuki0893"
s "「はい。では、コピーして皆さんに配布しますね」"
voice "Nanami0558"
n "「はい、宜しくお願いします」"


#allClear:
hide char tna02s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg04a
with dis


"わたしは不慣れながらも場を仕切って、みんなの報告を聞き、指示を出した。"
"沙雪さんはやっぱりとても優秀で、サポートがとても上手くて助かっている。"


show char tyu02s2
with dis



voice "Yuuna_0302"
y "「うふふ、これで環境整備委員会も安泰ね。七海ったら、すごく立派になっちゃって……」"
"お姉さまは、うんうんと満足げに、委員会でのわたし達のやりとりを眺めていたのでした。"


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


"それから更に、数日後。"
"今日は、引退式……あっという間に、この日が来てしまった。"
"お姉さまが今日で、環境整備委員会を引退する。"


show char tyu01s2
with dis



voice "Yuuna_0303"
y "「皆さん、今までどうもありがとうございました」"
voice "Yuuna_0304"
y "「頼もしい新委員長と副委員長、そして委員の皆さんがいて……私は安心して、この伝統のある環境整備委員会を引退することができます」"
voice "mobJyosiA0098"
mobA "「優菜さま、今までどうもありがとうございました……！」"
voice "mobJyosiB0059"
mobB "「寂しくなります……」"
voice "mobJyosiC0031"
mobC "「たまには、委員会にも遊びにいらしてくださいね」"
"委員の人たちの中には、お姉さまを始め、引退する先輩達のことを思って泣いている人たちもいる。"
voice "Yuuna_0305"
y "「もう……皆さんたら、永遠の別れじゃないんですから」"


#allClear:
hide char tyu01s2
#lastBG:
#scene bg bg04a
with dis


"そういうお姉さまも、今にも泣きそうな表情をしている。"
"その様子を見ていると、わたしもうるっときてしまった。"


#※EV043
scene bg EV43
with Dis



voice "Nanami0559"
n "「お疲れ様でした、優菜さま」"
"お姉さまに、委員会のみんなでお金を出し合って買った花束を手渡した。"
"みんなの感謝の想いがこもった、花束を。"
voice "Yuuna_0306"
y "「頑張ってね……七海さん」"
voice "Nanami0560"
n "「はいっ、優菜さまの守って来たこの委員会を、わたしもみんなで立派に守っていきます」"
voice "Yuuna_0307"
y "「ええ、また遊びにくるわね……うっ……」"
voice "Nanami0561"
n "「優菜さま……」"
"感極まったのか、お姉さまの目には、うっすら涙が滲んで。"
"やがてそれは、大きな雫となってぽろぽろと零れ落ちた。"
"それは何物にも代えがたい、美しくて綺麗な宝物のようだった。"
voice "Yuuna_0308"
y "「うっ、うぅ、委員会を宜しくねっ……」"
"珍しく嗚咽を漏らす、優菜お姉さま。"
"わたしもじわっと、熱い涙が溢れてしまった。"
voice "Nanami0562"
n "「はい、わかりました……はいっ！！」"
"わたしはお姉さまの手を取って、何度も何度も頷いた。"
"引退式のこの日、教室はみんなの涙と嗚咽で満ち溢れていたのでした……"


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
jump S076



