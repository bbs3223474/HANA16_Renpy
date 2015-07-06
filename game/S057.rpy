#「有能な社長秘書・璃紗」

label S057:
$ save_name = "◇有能な社長秘書・璃紗"


#**委員会室・昼
scene bg bg30a
with Dis


play music "sound/BGM12.ogg"

#mes on
#system on


show char tka01s2
with dis



voice "Kaede_0128"
k "「優菜さん、こちらのチェックお願いします」"


show char tka01s2 at left
show char tyu01s2 at right as r
with dis



voice "Yuuna_0182"
y "「はい、今行きます」"


#allClear:
hide char tka01s2 at left
hide char tyu01s2 at right as r
#lastBG:
#scene bg bg30a
show char trk03s2
with dis



voice "Rikka_1556"
rk "「プログラム見本、あがってきましたけど、これどうすれば……」"


show char tna01s2 at left
show char trk03s2 at right as r
with dis



voice "Nanami0288"
n "「それ、こちらにください」"


#allClear:
hide char tna01s2 at left
hide char trk03s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"今日もイベント実行委員の仕事は結構、盛りだくさん。"
"でも皆さん次々と、素早く仕事をこなしていく。"
"昨年からの引き続きだから、メンバーとしての結束もあるし。"
"新しく入った２人も、なかなかの人材だものね。"


show char tri01s2
with dis



voice "Risa_1139"
r "「このまま文化祭まで、スムーズに準備は進みそう……」"
"問題ありかと思われていた、美夜だって。"
"最近はすっごく、真面目になったもの。"


show char tmi03s2 at left
show char tri01s2 at right as r
with dis



voice "Miya_0706"
m "「ん……どうしたの、璃紗。そんなにじっと、わたくしを見つめて？」"
voice "Risa_1140"
r "「別に……美夜が真面目にやっているかなって、思って」"


show char tmi02s2 at left
with dis



voice "Miya_0707"
m "「ふふふっ、そんなとってつけたような言い訳なんて、いらないわ」"


show char tri03s2 at right as r
with dis



voice "Risa_1141"
r "「はぁ……？」"
voice "Miya_0708"
m "「仕事で疲れている時、ついわたくしの顔が見たくなるのは当然だわ。なんならもっと近くで、たっぷり見つめていてもいいのよ」"
voice "Risa_1142"
r "「いいわよ、そんなつもりじゃないから」"
voice "Miya_0709"
m "「あら、遠慮なんてしなくていいのに」"
"そう言って、なんだかポーズを取る美夜。"
voice "Risa_1143"
r "「うううっ……なんかキラキラしているわ」"
"ちょっと、圧倒されなくもないわね。"
"自信過剰なところもあるけれど、美夜が綺麗なのは確かだし……"
voice "Miya_0710"
m "「ふふふっ、好きなだけわたくしを見つめていていいのよ、璃紗なら{image=image/exch001.png}」"


show char tri04s2 at right as r
with dis



voice "Risa_1144"
r "「な、なななな、何よぉぉっ」"
"いつの間にやら、ものすごく顔が近いんですけど……"
"こんなたくさんの人がいる前で、今にも触れてしまいそうな距離。"
"ダメ、胸がドキドキしちゃうよ。"


show char tri05s2 at right as r
with dis



voice "Risa_1145"
r "「だ、だめぇ……」"
voice "Miya_0711"
m "「何がだめなのかしら、璃紗？」"


#**委員会室・昼

#//SE：ドアの開く音
#♀SE003
play sound "sound/SE003.ogg"


#allClear:
hide char tmi02s2 at left
hide char tri05s2 at right as r
#lastBG:
#scene bg bg30a
show char tma03s2
with dis



voice "Mai_0245"
ma "「すいません、遅くなりましたー」"
"急にドアが開いて、麻衣さまが飛び込んでくる。"
"ああ、助かったわ。"
"私はあわてて、美夜から距離をとって離れる。"


show char tmi03s2
with dis



voice "Miya_0712"
m "「もう……あと少しだったのに、残念だわ」"


show char tmi03s2 at left
show char tri09s2 at right as r
with dis



voice "Risa_1146"
r "「何があと少しなのよ～！」"
"最近の美夜は本当に、大胆すぎるわ。"


#allClear:
hide char tmi03s2 at left
hide char tri09s2 at right as r
#lastBG:
#scene bg bg30a
show char tre08s2
with dis



voice "Reo_0189"
re "「まーいー、やっと来た！　遅いわよ」"


show char tma01s2 at left
show char tre08s2 at right as r
with dis



voice "Mai_0246"
ma "「はいはい、すぐに手伝いますよ～」"


show char ter01f2 at left
show char tsi01f2 at right as r
with dis



voice "Erisu_0116"
e "「麻衣さんが遅れるなんて、めずらしいよね～」"
voice "Sizuku0098"
sk "「何かあったのでしょうか？」"

hide char ter01f2 at left
hide char tsi01f2 at right as r
show char tma01s2 at sleft as l
show char ter01f2
show char tsi01f2 at sright as sr
with dis



voice "Mai_0247"
ma "「あっ、エリスさまたちも手伝いにいらしてたんですね。ありがとうございます」"


show char ter02f2
with dis



voice "Erisu_0117"
e "「麻衣さんがいない間は、ワタシがしっかり玲緒の子守りをしていたよ」"


#allClear:
hide char tma01s2 at sleft as l
hide char ter02f2
hide char tsi01f2 at sright as sr
#lastBG:
#scene bg bg30a
show char tre09s2
with dis



voice "Reo_0190"
re "「子守ってなによー」"


show char tma02s2
with dis



voice "Mai_0248"
ma "「あはははっ、重ね重ね、お礼を申し上げます」"


show char tma02s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0191"
re "「お礼なんていらないわよ、ワタシが遊んであげていたんだから」"
"ぎゃあぎゃあ騒ぐ玲緒さまをよそに、麻衣さまはすぐに作業を始めた。"


#allClear:
hide char tma02s2 at left
hide char tre08s2 at right as r
#lastBG:
#scene bg bg30a
show char tma01s2
with dis



voice "Mai_0249"
ma "「さてと、遅れた分を早く、取り戻さないとね」"


show char tyu01s2 at left
show char tma01s2 at right as r
with dis



voice "Yuuna_0183"
y "「そんなに気にしなくてもいいと思うわ。みんなそれぞれ、クラスの用事とか色々あるんだから、お互い様よ」"


show char tma03s2 at right as r
with dis



voice "Mai_0250"
ma "「それはそうなんだけど、今日の場合はクラスメートに捕まって……その、恋愛相談みたいなものをされちゃったんですよ」"


show char tsa02s2 at left
with dis



voice "Sara_0178"
sr "「恋愛相談！？　なんか面白そう」"
"うんうん、私も紗良さんに同意。"
"思わず、耳を傾けてしまう。"
voice "Mai_0251"
ma "「別に、期待するほどの内容でもないんですけどねー」"


show char tma01s2 at right as r
with dis



voice "Mai_0252"
ma "「憧れの人に『文化祭を一緒にまわりませんか？』と声をかけたいんですが、どうしたらいいんでしょうか……みたいな」"
voice "Sara_0179"
sr "「イベントを利用して、憧れの人と仲良くなりたいって、何とも乙女心だよね～」"


show char tma01s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0192"
re "「ふん、なんで麻衣にわざわざ、そんなこと相談するのかしら……」"


show char tma02s2 at left
with dis



voice "Mai_0253"
ma "「あらあら、玲緒ったら焼きもちかしら？」"


show char tre04s2 at right as r
with dis



voice "Reo_0193"
re "「ち、違うわよっ！」"


#allClear:
hide char tma02s2 at left
hide char tre04s2 at right as r
#lastBG:
#scene bg bg30a
show char tka01s2
with dis



voice "Kaede_0129"
k "「私もそれと似たような相談なら、受けたことはあるわ」"


show char tsa01s2
with dis



voice "Sara_0180"
sr "「紗良もだよ～」"


show char tmi01s2
with dis



voice "Miya_0713"
m "「……なるほどね」"
"めずらしく美夜が興味深そうに、みんなの話を聞いている。"


show char tna03s2 at left
show char tmi01s2 at right as r
with dis



voice "Nanami0289"
n "「頷いているけれど、美夜さんにも同じ経験あるの？」"


show char tna01s2 at left
with dis



voice "Miya_0714"
m "「それはないけれど……ベストカップルなんて公式に認められている皆さんだから、恋愛経験には長けていると思われているんじゃないかしら？」"
voice "Nanami0290"
n "「あっ、そうか！　だからそういった相談が多いってことなんだね」"
voice "Miya_0715"
m "「……でもこれ、逆に使えそうね」"


show char tyu01s2 at left
with dis



voice "Yuuna_0184"
y "「美夜ちゃん、何に使えるの？」"
voice "Miya_0716"
m "「ベストカップル占いの部屋みたいなのを作ったら、いいビジネスになりそうじゃないかしら」"


show char tmi01s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_1147"
r "「占い？　私たち占いなんて、とてもできないわよ」"
voice "Miya_0717"
m "「ああいうのはほとんど、恋愛相談みたいなものだわ」"
voice "Miya_0718"
m "「彼女たちはただ話を聞いてもらいたいだけなんだから、黙って聴いてあげて、最後にちょっとしたアドバイスを言うだけで十分なのよ」"


show char tri01s2 at right as r
with dis



voice "Risa_1148"
r "「確かに……ベストカップルである皆さんが話を聞いてくれるだけで、人が集まりそうかも」"


#allClear:
hide char tmi01s2 at left
hide char tri01s2 at right as r
#lastBG:
#scene bg bg30a
show char tyu01s2
with dis



voice "Yuuna_0185"
y "「美夜ちゃん、面白いこと考えるわね。文化祭の演し物（だしもの）、それでも良かったかもしれないわね」"


show char trk01s2
with dis



voice "Rikka_1557"
rk "「沙雪さんがベールをかぶって、占い師っぽい格好したら……すごく雰囲気でるかも」"


show char tma02s2 at left
show char trk01s2 at right as r
with dis



voice "Mai_0254"
ma "「本当ね、すごく可愛いと思うわ♪」"

hide char tma02s2 at left
hide char trk01s2 at right as r
show char tma02s2 at sleft as l
show char trk01s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0851"
s "「占い師ですか？　よくわかりませんが、六夏さんが望むのなら、私……その格好をしてみたいです」"


show char trk01s2 at sleft as l
show char tsy01s2
show char ter02f2 at sright as sr
with dis



voice "Erisu_0118"
e "「ふふふっ、沙雪、ノリ気だね♪」"


#allClear:
hide char trk01s2 at sleft as l
hide char tsy01s2
hide char ter02f2 at sright as sr
#lastBG:
#scene bg bg30a
with dis


"作業をしながら、みんな美夜の提案した、占いの部屋の話に夢中になっていた。"
"１年前なら、みんながお喋りしていても、黙々と作業を続けるだけの美夜だったのに。"
"今は普通に、みんなと交流している。"
"それが……なんか、すごく嬉しい。"
"玲緒さまに対して、麻衣さまが抱いている気持ちに近いかも。"


show char tmi03s2 at left
show char tri02s2 at right as r
with dis



voice "Miya_0719"
m "「璃紗……にやにやして、どうしたのかしら？」"
voice "Risa_1149"
r "「美夜がね、皆さんと仲良くしているのが、なんか嬉しいのよ」"


show char tmi01s2 at left
with dis



voice "Miya_0720"
m "「………………ふっ」"
"私の発言に、怒るかも……と思ったけれど、美夜は小さく微笑んだ。"
voice "Miya_0721"
m "「皆さん優秀だから、今のうちに仲良くなっておこうと思って……将来、私の会社で働いてもらうかも知れないし」"


show char tri04s2 at right as r
with dis



voice "Risa_1150"
r "「ええええっ！？」"
"まさか、そんなことを企んで……いや、考えていたなんて。"


show char tri03s2 at right as r
with dis



voice "Risa_1151"
r "「美夜、それ冗談よね？」"
voice "Miya_0722"
m "「さあ……でも璃紗は当然、わたくしに着いてくるでしょう？」"
voice "Risa_1152"
r "「それは……まあ、そうだけど」"
voice "Miya_0723"
m "「璃紗はもちろん、わたくし付きの秘書よ」"
voice "Risa_1153"
r "「ひ、秘書……」"
voice "Miya_0724"
m "「わたくしのすぐ隣にいて、わたくしのマネジメントはもちろん、ありとあらゆることをサポートするのよ」"
voice "Risa_1154"
r "「はぁ、なんだかすごそうだわ」"
voice "Miya_0725"
m "「そして、仕事の合間には……」"


show char tri01s2 at right as r
with dis



voice "Risa_1155"
r "「もちろん、お茶をいれるのね♪」"


show char tmi02s2 at left
with dis



voice "Miya_0726"
m "「……違うわよ、ふふふっ……あんな事やこんな事、しちゃうのよ{image=image/exch001.png}」"


show char tri04s2 at right as r
with dis



voice "Risa_1156"
r "「あんな事や、こんな事って……っ！！」"
"私の頭の中で、こないだアトリエでした、美夜とのエッチが思い浮かんでしまった。"
"も、もしかして……"


show char tri05s2 at right as r
with dis



voice "Risa_1157"
r "「だ、だめよ、職場でそんなことするのは、イケナイと思うわ」"


show char tmi01s2 at left
with dis



voice "Miya_0727"
m "「校内ならいいのに？　おかしいわね」"


show char tri03s2 at right as r
with dis



voice "Risa_1158"
r "「そ、それは……」"


show char tyu02s2 at left
with dis



voice "Yuuna_0186"
y "「あらあら、なんか楽しそうな話をしているわね」"
voice "Risa_1159"
r "「えっ？」"

hide char tyu02s2 at left
hide char tri03s2 at right as r
show char tyu02s2 at sleft as l
show char tri03s2
show char tna01s2 at sright as sr
with dis



voice "Nanami0291"
n "「璃紗さんって将来、美夜さんの秘書になるの？」"
"まさか今の話を、聞かれていた！？"
"さっきまでみんな、占い部屋の話に夢中だったのに。"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0181"
sr "「だって、なんか面白そうな話、聞こえちゃったんだもん{image=image/exch001.png}」"


#allClear:
hide char tsa02s2 at sleft as l
hide char tri03s2
hide char tna01s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tri05s2
with dis



"ううううっ、もぉ、恥ずかしい！！"


show char tmi01s2 at left
show char tri05s2 at right as r
with dis



voice "Miya_0728"
m "「思い切って皆さんの前で、将来の進路を発表するのも、いいんじゃないかしら」"
voice "Risa_1160"
r "「しっ、しないわよ～」"


#allClear:
hide char tmi01s2 at left
hide char tri05s2 at right as r
#lastBG:
#scene bg bg30a
with dis


"するわけないじゃない。"
"私は作業に集中するフリをして、後はもう何も言わなかった。"
"そこでようやく、話題がまた別な方に流れていった。"
"でも。"
"将来、もしそんな風に美夜とずっと一緒にいられたら、恥ずかしいけど……嬉しいかも。"
"秘書兼、妻……みたいな感じで。"

#//（以下妄想）

#※CU10
show char CU10
with dis



voice "Miya_0729"
m "「璃紗、今日のわたくしのスケジュール、どうなっているのかしら？」"
voice "Risa_1161"
r "「昼からは、ふぐり商事と食事会……その後は本社に戻り、会議になっていますわ」"
voice "Miya_0730"
m "「その後は……？」"
voice "Risa_1162"
r "「特に、何もありませんが」"
voice "Miya_0731"
m "「本当に、ないのかしら？」"
voice "Risa_1163"
r "「待って下さい、社長。そう言われますと、気になります……もう一度、スケジュール管理チェックして来ますね」"
voice "Miya_0732"
m "「………………」"
voice "Risa_1164"
r "「安心して下さい、社長。やっぱり会議で終わりです」"
voice "Miya_0733"
m "「もぉ……だめな秘書さんね、大事な事を忘れているわ」"
voice "Risa_1165"
r "「えっ？」"
voice "Miya_0734"
m "「その後のスケジュールはね……わたくしが、璃紗をたくさん可愛がるのよ{image=image/exch001.png}　決まっているじゃない」"
voice "Risa_1166"
r "「み、美夜……」"
voice "Miya_0735"
m "「ふふふっ、今日も一日頑張りましょうね{image=image/exch001.png}」"
voice "Risa_1167"
r "「え、ええ……頑張りますっ{image=image/exch001.png}」"

#//（妄想終了）

#**委員会室・昼
show char tri02s2
with Dis



voice "Risa_1168"
r "「ふふっ……頑張ります、社長……んふふっ{image=image/exch001.png}」"


show char tri02s2 at left
show char trk03s2 at right as r
with dis



voice "Rikka_1558"
rk "「リサ姉、さっきから手が止まってるよ？」"

hide char tri02s2 at left
hide char trk03s2 at right as r
show char tsa02s2 at sleft as l
show char tri02s2
show char trk03s2 at sright as sr
with dis



voice "Sara_0182"
sr "「これは……むふふ、きっと美夜ちゃんとの楽しい秘書生活を、妄想しているみたいだね♪」"


show char tka02s2 at sleft as l
show char tsa02s2
show char tri02s2 at sright as sr
with dis



voice "Kaede_0130"
k "「璃紗さんって本当に、美夜さんのことが好きなのねぇ」"


#allClear:
hide char tka02s2 at sleft as l
hide char tsa02s2
hide char tri02s2 at sright as sr
#lastBG:
#scene bg bg30a
show char tri04s2
with dis



voice "Risa_1169"
r "「……へっ………………えぇぇっ！？」"
"まわりのみんなの生暖かい眼差しで、現実に戻ってこさせられた。"


show char tri03s2
with dis



voice "Risa_1170"
r "「あ、あの……今はちょっと、ぼんやりしてただけで……」"


show char tsa02s2 at left
show char tri03s2 at right as r
with dis



voice "Sara_0183"
sr "「大丈夫大丈夫、わかってるから{image=image/exch001.png}」"

hide char tsa02s2 at left
hide char tri03s2 at right as r
show char tsa02s2 at sleft as l
show char tri03s2
show char tna02s2 at sright as sr
with dis



voice "Nanami0292"
n "「璃紗さんも、わたしと同じで妄想しちゃうんだよね♪」"
"私たち、なんでもわかってますから……みたいな目で、見つめられてしまって。"
"今度こそ本当に恥ずかしくて、私はまた無言のまま、作業を続けたのでした。"


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


$ _skipping = False
$ _dismiss_pause = False
#log off

scene image "image/eyecatch02.png"
with vs

pause 3

scene black
with Dis

#log on
$ _skipping = True
$ _dismiss_pause = True


#//END
jump S058



