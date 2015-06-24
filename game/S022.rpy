#「たまにはお仕事も……」

label S022:
$ save_name = "◇たまにはお仕事も……"


#※ここは楓視点です

#**海岸通り・昼
scene bg bg39a
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


"昨年、ベストカップルに選ばれて、イベント実行委員の仕事を始めた時は。"
"みんなで合宿をしたり準備をしたりと、時間が過ぎるのを早く感じるほど、楽しかった。"
"だけど、今年に入ってから……"
"紗良と一緒にしてる仕事の方が忙しくて、学校だって休みがち。"
"ベストカップルのみんなともなかなか会えなくて、少し寂しかった。"
"だから、夏休みに入って、麗奈先生から誘いの電話が来た時は、すごく嬉しくて。"
"紗良やマネージャーと相談して、何とかスケジュールをやりくりしてもらって、バカンスに参加させてもらうことになった。"


show char tma02m
with dis



voice "Mai_0146"
ma "「紗良ちゃんも楓さんも、お休み取れて良かったですね」"


show char tma02m at left
show char tyu03m at right as r
with dis



voice "Yuuna_0129"
y "「本当に、会えないままだったから気になっていたのよ。忙しかったんじゃない？」"

hide char tma02m at left
hide char tyu03m at right as r
show char tma02m at sleft as l
show char tyu03m
show char tka01m at sright as sr
with dis



voice "Kaede_0058"
k "「ここに来るために、ギリギリまで仕事はあったけれど……我慢出来ました」"
voice "Mai_0147"
ma "「えらいなぁー、さすが楓さんだわ」"
voice "Kaede_0059"
k "「そんなことないです」"
"紗良と比べたら、私のほうが仕事は少なかったから。"
"褒められてしまうと、どんな顔をしていいかわからなくなる。"
voice "Mai_0148"
ma "「でも、久しぶりに３年生会、全員そろったわね♪」"


show char tyu01m
show char tka03m at sright as sr
with dis



voice "Kaede_0060"
k "「あ、そうですね……いつも私の都合でいけなくてすいません」"
"３年生会……昨年までは、２年生会だった集まり。"
"別名『恋愛相互応援の為の会』。"
"恋人とのことで溜まったストレスを、一緒に遊んで発散したりする会で。"
"昨年は紗良のことで、随分とお世話になったのよね。"
"最近は仕事が忙しくて、なかなか集まりに顔を見せられなかった。"
voice "Yuuna_0130"
y "「そんなことないわ、私だって委員の方で、時間がとれなかったりしているし」"
voice "Mai_0149"
ma "「わたしも玲緒の面倒、見ないといけないし……ふふっ」"
"２人とも優しいから、そんな風に言ってくれるけど。"
"私がドタキャンしてしまうことも多かったので。"
"こうして今、みんなで何の心配もせずに会えて、本当に良かった。"


show char tma01m at sleft as l
with dis



voice "Mai_0150"
ma "「普段生活してる場所から遠く離れているせいか、ここって時間の流れがゆっくりよね～」"
voice "Yuuna_0131"
y "「リフレッシュするには、最適よね。あっ、ついでにホテルにあったエステにみんなで行かない？　もっと、リフレッシュ出来そうよ」"
voice "Kaede_0061"
k "「エステ……私、行ったことないわ」"
voice "Mai_0151"
ma "「わたしもだけど、みんなと一緒ならいいかも」"


show char tka01m at sright as sr
with dis



voice "Kaede_0062"
k "「そうね」"
voice "Yuuna_0132"
y "「じゃあ帰ったら、予約しておきましょう」"
"のんびり過ごす……こんなのって、本当に久しぶり。"
"楽しくお喋りしてると、紗良たちが海から上がってきた。"


#allClear:
hide char tma01m at sleft as l
hide char tyu01m
hide char tka01m at sright as sr
#lastBG:
#scene bg bg39a
show char tsa01m
with dis



voice "Sara_0101"
sr "「楓ちゃん～♪　楽しそうだね、何の話してたの？」"


show char tka02m at left
show char tsa01m at right as r
with dis



voice "Kaede_0063"
k "「ふふふ、何でしょうね」"


show char tsa08m at right as r
with dis



voice "Sara_0102"
sr "「あっ、ずるいー」"
"別に内緒にするつもりはないけれど、なんとなくそう言ったら、紗良が子供のように悔しがる。"
voice "Sara_0103"
sr "「もぉ……じゃあ麻衣さま、教えて？」"


show char tma01m at left
with dis



voice "Mai_0152"
ma "「そうよ、３年生会だけの秘密よ。２年生会には言えないわね」"
"麻衣さんも面白がってのってくる。"
"ちょうど紗良の隣には、璃紗さんと七海さんもいて、ここに『２年生会』と『３年生会』が一同に揃っていた。"


#allClear:
hide char tma01m at left
hide char tsa08m at right as r
#lastBG:
#scene bg bg39a
show char tsa03m
with dis



voice "Sara_0104"
sr "「がーん、楓ちゃんたちが秘密を作ってるなんて……璃紗ちゃん、こっちでも何か秘密を作ろうよ」"


show char tsa03m at left
show char tri03m at right as r
with dis



voice "Risa_0668"
r "「秘密って……」"
"璃紗さんが苦笑している。"
voice "Risa_0669"
r "「七海さん、何かありますか？」"


show char tna03m at sleft as l
show char tsa03m
show char tri03m at sright as sr
with dis



voice "Nanami0243"
n "「急に、何かと言われても……」"


#allClear:
hide char tna03m at sleft as l
hide char tsa03m
hide char tri03m at sright as sr
#lastBG:
#scene bg bg39a
show char tyu01m
with dis



voice "Yuuna_0133"
y "「あら、七海は私に秘密を持ってるの？　教えて欲しいわ、ここに書き記すから」"
"優菜さんがどこから出したのか、ちらっとノートを見せる。"
"何かしら、あれ？"


show char tyu01m at left
show char tna04m at right as r
with dis



voice "Nanami0244"
n "「お、お姉さま、それ、もしかして……」"
voice "Yuuna_0134"
y "「もちろん七海ちゃん手ちょ……」"


show char tna09m at right as r
with dis



voice "Nanami0245"
n "「わーーーーっ！！」"
"七海さんが大声をだして、ビーチが騒然となる。"


show char tma03m
with dis



voice "Mai_0153"
ma "「七海ちゃん……どうしたのかしら？」"


show char tma03m at left
show char tri03m at right as r
with dis



voice "Risa_0670"
r "「さ、さあ……あれって、前に美夜が言っていた、秘密ノートじゃ……」"
"璃紗さんも何か知ってるみたいだけど。"
"口には出さなかった。"
"何でこんな騒ぎになったのかわからないけど、楽しいわ。"


#allClear:
hide char tma03m at left
hide char tri03m at right as r
#lastBG:
#scene bg bg39a
show char tka02m
with dis



voice "Kaede_0064"
k "「ふふふっ」"
"口元から笑みがこぼれていく。"


show char tka02m at left
show char tsa01m at right as r
with dis



voice "Sara_0105"
sr "「楓ちゃん……楽しそう」"
voice "Kaede_0065"
k "「ええ、楽しいわ。紗良もでしょう？」"


show char tsa02m at right as r
with dis



voice "Sara_0106"
sr "「紗良は楽しそうな楓ちゃんをみているだけで、もっと嬉しくなるよ」"


show char tka01m at left
with dis



voice "Kaede_0066"
k "「そうなの？」"
voice "Sara_0107"
sr "「うん、紗良も楓ちゃんみたいにもっと遊ぶよぉー、璃紗ちゃん七海ちゃん、また泳ごうよ」"


hide char tsa02m at right as r
with dis


"そう言って、紗良たちはまた海に入っていく。"
voice "Kaede_0067"
k "「元気ね、あの子たちは」"


show char tka01m at left
show char tma03m at right as r
with dis



voice "Mai_0154"
ma "「楓さん、年寄りっぽいわよ。わたしたちと一つしか違わないんだから」"

hide char tka01m at left
hide char tma03m at right as r
show char tka01m at sleft as l
show char tma03m
show char tyu01m at sright as sr
with dis


voice "Yuuna_0135"
y "「そうよ、私たちも元気よく泳いできましょう」"
voice "Kaede_0068"
k "「ええ」"
"そうね。"
"バカンスをもっと、満喫しないとね。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチテラス・昼
scene bg bg40a
with Dis



#mes on
#system on


"海で遊んだ後。"
"ビーチで一休みしていると、墨廼江先生がやってきた。"


show char tta01m
with dis



voice "Takako0034"
t "「ね、隣座って、いいかしら」"


show char tka01m at left
show char tta01m at right as r
with dis



voice "Kaede_0069"
k "「はい、どうぞ」"


#※EV008
#allClear:
hide char tka01m at left
hide char tta01m at right as r
#lastBG:
#scene bg bg40a
scene bg EV08
with Dis



"海の方ではお互いのパートナーである、紗良と瑠奈さんがはしゃいでる。"
voice "Kaede_0070"
k "「瑠奈さん、楽しそうですね」"
voice "Takako0035"
t "「麗奈先輩もいるし、楓さんたちも来てくれたから、最近すごくアクティブなのよ。前は何かあるとすぐ、部屋でゲームばっかりだったんだけどね」"
voice "Kaede_0071"
k "「そういえば、墨廼江先生たちの部屋、ゲームがいっぱいありましたよね」"
"附属の先生である墨廼江先生とは、ベストカップルの合宿で会うまでは、面識はなかったけれど。"
"いろいろ話をしていくうちに、結構気が合って。"
"最近はプライベートでも会ったり、墨廼江先生の家にも遊びに行ったりするくらいの仲に進展している。"
"年上の知り合いは、仕事関係が多いけれど。"
"墨廼江先生はそれらの人たちとは、まったく違って。"
"一緒にいて、安心するというか、気が楽になれるというか……"
"似たもの同士なのかもしれないわね。"
voice "Takako0036"
t "「こうして、お互い水着でいると……思い出すことがあるわね」"
voice "Kaede_0072"
k "「あ、あれですね……」"
"思わず、顔が赤くなる。"
"前に、私たち二人で水着の撮影会をしたことがあった。"
"私と紗良は仕事で、墨廼江先生たちは休暇で、リゾートホテルに来ていたら。"
"そこのエロっぽいカメラマンの目に留まって、やたらときわどい水着で写真を撮らされたりしたのよね。"
"それに紗良と瑠奈さんが、めちゃくちゃ興奮しちゃって。"
"撮影後、すごく恥ずかしいことになったような……"
voice "Kaede_0073"
k "「あの時の写真……私、とても見れません」"
voice "Takako0037"
t "「私もよ。なのに瑠奈ったら、大きく引き延ばして部屋に貼ろうとしたのよ」"
voice "Kaede_0074"
k "「それは……なんていうか、愛されてますね」"
voice "Takako0038"
t "「楓さん、そういう問題じゃないわ」"
voice "Kaede_0075"
k "「ふふふっ」"
"２人で話をしていると、紗良たちがこちらに向かって手を振っている。"
voice "Takako0039"
t "「２人とも、はしゃいじゃってるわね」"
voice "Kaede_0076"
k "「ええ……楽しそう」"
"私たちも大きく手を振り返す。"
voice "Takako0040"
t "「でも、お互い……」"
voice "Kaede_0077"
k "「大変な相方を持っていますね」"
voice "Takako0041"
t "「ねぇぇー」"
"まさかそんな会話をしているとは気づかずに、紗良たちは笑顔でこっちを見ている。"
voice "Takako0042"
t "「瑠奈ったら、校舎が違うのに、すぐに私の受け持ちの教室にまでやってくるのよ」"
"墨廼江先生はやれやれ、といったような表情を浮かべた。"
voice "Takako0043"
t "「今の担任している子たちにまで『お迎えがきましたよ、センセイ』って言われて、冷やかされちゃう」"
"恥ずかしいわと……言いながらも、墨廼江先生はちょっと自慢しているようにも見えた。"
voice "Kaede_0078"
k "「わかります。紗良も急な仕事がある時、わざわざ３年の教室まで来ちゃうんですよ、校門前で待ってればいいのに」"
voice "Takako0044"
t "「楓さんこそ……愛されているじゃない」"
voice "Kaede_0079"
k "「そうかしら……」"
"今度は私の方が、ちょっと得意げになってしまった。"
voice "Takako0045"
t "「………………」"
voice "Kaede_0080"
k "「………………」"
"一瞬の沈黙の後。"
"私たちは愚痴と言う名の、お惚気大会を始めてしまった。"


#※EV008P1
scene bg EV08p1
with Dis



voice "Takako0046"
t "「中等部でも相変わらず女王様キャラは健在みたいだけど、それが似合っちゃうのよね、瑠奈は」"
voice "Kaede_0081"
k "「紗良も最近になって、やっと料理と覚える気にはなったみたいだけど、まだまだなんですよ。それでも私のために、朝食を作ってくれたことがあって」"
voice "Takako0047"
t "「でもね、瑠奈はね……」"
voice "Kaede_0082"
k "「それと、紗良なんですが……」"
"その後も惚気大会は白熱して、いつしか声も大きくなってしまって。"
"それを聞きつけたのか、何事かと海にいた２人が上がってきてしまった。"
voice "Sara_0108"
sr "「楓ちゃんたち、何を話してるの～」"
voice "Runa_0034"
rn "「きっと、わたしの自慢よね♪」"
voice "Sara_0109"
sr "「瑠奈ちゃんは、先生に迷惑いっぱいかけてるでしょう。絶対、紗良の自慢だよ、ねっ？」"
voice "Runa_0035"
rn "「この人、何を言ってるのかしら……おかしいわよね、せんせい♪」"
voice "Sara_0110"
sr "「うううっー、年下なのに生意気だよ、瑠奈ちゃんは」"
voice "Runa_0036"
rn "「年は関係ないわ。わたしがせんせいの自慢のパートナーだって事だけよ」"
"睨み合う２人。"
"こんなとこに来てまで、ケンカしなくてもいいのに。"
voice "Kaede_0083"
k "「ちょっと２人とも、止めて」"
voice "Takako0048"
t "「瑠奈も、すぐに口答えしないの」"
"仲裁に入る、私たち。"
"墨廼江先生たちと仲良くなれたのはいいけれど、仲が良すぎるのかも。"
"紗良と瑠奈さんは度々、こんなケンカを繰り返していた。"
"仲が良すぎて、ある意味困ったものね……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・夜
scene bg bg37c
with Dis



#mes on
#system on


show char tka01f2
with dis



voice "Kaede_0084"
k "「ああ、夜は結構涼しいわね」"
"夜も結構、更けてきたけど。"
"まだ遊び足りなくて、みんなでお喋りしていた。"
"昼間の暑さが半減して、ちょうど良い感じだったから、まだ寝るのはもったいなかった。"


show char tsa01f2
with dis



voice "Sara_0111"
sr "「ねー、明日は何しようか？」"


show char tsa01f2 at left
show char tri01f2 at right as r
with dis



voice "Risa_0671"
r "「ホテルに置いてあったガイドブックを見て決めるのはどうかしら」"

hide char tsa01f2 at left
hide char tri01f2 at right as r
show char tsa01f2 at sleft as l
show char tri01f2
show char tna01f2 at sright as sr
with dis



voice "Nanami0246"
n "「いいですね、海で遊ぶのもいいけど、まだ島の行ってないところも周りたいし」"
voice "Sara_0112"
sr "「ホテル以外の施設も、あるらしいし……んっ？」"


#allClear:
hide char tsa01f2 at sleft as l
hide char tri01f2
hide char tna01f2 at sright as sr
#lastBG:
#scene bg bg37c
with dis


#//SE：携帯着信音
#♀SE012
play sound "sound/SE012.ogg"


"紗良が携帯を取り出す。"
"誰かから、メールかしら？"
"まさか、仕事……じゃないわよね。"


show char tsa08f2
with dis



voice "Sara_0113"
sr "「………あー………」"
"お喋りをやめて、画面を食い入るように眺めている紗良。"
"この真剣な表情……やっぱり……"
"聞く前から何となく、想像できてしまった。"


show char tka03f2 at left
show char tsa08f2 at right as r
with dis



voice "Kaede_0085"
k "「紗良……メール、誰から？」"


show char tsa03f2 at right as r
with dis



voice "Sara_0114"
sr "「マネージャーさんから……」"
"紗良がそっと、画面を見せてくれる。"
"そこには以前から紗良がやりたがっていた、映画出演の仕事の話が書かれていた。"
"さすがに主演ではないけれど、なかなかに良い役だった。"
"普通なら、喜んでしかるべきなのに……紗良は複雑そうな表情をしていた。"
voice "Kaede_0086"
k "「……紗良？」"
voice "Sara_0115"
sr "「んっ……ちょっと席はずすね、楓ちゃん」"


show char tsa03f2 at left
show char tri03f2 at right as r
with dis



voice "Risa_0672"
r "「紗良さん、どうしたの？」"
voice "Sara_0116"
sr "「うん、すぐ戻ってくるから……」"


#allClear:
hide char tsa03f2 at left
hide char tri03f2 at right as r
#lastBG:
#scene bg bg37c
with dis


"バタバタと部屋から出て行く紗良。"

#♀SE064
play sound "sound/SE064.ogg"


show char tka03f2
with dis



voice "Kaede_0087"
k "「何だか様子がおかしいわ……紗良」"
"私は静かに、紗良の後を追いかけていた。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・夜
scene bg bg38c
with Dis



#mes on
#system on


show char tsa03f2
with dis



voice "Sara_0117"
sr "「……そういうことで、お願いします」"
"紗良はすぐ見つかった。"
"人気のない場所で、電話をしていた。"
"終ったら声をかけようかと、思ったけれど……"
"小さく聞こえてきたその内容に、私は仰天してしまった。"


show char tsa08f2
with dis



voice "Sara_0118"
sr "「だから、今回のその仕事、断って欲しいって言ってるじゃない……」"
"あれだけ憧れていた仕事を、紗良はあっさりと断ろうとしている。"
"私の足は勝手に、歩み出てしまっていた。"


show char tka08f2 at left
show char tsa08f2 at right as r
with dis



voice "Kaede_0088"
k "「紗良……あなた、何を言ってるの？」"


show char tsa03f2 at right as r
with dis



voice "Sara_0119"
sr "「か、楓ちゃん、どうして……あっ、はい、また後でかけなおします」"
"慌てて電話を切る、紗良。"
"その紗良に、私は詰め寄る。"
voice "Kaede_0089"
k "「映画の仕事、断るつもりなの？」"
voice "Sara_0120"
sr "「……っ」"


show char tka07f2 at left
with dis



voice "Kaede_0090"
k "「そんなのダメよ、せっかくのチャンスなのに！！」"
voice "Sara_0121"
sr "「だって、急すぎるんだもの。今からすぐ戻ってこいって言われたから……」"


show char tka08f2 at left
with dis



voice "Kaede_0091"
k "「それは仕方ないわ。紗良、あんなにやりたがっていたじゃない」"


show char tsa07f2 at right as r
with dis



voice "Sara_0122"
sr "「……いいの、紗良がいいって言ってるんだから、いいじゃないっ！」"
voice "Kaede_0092"
k "「ダメよっ」"
"思わず声が大きくなってしまって……ちょっとした言い合いになってしまう。"
"そこに止めにはいってくれた人がいた。"


#allClear:
hide char tka08f2 at left
hide char tsa07f2 at right as r
#lastBG:
#scene bg bg38c
show char tta03f2
with dis



voice "Takako0049"
t "「ちょっと２人とも、どうしたの？」"


show char tru03f2 at left
show char tta03f2 at right as r
with dis



voice "Runa_0037"
rn "「それ以上大きな声出したら、周りにまる聞こえよ……みっともないわ」"
"墨廼江先生と……瑠奈さん？"
"２人とも私たちが気になって、様子を見に来てくれたようだった。"
"だけど私はまだ、紗良に言い足りない気持ちでいっぱいだった。"


#allClear:
hide char tru03f2 at left
hide char tta03f2 at right as r
#lastBG:
#scene bg bg38c
show char tka08f2
with dis



voice "Kaede_0093"
k "「その……紗良が、わからず屋なんです」"


show char tka08f2 at left
show char tsa08f2 at right as r
with dis



voice "Sara_0123"
sr "「ひどいよぉ、それは楓ちゃんじゃないっ！」"

hide char tka08f2 at left
hide char tsa08f2 at right as r
show char tta01f2 at sleft as l
show char tka08f2
show char tsa08f2 at sright as sr
with dis



voice "Takako0050"
t "「まぁまぁ……とりあえず、話を聞かせてくれるかしら」"


#allClear:
hide char tta01f2 at sleft as l
hide char tka08f2
hide char tsa08f2 at sright as sr
#lastBG:
#scene bg bg38c
with dis


"そこで私は、今までのいきさつを２人に軽く話した。"


show char tta01f2 at sleft as l
show char tka08f2
show char tsa08f2 at sright as sr
with dis



voice "Kaede_0094"
k "「……というワケで、私は紗良のことを止めているんです。せっかく掴んだチャンスを、こんなことでムダにさせたくないんです」"
voice "Sara_0124"
sr "「紗良はやらないって言ってるのに……楓ちゃんが聞いてくれないんです」"


show char tta03f2 at sleft as l
with dis



voice "Takako0051"
t "「そうなの……困ったわね」"
"おろおろする、墨廼江先生。"
"一方の瑠奈さんは、ふんと軽く鼻を鳴らした。"


show char tru08f2 at sleft as l
with dis



voice "Runa_0038"
rn "「何かと思えば……こんなことだったの」"
voice "Kaede_0095"
k "「こんな、ことって……」"
"あまりに軽々しく言われてしまったので、ちょっとムッとなってしまった。"
"瑠奈さんに、私たちの何がわかるっていうの……？？"
voice "Runa_0039"
rn "「簡単だわ。今、一番大切な事を考えれば良いだけじゃない……それは何なの？」"
"瑠奈さんの問いに、私は答えに詰まる。"
"でも紗良は、すぐにハッキリと答えた。"
voice "Sara_0125"
sr "「はいっ！　楓ちゃんやみんなと、楽しい時間を過ごすこと！」"
voice "Runa_0040"
rn "「……理由は？」"
voice "Sara_0126"
sr "「仕事の機会はまたあるけれど、今この時間は、２度とないから……いつもみんなと会えない分、紗良はこの時間を大切にしたいの、楓ちゃんと一緒に」"


show char tka04f2
with dis



voice "Kaede_0096"
k "「さ……紗良、あなた……」"
voice "Runa_0041"
rn "「次は楓の番よ……今、一番大切な事は何？」"


show char tka03f2
with dis



voice "Kaede_0097"
k "「わ、私は……私は、紗良が大事なの。紗良にとって一番良いと思うことを、してあげたいの」"
"その私の言葉を聞いて、瑠奈さんは小さく笑った……まるで大人のような表情で。"


show char tru01f2 at sleft as l
with dis



voice "Runa_0042"
rn "「だったら答えはもう、出ているじゃない……年上のクセに、そんなこともわからないのね」"


show char tka04f2
with dis



voice "Kaede_0098"
k "「あっ……」"


show char tsa01f2 at sright as sr
with dis



voice "Sara_0127"
sr "「楓ちゃん……紗良、もう一回電話して、ちゃんと断ってくるね」"


show char tka01f2
with dis



voice "Kaede_0099"
k "「……ええ、わかったわ……」"


#allClear:
hide char tru01f2 at sleft as l
hide char tka01f2
hide char tsa01f2 at sright as sr
#lastBG:
#scene bg bg38c
with dis


"もう私は、反対しなかった。"
"そして、紗良の電話が終ると。"
"私達は一緒に、みんなの所へと戻っていったのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・夜
scene bg bg37c
with Dis



#mes on
#system on


show char tna01f2
with dis



voice "Nanami0247"
n "「……あっ、やっと戻って来た～」"


show char tsa03f2 at left
show char tna01f2 at right as r
with dis



voice "Sara_0128"
sr "「ごめんね。で、明日どこに行くか決めた？」"

hide char tsa03f2 at left
hide char tna01f2 at right as r
show char tri01f2 at sleft as l
show char tsa03f2
show char tna01f2 at sright as sr
with dis



voice "Risa_0673"
r "「それだけど……レンタル自転車借りて、この見晴らしのいいところまで行かない？」"


show char tsa02f2
with dis



voice "Sara_0129"
sr "「わぁー、すごい綺麗な景色だねー」"


#allClear:
hide char tri01f2 at sleft as l
hide char tsa02f2
hide char tna01f2 at sright as sr
#lastBG:
#scene bg bg37c
show char tka01f2
with dis



voice "Kaede_0100"
k "「………………」"
"楽しそうな紗良を見つめる、私の傍らには墨廼江先生が立っていた。"


show char tta03f2 at left
show char tka01f2 at right as r
with dis



voice "Takako0052"
t "「ゴメンなさい、楓さん。瑠奈ってああいう性格だから……でもあの子は本気で、二人のことを想って……」"
voice "Kaede_0101"
k "「……はい、わかっています、墨廼江先生」"
"大きな仕事を断ってしまったのは、残念に思う。"


show char tka02f2 at right as r
with dis



voice "Kaede_0102"
k "「でも……本当は私、嬉しいんです」"
voice "Takako0053"
t "「……えっ？」"
voice "Kaede_0103"
k "「紗良が私と過ごす時間や、みんなと過ごす時間を大切に想っていること、そしてここにいるみんなも、私たちのことを大切に思ってくれていることが」"
voice "Kaede_0104"
k "「本当に幸せです、私と紗良は……」"


show char tta02f2 at left
with dis



voice "Takako0054"
t "「あら、私も幸せよ。楓さんやみんなに会えて、本当に良かったわ」"
"２人でしみじみしていると、紗良と瑠奈さんがやってきて、私たちの腕を引っ張った。"


show char tka02f2 at left
show char tsa02f2 at right as r
with dis



voice "Sara_0130"
sr "「楓ちゃん、今からビーチに出て、花火やろうよ！」"


show char tka01f2 at left
with dis



voice "Kaede_0105"
k "「紗良、もうみんなと話はいいの？」"
voice "Sara_0131"
sr "「うん！　明日の予定なら決まったから、それより花火っ！」"


show char tru01f2 at left
show char tta02f2 at right as r
with dis



voice "Runa_0043"
rn "「せんせい、花火だって、すぐ行きましょうよ」"


show char tta01f2 at right as r
with dis



voice "Takako0055"
t "「ええ……でもそろそろ、瑠奈は寝る時間じゃないの？」"
voice "Runa_0044"
rn "「子供扱いしないでよ、せんせいは腰が重いんだから……行くわよっ」"


#allClear:
hide char tru01f2 at left
hide char tta01f2 at right as r
#lastBG:
#scene bg bg37c
with dis


"あなた達が元気すぎるのよ、という言葉を飲み込んで。"
"私と墨廼江先生は、思わず苦笑する。"
"そしてそれぞれのパートナーに誘われるまま、花火をしにビーチに向かった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**海岸通り・夜
scene bg bg38c
with Dis



#mes on
#system on


show char tsa02f2
with dis



voice "Sara_0132"
sr "「花火、楽しかったね、楓ちゃん」"


show char tka02f2 at left
show char tsa02f2 at right as r
with dis



voice "Kaede_0106"
k "「ええ、そぅね。なんだか童心に戻ったみたい」"
voice "Sara_0133"
sr "「瑠奈ちゃんも、すっごく楽しそうだったよ。ねずみ花火と追いかけっこしてたし」"

hide char tka02f2 at left
hide char tsa02f2 at right as r
show char tka02f2 at sleft as l
show char tsa02f2
show char tru03f2 at sright as sr
with dis



voice "Runa_0045"
rn "「あ、あれは……違うわ、花火が勝手に、わたしを追いかけてきたから……ぅぅ」"


show char tsa01f2
with dis



voice "Sara_0134"
sr "「花火は勝手に追いかけたりしないよ。それとも瑠奈ちゃんが子供だから、花火が着いていったのかも」"


show char tru08f2 at sright as sr
with dis



voice "Runa_0046"
rn "「むぅぅっ……」"


show char tka08f2 at sleft as l
with dis



voice "Kaede_0107"
k "「ちょっと紗良、年下の子をからかってはダメでしょう」"


show char tru09f2 at sright as sr
with dis



voice "Runa_0047"
rn "「わたし、子供じゃない！　紗良の方がよっぽど子供でしょ！」"


show char tsa09f2
with dis



voice "Sara_0135"
sr "「なんだってぇ、現役アイドルにケンカ売ろうっていうのね。捕まえてくすぐりの刑よっ！！」"
voice "Runa_0048"
rn "「ふん、紗良なんかに捕まらないわ！」"


#allClear:
hide char tka08f2 at sleft as l
hide char tsa09f2
hide char tru09f2 at sright as sr
#lastBG:
#scene bg bg38c
show char tka03f2
with dis



voice "Kaede_0108"
k "「ちょっと、紗良……もう、紗良の方がよっぽど子供ね。ゴメンなさい、墨廼江先生」"


show char tta02f2 at left
show char tka03f2 at right as r
with dis



voice "Takako0056"
t "「いいんですよ。瑠奈だって本当は、とっても楽しんでいるんですよ」"

hide char tta02f2 at left
hide char tka03f2 at right as r
show char tta02f2 at sleft as l
show char tka03f2
show char trk01f2 at sright as sr
with dis



voice "Rikka_0382"
rk "「そんな風に見えますね……っていうか、ベストカップルの皆さんって本当に、仲が良いんですね」"


show char tta01f2 at sleft as l
with dis



voice "Takako0057"
t "「篠崎さんがそう見えるなら、きっとそうね……みんな、色々あったから」"


show char tka01f2
with dis



voice "Kaede_0109"
k "「でも六夏さんも、もう私たちの一員なのよ。沙雪さんも、ね」"
voice "Rikka_0383"
rk "「そ、そんな……でも、なんか……嬉しい、です」"


show char tka02f2
with dis



voice "Kaede_0110"
k "「これからも、よろしくね、ふふっ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・夜
scene bg bg37c
with Dis



#mes on
#system on


show char tru03f2
with dis



voice "Runa_0049"
rn "「はぁ、はぁ……せんせい、疲れたぁ～」"


show char tta01f2 at left
show char tru03f2 at right as r
with dis



voice "Takako0058"
t "「いつまでも紗良さんと、砂浜で追いかけっこしているからよ」"
voice "Runa_0050"
rn "「せんせい、足と腰、揉んで頂戴」"
voice "Takako0059"
t "「ええ、いいわよ。いくらでもしてあげるわ」"
voice "Runa_0051"
rn "「……なんか、下心とかあるの？」"


show char tta02f2 at left
with dis



voice "Takako0060"
t "「違うわよ。今日のご褒美よ」"
voice "Runa_0052"
rn "「ご褒美もらうような事なんかわたし、してないわよ」"
voice "Takako0061"
t "「ううん、したわ……楓さんと紗良さんに、良いこと言ったでしょ？」"


show char tru05f2 at right as r
with dis



voice "Runa_0053"
rn "「あ、あれくらい……別に、普通よ」"
voice "Takako0062"
t "「ううん、とってもえらかったわ、瑠奈。はい、マッサージ」"


show char tru02f2 at right as r
with dis



voice "Runa_0054"
rn "「ん、んんっ……ああ、気持ちいい♪」"
voice "Takako0063"
t "「うふふ、そう？」"
voice "Runa_0055"
rn "「気持ちよくて……寝ちゃい、そう……ん……ん、ｚｚｚ……」"
voice "Takako0064"
t "「あらあら、瑠奈ったら……本当に寝ちゃったわ」"
voice "Takako0065"
t "「でも今日は、本当にえらかったわ、瑠奈……ふふふっ{image=image/exch001.png}」"


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
jump S023



