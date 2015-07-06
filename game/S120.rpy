#「家族の一員」

label S120:
$ save_name = "◇家族の一員"


#**沢口家ダイニング・昼
scene bg bg15a
with Dis



#mes on
#system on


#♂MP18
play music "sound/BGM18.ogg"


show char tma02s2
with dis



voice "Mai_0855"
ma "「いらっしゃい、玲緒♪」"


show char tma02s2 at left
show char tre01s2 at right as r
with dis



voice "Reo_1005"
re "「う、うん……」"


#**青空
#allClear:
hide char tma02s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg15a
scene bg bg42a
with Dis



"連休明け、わたしの家から帰る時は、涙ぼろぼろだった玲緒だけど。"
"あれから何日か経って、母が実家から戻って来たことを伝えたら。"
"すぐに『麻衣のところの赤ちゃん、見に行きたい』って言い出した。"
"涙の別れが照れくさくて、しばらくは家には来ないかなって気もしたけど……"
"それはどうやら、わたしの考えすぎだったみたいね。"


#**沢口家ダイニング・昼
scene bg bg15a
with Dis



"というわけで、今日は登校前に玲緒にウチに寄ってもらって、赤ちゃんとご対面なのでした～"


show char tma01s2
with dis



voice "Mai_0856"
ma "「じゃあ、ちょっと待ってて……」"
"立ち上がって、ドアを開けるとすぐに……"
voice "Mobmaibrz0050"
mao "「ねー、れおきてるの？」"
voice "Mobmaisis0043"
mai "「れおちゃん、あそぼーよー」"
"弟たちが嬉しそうに飛び込んできた。"


show char tre09s2
with dis



voice "Reo_1006"
re "「もぉ、アンタたち！　呼び方が戻ってるわよ、玲緒じゃなくて『れおお姉ちゃん』でしょ！」"
"びしっとお姉さん風を吹かせて、玲緒が子供たちに言い返す。"
"しかし２人とも『にししっ』と顔を見合わせて、無邪気に笑っていた。"
voice "Mobmaibrz0051"
mao "「だってれおは、すぐ泣くじゃん。『おねえちゃん』が泣き虫なんて、おかしいよ」"
voice "Mobmaisis0044"
mai "「そうそう、麻衣おねえちゃんにだきついて泣いてたの、見ちゃったもん」"


show char tre05s2
with dis



voice "Reo_1007"
re "「なっ……」"
"妹たちの言葉に、玲緒は顔を真っ赤にさせた。"
"どうやら２人に、玲緒が泣きじゃくってたところを見られていたらしい。"


show char tre09s2
with dis



voice "Reo_1008"
re "「あっ、あれは違うの、ふぎーーーーっ！！」"
voice "Mobmaibrz0052"
mao "「おっ、やるのか、れお」"
voice "Mobmaisis0045"
mai "「おにいちゃん、がんばれー！」"


show char tma09s2 at left
show char tre09s2 at right as r
with dis



voice "Mai_0857"
ma "「ちょっとあなたたち、家の中で騒がないのっ！」"
voice "Reo_1009"
re "「そうよそうよ、お子様はもっと静かにしなさいっ！」"
voice "Mai_0858"
ma "「玲緒、あなたもよっ！！」"


show char tre03s2 at right as r
with dis



voice "Reo_1010"
re "「うにゅぅぅ～」"
voice "Mobmaibrz0053"
mao "「やーい、れおも怒られてやんの！」"


show char tre09s2 at right as r
with dis



voice "Reo_1011"
re "「うるさいっ、うきゃぁぁぁっ！！」"


hide char tre09s2 at right as r
show char tma03s2
with dis



voice "Mai_0859"
ma "「やれやれ……」"
"隣の部屋では、さっき寝かしつけたばかりの赤ちゃんがいる。"
"ただでさえ弟たちは騒がしいのに、今日はそれにプラス１人。"
voice "Mai_0860"
ma "「ああ、なんかイヤな予感が……」"
voice "Mobmaibrz0054"
mao "「おっ、れおのヤツ、なんかかくしてるぞ」"
voice "Mobmaisis0046"
mai "「えーっ、なにそれ、見せて～」"


show char tre02s2
with dis



voice "Reo_1012"
re "「ふふふっ、これが大人と子供の違いよ。大人の財力、見せつけてやるわ」"
"ばーんと、玲緒は制服のポケットから、大量のお菓子を取り出した。"
voice "Reo_1013"
re "「これは昨日、綾瀬美夜と共同購入で手に入れた、まぼろしのチョコレート」"
voice "Mobmaibrz0055"
mao "「おおおおっ～！」"
voice "Mobmaisis0047"
mai "「おいしそう～、れおちゃん、ちょーだい！」"
voice "Reo_1014"
re "「ふん！　子供なんてちょろいわね……」"


show char tma03s2 at left
show char tre02s2 at right as r
with dis



voice "Mai_0861"
ma "「玲緒、あなた……」"
"子供相手に、そんなところで得意げになる玲緒の方が、よっぽど子供よ……ってことは、言わない方がいいわね。"
"でもそろそろ、静かにしてもらわないと困るわね。"


show char tma01s2 at left
with dis



voice "Mai_0862"
ma "「あなたたち、もうちょっと静かに……んっ？」"

#♀SE080
play sound "sound/SE080.ogg"


"隣りの部屋から、赤ちゃんの泣き声が聞こえてきた。"
"うううーっ、やっぱり起きちゃったみたい。"


show char tma09s2 at left
with dis



voice "Mai_0863"
ma "「もう、あなた達がうるさいから、赤ちゃんが泣いちゃってるでしょう！　いいかげん静かにしなさい～！！」"


show char tre04s2 at right as r
with dis



voice "Reo_1015"
re "「ひゃあああーっ！」"
voice "Mobmaibrz0056"
mao "「うわああああっ！」"
voice "Mobmaisis0048"
mai "「麻衣おねえちゃんが怒った～」"


#allClear:
hide char tma09s2 at left
hide char tre04s2 at right as r
#lastBG:
#scene bg bg15a
show char tma03s2
with dis



voice "Mai_0864"
ma "「もう、うるさすぎ……本当に、勘弁してぇ～」"
"これって『玲緒がお姉さんになった』というより、もう１人子供が増えたみたいよ……はぁ～"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**沢口家ダイニング・昼
scene bg bg15a
with Dis



#mes on
#system on


show char tma01s2
with dis



voice "Mai_0865"
ma "「ほら玲緒、赤ちゃんだよ」"


show char tma01s2 at left
show char tre04s2 at right as r
with dis



voice "Reo_1016"
re "「う……うわぁ……」"
"ビックリして泣き出した赤ちゃんだったけど、みんなであやしたらすぐ、機嫌を良くしてくれた。"
"玲緒は、目をまるくして、その小さな命を見つめる。"


show char tre02s2 at right as r
with dis



voice "Reo_1017"
re "「わっ、わぁ……すっごく可愛いわね～」"
voice "Mai_0866"
ma "「玲緒もちょっと、抱いてみる？」"


show char tre03s2 at right as r
with dis



voice "Reo_1018"
re "「うーん……大丈夫かなぁ」"
voice "Mai_0867"
ma "「まだ首がすわってないから、怖いかな？　また今度にしようか」"


show char tre01s2 at right as r
with dis



voice "Reo_1019"
re "「うん、じゃあ練習してくるわ」"


show char tma03s2 at left
with dis



voice "Mai_0868"
ma "「れ、練習って？」"


show char tre02s2 at right as r
with dis



voice "Reo_1020"
re "「そうよ、練習よ。次回は必ず、抱っこするからね♪」"
"練習って……どうするつもりかしら？"
"玲緒のことだから、またとんでもないことを考えてそうだけど……"
"でも赤ちゃん目当てで、これからもちょくちょく、ウチに来そうな感じね。"
"他にも、ここには玲緒を待っている子たちもいるし。"


show char tma02s2 at left
with dis



voice "Mai_0869"
ma "「この子たちもすっかり、玲緒を……ふふっ」"
"弟と妹を、じっと見つめる。"
"玲緒に会うといっぱい、生意気なことを言うくせに。"
"今度、玲緒がいつ遊びに来るのか、何度もわたしに聞いていたっけ。"
voice "Mai_0870"
ma "「ふふふっ」"


show char tre03s2 at right as r
with dis



voice "Reo_1021"
re "「んっ？　なによ、麻衣」"
voice "Mai_0871"
ma "「みんな、本当に可愛いなぁーって思って{image=image/exch001.png}」"

#//SE：玄関チャイムの音
#♀SE024
play sound "sound/SE024.ogg"


show char tma01s2 at left
with dis



voice "Mai_0872"
ma "「あっ、母さん達、帰って来たみたい」"
"わたしは赤ちゃんを抱っこしたまま、立ち上がる。"


show char tre01s2 at right as r
with dis



voice "Reo_1022"
re "「あっ……赤ちゃん、バイバイ！　またね～」"


#allClear:
hide char tma01s2 at left
hide char tre01s2 at right as r
#lastBG:
#scene bg bg15a
with dis


"お母さんのところへ連れて行く前に、玲緒が赤ちゃんに手を振る。"
"それだけのことなのに、なんだかわたしはすごく幸せを感じてしまったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**沢口家ダイニング・昼
scene bg bg14a
with Dis



#mes on
#system on


show char tma03s2
with dis



voice "Mai_0873"
ma "「ん………………ちょっと何よ、この大騒ぎは！？」"


#allClear:
hide char tma03s2
#lastBG:
#scene bg bg14a
with dis


"赤ちゃんをお母さんに預けて、部屋に戻ると。"
"そこはもう、ちょっとした戦争状態だった。"
voice "Mobmaibrz0057"
mao "「お母さんも麻衣おねえちゃんも、赤ちゃんばかり相手にして、つまんない」"
voice "Mobmaibrz0058"
mao "「れお、遊べよー」"
voice "Mobmaisis0049"
mai "「れおちゃん、またお馬さんやって！」"


show char tre09s2
with dis



voice "Reo_1023"
re "「だから、れおお姉ちゃんだって言ってるでしょー！！」"
"ぎゃあぎゃあ騒ぐ３人の声を聞いてると、思わず笑いがこぼれちゃう。"


show char tma02s2
with dis



voice "Mai_0874"
ma "「ぷぷっ、ふふふっ……玲緒、すごく大変そうね」"
"この功労に応えて、今日の朝ご飯は、玲緒の好きなものでも作ってあげようかしら……♪"


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


show char tre02s2
with dis



voice "Reo_1024"
re "「あー、おなかいっぱい♪」"


show char tma02s2 at left
show char tre02s2 at right as r
with dis



voice "Mai_0875"
ma "「ふふっ……でももう、玲緒もすっかり、我が家の一員だね」"


show char tre05s2 at right as r
with dis



voice "Reo_1025"
re "「そ、そうかな……？」"
voice "Mai_0876"
ma "「だってウチの家族とも、すごく仲良しじゃない。弟も妹も、すっかり玲緒に懐いちゃったし」"


show char tre08s2 at right as r
with dis



voice "Reo_1026"
re "「あれは……ワタシの家来なのっ」"


show char tma01s2 at left
with dis



voice "Mai_0877"
ma "「はいはい、そういうことでいいわ」"
"相変わらず、素直じゃないんだから……"
"家来に『お馬さん』やってあげる人なんて、いないわよ。"


show char tma02s2 at left
with dis



voice "Mai_0878"
ma "「でも、これでいつでも『沢口玲緒』になれそうね{image=image/exch001.png}」"


show char tre05s2 at right as r
with dis



voice "Reo_1027"
re "「さわぐち……れお？　そ、それって……っ！！」"
"わたしの言っている“意味”に気づいた玲緒は、火でも噴きそうなほど真っ赤になった。"
voice "Mai_0879"
ma "「きっと弟や妹も、わたしたちの結婚を祝福してくれるわ{image=image/exch001.png}」"


show char tre04s2 at right as r
with dis



voice "Reo_1028"
re "「な、ななななっ！？」"
voice "Mai_0880"
ma "「ああ、２人のウェディングベルが、わたしには聞こえてくるわ～」"


show char tre05s2 at right as r
with dis



voice "Reo_1029"
re "「ば、ばかっ、ワタシには聞こえないわよ」"
voice "Mai_0881"
ma "「それではここで、誓いのキスを……ちゅっ{image=image/exch001.png}」"


#※EV080
#allClear:
hide char tma02s2 at left
hide char tre05s2 at right as r
#lastBG:
#scene bg bg08a
scene bg EV80
with Dis



voice "Reo_1030"
re "「んっ、もぉ……ちゅっ{image=image/exch001.png}」"
"玲緒には、不意のキスに見えたかもしれないけれど。"
"本当はさっきから、ずっとしたかったのよね……"
"わたしと会う前の玲緒は『友達』とか『家族』とかいうのは、とても遠い存在だった。"
"でも今は、それがずっと近くにある。"
"さっき、赤ちゃんに手を振る玲緒を見ていて、わたしはハッキリとそれを感じた……"
"どうしようもないほど、愛しさが溢れて。"
"どうしても触れてしまいたくて、仕方なかった。"
voice "Mai_0882"
ma "「早く『沢口玲緒』になってね、玲緒♪」"
voice "Reo_1031"
re "「ま、麻衣のバカ{image=image/exch001.png}」"


#※EV80P1
scene bg EV80p1
with Dis



voice "Mai_0883"
ma "「うふふ、大好きよ、玲緒♪」"
voice "Reo_1032"
re "「もうっ……」"
"恥ずかしさで真っ赤になってしまう玲緒。"
"繋いだこの手を離したら、恥ずかしさのあまり、駆け出してしまうかも♪"
"でも絶対、わたしは彼女の後を追いかけるの。"
"そう……二人はずっと、一緒なんだから♪"
voice "Mai_0884"
ma "「どんなに逃げたって、ムダよ……わたしの方が、玲緒より足が速いんだからねっ{image=image/exch001.png}」"

"麻衣＆玲緒　ＨＡＰＰＹ　ＥＮＤ{image=image/exch001.png}"


#mes off
#mes clear
#system off


$ _skipping = False
$ _dismiss_pause = False
#log off


scene image "image/end05.png"
with Dis


pause5


#log on
$ _skipping = True
$ _dismiss_pause = True


#**暗転
scene black
with Dis


#♂MS
stop music fadeout 1


#//END
#set f2 5
jump staffroll



