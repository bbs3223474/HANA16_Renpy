#「麻衣と雫の逆襲！？」

label S107:
$ save_name = "◇麻衣と雫の逆襲！？"


#**旧校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#♂MP08
play music "sound/BGM08.ogg"


show char tma03s2
with dis



voice "Mai_0433"
ma "「後は……つけられていないわね」"
"放課後、わたしはあたりを見回す。"
"挙動不審に見られるかもしれないけれど、それも仕方のないこと。"
"例の『リリ・プラチナム』の会員たちが神出鬼没にどこでも現れて、相変わらず玲緒にエリスさまの後をついで欲しいと迫ってくる。"
voice "Mai_0434"
ma "「だからって、変に係わると今度はわたしと雫さまでもいいなんて言い出すし」"
"本当に油断ならない。"
"わたしはすばやく廊下を通り過ぎ、イベント委員のある教室へと急ぐ。"
voice "Mai_0435"
ma "「文化祭の準備も、やらないといけないことがたまっているのよね」"
"頭の中で、これからの作業を考える。"
"優菜さんに書類のチェックを頼んでいたから、まずはそれをもらって……後は足りない備品のリストを作って。"


show char tre09p
with dis



voice "Reo_0314"
re "「もう～、しつこいわよ、アンタたち！」"


show char tma03s2
with dis



voice "Mai_0436"
ma "「んっ？」"
"思考を妨げる声、それは中庭から聞こえてきた。"
voice "Mai_0437"
ma "「あれは、玲緒！？」"
"見れば玲緒が、ファンクラブの子たちに囲まれていた。"
"先に委員会に行ってなさいと伝えておいたのに、何で中庭なんかに……"
"その理由はすぐにわかった。"
"玲緒の隣には、エリスさまがいたからだ。"
"エリスさまは隣接している短大から、よく中庭を通ってこっちの校舎にやってくる。"
"エリスさまの姿を見かけた玲緒が、後先考えずに走り寄り。"
voice "Mai_0438"
ma "「いつものように、勝負をしかけたりして大騒ぎしているところを、彼女たちに見つけられた」"
"まず、そんなところだろう。"
voice "Mai_0439"
ma "「見かけたからには無視するわけにはいかないわよね……」"


#allClear:
hide char tma03s2
#lastBG:
#scene bg bg05a
with dis


"巻き込まれるとわかっていながらも、わたしも中庭に向かった。"


#**中庭・昼
scene bg bg21a
with Dis



show char tma01s2
with dis



voice "Mai_0440"
ma "「玲緒！」"


show char tre01s2
with dis



voice "Reo_0315"
re "「あっ、麻衣」"
"わたしの出現で、玲緒たちのまわりを囲っていたファンクラブの子たちが、一瞬だけ離れてくれる。"


show char ter01f2
with dis



voice "Erisu_0169"
e "「麻衣さん、ごきげんよう」"


show char tma01s2 at left
show char ter01f2 at right as r
with dis



voice "Mai_0441"
ma "「ごきげんよう、エリスさま、これってやっぱり」"
voice "Erisu_0170"
e "「んー、みんなまだあきらめられないみたいで、玲緒をどうしても後継者に迎えたいって」"


#allClear:
hide char tma01s2 at left
hide char ter01f2 at right as r
#lastBG:
#scene bg bg21a
show char tre07s2
with dis



voice "Reo_0316"
re "「だーかーらー、ワタシはやらないって」"
"顔を真っ赤にさせて、怒りだす玲緒。"


show char tre07s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0171"
e "「まあまあ、玲緒も落ち着きなよ」"
"エリスさまは、ファンクラブの会員たちと玲緒の間に立たされて、大変そうだわ。"


#allClear:
hide char tre07s2 at left
hide char ter01f2 at right as r
#lastBG:
#scene bg bg21a
with dis


voice "Mobkaiina0032"
ka "「なにがそんなに、玲緒さまはお嫌なんでしょうか？」"
voice "Mobkaiinb0015"
kb "「麻衣さまは、どう思いますか？」"


show char tma03s2
with dis



voice "Mai_0442"
ma "「わ、わたしは……」"
"そう聞かれても。"
"『玲緒は人見知りの面倒くさがりだから』で済んじゃう問題だけど。"
"そんなことは言えないわよね。"
"彼女たちにとって『リリ・プラチナム』は、特別な存在なのだから。"
voice "Mobkaiina0033"
ka "「そういえば、麻衣さま、この間のお話は考えてくれましたか？」"
voice "Mai_0443"
ma "「えっ？」"
"それって、もしかして。"
"わたしと雫さまのファンクラブを作るってこと！？"
"いやよ、冗談じゃないわ。"
"何よりも、キャラじゃないもの。"
voice "Mai_0444"
ma "「ごめんね……玲緒」"
"わたしは、玲緒の小さい体をぐいっとひっぱった。"


show char tma03s2 at left
show char tre03s2 at right as r
with dis



voice "Reo_0317"
re "「なにするのよ、麻衣」"
"そして、会員の子たちの前に差し出す。"


show char tma01s2 at left
with dis



voice "Mai_0445"
ma "「わたしはイヤだけど、玲緒はやってあげればいいのに。『２代目リリ・プラチナム』」"


show char tre04s2 at right as r
with dis



voice "Reo_0318"
re "「麻衣はやらなくて、どうしてわたしはやるのよ？」"
voice "Mai_0446"
ma "「だって、後輩の役に立てれば、玲緒ももっと成長を……」"


show char tre09s2 at right as r
with dis



voice "Reo_0319"
re "「ぜぇぇぇーーーーーーーたいに、イヤよ！！」"
"さっきよりも、さらに大きな声で玲緒は否定する。"


show char tre07s2 at right as r
with dis



voice "Reo_0320"
re "「麻衣ったら、自分だってやりたくないくせに、ワタシに押しつけようとしないで」"


show char tma03s2 at left
with dis



voice "Mai_0447"
ma "「そ、それは……」"
"それは確かにその通りなんだけど。"
"どうしたものかと、悩んでいるとエリスさまが提案をしてきた。"


show char tre07s2 at left
show char ter01f2 at right as r
with dis



voice "Erisu_0172"
e "「じゃあさ玲緒、こういうのはどう？」"


show char tre08s2 at left
with dis



voice "Reo_0321"
re "「なによ」"
voice "Erisu_0173"
e "「ワタシと玲緒で、勝負するのよ」"
voice "Reo_0322"
re "「ふん、そんなのいつも通りじゃない」"


show char ter02f2 at right as r
with dis



voice "Erisu_0174"
e "「ええ、でも今回は本気をかけた勝負だよ～♪」"
voice "Reo_0323"
re "「本気……臨むところよ」"
voice "Erisu_0175"
e "「フフフ、ワタシが勝ったら、玲緒は『２代目リリ・プラチナム』になる」"


show char tre03s2 at left
with dis



voice "Reo_0324"
re "「うううっ、それって……」"
voice "Erisu_0176"
e "「あれー？　玲緒もしかして、負けるって思ってるの」"


show char tre09s2 at left
with dis



voice "Reo_0325"
re "「負けるわけないじゃない！」"
"玲緒ったら、ムキになってる。"
"エリスさま、玲緒の扱いがかなりうまくなってるわ。"


#allClear:
hide char tre09s2 at left
hide char ter02f2 at right as r
#lastBG:
#scene bg bg21a
with dis


"そう思ったのは、わたしだけじゃないらしい。"
voice "Mobkaiinb0016"
kb "「ああ、至福ですわ～」"
voice "Mobkaiinc0015"
kc "「エリスさまと玲緒さまのツーショット、まるで本物の姉妹のようです」"
voice "Mobkaiina0034"
ka "「萌えますわ～」"
"会員の子たちは、金髪好きっていうのもあるけれど、この２人のやりとりに完全にメロメロになっていた。"
"目なんか、ハート型になっている。"


show char tre08s2 at left
show char ter01f2 at right as r
with dis



voice "Reo_0326"
re "「じゃあ、もしワタシが勝ったらどうするの……」"
voice "Erisu_0177"
e "「玲緒が勝ったら……ワタシが玲緒に」"


show char tre02s2 at left
with dis



voice "Reo_0327"
re "「何をしてくれるのかしら、ふふふっ」"
voice "Erisu_0178"
e "「『リリ・プラチナム』の座を譲るわ」"


show char tre04s2 at left
with dis



voice "Reo_0328"
re "「なぁぁ～～～～っ」"
voice "Erisu_0179"
e "「どうかな？」"


show char tre03s2 at left
with dis



voice "Reo_0329"
re "「ど、どうって……」"
"わなわなと震える、玲緒。"
"完全に、遊ばれてるわね。"


show char tre08s2 at left
with dis



voice "Reo_0330"
re "「もう、どっちにしてもワタシがアンタの後を継ぐってことじゃない」"
voice "Erisu_0180"
e "「バレた？」"


show char tre09s2 at left
with dis



voice "Reo_0331"
re "「エリスのばかぁ、無駄ちち、エセハーフ」"


show char ter03f2 at right as r
with dis



voice "Erisu_0181"
e "「エセじゃないんだけどね……」"


#allClear:
hide char tre09s2 at left
hide char ter03f2 at right as r
#lastBG:
#scene bg bg21a
show char tma08s2
with dis



voice "Mai_0448"
ma "「ちょっと、玲緒、エリスさまに向かってなんてことを」"
"こんなやりとり、他の子たちに聞かれたら……"


show char tma03s2
with dis



voice "Mai_0449"
ma "「あっ……」"
voice "Mobkaiinb0017"
kb "「ああ、なんて素敵なの{image=image/exch001.png}」"
voice "Mobkaiinc0016"
kc "「お二人が一緒にいるだけで……もう{image=image/exch001.png}」"
"彼女たちは、ぽわんとした表情で２人をただ見つめているだけだった。"
"完全にトリップしている。"
"どうやら、話の内容までは聞いてないようだった。"
voice "Mai_0450"
ma "「助かったわ……」"
"それにしても。"
"玲緒とエリスさま。"
"こうしてみると、本当の姉妹のように見えるわね。"
"２人の金髪がキラキラに輝いて。"
"なんだか、そこだけ違う空気が流れているみたい。"
voice "Mai_0451"
ma "「……ちょっとだけ羨ましい……かも」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


show char tma01s2
with dis



voice "Mai_0452"
ma "「ねぇ、玲緒」"
"その日の帰り道。"
"玲緒は、まだ機嫌が悪かった。"


show char tma01s2 at left
show char tre08s2 at right as r
with dis



voice "Reo_0332"
re "「エリスの後なら継がないわよっ」"
voice "Mai_0453"
ma "「そうじゃなくて、今度の休日デートしない」"


show char tre01s2 at right as r
with dis



voice "Reo_0333"
re "「デ、デート……」"
"ぱぁぁんと、わかりやすいくらいに玲緒の顔が輝いた。"


show char tma02s2 at left
with dis



voice "Mai_0454"
ma "「ふふふっ、そんなに嬉しい」"


show char tre03s2 at right as r
with dis



voice "Reo_0334"
re "「ち、違うわよ、今のは今日のおやつのことを考えていたのよ」"
voice "Mai_0455"
ma "「はいはい」"
"変なところで、ツンデレなんだから。"
"むしろ、おやつでそれだけ喜んでいる方が、恥ずかしいような気もするけど。"
"それに気づかないのが、玲緒よね。"


show char tre08s2 at right as r
with dis



voice "Reo_0335"
re "「デートは……麻衣がそんなに行きたいなら、行ってもいいわよ」"
voice "Mai_0456"
ma "「うん、いきたい！　その日は玲緒の大好物、いっぱい作ってあげるわね」"


show char tre04s2 at right as r
with dis



voice "Reo_0336"
re "「ほ、本当に？」"
voice "Mai_0457"
ma "「ええ、おいしいお弁当とお菓子を持って、遊びに行きましょう」"


show char tre02s2 at right as r
with dis



voice "Reo_0337"
re "「わぁーい♪」"
"エリスさまと玲緒の関係は、羨ましい。"
"でも２人は、恋人じゃない……姉妹みたいなものだもの。"
"こっちは恋人なの、ラヴラブなんだから！"
"わたしは玲緒といっぱい一緒にいて、デートすればいいんだから。"
voice "Mai_0458"
ma "（デートの日は、玲緒をとことん甘やかしてあげよう……んふふっ）"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**玲緒の部屋・昼
scene bg bg33a
with Dis



#mes on
#system on


"そして、デート当日。"


show char tma01f2
with dis



voice "Mai_0459"
ma "「さて、お弁当作りから始めましょうか」"
"玲緒の好きなハンバーグは、はずせないわよね。"
"わたしははりきって、お弁当作りを始めた。"
"しばらくして……"

#//SE:携帯の音
#♀SE012
play sound "sound/SE012.ogg"


voice "Mai_0460"
ma "「玲緒、携帯が鳴ってるわよ」"


show char tma01f2 at left
show char tre03p at right as r
with dis



voice "Reo_0338"
re "「んー、眠い」"
voice "Mai_0461"
ma "「早く出なさいよ～」"
voice "Reo_0339"
re "「わかったわよぉ～」"
"眠い目をこすりながら、お弁当ができるまでソファーで二度寝を決め込んでいた玲緒が、しぶしぶ電話を取る。"
voice "Reo_0340"
re "「なんだ……メールじゃない」"


#allClear:
hide char tma01f2 at left
hide char tre03p at right as r
#lastBG:
#scene bg bg33a
show char tma03f2
with dis



voice "Mai_0462"
ma "「そう、もうすぐお弁当できるから、玲緒もそろそろ出かける準備を……ちょっと、玲緒？」"


show char tre08f2
with dis



voice "Reo_0341"
re "「………………」"
"玲緒は真剣な眼差しで、携帯を凝視していた。"


show char tma03f2 at left
show char tre08f2 at right as r
with dis



voice "Mai_0463"
ma "「誰からのメールなの？」"
voice "Reo_0342"
re "「これは……エリスよ」"
voice "Mai_0464"
ma "「エリスさま？」"
voice "Reo_0343"
re "「いきなり、勝負を挑まれたわ」"
"そう言って、玲緒はわたしにメールを見せてくれた。"
"そこにはこう書かれていた。"

"『プールの招待券もらったけど、シズクはちょっと風邪気味なの。で、玲緒行かない？　今日は水泳勝負よ』"

voice "Mai_0465"
ma "「玲緒……まさか行くの？　あなたあまり泳げないじゃない」"
voice "Reo_0344"
re "「泳ぎだけとは限らないわ、潜水勝負かもしれないじゃない」"
"……それは違うと思うけど。"
voice "Reo_0345"
re "「勝負を持ちかけられたら、断れないわ」"
voice "Mai_0466"
ma "「えっ、ちょっと玲緒……」"
voice "Reo_0346"
re "「麻衣、ゴメンね。勝負を挑まれて、逃げちゃったら……ワタシ、負け犬になっちゃうわ！！」"


show char tma04f2 at left
with dis



voice "Mai_0467"
ma "「ちょ、ちょっと玲緒、でも今日は、わたしとデートの……」"


show char tre07f2 at right as r
with dis



voice "Reo_0347"
re "「デートならいつでもいけるでしょう、また来週ね！　待ってなさい、エリスぅ～」"


hide char tre07f2 at right as r
with dis


"なんと玲緒は、わたしの作ったお弁当だけ持って。"
"エリスさまとの勝負に、出かけてしまった……"


show char tma03f2
with dis



voice "Mai_0468"
ma "「そんなぁ……もう！　玲緒はわたしとのデートより、勝負の方が大事っていうの！？」"


#allClear:
hide char tma03f2
#lastBG:
#scene bg bg33a
with dis


"ここ数日のわくわく感、全部パーだわ。"


#**カフェ・昼
scene bg bg36a
with Dis



show char tma07f2
with dis



voice "Mai_0469"
ma "「まったく、玲緒ったら……」"
"そのまま家に戻っても、落ち込んでしまいそうだったので、わたしは１人で出かけることにした。"
"いろいろお店を見てまわったけれど、なかなか気分は晴れず。"
"一休みをするため、カフェに立ち寄った。"
"すると……"


show char tma03f2
with dis



voice "Mai_0470"
ma "「えーと、席は……あれっ、雫さま」"


show char tma03f2 at left
show char tsi01f2 at right as r
with dis



voice "Sizuku0137"
sk "「麻衣さん……偶然ですね、お１人ですか」"


show char tma01f2 at left
with dis



voice "Mai_0471"
ma "「ええ、お隣りいいですか？」"
voice "Sizuku0138"
sk "「どうぞ、ご遠慮なさらずに」"
"わたしは雫さまの隣りに座る。"
"このカフェは、イベント委員のみんなとも何度か来たことがあったけど。"
"まさか、雫さまに会えるなんて……"


show char tma03f2 at left
with dis



voice "Mai_0472"
ma "「エリスさまから、雫さまが風邪気味だって聞いたけれど……大丈夫なんですか？」"
voice "Sizuku0139"
sk "「風邪自体は大したことありません、でも大事をとって、ぷーるはやめただけです」"


show char tma01f2 at left
with dis



voice "Mai_0473"
ma "「そうだったんですか……」"


show char tsi03f2 at right as r
with dis



voice "Sizuku0140"
sk "「家で、お茶でも点ててようかとも思いましたが、なんとなく気分が乗らなくて……」"
voice "Mai_0474"
ma "「それで１人で、カフェに……」"
"雫さまのカップには抹茶ラテが入っていたが、ほとんど口をつけていなかった。"
"なんとなく、元気がなく見えるのは……わたしと同じ理由かもしれない。"
voice "Sizuku0141"
sk "「こんな時に、体調管理もできないわたくしが悪いのかもしれませんが……でも、おいてかれるのは寂しいです」"


show char tma03f2 at left
with dis



voice "Mai_0475"
ma "「雫さま……そうですよね」"
"わたしが今日のデートを楽しみにしていたように、雫さまもエリスさまとのプールを楽しみにしていたに違いない。"
"でも、エリスさまと玲緒はそんなことも気づかずに、今頃２人で楽しくやっているんだわ。"
"水の中、お揃いの金髪をキラキラさせて。"


#★★★選択肢　ここから


"なんか、嫉妬しちゃう……"


#++選択肢（２）
#１．『玲緒への愚痴を言う』○
#２．『玲緒の悪口を、思いっきり言う』×
menu:
 "玲緒への愚痴を言う":
  jump select20_1
 "玲緒の悪口を、思いっきり言う":
  jump select20_2



#１．『玲緒への愚痴を言う』
label select20_1:


voice "Mai_0476"
ma "「玲緒と、エリスさま……あの２人って、仲良すぎですよね。いくら姉妹みたいだからって言っても……肝心の恋人を放っておくなんて」"
voice "Sizuku0142"
sk "「……はい、ちょっと寂しいです」"
"わたしの愚痴に、雫さまも控えめに乗っかってきた。"
"わがままな恋人に放っておかれる寂しさに、共感しているのよね……お互い。"


#set f1 f1+1
jump select20_end


#２．『玲緒の悪口を、思いっきり言う』
label select20_2:


show char tma09f2 at left
with dis



voice "Mai_0477"
ma "「もぉ……玲緒のおバカ、チビチビお子様、ダメッ子小動物、つるぺた平たい胸族っ！！」"
voice "Sizuku0143"
sk "「麻衣さん……それは、言い過ぎでは……？」"


show char tma03f2 at left
with dis



voice "Mai_0478"
ma "「……確かに……そう、かも……」"
"言っていて、ちょっと悲しくなってきたし。"
"やっぱり自分の恋人を、悪く言ってはダメよね……"
voice "Sizuku0144"
sk "「でも、麻衣さんの気持ちも少しは分かります。わたくしもエリスに放っておかれると、寂しいですし……」"
jump select20_end

#++選択肢終了
#★★★選択肢　ここまで
label select20_end:


"ちょっと前にも、似たようなことがあったわよね。"
"だからわたしと雫さまも『玲緒とエリス様に対抗して、わたしたちも姉妹になりましょう』ってことになって。"
"色々と楽しいことをしたけれど、勘違いした玲緒に泣きつかれたのよね……ワタシから、麻衣を取らないで、って。"


show char tma01f2 at left
with dis



voice "Mai_0479"
ma "「あっちも姉妹だっていうなら、こちらも……ね、雫さま？」"


show char tsi01f2 at right as r
with dis



voice "Sizuku0145"
sk "「麻衣さん……そうですね。久しぶりに、こちらも姉妹遊びを………………はっ！？」"
"いきなり頭を落とした雫さまは、わたしに小声で話しかけた。"


show char tsi03f2 at right as r
with dis



voice "Sizuku0146"
sk "「麻衣さん、またあの方たちが、外に……」"


show char tma03f2 at left
with dis



voice "Mai_0480"
ma "「あの方たちって……あっ、あの『リリ・プラチナム』の……」"
"あんまり会いたくないのに、どうして出会っちゃうのかなあ……もう。"
voice "Sizuku0147"
sk "「見つかると、困ったことになりそうで……早く行ってほしいです」"
voice "Mai_0481"
ma "「ええ、本当に………………ん、待って……」"
"その時、わたしの頭の中でピーンと何かがひらめいた。"
"相変わらずエリスさまと仲がよすぎて、わたしとのデートをすっぽかす悪い子、玲緒への復讐劇が。"


show char tma01f2 at left
with dis



voice "Mai_0482"
ma "「……うん、やってやるわ……うん！」"
voice "Sizuku0148"
sk "「麻衣さんどうかしましたか？」"


show char tma02f2 at left
with dis



voice "Mai_0483"
ma "「ちょっと、妙案が……力を貸してください、雫お姉さま{image=image/exch001.png}」"
voice "Sizuku0149"
sk "「は、はい……また、姉妹ごっこをするのですか？」"
voice "Mai_0484"
ma "「そのもう一つ、上をいくことですよ……んふ、んふふっ」"
"わたしは雫さまの美しい黒髪を見ながら、彼女にあることを提案したのでした……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**旧校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


#※ここから少し、玲緒視点で

show char tre03s2
with dis



voice "Reo_0348"
re "「うううっ、水泳対決は負けたけど、次回は絶対エリスに勝つんだから」"
"昨日の勝負、散々だったわ。"
"あそこで体がブクブクと沈まなかったら、ワタシの勝ちだったのよ。"
"次回はビート板、バタ足対決にしてもらうわ。"


show char tre08s2
with dis



voice "Reo_0349"
re "「それなら理論上、ワタシの勝ちよ！　ワタシはビート板でしか泳がないんだから」"
"よし、早速エリスにメールを……"


show char tre04s2
with dis



voice "Reo_0350"
re "「ひゃああ……あれは」"
"目の前から歩いてくる連中。"
"ワタシをしつこくつけまわす、なんだっけ……変な名前のエリスのファンクラブの子たち。"


show char tre03s2
with dis



voice "Reo_0351"
re "「どこか隠れるところ～」"
"なにもないわ。"
"こうなったら……"
"ワタシは下を向いて、手で顔を隠しながら、そのまま歩き続けた。"
"こういう時、小柄な体が役に立つわ。"


show char tre02s2
with dis



voice "Reo_0352"
re "「ふふふ、これならバレないわね」"
"彼女たちは、お喋りに夢中になってるし、なんとかなりそうだわ。"
"そして、すれ違いざま彼女たちの会話の一部が聞こえてきた。"
voice "Mobkaiina0035"
ka "「本当に昨日のパーティは、楽しかったですわね～」"
voice "Mobkaiinb0018"
kb "「麻衣さまも雫さまも、とても素敵で」"
voice "Mobkaiinc0017"
kc "「わたし、あらためて、お二人のファンになりましたわ」"


show char tre04s2
with dis



voice "Reo_0353"
re "「……えっ！？」"
"今……麻衣と雫って言ったの？"


show char tre03s2
with dis



voice "Reo_0354"
re "「ちょ、ちょっと待ちなさい～」"
"ワタシは、彼女たちを慌てて呼び止めた。"
voice "Mobkaiinc0018"
kc "「あら、玲緒さま、ごきげんよう」"
voice "Mobkaiina0036"
ka "「どうかなさいましたか」"
voice "Reo_0355"
re "「今の話……ちゃんと聞かせてちょうだい」"


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


"………………"
"…………"
"……"


#**旧校舎廊下・昼
scene bg bg05a
with Dis



"そこで、聞いたことはまさに衝撃的だった。"
"なんと麻衣と霧島雫が『黒髪姉妹の集い』と称して、黒髪の人専用のミニパーティを開いているというのだから。"


show char tre03s2
with dis



voice "Reo_0356"
re "「そ、そんな話……ワタシ、まったく聞いてないわよ～！」"
voice "Mobkaiina0037"
ka "「それは……玲緒さまは黒髪じゃない方だからでは？」"
voice "Mobkaiinb0019"
kb "「そうそう、見事なブロンドですもの……ね～」"
voice "Reo_0357"
re "「関係ないわよ～～～～」"
"だって麻衣は、麻衣はワタシの恋人なのに。"
"そのワタシに内緒で、そんな楽しそうなこと、やってるなんて！"
voice "Reo_0358"
re "「これは一度、見に行かないと……」"
"ワタシは無理矢理彼女たちに、次回のパーティの日時と場所を聞きだして。"
"その場に乗り込むことにした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**中庭・昼
scene bg bg21a
with Dis



#※EV068
scene bg EV68
with Dis



#mes on
#system on


voice "Reo_0359"
re "「うううっ……本当にやってるわ」"
"休日、その場所に行ってみると。"
"なんと本当に、麻衣と霧島雫を囲んでお茶会がもようされていた。"
"お休みだから、みんな私服みたい。"
"お茶会……ではないが、楽しそうなピクニックのようで。"
voice "Mai_0485"
ma "「今日はからあげと卵焼き、それとおにぎりを持ってきました。皆さんで食べましょう」"
voice "Sizuku0150"
sk "「お茶もすぐ、たてますね。お待ちください」"
"そんな２人の周りで、わいわいしているのは……黒髪の子たちばかりだった。"
voice "Reo_0360a"
re "「麻衣ったら、こんなコトやって……文句言ってやる！」"
"そのまま、パーティの中に入ろうとしたんだけど、横から止められてしまった。"
voice "Mobkaiinb0020"
kb "「玲緒さま、いけません」"
voice "Reo_0361"
re "「なんでよ」"
voice "Mobkaiina0038"
ka "「だってこれは、黒髪の方専用のパーティですから」"
voice "Reo_0362"
re "「くっ、うう～～っ」"
voice "Mobkaiina0039"
ka "「あくまで、決まり……ですから」"
"彼女たちに行く手を阻まれて、麻衣の近くに行くことさえできない。"
voice "Mai_0486"
ma "「まぁ、そうなんですか～」"
voice "Sizuku0151"
sk "「ええ、そうですわ、ふふふっ」"
"たまにチラっと見える、２人はとても仲むつまじく見えて。"
voice "Reo_0363"
re "「麻衣……あんなに霧島雫と仲良くしちゃって……ううううっ、こんなのやだぁ、やだやだぁっ！！」"
voice "Mobkaiina0040"
ka "「あっ、玲緒さまっ！！」"


#※EV068P1
scene bg EV68p1
with Dis



voice "Reo_0364"
re "「麻衣の、麻衣のばかぁぁっ！！」"
voice "Mai_0487"
ma "「えぇっ！？　ちょ、ちょっと玲緒？」"
voice "Sizuku0152"
sk "「玲緒さん……やっぱり、見ていたのですね」"
voice "Reo_0365"
re "「こんなパーティ、おしまいよ！　麻衣の料理は全部、ワタシのものなんだから、ぱくぱく、もぐ……んぐ、けほけほけほっ」"


#**青空
scene bg bg42a
with Dis



"こうして黒髪パーティに乱入したワタシは、麻衣の料理を食べつくして。"
"強引に、そのパーティを終わらせてやった。"
"後で……麻衣にすっごく、怒られるかも知れないけれど。"
"でもワタシ、悪くない……恋人のワタシをないがしろにして、霧島雫や、黒い髪の後輩だけで、パーティする麻衣が悪いのよ……ふんッ。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**玲緒の部屋・夜
scene bg bg33c
with Dis



#mes on
#system on


show char tre03f2
with dis



voice "Reo_0366"
re "「………………」"


show char tma03f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0488"
ma "「玲緒、宿題できた？　手が止まっているわよ」"
"翌日、いつも通りにワタシの部屋にやって来た麻衣。"
"メチャクチャ、怒られると思ったのに……軽く『ダメでしょ』と、注意されただけ。"
"それ以上、何も言われなくて。"
"それが余計に、ワタシを不安にさせていた。"
voice "Reo_0367"
re "「……あ……あの、麻衣……」"


show char tma01f2 at left
with dis



voice "Mai_0489"
ma "「ん、何かわからないところでもあった？」"
voice "Reo_0368"
re "「……あの、黒髪の、パーティ……もう止めてよ」"
voice "Mai_0490"
ma "「玲緒……」"


show char tre08f2 at right as r
with dis



voice "Reo_0369"
re "「あんな変なパーティ、やめればいいじゃない！」"


show char tma02f2 at left
with dis



voice "Mai_0491"
ma "「そうはいかないわよ。だって皆さん、楽しみにしているんですもの」"


show char tre03f2 at right as r
with dis



voice "Reo_0370"
re "「でも……麻衣は、ワタシと……」"


show char tma01f2 at left
with dis



voice "Mai_0492"
ma "「玲緒はエリスさまと、遊べばいいでしょう？」"
voice "Reo_0371"
re "「えっ……？」"
"なんで、どうしてここで、エリスのことが出てくるの？"
"麻衣は『その話はこれでおしまい』とばかりに、再び宿題をやり始めた。"


show char tre08f2 at right as r
with dis



voice "Reo_0372"
re "「……麻衣の」"


show char tma03f2 at left
with dis



voice "Mai_0493"
ma "「……んっ？」"


show char tre09f2 at right as r
with dis



voice "Reo_0373"
re "「麻衣のバカ～～～っ！！」"


#allClear:
hide char tma03f2 at left
hide char tre09f2 at right as r
#lastBG:
#scene bg bg33c
with dis


"ワタシはそう叫ぶと、部屋を飛び出していた。"


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
jump S108



