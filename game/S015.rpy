#「七夕の恋人たち」

label S015:
$ save_name = "◇七夕の恋人たち"


#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP06
play music "sound/BGM06.ogg"


show char tri01s2
with dis



voice "Risa_0438"
r "「………………はぁ～、良かったぁ」"
"美夜のノートのおかげで、期末テストも無事に乗り切れたし。"
"テストの結果？　順位？？"
"ヤボな事、聞いてはダメよ……はいはい、どうせ私は学年２位でしたよ。"


show char tri03s2
with dis



voice "Risa_0439"
r "「でも……美夜のノートがなかったら、２位も危なかったかも」"
"今回だけは、素直に感謝しておかなくちゃ。"
"テストが終わると、もうすぐ夏休み。"
"クラスメイトたちは、夏のバカンスをどう過ごすのか、楽しそうに話していたけれど。"


show char tri01s2
with dis



voice "Risa_0440"
r "「夏休み後には、文化祭があるのよね……イベント実行委員の方は、忙しくなりそうよね」"
"今までは、のんびりしていたけど。"
"そろそろ準備に入らないといけない。"
"夏休みまでの間、時間のある人は放課後、委員会室に集まることになっていた。"
"そして、今日も……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**委員会室・昼
scene bg bg30a
with Dis



#mes on
#system on


show char tna01s2
with dis



voice "Nanami0127"
n "「各クラスの部活動の出し物は今のところ、こんな感じです」"


show char tma01s2 at left
show char tna01s2 at right as r
with dis



voice "Mai_0104"
ma "「それって、この間クラスごとで話しあったヤツかしら」"
voice "Nanami0128"
n "「ええ、環境整備委員の方で、それぞれ第一希望を統計したものを持ってきました」"


show char tyu01s2 at left
with dis



voice "Yuuna_0032"
y "「毎年のことだけど、展示と喫茶がほとんどね……喫茶はあまり多すぎても、調理場とかの問題があるから、調節したりするのが大変なのよね」"
voice "Nanami0129"
n "「部活に関しては、体育館のステージを使う時間の割り振りとか、そういうものも考えないといけませんよね」"
"ミカ女の運営の要とも言える、環境整備委員会の方は、そういうことを全部決めないといけないから大変そうだわ。"
"一方、イベント実行委員の私たちは、全体的な出し物を把握しながら、何か出し物を考えないといけないし。"


#allClear:
hide char tyu01s2 at left
hide char tna01s2 at right as r
#lastBG:
#scene bg bg30a
show char tri03s2
with dis



voice "Risa_0441"
r "「それはそれで、大変そう……」"


show char tsa02s2
with dis



voice "Sara_0051"
sr "「クリスマスやバレンタインの時のように、みんなで楽しめるのがいいよね♪」"


show char tka02s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0033"
# "【　楓　】「そうね……」"


#allClear:
hide char tka02s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"とりあえず、文化祭時の飾り付けに使うものだけは、先にデザインを決めて作り始めることにした。"
"今回は学生がメインの、本当の意味でのお祭りだから、今までよりも少しだけ派手な感じにはなるみたい。"


show char tyu01s2
with dis



voice "Yuuna_0033"
y "「私たちの出し物に関しては、２学期にはいったら本格的に決めましょうね」"


show char tsa02s2
with dis



voice "Sara_0052"
sr "「はーい。でも喫茶店とか……ああ、やってみたいよね♪」"


show char tka03s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0034"
# "【　楓　】「でも、コスプレはしないわよ」"


show char tsa03s2 at right as r
with dis



voice "Sara_0053"
sr "「うっ、先手を打たれてしまった……楓ちゃん、つまんなーい」"


show char ter02f2 at left
show char tka03s2 at right as r
with dis



voice "Erisu_0025"
e "「本当だよ、コスプレ喫茶はいいアイディアなのにね{image=image/exch001.png}」"


show char tka04s2 at right as r
with dis



voice "Kaede_0035"
# "【　楓　】「きゃっ！？　エリスさま、いつの間に……」"


show char ter01f2 at left
with dis



voice "Erisu_0026"
e "「ごきげんよう、手伝いにきたよ」"


show char tsi01f2 at right as r
with dis



voice "Sizuku0022"
# "【　雫　】「ごきげんよう、皆さん」"


#allClear:
hide char ter01f2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0105"
ma "「お二人とも、ごきげんよう。短大の方はいつからお休みなんですか」"


show char ter01f2 at left
show char tma01s2 at right as r
with dis



voice "Erisu_0027"
e "「もう、明日からだよ」"


show char tre08s2 at right as r
with dis



voice "Reo_0077"
re "「えぇっ、ずっるい～、でもいいなぁ」"


show char tsi03f2 at left
with dis



voice "Sizuku0023"
# "【　雫　】「ですが課題も多いですし、調べものもあるので……休み中も、学校に行くことは多くなりそうです」"


show char tre03s2 at right as r
with dis



voice "Reo_0078"
re "「か、課題……ううっ、面倒くさそう」"


#allClear:
hide char tsi03f2 at left
hide char tre03s2 at right as r
#lastBG:
#scene bg bg30a
show char tri01s2
with dis



voice "Risa_0442"
r "「やっぱり短大の方も、色々と大変なんですね」"


show char ter02f2 at left
show char tri01s2 at right as r
with dis



voice "Erisu_0028"
e "「でも、なんとかなってるよ……シズクの完璧なノートのおかげでね{image=image/exch001.png}」"


show char tsi08f2 at right as r
with dis



voice "Sizuku0024"
# "【　雫　】「エリスは授業中、すぐに居眠りするんですから」"
voice "Erisu_0029"
e "「まぁまぁ」"


#allClear:
hide char ter02f2 at left
hide char tsi08f2 at right as r
#lastBG:
#scene bg bg30a
show char tri03s2
with dis



"居眠り？"
"エリスさまって美夜と同じで、もしかしてサボり魔なのかしら。"


show char tmi08s2 at left
show char tri03s2 at right as r
with dis



voice "Miya_0206"
m "「どうしてそこで、わたくしの顔を見るのかしら……璃紗？」"
voice "Risa_0443"
r "「な、なんとなく……ね」"

hide char tmi08s2 at left
hide char tri03s2 at right as r
show char tyu01s2 at sleft as l
show char tmi08s2
show char tri03s2 at sright as sr
with dis



voice "Yuuna_0034"
y "「美夜ちゃん、それ塗り終わったら、こちらやってもらえるかしら」"


show char tmi01s2
with dis



voice "Miya_0207"
m "「……はい」"


#allClear:
hide char tyu01s2 at sleft as l
hide char tmi01s2
hide char tri03s2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"黙々と作業を続ける美夜は、口数は少ないけれど、すっかりこの場に馴染んでいた。"
"新メンバーの二人は……どうかしら？"
"六夏は皆さんに恋愛相談しているおかげで、それぞれと仲良くなっているし。"
"沙雪さんは、七海さんや優菜さまと委員も同じだし、特に物怖じせず、作業に勤しんでいる。"
"うん、今のところグループとしてのまとまりは、良い感じだわ。"


show char trk01s2
with dis



voice "Rikka_0283"
rk "「文化祭、ウチのクラスも喫茶店がやりたいって意見が多かったですね」"


show char tna01s2 at left
show char trk01s2 at right as r
with dis



voice "Nanami0130"
n "「六夏さんは……そうね、執事とか似合いそう」"


show char trk03s2 at right as r
with dis



voice "Rikka_0284"
rk "「それ、みんなから言われました……」"


#allClear:
hide char tna01s2 at left
hide char trk03s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa02s2
with dis



voice "Sara_0054"
sr "「やっぱり～、楓ちゃんも」"


show char tka08s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0036"
# "【　楓　】「私は執事もメイドも、やらないわよ」"


show char tsa10s2 at right as r
with dis



voice "Sara_0055"
sr "「ふにゃー、今日の楓ちゃん、厳しすぎるよぉ」"


#allClear:
hide char tka08s2 at left
hide char tsa10s2 at right as r
#lastBG:
#scene bg bg30a
show char tre01s2
with dis



voice "Reo_0079"
re "「ワタシは……あれがやりたい。お正月の初詣の時にみたヤツ」"


show char tma04s2 at left
show char tre01s2 at right as r
with dis



voice "Mai_0106"
ma "「えっ、もしかして巫女さんやりたいの？」"


#allClear:
hide char tma04s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg30a
show char ter02f2
with dis



voice "Erisu_0030"
e "「エクセレント！　シズクのミコさん、見てみたいよ」"


#allClear:
hide char ter02f2
#lastBG:
#scene bg bg30a
with dis


"それは……うん、すごく似合いそう。"
"というか、雫さまみたいな巫女さんがいたら、そこの神社は大評判になっちゃいそうだわ。"
"しかし玲緒さまが言いたかったのは、別のことのようだった。"


show char tre08s2
with dis



voice "Reo_0080"
re "「そうじゃなくて、たくさん並んでいたお店のことよ」"


show char tri03s2 at left
show char tre08s2 at right as r
with dis



voice "Risa_0444"
r "「それって……屋台のことですか？」"


show char tre01s2 at right as r
with dis



voice "Reo_0081"
re "「そうよ、安曇璃紗。たまにはアンタも役にたつわね」"
"た、たまにはって……"


#allClear:
hide char tri03s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg30a
show char tmi02s2
with dis



voice "Miya_0208"
m "「………………ぷっ、んふふっ」"
"もう、美夜ったら……何笑ってるのよ。"


show char trk01s2
with dis



voice "Rikka_0285"
rk "「文化祭で屋台って、よく見かけますよね」"


show char tyu01s2 at left
show char trk01s2 at right as r
with dis



voice "Yuuna_0035"
y "「そうね。でもミカ女では、景観を損ねるってことで、許可していないわ」"


show char tna03s2 at right as r
with dis



voice "Nanami0131"
n "「えっ、そうなんですか？」"

hide char tyu01s2 at left
hide char tna03s2 at right as r
show char tyu01s2 at sleft as l
show char tna03s2
show char tma01s2 at sright as sr
with dis



voice "Mai_0107"
ma "「そういえば今までも、見たことないわよね」"
"確かにミカ女の校庭や中庭に、屋台が並んでいたら……"
"なんだか、すごくミスマッチだわ。"


#allClear:
hide char tyu01s2 at sleft as l
hide char tna03s2
hide char tma01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tre03s2
with dis



voice "Reo_0082"
re "「えーっ、出来ないのぉ～」"


show char tka01s2 at left
show char tre03s2 at right as r
with dis



voice "Kaede_0037"
# "【　楓　】「玲緒さんは、どんな店をやってみたかったのかしら？」"


show char tre02s2 at right as r
with dis



voice "Reo_0083"
re "「チョコバナナ！　初めて食べたけど、甘くてすごぉーく美味しかった{image=image/exch001.png}　あれなら簡単そうじゃない？」"
"チョコバナナ？"
"確かに、材料も少ないし簡単そうには見えるわ。"


show char tma08s2 at left
show char tre02s2 at right as r
with dis



voice "Mai_0108"
ma "「玲緒、あなたは屋台の……チョコバナナの恐ろしさを知らないのね」"


show char tre03s2 at right as r
with dis



voice "Reo_0084"
re "「な、なによ、麻衣、チョコバナナのどこが恐ろしいのよ？」"
"麻衣さまはやれやれと、肩をすくめる。"
voice "Mai_0109"
ma "「じゃあ、玲緒にも分かりやーすく説明してあげるわ」"
voice "Mai_0110"
ma "「文化祭当日、業者からバナナが届く……それをみんなで皮をむく」"
voice "Reo_0085"
re "「それが、何なのよ」"
voice "Mai_0111"
ma "「そこに、遅れてきた玲緒が登場」"


show char tre08s2 at right as r
with dis



voice "Reo_0086"
re "「遅れないわよ」"
voice "Mai_0112"
ma "「前日、文化祭が楽しみすぎて眠れなかった玲緒は、寝坊するのが必然」"


show char tre03s2 at right as r
with dis



voice "Reo_0087"
re "「……し、しないって」"
"思い当たるところがあるのか、少し玲緒さまはたじろいだ。"
voice "Mai_0113"
ma "「ゴミ袋に入れておいたバナナの皮が、何かの拍子で床に落ち……そこにちょうど走ってくる、玲緒の姿が」"
voice "Reo_0088"
re "「………………」"
voice "Mai_0114"
ma "「玲緒はお約束のすってんころりん。慌てて周りの何かを掴む玲緒、そこにはちょうど用意してあったチョコレートが……」"
voice "Reo_0089"
re "「………………」"


show char tma02s2 at left
with dis



voice "Mai_0115"
ma "「あっと言うまに、玲緒のチョコレートがけが出来上がり。ねっ、怖いでしょう？」"


show char tre09s2 at right as r
with dis



voice "Reo_0090"
re "「ば、ばっかじゃないの……麻衣」"
"玲緒さまが怒り、みんながにこやかに笑う中、ただ１人……青ざめている者がいた。"


#allClear:
hide char tma02s2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg30a
show char tsy03s2
with dis



voice "Sayuki0120"
s "「り、六夏さん……屋台というものは知りませんが、実に恐ろしいものなんですね」"


show char trk03s2 at left
show char tsy03s2 at right as r
with dis



voice "Rikka_0286"
rk "「沙雪さん……あっ、えっと、それは……」"
"沙雪さんはどうやら、麻衣さまの話を本気で信じ込んでいるようだった。"


show char tsy01s2 at right as r
with dis



voice "Sayuki0121"
s "「ですが、チョコレートがけの玲緒さまは……きっと彫刻のように、お美しくなるような気がしますわ」"


show char trk04s2 at left
with dis



voice "Rikka_0287"
rk "「えええええっ？」"


#allClear:
hide char trk04s2 at left
hide char tsy01s2 at right as r
#lastBG:
#scene bg bg30a
show char tre09s2
with dis



voice "Reo_0091"
re "「ちょっとそこの１年、何か失礼なこと言ってないかしら」"


show char tma01s2 at left
show char tre09s2 at right as r
with dis



voice "Mai_0116"
ma "「まぁまぁ」"
"沙雪さんは多分、天然なんだろうけど。"
"なんだかこれじゃ、収集がつかなくなってきた。"


#allClear:
hide char tma01s2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg30a
show char tna01s2
with dis



voice "Nanami0132"
n "「屋台は無理なのは、わかってるけど……金魚すくいとか出来たら、おもしろそうですね～」"
"七海さんがすかさず、話題をそらす。"
"さすが次世代リーダー候補、場を仕切るのがうまくなってきたわね。"


show char tna02s2
with dis



voice "Nanami0133"
n "「優菜さまと以前、一緒に金魚すくいしたんですけど……あれはすごかったわ。優菜さまは金魚すくいの天才です」"


show char tmi01s2
with dis



voice "Miya_0209"
m "「……天才？」"
"ぴくっと、美夜がその一言に反応をしめす。"
voice "Miya_0210"
m "「璃紗、屋台じゃなくて、教室で金魚すくいは出来ないのかしら？」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0445"
r "「ど、どうかな……今のところ、ウチのクラスでは金魚すくいの案は出てないから」"
"生き物扱うのは、大変そうだし……"
"うちのクラスメイトに任せたら、とんでもない高級な金魚とか鯉とか、平気で買ってきちゃいそうなんだけど。"
voice "Miya_0211"
m "「璃紗の委員長特権で、どうにか出来ないものかしら……」"
voice "Risa_0446"
r "「でっ、出来ないわよ……もう」"
"そんなもの、これまで行使したこともないし。"


#allClear:
hide char tmi01s2 at left
hide char tri03s2 at right as r
#lastBG:
#scene bg bg30a
show char tma08s2
with dis



voice "Mai_0117"
ma "「でもね、美夜ちゃん……金魚すくいだって恐ろしいわよ」"


show char tma08s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0092"
re "「またワタシがどうにかなるって言いたいの？　言っておくけど金魚すくいくらい、ワタシだって出来るわよ。網で金魚を捕ればいいんでしょう」"

hide char tma08s2 at left
hide char tre08s2 at right as r
show char tma08s2 at sleft as l
show char tre08s2
show char tsi01f2 at sright as sr
with dis



voice "Sizuku0025"
# "【　雫　】「網ではなくポイですよ、玲緒さん」"


show char tre03s2
with dis



voice "Reo_0093"
re "「し、知ってるわよ、それくらい……ポイね、ポイ」"


#allClear:
hide char tma08s2 at sleft as l
hide char tre03s2
hide char tsi01f2 at sright as sr
#lastBG:
#scene bg bg30a
show char tri01s2
with dis



voice "Risa_0447"
r "「モナカのもありますけど、やっぱり紙の方が金魚すくいって感じですよね」"


show char tsy03s2
with dis



voice "Sayuki0122"
s "「金魚すくい……ですか。生き物の命を救う、尊いイベントなのでしょうか……」"
"また沙雪さん、ちょっとついていけてないみたい。"


show char tma03s2
with dis



voice "Mai_0118"
ma "「その金魚すくいの水で、玲緒が溺れたりするかも……ああ、恐ろしい」"


show char tma03s2 at left
show char tre09s2 at right as r
with dis



voice "Reo_0094"
re "「なぁーーーー、溺れないわよ」"
voice "Mai_0119"
ma "「一般人なら溺れないけど、ちっちゃい玲緒はあの中で、足がつかないかもしれないわ」"
voice "Reo_0095"
re "「つくわよっ！」"


#allClear:
hide char tma03s2 at left
hide char tre09s2 at right as r
#lastBG:
#scene bg bg30a
show char tsy04s2
with dis



voice "Sayuki0123"
s "「まぁ、金魚すくいってやはり、とても危険なんですね、六夏さん」"


show char trk03s2 at left
show char tsy04s2 at right as r
with dis



voice "Rikka_0288"
rk "「えーと……」"


#allClear:
hide char trk03s2 at left
hide char tsy04s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"また、六夏が困っている。"
"文化祭の飾り付けとはいえ、紙や布を切ったり貼ったりと、単純作業の繰り返しでみんなも退屈しているんでしょう。"
"何をやるか決めるよりも、ただの雑談になっていった。"


show char trk01s2
with dis



voice "Rikka_0289"
rk "「そういえば……」"
"星形に切った紙を眺めながら、六夏がふと呟いた。"
voice "Rikka_0290"
rk "「このミカ女って、色々な行事がありますが、七夕はやらないんですか？」"
"今日って……７月７日。"
"六夏の言う通り、七夕だったわ。"


show char tyu01s2 at left
show char trk01s2 at right as r
with dis



voice "Yuuna_0036"
y "「六夏ちゃんは外部だから、知らないのも無理はないわね」"
"六夏の疑問にすぐ、優菜さまが答えてくれた。"
voice "Yuuna_0037"
y "「ここはミッション系の学校だから、日本固有の行事はやらないのよ」"
voice "Rikka_0291"
rk "「そうだったんですか」"


#allClear:
hide char tyu01s2 at left
hide char trk01s2 at right as r
#lastBG:
#scene bg bg30a
show char tsa02s2
with dis



voice "Sara_0056"
sr "「別に、やってもいいのにね～♪」"


show char tka02s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0038"
# "【　楓　】「そうね……みんなで浴衣を着たりするのもいいわね」"


#allClear:
hide char tka02s2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"七夕かぁ……今日は天気も良いし、天の川がきれいに見えるかもしれないわ。"
"１年に一度だけ会える、彦星と織姫の逢瀬。"
"最初に二人は、どんな会話をかわすのかしら……"


show char tmi02s2
with dis



voice "Miya_0212"
m "「……ふふふっ、璃紗。また恥ずかしい妄想をしているんでしょう」"
"小声でこそっと、美夜が囁く。"


show char tmi02s2 at left
show char tri05s2 at right as r
with dis



voice "Risa_0448"
r "「わ、悪い！？」"
voice "Miya_0213"
m "「ふふっ……いいえ、素敵よ。いつまでも少女の心を忘れない、璃紗……んふふっ」"
"もう……美夜ったら。"
"でも美夜とそんな話をしているうちに、いいことを思いついてしまった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・昼
scene bg bg08c
with Dis



#mes on
#system on


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



"久しぶりに美夜と一緒の帰宅。"
"でも、もうすぐ分かれ道にさしかかる。"
"私は思い切って、美夜を誘った。"


show char tri03s2 at right as r
with dis



voice "Risa_0449"
r "「ね、美夜……今日は時間、あるかしら」"
voice "Miya_0214"
m "「ええ、特に何も予定は入ってないわ」"


show char tri01s2 at right as r
with dis



voice "Risa_0450"
r "「それなら今夜、ウチで一緒に七夕しましょうよ」"
voice "Miya_0215"
m "「……珍しいわね、璃紗から誘いがかかるなんて」"
voice "Risa_0451"
r "「そんな言い方しないでよ。そりゃあ最近は、ずっと六夏のことばかり気にかけていたけれど」"
voice "Miya_0216"
m "「自覚はあるのね、さすがの璃紗にも」"


show char tri03s2 at right as r
with dis



voice "Risa_0452"
r "「うううっ」"
"美夜を放っておいたのは私だから、あまり強くはでれないけど。"
"美夜を優位に立たせると、とんでもない条件を出してきそうだから。"
"今日は何としても、私のペースで美夜を誘わないと。"


show char tri01s2 at right as r
with dis



voice "Risa_0453"
r "「それに……テストのノート、あれとても助かったわ。そのお礼もしたいのよ」"
voice "Miya_0217"
m "「お礼？」"
"美夜の目がキラン、と光る。"


#♀SE062
play sound "sound/SE062.ogg"


show char tri09s2 at right as r
with dis



voice "Risa_0454"
r "「お、お礼って言っても、えっちなお礼じゃないからねっ！」"
"美夜が何か言う前に、しっかりと釘を刺しておく。"


show char tmi02s2 at left
with dis



voice "Miya_0218"
m "「ふふふっ、住宅街の真ん中で、璃紗ったら……大胆な発言をするのね」"


show char tri03s2 at right as r
with dis



voice "Risa_0455"
r "「あっ……」"
"周りは幸い、誰も歩いていなかったけれど。"
"今の私の声、大きかったかもしれないわ。"
"え、えっちとか……叫んじゃったし。"


show char tri02s2 at right as r
with dis



voice "Risa_0456"
r "「とにかく、学校行事では七夕はないけど、私たち２人でなら……ね？」"
"そう言って笑いかけると、美夜は恥ずかしそうに横を向いた。"


show char tmi05s2 at left
with dis



voice "Miya_0219"
m "「……璃紗がしたいっていうなら、わたくしは……」"


show char tri01s2 at right as r
with dis



voice "Risa_0457"
r "「いいのね？」"
voice "Miya_0220"
m "「璃紗がどうしても、って言うのなら、ね」"


show char tri02s2 at right as r
with dis



voice "Risa_0458"
r "「ありがとう、美夜」"
"ちょっとまだ素直になれないところがあるみたいだけど、美夜は了承してくれた。"


show char tri01s2 at right as r
with dis



voice "Risa_0459"
r "「そうと決まれば、早く帰りましょう」"


show char tmi01s2 at left
with dis



voice "Miya_0221"
m "「ええ……」"
"どちらからともなく差し出した手を握り、私の家まで２人で並んで帰った。"
"六夏の言葉で思い出した、七夕だけど。"
"他のカップル達も、もしかしたら……私と同じようなこと考えているかしら？"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（七海と優菜の七夕）

#**繁華街・夜
scene bg bg17c
with Dis



#mes on
#system on


show char tna02s2
with dis



voice "Nanami0134"
n "「あっ、見てください、お姉さま。商店街で七夕祭りやってますよ」"


show char tyu02s2 at left
show char tna02s2 at right as r
with dis



voice "Yuuna_0038"
y "「本当だわ、きれいに飾り付けされているわね」"
voice "Nanami0135"
n "「六夏さんが言ってたみたいに、ミカ女でもこういうのが出来たら楽しそうでしたね」"


show char tyu01s2 at left
with dis



voice "Yuuna_0039"
y "「そうね……あらっ、七海ここにある短冊、好きに書いていいみたいよ、せっかくだから書いていかない？」"
voice "Nanami0136"
n "「いいですね。じゃあわたしは、この水色の紙に書きますね」"
voice "Yuuna_0040"
y "「じゃあ私は……七海色の、ピンクの紙にしようかしら」"


show char tna03s2 at right as r
with dis



voice "Nanami0137"
n "「………………」"


show char tyu02s2 at left
with dis



voice "Yuuna_0041"
y "「もちろん、七海のあそこの色よ」"


show char tna04s2 at right as r
with dis



voice "Nanami0138"
n "「わー、わかってますから！　だからあえてツッコまなかったのに……」"
voice "Yuuna_0042"
y "「ふふふっ、何書こうかしら、七海と……できますように」"


show char tna01s2 at right as r
with dis



voice "Nanami0139"
n "「……が、怖いです」"


show char tyu01s2 at left
with dis



voice "Yuuna_0043"
y "「はい、書けたわ。七海は？」"
voice "Nanami0140"
n "「わたしも、書けました」"
voice "Yuuna_0044"
y "「じゃあこれを、笹につけて……っと」"


show char tna04s2 at right as r
with dis



voice "Nanami0141"
n "「ちょ、ちょっと待ってください、それなんて書いてあるんですか」"


show char tyu02s2 at left
with dis



voice "Yuuna_0045"
y "「今年の夏も七海とたぁくさ～ん、えっち出来ますように{image=image/exch001.png}」"
voice "Nanami0142"
n "「だ、だめです、そんなの飾らないでください」"


show char tyu10s2 at left
with dis



voice "Yuuna_0046"
y "「ええっ、せっかくの願い事なのに……くすん」"


show char tna08s2 at right as r
with dis



voice "Nanami0143"
n "「誰かに見られたら、どうするんですか」"


show char tyu02s2 at left
with dis



voice "Yuuna_0047"
y "「見せたいのよ、織姫さまと彦星さまに見せるのよ、私たちの愛を{image=image/exch001.png}」"


show char tna07s2 at right as r
with dis



voice "Nanami0144"
n "「それでも、だめですって」"


show char tyu01s2 at left
with dis



voice "Yuuna_0048"
y "「それなら七海が、願いを叶えてくれる？」"


show char tna03s2 at right as r
with dis



voice "Nanami0145"
n "「わ、わかりましたから……やめてください」"


show char tyu02s2 at left
with dis



voice "Yuuna_0049"
y "「そう{image=image/exch001.png}　じゃあやめるわ」"
voice "Nanami0146"
n "「あっ……」"
voice "Yuuna_0050"
y "「それじゃあ早速、帰ってたぁくさ～んえっちしようね、七海ぃ～」"
voice "Nanami0147"
n "「うぅぅ……なんかハメられたような……」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（楓と紗良の七夕）

#**商店街・夜
scene bg bg16c
with Dis



#mes on
#system on


show char tsa03f2
with dis



voice "Sara_0057"
sr "「わぁ、街は七夕一色だね。でもせっかくの七夕なのに……急なお仕事、入っちゃったね。がっかり」"


show char tka01f2 at left
show char tsa03f2 at right as r
with dis



voice "Kaede_0039"
# "【　楓　】「そうね……でもそんなにガッカリしなくてもいいんじゃない、紗良」"
voice "Sara_0058"
sr "「えっ？　あんまり仕事が好きじゃない楓ちゃんにしては、珍しい発言だね……ひょっとして、モデルスピリッツに目覚めた、とか？」"
voice "Kaede_0040"
# "【　楓　】「違うわ、そうじゃなくて……ほら、七夕って年に一度、織姫様と彦星様が逢える日でしょう？」"
voice "Sara_0059"
sr "「うん、そうだよね……でも一年に一度しか逢えないなんて、寂しすぎるよ」"


show char tsa10f2 at right as r
with dis



voice "Sara_0060"
sr "「紗良がもし、一年に一度しか、楓ちゃんに逢えなかったら……残りの３６４日は、泣いて過ごすよ」"
voice "Kaede_0041"
# "【　楓　】「ありがとう。だから、そういう事が言いたかったのよ」"


show char tsa03f2 at right as r
with dis



voice "Sara_0061"
sr "「そういう……事？？」"
voice "Kaede_0042"
# "【　楓　】「確かに今日はお仕事になっちゃったけれど、それでも私と紗良は、こうして一緒にいられるでしょう……ね？」"


show char tsa01f2 at right as r
with dis



voice "Sara_0062"
sr "「楓ちゃん……そうだね。紗良と楓ちゃんは一年中、七夕みたいなものだよね～」"


show char tka02f2 at left
with dis



voice "Kaede_0043"
# "【　楓　】「そうよ……感謝しなくちゃ、ね」"


show char tsa02f2 at right as r
with dis



voice "Sara_0063"
sr "「もう、良いこと言うなぁ、楓ちゃん……大好きっ{image=image/exch001.png}」"


show char tka05f2 at left
with dis



voice "Kaede_0044"
# "【　楓　】「ちょ、ちょっと紗良っ！　もうカメラ回ってるわよ、抱きついちゃダメぇっ……ぁん{image=image/exch001.png}」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（玲緒と麻衣の七夕）

#**玲緒の部屋・夜
scene bg bg33c
with Dis



#mes on
#system on


show char tre01f2
with dis



voice "Reo_0096"
re "「まーいーっ、ごはんまだー！？」"


show char tma03p at left
show char tre01f2 at right as r
with dis



voice "Mai_0120"
ma "「ゴメン、もうちょっとだけ待っててね、玲緒」"


show char tre03f2 at right as r
with dis



voice "Reo_0097"
re "「ぅぅっ、いつもより１時間も遅いんだから。もうお腹ペコペコよぉ……あっ、そういえば、綾瀬美夜から貰った焼き菓子の残りが……」"


show char tma01p at left
with dis



voice "Mai_0121"
ma "「お菓子は食べちゃダメよ、玲緒。あと３分くらいだから、ね？」"


show char tre01f2 at right as r
with dis



voice "Reo_0098"
re "「……はぁい。もう、どうしてわかっちゃったのかな、麻衣。でも３分ね、それ以上は待たないわよ……いーち、にー、さーん、よーん………………」"
voice "Reo_0099"
re "「………………よんじゅはーち、よんじゅきゅー、ごーじゅ！　はい麻衣、３分経ったわよ」"


show char tma01f2 at left
with dis



voice "Mai_0122"
ma "「どういう数え方よ、それ……でもはい、できたわよ」"


show char tre04f2 at right as r
with dis



voice "Reo_0100"
re "「こ……ここっ、これは……！？　これどうしたの、麻衣？」"


show char tma02f2 at left
with dis



voice "Mai_0123"
ma "「目玉焼きハンバーグでしょ、大盛りスパゲティでしょ、他にもから揚げと、カレーグラタンと……そして締めには、特盛りかき氷のアイス添え♪」"


show char tre03f2 at right as r
with dis



voice "Reo_0101"
re "「こんなにいっぱい、好きなのばっかり、全部食べていいの？」"
voice "Mai_0124"
ma "「もちろんいいわよ。玲緒の為に作ったんだもの{image=image/exch001.png}」"


show char tre02f2 at right as r
with dis



voice "Reo_0102"
re "「い、いただきます………………もぐもぐもぐ、ぱくぱく、ずずずっ」"
voice "Mai_0125"
ma "「本当に美味しそうに食べてくれるわね、玲緒は。こっちも作り甲斐があるわ」"


show char tre03f2 at right as r
with dis



voice "Reo_0103"
re "「もぐむしゃ、ぱくっ……でも麻衣、どうして今日はこんなに気前がいいの？」"


show char tma01f2 at left
with dis



voice "Mai_0126"
ma "「だって……七夕だもの。年に一度の、特別な日だもの」"


show char tre01f2 at right as r
with dis



voice "Reo_0104"
re "「おり姫と、ひこ星……逢えたかな？」"
voice "Mai_0127"
ma "「きっと逢えたわよ。だからそのお祝いディナーね」"
voice "Reo_0105"
re "「今夜の麻衣、ふとっ腹ね……はっ、まさかこの後、激しいエロスをする気で……」"
voice "Mai_0128"
ma "「まあ、それもあるけど……玲緒に、年に一度のご馳走、作ってあげたかったのよ」"


show char tre03f2 at right as r
with dis



voice "Reo_0106"
re "「……エロスの否定はしないのね」"


show char tma02f2 at left
with dis



voice "Mai_0129"
ma "「さぁて、今日は奮発しちゃったから、明日から財布のひもを締めていくわよ。当分、ふりかけご飯だからね♪」"


show char tre10f2 at right as r
with dis



voice "Reo_0107"
re "「そ、そんなぁ、麻衣のばかぁ～っ！！」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（雫とエリスの七夕）

#**雫の部屋・夜
scene bg bg27c
with Dis



#mes on
#system on


show char ter02f2
with dis



voice "Erisu_0031"
e "「わぁ～、シズク、これどうしたの？」"


show char ter02f2 at left
show char tsi02f2 at right as r
with dis



voice "Sizuku0026"
# "【　雫　】「七夕ぱーてぃです」"
voice "Erisu_0032"
e "「素麺の上に星型の野菜や玉子の飾りが乗ってて、ビューティフル♪」"


show char tsi01f2 at right as r
with dis



voice "Sizuku0027"
# "【　雫　】「それは天の川に見立ててみました。あと、こちらは押し寿司です」"


show char ter01f2 at left
with dis



voice "Erisu_0033"
e "「ケーキみたいで可愛い。これ全部、シズクが作ったの？」"
voice "Sizuku0028"
# "【　雫　】「ええ、エリスを驚かせようとして用意しておいたのです。エリスは七夕はしたことないと思ったので」"


show char ter02f2 at left
with dis



voice "Erisu_0034"
e "「ありがとう～、うん、初めてだよ、嬉しい♪　あっ、だからここ最近帰りが早かったんだね」"
voice "Sizuku0029"
# "【　雫　】「ええ、こっそり準備をしていました。六夏さんが七夕の話をした時はバレてしまわないかと、ドキドキしてました」"


show char ter01f2 at left
with dis



voice "Erisu_0035"
e "「ううん、全然気づかなかったよ」"
voice "Sizuku0030"
# "【　雫　】「それなら良かったです。こちらには浴衣も用意してありますよ」"
voice "Erisu_0036"
e "「わぁ、とことん本格的だね」"
voice "Sizuku0031"
# "【　雫　】「ええ、エリスに日本の夏らしいものを、今年はたくさん体験してもらいたいので」"


show char ter02f2 at left
with dis



voice "Erisu_0037"
e "「なんかすっごく楽しみだよ」"
voice "Sizuku0032"
# "【　雫　】「日本の夏といえば……浴衣、花火」"
voice "Erisu_0038"
e "「うんうん」"
voice "Sizuku0033"
# "【　雫　】「すいか割り、心霊すぽっとめぐり」"


show char ter03f2 at left
with dis



voice "Erisu_0039"
e "「……えっ？」"
voice "Sizuku0034"
# "【　雫　】「お休みの最終日に、みんなで集まって宿題をする」"


show char ter04f2 at left
with dis



voice "Erisu_0040"
e "「ええええっ？　な、なんかおかしくないかな？」"


show char tsi03f2 at right as r
with dis



voice "Sizuku0035"
# "【　雫　】「そうですか、ねっとで調べてみたんですが」"


show char ter03f2 at left
with dis



voice "Erisu_0041"
e "「な、なんか調べ方、間違っているような……」"
voice "Sizuku0036"
# "【　雫　】「？？？」"


show char ter02f2 at left
with dis



voice "Erisu_0042"
e "「とりあえず、今日は七夕を楽しもうね{image=image/exch001.png}」"


show char tsi02f2 at right as r
with dis



voice "Sizuku0037"
# "【　雫　】「はい、エリス{image=image/exch001.png}」"


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

#※六夏視点
show char tta01s2
with dis



voice "Takako0006"
x "「こんばんは」"


show char tta01s2 at left
show char trk01s2 at right as r
with dis



voice "Rikka_0292"
rk "「あっ、こんばんは」"
"また、あのお姉さんとすれ違った。"
"あれっ……今日は小さな子も、一緒にいるみたい。"

hide char tta01s2 at left
hide char trk01s2 at right as r
show char tru01s2 at sleft as l
show char tta01s2
show char trk01s2 at sright as sr
with dis



voice "Runa_0000"
x "「ちょっとせんせい、この人だれ？　知り合い？」"
voice "Takako0007"
x "「同じマンションに住んでいるお姉さんよ。ほら、瑠奈も挨拶したら」"


show char tru08s2 at sleft as l
with dis



voice "Runa_0001"
x "「別に……関係ないわ」"


show char tta03s2
with dis



voice "Takako0008"
x "「もう、瑠奈ったら……」"


show char trk03s2 at sright as sr
with dis



voice "Rikka_0293"
rk "「………………」"
"この２人、どんな関係なのかしら？"
"あのお姉さんの、子供……のわけないよね？"
"それはさすがに、無理があるし。"
"じゃあ、妹さん……かな？"


show char tru01s2 at sleft as l
with dis



voice "Runa_0002"
x "「今日は七夕よね。いつもより期待していいのかしら、せんせい？」"


show char tta01s2
with dis



voice "Takako0009"
x "「そうね……色々準備はしているわ」"


show char tru02s2 at sleft as l
with dis



voice "Runa_0003"
x "「準備だって……んふふっ、せんせいやらしい{image=image/exch001.png}」"


show char tta03s2
with dis



voice "Takako0010"
x "「ええっ？　準備って、ご飯のことじゃないの？」"
"な、なんだろう……この会話。"
"妹にしては何だか、変な雰囲気があるような……"
"思わずジッと見つめてしまったら、小さな女の子とばっちり、目が合ってしまった。"


show char tru09s2 at sleft as l
with dis



voice "Runa_0004"
x "「ちょっとあなた、何見ているのよっ！」"
voice "Rikka_0294"
rk "「ご、ゴメンなさい！」"


#allClear:
hide char tru09s2 at sleft as l
hide char tta03s2
hide char trk03s2 at sright as sr
#lastBG:
#scene bg bg08c
with dis


"明らかに自分より年下の子に怒鳴られて、ワタシはあわてて部屋に戻ってしまった。"


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


show char tru03s2
with dis



voice "Runa_0005"
rn "「……さっきの人、なんだったのかしら？」"


show char tru03s2 at left
show char tta03s2 at right as r
with dis



voice "Takako0011"
t "「ご近所さんなんだから、もっと仲良くしましょうよ……うっ、これ運びずらいわね」"
voice "Runa_0006"
rn "「せんせい、それどうしたの？」"


show char tta01s2 at right as r
with dis



voice "Takako0012"
t "「昼間のうちに買っておいたのよ。七夕の準備はしてある、って言ったあったでしょう？」"
voice "Runa_0007"
rn "「そうだけど……そんな大きな笹どこに置くのよ？」"
voice "Takako0013"
t "「ベランダに、おけばいいんじゃないかしら」"


show char tru05s2 at left
with dis



voice "Runa_0008"
rn "「このマンションで、そんなことしてる人なんていないわよ。もう……恥ずかしいわ」"
voice "Takako0014"
t "「そう？　瑠奈が喜ぶと思って」"


show char tru08s2 at left
with dis



voice "Runa_0009"
rn "「わたし、もうそんなに子供じゃないわよ」"


show char tta03s2 at right as r
with dis



voice "Takako0015"
t "「……ええ、そうね……ゴメンね」"


show char tru03s2 at left
with dis



voice "Runa_0010"
rn "「うっ、そんな顔したって、しないものはしないわ」"
voice "Takako0016"
t "「……そうね、七夕ケーキも買ってきたけど、いらないわよね」"


show char tru04s2 at left
with dis



voice "Runa_0011"
rn "「け、ケーキ？」"
voice "Takako0017"
t "「星形のケーキなんて、子供っぽかったわよね……あっ！」"


show char tru08s2 at left
with dis



voice "Runa_0012"
rn "「こ、これはいただくわ……もったいないし」"


show char tta02s2 at right as r
with dis



voice "Takako0018"
t "「瑠奈{image=image/exch001.png}」"


show char tru05s2 at left
with dis



voice "Runa_0013"
rn "「わたしはただ、せんせいに付き合ってあげるだけだからね。さっさと飾り付けしちゃって、ケーキ食べましょう」"
voice "Takako0019"
t "「そうね……一緒に飾りましょう、瑠奈{image=image/exch001.png}」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**六夏の部屋・夜
scene bg bg34c
with Dis



#mes on
#system on


show char trk01f2
with dis



voice "Rikka_0295"
rk "「ああ……今日は星がとっても、良く見えるなぁ」"


show char trk02f2
with dis



voice "Rikka_0296"
rk "「七夕の日って、天気が悪い日が多いけれど、今年はそうならなくて良かったよね」"
"年に一度しか会えない、星の恋人たちの日だもんね。"


show char trk01f2
with dis



voice "Rikka_0297"
rk "「そういえば、子供の頃……リサ姉と一緒に、短冊に願い事を書いたりしたなぁ」"
voice "Rikka_0298"
rk "「リサ姉はいつも、勉強のコトとか書いてたような気がする」"


show char trk03f2
with dis



voice "Rikka_0299"
rk "「ワタシは……何、書いたんだろう……」"
voice "Rikka_0300"
rk "「うーん、もう忘れちゃったなぁ」"
"でも、今だったら……"
voice "Rikka_0301"
rk "「やっぱり……沙雪さんのこと、かな……」"
"ワタシと沙雪さんも、いつか……織姫さまと、彦星さまのように……"


show char trk06f2
with dis



voice "Rikka_0302"
rk "「……って、そんなのダメダメ、一年に一度しか会えない恋人なんて、寂しいよぉ」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**繁華街・夜
scene bg bg17c
with Dis



#mes on
#system on


show char tsy03s2
with dis



voice "Sayuki0124"
s "「はぁ～……すっかり、遅くなってしまいました……」"
voice "Sayuki0125"
s "「叔父様に頼まれた用事とはいえ、学校帰りに済まそうとするものではありませんね。もう日がすっかり落ちてしまいました」"
voice "Sayuki0126"
s "「もう、星が瞬いています……そう言えば六夏さん、今日は七夕だと仰っられておりました」"
voice "Sayuki0127"
s "「一年に一度だけしか会えない、織姫と彦星……今日はどんな気持ちでいるのでしょう？」"
voice "Sayuki0128"
s "「ベストカップルの先輩方は、恋をしている皆さんは、その切なさをご存知なのでしょうか？」"
voice "Sayuki0129"
s "「六夏さんも……知っているのでしょうか？」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**璃紗の部屋・夜
scene bg bg01c
with Dis



#mes on
#system on


show char tri02s2
with dis



voice "Risa_0460"
r "「ねぇ、美夜、見てみて、すごい綺麗な星空よ」"
"部屋の窓を開けて、空を見上げる。"
"そこには美しい星が、無数に瞬いていた。"


show char tmi01s2 at left
show char tri02s2 at right as r
with dis



voice "Miya_0222"
m "「ええ、綺麗ね」"
voice "Risa_0461"
r "「ねっ、織姫と彦星もきっと、素敵なデートをしているんでしょうね」"
voice "Miya_0223"
m "「………………」"


show char tri03s2 at right as r
with dis



voice "Risa_0462"
r "「何よ……どうせまた、乙女な妄想しているって言いたいの？」"


show char tmi02s2 at left
with dis



voice "Miya_0224"
m "「ううん、璃紗らしくって、可愛いわ{image=image/exch001.png}」"


show char tri04s2 at right as r
with dis



voice "Risa_0463"
r "「か、可愛いって……んんっ！？」"
"肩をつかまれた次の瞬間、美夜の唇が私の唇に触れていた。"


show char tmi11s2 at left
show char tri11s2 at right as r
with dis



voice "Miya_0225"
m "「ちゅっ……んふ、でも夜空の二人より、わたくしたちの方がもっと親密だと思わない？」"
voice "Risa_0464"
r "「んちゅ……ふうっ……お、思う……わ」"
voice "Miya_0226"
m "「ちゅる、ちゅっ……じゃあ、見せつけてあげましょうよ{image=image/exch001.png}」"


#※EV003
#allClear:
hide char tmi11s2 at left
hide char tri11s2 at right as r
#lastBG:
#scene bg bg01c
scene bg EV03
with Dis



voice "Risa_0465"
r "「ん……ちゅ、美夜……{image=image/exch001.png}」"
voice "Miya_0227"
m "「璃紗……可愛い、どんな星よりも輝いていて、可愛いわ」"
voice "Risa_0466"
r "「もぉ……そんな恥ずかしいこと、言っちゃ……あんっ{image=image/exch001.png}」"
"素敵な、七夕の夜。"
"私たちは久しぶりに、たっぷりと甘い時間を過ごしたのでした。"


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
jump S016


