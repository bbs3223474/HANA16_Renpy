#「イベント委員会で待ってるわ\001」

label S079:
$ save_name = "◇イベント委員会で待ってるわ♪"


#**委員会室・昼
scene bg bg30a
with Dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


"環境整備委員会を引退したお姉さまは、イベント委員会に入り浸るようになった。"


show char tyu01s2
with dis



voice "Yuuna_0439"
y "「じゃあ、この件は、私がやっておきますね」"


show char tyu01s2 at left
show char tri02s2 at right as r
with dis



voice "Risa_1856"
r "「はい、宜しくお願いします。優菜さまがいてくれると百人力ですね。最近よくこちらにいらして下さるから、助かります」"


show char tyu02s2 at left
with dis



voice "Yuuna_0440"
y "「うふふ、そう言って貰えると嬉しいわ。環境整備委員会の方を引退したら、学園内ですることがぜーんぜんなくなっちゃって……」"
voice "Risa_1857"
r "「こちらとしては、とてもありがたいです」"


show char tyu01s2 at left
with dis



voice "Yuuna_0441"
y "「まあ、私が暇になった分、七海が忙しくなっちゃったんだけど……ねぇ？」"
"唐突に話を振られて、わたしはびくっとする。"


#allClear:
hide char tyu01s2 at left
hide char tri02s2 at right as r
#lastBG:
#scene bg bg30a
show char tna04s2
with dis



voice "Nanami0717"
n "「ひぇっ？　あ、そうですね」"


show char tyu03s2 at left
show char tna04s2 at right as r
with dis



voice "Yuuna_0442"
y "「本当、七海には負担を押し付けちゃって……」"


show char tna01s2 at right as r
with dis



voice "Nanami0718"
n "「いやっ、全然ですっ。イベント委員会と環境整備委員会の両立なんて、優菜さまもちゃんと、されていたことじゃないですか」"
voice "Yuuna_0443"
y "「そうなんだけど～、引退したから私が環境整備委員会で、七海と顔を合わすことはなくなったワケだし……」"
voice "Nanami0719"
n "「いやいや、でもこっちの委員会でも会えますしっ」"
voice "Yuuna_0444"
y "「でもね～～、七海は、とーっても忙しいから、こっちにもあまりいれないワケじゃない？」"


show char tna03s2 at right as r
with dis



voice "Nanami0720"
n "「そ、それは、そうですけれど……」"
voice "Yuuna_0445"
y "「七海も、私と一緒にいれなくて、寂しいでしょ～？」"


show char tna04s2 at right as r
with dis



voice "Nanami0721"
n "「なななっ、何言ってるんですかっ」"


show char tyu02s2 at left
with dis



voice "Yuuna_0446"
y "「強がらなくても良いのよ～、おー、よしよし{image=image/exch001.png}」"
"宥める様に頭を撫でてくれるお姉さまの手付きは、まるでトップブリーダーのそれで。"
"飼い犬のような扱いに、わたしはちょっとムッとする。"


show char tna08s2 at right as r
with dis



voice "Nanami0722"
n "「少しぐらい優菜さまと会えなくても、ぜーんぜん、これっぽっちも寂しくなんてありません！」"
voice "Yuuna_0447"
y "「もー、そんなこと言って……自分の気持ちに正直になりなさいな～」"
"わたしをギュッと抱きしめて、お姉さまはすりすりと頬ずりをしてくる。"


show char tna09s2 at right as r
with dis



voice "Nanami0723"
n "「ぎゃー、優菜さまっ！！　人前です！！　止めてください～～！！」"
voice "Yuuna_0448"
y "「私はぜ～んぜん、気にしてないわ～～♪」"
voice "Nanami0724"
n "「わたしと、みんなが気にします～～っ！！」"


#allClear:
hide char tyu02s2 at left
hide char tna09s2 at right as r
#lastBG:
#scene bg bg30a
show char tri03s2
with dis



voice "Risa_1858"
r "「いや……七海さん、今さらだから……ね？」"


show char tsa02s2 at left
show char tri03s2 at right as r
with dis



voice "Sara_0280"
sr "「そうだよ～、いっつも２人はラブラブで羨ましいな。ねっ、楓ちゃん？」"

hide char tsa02s2 at left
hide char tri03s2 at right as r
show char tka03s2 at sleft as l
show char tsa02s2
show char tri03s2 at sright as sr
with dis



voice "Kaede_0140"
k "「えっ……ええ、そうね……」"


#allClear:
hide char tka03s2 at sleft as l
hide char tsa02s2
hide char tri03s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tna03s2
with dis



voice "Nanami0725"
n "「うっ……うう……」"
"みんな、すごく寛容すぎない！？"
"いくらミカ女内で、公認のカップルだからといっても……"



#★★★選択肢　ここから



voice "Nanami0726"
n "「ゆ、優菜さま、人前では……」"


#++選択肢（３）
#１．『ベタベたしないでくださいっ！！』×
#２．『もう少し、控えてくださいっ』○
menu:
 "ベタベたしないでくださいっ！！":
  jump select15_1
 "もう少し、控えてくださいっ":
  jump select15_2



#１．『ベタベたしないでくださいっ！！』
label select15_1:


show char tna07s2
with dis



voice "Nanami0727"
n "「人前では、ベタベタしないで下さい。人の目が気になりますっ」"


show char tyu03s2 at left
show char tna07s2 at right as r
with dis



voice "Yuuna_0449"
y "「そ、そんな……ひどい、ひどすぎるわ。恋人の七海に近づくことも許されないの、私は……うぅっ」"


show char tna03s2 at right as r
with dis



voice "Nanami0728"
n "「だ、誰もそこまで言ってません……もう、困ったよぉ」"
"優菜お姉さま、かなりしょげてしまったわ……"


jump select15_end


#２．『もう少し、控えてくださいっ』
label select15_2:


voice "Nanami0729"
n "「もう少し、控えてください……お願いですから」"


show char tyu03s2 at left
show char tna03s2 at right as r
with dis



voice "Yuuna_0450"
y "「七海が、そこまで言うのなら……優しくそっと、触るくらいにしておくわね」"
voice "Nanami0730"
n "「そうですか、そのくらいなら………………ん？」"
"それってヘタをすると、抱きつかれるより困るかも。"
"感じちゃって、ヘンな声が出てしまったら……あわわっ。"


#set f1 f1+1


#++選択肢終了
#★★★選択肢　ここまで
label select15_end:


voice "Nanami0731"
n "「す、すみません……わたし、そろそろ行かないと」"
"時計を見ると、もうすぐ環境整備委員会の時刻が迫っていた。"
"委員長であるわたしが、委員会に遅刻なんて、もっての外だし。"


show char tyu01s2 at left
with dis



voice "Yuuna_0451"
y "「あら、そうなの……今日もうーんと、頑張ってきなさいな」"
"お姉さまに抱きしめられたままでは委員会には行けないから、やんわりとわたしを抱きしめていた体を押すと、あっさりお姉さまはわたしから離れた。"
"なんだかその態度に、ちょっと拍子抜けしてしまう。"


#allClear:
hide char tyu01s2 at left
hide char tna03s2 at right as r
#lastBG:
#scene bg bg30a
show char tna03s2
with dis



voice "Nanami0732"
n "「あ、はい……ごめんなさい。中途半端にしか手伝えなくて……」"


show char tri01s2 at left
show char tna03s2 at right as r
with dis



voice "Risa_1859"
r "「いいえ、むしろ忙しいのにこっちにも顔を出してくれて、ありがとう」"
voice "Nanami0733"
n "「全然です、あんまり役に立たなくて……」"
voice "Risa_1860"
r "「ううん、そんなことはないわよ、後は私たちにまかせて」"

hide char tri01s2 at left
hide char tna03s2 at right as r
show char tmi01s2 at sleft as l
show char tri01s2
show char tna03s2 at sright as sr
with dis



voice "Miya_1045"
m "「わたくしが１人で１０人分くらいの働きをするから、大丈夫よ」"


show char tri03s2
with dis



voice "Risa_1861"
r "「美夜はまた、そんなことを……」"


show char tna01s2 at sright as sr
with dis



voice "Nanami0734"
n "「１０人……それはすごいなぁ」"
"ここは美夜さんたちに任せるとして、わたしは急がなくちゃ。"


#allClear:
hide char tmi01s2 at sleft as l
hide char tri03s2
hide char tna01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0452"
y "「七海……私と離れるのは、寂しいでしょう？」"


show char tyu01s2 at left
show char tna03s2 at right as r
with dis



voice "Nanami0735"
n "「はっ？」"


show char tyu02s2 at left
with dis



voice "Yuuna_0453"
y "「私に会いたければ、早く環境整備委員会の仕事を終わらせて、こっちに来ることね{image=image/exch001.png}」"
voice "Nanami0736"
n "「なっ……なにを……」"
voice "Yuuna_0454"
y "「早く帰ってきたら、ぎゅーって抱きしめてあげる{image=image/exch001.png}」"


show char tna09s2 at right as r
with dis



voice "Nanami0737"
n "「けっ、結構ですっ！！」"
voice "Yuuna_0455"
y "「遠慮しなくてもいいのよ～」"
voice "Nanami0738"
n "「してません～！！」"
"お姉さまは、クスクス笑っている。"
"イジワルだ、これはぜーったい、イジワルで言っているのよ。"
"確かにお姉さまと離れるのは、とても寂しい……"
"だけど絶対、委員会に穴を開けるワケにはいかないし。"


show char tna01s2 at right as r
with dis



voice "Nanami0739"
n "「でも、こっちもお手伝いしたいから……なるべく早く帰ってきます～」"
voice "Yuuna_0456"
y "「ええ、いってらっしゃい{image=image/exch001.png}　急いで帰ってくるのよ～」"
"わたしは後ろ髪を引かれる思いで、イベント委員会の教室を後にしたのでした。"


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


show char tna03s2
with dis



voice "Nanami0740"
n "「……はぁ～、まったく……」"
"わたしは最近、よく思う。"
"お姉さま、キャラが変わりすぎじゃないかしら！？"
"そう思っているのは、絶対わたしだけではないはず。"


#**青空
#allClear:
hide char tna03s2
#lastBG:
#scene bg bg04a
scene bg bg42a
with dis



"そこでわたしは、イベント委員会のベストカップルのみんなに、最近の優菜お姉さまのキャラの変貌ぶりについて聞いてみることにした。"


#**委員会室・昼
scene bg bg30a
with Dis



"名付けて……『七海ちゃんの突撃インタビュー！！』"


show char tna01s2
with dis



voice "Nanami0741"
n "「そういうワケで、最近のお姉さまについてどう思いますか？」"


show char tna01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_1862"
r "「うーん……前より親しみやすくなったんじゃないかしら。とても話しかけやすくなったわ」"


show char tsa02s2 at left
show char tna01s2 at right as r
with dis



voice "Sara_0281"
sr "「そうそう、フランクな優菜さま、とってもステキー{image=image/exch001.png}」"


show char tka02s2 at left
with dis



voice "Kaede_0141"
k "「こういう優菜さんも、ありじゃないかしら」"


show char tna01s2 at left
show char tmi01s2 at right as r
with dis



voice "Miya_1046"
m "「欲望に忠実な生き方は、嫌いじゃないわ」"


show char tre01s2 at left
show char tna01s2 at right as r
with dis



voice "Reo_0210"
re "「松原優菜は、お菓子をよく持ってくるから……悪い気はしないわ」"


show char tma01s2 at left
with dis



voice "Mai_0278"
ma "「……玲緒らしい意見ね、そうね、わたしも今の優菜さんは好きよ」"


show char tna01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_1615"
rk "「後輩のワタシにも気さくに接して下さって……優しい先輩です」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0894"
s "「はい、いつも気軽に声を掛けてくださって、とてもありがたく思っております」"


#allClear:
hide char tna01s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg30a
show char tna03s2
with dis



voice "Nanami0742"
n "「むむ～……」"
"お姉さまの変貌ぶりについては、おおむね好評かも……むしろ、逆に受けているよう。"
"そりゃあお姉さまは、綺麗で、聡明で、優しくて……女性のありとあらゆる美しさが全部揃った様な人だから。"
"それに気軽さがプラスされると、ますます印象がよくなるのはわかるけれど……"
"よーく、わかるけれど！！"
voice "Nanami0743"
n "「まあ、これはこれで、いいんだけれど……」"
"いつか人前でも、キスされたり、おっぱい触られたり、押し倒されたりしないか、不安になってきたわ……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//七海の妄想

#**新校舎教室・昼
show char moyan as c
scene bg bg04a
with Dis



#mes on
#system on


show char tyu01s2
with dis



voice "Yuuna_0457"
y "「それでは皆さん……今日は皆さんに、私と七海の実践エッチをお見せします～」"


show char tyu01s2 at left
show char tna04s2 at right as r
with dis



voice "Nanami0744"
n "「ええええぇぇっ！？　いやぁ、いやですぅ、許して～」"


show char tyu02s2 at left
with dis



voice "Yuuna_0458"
y "「皆さんもじっくり見て、七海ちゃんの可愛さにほれぼれしてね。そぉれ、脱ぎ脱ぎ♪」"
voice "Nanami0745"
n "「だめだめぇ、みんな見てますし、脱がしちゃダメぇぇっ」"


show char tyu01s2 at left
show char tna04z at right as r
with dis



voice "Yuuna_0459"
y "「ほら、これが剥きたて七海ちゃんです。さらにこうやって、脚をグイッと開いて……」"
voice "Nanami0746"
n "「いやぁぁん！！」"


show char tyu02s2 at left
with dis



voice "Yuuna_0460"
y "「さらにさらに、可愛いおまんこのヒダを……こうやって、広げちゃうと……んふふっ{image=image/exch001.png}」"


show char tna05z at right as r
with dis



voice "Nanami0747"
n "「みんなお願い、見ないで、見ちゃやぁ、やだぁぁ、恥ずかしいよぉっ{image=image/exch001.png}」"


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


show char tna03s2
with dis



voice "Nanami0748"
n "「……なんてことは、絶対にイヤだわ、ぞぞぞっ」"
"最近のお姉さま、人前でも全然、躊躇しないし、みんなに自慢したがっているし。"
"これが調子に乗りすぎると、いつか今の妄想したようなプレイにまで、発展しちゃうかも。"
voice "Nanami0749"
n "「人前で、エッチ……みんなの前でのキスはもう、バカンスの時にしちゃったわよね」"
"恋人同士の伝説を実践したけど、あれは…まあ、みんなもしていたし。"
"今はまだみんなの前で、イチャイチャしてくるだけだけど。"
"その内、もっとエスカレートしていきそうな予感。"
voice "Nanami0750"
n "「ああ……すごく不安だなぁ～……」"
"お姉さま、ヘンな方向に暴走しなきゃいいんだけど……"
"以前までとは全然違った意味での心配が、わたしにどっと押し寄せてくるのであった。"


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
jump S080



