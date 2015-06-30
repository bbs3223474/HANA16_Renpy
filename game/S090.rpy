#「紗良の力になりたい」

label S090:
$ save_name = "◇紗良の力になりたい"


#**北嶋家ダイニングキッチン・夜
scene bg bg13c
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


show char tka01f2
with dis



voice "Kaede_0264"
k "「……ふう、これでいいわ」"
"スーパーで大量に買った食材を、私はすぐ調理した。"
"今日の夕飯は、私の手料理。"
"久々の料理に感覚が鈍っていないか、ちょっと心配になったけど……味見をしてみて、その不安も消えた。"


show char tka02f2
with dis



voice "Kaede_0265"
k "「うん……良かった、美味しくできたわ」"
"張り切って作った料理を、テーブルいっぱいに並べたけど。"
"でもメールの返信通り、紗良はなかなか帰って来なかった。"
"ラップをかけた料理は、すっかり冷めきってしまって。"
voice "Kaede_0266"
k "「なんか前にも、こんな経験あったわね……ふふっ」"


#allClear:
hide char tka02f2
#lastBG:
#scene bg bg13c
with dis


"あの時はすごく不安だったけれど、今はもうそれはない。"
"私と紗良は離れていても……強く繋がっているんだもの。"
"私はぼんやりとテレビを見て、紗良の帰りを待っていた。"
"しばらくそうしていると、やがて玄関のドアが開く音がした。"


show char tsa01f2
with dis



voice "Sara_0368"
sr "「はぁ、はぁ……ただいまー」"


show char tka01f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0267"
k "「紗良、お帰りなさい！」"
"玄関に出て、紗良を出迎える。"
"夜中前に帰って来た紗良はモデルらしからぬ、くたびれた顔をしていた。"
"相当の、お疲れモードだ。"
voice "Sara_0369"
sr "「わーん、楓ちゃん、会いたかったよ～」"
"甘えて抱きついてくる身体を、いたわるように抱きしめ返す。"


show char tka02f2 at left
with dis



voice "Kaede_0268"
k "「よしよし、紗良、お疲れ様ね」"
voice "Sara_0370"
sr "「あぁ、楓ちゃんのなでなで、癒される～……今日の撮影、本当に疲れちゃったよぉ」"


show char tka01f2 at left
with dis



voice "Kaede_0269"
k "「でもちゃんと、無事に終わったんでしょう？」"
voice "Sara_0371"
sr "「うん、なんとかね……こんな遅くまで、かかっちゃったけど」"
voice "Kaede_0270"
k "「じゃあ良いじゃない。終わりよければ、全てよしよ」"
voice "Sara_0372"
sr "「それもそうかぁ、うん、楓ちゃんもそう言ってるし、今日のこのイライラは水に流そうっと」"
voice "Kaede_0271"
k "「そうそう紗良、お腹は空いてる？」"


show char tsa03f2 at right as r
with dis



voice "Sara_0373"
sr "「うん、お昼からずっと食べてないから、もうペコペコだよっ」"
voice "Kaede_0272"
k "「こんな夜遅くだけど……ご飯作ってあるの、食べない？」"


show char tsa04f2 at right as r
with dis



voice "Sara_0374"
sr "「も、もしかして……楓ちゃんの手作り料理！？」"
voice "Kaede_0273"
k "「うん。この間、紗良がオムライス作ってくれたじゃない？　だから、私も……と思って」"


show char tsa02f2 at right as r
with dis



voice "Sara_0375"
sr "「やったぁ、楓ちゃんの料理、すっごく嬉しいよぉ～」"
"紗良はさっきまで疲れてた顔を輝かせて、喜んでくれた。"
"料理ひとつでこんなに喜んでくれるなら、毎日だって作ってあげたい……そう思った。"
voice "Kaede_0274"
k "「お口に合うか、わからないけれど」"
"テーブルに移動し、料理を見る紗良の瞳は、今にもこぼれ落ちそうな程、輝いていた。"
voice "Sara_0376"
sr "「わー、これ、すっごく豪華だね、こんなにいっぱい……食べきれるのかなぁ？」"
voice "Kaede_0275"
k "「ちゃんとカロリー計算して作ったから、いっぱい食べても太らないわよ。余ったら、明日の朝やお弁当にすればいいし」"


show char tsa10f2 at right as r
with dis



voice "Sara_0377"
sr "「楓ちゃんの手料理、久々だなぁ……頑張れば、こんなに良いこともあるんだねぇ」"


show char tka03f2 at left
with dis



voice "Kaede_0276"
k "「ちょっと紗良、うるうるして、どうしたの？」"
voice "Sara_0378"
sr "「紗良は今、モーレツに感動していますっ！！」"


show char tka01f2 at left
with dis



voice "Kaede_0277"
k "「もう……大げさなんだから」"
voice "Sara_0379"
sr "「そんなことないっ、ああ、嬉しさで前が見えないよぉ～」"
"そんな紗良の姿を見ていると、やっぱり作って良かったと思う。"
"私もこの間、紗良に手料理を作って貰えて嬉しかったから、その気持ちはよく分かる。"
voice "Kaede_0278"
k "「はい紗良、いっぱい召し上がれ」"
voice "Sara_0380"
sr "「いただきますっ……もぐもぐ、うわ、すっごく美味しいーっ！！」"
"グルメリポートのお仕事をすることもあって、紗良のリアクションは抜群だ。"
"でもそれは、仕事用の顔じゃなくて。"
"素の彼女が、本当に美味しいと思って言ってくれているのが、しっかりと伝わってくる。"


show char tka02f2 at left
with dis



voice "Kaede_0279"
k "「良かった……紗良にそう言って貰えると、私も嬉しいわ」"
voice "Sara_0381"
sr "「ううっ、楓ちゃん、絶対に良いお嫁さんになれるよ！　紗良に毎日、お味噌汁作ってね」"
voice "Kaede_0280"
k "「紗良がそうして欲しいなら、いくらでも作るわ」"
voice "Sara_0382"
sr "「紗良、嬉しすぎて、このまま死んでもいいよぉ……ぅぅぅっ」"


show char tka01f2 at left
with dis



voice "Kaede_0281"
k "「ちょっと紗良、今死んじゃったら、私が悲しいわ」"


show char tsa01f2 at right as r
with dis



voice "Sara_0383"
sr "「そうでした、楓ちゃんを残して、死ねないよねっ」"
voice "Kaede_0282"
k "「もちろん、私もよ」"


show char tsa02f2 at right as r
with dis



voice "Sara_0384"
sr "「うんうん、これからの人生、楓ちゃんといーっぱい楽しんでいきたいもんね」"


show char tka02f2 at left
with dis



voice "Kaede_0283"
k "「ずっと一緒に、楽しみましょうね」"
voice "Sara_0385"
sr "「はぁ～い！　でも楓ちゃん、この味付け最高過ぎるよぉ～」"


show char tka01f2 at left
with dis



voice "Kaede_0284"
k "「紗良は私好みの味付け、研究しているんでしょう？　私も紗良の好きな味、熟知しているつもりよ」"
voice "Sara_0386"
sr "「おお～、楓ちゃん……楓ちゃんは紗良にとって、最高に理想の恋人だよぉ{image=image/exch001.png}」"


show char tka02f2 at left
with dis



voice "Kaede_0285"
k "「うふふっ、ありがとう。お仕事を頑張っている紗良も、私にとっては最高の恋人よ」"
voice "Sara_0387"
sr "「あーん、楓ちゃん、大好きっ」"
voice "Kaede_0286"
k "「私も……好きよ、紗良が大好き」"
voice "Sara_0388"
sr "「えへへっ……」"
voice "Kaede_0287"
k "「うふふっ……」"
"ああ、なんだか照れ臭い。"
"顔を見合わせて、２人で笑い合う。"
"紗良はその細い体に似合わず、大半の料理を見事にお腹に収めた。"
"ちょっと残ったけれど、それは明日のお弁当に入れてあげよう。"


show char tsa01f2 at right as r
with dis



voice "Sara_0389"
sr "「ご馳走さまでした、楓ちゃんっ」"


show char tka01f2 at left
with dis



voice "Kaede_0288"
k "「紗良、お風呂もわいてるわよ」"


show char tsa02f2 at right as r
with dis



voice "Sara_0390"
sr "「もう、楓ちゃんったら……至れり尽くせり、良妻過ぎっ」"
voice "Kaede_0289"
k "「ゆっくり温まって、ちゃんと疲れを落としてね」"


show char tsa01f2 at right as r
with dis



voice "Sara_0391"
sr "「はーい……あっ、でも後片付けが……」"
voice "Kaede_0290"
k "「やっておくからいいわ。早くお風呂に入ってきなさい」"


show char tsa02f2 at right as r
with dis



voice "Sara_0392"
sr "「ありがと、楓ちゃんっ！」"


hide char tsa02f2 at right as r
with dis


"紗良は一回、自室に戻って準備をしてから、パタパタとお風呂場へと向かった。"
"その間に私は、洗いものを始めた。"


show char tka01f2
with dis



voice "Kaede_0291"
k "「なんか……これってまるっきり、主婦みたいね」"
"だけど、紗良を思ってすることだから、全然苦にならない。"
voice "Kaede_0292"
k "「私の原動力は、食べ物ではなくて、紗良そのものなんだわ……きっと」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**北嶋家ダイニングキッチン・夜
scene bg bg13c
with Dis



#mes on
#system on


show char tsa02f2
with dis



voice "Sara_0393"
sr "「はぁ、良いお湯でした～」"
"数十分経って、紗良がお風呂から上がってきた。"
"お湯で清めた紗良の肌は、つやつやのすべすべだ。"


show char tsa01f2
with dis



voice "Sara_0394"
sr "「あっ、そうだ。見たい深夜番組があったんだ～。ねっ、見てもいい？」"


show char tka01f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0293"
k "「ええ、いいわよ」"
"ソファに座る私の隣に腰かけた紗良は、早速テレビを付けた。"
"賑やかな音声が、深夜の室内に響き渡る。"
voice "Sara_0395"
sr "「これ、楓ちゃんが出演したヤツだよね」"


show char tka05f2 at left
with dis



voice "Kaede_0294"
k "「あっ……そうね。あらたまって見ると、なんか恥ずかしいわ」"
"自分がテレビに出ているのを見ると、今でも不思議な感覚になる。"


show char tsa02f2 at right as r
with dis



voice "Sara_0396"
sr "「楓ちゃん、可愛いなぁ……他の子たちよりも、ずっと可愛いよ」"
voice "Kaede_0295"
k "「紗良……もういいわよ、そんな」"
voice "Sara_0397"
sr "「まあ、実物はもっともっと美人なんだけどね{image=image/exch001.png}」"
voice "Kaede_0296"
k "「紗良ったら……」"


#allClear:
hide char tka05f2 at left
hide char tsa02f2 at right as r
#lastBG:
#scene bg bg13c
with dis


"しばらく見入って、やがて、私の出演番組も終わって。"


show char tka01f2
with dis



voice "Kaede_0297"
k "「じゃあ、そろそろ部屋に戻りましょうか、紗良……紗良？」"
voice "Sara_0398"
sr "「……すぅ……くぅ、すぅ……」"
"隣りにいる紗良に目をやると、いつの間にかぐっすりと寝入ってしまっていた。"


show char tka03f2
with dis



voice "Kaede_0298"
k "「もう……困ったわね。こんなところで寝ていると、風邪を引いちゃうわよ」"
"紗良の体を抱えて、ベッドまで運んであげられれば良いのだけど。"
"あいにく私には、そんな腕力はない。"
voice "Kaede_0299"
k "「ああ、どうしようかしら……あっ、そうだわ」"


#※EV055
#allClear:
hide char tka03f2
#lastBG:
#scene bg bg13c
scene bg EV55
with Dis



"私はベッドから毛布を持ってきて、それをそっと紗良にかけてあげた。"
voice "Kaede_0300"
k "「紗良……お仕事、お疲れ様……ちゅっ」"
"紗良のつるつるほっぺを撫でながら、額に軽くキスを落とした。"
"紗良からはほのかに、ボディソープの良い匂いが漂ってきて、私の鼻腔をくすぐる。"
voice "Kaede_0301"
k "「本当に、お疲れ様……紗良は偉いわね」"
voice "Sara_0399"
sr "「くぅ……すぅ、くぅ……ぅぅん……かえで、ちゃん……すぅ」"
"あどけない顔で眠る紗良に愛しさが溢れて、思わず抱きつきそうになる。"
"私のお仕事を見て、紗良が可愛いとか、綺麗とか言ってくれることは、とても嬉しい。"
"決して私は、アイドルの仕事が嫌いなのではない。"
voice "Kaede_0302"
k "「でも……それ以上に、やりたいことがあるの」"
"今、それをはっきりと自覚した。"
"頑張っている紗良を見ることは、本当に大好きで。"
"でも、忙しくて自己管理ができていないような面もあって。"
"たまに見ていて、胸が張りさけそうに苦しくなる時がある。"
"だったら……私がずっと傍に付いて、紗良を見守っていきたい。"
voice "Kaede_0303"
k "「そうよ……私は、紗良のマネージャーになりたいの……」"
"紗良のサポートがしたい、私は今、そう強く願っている。"
"紗良を守ってあげる、そんな存在になりたい。"
"芸能界が華やかなだけじゃないことは、自分も経験したから、少しはわかっている。"
"そんな場所で、周りが敵ばかりになっても、紗良を力強く支えてあげて。"
"時には厳しく意見し、時には優しく褒めてあげたい。"
"その為の勉強がしたいから、学校にもちゃんと行っておきたい。"
voice "Kaede_0304"
k "「でも、そうなったら……アイドルを辞めなくてはならないわ」"
"元々、紗良の強い意向で入った芸能界。"
"紗良はアイドルをしている私を、応援してくれている。"
voice "Kaede_0305"
k "「裏方になりたい、なんて言ったら……」"
"もしかしたら、反対するかもしれない。"
"それでも私は、やっぱり……"
voice "Sara_0400"
sr "「……ん……楓ちゃん、それは……ダメ……」"
voice "Kaede_0306"
k "「えっ！？」"
"紗良は起きていて、私の内心を読んだ……と思って、驚いてしまった。"
"でもその紗良が目を開けて、起きてくる様子は一向にない。"
voice "Kaede_0307"
k "「紗良……？」"
voice "Sara_0401"
sr "「むにゃ……そんな、そんなとこ触ったら、紗良はもう、もうダメだよぉ……あぁ、無理ぃ」"
voice "Kaede_0308"
k "「………………もぉっ！」"
"どうやら、ただの寝言だったようだ。"


#※EV055P1
scene bg EV55p1
with Dis



voice "Kaede_0309"
k "「紗良ったら……一体、どんな夢を見ているのかしら……ふふっ{image=image/exch001.png}」"
"ちょっとエッチな夢を見ていると思うと、私はドキドキしながらも、苦笑してしまった。"
"身じろいでずれた毛布を、肩まで掛け直して、軽く溜息をつく。"
voice "Kaede_0310"
k "「紗良……私の気持ち、分かってくれるかしら……」"
"もう決意したことだけれど、紗良の寝顔を見つめていると、私は迷わずにはいられなかった……"


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
jump S091


