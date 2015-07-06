# 七海的音频文件名没有下划线！
# 本章第一次出现选择肢
# 由于Ren'py使用Python语言编写，对多平台通用性很强，
# 因此它对空格和文件名大小写要求也非常严格。
# 编写选择肢时，menu命令的格式如下：
# menu:
#     （空4格）"（选择肢1内容）":
#      （空5格）jump choice1
#     （空4格）"（选择肢2内容）":
#      （空5格）jump choice2
# label choice1:
# 内容
# jump choice1_done
###############################
# 如上，其中choice1是选择后跳到的脚本分支的名称，可随意命名，choice1_done是选择肢分支剧情结束后
# 跳到的共通文本，也可随意命名。
# 
# 同时，S003也开始出现三个立绘同屏的场景。
# 在这里再次强调定义方法：最左的用show char xx at sleft as l，中间的保持show char xx，最右用show char xx at sright as sr
# 同时，若之前存在立绘，则必须要用hide命令先隐藏立绘后再进行显示，否则会出现新旧立绘层叠的问题。

#「１年生会あらため、２年生会」

label S003:
$ save_name = "◇１年生会あらため、２年生会"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


show char tna01s2
with dis



voice "Nanami0000"
n "「璃紗さん、お待たせ～」"


show char tna01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0067"
r "「じゃあ、行きましょうか」"
voice "Nanami0001"
n "「いつものカフェでいいよね」"
voice "Risa_0068"
r "「ええ」"
"七海さんにメールした翌日。"
"早速、放課後一緒に待ち合わせて、２人でお茶をすることになった。"
"七海さんも『新１年生ベストカップル』の話には興味津々で、話したいコトがたくさんあるからって言っていたし。"
voice "Risa_0069"
r "「ん……ところで今日、紗良さんは？」"
voice "Nanami0002"
n "「誘ってみたんだけど、仕事で来れないって、今朝メールが来ていたの……すごく来たがっていたわ」"
voice "Risa_0070"
r "「残念だけど……それだけ人気があるってことだもんね、紗良さん」"
voice "Nanami0003"
n "「だから今日は、２人で１年生会だね」"
voice "Risa_0071"
r "「ううん、違うわよ、七海さん」"


show char tna03s2 at left
with dis



voice "Nanami0004"
n "「えっ……何が違うの？」"
voice "Risa_0072"
r "「私たち、もう２年生でしょう……だからこれからは、２年生会よ」"


show char tna05s2 at left
with dis



voice "Nanami0005"
n "「ふえっ、そうだったね」"
"ベストカップルに選ばれた、私と七海さん、そして北嶋紗良さん。"
"私たち３人は昨年『１年生会』というものを結成した。"
"といっても大げさなものじゃなくて、カフェでお喋りしたりするだけの集まりなんだけどね。"
"みんな恋人持ち、って共通点があるので、恋愛相談や惚気話も気兼ねなく出来るのが楽しくて。"
"私たちは何かあるたびに、よく集まっていた。"
"だけど今年になってから、紗良さんはなかなか参加できず、私と七海さんだけってことが多くなった。"
"紗良さんは元々、モデルのお仕事をしていて、忙しい人だったんだけど。"
"恋人である楓さまとユニットを組んでから、ますます仕事が忙しくなってしまった。"
"モデルにＣＭに歌に大活躍で、なかなか時間がとれないみたい……"


show char tna01s2 at left
with dis



voice "Nanami0006"
n "「ところで璃紗さん、知ってる？　紗良さん映画出演のオファーが来たって、噂もあるの」"


show char tri04s2 at right as r
with dis



voice "Risa_0073"
r "「ええっ～、そうなんだ。すごいねぇ」"
voice "Nanami0007"
n "「ますます忙しくなっちゃいそうだね……紗良さん」"


show char tri01s2 at right as r
with dis



voice "Risa_0074"
r "「ええ、本当に……」"
"恋人の楓さまの話になると、めちゃくちゃ暴走してしまう紗良さん。"
"この会のムードメーカー的な紗良さんがいないと、なんだか物足りなさを感じてしまう。"
"七海さんも、それは同じみたいで……お互い、ちょっとしんみりしてしまった。"


#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


scene bg bg17a
with dis


#mes on
#system on


"あれこれ考えていると、いつの間にかカフェの前に到着していた。"


show char tna02s2
with dis


voice "Nanami0008"
n "「今日のおすすめケーキ、何かな？」"
"寂しさを紛らわせるように、七海さんが楽しそうに店頭のメニュー表をのぞき込む。"
"私はそんな彼女に習うように、メニューを指さして、あれが美味しそうだわと微笑んだ。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**カフェ・昼
scene bg bg36a
with Dis



#mes on
#system on


show char tri01s2
with dis



voice "Risa_0075"
r "「では……ただいまより、２年生会を開催します」"


show char tna02s2 at left
show char tri01s2 at right as r
with dis



voice "Nanami0009"
n "「ふふっ、乾杯♪」"


show char tri02s2 at right as r
with dis



voice "Risa_0076"
r "「乾杯♪」"
"ティーカップの端をちょっとだけ触れさせて、乾杯する。"
"お酒じゃないけど、この会のちょっとした『お約束』みたいな感じかな。"


show char tna01s2 at left
show char tri01s2 at right as r
with dis



voice "Nanami0010"
n "「そろそろアイスティーの季節かなって思うけれど……」"
voice "Risa_0077"
r "「ついつい、ホットで頼んじゃうのよね～」"


show char tna03s2 at left
with dis



voice "Nanami0011"
n "「そしてケーキも毎回、頼んじゃう……ダイエットしなきゃなんだろうけど」"


show char tri03s2 at right as r
with dis



voice "Risa_0078"
r "「それは、私もよ……まったく、世の中にはダイエットには無縁の人もいるのにね」"
voice "Nanami0012"
n "「そうそう、なんであれだけ食べてるのに」"
voice "Risa_0079"
r "「太らないのかしら」"
voice "Nanami0013"
n "「ねーっ」"
voice "Risa_0080"
r "「ねーっ」"


show char tna02s2 at left
show char tri02s2 at right as r
with dis



"２人の声が重なったところで、思わず吹き出してしまう。"
"お互い、いくら食べても太らない、自分たちの恋人のことを考えていたに違いない。"
voice "Nanami0014"
n "「ふふふっ、璃紗さん前と比べると、普通に美夜さんの話題を出すようになったよね」"


show char tri04s2 at right as r
with dis



voice "Risa_0081"
r "「えええっ、そうかしら……」"


show char tna01s2 at left
with dis



voice "Nanami0015"
n "「うん。前は恥ずかしがって、なかなか話してくれなかったから」"


show char tri05s2 at right as r
with dis



voice "Risa_0082"
r "「そ、そう……かも……」"
"指摘されると、その通りなのかもしれない。"
"でも恥ずかしいのは、今でもそんなに変わってはいない。"
"私はこれ以上そっちの話題が膨らむ前に、すかさず話題を変えた。"


show char tri01s2 at right as r
with dis



voice "Risa_0083"
r "「１年のベストカップルのことだけど……七海さん、何か知ってる？」"
"すると『よくぞ聞いてくれました』とばかりに、七海さんが勢いよく喋り始めた。"


show char tna02s2 at left
with dis



voice "Nanami0016"
n "「もちろん。１年生の間ではもう、この２人で決まりって言われてるほどなの」"
voice "Risa_0084"
r "「へぇ～……そんなに有名なの？」"


show char tna01s2 at left
with dis



voice "Nanami0017"
n "「璃紗さん、全然心当たり、ないの？」"


show char tri03s2 at right as r
with dis



voice "Risa_0085"
r "「ええ、実は……１年生がそのことで盛り上がっているのも、昨日聞いたばかりで」"
voice "Nanami0018"
n "「そう。上級生の間でも、この２人のことは結構、知れ渡ってるみたいなの」"
"そうなんだ、すごいなぁ。"
"私って相変わらず、この手の話題には本当にうといのよね。"
"美夜じゃないけれど、自分たちのことにばかり興味がいきすぎて、他に目が行ってないというか。"
"美夜しか見えてない……というか。"
voice "Risa_0086"
r "「……私もあんまり、美夜のこと言えないかも」"
voice "Nanami0019"
n "「んっ、どうしたの？」"


show char tri01s2 at right as r
with dis



voice "Risa_0087"
r "「な、なんでもないわ。それで、そのお２人ってどんな人なの？」"
voice "Nanami0020"
n "「オッホン、それでは解説します。１年生のベストカップルの候補の１人は『白河沙雪』さん」"
voice "Nanami0021"
n "「武家の血を引く名家のお嬢様で、麗奈先生以来の『究極の淑女』と呼ばれているんだって」"
voice "Risa_0088"
r "「す、すごい人なのね……」"
"麗奈先生は今年の春まで、私の担任だった、ミカ女のＯＧ。"
"過去に『究極の淑女』と呼ばれるほど、ものすごいキャラだったみたい。"
"その名にふさわしく、とても綺麗でカリスマ性溢れる先生で、学生たちには大人気だった。"
"その麗奈先生と比べられるなんて……"
voice "Nanami0022"
n "「更に容姿端麗、性格良し、何でもこなす完璧超人。あだ名はお名前の一部を取って『白雪姫』って言うんですって」"
voice "Risa_0089"
r "「白雪姫、かぁ……ずいぶんと可愛い呼び名ね」"
"そういう可愛いあだ名なら、私もつけて欲しいかも。"
voice "Nanami0023"
n "「容姿や性格も、なんかお姫様っぽいみたいだからね」"
"お姫様っぽい性格って……それって、どんなのかしら。"
"少しずつ、興味がわいてくる。"
voice "Nanami0024"
n "「それでね、１年生ながら早くも『環境整備委員会』でも活躍中なの」"
voice "Risa_0090"
r "「そうだったのね……」"
"どおりで、七海さんが詳しいわけだわ。"
"彼女と同じ、環境整備委員だったのね。"
voice "Nanami0025"
n "「本当に、優秀なのよ……ものすごく、ね」"
"その話を聞きながら、私は先日、校内で七海さんが愚痴っていたのを思い出した……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（回想シーン）

#**新校舎廊下・昼
scene bg bg05a
with rr


#mes on
#system on


show char tna04s2
with dis



voice "Nanami0026"
n "「とにかく、沙雪さんはすごいのよ……すごすぎよ！」"


show char tna04s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0091"
r "「沙雪さんって？」"


show char tna01s2 at left
with dis



voice "Nanami0027"
n "「環境整備委員に最近入った、１年生の子なんだけどね」"


show char tri01s2 at right as r
with dis



voice "Risa_0092"
r "「七海さんの後輩ね。でも環境整備委員に入っている方は、みんなすごい人ばかりじゃない」"
voice "Nanami0028"
n "「レベルが違うのよ。沙雪さんは『優菜さまの再来』とか『麗奈先生の再来』なんて呼ばれているのよ」"
"優菜さまとミカ女ＯＧの麗奈先生といえば、まさに淑女の中の淑女ってイメージ。"
"その２人と並べ立てられるってことは……"
voice "Risa_0093"
r "「それって、とても優秀な方なのね……」"


show char tna03s2 at left
with dis



voice "Nanami0029"
n "「そうなの！　上と下に優秀な人がいると、わたしも大変だよ～」"
voice "Risa_0094"
r "「本当に苦労が多いわね、七海さん」"
voice "Nanami0030"
n "「わかってくれる？」"


show char tri03s2 at right as r
with dis



voice "Risa_0095"
r "「うんうん、私もね……」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（回想シーン終了）
#mes on
#system on


"その後、私も美夜の天才っぷりに着いて行けない悔しさを、愚痴ったりしたのよね。"
"その時は一度しか名前を聞いてなかったから、忘れていたけれど。"
"七海さんが嘆いていた原因の方が、この沙雪さんだったのね……"


#**カフェ・昼
scene bg bg36a
with lr


"今日も沙雪さんの話をしている七海さんの声のトーンが、ずるずるっと一段落ちた。"


show char tna03s2
with dis



voice "Nanami0031"
n "「わたし、優菜さまの後継者としてスパルタ教育中なんだけど……沙雪さんはわたしよりも、ずっと優秀だから」"


show char tna03s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0096"
r "「七海さん……」"
voice "Nanami0032"
n "「きっと沙雪さんの方が、優菜さまの後継者にふさわしいかも……」"
"だんだん声が小さくなり、ちょっと自己嫌悪に陥っているみたい。"
"そんな友達を、私は少しでも励ましたかった。"
voice "Risa_0097"
r "「でも七海さんだって、去年は１年生ながら、環境整備委員会に選ばれたじゃない」"
voice "Nanami0033"
n "「あれは、おねえ……ううん、優菜さまの配慮だから」"
voice "Risa_0098"
r "「その後、アルバム委員の仕事だってしっかりこなしていたでしょう。七海さんは立派な、優菜さまの後継者よ」"


show char tna01s2 at left
with dis



voice "Nanami0034"
n "「璃紗さん……ありがとう、璃紗さんみたいな優秀な人にそう言われると、自信ついてきちゃう」"
"良かった、少しは元気になってくれたみたいね。"
voice "Nanami0035"
n "「あーっ、わたしもっとしっかりしなきゃ、璃紗さんみたいに」"


show char tri03s2 at right as r
with dis



voice "Risa_0099"
r "「私だって、そんな自信満々なわけじゃないわ」"


show char tna04s2 at left
with dis



voice "Nanami0036"
n "「えっ……そうなの？」"


show char tri01s2 at right as r
with dis



voice "Risa_0100"
r "「ええ。だから自信をつけるためにも、努力はかかさないけどね」"


show char tna01s2 at left
with dis



voice "Nanami0037"
n "「ふぇっ……そういうところ、やっぱり璃紗さんは、みんなと違うわ」"
voice "Risa_0101"
r "「そうかしら？」"
"私をにこにこと見つめながら、七海さんは話を続けた。"


show char tna02s2 at left
with dis



voice "Nanami0038"
n "「じゃあ、もう１人のことも……その沙雪さんのお相手と言われているのは『篠崎六夏』さんよ」"


show char tri03s2 at right as r
with dis



voice "Risa_0102"
r "「………………リッカ？？」"


#★★★選択肢　ここから
#++選択肢（１）
#１．『聞いた事のない……名前ね』×
#２．『どこかで……聞いたような……』○
menu:
 "聞いた事のない……名前ね":
  jump select01_1
 "どこかで……聞いたような……":
  jump select01_2



label select01_1:
#１．『聞いた事のない名前ね……』


voice "Risa_0103"
r "「聞いた事のない……名前ね」"
"何かちょっと、頭に引っかかったような気がした。"
"でもやっぱり、覚えていない名前だし……"
"とりあえず、今はちゃんと七海さんの話を聞かなくちゃね。"


jump select01_end


label select01_2:
#２．『どこかで……聞いたような……』○


"その名前を聞いた瞬間、何かが頭をよぎった。"
voice "Risa_0104"
r "「うーん、聞いた事あるような……」"
"………………でもダメ、思い出せない。"


show char tna01s2 at left
with dis



voice "Nanami0039"
n "「璃紗さん、ひょっとして知ってるの？」"
voice "Risa_0105"
r "「うーん、知ってるような、知らないような……」"
voice "Nanami0040"
n "「すごく有名な人だから、どこかで名前だけでも聞いたことあるかもしれないね」"
voice "Risa_0106"
r "「そうね、そうかもしれないわね」"
"でも何だか、少しひっかかる。"
"思い出したい……でも七海さんの話も、ちゃんと聞かなくちゃ。"


#set f1 f1+1


#++選択肢終了
#★★★選択肢　ここまで
label select01_end:


voice "Nanami0041"
n "「六夏さんは外部からの編入生で、成績は中の上くらいなんだって」"


show char tri01s2 at right as r
with dis



voice "Risa_0107"
r "「そう……普通ね。じゃあルックスがとっても素敵、とか？」"
voice "Nanami0042"
n "「すごいのはそっちじゃなくて、身体的性能なの。長身でスポーツ万能、陸上ではすごい記録の持ち主なんですって」"
voice "Risa_0108"
r "「へぇ……そっちも話だけ聞くと、やっぱりすごそうね」"
voice "Nanami0043"
n "「楓さまにも通じるところのある、王子様キャラなんですって。だから、あだ名は『白雪の騎士』」"


show char tri04s2 at right as r
with dis



voice "Risa_0109"
r "「白雪の……騎士！？」"
voice "Nanami0044"
n "「ね、面白いでしょう？　白雪姫を守る騎士だから、みんなそう呼ぶんだって」"
"姫の次は、騎士かぁ……なんだかロマンチックなワードばかり。"
"いつも家で読んでいる、ロマンス小説のワンシーンが浮かんできちゃうわ。"
"やっぱり騎士がお姫様に『貴女を一生、守らせてください』とか言うのかしら。"


show char tri02s2 at right as r
with dis



voice "Risa_0110"
r "「……ふふふっ、そういうのって素敵{image=image/exch001.png}」"


show char tna03s2 at left
with dis



voice "Nanami0045"
n "「璃紗さん、どうしたの？　ニヤニヤしちゃって」"


show char tri05s2 at right as r
with dis



voice "Risa_0111"
r "「あっ！　ななな、なんでもないわ……」"
"もう、恥ずかしいわ……七海さんの前なのに、妄想に耽りそうになってしまった。"


show char tri01s2 at right as r
with dis



voice "Risa_0112a"
r "「コホン……でもどちらも、すごい方なのね」"


show char tna01s2 at left
with dis



voice "Nanami0046"
n "「ええ。そんな２人がもし、わたしたちベストカップルのメンバーに加わったら……どうなるのかなぁ」"
voice "Risa_0113"
r "「どうかしら……少なくとも私たちには、ようやく後輩が出来るってことね」"


show char tna02s2 at left
with dis



voice "Nanami0047"
n "「ふふふっ、そうだね」"
"今のところ、１年だけで勝手に盛り上がっている話だから、彼女達が本当に私たちのメンバーになるかどうか、分からないけれど。"
"興味深いのは、確かだわ。"
"近いうちに本人たちを是非、見てみたいかも……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#mes on
#system on


"その後、私たちは情報交換という名目のおしゃべりを続けて。"
"陽が傾き始めた頃になって、やっと店を出た。"


#**繁華街・昼
scene bg bg17a
with Dis



"会計を済ませて、店を出た直後。"
"よく知った顔が、息を切らせて現れた。"


show char tsa03f2
with dis



voice "Sara_0000"
sr "「はぁ、はぁ、おまたせ～……あれっ、もしかしてもう、店を出ちゃった？」"


show char tsa03f2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0114"
r "「紗良さん……」"

hide char tsa03f2 at left
hide char tri01s2 at right as r
show char tna03s2 at sleft as l
show char tsa03f2
show char tri01s2 at sright as sr
with dis



voice "Nanami0048"
n "「今日はお仕事じゃなかったの？」"


show char tsa02f2
with dis



voice "Sara_0001"
sr "「うん。紗良ね、仕事抜けてきたんだよー、さぁ、２年生会始めようよ♪」"
voice "Nanami0049"
n "「それが……ちょうど今、終わったところで……」"


show char tsa04f2
with dis



voice "Sara_0002"
sr "「ええっ、そんなぁ～」"


show char tna02s2 at sleft as l
show char tri02s2 at sright as sr
with dis



voice "Risa_0115"
r "「ふふふっ」"
voice "Nanami0050"
n "「ふふふっ」"


show char tsa03f2
with dis



voice "Sara_0003"
sr "「ちょっとちょっと、どうして笑うの、２人とも？」"
voice "Risa_0116"
r "「だって……んふ、ふふふっ」"
"七海さんと２人して、笑ってしまった。"
"紗良さんがアイドルになって、忙しくて、少し遠い存在になってしまった……そんな風にも思ったけれど。"
"彼女はこうして、変わらない存在でいてくれるんだもの。"
"心配は全然、杞憂だった。"


show char tna01s2 at sleft as l
with dis



voice "Nanami0051"
n "「紗良さん、すぐまた戻るの？」"


show char tsa01f2
with dis



voice "Sara_0004"
sr "「うん……空き時間に出てきただけだから」"
voice "Nanami0052"
n "「だったら、駅まで一緒に行きましょう。話したいこともあるし」"


show char tsa02f2
with dis



voice "Sara_0005"
sr "「七海ちゃん{image=image/exch001.png}　やっさしぃー♪」"


show char tri01s2 at sright as sr
with dis



voice "Risa_0117"
r "「私も途中まで、一緒に行くわ」"
voice "Sara_0006"
sr "「璃紗ちゃんも、ありがとう♪　それじゃ駅まで、２年生会でお喋りしよう」"
"少し遠回りになってしまったけれど。"
"久しぶりに３人揃った、２年生会。"
"私たちは仲良く、駅まで一緒に歩いた。"
"その道すがら、新１年生のベストカップルの話を紗良さんにもしてみたら……"


show char tsa09f2
with dis



voice "Sara_0007"
sr "「ダメだよぉ、楓ちゃん以上の王子様キャラなんて、ミカ女にはいないもん」"
"紗良さんはきっぱり、そう言い切ったのだった。"
"私はどこかで聞き覚えのある『白雪の騎士』の名前を再び、考えてみた……"
"でもどうしても、思い出せなかった。"


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
jump S004



