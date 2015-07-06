#「『お姉さん』らしくなっていく」

label S117:
$ save_name = "◇『お姉さん』らしくなっていく"


#**沢口家ダイニングキッチン・昼
scene bg bg15a
with Dis



#mes on
#system on


#♂MP07
play music "sound/BGM07.ogg"


"そして、翌日。"
voice "Reo_0872"
re "「じゃあ、いただきまーす」"
voice "Mobmaibrz0020"
mao "「いただきまーすっ！」"
voice "Mobmaisis0014"
mai "「いただきまーす」"
"いつもの休みの日なら、お昼くらいまで布団の中にいたかったけれど。"
"お子様２人に起こされてしまい、ご飯の支度をすることになって。"
"その準備をする間も、落ち着かない子供相手に、何度もケンカになったりしたけれど。"
"不思議と昨日ほどは、腹も立たなくなっていた。"
voice "Mobmaisis0015"
mai "「れおちゃん、ご飯食べたあと、いっしょにあそんでくれる？」"


show char tre01f2
with dis



voice "Reo_0873"
re "「うん、いいわよ。そのかわり、残しちゃだめだからね。ご飯残すと、こわーいお化けが出るのよ」"
voice "Mobmaibrz0021"
mao "「それって、れおみたいなおばけ？　れおってちょーこえーし」"


show char tre08f2
with dis



voice "Reo_0874"
re "「そうよ……食べ物残す、悪い子はいねーがーっ！！」"
voice "Mobmaibrz0022"
mao "「うわーまじこえー」"
voice "Mobmaisis0016"
mai "「はーい、のこさないよ、れおちゃん」"


show char tre02f2
with dis



voice "Reo_0875"
re "「……ふふっ」"
"昨日一日、ずっと一緒にいたせいか、なんだか前よりも仲良しになった気もする。"


show char tre01f2
with dis



voice "Reo_0876"
re "「さぁて、じゃあ今のうちに、メールして……」"
voice "Mobmaibrz0023"
mao "「あーっ、れお、ご飯食べながら、ケータイいじってる」"
voice "Reo_0877"
re "「いいのよ、これは。緊急の呼び出しをかけているだけなんだから」"
"もちろん、ウソだけど。"
voice "Mobmaibrz0024"
mao "「いけないんだー、そういうの、ぎょーぎが悪いって、いつも麻衣おねえちゃんが言ってるよー」"
voice "Reo_0878"
re "「ワタシはもう食べ終わったから、いいのよ」"
"メールの送信を済ませると、携帯をポケットにしまう。"
"まったく、もう……子供はすぐ、あげ足取りをしたがるんだから。"
voice "Reo_0879"
re "「さあ、早く食べるのよ。終わったら遊ぶんでしょう」"
voice "Mobmaisis0017"
mai "「はーい♪」"


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


"そして食事を終えて、かたづけをしている頃。"

#//SE：チャイムの音
#♀SE024
play sound "sound/SE024.ogg"


voice "Reo_0880"
re "「はーい……ふふふっ、来たわね」"
"さっき呼び出した２人が、やってきたようね。"


#**麻衣の部屋・昼
scene bg bg14a
with Dis



show char tre01f2
with dis



voice "Reo_0881"
re "「ここが、麻衣の部屋よ」"


show char tre01f2 at left
show char tri01f2 at right as r
with dis



voice "Risa_1936"
r "「わぁー……おじゃましまーす」"

hide char tre01f2 at left
hide char tri01f2 at right as r
show char tre01f2 at sleft as l
show char tmi01f2
show char tri01f2 at sright as sr
with dis



voice "Miya_1140"
m "「失礼します」"
"安曇璃紗と綾瀬美夜の二人組が、興味深そうに麻衣の部屋を見渡す。"


show char tri03f2 at sright as sr
with dis



voice "Risa_1937"
r "「麻衣さまがいないのに、私たちが勝手に来ちゃって……本当に、いいのかしら？」"
voice "Miya_1141"
m "「別にいいんじゃない。麻衣さまの恋人の、玲緒さまのご招待なんだから」"
voice "Reo_0882"
re "「ええ、気にする必要なんてないわ」"
"ワタシがこの２人を呼んだのには、理由がある。"
"さすがに２日続けて、ワタシ一人でこの子たちの面倒をみるのは、大変だから。"
"少しだけ、手伝ってもらうためだった。"
"それと……あとひとつ。"
voice "Risa_1938"
r "「えっと……玲緒さま、私たちはまず、何からしたらいいですか？」"
voice "Reo_0883"
re "「それはね……おやつ係よ」"
voice "Risa_1939"
r "「えっ！？」"
voice "Reo_0884"
re "「もう少ししたら、子供たちのおやつの時間だから、それを用意してもらいたいの」"


show char tri01f2 at sright as sr
with dis



voice "Risa_1940"
r "「ああ、そういうことでしたら、喜んで準備します。キッチン、お借りしますね」"


hide char tri01f2 at sright as sr
with dis


"いそいそと安曇璃紗は、ダイニングキッチンへと入っていった。"

hide char tre01f2 at sleft as l
hide char tmi01f2
show char tre02f2 at left
show char tmi01f2 at right as r
with dis



voice "Reo_0885"
re "「ふふふっ……うまくいったわ」"
"安曇璃紗はお菓子作りが得意で、イベント実行委員の時もよく、手作りお菓子を持ってきてくれていたから。"
"子供たちの世話を手伝ってもらいながら、美味しいお菓子も食べられるなんて。"
voice "Reo_0886"
re "「ワタシってとっても、頭いいわ♪」"


show char tmi02f2 at right as r
with dis



voice "Miya_1142"
m "「………………ふふっ」"


show char tre03f2 at left
with dis



voice "Reo_0887"
re "「んっ？　綾瀬美夜、なに笑ってるのよ」"


show char tmi01f2 at right as r
with dis



voice "Miya_1143"
m "「いいえ、何でもありません。ところでわたくしは、何をすればいいんでしょうか」"


show char tre01f2 at left
with dis



voice "Reo_0888"
re "「アンタは……そうね、ワタシと一緒に、子供たちの相手よ」"
"自称天才・綾瀬美夜。"
"でも、人とのコミュニケーションは、ワタシと同じく苦手そうよね。"
"きっと子供相手だと、あたふたするに決まってるわ。"


show char tre02f2 at left
with dis



voice "Reo_0889"
re "「いつもクールにすましているけど、あの騒がしい２人に囲まれたら……どんなことになるかしら……ふふふっ、楽しみー」"
voice "Miya_1144"
m "「………………」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**麻衣の部屋・昼
scene bg bg14a
with Dis



#mes on
#system on


show char tre03f2
with dis



voice "Reo_0890"
re "「うぐぐぐっ……」"
"ワタシはがっくりと肩を落とし、ゲームのコントローラーを投げ出した。"


show char tre03f2 at left
show char tmi02f2 at right as r
with dis



voice "Miya_1145"
m "「ふふふっ、玲緒さま、またわたくしの勝ちですね」"
voice "Mobmaisis0018"
mai "「みやおねーちゃん、すごーい♪」"
voice "Mobmaibrz0025"
mao "「これで何連勝だよ、まじつえーなぁー、みやおねえちゃんかっけー！」"
voice "Miya_1146"
m "「このくらい、普通よ……んふふっ」"
voice "Reo_0891"
re "「うにゅ……どうして、こんなことに……」"
"みんなで楽しくゲームをして、最初のうちはとまどっていた綾瀬美夜だけど。"
"その綾瀬美夜はなんと、ゲームで連戦連勝。"
"子供相手なのに、手を抜くってことをしない。"
"負けてばかりの子供たちは悔しがるどころか、ワタシと綾瀬美夜で勝負しろって言い出して。"
"だからワタシは、みじめに連敗中だった。"
"綾瀬美夜の華麗なゲームテクニックに、子供たちは尊敬の眼差しを向けている。"


show char tre03f2 at left
show char tmi01f2 at right as r
with dis



voice "Miya_1147"
m "「どうします、玲緒さま……もう一試合しますか？」"
voice "Reo_0892"
re "「ううううっ」"
voice "Mobmaisis0019"
mai "「れおちゃん、がんばって！」"
voice "Mobmaibrz0026"
mao "「次はきっと、れおも勝てるよ」"
voice "Reo_0893"
re "「あ、ありがと……ぅぅっ」"
"子供たちに応援されている、ワタシって……"


show char tre08f2 at left
with dis



voice "Reo_0894"
re "「というか、どうして綾瀬美夜が『みやおねえちゃん』で、ワタシが『れお』とか『れおちゃん』なのよぉ」"
voice "Mobmaisis0020"
mai "「だって……れおちゃんは、れおちゃんだもん」"
voice "Mobmaibrz0027"
mao "「『れおおねえちゃん』なんて、気持ちわるいよ～」"


show char tre09f2 at left
with dis



voice "Reo_0895"
re "「むきーーーーっ！！」"


show char tmi02f2 at right as r
with dis



voice "Miya_1148"
m "「ふふふふっ、玲緒さま、勝負はもうこれで終わりですか？」"
voice "Reo_0896"
re "「や、やるわよ……今度は勝つわ、ぜったいに！！」"
"綾瀬美夜ったら……嬉しそうに笑っちゃって。"
"でもここでまた負けたら、子供たちの『綾瀬美夜株』はどんどん上がって。"
"逆にワタシの株は、ますます大暴落になりそうな……"


#allClear:
hide char tre09f2 at left
hide char tmi02f2 at right as r
#lastBG:
#scene bg bg14a
show char tri01f2
with dis



voice "Risa_1941"
r "「みんな、盛り上がっているところ、ちょっといいかしら？」"
"キッチンでおやつ作りをしていた安曇璃紗が、部屋に入ってきた。"
voice "Risa_1942"
r "「おやつにクッキーを焼こうと思って、今生地を作ったところなんだけど……型抜きは、みんなでやらない？」"
voice "Mobmaisis0021"
mai "「えっ、クッキー、つくるつくる」"
voice "Mobmaibrz0028"
mao "「ボクもやりたいー」"
voice "Risa_1943"
r "「それじゃあみんな、キッチンの方に行きましょうね」"


show char tre01f2
with dis



voice "Reo_0897"
re "「………………ほっ」"
"うまい具合に子供たちの興味がおやつに移ってくれて。"
"ワタシはこれ以上、綾瀬美夜と勝負をしなくて良くなったのだった。"


show char tri01f2
with dis



voice "Risa_1944"
r "「ねっ、美夜と玲緒さまも、やりますよね？」"


show char tmi02f2 at left
show char tri01f2 at right as r
with dis



voice "Miya_1149"
m "「ええ、今行くわ……行きましょう、玲緒さま」"
"ニヤリと、綾瀬美夜が笑う。"
"まるでワタシの心を読んでいるかのようで……"

hide char tmi02f2 at left
hide char tri01f2 at right as r
show char tre03f2 at sleft as l
show char tmi02f2
show char tri01f2 at sright as sr
with dis



voice "Reo_0898"
re "「い、言っておくけど、今回は子供の手前、本気じゃなかったのよ」"


show char tre01f2 at sleft as l
with dis



voice "Reo_0899a"
re "「だって、大人ふたりで本気でムキになってゲームするなんて、おかしいもの」"


show char tmi01f2
with dis



voice "Miya_1150"
m "「はい……奇遇ですね、わたくしもです」"
"えっ？"


show char tmi02f2
with dis



voice "Miya_1151"
m "「でしたら今度は、本気で勝負しましょうね……玲緒さま{image=image/exch001.png}」"


show char tre03f2 at sleft as l
with dis



voice "Reo_0899b"
re "「そ、そう……ね、本気で……ね」"


#allClear:
hide char tre03f2 at sleft as l
hide char tmi02f2
hide char tri01f2 at sright as sr
#lastBG:
#scene bg bg14a
with dis


"あれが本気じゃないなんて。"
"うわーん。"
"今すぐ、麻衣に泣きつきたい気分だった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**麻衣の部屋・昼
scene bg bg14a
with Dis



#mes on
#system on


"その後、みんなで作ったクッキーを食べたりと、楽しく過ごした。"
voice "Mobmaisis0022"
mai "「ねぇ、れおちゃん！　お馬さんやって」"


show char tre03f2
with dis



voice "Reo_0900"
re "「お、お馬さん？　このワタシが？」"
"そんなの、冗談じゃないわ……"
voice "Mobmaisis0023"
mai "「やってぇ、麻衣おねえちゃんはいつも、やってくれるよ？」"
voice "Mobmaibrz0029"
mao "「そうだぞ、れおだってやれよー」"
voice "Reo_0901"
re "「くっ……」"
"でも麻衣が、いつもやっているなら……"
"今日のワタシは、麻衣の代わりに２人のお姉ちゃんをやっているんだから。"
"やるべきなのかな……やりたくないけど、仕方ないよね。"


##cg 1 tre08f2 400 0
##wipe fade


#voice RISA_1945
##voice RISA_1946
#【璃　紗】「いいわよ、ワタシが馬、やってあげるわよ」
"ワタシはしぶしぶと、床に四つん這いになった。"
"すると２人は争うようにして、ワタシの背中に飛び乗った。"


#※CU20
show char CU20
with dis



voice "Mobmaisis0024"
mai "「わぁ～い、お馬さん、お馬さん～」"
voice "Mobmaibrz0030"
mao "「次はボクだからね」"
voice "Reo_0902"
re "「ひぃ……ちょっと髪の毛、ひっぱらないの」"
voice "Mobmaisis0025"
mai "「だってお馬さんの毛だもん、それそれ～」"
voice "Reo_0903"
re "「イタッ、もう暴れないで」"
"重たいし、痛いし。"
"いつもこんなのやってるなんて……麻衣って、本当にすごいわ。"
"世の中のおねえちゃんって、みんなこんなに大変なのかしら。"


#**麻衣の部屋・昼
#allClear:
hide char CU20
#lastBG:
#scene bg bg14a
with dis


voice "Mobmaisis0026"
mai "「ふふふっ、おもしろかった、ありがとー、れおちゃん」"


show char tre03f2
with dis



voice "Reo_0904"
re "「あっ、う、うん……」"
voice "Mobmaibrz0031"
mao "「じゃあ、次はボクだよ」"


show char tre01p
with dis



voice "Reo_0905"
re "「はいはい、どうぞ」"
"乗りやすい体勢になってあげると、麻衣の弟は嬉しそうに、ワタシの背中にまたがってきた。"
voice "Mobmaibrz0032"
mao "「わーい！」"


show char tre03p
with dis



voice "Reo_0906"
re "「ちょ、ちょっと暴れすぎよ、まったく……もう」"
"すごく大変だったけれど、２人の楽しそうな声を聞いていると、それだけでなんだか頑張れるような気がした。"


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


play music "sound/BGM12.ogg"


#**麻衣の部屋・夜
scene bg bg14c
with Dis



#mes on
#system on


show char tri01f2
with dis



voice "Risa_1947"
r "「それでは玲緒さま、失礼します」"


show char tmi01f2 at left
show char tri01f2 at right as r
with dis



voice "Miya_1152"
m "「お邪魔しました」"

hide char tmi01f2 at left
hide char tri01f2 at right as r
show char tre01f2 at sleft as l
show char tmi01f2
show char tri01f2 at sright as sr
with dis



voice "Reo_0907"
re "「その、えっと……２人とも、どうも……ありがとう」"


#allClear:
hide char tre01f2 at sleft as l
hide char tmi01f2
hide char tri01f2 at sright as sr
#lastBG:
#scene bg bg14c
with dis


"夕方になって、夕飯の支度をしてくれて。"
"安曇璃紗と綾瀬美夜は、帰っていった。"
"コンビニで適当にお総菜を買って、済ませようかと思っていたから、正直助かったわ。"
"それを食べ終える頃には、すっかり夜になっていた。"
"でも……麻衣からの連絡は、まだない。"
"昼間はあれだけ騒がしかったのに、何故か３人とも、無口になってしまっていた。"

#//SE：携帯の音
#♀SE007
play sound "sound/SE007.ogg"


show char tre01f2
with dis



voice "Reo_0908"
re "「あっ、麻衣からだわ！！」"
"急いで電話に出ると、子供たち２人も近くで固唾をのんで、ワタシを見つめていた。"
voice "Reo_0909"
re "「もしもし、麻衣っ？」"


show char tma03p at left
show char tre01f2 at right as r
with dis



voice "Mai_0779"
ma "『あっ、玲緒、ごめんね。昼間、全然連絡できなくて』"


show char tre03f2 at right as r
with dis



voice "Reo_0910"
re "「それよりも、お母さんはどうなの？」"


stop music fadeout 1


play music "sound/BGM15.ogg"


voice "Mai_0780"
ma "『お母さん……今夜が山場だから、また泊まりなの。もう１日だけ、２人をお願い』"
voice "Reo_0911"
re "「えっ……それって……」"
"山場ってことは……まさかの、まさか……"
voice "Mai_0781"
ma "『わたし、すぐに病室戻らないといけないから……後はよろしくね』"
voice "Reo_0912"
re "「ちょっと待ってよ、麻衣」"


hide char tma03p at left
with dis


#♀SE059
play sound "sound/SE059.ogg"


"なんか大変なの？　アブナイってことなの？？"
"何も聞き返すこともできず、麻衣からの電話は一方的に切れてしまった。"


#allClear:
hide char tre03f2 at right as r
#lastBG:
#scene bg bg14c
show char tre03f2
with dis


voice "Reo_0913"
re "「……ぁぁ……はぁ～」"
"携帯をしまい、ため息をつくと、こっちを必死に見つめてる子供たちと目が合った。"
voice "Reo_0914"
re "「あ、あのね……」"
voice "Mobmaibrz0033"
mao "「麻衣おねえちゃん、まだびょーいんなの？」"
voice "Mobmaisis0027"
mai "「お母さん、たいへんなの？」"
"ワタシと麻衣の会話が漏れていたみたいで、二人の顔には不安の色が見え隠れしていた。"
voice "Reo_0915"
re "「それは、その……」"
"だめだわ、ワタシがしっかりしなきゃ。"
"だってワタシは、麻衣の代わり……この子たちのお姉ちゃんなんだから。"


show char tre01f2
with dis



voice "Reo_0916"
re "「大丈夫だよ。麻衣も明日には、きっと帰ってくるよ」"
voice "Mobmaisis0028"
mai "「でも、でもぉ……ぅぅっ」"
voice "Reo_0917"
re "「お母さんも今、必死でがんばっているんだから。ワタシたちはいっぱい、神様にお祈りするのよ」"
voice "Mobmaibrz0034"
mao "「かみさまに……おいのり……」"
voice "Reo_0918"
re "「そうよ、お祈りよ」"
"学校でお祈りする時でも、こんなに真面目にしたことはなかったけれど……"
"ワタシは指を組んで、瞳を閉じて、祈りを捧げる。"
"子供たちも同じように、ワタシの真似をする。"
voice "Mobmaisis0029"
mai "「どうかおかあさんが、はやくよくなりますように」"
voice "Mobmaibrz0035"
mao "「かみさま、おねがいします」"
voice "Reo_0919"
re "「お願い……お願いします……」"
"強くつよく祈る、ワタシたち。"
"それでも不安に耐えきれず、子供たちはやっぱり泣き出してしまった。"
voice "Mobmaisis0030"
mai "「おかあさ～ん、ふぇぇぇん」"
voice "Mobmaibrz0036"
mao "「うううっ、おかあさん……ひっく」"
voice "Reo_0920"
re "「大丈夫……ぜったい、だいじょうぶだから！！」"


#allClear:
hide char tre01f2
#lastBG:
#scene bg bg14c
with dis


"ワタシは泣いてる子供たちを慈しむように、ぎゅっと抱きしめた。"


#※EV076
scene bg EV76
with Dis



voice "Reo_0921"
re "「絶対に、大丈夫だから……ねっ」"
voice "Mobmaibrz0037"
mao "「れお……」"
voice "Mobmaisis0031"
mai "「れおちゃん……ぅぅっ……」"
"子供たちの姿に、ワタシも泣きそうになったけど。"
"だからって、一緒に不安になってはダメだもん。"
voice "Reo_0922"
re "「アンタたち、泣いちゃダメよ。泣いてばっかりいたら、目がとけちゃうわよ」"
voice "Mobmaibrz0038"
mao "「ひっく……なんだよ、それ」"
voice "Mobmaisis0032"
mai "「とけないもん……うううっ……」"
"泣きながら、ワタシにしがみつく２人。"
"ああ、もう……どうすればいいの？"
voice "Reo_0923"
re "「……あっ、そうだわ……」"


#**夜空
scene bg bg42c
with Dis



"ワタシは子守歌代わりに、賛美歌を歌ってあげた。"
voice "Mobmaibrz0039"
mao "「れお……？」"
voice "Mobmaisis0033"
mai "「れおちゃん……」"
"２人は黙って、その歌を聴いてくれて。"
"そしてそのまま、ワタシたち３人は抱き合って、朝まで一緒に眠ったのだった。"


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
jump S118



