label S026:
#S026「真夏の恋の物語」
$ save_name = "◇真夏の恋の物語"


#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


"告白の決意はしたものの、まずはチャンスを作らなくては……"
"２人だけで沙雪さんと話をするには、まず沙雪さんを誘わないといけない。"


show char trk03f2
with dis



voice "Rikka_0427"
rk "「とはいえ、どこに誘えばいいのかな……」"
"ここに来てからは、なんだかんだで団体行動が多く。"
"今日はスキューバー次はクルーズと忙しくまわりに合わせているだけで。"
"他にどんな遊び場があるかは、全然知らなかったりする。"
voice "Rikka_0428"
rk "「この場所に一番詳しいのはあの人かな、一応聞いてみよう」"


#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


scene bg bg40a
with Dis


#mes on
#system on


show char trn01f2 at left
show char trk03f2 at right as r
with dis



voice "Rena_0061"
ren "「あらっ、篠崎さんどうしたの？　よかったら飲む」"
"昼間から、ロビーでワインをたしなんでいる麗奈先生。"
"お酒はもちろん断って、用件を伝える。"


show char trk01f2 at right as r
with dis



voice "Rikka_0429"
rk "「あの、この辺のお勧めスポットを教えてもらえませんか」"


show char trn02f2 at left
with dis



voice "Rena_0062"
ren "「お勧めねぇ……ふふふっ{image=image/exch001.png}」"


show char trk03f2 at right as r
with dis



voice "Rikka_0430"
rk "「な、何ですか？」"
"麗奈先生、にやにやしてる。"
"酔っぱらっているんだろうか？"
voice "Rena_0063"
ren "「お勧めデートスポットね、いいわよ、しっかり教えてあげるわ」"


show char trk05f2 at right as r
with dis



voice "Rikka_0431"
rk "「でっ、デートって」"
voice "Rena_0064"
ren "「照れない照れない、そうね、２人っきりになれる場所といえば」"
voice "Rikka_0432"
rk "「………………」"


#allClear:
hide char trn02f2 at left
hide char trk05f2 at right as r
#lastBG:
#scene bg bg40a
with dis


"自分のやろうとしていることが、麗奈先生にはバレバレなのが恥ずかしいけれど。"
"ワタシは、それを悟られないように、あくまでお勧めスポットを聞いているだけと、自分に言い聞かせながら、メモを取る。"


show char trn01f2
with dis



voice "Rena_0065"
ren "「――とまあ、こんなとこかしら」"


show char trn01f2 at left
show char trk01f2 at right as r
with dis



voice "Rikka_0433"
rk "「ありがとうございました」"


show char trn02f2 at left
with dis



voice "Rena_0066"
ren "「ふふふ、頑張ってね……あっ、そうだわ。みんな集まって」"


#allClear:
hide char trn02f2 at left
hide char trk01f2 at right as r
#lastBG:
#scene bg bg40a
with dis


"突然、麗奈先生がその場で召集をかけた。"
"朝食を食べ終わり、今日はなにをするか相談していた先輩方が続々と集まってくる。"


show char tru03f2
with dis



voice "Runa_0060"
rn "「ねえさま、急になによ」"


show char trn01f2 at left
show char tru03f2 at right as r
with dis



voice "Rena_0067"
ren "「これからの予定だけど、今日と明日は自由行動にするから。食事の時間以外、みんな好きにしていいわよ」"


#allClear:
hide char trn01f2 at left
hide char tru03f2 at right as r
#lastBG:
#scene bg bg40a
show char trk04f2
with dis



voice "Rikka_0434"
rk "「えっ……」"


show char trk01f2
with dis



"自由にしていいって、つまりそれは。"
"麗奈先生がワタシに向かいウィンクする。"
"このまま沙雪さんを誘えってことなんですね。"
"先生に背中を押され、ワタシは勇気をもらった気分になった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**リゾートホテルの部屋・昼
scene bg bg37a
with Dis



#mes on
#system on


show char tsa01f2
with dis



voice "Sara_0136"
sr "「自由時間だって～、楓ちゃんどこに行こうかぁ～」"


show char tka01f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0111"
k "「買い物でも行く？　まだお土産あまり見てないでしょう」"


show char tsa02f2 at right as r
with dis



voice "Sara_0137"
sr "「うんうん、行く～」"


#allClear:
hide char tka01f2 at left
hide char tsa02f2 at right as r
#lastBG:
#scene bg bg37a
show char tma01f2
with dis



voice "Mai_0214"
ma "「玲緒はどこに行きたいのかな？」"


show char tma01f2 at left
show char tre01f2 at right as r
with dis



voice "Reo_0167"
re "「ワタシは部屋で、アイスを食べるわ」"


show char tma03f2 at left
with dis



voice "Mai_0215"
ma "「それ、家でもできるじゃない」"
voice "Reo_0168"
re "「オーシャンビュー、しながらだから、家とは違うわ」"


show char tma01f2 at left
with dis



voice "Mai_0216"
ma "「はいはい、今日くらいは玲緒のわがまま聞いてあげるわよ」"


#allClear:
hide char tma01f2 at left
hide char tre01f2 at right as r
#lastBG:
#scene bg bg37a
with dis


"みんながそれぞれ、好きなところにカップルで、出かけて行く中。"
"沙雪さんは一人、テラスでただずんでいた。"


show char tsy01f2
with dis



voice "Sayuki0178"
s "「………………」"


show char trk01f2
with dis



voice "Rikka_0435"
rk "「沙雪……さん……」"
"ワタシはさっき麗奈先生に教わりながらメモした紙をジッと見つめながら、最終確認。"


show char trk08f2
with dis



voice "Rikka_0436"
rk "「よし、場所もばっちり覚えた……後は、声をかけるだけ……」"
"緊張してきた……ああ、手が汗ばんでいるし。"
"どんな陸上の大会よりも、今の方が緊張している。"
"震える足を必死に動かして、沙雪さんへと歩み寄り。"
"そっと、その背中に声をかける。"


show char trk01f2
with dis



voice "Rikka_0437"
rk "「さ、沙雪さん……ちょっといいですか」"


show char trk01f2 at left
show char tsy01f2 at right as r
with dis



voice "Sayuki0179"
s "「ええ、何でしょうか？」"
"ダメだ、その穏やかな顔を見ただけで、心臓がばくばくする。"
"ああ、落ち着け……落ち着け、ワタシ。"
"喉の奥から、声をしぼり出す。"
voice "Rikka_0438"
rk "「あの……すごく景色が綺麗な場所があるって、さっき聞いたんだけど……一緒に行きませんか？」"
"言った、ついに言ってしまった。"
"ああ……イエスって、言ってくれるだろうか。"
"恐る恐る返事を待つと、沙雪さんは薔薇のような微笑みを浮かべた。"


show char tsy02f2 at right as r
with dis



voice "Sayuki0180"
s "「……はい。是非、ご一緒させて下さい」"
"その表情に、ドキドキが加速されていく。"
"つ、ついに……沙雪さんを誘ったんだ、言えたんだ！"
voice "Rikka_0439"
rk "「そ、それじゃあ、準備してから……また、ロビーで落ち合いましょう」"
voice "Sayuki0181"
s "「はい、わかりました」"


hide char tsy02f2 at right as r
with dis


"静かに去っていく沙雪さんを見つめながら、ワタシはギュッと拳を握りしめた。"


show char trk02f2
with dis



voice "Rikka_0440"
rk "「やっ……やった！！」"
"あまりの喜びに、ワタシはしばらくの間、その場に立ち尽くしたのだった……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**岩場・昼
scene bg bg41a
with Dis



#mes on
#system on


show char trk01f2
with dis



voice "Rikka_0441"
rk "「沙雪さん、足元に気をつけて、慎重に進んでください」"


show char tsy03f2
with dis



voice "Sayuki0182"
s "「は、はい……」"
"麗奈先生の教えてくれた見晴らしの良い場所に上がるまでは、ちょっとした岩場を進まなくてはならなかった。"


show char trk01f2
with dis



voice "Rikka_0442"
rk "「さあ、こっちですよ」"
"多少の歩きずらさはあるけれど、思ったほどではない。"
"それよりもワタシは、沙雪さんと２人っきりでいることに、動揺してしまう。"
"恥ずかしさもあってか、少し早歩きで進んでしまう。"
"するとつい、沙雪さんとの距離が開いてしまうのだった。"
voice "Rikka_0443"
rk "「だいぶ、景色が変わって来ましたね……あと、少しですから……」"


show char tsy01f2
with dis



voice "Sayuki0183"
s "「はい……」"
"後ろから沙雪さんが着いて来ているのは、気配で感じていたけれど。"
"照れがあって、あまり振り向けずにいた。"
"でも少し、距離が開いてきたようなので、そこでようやくワタシは振り向いた。"


show char trk04f2
with dis



voice "Rikka_0444"
rk "「あっ……」"


show char tsy03f2
with dis



voice "Sayuki0184"
s "「はぁ……はぁ、はぁ……」"
"息を切らして、沙雪さんが岩場を危なげな足取りで上がってくる。"
"その姿を見て、ワタシは激しく自己嫌悪した。"


show char trk03f2
with dis



voice "Rikka_0445"
rk "「ワタシったら……自分のことばっかりで」"
"沙雪さんのことを、あまり考えていなかった。"
"自慢ではないけれど、陸上で記録を出したりするくらいの運動神経があるワタシと、沙雪さんが同じ速さで上がってこれるはずがない。"
voice "Rikka_0446"
rk "「すいません、沙雪さん……少しペース、落としますね」"
"楽にしてあげたくて、思わず彼女に手を伸ばす。"


show char trk03f2 at left
show char tsy03f2 at right as r
with dis



voice "Sayuki0185"
s "「はぁ、はぁ……はい……ありがとうございます」"
"沙雪さんはワタシの差し出した手を、ぎゅっと握る。"
"恥ずかしさと興奮で一瞬、たじろいだ……が、彼女のその手を強く握り返す。"


show char trk08f2 at left
with dis



voice "Rikka_0447"
rk "（だって……ワタシは、騎士……なんだもんね、沙雪さんの……）"
voice "Rikka_0448"
rk "「……では、行きましょうか」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0186"
s "「はい」"
"柔らかい、沙雪さんの手。"
"ワタシは今、沙雪さんと触れ合っているんだ。"
"ああ、手を通して、ワタシのドキドキが伝わってしまうかも……それがちょっとだけ、心配だった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**岩場・昼
scene bg bg41a
with Dis



#mes on
#system on


"ようやく登りついた先で、ワタシは沙雪さんと並んで、海を眺めた。"


show char tsy02f2
with dis



voice "Sayuki0187"
s "「ああ……すごいですね、なんて綺麗なんでしょう」"
"その雄大な景色に、沙雪さんは歓喜の声を上げる。"
"それほどまでに、そこは美しかった。"
"青い海と青い空が一体化したような、透き通るような世界……"


show char trk01f2 at left
show char tsy02f2 at right as r
with dis



voice "Rikka_0449"
rk "「ここまで来た甲斐、ありましたね……」"
"ここを教えてくれた麗奈先生に、感謝しなくちゃ。"
"そう思いながら、この雄大な光景に見とれていると、ふと熱い視線を感じた。"
voice "Rikka_0450"
rk "「……沙雪……さん」"
voice "Sayuki0188"
s "「六夏さん……こんな素敵な場所に誘って頂いて、ありがとうございます」"
voice "Rikka_0451"
rk "「そ、そんな………………あっ」"
"……きゅううっ～"


show char trk05f2 at left
with dis



voice "Rikka_0452"
rk "「こ、こんな時に……うぅっ……」"
"どうしてこんなタイミングで、お腹が鳴っちゃうのよ、もう！"
voice "Sayuki0189"
s "「……ふふっ、ふふふっ{image=image/exch001.png}」"
voice "Rikka_0453"
rk "「沙雪さん……そんなに笑わなくても……」"
voice "Sayuki0190"
s "「だっ、だって………………あっ」"
"……きゅぅ……きゅぅぅ～"


show char tsy05f2 at right as r
with dis



voice "Sayuki0191"
s "「やっ、あぁ……私、まで……うぅっ、恥ずかしい……です」"
"なんと沙雪さんも、お腹が鳴ってしまった。"
"この場所まで夢中になって、歩いてきたけれど……もうとっくに、お昼を過ぎていた。"
"お腹が空いても、当然だった。"
"さっきまで楽しげに笑っていた沙雪さんは、真っ赤になった顔をうつむかせてしまった。"
voice "Sayuki0192"
s "「ぁぁ……本当に恥ずかしい……私ったら……」"
voice "Rikka_0454"
rk "「それを言うなら、ワタシも……恥ずかしい、です」"
"ワタシもきっと、沙雪さんと同じくらい、赤くなっているに違いない。"
"ああ、どうにかしないと……"
"するとふと、ワタシは思い出した……しょってきたリュックの中に、入っているものの事を。"


show char trk01f2 at left
with dis



voice "Rikka_0455"
rk "「沙雪さん、お昼にしましょう！　お弁当、作ってもらってきたんです」"


show char tsy04f2 at right as r
with dis



voice "Sayuki0193"
s "「まぁ、お昼まで用意してあったんですか？」"


show char trk02f2 at left
with dis



voice "Rikka_0456"
rk "「ええ、ちょっとした遠足です」"
"顔を上げてくれた沙雪さんは、嬉しそうに微笑んだ。"


show char tsy02f2 at right as r
with dis



voice "Sayuki0194"
s "「六夏さんって本当に、気が利くのですね……皆さんに慕われるのも、当然ですね」"


show char trk05f2 at left
with dis



voice "Rikka_0457"
rk "「い、いえ、そんな……大したこと、ありません」"
"沙雪さんに誉められて、頬がゆるみそうになるのを引きしめながら、お昼の用意をする。"
"お弁当はサンドイッチと、美味しそうなおかずばかりだった。"


show char trk01f2 at left
with dis



voice "Rikka_0458"
rk "「さあ、いただきましょうか」"
voice "Sayuki0195"
s "「本当に、美味しそうですね……では、いただきます」"


#**青空
#allClear:
hide char trk01f2 at left
hide char tsy02f2 at right as r
#lastBG:
#scene bg bg41a
scene bg bg42a
with Dis



"綺麗な景色を見ながら、沙雪さんと食事するのはとても楽しかった。"
"２人ともお腹が空いていたから、あっと言う間に食べ終わってしまって。"
"食後はゆったりしながら、また２人で海を眺めて。"
"好きな人と、静かに波の音を聞いているだけで、本当に幸せな気持ちになってくる。"


#**岩場・昼
scene bg bg41a
with Dis



show char trk01f2
with dis



voice "Rikka_0459"
rk "「こんな綺麗な景色が見れるなら、デジカメ持ってくれば良かったですね」"


show char trk01f2 at left
show char tsy01f2 at right as r
with dis



voice "Sayuki0196"
s "「ええ、そうですね……でも、ここだけの思い出としてとっておくのも、素敵だと、私は思います」"
voice "Rikka_0460"
rk "「沙雪さん……そう、ですね……」"
"ワタシと一緒に見た景色を、大事な思い出として、アナタが心に残してくれるなら。"
"こんなに嬉しいことはないよね。"
voice "Rikka_0461"
rk "「じゃあワタシも、しっかり思い出に残せるよう、今のうちにいっぱい見ておきますね」"
voice "Sayuki0197"
s "「……ええ」"
voice "Rikka_0462"
rk "「………………」"


#allClear:
hide char trk01f2 at left
hide char tsy01f2 at right as r
#lastBG:
#scene bg bg41a
with dis


"そして……会話が途切れて。"
"いつもなら、周りにリサ姉やみんながいるから、騒がしいけれど。"
"今日は誰もいない……ワタシと沙雪さんの、２人だけ。"
"その分、波の音が大きく、耳に響く。"
"沙雪さん……退屈していないかな？"
"心配になって、隣りをチラッと見てしまうと……"


show char trk03f2
with dis



voice "Rikka_0463"
rk "「あっ……」"


show char trk03f2 at left
show char tsy03f2 at right as r
with dis



voice "Sayuki0198"
s "「………………」"
"そこには寂しそうに海を見つめている、沙雪さんの横顔があった。"
"こんな彼女を見るの、初めてだ。"
"彼女はいつだって、穏やかに笑っているから。"
voice "Rikka_0464"
rk "（どうしたんだろう……疲れちゃったのかな。それとも何か、悩みでもあるとか……）"
"気になってならないワタシは、余計なお世話かも……と思いつつも、つい聞いてしまった。"
voice "Rikka_0465"
rk "「あ、あの……沙雪さん、何か心配ごとでも？」"
voice "Sayuki0199"
s "「………………」"
"沙雪さんと目が合う。"
"でも彼女は、何も答えてくれない。"


show char tsy02f2 at right as r
with dis



voice "Sayuki0200"
s "「……気にしないで、ください。大丈夫ですから」"
voice "Rikka_0466"
rk "「あっ……」"
"いつものように、にっこりと微笑む。"
"でもその笑顔でさえ、ワタシにはどこか寂しく思えてしまった。"
voice "Sayuki0201"
s "「こんなに楽しい旅行、楽しい休日……初めてです。きっと、六夏さんが一緒だから……」"
voice "Rikka_0467"
rk "「そ、そんな、ワタシなんか……」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0202"
s "「いいえ……実は私、ベストカップルの先輩方に囲まれて、ずっと緊張していたんです」"
voice "Rikka_0468"
rk "「沙雪さんが？　そうなんですか？？」"
"いつだって堂々としていて、とてもそうは見えなかったのに。"
voice "Sayuki0203"
s "「環境整備委員会でご一緒している優菜さまや七海さま以外、あまり存じ上げない方ばかりでしたから……」"


show char trk01f2 at left
with dis



voice "Rikka_0469"
rk "「ワタシもですよ。リサ姉以外、誰も知らなかったから、最初は緊張でガチガチでした」"


show char tsy02f2 at right as r
with dis



voice "Sayuki0204"
s "「本当にそうでしたね、六夏さんは……ふふっ」"


show char trk05f2 at left
with dis



"恥ずかしくなってうつむくと、沙雪さんは言った。"


show char tsy01f2 at right as r
with dis



voice "Sayuki0205"
s "「私たち……一緒だったんですね」"
voice "Rikka_0470"
rk "「え、ええ……そうですね」"


show char trk02f2 at left
show char tsy02f2 at right as r
with dis



"２人で思わず、笑い合う。"
"こんなにすごい沙雪さんも、ワタシと同じだったんだ。"
"それを聞いて、何だか前よりも、沙雪さんとの距離が縮まったみたいに思えた。"
"彼女をグッと、身近に感じられた。"
"それだけでも、ここに来て良かったと思えた。"
"あまりに嬉しくなったワタシはいつの間にか、さっきまでの沙雪さんの寂しそうな様子を忘れてしまった。"


show char trk01f2 at left
with dis



voice "Rikka_0471"
rk "「じゃあ、そろそろ戻りましょうか？　あんまり遅くなると、みんなに心配かけますから……」"


show char tsy01f2 at right as r
with dis



voice "Sayuki0206"
s "「ええ、そうですね……行きましょう」"
"そう言って、沙雪さんが自分から手を差し出してきた。"


show char trk03f2 at left
with dis



voice "Rikka_0472"
rk "「沙雪……さん？？」"
voice "Sayuki0207"
s "「帰りも……繋いでくださいね」"


show char trk01f2 at left
with dis



voice "Rikka_0473"
rk "「あっ、そうですね……岩場、歩きづらいですし」"
voice "Sayuki0208"
s "「お願いしますね、六夏さん」"
voice "Rikka_0474"
rk "「ま、まかせて、ください」"
"ああ、何だか舞い上がってしまう。"
"沙雪さんからワタシに、手を差し伸べてくれるなんて。"
"今まで、頼りになるとか、騎士だとか、色々と言われていたワタシだけど。"
"当たり前のことをしているだけで、何を言ってるんだろう……って思っていた。"
"でもこうして、沙雪さんに頼りにされると。"
"どんどん、頼りにして欲しいって思いたくなる。"
"姫を守る、騎士……本物の騎士に、なりたくなる。"
voice "Rikka_0475"
rk "「では、行きますか……姫」"


show char tsy04f2 at right as r
with dis



voice "Sayuki0209"
s "「えっ！？」"


show char trk05f2 at left
with dis



voice "Rikka_0476"
rk "「い、いえ……行きましょうか、沙雪さん」"


show char tsy02f2 at right as r
with dis



voice "Sayuki0210"
s "「はい……ふふっ」"


#allClear:
hide char trk05f2 at left
hide char tsy02f2 at right as r
#lastBG:
#scene bg bg41a
with dis


"行きと違って、帰りは岩場を下るので、足をすべらせたら大変だった。"
"ワタシは慎重に、彼女の手を引いていった。"
"他の誰よりも大切な、姫の手を……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**ビーチ・昼
scene bg bg39a
with Dis



#mes on
#system on


show char trk01f2
with dis



voice "Rikka_0477"
rk "「……はぁ、やっと着きましたね」"


show char trk01f2 at left
show char tsy01f2 at right as r
with dis



voice "Sayuki0211"
s "「はい、ありがとうございます。帰りは私のペースに合わせてくださったんですね、六夏さん」"
voice "Rikka_0478"
rk "「いいえ……行きが早すぎたんです」"


show char tsy02f2 at right as r
with dis



voice "Sayuki0212"
s "「ありがとうございます。六夏さんはお優しい方ですね」"


show char trk05f2 at left
with dis



voice "Rikka_0479"
rk "「そ、そんな……」"
"沙雪さんこそ、優しくて天使みたいですよ……"
"……とは、さすがに恥ずかしくて言えなかった。"


show char tsy01f2 at right as r
with dis



voice "Sayuki0213"
s "「明日も、自由行動なんですよね……六夏さん、何かご予定は？」"


show char trk03f2 at left
with dis



voice "Rikka_0480"
rk "「い、いえ……特には……」"
"麗奈先生、今日と明日の両方、自由行動だって言っていたっけ……"
"今日のことがいっぱいいっぱいで、すっかり忘れていたよ。"
voice "Sayuki0214"
s "「明日、なのですが……この島のガイドを見て、行きたいなぁと思うところがありまして……」"


show char trk01f2 at left
with dis



voice "Rikka_0481"
rk "「はい……」"
voice "Sayuki0215"
s "「できれば六夏さんに、一緒に行って頂けたらと……」"


show char trk04f2 at left
with dis



voice "Rikka_0482"
rk "「……えっ！？」"
"沙雪さんからの……お誘い！？"
"これって、ひょっとして夢？？"


show char tsy03f2 at right as r
with dis



voice "Sayuki0216"
s "「いかが……でしょうか？」"


show char trk08f2 at left
with dis



voice "Rikka_0483"
rk "「は、はい、行きます、行かせてください！！」"


#allClear:
hide char trk08f2 at left
hide char tsy03f2 at right as r
#lastBG:
#scene bg bg39a
with dis


"うんうんと、何度も頷く。"
"これが夢だっていい、こんな幸せな夢なら、いくらでも見ていたいから。"
"ああ、明日も沙雪さんと２人になれる……夢じゃないんだよね。"
"もう何だか幸せ過ぎて、恐くなりそうな気分だった。"


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
jump S027


