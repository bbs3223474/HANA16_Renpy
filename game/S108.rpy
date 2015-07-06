#「玲緒が好きよ」

label S108:
$ save_name = "◇玲緒が好きよ"


#**カフェ・昼
scene bg bg36a
with Dis



#mes on
#system on


#♂MP01
play music "sound/BGM01.ogg"


"部屋を出ていった後。"
"ワタシはエリスを呼び出して、今回の件を相談した。"


show char ter01f2
with dis



voice "Erisu_0182"
e "「ふぅん……そんなことがあったんだ」"


show char tre03f2 at left
show char ter01f2 at right as r
with dis



voice "Reo_0374"
re "「うん」"


show char ter03f2 at right as r
with dis



voice "Erisu_0183"
e "「ここ数日、シズクがワタシの部屋に来ないから、なんか変だとは思っていたけど」"


show char ter01f2 at right as r
with dis



voice "Erisu_0184"
e "「黒髪パーティかぁ……」"
"エリスは憧れのまなざしで、どこか遠くを見ている。"
voice "Reo_0375"
re "「エリスもワタシと同じく黒髪じゃないから、入れてもらえないわよっ」"
voice "Erisu_0185"
e "「それは……残念ね」"


show char tre09f2 at left
with dis



voice "Reo_0376"
re "「もう、問題はそこじゃないわよ！」"


show char ter03f2 at right as r
with dis



voice "Erisu_0186"
e "「そうだね……ワタシがいけなかったのかも」"


show char tre03f2 at left
with dis



voice "Reo_0377"
re "「えっ？？」"
voice "Erisu_0187"
e "「玲緒と遊ぶのは楽しいけど、シズクを放っておいたかも……ワタシ、謝ってくるよ」"


hide char ter03f2 at right as r
with dis


"エリスは席を立った。"
"今すぐにでも、霧島雫のところへと行きたい感じだ。"
voice "Reo_0378"
re "「ちょっと、待ってよ」"


show char ter03f2 at right as r
with dis



voice "Erisu_0188"
e "「ねぇ、玲緒も一緒に、謝りに行こうよ」"


show char tre09f2 at left
with dis



voice "Reo_0379"
re "「絶対イヤっ！！」"
voice "Erisu_0189"
e "「どうして？」"


show char tre08f2 at left
with dis



voice "Reo_0380"
re "「だ、だって……ワタシは悪くないもん、麻衣たちが勝手にしたことじゃない」"
voice "Erisu_0190"
e "「でも、元々はワタシたちが、恋人を放っておいて、デートをすっぽかして、仲良く遊びすぎたから……」"


show char tre07f2 at left
with dis



voice "Reo_0381"
re "「そんなの知らないわよ、ワタシは謝ったりしないわ！」"
"ワタシも立ち上がる。"
voice "Reo_0382"
re "「とにかく、ぜったいのぜったーい、ワタシからは謝らないからねっ」"


#allClear:
hide char tre07f2 at left
hide char ter03f2 at right as r
#lastBG:
#scene bg bg36a
with dis


"そのままワタシは、カフェを出た。"
"エリスがなにか叫んでいたけれど、聞こえないフリをしてワタシは走りだした。"


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



#mes on
#system on


"翌日。"
"エリスからメールで『こっちはシズクに謝って仲直りをしたよ。玲緒も早く謝りなよ』と言われたけれど。"
"ワタシはスルーした。"


show char tre03s2
with dis



voice "Reo_0383"
re "「なんでよ……どうしてワタシが、謝るのよ……」"
"なんとなく、今朝から麻衣とあまり話もしていない。"
"お昼もバラバラに食べた。"
"いつもならランチが終わった後は、麻衣とお喋りをして過ごすけれど、今日は時間をもてあましている。"
"そしてなんとなく、中庭に来たけれど。"
"特にすることもない。"
voice "Reo_0384"
re "「あーあ、教室に戻ろうかな……」"


show char tma02p
with dis



voice "Mai_0494"
ma "「雫さまのお弁当、本当に美味しそうですねー」"


show char tma02p at left
show char tsi01p at right as r
with dis



voice "Sizuku0153"
sk "「いいえ、わたくしのなんて大したことありません。麻衣さんこそ……」"


#allClear:
hide char tma02p at left
hide char tsi01p at right as r
#lastBG:
#scene bg bg21a
show char tre03s2
with dis



voice "Reo_0385"
re "「えっ？」"
"聞き覚えのある声に、とっさに姿を隠す。"
voice "Reo_0386"
re "「やっぱり麻衣と霧島雫……教室にいないと思ったら……」"
"麻衣はこんなところで、霧島雫とランチをしていたんだわ。"


show char tma01s2
with dis



voice "Mai_0495"
ma "「ところで今日、エリスさまは？」"


show char tma01s2 at left
show char tsi01f2 at right as r
with dis



voice "Sizuku0154"
sk "「エリスは午前中の授業が休講になってしまったので、いったん自分の部屋に戻ってます」"


show char tma02s2 at left
with dis



voice "Mai_0496"
ma "「そうですか、学校から家が近いと便利ですねー」"
"うううっ、なによ、なによ。"
"楽しそうに話しちゃって。"
"なんでこんな時に、エリスは家に帰っているのよ。"
"これだから、短大生は遊んでばかりに見えるのよ。"


show char tma01s2 at left
with dis



voice "Mai_0497"
ma "「明日の黒髪パーティ、このお料理を持っていくつもりなんです」"
voice "Sizuku0155"
sk "「そうですか。ではわたくしは、お菓子を作っていこうと思います」"


show char tma02s2 at left
with dis



voice "Mai_0498"
ma "「ええ～！　それ雫さまのファンの子、すごく喜びますよ」"
voice "Sizuku0156"
sk "「そうでしょうか？」"
voice "Mai_0499"
ma "「もちろんですよ」"


#allClear:
hide char tma02s2 at left
hide char tsi01f2 at right as r
#lastBG:
#scene bg bg21a
show char tre03s2
with dis



voice "Reo_0387"
re "「ううううっ、また黒髪の、パーティ……ぅぅっ」"
"明日もまた、開くつもりなのね。"
"ワタシだけをのけ者にして、楽しむんだわ。"
voice "Reo_0388"
re "「どうせ、ワタシは黒髪じゃないから……金髪だから……」"
"麻衣のばかっ。"
"ばか、ばか。"


show char tre08s2
with dis



voice "Reo_0389"
re "「こ、こうなったら……」"
"もう、あれしかないわ。"
voice "Reo_0390"
re "「あれを、実行してやるわ」"
"ワタシの中に、ある決意が生まれていた。"


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
scene bg bg08a
with Dis



#mes on
#system on

#※ここから麻衣視点に戻します
show char tma03f2
with dis



voice "Mai_0500"
ma "「うーん……少し、やりすぎかなぁ。玲緒、かなり落ち込んでいるみたいだし」"
"昨日、玲緒が部屋を飛び出してから。"
"今日一日は、なんとなくぎこちなかった。"
voice "Mai_0501"
ma "「少しは玲緒にも、わたしの気持ちがわかってくれたら……って思っただけなんだけど」"
"それは伝わっているのかな？"
"色々なことを考えているうちに、玲緒のマンションの前まで着いた。"
voice "Mai_0502"
ma "「玲緒は今、なにを考えているのかしら……」"


#**玲緒の部屋・昼
#allClear:
hide char tma03f2
#lastBG:
#scene bg bg08a
scene bg bg33a
with Dis



show char tma01f2
with dis



voice "Mai_0503"
ma "「ちょっと玲緒、入るわよー」"


show char tma01f2 at left
show char tre04f2 at right as r
with dis



voice "Reo_0391"
re "「ま、麻衣っ！　待って、ちょっと待って！！」"
"わたしが部屋に入ると、玲緒は慌てて何かを隠した。"


show char tma03f2 at left
with dis



voice "Mai_0504"
ma "「玲緒……今、なにしてたの？」"


show char tre03f2 at right as r
with dis



voice "Reo_0392"
re "「なんでも……ないわよ」"
voice "Mai_0505"
ma "「なんでもないなら、その後ろに隠したもの見せなさい、なに、お菓子？」"
voice "Reo_0393"
re "「お菓子なんて、持ってないわよ」"
"確かに、お菓子ではなさそう。"
"というより、入った瞬間から感じたんだけど。"
"なんか変な匂いがするのよね。"
"食べ物とは違う、化粧品のような匂い。"
voice "Mai_0506"
ma "「この匂い……なんだっけ？」"


show char tre08f2 at right as r
with dis



voice "Reo_0394"
re "「なんでもないから、麻衣は出てって」"


show char tma01f2 at left
with dis



voice "Mai_0507a"
ma "「だーめ、見せなさい」"
"これだけムキになるってことは、見られたら相当やばいものよね。"
"もう、なにを隠しているのかしら。"
voice "Mai_0507b"
ma "「えーい、もうくすぐるわよ……こちょこちょ」"


show char tre02f2 at right as r
with dis


##voice REO_0395
voice "Reo_0396"
re "「きゃははは……もう、だめぇ～」"


#allClear:
hide char tma01f2 at left
hide char tre02f2 at right as r
#lastBG:
#scene bg bg33a
with dis


#//SE:物が落ちる音
#♀SE048
play sound "sound/SE048.ogg"


"くすぐり攻撃により、玲緒の後ろ手に隠していたものが床に転がった。"
"それは……"


stop music fadeout 1


play music "sound/BGM15.ogg"


show char tma03f2
with dis



voice "Mai_0508"
ma "「これって……ヘアカラー」"
"それも黒色に染まるやつだった。"
"こんなものを使ったら……"
"不器用な玲緒のことだ、きれいな髪がまだらの汚い黒髪になってしまうかもしれない。"
"封は開いていたけれど、まだ使用前だったことにほっとする。"
"でも。"


show char tma07f2
with dis



voice "Mai_0509"
ma "「なんでこんな事するの、玲緒っ！」"


show char tma07f2 at left
show char tre03f2 at right as r
with dis



voice "Reo_0397"
re "「だって……麻衣が黒髪の子とパーティばかりやってるから、ワタシと遊んでくれないから、ワタシも黒髪になって、お茶会に……ぅぅっ」"


show char tma09f2 at left
with dis



voice "Mai_0510"
ma "「玲緒のおバカっ！！」"
"わたしは転がっているヘアカラーを拾うと、玲緒の手が届かないように向こうの部屋に投げた。"
"まさか、玲緒が自分の髪を染めようとするだなんて。"
"もし、気づくのが遅れたら……"


show char tma03f2 at left
with dis



voice "Mai_0511"
ma "「でも……ごめん、本当のおバカは、わたしだよ……」"
voice "Reo_0398"
re "「麻衣……？」"
voice "Mai_0512"
ma "「ごめんね、玲緒。玲緒がここまで落ち込むなんて、思わなくて……」"


#**青空
#allClear:
hide char tma03f2 at left
hide char tre03f2 at right as r
#lastBG:
#scene bg bg33a
scene bg bg42a
with Dis



"わたしは玲緒に、全て白状した。"
"あの『黒髪パーティ』は、雫さまとの姉妹ごっこを延長した、お遊び……やらせみたいなものだって。"
"お茶会を開きたがっていた後輩に協力してもらって、悪ノリで開いたパーティ。"
"雫さまはエリスさまに、そしてわたしは玲緒に、嫉妬して欲しくて……"
"そしてエリスさまは、雫さまの思いに気づいて、仲直りしたけれど。"
"玲緒は……気づいてくれない、それが寂しくて、わたしはやらせのパーティを続けていた……と。"


#**玲緒の部屋・昼
scene bg bg33a
with dis



show char tre03f2
with dis



voice "Reo_0399"
re "「麻衣……」"


show char tma03f2 at left
show char tre03f2 at right as r
with dis



voice "Mai_0513"
ma "「玲緒、ごめんね、玲緒がわたしとのデートをすっぽかして、エリスさまとばかり遊んでいるから、つい……わたしイジワルで、黒髪パーティなんて始めちゃったんだ」"


show char tma03f2 at left
show char tre10f2 at right as r
with dis



voice "Reo_0400"
re "「うううっ……まぁい……ぐすん」"
"玲緒の顔は、いつの間にか涙でぐしょぐしょだった。"
voice "Reo_0401"
re "「許さないんだから……」"
voice "Mai_0514"
ma "「ごめんね、玲緒。玲緒の美しいブロンドが、もう少しで汚れちゃうところだった……そんなにも、思いつめさせちゃったのね……本当に、ゴメンね」"


show char tre06f2 at right as r
with dis



voice "Reo_0402"
re "「もぉ、許さないんだから………………と、ととと」"
voice "Mai_0515"
ma "「と……？」"
voice "Reo_0403"
re "「特大……ハンバーグよ」"
voice "Mai_0516"
ma "「玲緒の大好物のやつね……ひょっとして、食べたいの？」"
voice "Reo_0404"
re "「ひっく……うううっ、それ、作ってくれないと許さないんだから……」"


show char tma02f2 at left
with dis



voice "Mai_0517"
ma "「……玲緒{image=image/exch001.png}」"


show char tre03f2 at right as r
with dis



voice "Reo_0405"
re "「それ、食べたら……なんか、全部許せそう……かも」"
"ああ……もう、なんて可愛いんだろう。"
"わたしのつまらない嫉妬で、泣かしてしまったのに。"
"大事なブロンド、なくしてしまうところだったのに。"
"こんな風に、玲緒はわたしを許してくれる。"
"自分勝手な子供のようで……実は優しくて、広い心を持っているのよね。"
"こんな愛らしい子が、わたしの恋人で……本当に贅沢よ、幸せものよ、わたしは。"
voice "Mai_0518"
ma "「じゃあすぐ、特大ハンバーグ作ってあげるね{image=image/exch001.png}」"
"今日は愛情をたっぷりとこめて。"
"うんと美味しいのを作ってあげよう……"


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


play music "sound/BGM02.ogg"


#**玲緒の部屋・夜
scene bg bg33c
with Dis


#mes on
#system on


show char tma02f2
with dis



voice "Mai_0519"
ma "「超豪華特製、麻衣ジャンボハンバーグのできあがり～、はいどうぞ♪」"


show char tma02f2 at left
show char tre04f2 at right as r
with dis



voice "Reo_0406"
re "「す、すごい……本当に、おっきい……」"
"玲緒が目を丸くしている。"
"どう、これがわたしの本気よ。"
"今日は特別に、目玉焼きに、たこさんウィンナー、ポテトにミックスベジタブルもついているのだから。"


show char tre02f2 at right as r
with dis



voice "Reo_0407"
re "「い、いただきまぁ～す！」"
"玲緒は嬉しそうに、ハンバーグにかぶりついた。"
"わたしはその様子を、幸せな気持ちで眺めていた……"


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


show char tre02f2
with dis



voice "Reo_0408"
re "「ふぅ～……ごちそうさまでした～」"
"満足そうに、玲緒がハンバーグを食べ終えた。"


show char tma01f2 at left
show char tre02f2 at right as r
with dis



voice "Mai_0520"
ma "「どう、美味しかった？」"
voice "Reo_0409"
re "「うん、すっごく{image=image/exch001.png}」"
voice "Mai_0521"
ma "「じゃあ今度は、わたしの番よね」"


show char tre03f2 at right as r
with dis



voice "Reo_0410"
re "「麻衣も、何か食べるの？」"


show char tma02f2 at left
with dis



voice "Mai_0522"
ma "「わたしは……可愛いヤキモチ焼きの玲緒、いただきま～す{image=image/exch001.png}」"


show char tre04f2 at right as r
with dis



voice "Reo_0411"
re "「ふえぇぇぇっ！？」"
"そのまま一気に、玲緒に飛びつく。"
"わたしの為に髪を染めようとしたり、泣きじゃくったりする玲緒。"
"そんなのを見ちゃったら、何もしないわけにはいかなかった。"


show char tma05f2 at left
with dis



voice "Mai_0523"
ma "「もう、さっきからずっと、可愛い玲緒を可愛がりたくてしょうがなかったんだから……はぁ、はぁ」"
voice "Reo_0412"
re "「ひ、ひぃん、麻衣のエロス、食後くらい休ませろ～」"


show char tma02f2 at left
with dis



voice "Mai_0524"
ma "「いいえ、逆にこれは、食後の運動なのよっ{image=image/exch001.png}」"


#♂MS
stop music fadeout 1

"以下内容可能会导致部分人的不适，是否跳过？"
menu:
 "是":
  jump reo1
 "否":
  jump hscene_reo1

label hscene_reo1:


#※EV069
#allClear:
hide char tma02f2 at left
hide char tre04f2 at right as r
#lastBG:
#scene bg bg33c
scene bg EV69
with Dis


#mes on
#system on


#♂MP09
play music "sound/BGM09.ogg"


voice "Mai_0525"
ma "「ほら、玲緒……わたしの上に乗って」"
voice "Reo_0413"
re "「な、なによ、この体勢は……やぁん」"
voice "Mai_0526"
ma "「ウフフ～、玲緒、お人形さんみたいで可愛い～♪」"
"全裸の玲緒を、わたしの膝の上で横抱きにする。"
voice "Mai_0527"
ma "「このわたしの上に乗っちゃうサイズっていうのがまた、たまらないのよね～」"
voice "Reo_0414"
re "「ちょっと……やだぁ、こんなの恥ずかしいでしょ」"
voice "Mai_0528"
ma "「んふ、玲緒のぷにぷになところ、いくらでも触り放題ね{image=image/exch001.png}」"
voice "Reo_0415"
re "「あっ、あぁん……はうっ、だめ、くすぐったいよぉ、麻衣ぃ」"
voice "Mai_0529"
ma "「この反応、可愛いすぎよ{image=image/exch001.png}　そうやっていちいち反応してくれるから、いっぱい触りたくなるのよね……玲緒に」"
voice "Reo_0416"
re "「もう……あん、バカっ……もうだめ、やだぁ」"
voice "Mai_0530"
ma "「玲緒、そんなにジタバタしないで。そんな子は……もっとイタズラしちゃうわよ」"
voice "Reo_0417"
re "「んぁっ！？　だ、だめぇ、麻衣、そんなとこ……あん、急に触ったらぁ……はぁ、はぁ」"
"わたしは、玲緒の熱くなっている部分を、撫でるように触れてみた。"
voice "Mai_0531"
ma "「ふふふっ……ちょっと感じちゃった、玲緒？」"
voice "Reo_0418"
re "「ん、んんっ……違うもん……あん、麻衣の指がイヤらしいから……あふぅ、らめぇっ」"
voice "Mai_0532"
ma "「当然でしょう、イヤらしいことしてるんだもん。だからもっともっと、イヤらしくしてあげる……ほぉら」"
"今度は指でいっぱい、擦ってあげた。"
"すると玲緒の体は、びくびくと激しく反応してしまった。"


#※EV069P1
scene bg EV69p1
with Dis



voice "Reo_0419"
re "「きゃん、あぁぁん……だめぇ、すごいの、全身がビリビリしちゃうよぉ……くぅん{image=image/exch001.png}」"
voice "Mai_0533"
ma "「玲緒、可愛いわ……じゃあもっと可愛いお顔、わたしに見せて{image=image/exch001.png}」"
"もっといっぱい感じている、玲緒の顔が見てみたい。"
"だから更に、指をこねくり回す。"
voice "Reo_0420"
re "「ひぁあ……ぁぁあっ、くぁん……麻衣の指、すごい、本当にすごいよぉ……こんなの、だめよぉっ」"
voice "Mai_0534"
ma "「玲緒、エッチな顔ね……もうだいぶ、気持ち良くなってきた？」"
voice "Reo_0421"
re "「う……うん……気持ちよく、なっちゃった……かも、はぁ、はぁ{image=image/exch001.png}」"
"玲緒の可愛い割れ目が、とろとろになってきた。"
voice "Mai_0535"
ma "「私の指、玲緒の蜜でこんなに濡れちゃったわ、もう……すごいわね」"
voice "Reo_0422"
re "「ん、ひぅ……っ……だって、麻衣がワタシの恥ずかしいとこ、いっぱい擦るから……んんっ{image=image/exch001.png}」"
voice "Mai_0536"
ma "「だって玲緒、ここ好きなんでしょう？」"
"すっかり膨れ上がった玲緒のクリトリスを、指できゅっと軽く擦る。"
"すると玲緒はわたしの膝の上で、その小さな体を大きく震えさせた。"
voice "Reo_0423"
re "「ひゃうううっ、麻衣……そんな、んあっ……感じちゃうよぉ{image=image/exch001.png}」"
voice "Mai_0537"
ma "「すごい……玲緒のおまんこからいっぱい、熱いお汁が溢れてきたよ{image=image/exch001.png}」"
voice "Reo_0424"
re "「だってぇ、あんっ……熱いのぉ……おかしくなってきちゃうよぉ～」"
voice "Reo_0425"
re "「はぁ、はぁぁ……あ……っ、ああっ、く……ぅ……麻衣ぃ～」"
"玲緒の声に、もう余裕がなくなってきた。"
"絶頂が近いみたいね{image=image/exch001.png}"
voice "Mai_0538"
ma "「はぁぁ、ぁぁ、こんなに感じちゃって……玲緒、もうイッてもいいのよ」"


#※EV069P2
scene bg EV69p2
with Dis



voice "Reo_0426"
re "「あっ、ぁぁん、んっ……麻衣っ……イク、イっちゃううううっっ{image=image/exch001.png}{image=image/exch001.png}」"
"ちょっと指を激しくした瞬間、玲緒は軽くイッてしまった。"
voice "Reo_0427"
re "「はぁ、はぅぅん、もぉ……体から力、抜けちゃったよぉ……くぅん」"
voice "Mai_0539"
ma "「やっぱり、イッちゃったのね、玲緒……でも、ここからが本番よ」"
voice "Reo_0428"
re "「えぇぇっ、ちょっと麻衣、まだダメぇ……ひゃああっ、だめなのぉ{image=image/exch001.png}」"


#※EV070
scene bg EV70
with Dis



"わたしはイッたばかりの玲緒の体を、ぐるっと回して。"
"今度はわたしと向かい合わせで、乗っけるように座らせた。"
voice "Mai_0540"
ma "「玲緒、さっき言ったでしょう、これは食後の運動だって……まだまだ、これからよ」"
voice "Reo_0429"
re "「えっ……？」"
voice "Mai_0541"
ma "「玲緒……んっ、ちゅっ{image=image/exch001.png}」"
voice "Reo_0430"
re "「んんっ、麻衣ぃ……ちゅっ……ちゅ{image=image/exch001.png}」"
voice "Mai_0542"
ma "「ああ、玲緒……好きよ、大好き……んふぅ」"
"わたしは玲緒と抱き合いながら、何度もキスをする。"
voice "Reo_0431"
re "「ちゅ……ちゅるる、ぁぁ……麻衣……んちゅ{image=image/exch001.png}」"
"玲緒の口腔に舌を挿入させていくと、暖かい玲緒の舌に当たって。"
"それをくちゅくちゅと絡ませて、お互いの唾液を味わった。"
voice "Mai_0543"
ma "「玲緒……ねぇ、もっと玲緒の唾液、飲ませて……ぅんっ{image=image/exch001.png}」"
voice "Reo_0432"
re "「あっ……いっぱい、いっぱい飲んで……麻衣ぃ{image=image/exch001.png}」"
"キスをしながら、お互いの指はそれぞれの太もものあたりを彷徨っていた。"
voice "Reo_0433"
re "「麻衣……やっ、んはぁ……だめよ、だめぇ{image=image/exch001.png}」"
"だめって言いながらも、玲緒の脚が少しずつ開く。"
"そのタイミングを見逃さずに、わたしはイッたばかりで、まだヒクついてる玲緒の割れ目に触れる。"
voice "Reo_0434"
re "「ひあぁぁん……麻衣ぃ、そこ……だめよぉ」"
voice "Mai_0544"
ma "「なんでダメなの？　まだ敏感なままだから？　でも触れば触るほど、もっと濡れてきてるけど……{image=image/exch001.png}」"
voice "Reo_0435"
re "「ま、麻衣だって……ほらぁ」"
"玲緒の小さな指が、わたしのおまんこに直接触れてきた。"
"玲緒の姿に興奮していた、わたしはもうぐちゅぐちゅに濡れてしまっていた。"
voice "Mai_0545"
ma "「んんっ……玲緒の指、すごくいい、いいよぉ……はぅぅん{image=image/exch001.png}」"
voice "Reo_0436"
re "「麻衣の中だって……ああ、すっごく熱いよ……」"
voice "Mai_0546"
ma "「ふふふっ、だってわたし、玲緒に触れられると、どんどん感じちゃうの……ぁぁ、すごく感じるの{image=image/exch001.png}」"
"一生懸命に、わたしに愛撫する玲緒。"
"それが可愛すぎて、ますますわたしの快感を促していく。"
voice "Reo_0437"
re "「んっ……はぁ……麻衣のおまんこ……すごいよ、びちょびちょ」"
voice "Mai_0547"
ma "「あっ……んんんっ、ぅ……玲緒ぉ{image=image/exch001.png}　あぅん、ああん{image=image/exch001.png}」"
"全身に、電気が走ったように震えてしまう。"
"わたしは玲緒の敏感な部分を、くすぐるように刺激した。"
voice "Reo_0438"
re "「んふっ……んあっ、すごい……すごすぎよぉ、麻衣ぃ、あふぅ{image=image/exch001.png}」"
voice "Mai_0548"
ma "「どう？　感じちゃってるの……んちゅ、ちゅう{image=image/exch001.png}」"
voice "Reo_0439"
re "「ちゅっ……あん、麻衣とキスして、おまんこ触られると……感じすぎちゃうぅぅ」"
voice "Mai_0549"
ma "「わたしも、玲緒にされてると……いいの、すっごく気持ちいい」"
"お互いの指の動きが、ますます激しくなっていって。"
"求め合うように、口づけをかわしながら、愛撫を続けていった。"
voice "Reo_0440"
re "「あふぅ……すごいの、ワタシ、ドキドキしてるよぉ……はぁ{image=image/exch001.png}」"
voice "Mai_0550"
ma "「そうね……玲緒、好きよ……だからもっと、わたしでドキドキして……あんっ、ああああっ」"
"いくら抑えようとしても、大きな声が出てしまう。"
"それと同時に玲緒のあそこが、わたしの指をきゅっと締め付けた。"
voice "Reo_0441"
re "「だめぇ……もう、ワタシイキそう……きゅぅんっ」"
voice "Mai_0551"
ma "「わたしもよ、玲緒……ちゅっ{image=image/exch001.png}」"
"玲緒の感じる場所を執拗に擦り、快感を与え続けて。"
"小さい玲緒の体は、わたしの上で身悶えた。"
voice "Reo_0442"
re "「ふぁぁぁんっ、麻衣のエロスぅ……そんなことしたら、あっ、あんっ、またいくぅ」"
voice "Mai_0552"
ma "「大丈夫よ、わたしも……わたしも、玲緒と同じくらい感じてるの、いきそうなのぉ{image=image/exch001.png}」"
"座っている椅子の下には、わたしと玲緒の愛液で水溜りができていた。"


#※EV070P1
scene bg EV70p1
with Dis



voice "Reo_0443"
re "「あぁう、もぉらめぇ、麻衣ぃぃっ……あぁぁっ、あうぅぅっっ{image=image/exch001.png}{image=image/exch001.png}」"
voice "Mai_0553"
ma "「玲緒、れおおぉっ、ああん、いくいくぅ……うううんんっ{image=image/exch001.png}{image=image/exch001.png}」"
"押し上げられるような強い感覚と共に、わたしたちは果てた……椅子の上でガクっと、脱力してしまうほどに。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


#endscene
#setscene 16

label reo1:

#**玲緒の部屋・夜
scene bg bg33c
with Dis



#mes on
#system on


show char tre03z
with dis



voice "Reo_0444"
re "「ぁぁ、んぁぁ……麻衣ぃ……どうして、くれるのよぉ……」"


show char tma03z at left
show char tre03z at right as r
with dis



voice "Mai_0554"
ma "「はぁ、はぁ……ん、玲緒、まさか……イケなかったの？」"
voice "Reo_0445"
re "「違うぅ、イッたわよ、また……だから、なくなっちゃたの」"
voice "Mai_0555"
ma "「なくなったって、何がなくなったのよ？」"
voice "Reo_0446"
re "「お腹の中の……ハンバーグよ！　エッチのしすぎで、またお腹が空いちゃったでしょ」"


show char tma02z at left
with dis



voice "Mai_0556"
ma "「あら……そんなに激しかったかしら、んふふっ{image=image/exch001.png}」"
voice "Reo_0447"
re "「麻衣、またなんか作ってよねっ」"
voice "Mai_0557"
ma "「はいはい、わかったわよ、玲緒{image=image/exch001.png}」"
"わたしは愛しい玲緒の要望通り、甘くて美味しいデザートを作ってあげたのでした。"


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
jump S109



