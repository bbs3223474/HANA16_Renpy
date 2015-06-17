# 注：从S002开始出现两个立绘同时出现的场景，根据Ren'py官方文档的要求，
# 同一个show命令出现两次时，如果它们的Tag都一样，那么新一行的show将会覆盖旧的。
# 因此，在使用at left、at right时，需要在其中一个后面加上as命令，
# 将其中一个show命令赋予Tag，使其与另一个立绘区分开，这样才不会被游戏覆盖显示。
# 因此，可以看见代码中使用了show char tri08s2 at right as r这样的代码，
# 也就是说，通过as r，对char tri08s2这张立绘赋予了“r”这个Tag，另外Tag名称可随意。
# 执行时，show char tmi01s2 at left将之前的show char tri08s2覆盖，因为他们的Tag都是相同的（空白）。
# 如果同一个背景要换回一人或两人的，那么需要使用hide命令将原先被赋予了Tag的立绘先隐藏，
# 注意是所有赋予了Tag的立绘才需要hide，本来没有赋予Tag的不用，直接用下一个show命令覆盖，
# 然后再继续正常使用show命令，并根据实际情况添加Tag。
# 如果需要更换背景，那么直接使用scene命令即可清除屏幕上所有图像而无需hide。
# 如果两个立绘中需要单独替换其中一个人的立绘，那么只需要按照设定的Tag来使用show命令即可。

label S002:
$ save_name = "◇新１年生のベストカップル"

play music "sound/BGM17.ogg"
scene bg bg29a
show char tri08s2
voice "Risa_0023"
r "「美夜……いるんでしょう？　入るわよ」"
"結局、今日は教室で、美夜の姿を見かけることはほとんどなくて。"
"そのまま、放課後になってしまった。"
"昼間はいなかったくせに、授業が終った途端、アトリエに戻っているんだから。"
voice "Risa_0024"
r "「もぉ……絶対に、確信犯だわ」"
"私は相手の返事を待つ前に、ドアを開けた。"
"私と美夜だけが知っている、秘密のアトリエのドアを。"

show char tmi01s2 at left
show char tri08s2 at right as r
with dis
voice "Miya_0000"
m "「あら、いらっしゃい、璃紗。ちょうどお茶が入ったところよ」"
"私がここに来るのを待っていたかのように、部屋は紅茶の良い香りで包まれていた。"
"まぁ、わかっていたんだけど。"
voice "Risa_0025"
r "「美夜、お茶はありがたく頂くわ……でも、その前に」"
show char tmi02s2 at left
with dis
voice "Miya_0001"
m "「いつものお説教かしら、ふふふっ」"

show char tri07s2 at right as r
with dis
voice "Risa_0026"
r "「もう！　わかってるなら何回も言わせないで。今日も授業、サボったわね」"
show char tmi01s2 at left
with dis
voice "Miya_0002"
m "「そうね、サボったわ」"
show char tri08s2 at right as r
with dis
voice "Risa_0027"
r "「校内、どこを探してもいなかったじゃない。どこにいたのよ？」"
show char tmi08s2 at left
with dis
voice "Miya_0003"
m "「……貴女の後ろ、よ」"
show char tri04s2 at right as r
with dis
voice "Risa_0028"
r "「ひゃっ！　な、なんかその言い方、怖いんだけど……都市伝説のアレみたい」"
show char tmi01s2 at left
with dis
voice "Miya_0004"
m "「都市伝説のあれって……何かしら？」"
show char tri03s2 at right as r
with dis
voice "Risa_0029"
r "「ほら、あれよ。人形から電話がかかってくるヤツよ」"
voice "Risa_0030"
r "「今、あなたの家に向かっているの……今、玄関についたわ……って、だんだん近づいてくるのよ」"
voice "Risa_0031"
r "「そして、最後は………………」"
voice "Miya_0005"
m "「貴女の後ろ……？」"
voice "Risa_0032"
r "「そうよ……ねっ、怖いでしょう」"
voice "Miya_0006"
m "「璃紗、可愛いもの好きなくせに、そんな話が怖いの？　璃紗の部屋に行けば、背後にたくさんのぐったりベアがいるじゃない」"

show char tri01s2 at right as r
with dis
voice "Risa_0033"
r "「それはちょっと、例えが違うような……んっ、今日の紅茶、とっても美味しいわ」"
show char tmi02s2 at left
with dis
voice "Miya_0007"
m "「んふふっ、良かったわ……おかわりもどうぞ」"
show char tri02s2 at right as r
with dis
voice "Risa_0034"
r "「ありがとう……いい香り♪」"
"ティーポットから注がれる、紅茶を見ているとほっこりしてしまう。"
"放課後にお喋りをしながらのティータイムって、やっぱりいいわね。"
"今日一日の疲れが、吹き飛んでいくような……"

show char tri09s2 at right as r
with dis
voice "Risa_0035"
r "「って！　何をまったりしてるのよ私、今は放課後ティータイムじゃなくて、美夜のお説教タイムじゃない」"
show char tmi03s2 at left
with dis
voice "Miya_0008"
m "「イヤなタイムね」"
voice "Risa_0036"
r "「イヤでも、聞いてもらうわよ。このまま授業をサボり続けて夏休みに突入なんて、私は絶対に許さないからね」"
show char tmi01s2 at left
with dis
voice "Miya_0009"
m "「もう……まだ６月よ。夏休みだなんて、璃紗ったら気が早いのね」"
show char tri08s2 at right as r
with dis
voice "Risa_0037"
r "「だって美夜なら、十分にありえるわ」"
voice "Risa_0038"
r "「じめじめした気候の時は、気分が乗らないとか言ってサボり。からっとした陽気になれば、暑くて授業に出たくないってサボり……そうなりそうだもの」"
"そしてそのまま、夏休みになってしまう。"
"ああ、見えるわ……"
voice "Risa_0039"
r "「美夜のサボり道が、私にははっきりと見えるの」"

show char tmi01s2 at left
with dis
voice "Miya_0010"
m "「ふふふっ、璃紗ったら……わたくしのこと本当に良くわかっているのね」"
show char tri03s2 at right as r
with dis
voice "Risa_0040"
r "「……えっ？」"
"美夜の綺麗な顔が、スッと近づいてくる。"
voice "Miya_0011"
m "「さすが、わたくしの恋人ね……ちゅっ」"
show char tri04s2 at right as r
with dis
voice "Risa_0041"
r "「んっ！？　も、もぉ……美夜ったら……」"
"美夜の唇と私の唇が、いつものように重なり合う。"
show char tmi11s2 at left
show char tri11s2 at right as r
with dis
voice "Miya_0012"
m "「ふふふっ……璃紗、可愛い……ちゅるる"
voice "Risa_0042"
r "「んあっ……んちゅ……ちゅ」"
"美夜の甘い吐息を感じて、それだけで頭の中がふわっとする。"
"そして名残惜しそうに、唇が離れていく。"
show char tmi01s2 at left
show char tri05s2 at right as r
with dis
voice "Miya_0013"
m "「璃紗、授業をサボって悪かったわ……だから、これで許して」"
voice "Risa_0043"
r "「……んっ、もぉ……ズルいわよ……ちゅっ」"
"キスの余韻が残る私は、もっと美夜が欲しくて……顔を赤くさせたまま、自分からもキスをしたのだった。"

scene bg bg29a
show char tmi01s2
with fade
######################## 此处保留，之后需要将fade修改为1.0秒 ########################

voice "Miya_0014"
m "「璃紗、これ食べる？」"
show char tmi01s2 at left
show char tri01s2 at right as r
with dis
voice "Risa_0044"
r "「ええ、頂くわ。美味しそうなマフィンね、またお取り寄せスイーツ？」"
voice "Miya_0015"
m "「いいえ、これは玲緒さまに教えてもらったお店で買って来たのよ」"
voice "Risa_0045"
r "「玲緒さまに……」"
voice "Risa_0016"
r "「璃紗はキャラメルとチョコ、どっちがいいかしら？」"
voice "Risa_0046"
r "「………………」"

show char tmi03s2 at left
with dis
voice "Miya_0017"
m "「……璃紗？」"
voice "Risa_0047"
r "「……あっ、ごめんね。キャラメルを頂くわ」"
"いけない、ぼーっとしてしまったわ。"
show char tmi01s2 at left
with dis
voice "Miya_0018"
m "「んんっ、何を考えていたのかしら、璃紗？　そろそろブラのサイズをもうワンカップあげようか……」"
show char tri09s2 at right as r
with dis
voice "Risa_0048"
r "「そんなこと考えてません、もうっ」"
voice "Miya_0019"
m "「なんならわたくしが、自ら測ってあげてもいいわよ……この手で」"
voice "Risa_0049"
r "「だから、違うって」"
voice "Miya_0020"
m "「あら、残念……誤差１センチ以内で当ててあげるのに」"

show char tri08s2 at right as r
with dis
"確かに今のブラ、ちょっときついかなって思うこともあるけれど。"
voice "Miya_0021"
m "「じゃあ璃紗が、他に考えそうなことと言えば……」"
show char tri01s2 at right as r
with dis
voice "Risa_0050"
r "「だから勝手に、妄想しないで。私はただ……美夜の口からいきなり、玲緒さまの名前が出たのが嬉しくて」"
show char tmi03s2 at left
with dis
voice "Miya_0022"
m "「えっ……？」"
voice "Risa_0051"
r "「ベストカップルの人たちって、美夜の中ではもう普通に、友達として存在してるんだなって……」"
show char tmi01s2 at left
with dis
voice "Miya_0023"
m "「なんだ、そんなことだったの」"
show char tri02s2 at right as r
with dis
voice "Risa_0052"
r "「私にとっては、重要なのよ……美夜がみんなと仲良くしてくれるのは、私も嬉しいの」"
show char tmi02s2 at left 
with dis
voice "Miya_0024"
m "「ふふふっ、ありがとう、真面目なクラス委員長さん」"
show char tri03s2 at right as r
with dis
voice "Risa_0053"
r "「ま、また……そんな言い方して」"
"でもそれは、美夜の照れ隠しだってことが、私にはわかっていたから。"
"それ以上はもう、突っ込まないことにした。"
"クラスではまだ馴染んでいない美夜だけど、ベストカップルの方たちの中ではすっかり打ち解けているみたいだもの。"
"また去年みたいに、みんなで合宿とか出来たら……今度は美夜も、いっぱい楽しめるんだろうな……あっ！！"
"ベストカップルといえば、さっきの話題をふと思いだした。"

show char tri01s2 at right as r
with dis
voice "Risa_0054"
r "「あのね、美夜。美夜を探してる時、１年生の子たちが話してるのを聞いたんだけど……」"
show char tmi01s2 at left
with dis
voice "Miya_0025"
m "「何かしら？」"
voice "Risa_0055"
r "「今ね『新１年生ベストカップル』を選ばないかって、盛り上がってるみたいなのよ。なんか面白そうじゃない？」"
voice "Miya_0026"
m "「……わたくし、そういうのは興味ないわね」"
show char tri04s2 at right as r
with dis
voice "Risa_0056"
r "「ええっ、そうなの？　私たちの後輩が出来るかもしれないのよ」"
voice "Miya_0027"
m "「だから？」"
show char tri03s2 at right as r 
with dis
"だからって、言われても……"
"美夜は本当に興味がなさそうで、私の話には乗ってこなかった。"
show char tmi01s2 at left
with dis
voice "Miya_0028"
m "「わたくしが一番、興味があるのは……璃紗、貴女だけよ」"
show char tri01s2 at right as r
with dis
voice "Risa_0057"
r "「美夜……」"
voice "Miya_0029"
m "「それとも璃紗はわたくしより、新しい１年生が気になるのかしら？」"
voice "Risa_0058"
r "「そんなこと、ないわ……私だって、美夜が一番……」"
voice "Miya_0030"
m "「わたくしが、一番……なぁに？」"
"美夜が艶っぽい瞳で、私を見つめる。"
"心臓が、どくんどくんと五月蝿い。"
show char tri05s2 at right as r
with dis
voice "Risa_0059"
r "「あー、もうっ、わかるでしょう」"
"顔を真っ赤にさせる私に、美夜はくすくすと笑い続ける。"
show char tmi02s2 at left
with dis
voice "Miya_0031"
m "「ええ、わかるわ。わたくしのことが好きで好きでたまらないのよね、璃紗も」"
voice "Risa_0060"
r "「うううっ」"
"本当のことだけに、否定出来ない。"
voice "Miya_0032"
m "「璃紗の困ってる顔、とっても可愛いわ。その顔を堪能しながら、マフィンを頂きましょう」"
voice "Risa_0061"
r "「………………」"
"一番興味のあることは、私……美夜にそう言われて、それはそれで嬉しいけれど。"

show char tri01s2 at right as r
with dis
"『新１年生ベストカップル』のことはやっぱり、気になる……"
"昨年のように、自分たちがその話題の中心になるのは、もう懲り懲りだけど。"
"そうでないのなら、面白そうだもの……他人の恋愛事情とか、イベントごとって、気になるのが女の子なのよね。"
"一体、どんな人たちが選ばれるのかしら……"
voice "Risa_0062"
r "「可愛い子なのかしら、それとも上品な……」"
show char tmi03s2 at left
with dis
voice "Miya_0033"
m "「……璃紗、食べてる？」"
voice "Risa_0063"
r "「え、ええ、とても美味しいわ」"
"美味なマフィンを食べながらも、私はベストカップルの話がしたくて、うずうずしていた。"
"うううっ、誰かと話したい！！"
"こういう話が、好きな人といえば……"
voice "Risa_0064"
r "「……あっ、そうだわ！」"
voice "Miya_0034"
m "「どうしたの、璃紗？」"
voice "Risa_0065"
r "「ううん、なんでもないわ……美夜のチョコマフィンの方、味見したいわ。もらってもいいかしら？」"
show char tmi01s2 at left
with dis
voice "Miya_0035"
m "「ええ、たくさんあるからどうぞ」"
"美夜が差し出した袋の中からは、マフィンが何十個と顔を出していた。"
show char tri03s2 at right as r
with dis
voice "Risa_0066"
r "「ちょ、ちょっと、買いすぎじゃないかしら？」"
voice "Miya_0036"
m "「そうかしら？　１個１個が小さいから、これくらい普通だと思うわ」"
"決して小さいとはいえないマフィンが、瞬く間に美夜の口の中に消えていく。"
"美夜の超絶大食いっぷりを眺めながら、私はこっそりメールを打ち始めていた。"
"新１年ベストカップルの話、この人なら絶対、食いついてきそうだわ。"
"私と同じように、ベストカップルに選ばれた同級生――織田七海さんなら、きっと。"

hide bg bg29a
hide char tri03s2 as r
hide char tmi01s2
with fade
stop music fadeout 1
scene black
jump S003

# 第二章结束
