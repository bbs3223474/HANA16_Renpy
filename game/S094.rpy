#「紗良、楓が心配で……」

label S094:
$ save_name = "◇紗良、楓が心配で……"


#//紗良視点
#//紗良の立ちキャラは制服で

#♂MP01
play music "sound/BGM01.ogg"


#**繁華街
scene bg bg17a
with Dis



#mes on
#system on


show char tsa03f2
with dis



voice "Sara_0503"
sr "「あーん、楓ちゃん、どこ～？」"
"紗良は街中を歩いて、楓ちゃんを捜していた。"
"急に仕事がオフになったから、楓ちゃんと遊ぼうと思ったのに。"
"学校に戻ったら、楓ちゃんはすでにおらず。"
"メールを送っても、返信はナシ。"
voice "Sara_0504"
sr "「ふえ～ん、タイミング悪すぎだよ。誰かと遊びに行っちゃったのかな？」"
"楓ちゃんは最近よく、友達と遊んでいることが多い。"
"楓ちゃんも仕事が忙しくて、学校をお休みすることが多いから、友達との時間も欲しいだろう。"
"それは全然良いんだけど。"


show char tsa09f2
with dis



voice "Sara_0505"
sr "「もぉ、紗良ともいーっぱい遊んで欲しいっ！」"
"折角のオフなのに！　"
"ワガママだって分かっているけど！！"


show char tsa08f2
with dis



voice "Sara_0506"
sr "「誰かと会ってるとしたら……多分、カフェあたりじゃないかなぁ」"
"そう思って、よくミカ女の皆と行くカフェを目指した。"


show char tsa02f2
with dis



voice "Sara_0507"
sr "「おお……ビンゴっ！！」"
"予想通り、楓ちゃんを発見した。"
"外からガラス越しに捉えたのは、まさしく楓ちゃんの姿だった。"


show char tsa03f2
with dis



voice "Sara_0508"
sr "「あれっ、一緒にいるのは……貴子先生？」"
"楓ちゃんの向かいには、貴子先生が座っていた。"
"やけに話が盛り上がっているみたい……楽しそう。"
voice "Sara_0509"
sr "「何を話してるんだろう……気になるなぁ」"


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


show char tsa01f2
with dis



voice "Sara_0510"
sr "「……こっそり……こっそり、とね」"


with dis


"２人には見つからぬよう、カフェにこっそり入店した。"
"徐々に近づいていくと、微かに声が聞こえてきて……"


show char tka02p
with dis



voice "Kaede_0521"
k "「貴子先生……私、今日貴子先生に会えて、良かったです」"


show char tka02p at left
show char tta02p at right as r
with dis



voice "Takako0121"
t "「まあ、私も、楓さんと会えて、すごく嬉しいわ」"
"何の話をしているんだろう？"


#allClear:
hide char tka02p at left
hide char tta02p at right as r
#lastBG:
#scene bg bg36a
show char tsa08f2
with dis



voice "Sara_0511"
sr "「何だか……アヤシイ……」"
"でも、貴子先生には瑠奈ちゃんがいるんだから、そんなことは万が一にもあり得ないよね？"
"楓ちゃんも、真面目で誠実だから、浮気なんてしないだろうし……"


show char tsa03f2
with dis



voice "Sara_0512"
sr "「うーっ、でも楓ちゃんは魅力的だから、時々紗良は不安になっちゃうけど……」"
"更にばれないよう距離を縮めて、すぐ近くの席に着く。"
"声がはっきり、聞きとれる距離だ。"


show char tka01p
with dis



voice "Kaede_0522"
k "「で……教師になる方法、もっと教えて下さい」"


show char tsa03f2
with dis



voice "Sara_0513"
sr "「教師？　教師って何？？」"
"紗良の頭は一瞬、真っ白になった。"
"だって、楓ちゃんは……その衝撃に、紗良は思わず立ち上がってしまった。"


show char tsa09f2
with dis



voice "Sara_0514"
sr "「楓ちゃんは、アイドルになるのっ！！」"


show char tsa09f2 at sleft as l
show char tka04f2
show char tta04s2 at sright as sr
with dis



voice "Kaede_0523"
k "「さ、紗良！？」"
voice "Takako0122"
t "「紗良さん！？」"
voice "Sara_0515"
sr "「ね、そうでしょう、楓ちゃん！　楓ちゃんは、この世で一番のアイドルになるんでしょう！？」"


show char tka03f2
with dis



voice "Kaede_0524"
k "「この世で一番って、何？」"


show char tta03s2 at sright as sr
with dis



voice "Takako0123"
t "「そ、それは、壮大な夢ね……」"
voice "Kaede_0525"
k "「違います、貴子先生。そんなに真面目に受け取らないで下さいっ」"
voice "Sara_0516"
sr "「楓ちゃんったら、紗良に熱く誓ったじゃない。あれって嘘だったの！？」"


show char tka08f2
with dis



voice "Kaede_0526"
k "「違うわ、私がなるのは、紗良のマネージャーでしょう！」"


show char tsa03f2 at sleft as l
with dis



voice "Sara_0517"
sr "「あっ……そうだったね」"
"なんだか混乱して、変なこと口走っちゃった。"


show char tka01f2
with dis



voice "Kaede_0527"
k "「もう、紗良ったら……で、どうしてここにいるの？」"


show char tta01s2 at sright as sr
with dis



voice "Takako0124"
t "「紗良さんもここに来ていたのね。気付かなかったわ」"
voice "Sara_0518"
sr "「そ、それは……」"
"しまった、後先考えずに、立ち上がっちゃった。"
"こうなったら、正直に言うしかないか……"
voice "Sara_0519"
sr "「今日、オフになったから、楓ちゃんと遊びたいなって思って、メール入れたんだけど、返事が無くて」"
voice "Sara_0520"
sr "「でね、多分カフェ辺りにいるんじゃないかなって思ったら、楓ちゃんを発見して……」"
voice "Kaede_0528"
k "「あっ、さっきのメール、もしかして紗良だったの？」"
"楓ちゃんがカバンから携帯を取り出して、メールをチェックする。"
"ああ、気付いてなかったんだ……"


show char tka03f2
with dis



voice "Kaede_0529"
k "「あっ、やっぱり……ゴメンね、私見てなくて……」"


show char tsa01f2 at sleft as l
with dis



voice "Sara_0521"
sr "「ううん、全然良いよ」"


show char tka01f2
with dis



voice "Kaede_0530"
k "「話に夢中だったのよ」"


show char tsa03f2 at sleft as l
with dis



voice "Sara_0522"
sr "「あっ、そうだ楓ちゃん、教師になりたいって、どういうこと？？」"
voice "Sara_0523"
sr "「紗良にも事務所にも、マネージャーになりたいって言ったじゃない」"
"ついこの間、そう言ってくれたばっかりだったのに……"
voice "Kaede_0531"
k "「それがね、紗良……今日、貴子先生と話していて、ちょっと思い出したの」"
voice "Sara_0524"
sr "「ん、何を？」"
voice "Kaede_0532"
k "「私、小さい頃、教師になりたかったんだって……」"
voice "Sara_0525"
sr "「えっ、そうなの？　そんなの初めて聞いたよ？」"
voice "Kaede_0533"
k "「私も、初めて話したと思うわ」"
"楓ちゃんが教師だなんて……なんか、似合い過ぎてる！"
voice "Sara_0526"
sr "「えっ、でも……それが、何で……」"
voice "Kaede_0534"
k "「その話をしていたら、貴子先生が両方目指してみたら良いんじゃないかって……」"
voice "Kaede_0535"
k "「だから私、貴子先生に色々教えて貰って、両方を目指すことにしたの」"
"両方を目指すなんて……そんなこと、可能なのかな？"
"てっきり楓ちゃんは、マネージャー１本を目指すんだと思っていたのに……"
voice "Sara_0527"
sr "「楓ちゃんは、紗良専属のマネージャーになるんじゃなかったの？」"
"みっともないかもしれないけれど、不満たらたらの言葉をもらした、その時……"

#//瑠奈の立ちキャラは制服で
#allClear:
hide char tsa03f2 at sleft as l
hide char tka01f2
hide char tta01s2 at sright as sr
#lastBG:
#scene bg bg36a
show char tru01s2
with dis



voice "Runa_0073"
rn "「別にいいじゃない、将来の選択肢は多いに越したことはないわ」"
"急に聞こえた声に、みんなびっくりした。"


show char tsa04f2 at sleft as l
show char tka04f2
show char tta04s2 at sright as sr
with dis



voice "Takako0125"
t "「る、瑠奈っ！？」"
voice "Sara_0528"
sr "「い、いつの間にっ！？」"
voice "Kaede_0536"
k "「全然、気が付かなかったわ……」"
"いきなり現れたのは、なんと瑠奈ちゃんだった。"
"全然気付かなかった、気配すら感じなかったよ。"
"でも、なんでいるの！？"


#allClear:
hide char tsa04f2 at sleft as l
hide char tka04f2
hide char tta04s2 at sright as sr
#lastBG:
#scene bg bg36a
show char tru03s2
with dis



voice "Runa_0074"
rn "「まあ、それは……気にしないことね」"


show char tta04s2 at left
show char tru03s2 at right as r
with dis



voice "Takako0126"
t "「いや、気になるわよ！？」"

hide char tta04s2 at left
hide char tru03s2 at right as r
show char tsa01f2 at sleft as l
show char tta04s2
show char tru03s2 at sright as sr
with dis



voice "Sara_0529"
sr "「うんうん、気になるっ」"


show char tka01f2 at sleft as l
show char tsa01f2
show char tta04s2 at sright as sr
with dis



voice "Kaede_0537"
k "「びっくりしたわ……」"


#allClear:
hide char tka01f2 at sleft as l
hide char tsa01f2
hide char tta04s2 at sright as sr
#lastBG:
#scene bg bg36a
show char tru01s2
with dis



voice "Runa_0075"
rn "「とにかくわたしは、マネージャーと教師、両方を目指すことには賛成よ」"


show char tsa03f2 at left
show char tru01s2 at right as r
with dis



voice "Sara_0530"
sr "「なんで？」"
voice "Runa_0076"
rn "「何でも……よ」"
voice "Sara_0531"
sr "「うう～……」"
"何となく瑠奈ちゃんのオーラに負けて、言い返せない……情けない。"
voice "Runa_0077"
rn "「とにかく、これで３対１ね」"


show char tta08s2 at left
with dis



voice "Takako0127"
t "「こら、瑠奈、３対１って……」"
voice "Runa_0078"
rn "「だって、事実じゃない」"


#allClear:
hide char tta08s2 at left
hide char tru01s2 at right as r
#lastBG:
#scene bg bg36a
show char tsa03f2
with dis



voice "Sara_0532"
sr "「うう……っ」"


show char tka03f2 at left
show char tsa03f2 at right as r
with dis



voice "Kaede_0538"
k "「紗良……わたしがマネージャーと教師を目指すことには、反対なの？」"
"楓ちゃんが、不安げな表情で紗良を見つめてくる。"
"うう、その顔には弱いのに……"
"正直、不満だけど、場の流れに負けた。"
"こんなの勝てるわけがないよぉ～"
voice "Sara_0533"
sr "「……不満じゃ、ないけど……」"


show char tka02f2 at left
with dis



voice "Kaede_0539"
k "「本当！？　紗良も私の夢を応援してくれるのねっ！？」"
"目を輝かせる楓ちゃんにそう言われては、もう、うんと頷くより他はなかった。"
voice "Sara_0534"
sr "「……応援、しているよ……」"


#※CU17
#allClear:
hide char tka02f2 at left
hide char tsa03f2 at right as r
#lastBG:
#scene bg bg36a
show char CU17
with dis



voice "Kaede_0540"
k "「紗良……ありがとうっ！」"
voice "Sara_0535"
sr "「か、楓ちゃんっ」"

#♀SE075
play sound "sound/SE075.ogg"


"楓ちゃんがギュッと抱きついてくる。"
"人前で、楓ちゃんがこんなに大胆になるなんて、すごく珍しい。"
"楓ちゃんからのハグは、嬉しいけれど……今の気分は複雑だった。"
voice "Takako0128"
t "「理解のある恋人で良かったわね、楓さん」"
voice "Kaede_0541"
k "「はいっ、貴子先生っ」"
voice "Runa_0079"
rn "「理解のある恋人、ねぇ……」"
voice "Sara_0536"
sr "「うぅ……」"
"瑠奈ちゃんが、含みのある目で見つめてくる。"
"ちょっと天然な楓ちゃんや貴子先生に比べて、この子は本当に鋭い。"
"とても年下とは思えないよぉ～"


#**カフェ・昼
show char tka02f2
with dis



voice "Kaede_0542"
k "「紗良……私、頑張るからねっ」"


show char tka02f2 at left
show char tsa01f2 at right as r
with dis



voice "Sara_0537"
sr "「う、う～ん……紗良はいつだって、楓ちゃんの味方だからね」"
voice "Kaede_0543"
k "「本当に？　ありがとう」"
voice "Sara_0538"
sr "「だって、紗良は楓ちゃんの一番の理解者なんだから」"
voice "Kaede_0544"
k "「うんうんっ、紗良ならそう言ってくれるって、信じていたわ」"
voice "Sara_0539"
sr "「そうそう……紗良が楓ちゃんの夢を反対なんてするワケないじゃん」"
voice "Kaede_0545"
k "「私、こんなに良い恋人がいて、幸せよ」"
voice "Sara_0540"
sr "「……紗良も……だよ」"
"楓ちゃんが感動のあまり、目を潤ませている。"
"そんなのを見てしまったら、もう後には引けない。"
"気持ちはちょっぴり……ううん、かなり不満で溢れているけど。"


show char tru02s2 at left
show char tta02s2 at right as r
with dis



voice "Runa_0080"
rn "「この件は、めでたしめでたしね」"
voice "Takako0129"
t "「そうね、良かったわね～」"
"外野の２人は、のほほんとしている。"
"やっぱり、何だか複雑な気分……"


#**カフェ・昼


voice "Runa_0081"
rn "「じゃあ早速、ウチで練習しましょうよ」"


#allClear:
hide char tru02s2 at left
hide char tta02s2 at right as r
#lastBG:
#scene bg bg36a
show char tsa03f2
with dis



voice "Sara_0541"
sr "「はっ！？」"
"ニヤニヤする瑠奈ちゃんの提案に、ポカンとしてしまった。"
"『ウチで練習』って……一体、どういうこと！？"


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
jump S095



