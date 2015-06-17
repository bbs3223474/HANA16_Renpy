#「六夏の苦悩……」

label S006:
$ save_name = "◇六夏の苦悩……"


#※ここは六夏視点で

#**中庭・昼
scene bg bg21a
with Dis



#mes on
#system on


#♂MP06
play music "sound/BGM06.ogg"


show char trk01s2
with dis



voice "Rikka_0011"
rk "「ふぅ……」"
"昼休み。"
"教室ですばやくお昼を食べ終えると、ワタシは１人になりたくて、中庭まで出てきた。"
"クラスメイトたちはひょっとすると、ワタシのことを探しているかも。"


show char trk03s2
with dis



voice "Rikka_0012"
rk "「でも質問には、うかつに答えたくないし……あーあ、せっかくリサ姉と再会出来たっていうのに」"
"そのリサ姉が、このワタシの恋人だなんて。"
"みんな、勘違いにもほどがある。"
"教室にいる間は、みんなそのことを聞きたがって目がキラキラしている。"
voice "Rikka_0013"
rk "「お嬢様学校の子って、こんなに噂好きだったんだな……はぁ～」"
"リサ姉も、同じ目に遭っているのかな？"
voice "Rikka_0014"
rk "「リサ姉に、迷惑かけるつもりじゃなかったんだけど……」"
"自分のことなら、自分一人で我慢すればいいことだけれど。"
"今回は大好きなリサ姉と、その恋人である美夜さまに、多大なる迷惑をかけてしまった。"
voice "Rikka_0015"
rk "「ああ、どうすればいいのかな……」"
"美夜さまはワタシのこと、すごく怒っているんだろうな。"
"この間は、話の途中でいなくなってしまったし……"
voice "Rikka_0016"
rk "「うううっ……なんかワタシ、昔とちっとも変わってないのかもしれないなぁ。いつもリサ姉の後をついてまわってた頃と……」"
"あれから、ずいぶん経つと言うのに……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**住宅街・夕
scene bg bg08c
with Dis



#mes on
#system on


show char trk01s2
with dis



voice "Rikka_0017"
rk "「夕飯の買出しも終わったし……もう、帰るかな」"
"結局今日も、また美夜さまの誤解はとけなかった。"
"ワタシは足取りも重く、自分の家へと向かう。"
voice "Rikka_0018"
rk "「ワタシなんかが、ミカ女に通っているのも、らしくないけれど……」"
"立ち止まり、フッと上を見上げる。"
"そこには高級そうなマンションがあった。"


show char trk03s2
with dis



voice "Rikka_0019"
rk "「このマンションに１人暮らしをしているなんて、もっとワタシらしくない気がするよ……」"
"新婚ほやほやの母と義父の側に居づらいこともあって、ミカ女の近くに部屋を借りてもらったんだけど。"
"まさか、こんな高そうなところだとは思わなかった……"


show char tta01s2 at left
show char trk03s2 at right as r
with dis



voice "Takako0000"
x "「……あら、おかえりなさい」"
"マンションの出入り口に立っていると、近所のお姉さんとすれ違った。"


show char trk01s2 at right as r
with dis



voice "Rikka_0020"
rk "「あっ……ただいま、です」"


hide char tta01s2 at left
with dis


"会釈をして、通り過ぎる。"
voice "Rikka_0021"
rk "「ああ……綺麗な人だなぁ……」"
"ＯＬさんかなぁ？"
"ここのところ、よく見かける。"
"こういうところのご近所つきあいなんて、薄いものかと思っていたけれど。"
"あの人だけはいつもちゃんと挨拶してくれるんだよね。"
"顔だけじゃなくて、心もきっと綺麗な人なんだろうなぁ。"
voice "Rikka_0022"
rk "「沙雪さんの綺麗さとは、また違う綺麗さで……はっ」"
"ちょっと恥ずかしくなったワタシは、そのまま黙ってエントランスに入っていった。"


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



voice "Rikka_0023"
rk "「よし、ダンボールも全部開けたし……後はこれをしまうだけかな」"
"引越しの後片付けをしていると、不意にアルバムが目に入った。"


show char trk02f2
with dis



voice "Rikka_0024"
rk "「これ、懐かしいなぁ～」"
"アルバムをペラペラと捲ると、リサ姉と一緒に写っている写真が目に止まった。"
"一気に、懐かしい気分になった。"
voice "Rikka_0025"
rk "「この頃はいっぱい、面倒を見てもらったんだよね～」"
"その後のページからは、リサ姉はいなくなるけど。"
"代わりに大会での、自分の写真が増えていく。"


show char trk01f2
with dis



voice "Rikka_0026"
rk "「リサ姉が引っ越した後から……色々あったなぁ」"
"ワタシは写真を見ながら、これまでのことを振り返っていた。"
"リサ姉の引越し後、近所で他に遊んでくれる人もいなくて。"
"放課後、ワタシはずっと１人だった。"
voice "Rikka_0027"
rk "「その暇つぶしになればって思って、陸上を頑張るようになったんだよね」"
"クラブに入って、遅くまで練習に励んだ。"
"何も考えずに、頭の中を空にして走るのは、自分にはよく合っていた。"
"気がつけば、大会でも記録を出すほどにもなっていた。"
"そんなある日……急に、母親が再婚することになった。"
"もちろん、反対なんてしなかった。"
"女手ひとつで自分を育ててくれた母に、幸せになって欲しかったから。"
voice "Rikka_0028"
rk "「でもそこから、ワタシの生活が変わっていったんだよね……」"
"母の再婚相手は資産家で、ワタシたち母娘は揃って、その家にお世話になることになった。"
voice "Rikka_0029"
rk "「でも結局、ワタシはそこを出て、一人暮らしになっちゃったけどね」"
"家の前で母と義父とワタシ、３人で撮った写真が、アルバムの一番最後に貼ってあった。"
"その写真の中のワタシは……ミカ女の制服を着ていた。"
voice "Rikka_0030"
rk "「学校は今まで通り、普通の公立で良かったのに……世間体を考えてミカ女へ入ることになったんだっけ」"
voice "Rikka_0031"
rk "「ミカ女……お嬢様学校だってことは昔から知っていたけれど、まさかこんなところだったなんて……」"


#（回想シーン）

#**新校舎教室・昼
#allClear:
#hide char trk01f2
#lastBG:
scene bg bg04a
with rr


voice "mobJyosiA0013"
mobA "「六夏さん、ごきげんよう」"


show char trk03s2
with dis



voice "Rikka_0032"
rk "「ご、ごきげんよう……」"
"ミカ女に入学して結構経つけれど、このお嬢様的な挨拶に、ワタシはまだ慣れずにいた。"
"どうしても、ぎこちなさを感じる。"
voice "mobJyosiA0014"
mobA "「もうクラスには慣れましたか？　外部からの方は、わからないことも多いでしょう」"
voice "Rikka_0033"
rk "「ええ……まあ」"
"正直、わからないことだらけです……とは、言えなかった。"
voice "mobJyosiA0015"
mobA "「わからないことがあれば、わたくしにお尋ねになってくださいね」"
voice "Rikka_0034"
rk "「は、はぁ……」"
voice "mobJyosiB0011"
mobB "「あら、アナタばかりずるいわ。六夏さん、私も頼ってくださいね」"
voice "mobJyosiA0016"
mobA "「貴女こそ、しっかりアピールなさってるじゃない」"
voice "mobJyosiB0012"
mobB "「別に、そんなことありませんわ」"
voice "Rikka_0035"
rk "「あ……あはは……」"
"何を言い合っているのか、よくわからないけれど圧倒された。"
"ここは笑顔で、何とかこの場を切り抜けないと。"


show char trk02s2
with dis



voice "Rikka_0036"
rk "「あ、あの……皆さん、ご親切にありがとうございます。何かあったら是非、お願いしますね」"
"穏やかに、微笑んでみせる。"
voice "mobJyosiA0017"
mobA "「は、はい{image=image/exch001.png}　もちろんですわ」"
voice "mobJyosiB0013"
mobB "「ええ、六夏さん{image=image/exch001.png}」"
"何故か２人とも、顔を赤らめて、ワタシから離れていく。"
"『さすが王子ですわ』とか、意味不明の言葉が聞こえてくるけれど、それはどうでもいい。"


show char trk03s2
with dis



voice "Rikka_0037"
rk "「なんて言うか……もう、人種が違う感じ」"
"こんなところに、自分は馴染んでいけるのだろうか。"
"高い入学金を払ってくれた義父には悪いけれど正直、普通の学校に転校したい。"
"そう思ったのはもう、１度や２度ではなかった。"
voice "Rikka_0038"
rk "「でも、気になる人もいるし……あっ」"

#//SE：ドアの開く音
#♀SE003
play sound "sound/SE003.ogg"


show char tsy01s2
with dis



voice "Sayuki0001"
s "「………………」"
voice "mobJyosiA0018"
mobA "「あら、沙雪さんだわ」"
voice "mobJyosiB0014"
mobB "「白雪姫よ……いつも優雅ね」"


show char trk05s2
with dis



voice "Rikka_0039"
rk "「沙雪……さん………………ぁぁ」"
"教室に現れた彼女は、白河沙雪さんだった。"
"名家のお嬢様である彼女は『究極の淑女』とも呼ばれているくらいで、その美しい姿に誰もが見惚れていた……もちろん、ワタシも。"


show char tsy02s2
with dis



voice "Sayuki0002"
s "「皆さま、ごきげんよう」"
voice "mobJyosiA0019"
mobA "「ごきげんよう、沙雪さん」"
voice "mobJyosiB0015"
mobB "「ごきげんよう」"
"ゆったりと沙雪さんは、こちらに向かって歩いてくる。"
"ドキドキ……ドキ……"

#♀SE004
play sound "sound/SE004.ogg"


"胸の鼓動が、やたらとうるさい。"
"ああ、もうすぐ沙雪さんが、ワタシの側に来る……来てしまう。"


show char trk05s2 at left
show char tsy02s2 at right as r
with dis



voice "Sayuki0003"
s "「六夏さん……ごきげんよう」"
voice "Rikka_0040"
rk "「え、ええ……ごきげんよう、沙雪さん……」"
"ああ、今日もなんて綺麗なんだろう、沙雪さんは。"
"色白の肌に、赤く美しい唇。"
"まるで本物の、白雪姫のよう。"
"あまりジロジロ見るのも、失礼な気がして。"
"ワタシはすぐに、彼女から目を逸らした。"


hide char tsy02s2 at right as r
with dis


"だけど心の中では、同じ台詞が繰り返し再生されていた。"
voice "Sayuki0004"
s "『六夏さん、ごきげんよう』"
"沙雪さんが……自分の名前を呼んでくれる。"
"それだけで、何とも言えず嬉しかった。"
"ワタシがミカ女に居続ける理由は、この沙雪さんにあった。"
"ワタシはこのミカ女で、生まれて初めて『一目惚れ』というものを経験した。"
"その相手こそ……彼女だった。"
"不慣れな環境だけど、彼女がいてくれるなら、頑張れそうかも。"
"ここを辞めて、彼女に２度と会えなくなるなんて、考えられない。"
"彼女の姿を少しでも長く、見ていたい……"

hide char trk05s2 at left
show char trk05s2
with dis


voice "Rikka_0041"
rk "「……ああ……本当に、素敵……」"
voice "mobJyosiC0005"
mobC "「六夏さん……？」"


show char trk01s2
with dis



voice "Rikka_0042"
rk "「……うん、そうだよね、頑張らなくちゃ」"
voice "mobJyosiC0006"
mobC "「六夏さん、どこかお加減でも悪いのですか？」"
voice "Rikka_0043"
rk "「あっ、せ、先輩……来ていたのですか？」"
"沙雪さんのことを考えていると、いつの間にか目の前に、陸上部の先輩がいた。"
voice "mobJyosiC0007"
mobC "「週末の大会についての打ち合わせ、今日の放課後になりましたので、お知らせにと思いまして」"
voice "Rikka_0044"
rk "「そうですか。わざわざこちらまで出向いてくださり、ありがとうございます」"
voice "mobJyosiC0008"
mobC "「ちょうど近くに来る用事がありましたから……それに六夏さんにも会いたくて、ふふっ」"
"先輩はニコッと笑うと、ワタシの手を取った。"


show char trk04s2
with dis



voice "Rikka_0045"
rk "「えっ！？」"
voice "mobJyosiC0009"
mobC "「六夏さん、期待してますわ……大会、頑張ってくださいね♪」"


show char trk01s2
with dis



voice "Rikka_0046"
rk "「は、はい……頑張ります」"
"ぎゅっと握られた手を離すと、先輩は帰っていった。"
voice "mobJyosiA0020"
mobA "「……ねぇ、今の、ご覧になりました？」"
voice "mobJyosiB0016"
mobB "「六夏さん、上級生のお姉さま方にも人気がおありなのですね……あぁ」"
"何だかワタシ、いつの間にか教室の注目を浴びているような……気のせいかな？"


show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0005"
s "「あの、六夏さん……大会って陸上ですか？」"


show char trk04s2 at left
with dis



voice "Rikka_0047"
rk "「わぁ！？」"


show char tsy03s2 at right as r
with dis



voice "Sayuki0006"
s "「どうかなさいました、六夏さん？」"
"急に沙雪さんに話しかけられたら、ビックリもしますって。"
"ワタシは何とか落ちつきながら、沙雪さんの問いかけに答えた。"


show char trk03s2 at left
with dis



voice "Rikka_0048"
rk "「し、失礼しました、え、ええ……陸上の大会です」"


show char trk03s2 at left
with dis



voice "Sayuki0007"
s "「そうですか……では、頑張ってくださいね」"
voice "Rikka_0049"
rk "「は、はいっ」"


hide char tsy03s2 at right as r
with dis


"沙雪さんはそれだけ言うと、クラスメイトの輪の中に戻っていった。"


#allClear:
#hide char trk03s2 at left
#hide char tsy03s2 at right as r
#lastBG:
#scene bg bg04a
show char trk01s2
with dis



voice "Rikka_0050"
rk "「が、頑張ってください……って……」"
"沙雪さんがワタシに、そんな言葉をかけてくれるなんて。"
"なんか、胸が熱い……どうしよう、メチャクチャ嬉しい！！"


show char trk08s2
with dis



voice "Rikka_0051"
rk "「ワタシ、頑張ります……沙雪さん、見ていてくださいね」"
"彼女の美しい後ろ姿を見つめながら、ワタシはそう強く誓った。"
"それからワタシは、以前にも増して陸上に力を入れた。"
"沙雪さんに良いところを見せたいという、その一心で。"
"そして……ついには大会で自己ベスト記録を打ち立ててしまい、沙雪さんどころか、みんなの注目を浴びることとなったのだった……"

#（回想シーン終了）

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
with lr


show char trk03f2
with dis


#mes on
#system on



voice "Rikka_0052"
rk "「ちょっと、頑張りすぎたかも……」"
"陸上で一躍有名になったワタシは、いつしか１年生のベストカップル候補にあがっていた。"
voice "Rikka_0053"
rk "「ベストカップルなんて、最初は恥ずかしいと思ったけれど……」"
"実はちょっと、ううん、すごく嬉しくもあった。"
"何と言ってもワタシのお相手は、想いを寄せる彼女……沙雪さんだったから。"
"完璧超人である彼女が選ばれるのは、当然としても。"
"ワタシまで、一緒に選んでもらえるなんて……ラッキーとしかいいようがない。"


show char trk01f2
with dis



voice "Rikka_0054"
rk "「出来れば本当に、沙雪さんとカップルになりたいな……」"
"口にしてみても、それが到底現実になるとは思っていない。"


show char trk03f2
with dis



voice "Rikka_0055"
rk "「無理に……、決まってるよね……」"
"お嬢様の中のお嬢様である、沙雪さん。"
"こっちは『なんちゃってお嬢様』で、中身は庶民のワタシ。"
voice "Rikka_0056"
rk "「とても、釣り合うはずないよね……はぁ～」"
"スポーツは自信あるけれど、恋に関しては弱気になってしまう。"
"おっとりしてるミカ女のお嬢様方と比べたら、多少はワタシの方が、日常的なことは要領よくこなせる。"
"でもそれだけではとても、彼女に好きになってもらえるわけがない。"
voice "Rikka_0057"
rk "「……あっ、まだ片付けの途中だったんだ」"
"アルバムをパタンと閉じて、立ち上がる。"
voice "Rikka_0058"
rk "「夕飯の支度もあるし、早くやっちゃわないと……」"
"その後、大急ぎで片づけをすませて。"
"何とか荷物の整理は、終わらせることが出来たのだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎教室・昼
scene bg bg04a
with Dis



#mes on
#system on


show char trk03s2
with dis



voice "Rikka_0059"
rk "「ん……なんか、騒がしいな……」"
"教室に入ると、お嬢様らしからぬキャーキャーという黄色い悲鳴が聞こえた。"
voice "Rikka_0060"
rk "「あの……どうかしたんですか？」"
voice "mobJyosiA0021"
mobA "「あっ、六夏さん、大きな虫が教室に！」"
voice "Rikka_0061"
rk "「虫……？」"
"教室の中を見回すと、ぶんぶんと小さな虫が飛び回っていた。"
"全然、大きくないのに……虫一匹で大騒ぎなんて、さすがお嬢様学校かも。"


show char trk01s2
with dis



voice "Rikka_0062"
rk "「ちょっと待っててくださいね……えーと、いらない紙ってありますか？」"
voice "mobJyosiB0017"
mobB "「こ、これで良かったら……」"
"期限の過ぎたクラッシックコンサートのチラシを、パッと渡される。"
"ワタシはそれを丸めて虫を追い払い、窓の外へと逃がしてやった。"
"叩いても良かったけれど、可哀想だし……たまたま、この教室に迷いこんだだけなんだから。"
voice "Rikka_0063"
rk "「はい、これでもう大丈夫ですよ……えっ！？」"


show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0008"
s "「六夏さん……ああ、ありがとうございます」"
"みんなの方を振り返った瞬間、何故か沙雪さんにお礼を言われてしまった。"
voice "Sayuki0009"
s "「突然、虫が入って来たときはどうすればいいのかと思いました。六夏さんがいて下さって、本当に助かりました」"
voice "Rikka_0064"
rk "「い、いえ……こんなの、大したことじゃないから……」"
"ああ、心臓がバクバクしている……沙雪さんの前だと、大会の決勝よりも、ずっと緊張してしまう。"
voice "mobJyosiA0022"
mobA "「本当に六夏さんは、頼りになりますわね」"
voice "mobJyosiB0018"
mobB "「白雪の騎士、そのものですわ」"
voice "Rikka_0065"
rk "「あは、はははっ……」"
"白雪の騎士……か。"
"みんな口々に、ワタシをそう呼んで、誉めてくれるけれど。"
"今のワタシじゃとても、沙雪さんの騎士なんて、務まりそうになかった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with dis



#♂MS
stop music fadeout 1


#//END
jump S007
