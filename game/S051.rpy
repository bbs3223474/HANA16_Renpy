#「これにて、一件落着？？」
# 本脚本含有18禁剧情……这是第三个了……
# 18X scene contains, now make that three......

label S051:
$ save_name = "◇これにて、一件落着？？"


#**六夏の部屋・昼
scene bg bg34a
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


show char trk03p
with dis



voice "Rikka_1437"
rk "「……ん……ぁぁ、ワタシ……いつの間に……ぅん」"
"寝ちゃっていた、みたい……"
"心地良いけだるさが、ワタシの全身を包み込んでいた。"
"本当に気持ちいい、ずっとこのままでいたい。"
"でも……なにか、大事なコトを……"
"窓からうっすらと見えたのは、白々と輝く朝日だった。"


show char trk09p
with dis



voice "Rikka_1438"
rk "「朝まで愛しますって、沙雪さんに約束したのに……どうして自分だけ寝ちゃったのよ、ワタシっ！」"
"寝ぼけていた目が、一気に開いた。"


#allClear:
hide char trk09p
#lastBG:
#scene bg bg34a
with dis


"沙雪さん、怒っているかも……ドキドキしながら、辺りを見まわす。"
"するとすぐ傍に、あたたかな温もりを感じた。"

"以下内容可能会导致部分人的不适，是否跳过？"
menu:
 "是":
  jump route_rikka2
 "否":
  jump hscene_rikka4

label hscene_rikka4:


#※EV025
scene bg EV25
with Dis


#if m==1
play music "sound/BGM17.ogg"
#mes on
#system on
#endif


voice "Sayuki0767"
s "「すぅ……くぅ、ん……すぅ、すぅ……」"
voice "Rikka_1439"
rk "「沙雪さん……沙雪さんも、寝ちゃってたんだね……ほっ」"
"沙雪さんは横向きになって、ワタシの体に寄り添って。"
"しっかりとしがみつくように、眠っていたのだった。"
voice "Rikka_1440"
rk "「良かった……こんなに近くにいてくれて」"
voice "Sayuki0768"
s "「すぅ、すぅ………………ん、くぅん……」"
voice "Rikka_1441"
rk "「もう、離れたくない……離れないで下さいね、沙雪さん……」"
"ずっとずっと、こうしていたい……この人の、傍にいたい。"
"そうする為に、ワタシは……何をすれば良いのだろう？"
voice "Rikka_1442"
rk "「ワタシ、どうすればいいですか……教えてよ、沙雪さん」"
voice "Sayuki0769"
s "「くぅ……くぅ、すぅ……すぅ……」"
voice "Rikka_1443"
rk "「……って、それは自分で考える事だよね」"
"ワタシは沙雪さんの寝顔を見つめながら、彼女の腰をそっと抱き寄せた。"
"愛しい彼女と、もっと密着したかったから……"
voice "Rikka_1444"
rk "「大好きです……愛してます、沙雪さん……」"
voice "Sayuki0770"
s "「ん、んんっ……ん、ぁ……」"


#※EV025P1
scene bg EV25p1
with Dis



voice "Rikka_1445"
rk "「あっ……起こしちゃったかな、沙雪さん……」"
voice "Sayuki0771"
s "「ん、んん………………くぅ、すぅ……くぅ……」"
voice "Rikka_1446"
rk "「……良かった、まだ起きなくて」"
voice "Sayuki0772"
s "「ぁ……り、六夏……さん……？」"
"ああ……ダメだった、やっぱり起こしちゃったみたい。"
"ついつい、抱き寄せたりしちゃったから……"


#※EV025P2
scene bg EV25p2
with Dis



voice "Rikka_1447"
rk "「起こしちゃって、ゴメンね……沙雪さん」"
voice "Sayuki0773"
s "「……ぃ、いえ……ふぁぁぁ～……ぁっ、恥ずかしいっ」"
"あくびをしてしまった口を、慌てて塞いで。"
"照れながら、沙雪さんは小さくニッコリした。"
"愛しくも愛らしい、その天使の笑み。"
"引き寄せられるように、ワタシは……"
voice "Rikka_1448"
rk "「沙雪さん………………ん{image=image/exch001.png}」"
voice "Sayuki0774"
s "「んちゅ、ちゅ……{image=image/exch001.png}　んぁ……六夏、さん……{image=image/exch001.png}」"
"沙雪さんの小さな唇に、そっとキスをしながら。"
"ワタシはもう、決意していた。"
voice "Rikka_1449"
rk "「ちゅぱ……ん……あの、沙雪さん……」"
voice "Sayuki0775"
s "「はい……六夏さん」"
"ワタシが何か言いたげなのを察してくれたのか、沙雪さんは黙ってこっちを見つめていた。"
"本当は……言いたくない、もっと彼女と一緒にいたい。"
"でもそれは、彼女の為にならない……そう、思えたから。"


#endscene
#setscene 4

label route_rikka2:
#**六夏の部屋・昼
scene bg bg34a
with Dis



show char trk08z
with dis



voice "Rikka_1450"
rk "「やっぱり、お家に帰った方が良いです……沙雪さん」"


show char trk08z at left
show char tsy03z at right as r
with dis



voice "Sayuki0776"
s "「六夏さん……やはり、私がこちらにいるのは、ご迷惑でしたでしょうか……」"
voice "Rikka_1451"
rk "「そんな、そんなコトないですっ！！　できるコトなら、ずっと……このままずっと、ワタシの傍にいて欲しいです」"
voice "Sayuki0777"
s "「でしたら、何故……」"


show char trk03z at left
with dis



voice "Rikka_1452"
rk "「それは……今のワタシには、それを望む資格がないから……です」"
voice "Sayuki0778"
s "「資格、って……それはもしかして、家柄とか、世間的地位とか……」"
voice "Rikka_1453"
rk "「それも、あります……」"
voice "Sayuki0779"
s "「そんな……私、六夏さんにそのようなもの、望んでおりません。六夏さんが、私を愛してくれていると言って下されば、そのお言葉だけで……」"


show char trk08z at left
with dis



voice "Rikka_1454"
rk "「いえ、ダメなんです。ワタシは絶対、沙雪さんには幸せになって欲しい、幸せにしたいんです……その為には絶対、沙雪さんのご家族の許しを貰いたいんです」"


show char tsy06z at right as r
with dis



voice "Sayuki0780"
s "「六夏……さん……ぅ、うぅっ……」"
"穏やかだった沙雪さんに、涙がにじんで。"
"その涙をハンカチで拭きながら、ワタシはあらためて、彼女に告げた。"
voice "Rikka_1455"
rk "「沙雪さん……今のワタシでは、とても沙雪さんを迎えになんて行けません。でも……」"


show char tsy03z at right as r
with dis



voice "Sayuki0781"
s "「でも……？」"
voice "Rikka_1456"
rk "「頑張ります、努力します、立派な人間になります。立派になって、沙雪さんを迎えに行きます、だから……ぅぅっ」"
"感極まったワタシは、そのまま沙雪さんを抱きしめてしまった。"


show char trk09z at left
with dis



voice "Rikka_1457"
rk "「だからそれまで、待っていて下さい……絶対、迎えに行きますから！！」"


show char tsy08z at right as r
with dis



voice "Sayuki0782"
s "「六夏……さん……」"
"強く、ひたすらに強く、沙雪さんを抱きしめる。"
"彼女は何も言わず、ただ黙って、ワタシに身を委ねてくれた。"


show char trk03z at left
with dis



voice "Rikka_1458"
rk "（ああ……どうしよう、とんでもないコト言っちゃったよ……沙雪さん、呆れているかも……）"
"急に不安がわいてくる、ヘタレな自分に戻りそうになる。"
"そんなワタシの腕の中で、沙雪さんが静かに言った。"
voice "Sayuki0783"
s "「分かりました……六夏さん。私、六夏さんの言葉を信じます」"


show char trk01z at left
with dis



voice "Rikka_1459"
rk "「沙雪……さん、じゃあ……」"
"家に帰ってくれる気になってくれたのかな？"
voice "Sayuki0784"
s "「六夏さんを待ちます、私……ですがその為にも、今回の結婚話は絶対、断らなくてはなりません」"


show char trk04z at left
with dis



voice "Rikka_1460"
rk "「えっ！？」"
"それって、つまり……"
voice "Sayuki0785"
s "「六夏さんには申し訳ありませんが、まだ私は家に帰るわけにはいきません」"


show char trk03z at left
with dis



voice "Rikka_1461"
rk "「沙雪さん……」"
voice "Sayuki0786"
s "「もし私がここにいて、六夏さんにご迷惑をおかけするのでしたら……すぐに退去します」"
voice "Rikka_1462"
rk "「い、いや、あの、その……全然迷惑ではないんですが、その……」"
"いて欲しい、ずっと一緒にいられたら、どんなに嬉しいコトか。"
"でもこのまま、沙雪さんに家出を続けさせるのは、ダメだと思う。"
voice "Rikka_1463"
rk "（どうしよう、ああどうしよう、ワタシはどうすれば……）"
"考えれば考えるほど、テンぱってきてしまう。"
"このままじゃワタシの頭、オーバーヒートしてしまいそう……"

#//SE：電話のコール音
#♀SE026
play sound "sound/SE026.ogg"


show char trk04z at left
with dis



voice "Rikka_1464"
rk "「ひっ！？　でで、電話……！？」"
"その聞き慣れた音は、ワタシの家電だった。"
"こんな時に、一体何だろう、電話なんて出ているヒマないのに！！"


show char tsy03z at right as r
with dis



voice "Sayuki0787"
s "「六夏さん……お電話ですよ。出られた方が良いのでは……」"


show char trk03z at left
with dis



voice "Rikka_1465"
rk "「そそ、そうですね、はい、出ます出ます」"
"沙雪さんの体を解放し、慌てて受話器を取って。"
voice "Rikka_1466"
rk "「はい、もしもし、篠崎ですが……」"
voice "MobSayuGM0000"
x "『そちら、篠崎六夏殿のお宅で間違いなかろうか？』"
voice "Rikka_1467"
rk "「は、はい……ワタシが、六夏ですが……」"
voice "MobSayuGM0001"
x "『ウチの沙雪が、そちらにお邪魔しているはずじゃ。代わって頂けまいか』"


show char trk04z at left
with dis



voice "Rikka_1468"
rk "「う、うちの沙雪って………………えぇぇっ！？」"
"じゃあこの、電話の向こう側の人って……沙雪さんの家族？"
voice "Rikka_1469"
rk "「ど、どうしよう……うぅっ、なんて言えばいいのかなぁ……あっ！？」"


show char tsy08z at right as r
with dis



voice "Sayuki0788"
s "「お電話、代わりました……沙雪です。おばあ様ですよね」"
voice "Mobsayugm0002"
ss "『ああ、そうじゃ。やはりそこにおったか、沙雪』"


show char tsy03z at right as r
with dis



voice "Sayuki0789"
s "「おばあ様……どうやって、ここを調べさせたのですか？」"
voice "Mobsayugm0003"
ss "『そんな事より、沙雪……すぐに帰って来るのじゃ』"


show char tsy07z at right as r
with dis



voice "Sayuki0790"
s "「嫌です。私、どこの誰とも分からぬ方と、結婚なんてしたくありません！！」"
voice "Rikka_1470"
rk "「沙雪……さん……」"
"あのおとなしい、いつもおっとりしている沙雪さんが、大きな声を上げていた。"
"ワタシとの約束を、守る為に……本気で、家族と……"


show char trk08z at left
with dis



voice "Rikka_1471"
rk "（ワタシも、何か言いたい……自分の、決意とか……）"
"でも今、沙雪さんとその家族の会話に、割って入るのは難しそうだった。"
voice "Mobsayugm0004"
ss "『いいから、戻ってきておくれ、沙雪っ！』"
voice "Sayuki0791"
s "「絶対に、嫌です……今回の婚約話がなくならない限り、私は……家には戻りません！！」"
voice "Mobsayugm0005"
ss "『あの婚約話は、もう無くなったんじゃ。だから……頼む、すぐ戻ってきておくれ、沙雪』"


show char tsy03z at right as r
with dis



voice "Sayuki0792"
s "「ですから、私は戻りませ………………えっ！？　おばあ様、今なんと……？」"
voice "Mobsayugm0006"
ss "『だから、今回の婚約話はなしじゃ。あんな輩だとは思わなかったわ』"
voice "Sayuki0793"
s "「それって一体、どういう事で──」"


show char trk03z at left
with dis



voice "Rikka_1472"
rk "「沙雪さん……ひょっとして……」"
"受話器の向こうの声はよく聞こえなくて、状況はあまりわからないけれど。"
"どうやら、予想外の事態が起こっているのは、間違いなかった。"


show char trk01z at left
with dis



voice "Rikka_1473"
rk "「これなら、なんかイケそうかも……頑張って、沙雪さんっ！」"

#//SE：携帯着信音
#♀SE007
play sound "sound/SE007.ogg"


show char trk04z at left
with dis



voice "Rikka_1474"
rk "「ひっ、こ、今度は携帯に……」"
"とりあえず携帯を取って、画面を見てみる。"
"そこには見覚えのない電話番号が、表示されていた。"


show char trk03z at left
with dis



voice "Rikka_1475"
rk "「出ない方が、いいのかな……いや、出よう」"
"一瞬の躊躇の後、ワタシは着信ボタンを押した。"
voice "Rikka_1476"
rk "「もしもし……どちらさまでしょうか？」"
voice "Mobsayuhh0000"
sh "『六夏さんね、はじめまして。私、白河沙雪の母です』"


show char trk04z at left
with dis



voice "Rikka_1477"
rk "「えっ、えぇっ、ええええええぇぇっ！？　沙雪さんの、お母さんっ！？」"


show char tsy04z at right as r
with dis



voice "Sayuki0794"
s "「っっ！！」"
"ワタシのその叫び声を聞いた瞬間、沙雪さんの手がビュン、と伸びてきて。"
"震えるワタシの手から、携帯を奪い去っていった。"
"右手に家電の子機、左手にワタシの携帯……電話二刀流になった沙雪さんが、携帯の方に話しかけた。"
voice "Sayuki0795"
s "「お母様？　本当にお母様なのですか！？」"
voice "Mobsayuhh0001"
sh "『ええ、そうよ』"


show char tsy03z at right as r
with dis



voice "Sayuki0796"
s "「そんな……一体どうやって、六夏さんの携帯番号を調べ──」"
voice "Mobsayuhh0002"
sh "『そんな事はどうでもいいのよ。もう一度、六夏さんに代わってもらえるかしら』"


show char tsy08z at right as r
with dis



voice "Sayuki0797"
s "「嫌です、六夏さんにおかしな事を言うのなら……私だって、怒りますよ」"
voice "Mobsayuhh0003"
sh "『そんな失礼な事はしません。大切な娘を一晩、預かって頂いたお礼を言いたいだけですよ』"
voice "Sayuki0798"
s "「お母様……それは私から、言っておきます。とにかく六夏さんは、私の家出とは関係ありませんから」"
voice "Mobsayuhh0004"
sh "『ええ、分かっているわ……私は全部、分かっていますから。沙雪、貴女と六夏さんの事も、ね』"


show char tsy04z at right as r
with dis



voice "Sayuki0799"
s "「どっ、どうしてそのような事を、お母様が知っているのですか！？」"
voice "Mobsayuhh0005"
sh "『沙雪、母親をなめてもらっては困るわ。毎日あれだけ、貴女から六夏さんの話を聞かされれば……ねぇ』"


show char tsy03z at right as r
with dis



voice "Sayuki0800"
s "「うぅっ、そんな……六夏さんとの事、全てお母様には筒抜けだったなんて……」"


show char trk05z at left
with dis



voice "Rikka_1478"
rk "「沙雪、さん……あぁ」"
"傍で聞いているワタシまで、恥ずかしくなってきた。"
"クラスのみんなや、ベストカップルの先輩たちに、ワタシとの恋愛進行を報告していた、沙雪さん。"
"どうやら家では、母親にも話していたみたいで……"
voice "Sayuki0801"
s "「お母様は、何もかもお見通しなんですね……」"
voice "Mobsayuhh0006"
sh "『ええ、その通りよ』"
voice "Mobsayugm0007"
ss "『沙雪……そういう事なら、ワシにも言ってくれれば良いものを』"
"向こうがどういう状況なのかは分からないが、今度は家電の方の、沙雪さんのおばあ様が話しかけてきた。"
voice "Mobsayugm0008"
ss "『沙雪に、想いを寄せる相手がいるなら、すぐにワシが会いに行ってやるのに……この目で厳しく、品定めしてやる為にも』"


show char trk04z at left
with dis



voice "Rikka_1479"
rk "「ひっ、ひぃぃっ！！」"
"少しドスの効いた低い声に、ワタシは震え上がった。"


show char trk03z at left
with dis



voice "Rikka_1480"
rk "（そう、だよ……すごい財閥家の娘である沙雪さんと付き合うには、このおばあ様やお母様とも、付き合わなくちゃならないんだ……ぅぅ、くぅぅ……）"
"恐ろしい、本当に恐ろしい。"
"こんな超平民なワタシが、そのような大物達と渡り合っていけるだろうか？"
"正直、まったく自信なんてなかった。"
voice "Mobsayugm0009"
ss "『とにかく、沙雪。これ以上、人様に迷惑をかけてはならんぞ』"
voice "Mobsayuhh0007"
sh "『そうですよ、沙雪。今回の婚約話は消えたのですから、家でゆっくり話し合いましょう……今後の事を』"
"左右の電話から、同時に説き伏せられて。"
"沙雪さんは静かに、うなづいた。"
voice "Sayuki0802"
s "「わかり、ました……今から、帰ります」"
"どちらにもそう告げると、沙雪さんは家電を切り、携帯をワタシに手渡してくれた。"
voice "Mobsayuhh0008"
sh "『いきなりお電話してしまって、ゴメンなさいね、六夏さん』"
voice "Rikka_1481"
rk "「い、いえ……そんな、事は……」"
voice "Mobsayuhh0009"
sh "『今後は沙雪にも、携帯を持たせる事にするわ。それじゃ……またね』"


show char trk04z at left
with dis



voice "Rikka_1482"
rk "「は、はいっ、失礼しますっ！！」"
"背中に汗をびっしょりかいて、ドキドキしながら、ワタシは何とか沙雪さんのお母さんとの話を終えた。"


show char trk03z at left
with dis



voice "Rikka_1483"
rk "「はぁ、はぁ、はぁ……め、メチャクチャ緊張したぁ……はぅぅ……」"
voice "Sayuki0803"
s "「わ……私も、です……六夏、さん……はぁ～」"
"そのまま崩れ落ちるように、ワタシたち２人は床にへたり込んだ。"
"電話が来るまでは、まさかこんな急展開になるとは思っていなかった。"
"ワタシと沙雪さんは思わず、ニッコリ微笑みあった。"


show char trk02z at left
show char tsy02z at right as r
with dis



voice "Rikka_1484"
rk "「ふふっ、でも疲れたね……お茶でも飲む、沙雪さん？」"
voice "Sayuki0804"
s "「あっ、はい。頂きます。ですが……それを頂いたら、私……家に帰ります」"
voice "Rikka_1485"
rk "「そう、だよね……そうした方が、いいよね……うん」"


stop music fadeout 1


play music "sound/BGM20.ogg"


"沙雪さんが、帰ってしまう……昨日から、そうしてもらえるよう、望んでいたはずなのに。"
"いざ、その時が来ると、こんなにも寂しくなるなんて、思わなかった。"


show char trk03z at left
with dis



voice "Rikka_1486"
rk "（たった、２日なのに……２日間だけの、新婚さんみたいな時間が……終わってしまうんだ）"
"今更になって、すごく名残惜しくなってきた。"
"これなら、あと数日……ううん、何日でも泊まって欲しかった。"


show char trk02z at left
with dis



voice "Rikka_1487"
rk "「沙雪……さん、その……楽しかったよ」"
voice "Sayuki0805"
s "「私もです、六夏さん……本当に」"
voice "Rikka_1488"
rk "「楽しい、だけじゃないよ、なんかすごく、幸せで……とってもとっても、幸せで、メチャクチャ幸せだったよ」"
voice "Sayuki0806"
s "「六夏さん……ぅ、ぅぅ……そんな事、言わないで下さい。帰れなくなってしまいます……」"


show char trk10z at left
with dis



voice "Rikka_1489"
rk "「沙雪さん……ワタシ、沙雪さんを帰したくないよ……くっ、くぅぅっ」"
"ダメ、涙がにじんできた。"


show char tsy10z at right as r
with dis



"そしてそれは、沙雪さんも同じだった。"
"どちらからともなく、ワタシ達は抱きあっていた。"
voice "Rikka_1490"
rk "「あぁ、沙雪さん……さゆ……ぅぅ、ひっく……」"
voice "Sayuki0807"
s "「六夏さん……ありがとう、ございます。本当に、お世話になりました」"
"離れたくない、このままでいたい……沙雪さんだって、そう思っている。"
"でもそれではダメだって事も、分かっている。"
"だから彼女は、悲しみを堪えて、言ってくれたんだ……別れの挨拶を。"
"そんな決意をしてくれた沙雪さんをこれ以上、引き止めておくワケにはいかない。"
"だからワタシはそっと、愛しい沙雪さんの体を放した。"


show char trk01z at left
with dis



voice "Rikka_1491"
rk "「沙雪さん……じゃあ、またね……」"


stop music fadeout 1


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


play music "sound/BGM22.ogg"


#**アトリエ・昼
scene bg bg29a
with Dis



#mes on
#system on


#//SE：携帯コール音
#♀SE007
play sound "sound/SE007.ogg"


show char tmi01s2
with dis



voice "Miya_0559"
m "「はい……」"
voice "Mobsayugm0010"
ss "『綾瀬のお嬢ちゃん……本当にありがとう。大事な孫娘を、とんでもないところにやるところだった……恩に着る』"
voice "Miya_0560"
m "「沙雪さんは、わたくしの友人ですから……お役に立てて、何よりです」"
voice "Mobsayugm0011"
ss "『しかしワシも、もう歳かのぉ……『すまほ』とか『そーしゃるあぷり』とか、さっぱり分からん事が増えてしまってのぉ』"
voice "Miya_0561"
m "「いえ、まだまだ現役でいけますわ。ですが最近は、昔とは違った変わったビジネスも多くなりました……誰かその方面に精通した、若い補佐をつければ良いと思います」"
voice "Miya_0562"
m "「そして最終的なご判断は、聡明な白河会長がなされば良いのです」"
voice "Mobsayugm0012"
ss "『的確な意見じゃな……どうじゃ、綾瀬のお嬢ちゃん。貴女を『へっどはんてぃんぐ』したいのじゃが』"


show char tmi03s2
with dis



voice "Miya_0563"
m "「お気持ちは嬉しいですが……」"
voice "Mobsayugm0013"
ss "『ああ、わかっておる。年寄りの冗談じゃ』"


show char tmi02s2
with dis



voice "Miya_0564"
m "「ふふっ……ところで、お願いしていたものですが、先ほど届きました。ありがとうございます」"
voice "Mobsayugm0014"
ss "『今回の礼が、あのようなもので良いのかい？』"
voice "Miya_0565"
m "「いいえ、十分です……感謝致します」"
voice "Mobsayugm0015"
ss "『今度また、ゆっくり話でもしたいものじゃ……何っ、沙雪が帰ってきた！？　すまんが綾瀬のお嬢ちゃん、今日はこの辺でな』"


show char tmi01s2
with dis



voice "Miya_0566"
m "「はい、それではごきげんよう……あらっ、ナイスタイミングね」"

#//SE：ドアの開く音
#♀SE027
play sound "sound/SE027.ogg"


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0920"
r "「お待たせ、美夜。誰かと電話でもしていたの？」"
voice "Miya_0567"
m "「ええ、ちょっと商談をね……ところで璃紗、美味しいトリュフチョコが手に入ったの。一緒に食べましょう」"


show char tri02s2 at right as r
with dis



voice "Risa_0921"
r "「私、トリュフチョコ大好きなの……ってこれ、この前テレビでやってた、フランスの超高級なヤツじゃない♪　うわぁ{image=image/exch001.png}　本当にいいの、美夜？」"


show char tmi02s2 at left
with dis



voice "Miya_0568"
m "「もちろん。好きなだけ食べてね、璃紗……ふふふっ{image=image/exch001.png}」"


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
jump S052



