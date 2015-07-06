#「謎の……『黒髪会』」

label S110:
$ save_name = "◇謎の……『黒髪会』"


#※ここから玲緒視点で

#**委員会室・昼
scene bg bg30a
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


"この間まで、エリスの元ファンクラブだか何だかしらないけれど。"
"その子たちがワタシたちの周りをうろついて、ワタシを無理矢理、妙なお茶会に誘ったり。"
"麻衣や霧島雫を、エリスの後継者に誘ってみたり。"
"すっごく騒がしくて、すっごく迷惑だった。"
"だけどこの頃、やっと静かになってくれたのよね……"


show char tre07s2
with dis



voice "Reo_0496"
re "「当然よ、麻衣はワタシのなんだから、そんな変なファンクラブの子になんか麻衣を近づけさせるものですかっ！」"
"でも……あれからひとつだけ、気になることがある。"
"気になって気になって、ちょー気になっていることが。"


show char tre03s2
with dis



voice "Reo_0497"
re "「結局、あの『黒髪会』って……なに？」"
"あの子たちがその名前を出したとき、麻衣も雫も、明らかに動揺していた。"
"だけどそれが何なのかは結局、教えてもらえなかった。"
voice "Reo_0498"
re "「あのエリスも、知らないみたいだったわ……もぐもぐ」"
"考えごとしていると、おなかが空くわね。"
"カバンの中から、チョコレートを出して、次々と口に放り込む。"


show char tre02s2
with dis



voice "Reo_0499"
re "「美味しい～、ふふ、もっと食べよ～♪」"


show char tre02s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_1895"
r "「あ、あの……玲緒さま」"


show char tre03s2 at left
with dis



voice "Reo_0500"
re "「なに、安曇璃紗？　チョコだったらあげないわよ」"


show char tri01s2 at right as r
with dis



voice "Risa_1896"
r "「チョコはいいですから、こちらをお願いします」"
"文化祭で使う飾りが入った箱を、差し出される。"
voice "Reo_0501"
re "「もう、今からやるわよ。他の人はどーしたの？」"
voice "Risa_1897"
r "「まだ来ていないみたいです。今日はどうやら、別の委員の集まりが多いみたいで……」"
"久しぶりの、イベント実行委員会。"
"しかし周りを見てみると、ワタシと安曇璃紗以外、まだ誰も来ていなかった。"


show char tre01s2 at left
with dis



voice "Reo_0502"
re "「だったら、みんなが来てからやればいいんじゃないかしら。２人でやってもきっと、あまり進まないわ」"


show char tri03s2 at right as r
with dis



voice "Risa_1898"
r "「それは……」"
"麻衣だったらこういう時、きっとお説教するだろうけど。"
"後輩の安曇璃紗は、ワタシに何もいわなかった。"
"さすがワタシ、先輩ってことよね。"
"あっ、そうだわ……"
voice "Reo_0503"
re "「ねぇ、アンタ『黒髪会』って知ってる？」"
voice "Risa_1899"
r "「『黒髪会』？　何ですか、それって」"
voice "Reo_0504"
re "「ううん……知らないならいいわ」"
"なんとなく聞いてみたけれど、反応はなし。"
"そう簡単にはいかないのね。"
voice "Risa_1900"
r "「……あっ、でも……ちょっと、聞いたことあるような……」"


show char tre03s2 at left
with dis



voice "Reo_0505"
re "「えっ……？」"


show char tri01s2 at right as r
with dis



voice "Risa_1901"
r "「ちょっと、待ってくださいね」"
"安曇璃紗は携帯を取り出して、何かを打ち始めた。"
voice "Reo_0506"
re "「ねぇ、何かわかったの？」"
voice "Risa_1902"
r "「あっ……やっぱり」"
voice "Reo_0507"
re "「なになに？」"
voice "Risa_1903"
r "「ネットの掲示板などに、その名前がいくつかヒットしました……」"
voice "Risa_1904"
r "「内容についてはあまりよくわかりませんが、他にもミカ女コミュでかなり取り上げられてます」"


show char tre01s2 at left
with dis



voice "Reo_0508"
re "「ふーん……」"
"そういうの、ワタシは良くわからないけれど。"
"ネットで調べれば結構、出てくるものなのね。"


show char tre02s2 at left
with dis



voice "Reo_0509"
re "「わかったわ、ありがとう。後は自分で調べるわ♪」"


show char tri03s2 at right as r
with dis



voice "Risa_1905"
r "「えっ？　玲緒さま……どちらに？」"


show char tre01s2 at left
with dis



voice "Reo_0510"
re "「今日はワタシは、先に帰るわね」"


show char tri04s2 at right as r
with dis



voice "Risa_1906"
r "「えええっ！？」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#//SE：ダッシュ音
#♀SE049
play sound "sound/SE049.ogg"


"もうこんなところで、のんびりしている場合じゃないわ。"
"ワタシは麻衣が戻ってくる前に、教室を飛び出した。"

#//SE：メール送信音
#♀SE050
play sound "sound/SE050.ogg"


"そしてダッシュしながら、急いでメールを１通打ったのだった。"


#**カフェ・昼
scene bg bg36a
with Dis



#mes on
#system on


show char ter03f2
with dis



voice "Erisu_0195"
e "「玲緒……どうしたの、急に呼び出したりなんかして。ひょっとして、ワタシが恋しくなった？」"


show char tre01s2 at left
show char ter03f2 at right as r
with dis



voice "Reo_0511"
re "「違うわよ。『黒髪会』よ」"


show char ter01f2 at right as r
with dis



voice "Erisu_0196"
e "「あっ？　それって前に、シズクたちが話していたやつね」"
voice "Reo_0512"
re "「そう、その秘密を今、探っているところなのよ」"


show char ter03f2 at right as r
with dis



voice "Erisu_0197"
e "「玲緒が……１人で？」"
voice "Reo_0513"
re "「そうよ。それくらい、このワタシには簡単なことよ」"


show char ter01f2 at right as r
with dis



voice "Erisu_0198"
e "「すごいねー、で、なにがわかったの？」"


show char tre03s2 at left
with dis



voice "Reo_0514"
re "「な、なにがって」"
voice "Erisu_0199"
e "「『黒髪会』の秘密よ。実はワタシも、ちょっと気になっていたんだ」"
"期待を含んだ瞳で、エリスがワタシを見つめる。"
voice "Reo_0515"
re "「そ、それは……」"


show char ter02f2 at right as r
with dis



voice "Erisu_0200"
e "「うんうん」"
voice "Reo_0516"
re "「……ネットを見れば、色々と載ってるわ」"


show char ter03f2 at right as r
with dis



voice "Erisu_0201"
e "「ネット？」"
voice "Reo_0517"
re "「ミカ女こむー……だったかな、それとかにも書いてあるらしいわ」"
voice "Erisu_0202"
e "「こむーって？」"


show char tre08s2 at left
with dis



voice "Reo_0518"
re "「だからこむーよ、ミカ女の」"
"ひょっとして、安曇璃紗……ワタシにウソを教えたのかしら？"
"そのまま伝えているのに、エリスは首をかしげている。"


show char ter01f2 at right as r
with dis



voice "Erisu_0203"
e "「こむー、こむー？　ああ、なんだ、コミュのことね」"


show char tre03s2 at left
with dis



voice "Reo_0519"
re "「そ、そうよ……」"


show char ter02f2 at right as r
with dis



voice "Erisu_0204"
e "「ふふふっ、もしかして玲緒『ミカ女コミュ』がなんだか、知らないんじゃないの？」"
voice "Reo_0520"
re "「し、知ってるわよー」"


show char ter01f2 at right as r
with dis



voice "Erisu_0205"
e "「そう……まぁいいわ。じゃあ今、ワタシも見てみるね」"
"エリスは携帯をだして、さっきの安曇璃紗と同じく、何かを打ち込みはじめた。"


show char ter03f2 at right as r
with dis



voice "Erisu_0206"
e "「うーん……コミュ内ではかなり騒がれているけれど、その内容については、これだけじゃわからないね」"


show char tre08s2 at left
with dis



voice "Reo_0521"
re "「麻衣と、霧島雫が関係しているのは、間違いないはずよ」"
voice "Erisu_0207"
e "「そうだけど……個人情報をわざと載せないみたいで、２人の名前を検索しても出てこないのよ」"
"その後も、エリスがいろいろ調べてくれたけれど。"
"その活動内容や、メンバーについては、さっぱりわからなかった。"


show char tre03s2 at left
with dis



voice "Reo_0522"
re "「もうー、これだけ調べたのに、なんで何もわからないのかしら」"
voice "Erisu_0208"
e "「ワタシもシズクのことなら、何でも知りたいのに……ああ、お手上げだわ」"


#allClear:
hide char tre03s2 at left
hide char ter03f2 at right as r
#lastBG:
#scene bg bg36a
with dis


"ワタシもエリスも恋人として、あの２人のことを知りたいだけなのに。"
"さっぱり、その会のことはわからなかった。"


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


show char tma09s2
with dis



voice "Mai_0610"
ma "「ちょっとれーおー！　昨日、文化祭の準備サボったでしょう」"


show char tre04s2
with dis


voice "Reo_0523"
re "「ひゃあああ～！！」"
"麻衣が鬼のような形相で、ワタシを追いかけてくる。"
"もう、たった一日出なかったくらいで、そんなに怒らなくてもいいのに。"


show char tre09s2
with dis



voice "Reo_0524"
re "「他にもサボってる人、いたじゃないっ！」"


show char tma07s2
with dis



voice "Mai_0611"
ma "「みんな事情があって、これなかったのよ。あなたには用事、何もないじゃない」"


show char tre09s2
with dis



voice "Reo_0525"
re "「ワタシだって、あったわよ！」"


show char tma08s2
with dis



voice "Mai_0612"
ma "「一体、どんな用事よ？」"


#★★★選択肢　ここから


show char tre03s2
with dis



voice "Reo_0526"
re "「それは……えっと……」"
"どうしよう……ぅぅっ……"


#++選択肢（３）
#１．『ウソをつく』×
#２．『素直に言う』○
menu:
 "ウソをつく":
  jump select21_1
 "素直に言う":
  jump select21_2



#１．『ウソをつく』
label select21_1:


show char tre09s2
with dis



voice "Reo_0527"
re "「と、とにかく、とっても大事な用事があったのよっ！！」"


show char tma09s2
with dis



voice "Mai_0613"
ma "「その大事な用事って何よ、言ってごらん！」"


show char tre03s2
with dis



voice "Reo_0528"
re "「だ、だから……あっ、妹が急に入院したから、お見舞いに……」"


show char tma09s2
with dis



voice "Mai_0614"
ma "「玲緒、アンタ妹なんていないでしょうっ！！」"


show char tre03s2
with dis



voice "Reo_0529"
re "「くぅぅ、ううぅぅ……」"
"バレちゃった、あっさりと。"
"麻衣、かなり怒ってる……怖いし、もう白状しよう。"
voice "Reo_0530"
re "「お、お茶よ、エリスとお茶してたのよっ」"


show char tma03s2
with dis



voice "Mai_0615"
ma "「えっ……エリスさまと？」"


jump select21_end


#２．『素直に言う』
label select21_2:


voice "Reo_0531"
re "「え、エリスと……お茶してたのよ」"


show char tma03s2
with dis



voice "Mai_0616"
ma "「エリスさまと？」"


#set f1 f1+1


#++選択肢終了
#★★★選択肢　ここまで
label select21_end:


"ぴたっと、麻衣の動きが止まった。"
"はぁ、はぁ、普段は廊下走るなとかいうクセに、麻衣はこういう時はしつこく追いかけまわすんだから。"
voice "Mai_0617"
ma "「昨日、玲緒はエリスさまと会っていたの？」"


show char tma03s2 at left
show char tre01s2 at right as r
with dis



voice "Reo_0532"
re "「そうよ、エリスの方が誘ってきたんだから」"
"本当は誘ったのは、ワタシの方だけど。"
"ここはこうでも言わないと、麻衣がまた怒りそうだもの。"


show char tma01s2 at left
with dis



voice "Mai_0618"
ma "「なんだ、そうだったの……」"


show char tre03s2 at right as r
with dis



voice "Reo_0533"
re "「そ、そうよ……だから、ふかこうりょく、ってヤツよ」"
voice "Mai_0619"
ma "「玲緒が放課後に遊べる友達ができたのは、嬉しいけど……文化祭までは少し我慢しなさい。みんな、本当に大変なんだから」"
voice "Reo_0534"
re "「わかったわ、次回からは気をつけるわ」"
voice "Mai_0620"
ma "「そうね……文化祭が終わってヒマになったら、また４人で放課後にお茶会したりしたいわね～」"


show char tre02s2 at right as r
with dis



voice "Reo_0535"
re "「うんうん、お菓子いっぱい持って」"


show char tma02s2 at left
with dis



voice "Mai_0621"
ma "「ふふふっ、楽しそうね♪」"
"あれっ？　なんか麻衣の機嫌が良くなったみたい。"
"よし、この流れのまま……思いきって、聞いちゃおうかな。"


show char tre01s2 at right as r
with dis



voice "Reo_0536"
re "「あのね麻衣、前に話していた『黒髪会』のことだけど……」"


show char tma01s2 at left
with dis



voice "Mai_0622"
ma "「………………」"


show char tre03s2 at right as r
with dis



voice "Reo_0537"
re "「……麻衣？」"
voice "Mai_0623"
ma "「……あっ、わたし文化祭のポスター、校外にも貼っていいのか、許可もらわないといけないんだったわ」"


show char tre04s2 at right as r
with dis



voice "Reo_0538"
re "「ちょっと、麻衣っ！」"
voice "Mai_0624"
ma "「このままわたしは、職員室に行ってくるから。玲緒は先に教室、戻っていなさいね」"


show char tre09s2 at right as r
with dis



voice "Reo_0539"
re "「ま、麻衣～ってば、『黒髪会』のこと、教えて行きなさいよぉ」"


show char tma02s2 at left
with dis



voice "Mai_0625"
ma "「じゃあね～」"


hide char tma02s2 at left
with dis


"はぐらかされて、行ってしまった。"


#allClear:
hide char tre09s2 at right as r
#lastBG:
#scene bg bg05a
show char tre07s2
with dis



voice "Reo_0540a"
re "「うっ、悔しい……あそこまで隠されると、どうしても知りたくなってくるわっ！！」"
"でも、一体どうすれば……"


show char tre03s2
with dis



voice "Reo_0541"
re "「……ん？　あれは……」"


show char tmi01s2
with dis



voice "Miya_1071"
m "「………………」"
"ワタシの目の前を、綾瀬美夜が歩いている。"


show char tre03s2
with dis



voice "Reo_0542"
re "「綾瀬美夜……アイツも確か、黒髪よね」"
"だったらダメ元で、聞いてみるわ。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**中庭・昼
scene bg bg21a
with Dis



#mes on
#system on


"綾瀬美夜に声をかけてから、落ち着いて話ができる中庭の方に移動して。"
"そこで彼女に『黒髪会』について、尋ねてみた。"
"もちろんワタシがこれまでに、調べたことも込みで。"


show char tmi01s2
with dis



voice "Miya_1072"
m "「ふぅん……なるほど」"


show char tre01s2 at left
show char tmi01s2 at right as r
with dis



voice "Reo_0543"
re "「それで、何か知らない、綾瀬美夜？」"
voice "Miya_1073"
m "「知りません……残念ながら」"
"やっぱり、無駄か。"
"綾瀬美夜は２年生の間でも、仲間外れにされて……"
"『２年生会』だったかしら、その会にも入れてもらえてないくらいだもの。"
"いくら頭がよくて綺麗でも、つまはじきの可哀想な子なのよね。"
"どこの会にも入れてもらえないような子が『黒髪会』について、知っているはずないわよね。"
voice "Miya_1074"
m "「でも玲緒さま。わたくし『黒髪会』は知りませんが『３年生会』でしたら知ってます」"


show char tre03s2 at left
with dis



voice "Reo_0544"
re "「……えっ？　なにそれ、ワタシ聞いたことないわよ」"
"３年生会？　そんなのあるの！？"


show char tmi02s2 at right as r
with dis



voice "Miya_1075"
m "「玲緒さまは、知らないと思いますが……ふふふっ」"
"な、なに笑っているのよ。"
"どっちにしても、ワタシには関係のない会よね。"


show char tre08s2 at left
with dis



voice "Reo_0545"
re "「今、ワタシが聞きたいのは『黒髪会』よ！　それ以外は興味はないわ」"


show char tmi03s2 at right as r
with dis



voice "Miya_1076b"
m "「それはさっきも言ったけれど、知りませんわ……でも『黒髪』というのは、気になるわね」"
voice "Reo_0546"
re "「アンタも同じ、黒髪だから？」"


show char tmi01s2 at right as r
with dis



voice "Miya_1077"
m "「そう……わたくしはこのミカ女では、黒髪ナンバー１キャラのはずなのに」"


show char tre03s2 at left
with dis



voice "Reo_0547"
re "「んっ……？」"
voice "Miya_1078"
m "「そのわたくしが知らないなんて、こんなことがあっていいのかしら……」"


show char tre08s2 at left
with dis



voice "Reo_0548"
re "「黒髪ナンバー１が誰かなんて、この際関係ないわよ」"


show char tmi07s2 at right as r
with dis



voice "Miya_1079"
m "「ありますっ！！」"


show char tre04s2 at left
with dis



voice "Reo_0549"
re "「ひぃっ！！」"


show char tre03s2 at left
with dis



"びっ、ビックリした。"
"もう急に、大声あげるんだから……綾瀬美夜は。"


show char tmi05s2 at right as r
with dis



voice "Miya_1080"
m "「いつも、璃紗が言ってくれるんです……『美夜の黒髪は、世界で一番美しいわ』って」"
"うっとりと、綾瀬美夜は語りだした。"
"もうー、ワタシの聞きたいのは、そんなことじゃないのに……"


show char tre08s2 at left
with dis



voice "Reo_0550"
re "「もうもう、お惚気はいいわ。それより力を貸して」"


show char tmi03s2 at right as r
with dis



voice "Miya_1081"
m "「そんなに気になるんですか？　玲緒さま」"


show char tre03s2 at left
with dis



voice "Reo_0551"
re "「ええ……もし手伝ってくれたら、ほ、報酬……あげるわよ」"


show char tmi02s2 at right as r
with dis



voice "Miya_1082"
m "「まぁ……んふふっ{image=image/exch001.png}」"
"やっと綾瀬美夜は、ワタシの話を真剣に聞いてくれるようになった。"


show char tmi01s2 at right as r
with dis



voice "Miya_1083"
m "「ところで何をいただけるのでしょう、玲緒さま？」"


show char tre01s2 at left
with dis



voice "Reo_0552"
re "「報酬は、ワタシの最新お勧めスイーツ十傑よ」"
voice "Miya_1084"
m "「………………」"


show char tre03s2 at left
with dis



voice "Reo_0553"
re "「なによ、文句あるの」"
voice "Miya_1085"
m "「いえ、オッケーです。わたくしも全力で、調査に協力致します」"


show char tre01s2 at left
with dis



voice "Reo_0554"
re "「そう」"
"ふふふ。"
"なんだかんだで、綾瀬美夜もお菓子で簡単に言うこと聞くのね。"
"校内一の才女とか、言われてるみたいだけど。"
"ワタシの手にかかれば、とっても簡単だわ。"


show char tmi03s2 at right as r
with dis



voice "Miya_1086"
m "「お菓子はともかく……この校内でわたくしが知らないことがあるのは、気になるもの」"


show char tre03s2 at left
with dis



voice "Reo_0555"
re "「んっ？　今なんて……？」"


show char tmi01s2 at right as r
with dis



voice "Miya_1087"
m "「いいえ……ではごきげんよう、玲緒さま」"


show char tre01s2 at left
with dis



voice "Reo_0556"
re "「ご……ごきげんよう」"


hide char tmi01s2 at right as r
with dis


"こうしてワタシは、見事に綾瀬美夜を巻き込むことに成功した。"


show char tre08s2
with dis



voice "Reo_0557"
re "「もっと、頑張らなくちゃ……絶対に『黒髪会』の秘密は暴いてみせる……川村玲緒の名にかけて！　なぁんて」"
"こうなったら仲間よ、仲間をもっと増やすのよ。"
"みんなで力を合わせて、悪の野望を打ち砕くのよっ！！"


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
jump S111



