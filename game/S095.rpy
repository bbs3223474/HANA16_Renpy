#「楓、禁断の女教師コス！？」

label S095:
$ save_name = "◇楓、禁断の女教師コス！？"


#※楓視点に戻ります

#**住宅街・昼
scene bg bg08a
with Dis



#mes on
#system on


#♂MP12
play music "sound/BGM12.ogg"


show char tru01s2
with dis



voice "Runa_0082"
rn "「３人とも早く～！　遅いわよ」"


show char tsa03s2
with dis



voice "Sara_0542"
sr "「瑠奈ちゃん歩くの早いよ、もっとゆっくり行こうよー」"


#allClear:
hide char tsa03s2
#lastBG:
#scene bg bg08a
with dis


"先頭で歩き出す、瑠奈さん。"
"そしてその後を付いていく、紗良。"
"そしてそして、少し困った顔の貴子先生。"


show char tta03s2
with dis



voice "Takako0130"
t "「いきなりこんなことになって、ごめんなさいね。瑠奈は言い出したら聞かなくて……」"


show char tka01s2 at left
show char tta03s2 at right as r
with dis



voice "Kaede_0546"
k "「いえ……大丈夫です」"


#allClear:
hide char tka01s2 at left
hide char tta03s2 at right as r
#lastBG:
#scene bg bg08a
with dis


"紗良に続いて、瑠奈さんも現れたのは驚いたけれど。"
"私は嬉しさでいっぱいだった。"
"マネージャーと教師、どっちも目指すなんてとても欲張りなこと、何を言っているんだって言われても、仕方がないと思った。"
"でも紗良は、それを快く認めて、応援してくれるとまで言ってくれた。"
"いつでも、味方になってくれるって……"
"ただ……どうしてわざわざ制服に着替えさせられた上に、貴子先生たちの部屋に行くことになったのかは、よくわからないんだけど……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**貴子の部屋・昼
scene bg bg26a
with Dis



#mes on
#system on


show char tsa01s2
with dis



voice "Sara_0543"
sr "「おじゃましまーす……わぁ、綺麗な部屋だねぇ」"


show char tka01s2 at left
show char tsa01s2 at right as r
with dis



voice "Kaede_0547"
k "「そうね、素敵……おじゃまします」"
"初めて入った２人のお部屋は、清潔感で溢れていて、とても居心地が良さそうだった。"

hide char tka01s2 at left
hide char tsa01s2 at right as r
show char tka01s2 at sleft as l
show char tsa01s2
show char tru01s2 at sright as sr
with dis



voice "Runa_0083"
rn "「それじゃ早速、始めるわよ」"


show char tka03s2 at sleft as l
with dis



voice "Kaede_0548"
k "「……えっ？」"


show char tsa03s2
with dis



voice "Sara_0544"
sr "「始めるって……何を？」"


show char tta03s2 at sright as sr
with dis



voice "Takako0131"
t "「ふうっ、また突拍子もないことなんでしょう、瑠奈？」"


#allClear:
hide char tka03s2 at sleft as l
hide char tsa03s2
hide char tta03s2 at sright as sr
#lastBG:
#scene bg bg26a
with dis


"ここに来るまでの間、瑠奈ちゃんからは何の説明もされなかった。"
"私の頭にはクエスチョンマークが飛び交っている。"
"それは紗良も、貴子先生も一緒だと思う。"


show char tru01s2
with dis



voice "Runa_0084"
rn "「何って……教師になりたいんでしょう？　だったら教師になる為のレッスンをしなくちゃダメだと思うのよ」"


show char tka03s2 at left
show char tru01s2 at right as r
with dis



voice "Kaede_0549"
k "「レッスン？」"

hide char tka03s2 at left
hide char tru01s2 at right as r
show char tka03s2 at sleft as l
show char tru01s2
show char tta03s2 at sright as sr
with dis



voice "Takako0132"
t "「レッスンって、何をするつもりなの？　瑠奈、あまり先輩方を困らせてはダメよ」"
voice "Runa_0085"
rn "「わたしは２人の為を思って、言っているのよ」"
voice "Kaede_0550"
k "「そうなの、瑠奈さん？」"
voice "Runa_0086"
rn "「そうよ、それとわたしのレッスンは厳しいけど……もし止めたいのなら、今の内よ」"
voice "Kaede_0551"
k "「………………」"
voice "Runa_0087"
rn "「どうする、辞める？」"


show char tka08s2 at sleft as l
with dis



voice "Kaede_0552"
k "「……いえ、やります、やらせて下さい！」"


show char tsa02s2 at sleft as l
show char tka03s2
show char tru01s2 at sright as sr
with dis



voice "Sara_0545"
sr "「おっ、楓ちゃんすごいやる気だね。よくわからないけど、紗良は応援するよ～♪」"


#allClear:
hide char tsa02s2 at sleft as l
hide char tka03s2
hide char tru01s2 at sright as sr
#lastBG:
#scene bg bg26a
with dis


"私も瑠奈さんのレッスン内容は、さっぱり想像できないけれど……"
"私の為を思って、言ってくれているのなら、その好意を無下にはできないわ。"


show char tru02s2
with dis



voice "Runa_0088"
rn "「やるのね……ふふふっ{image=image/exch001.png}」"


show char tka03s2 at left
show char tru02s2 at right as r
with dis



voice "Kaede_0553"
k "「えっ！？」"
"ニヤリと笑った瑠奈さんが、何かを企んでいるように見えた。"
"ああ、嫌な予感がする。"
"もしかして私、判断を誤ったかしら？"


show char tru01s2 at right as r
with dis



voice "Runa_0089"
rn "「よく言ってくれたわ、その言葉に二言はないわね？」"
voice "Kaede_0554"
k "「ええ、まぁ……」"
voice "Runa_0090"
rn "「じゃあ、これに着替えて」"


show char tka04s2 at left
with dis



voice "Kaede_0555"
k "「ええっ！？」"

#//SE：じゃじゃーん、的効果音
#♀SE046
play sound "sound/SE046.ogg"


"瑠奈さんがどこからともなく、取り出したもの……それはなんとスーツとブラウスだった。"


show char tka03s2 at left
with dis



voice "Kaede_0556"
k "「る、瑠奈さん……これは？」"


show char tsa03s2 at sleft as l
show char tka03s2
show char tru01s2 at sright as sr
with dis



voice "Sara_0546"
sr "「スーツ……だよね」"


show char tsa03s2 at sleft as l
show char tka03s2
show char tta03s2 at sright as sr
with dis



voice "Takako0133"
t "「就職活動の基礎対策でも、するつもりなのかしら？」"
"更に、私たちの疑問は高まる。"


#allClear:
hide char tsa03s2 at sleft as l
hide char tka03s2
hide char tta03s2 at sright as sr
#lastBG:
#scene bg bg26a
show char tru01s2
with dis



voice "Runa_0091"
rn "「わたしはね、何事も形から入るべきだと思うのよ」"


show char tka03s2 at left
show char tru01s2 at right as r
with dis



voice "Kaede_0557"
k "「か、形から？」"
voice "Runa_0092"
rn "「そう……これはズバリ、女教師ルックよ」"


show char tka04s2 at left
with dis



voice "Kaede_0558"
k "「ええっ！？」"
"瑠奈さんの脈絡のない言葉に、ガーンとショックを受けた。"

hide char tka03s2 at left
hide char tru01s2 at right as r
show char tsa04s2 at sleft as l
show char tka04s2
show char tru01s2 at sright as sr
with dis



voice "Sara_0547"
sr "「お、女教師ルック！？　それって……コスプレってヤツ！？」"


#allClear:
hide char tsa04s2 at sleft as l
hide char tka04s2
hide char tru01s2 at sright as sr
#lastBG:
#scene bg bg26a
show char tta03s2
with dis



voice "Takako0134"
t "「これに、何の意味が……」"


show char tru01s2 at left
show char tta03s2 at right as r
with dis



voice "Runa_0093"
rn "「せんせい……バカにしちゃいけないわ。形から入るって、とっても大事なことなのよ」"
voice "Takako0135"
t "「そうかしら……」"


#allClear:
hide char tru01s2 at left
hide char tta03s2 at right as r
#lastBG:
#scene bg bg26a
with dis


"貴子先生は、怪訝な表情をしている。"
"私も瑠奈さんの行動に、ただただ呆気にとられるばかりだった。"


show char tru01s2
with dis



voice "Runa_0094"
rn "「そうよ。さあ、これを着なさい」"


show char tka03s2 at left
show char tru01s2 at right as r
with dis



voice "Kaede_0559"
k "「で、でも……恥ずかしいわ。こんなことをしなくても良いんじゃ……」"
voice "Runa_0095"
rn "「何を言ってるの？　恥ずかしいなんて言ってたら、夢なんて叶えられないわよ」"
voice "Kaede_0560"
k "「そ、そんな……」"
"私は瑠奈さんの気迫に、ぐいぐいと押されていた。"
"どうしてだろう……年下なのに、なんか逆らえる雰囲気ではなくて。"


show char tsa08s2 at left
show char tka03s2 at right as r
with dis



voice "Sara_0548"
sr "「そうだよ、楓ちゃん。教師の格好ができなくて、どうして教師になれるの！？」"


show char tka04s2 at right as r
with dis



voice "Kaede_0561"
k "「さっ、紗良！？」"
voice "Sara_0549"
sr "「楓ちゃん……本気で教師を目指すなら、教師の格好が出来なきゃダメなんだよ！！」"
voice "Kaede_0562"
k "「えっ、ええっ……？」"
voice "Sara_0550"
sr "「紗良は楓ちゃんの夢を、本気で応援するとは言ったけれど……頑張れない楓ちゃんは、応援できないよ」"


show char tka01s2 at right as r
with dis



voice "Kaede_0563"
k "「紗良、あなた……」"
voice "Sara_0551"
sr "「だから楓ちゃん、瑠奈ちゃんの言うとおりにして！」"
"突然、話に入って来た紗良が、よくわからない説得を始めた。"
"一体どういう、心境の変化があったのかしら……？"
"本気で私の夢を応援してくれているから、もじもじしている私の背中を後押ししてくれているの？"


#★★★選択肢　ここから


#だとしたら、私は……


#++選択肢（３）
#１．『紗良の気持ちに応えたい』○
#２．『でもやっぱり、恥ずかしい……』×
menu:
 "紗良の気持ちに応えたい":
  jump select18_1
 "でもやっぱり、恥ずかしい……":
  jump select18_2



#１．『紗良の気持ちに応えたい』
label select18_1:


"だとしたら……抗えるはずない。"
"そんな紗良の応援に応えたい。"
voice "Kaede_0564"
k "「わかったわ……じゃあ着ます、着るから」"


show char tsa02s2 at left
with dis



voice "Sara_0552"
sr "「や、やったぁ……んふっ」"


show char tka03s2 at right as r
with dis



voice "Kaede_0565"
k "「えっ？　紗良……今なんて？」"


show char tsa01s2 at left
with dis



voice "Sara_0553"
sr "「ううん、なんでもないよ？　えへへ……」"


#set f1 f1+1
jump select18_end


#２．『でもやっぱり、恥ずかしい……』
label select18_2:


"紗良の気持ちが嬉しい、それに応えたい。"
"でもやっぱり……恥ずかしい、恥ずかしすぎるわ。"


show char tka05s2 at right as r
with dis



voice "Kaede_0566"
k "「あ、あの……やっぱり、今回は……普通に……」"


show char tsa09s2 at left
with dis



voice "Sara_0554"
sr "「だめだめだめっ！　夢を諦めちゃダメ、楓ちゃん！！」"


show char tka03s2 at right as r
with dis



voice "Kaede_0567"
k "「さ、紗良……あぁ、そんなに強く言われたら……」"
"拒みづらいじゃない、もう……"
voice "Kaede_0568"
k "「……わかったわ、着るわよ」"


show char tsa02s2 at left
with dis



voice "Sara_0555"
sr "「んふふ……成功せいこう」"
voice "Kaede_0569"
k "「えっ？　紗良……今なんて？」"


show char tsa01s2 at left
with dis



voice "Sara_0556"
sr "「ううん、なんでもないよ？　えへへ……」"


#++選択肢終了
#★★★選択肢　ここまで
label select18_end:



voice "Kaede_0570"
k "「そう？」"


show char tsa02s2 at left
with dis



voice "Sara_0557"
sr "「うん{image=image/exch001.png}　それより楓ちゃん、時間がもったいないから、早くそれ着てレッスンしようよ♪」"


show char tka08s2 at right as r
with dis



voice "Kaede_0571"
k "「そうね、恥ずかしいけれど……私、頑張るわ」"
voice "Sara_0558"
sr "「うんうん、ぜーったい似合うよ～～」"


#allClear:
hide char tsa02s2 at left
hide char tka08s2 at right as r
#lastBG:
#scene bg bg26a
show char tru01s2
with dis



voice "Runa_0096"
rn "「じゃあ……せんせい。せんせいは楓さんの制服を着て」"


show char tru01s2 at left
show char tta04s2 at right as r
with dis



voice "Takako0136"
t "「えぇえぇっ！？」"
"貴子先生の顔が、みるみる青ざめていく。"


show char tru02s2 at left
with dis



voice "Runa_0097"
rn "「ミカ女の制服、以前は着ていたんでしょう？　懐かしいわよね、せんせい♪」"
"瑠奈さんが、きっぱりと言った。"
"貴子先生の口元がぴくぴく、引きつっている。"


show char tta03s2 at right as r
with dis



voice "Takako0137"
t "「ちょっと瑠奈、それってどういう意味なの？？」"


show char tru08s2 at left
with dis



voice "Runa_0098"
rn "「つべこべ言わない。さっさと着て、せんせい」"


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


"瑠奈さんは無理やり、私たちを別室に押しやって。"
"そして私たちは女教師とミカ女の制服を、それぞれ着させられたのだった……"
"ちなみに……貴子先生はかつて着ていた自分の制服を着ることにしたのだけど……"
"実家暮らしでもないのに、なんでここにあるんだろう……？"


#※EV059
scene bg EV59
with Dis



voice "Kaede_0572"
k "「こ……これでいいの？」"
voice "Takako0138"
t "「こんなの、やだ……恥ずかしすぎるわ」"
"着替え終わって、紗良と瑠奈さんの前に立つ、私と貴子先生。"
"ううっ、なんだか見ている２人の視線が痛い。"
"痛すぎるわ……やっぱり、おかしな格好なのよね……えっ！？"


#※EV059P1
scene bg EV59p1
with Dis



voice "Sara_0559"
sr "「キターーー{image=image/exch001.png}　瑠奈ちゃん……萌えっ、萌えるよおおおおおお{image=image/exch001.png}{image=image/exch001.png}」"
voice "Runa_0099"
rn "「ふふふっ、レッスンなんて真っ赤なウソよ。これが今回の、全ての狙いだったのよっ{image=image/exch001.png}」"
voice "Sara_0560"
sr "「あ～んっ、楓ちゃんの女教師姿……ごちそうさまです、眼福です。写真撮りたいいいいいっ{image=image/exch001.png}」"
voice "Runa_0100"
rn "「後でレッスンにかこつけて撮りましょう。デジカメ用意しておいたわ」"
voice "Sara_0561"
sr "「あああんっ、瑠奈ちゃんったら、準備がいいんだから{image=image/exch001.png}」"
voice "Runa_0101"
rn "「わたしは、萌えの為なら、手段は選ばないのよ」"
voice "Sara_0562"
sr "「その姿勢、尊敬しますっ」"
voice "Runa_0102"
rn "「ええ、はあ、やっぱりせんせいの制服姿、最高ねっ」"
voice "Sara_0563"
sr "「楓ちゃんの教師姿も最高ですっ。萌え死んじゃう～～、瑠奈ちゃん、グッジョブ～♪」"
voice "Runa_0103"
rn "「ふふんっ、朝飯前よ」"
voice "Takako0139"
t "「ど、どうして私が、この制服を着るのよ、瑠奈？」"
"ミカ女の制服を着て、相当恥ずかしがっている先生の顔は真っ赤。"
"膝をもじもじさせている。"
"その姿がとても、愛らしい……しかもその制服が本当に似合っている。"
"そのままミカ女の校内を歩いても、きっと違和感はないと思う。"
voice "Runa_0104"
rn "「だってせんせい、学生役だもの……その服装は当然でしょう」"
voice "Takako0140"
t "「でもそれだったら、現役の瑠奈や紗良さんがやっても良いんじゃないかしら……」"
voice "Runa_0105"
rn "「せんせい、何を言ってるの？　楓さんに協力するって言っていたのは、嘘だったの？」"
voice "Takako0141"
t "「それは、そうだけど……でも、とっくの昔に卒業した私が、こんな格好をするなんて……」"
voice "Runa_0106"
rn "「よーく似合ってるわよ、うん、サイズもぴったりね。ふたりともおっぱいが大きいから{image=image/exch001.png}」"
voice "Takako0142"
t "「そんな……瑠奈ったら！？」"
"瑠奈さんが、ニヤニヤ笑っている。"
"とても悪い顔に見えるのは、気のせいじゃないと思う。"
"もしかして、私たちはハメられたのかしら……そんな考えが今更、脳裏に過った。"
voice "Sara_0564"
sr "「楓ちゃん、女教師スタイル、合格だよ……満点だよぉ」"
voice "Kaede_0573"
k "「えっ？」"
voice "Sara_0565"
sr "「ああ……教師になるの、許してもいいかも……{image=image/exch001.png}」"
voice "Kaede_0574"
k "「どういう意味よ！？」"
voice "Sara_0566"
sr "「だって、似合いすぎてるんだもん……そんな格好でいると、教え子を悩殺しまくっちゃいそう」"
voice "Kaede_0575"
k "「ええっ！？」"
voice "Sara_0567"
sr "「紗良、ちょっと鼻血噴いちゃいそう……うぶ」"
voice "Kaede_0576"
k "「ちょっと紗良、何だかよくわからないけれど、しっかりしてー！」"
voice "Runa_0107"
rn "「そうよ。これからが本番なのよ」"
voice "Sara_0568"
sr "「はっ……瑠奈ちゃん……！？」"
voice "Runa_0108"
rn "「じゃあ、始めましょうか」"
voice "Takako0143"
t "「始めるって……何を？」"
voice "Runa_0109"
rn "「教師の予行演習よ」"
voice "Kaede_0577"
k "「予行演習？」"
voice "Runa_0110"
rn "「そう。せんせいを教え子にして、ちょっと教師らしく振舞ってみて」"
voice "Kaede_0578"
k "「ええっ！？」"
voice "Runa_0111"
rn "「何、イヤなの？」"
voice "Kaede_0579"
k "「め、滅相もございません……」"
"瑠奈さんにギロっと鋭い視線を浴びせられて、私は竦み上がってしまった。"
"どうしてか、だんだんと変な方向に進んでいるような気がするわ……ああ。"
voice "Runa_0112"
rn "「先生も、立派な教え子役、頼むわよ」"
voice "Takako0144"
t "「え、ええ……」"


#※EV059
scene bg EV59
with Dis



voice "Kaede_0580"
k "「えっ、ええと……じゃあ、これから授業を始めます」"
voice "Sara_0569"
sr "「きゃあああああんっ、いいよぉ、楓ちゃん」"
voice "Runa_0113"
rn "「ちょっと、静かにして……じっくり楽しみましょう」"
voice "Kaede_0581"
k "「ま、まずは出席を取ります……墨廼江貴子さん」"
voice "Takako0145"
t "「は、はい」"
voice "Runa_0114"
rn "「むふふふ♪」"
voice "Sara_0570"
sr "「先生、私の名前も呼んで下さい～っ」"
voice "Kaede_0582"
k "「ええと、北嶋紗良さん」"
voice "Sara_0571"
sr "「は～いっ、先生、今日も一日、頑張りましょうねっ」"
voice "Kaede_0583"
k "「え、ええ……そうね」"
voice "Sara_0572"
sr "「あっ、ところで先生は恋人いるんですか～」"
voice "Kaede_0584"
k "「えっ！？　いっ、いますけど……」"
voice "Sara_0573"
sr "「それって……どんな人ですか～？」"
voice "Kaede_0585"
k "「はっ？　これって、教師の勉強に関係あるの！？」"
voice "Runa_0115"
rn "「わかってないわね。大アリよ。学生とコミュニケーションを上手く取るのも、教師の務めなのよ」"
"瑠奈さんの言葉には、妙に説得力がある。"
"でも、上手く言いくるめられているみたい。"
voice "Kaede_0586"
k "「それはそうかも、だけど……」"
voice "Sara_0574"
sr "「先生、私の質問に答えて下さいっ！　どんな人なんですかっ？」"
voice "Kaede_0587"
k "「そ、そうね……とても無邪気で、たまに子どもっぽくて、でも芯はしっかりしている人よ」"
voice "Sara_0575"
sr "「そうなんですか～、先生はその人のことが、とっても好きなんですねっ」"
voice "Kaede_0588"
k "「……ええ、そうね」"
voice "Sara_0576"
sr "「どのくらい好きなんですか～？」"
voice "Kaede_0589"
k "「ど、どのくらい？　そうね、このくらい……かな？」"
"私は、腕で大きな輪を作った。"
voice "Sara_0577"
sr "「えぇぇっ、それだけですか？」"
"紗良が不満そうに、唇を曲げている。"
voice "Kaede_0590"
k "「ええっ？　じゃあ、このくらい……かな？」"
"私はバッと大きく、両手を広げた。"
voice "Sara_0578"
sr "「ほうほう、参考になります。メモメモ……」"
voice "Kaede_0591"
k "「何の参考よ！？」"
voice "Runa_0116"
rn "「はいはーいっ、墨廼江さんの方も、恋人はいるんですかっ？」"
voice "Takako0146"
t "「えっ、私！？」"
voice "Runa_0117"
rn "「そうです、今後の勉強の為にも、聞かせて下さい」"
voice "Takako0147"
t "「何の勉強なの！？　いえ、まあ……居ますけれど……」"
voice "Runa_0118"
rn "「ほうほう……それは一体どんな方ですか？」"
voice "Takako0148"
t "「どんなって……小柄で、ワガママで我が強いわね。良いところもいっぱいあるけれど」"
voice "Runa_0119"
rn "「良いところとは？　その恋人の好きなところを教えて下さい」"
voice "Takako0149"
t "「それは……大人びた中にも、年相応のところもあって……可愛いな、と思うわ」"
voice "Runa_0120"
rn "「ここで、ちょっと突っ込んだ質問をさせて貰います。夜の生活はどんな感じですか？」"
voice "Takako0150"
t "「そ、そんなの……言わせないでよ、恥ずかしいっ！！」"
voice "Kaede_0592"
k "「貴子先生……思ったんですけれど、これって……」"
voice "Takako0151"
t "「ええ、勉強じゃなくて、ただ瑠奈がやりたいことをやってるだけね」"
voice "Kaede_0593"
k "「つまり、私たちは……」"
voice "Takako0152"
t "「ええ……完全にハメられたのよ」"
voice "Sara_0579"
sr "「先生っ、勉強でわからないところがあったんです。手取り足とり腰とり、教えて下さい{image=image/exch001.png}」"
voice "Runa_0121"
rn "「わたしもわたしも～」"
voice "Kaede_0594"
k "「もうっ、２人とも……」"
voice "Takako0153"
t "「いい加減にしてぇ～っ！！」"


#**青空
scene bg bg42a
with Dis



"……こうして結局、まともな勉強はこれっぽっちもできなかったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**貴子の部屋・夜
scene bg bg26c
with Dis



#mes on
#system on


show char tta03s2
with dis



voice "Takako0154"
t "「楓さん……瑠奈のせいで、あんな……ゴメンなさいね」"
"帰り際、貴子先生が申し訳なさそうに謝ってくれた。"


show char tka03s2 at left
show char tta03s2 at right as r
with dis



voice "Kaede_0595"
k "「いいえっ、貴子先生こそ、お疲れ様でした……」"
"私もぐったりだけれど、貴子先生も相当、疲れている。"
"私たちは、お互いの苦労をいたわりあった。"
voice "Kaede_0596"
k "「じゃあ、私たちはこれで失礼します」"


#allClear:
hide char tka03s2 at left
hide char tta03s2 at right as r
#lastBG:
#scene bg bg26c
show char tsa02s2
with dis



voice "Sara_0580"
sr "「瑠奈ちゃん、また宜しくねっ♪」"


show char tsa02s2 at left
show char tru01s2 at right as r
with dis



voice "Runa_0122"
rn "「もちろんよ。後で写真のデータ送るわ」"
voice "Sara_0581"
sr "「楽しみにしているね{image=image/exch001.png}」"


#allClear:
hide char tsa02s2 at left
hide char tru01s2 at right as r
#lastBG:
#scene bg bg26c
show char tka03s2
with dis



voice "Kaede_0597"
k "「もう……紗良ったら」"


show char tka03s2 at left
show char tta03s2 at right as r
with dis



voice "Takako0155"
t "「ヘンに結託しているわね……あの２人」"
"もしかしたら紗良と瑠奈さん、タイプが全然違うようで、実はかなり気が合うのかも……"


show char tta01s2 at right as r
with dis



voice "Takako0156"
t "「じゃあ、また何か知りたいことがあったら、いつでも連絡してね」"


show char tka01s2 at left
with dis



voice "Kaede_0598"
k "「はいっ、お世話になります。お邪魔しました」"

hide char tka01s2 at left
hide char tta01s2 at right as r
show char tsa01s2 at sleft as l
show char tka01s2
show char tta01s2 at sright as sr
with dis



voice "Sara_0582"
sr "「お邪魔しました～」"


#allClear:
hide char tsa01s2 at sleft as l
hide char tka01s2
hide char tta01s2 at sright as sr
#lastBG:
#scene bg bg26c
with dis


"こうして私たちは、貴子先生と瑠奈さんの部屋を後にしたのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・夜
scene bg bg08c
with Dis



#mes on
#system on


show char tsa02s2
with dis



voice "Sara_0583"
sr "「あ～、楽しかった♪　ねっ、楓ちゃん」"


show char tka03s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0599"
k "「そうかしら……」"


show char tsa03s2 at right as r
with dis



voice "Sara_0584"
sr "「楓ちゃん、目がすわっているよ？」"
voice "Kaede_0600"
k "「何だか私も貴子先生も、良いように操られていた気がするけれど……」"
voice "Sara_0585"
sr "「え～っ、気のせいだよ」"
voice "Kaede_0601"
k "「そうかしら……」"


show char tsa02s2 at right as r
with dis



voice "Sara_0586"
sr "「そうだよ、うんうん。また女教師ごっこしようね♪」"


show char tka08s2 at left
with dis



voice "Kaede_0602"
k "「もう、しないわよ」"
"私はキッパリ、即答した。"
"ああいうのはもう、こりごりだわ。"


show char tsa03s2 at right as r
with dis



voice "Sara_0587"
sr "「回答早っ、あーん紗良はまた楓ちゃんの女教師姿見たいよ～」"
voice "Kaede_0603"
k "「結局、本音はそこなのね」"


show char tsa01s2 at right as r
with dis



voice "Sara_0588"
sr "「ぎくっ……バレちゃしょうがないですなぁ。とってもハマってたから、個人的にまた、女教師のコスプレして欲しいな{image=image/exch001.png}」"


show char tka09s2 at left
with dis



voice "Kaede_0604"
k "「しないわ、しないっ、ぜーったいしないんだからっ！！」"


show char tsa04s2 at right as r
with dis



voice "Sara_0589"
sr "「えーっ！？」"
"心底残念な声を上げる紗良に、私はプンプンしながら帰り道を歩いたのだった。"


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
jump S096



