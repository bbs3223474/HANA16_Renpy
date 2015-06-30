#「先生って……いいかも」

label S093:
$ save_name = "◇先生って……いいかも"


#**カフェ・昼
scene bg bg36a
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


"翌日、私はマネージャーさんに今後のことについて、話がしたいと連絡をした。"
"すると、ちょうど仕事で近くに来ているからと駅前のカフェまで出てきてくれと言われて。"
"なので今、カフェに来ている。"
voice "Mobmanage0004"
mg "「それで、話っていうのは……？」"


show char tka01f2
with dis



voice "Kaede_0459"
k "「実はですね……」"
"すごくドキドキする。"
"こんなわがままが、すんなり通るとは思えないけれど。"
"でも、昨日紗良に言われたように、ちゃんと自分の気持ちを……今、自分がどうしたいかをきちんと伝えなくちゃいけない。"
"私は一生懸命、話をして。"
"マネージャーさんは真剣に聞き入ってくれて。"
"そして……その気持ちが、伝わったみたいで。"
"ちゃんと引退を、検討して貰えることとなった。"
voice "Kaede_0460"
k "「あ、ありがとうございますっ」"
voice "Mobmanage0005"
mg "「楓さんの意思がそんなに固いなら、しょうがないわ。でも……」"


show char tka03f2
with dis



voice "Kaede_0461"
k "「でも……？」"
voice "Mobmanage0006"
mg "「お仕事、結構入ってきてるから、もうしばらく頑張ってね」"


show char tka01f2
with dis



voice "Kaede_0462"
k "「そ、そうですよね……はい」"
"それは自分でも、覚悟していた。"
"立つ鳥後を濁さず、最後までやりきるつもり。"
voice "Mobmanage0007"
mg "「引退まで一生懸命、サポートするからね」"
voice "Kaede_0463"
k "「はい、宜しくお願いします！」"
"私は深々と、頭を下げた。"
"そして、これからについて軽く打ち合わせをしてから、店を出た。"


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


"芸能界のお仕事をしばらく頑張って、終えたらマネージャーの勉強も始めて……"


show char tka03f2
with dis



voice "Kaede_0464"
k "「はぁ～……これから今まで以上に、大変な日々が始まるんだわ」"
"でもそれも、自分で決めたこと。"
"しっかりと前を見て、頑張らなきゃ。"


show char tka08f2
with dis



voice "Kaede_0465"
k "「これからは自分の為に進む道なのよ、泣き言なんて言っていられないわ」"
"そんな、今の私にできることは……"

#//SE：携帯の音
#♀SE012
play sound "sound/SE012.ogg"


show char tka01f2
with dis



voice "Kaede_0466"
k "「メール？　紗良からね……ふふふっ」"
"引退話がうまくいったのか、心配しているのね。"
"でも最後の方には『今日はデート行くんだよね？』と甘えた文章。"


show char tka02f2
with dis



voice "Kaede_0467"
k "「そうね……今の私にできることは、残った休暇を楽しむことだわ」"
"私は『もちろん、デートしましょうね』と返信をした。"


#**繁華街・昼
#allClear:
hide char tka02f2
#lastBG:
#scene bg bg08a
scene bg bg17a
with dis



show char tsa02f2
with dis



voice "Sara_0497"
sr "「楓ちゃん、こっちこっち♪　あっちのお店の服、ちょー可愛いよっ」"


show char tka01f2 at left
show char tsa02f2 at right as r
with dis



voice "Kaede_0468"
k "「もう、紗良ったら、はしゃいじゃって。でも久しぶりのお休みだし、そうなるのも無理ないわね」"


show char tsa10f2 at right as r
with dis



voice "Sara_0498"
sr "「そうそうっ、楓ちゃんとデートだなんて……ううっ、涙が溢れて止まらない～」"


show char tka02f2 at left
with dis



voice "Kaede_0469"
k "「事務所に話もついて気が楽になったし、今日はいっぱい２人で遊ぼうね{image=image/exch001.png}」"


show char tsa02f2 at right as r
with dis



voice "Sara_0499"
sr "「うん{image=image/exch001.png}　上手く話がついて良かったね。もうちょっとの間、紗良とのユニットも宜しくね」"
voice "Kaede_0470"
k "「こちらこそ。最後まで、どうぞ宜しくお願いします」"
voice "Sara_0500"
sr "「さっ、行こ行こっ、紗良、楓ちゃんとお揃いの服欲しいし、オシャレなカフェでティータイムを楽しみたいなっ」"
voice "Kaede_0471"
k "「ええ、ひとつずつ、その願い叶えて行きましょう」"
voice "Sara_0501"
sr "「きゃ～んっ、楓ちゃん、さすが紗良の王子様だねっ{image=image/exch001.png}」"
voice "Kaede_0472"
k "「うふふ、行きましょう」"
voice "Sara_0502"
sr "「は～いっ」"


#allClear:
hide char tka02f2 at left
hide char tsa02f2 at right as r
#lastBG:
#scene bg bg17a
with dis


"紗良のことも事務所のことも、丸く収まって。"
"私たちはラブラブデートを楽しんだのでした……"


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


"私は、お休みを存分にエンジョイしていた。"
"紗良とデート出来たのは、あの１日だけだったけれど……"
"家で料理を作って、紗良の帰りをのんびり待ってたり。"
"少しでもサポートになればと、カロリー計算をしたお弁当を作ったりと。"
"紗良にも、とても喜んでもらえたわ。"


show char tka01s2
with dis



voice "Kaede_0473"
k "「麻衣さんや優菜さんとも、いっぱい遊んだわね……」"
"買い物したり、お喋りしたり。"
"とても楽しい時間を過ごした。"
voice "Kaede_0474"
k "「ずっとお休みだと良いのに……っと、いけないいけない」"
"もっとシャキッとしなくては。"
"ふと、なんとなくいじっていた携帯の写真が目に入った。"
"写っているのは、いつものベストカップルの面々と、麗奈先生。"
"それと……貴子先生と瑠奈さん。"
voice "Kaede_0475"
k "「あっ、そういえば……しばらく貴子先生とあまり会っていないかも」"
"南の島のバカンスの後、なかなか会う機会が無くなってしまった。"
"あの時は、貴子先生と瑠奈さんのおかげで、紗良と気まずくならずに済んだのよね。"
voice "Kaede_0476"
k "「貴子先生……今、どうしているかな……」"
"私はつい気になって、メールを送ることにした。"

"『貴子先生、お久しぶりです。しばらくお会いしていませんが、お元気ですか？』"

voice "Kaede_0477"
k "「ちょっと硬い文面かもしれないけど、相手は年上の先生なんだから……これくらいでちょうどいいのよね」"

#♀SE050
play sound "sound/SE050.ogg"


"ピッと、送信ボタンを押す。"

#//SE：メール着信音
#♀SE012
play sound "sound/SE012.ogg"


"ほどなくして、メール着信音が鳴った。"
voice "Kaede_0478"
k "「あっ、貴子先生だわ。なになに……」"

"『楓さん、メールどうもありがとう。私は元気です。楓さんの近況も聞きたいから、どうでしょう……会ってお茶をしませんか？』"

"貴子先生からのお茶のお誘いだ。"
"断る理由は、私には無かった。"


show char tka02s2
with dis



voice "Kaede_0479"
k "「なんか、楽しみ……返信へんしんっと」"
"メールで待ち合わせ場所と時間を決めると、なんだかとてもうきうきとした気分になった。"


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


"待ち合わせ場所のカフェへ向かうと、貴子先生は既に来ていた。"
"駆けよって、声をかける。"


show char tka01f2
with dis



voice "Kaede_0480"
k "「貴子先生、お待たせしましたっ」"


show char tka01f2 at left
show char tta02s2 at right as r
with dis



voice "Takako0082"
t "「いいえ、私も今、来たばかりよ。お久しぶりね、楓さん」"


show char tka02f2 at left
with dis



voice "Kaede_0481"
k "「はい、貴子先生。本当に……お久しぶりです」"


show char tta01s2 at right as r
with dis



voice "Takako0083"
t "「元気にしてました？　最近もお仕事、活躍しているようね」"


show char tka01f2 at left
with dis



voice "Kaede_0482"
k "「そんな……私なんて、全然です」"


show char tta02s2 at right as r
with dis



voice "Takako0084"
t "「そんなに謙遜しなくて良いのに、うふふ……この間、楓さんが載っていた雑誌、つい買っちゃったわ」"


show char tka04f2 at left
with dis



voice "Kaede_0483"
k "「ええっ！？」"
voice "Takako0085"
t "「とても可愛かったわよ」"


show char tka05f2 at left
with dis



voice "Kaede_0484"
k "「あ、ありがとうございますっ……」"
"貴子先生が、私の載った雑誌を買ってくれたなんて……何だか恥ずかしいやら申し訳ないやら。"


show char tta01s2 at right as r
with dis



voice "Takako0086"
t "「ゆっくりお茶しながら、近況を聞かせてね」"


show char tka01f2 at left
with dis



voice "Kaede_0485"
k "「はいっ」"
"席について、お茶を注文する。"
"それが運ばれてくると、私たちは話を始めた。"
voice "Takako0087"
t "「最近は、どんな感じなのかしら？」"


show char tka03f2 at left
with dis



voice "Kaede_0486"
k "「それが……結構モデルの仕事が忙しくて。学校に来るのも、なかなかままならなかったんです」"


show char tta03s2 at right as r
with dis



voice "Takako0088"
t "「まあ、単位は大丈夫なの？」"
voice "Kaede_0487"
k "「ええ、それは問題ないんですけど……」"


show char tta01s2 at right as r
with dis



voice "Takako0089"
t "「勉強に遅れはない？　もし、わからないところがあったら、良かったら教えるからね」"
voice "Kaede_0488"
k "「ええっ、そんな……貴子先生もお忙しいでしょう、悪いですよ」"


show char tta02s2 at right as r
with dis



voice "Takako0090"
t "「そんなことないわ。楓さんの為ですもの、全然迷惑じゃないから、頼ってね」"


show char tka01f2 at left
with dis



voice "Kaede_0489"
k "「貴子先生……ありがとうございます」"
"ニッコリと笑って申し出てくれる貴子先生に、胸がジーンとしてしまう。"
"普段はおっとりとしている貴子先生だけど、こういうところは学生思いの教師だなって感じる。"


show char tta01s2 at right as r
with dis



voice "Takako0091"
t "「でも、相当忙しそうよね。雑誌にもいっぱい出ているし、テレビに、歌に……」"


show char tka03f2 at left
with dis



voice "Kaede_0490"
k "「そうなんです。私、あまり人前に出るの得意じゃないから、いつも緊張しちゃって……」"
voice "Takako0092"
t "「そんなことないわ。メディアに出演している楓さんは、立派に芸能人しているじゃない」"
voice "Kaede_0491"
k "「そう……ですか？」"
voice "Takako0093"
t "「ええ、雑誌を読んで、紗良さんと一緒に頑張っているなって、いつも瑠奈と言っているのよ」"


show char tka01f2 at left
with dis



voice "Kaede_0492"
k "「瑠奈さんも、見てくれてるんですね」"
voice "Takako0094"
t "「もちろんよ、紗良さんの方は元気なの？」"
voice "Kaede_0493"
k "「同じく忙しいんですけれど……久しぶりにこの間、デートしたんです」"


show char tta02s2 at right as r
with dis



voice "Takako0095"
t "「まあ、相変わらず仲が良いのね」"
voice "Kaede_0494"
k "「はい、一緒に暮らしているのに、すれ違うことも結構多いんですけれど……なんだかんだで上手くやっています」"
voice "Takako0096"
t "「それは何よりだわ」"
voice "Kaede_0495"
k "「あの……貴子先生のところはどうですか？　その……瑠奈さんとは……」"


show char tta01s2 at right as r
with dis



voice "Takako0097"
t "「まあ、私の方も……うまくは行ってるわ」"
voice "Kaede_0496"
k "「貴子先生のところも、仲良しなんですね」"


show char tta02s2 at right as r
with dis



voice "Takako0098"
t "「ええ、ワガママいっぱいで困るけどね、ふふふっ」"


show char tka02f2 at left
with dis



voice "Kaede_0497"
k "「フフ、何となく想像が付きます。貴子先生、大変ですね」"


show char tta01s2 at right as r
with dis



voice "Takako0099"
t "「わかってくれる？」"


show char tka01f2 at left
with dis



voice "Kaede_0498"
k "「ちょっとは……」"


show char tta05s2 at right as r
with dis



voice "Takako0100"
t "「そう言ってくれる人がいるのって嬉しいわ。まあ、ワガママ言われるのも、イヤじゃないんだけど」"
"ポッと赤くなりながら話す貴子先生は、まるで恋する乙女のよう。"
"大人なのに、可愛らしくみえた。"
voice "Kaede_0499"
k "「大事な恋人……なんですね」"
voice "Takako0101"
t "「その……まあ、そうね……でも、楓さんもそうでしょう？」"
voice "Kaede_0500"
k "「……はい」"


show char tta02s2 at right as r
with dis



voice "Takako0102"
t "「ふふふっ」"


show char tka02f2 at left
with dis



voice "Kaede_0501"
k "「ふふふっ」"
"なんとなく、こういう話題は少し照れくさい。"
"お互い顔を赤くしながら、笑い合う。"
"ごまかすように、お茶を飲み一息ついたところで『そう言えば……』と貴子先生が尋ねてきた。"


show char tta01s2 at right as r
with dis



voice "Takako0103"
t "「楓さんは将来どうするの？　３年の夏休みも過ぎたし、そろそろ考えなくてはならない時期よね」"


show char tka01f2 at left
with dis



voice "Kaede_0502"
k "「あっ……」"
voice "Takako0104"
t "「ミカ女を卒業したら、そのままモデルやタレントの仕事を広げていくの？」"
voice "Kaede_0503"
k "「それは……違います」"


show char tta04s2 at right as r
with dis



voice "Takako0105"
t "「えっ？」"
"私の台詞に、貴子先生が驚いた表情をする。"
voice "Kaede_0504"
k "「私、芸能人としてのお仕事は、もう辞めようと思っているんです」"


show char tta03s2 at right as r
with dis



voice "Takako0106"
t "「そうなの？　私はてっきり、今のまま芸能界で活躍していくものとばかり……」"
voice "Kaede_0505"
k "「事務所にも、もう話してあるんです。もう少しだけ仕事をしたら、辞めるって」"


show char tta01s2 at right as r
with dis



voice "Takako0107"
t "「そうなの……何かやりたいことでもあるの？」"
voice "Kaede_0506"
k "「はい。私、将来マネージャーになりたいんです」"
voice "Takako0108"
t "「まあ、マネージャー？」"
voice "Kaede_0507"
k "「はい。紗良のマネージャーになって、公私共に支えていきたいな……って思いまして」"


show char tta02s2 at right as r
with dis



voice "Takako0109"
t "「そう……夢があって、それに向かっていくのは素敵ね」"


show char tka03f2 at left
with dis



voice "Kaede_0508"
k "「なれるかどうかは、わからないですけど」"
voice "Takako0110"
t "「そんなことはないわ。頑張っていれば、いつか夢はきっと叶うもの」"


show char tka01f2 at left
with dis



voice "Kaede_0509"
k "「貴子先生……先生は、小さな頃から教師になりたかったんですか？」"


show char tta01s2 at right as r
with dis



voice "Takako0111"
t "「ええ、そうなの。学生時代からずっと、思っていたわ」"


show char tka02f2 at left
with dis



voice "Kaede_0510"
k "「そうなんですか。夢を叶えられて、貴子先生こそ素敵ですね。尊敬します」"
voice "Takako0112"
t "「ありがとう。楓さんは、小さな頃、何になりたかったの？」"


show char tka03f2 at left
with dis



"貴子先生にそう問われて、私は少し逡巡する。"
"私がなりたかったのは……"


show char tka01f2 at left
with dis



voice "Kaede_0511"
k "「実は……教師になりたかったんです」"
voice "Takako0113"
t "「教師に？」"
voice "Kaede_0512"
k "「そうなんです……だから、貴子先生が羨ましいです」"
voice "Takako0114"
t "「それは初耳だわ」"
voice "Kaede_0513"
k "「人にものを教えたり、人生を応援するのが好きで……」"
voice "Takako0115"
t "「確かに、楓さんは教師に向いているかもね。クラスでもいつも委員長を務めているんでしょう？」"
voice "Kaede_0514"
k "「はい……でも、もうマネージャーを目指すって決めたので」"
voice "Takako0116"
t "「うーん……だったら、そっちの夢も同時に追いかけてみたら？」"


show char tka04f2 at left
with dis



voice "Kaede_0515"
k "「えっ！？」"
"思ってもいなかった貴子先生の提案に、目が丸くなる。"
voice "Takako0117"
t "「私でよければ、その相談にも乗るわ」"


show char tka03f2 at left
with dis



voice "Kaede_0516"
k "「で、でも……そんなこと、可能でしょうか？」"
"二兎を追うものは、一兎をも得ずって言うし……"
voice "Takako0118"
t "「楓さん、夢は叶えるものなのよ」"


show char tka01f2 at left
with dis



voice "Kaede_0517"
k "「貴子先生……」"
"夢は叶えるもの……貴子先生のその言葉に、胸が熱くなる。"
"私の心の中で、新たな思いが生まれてくる。"
voice "Kaede_0518"
k "「是非、お願いします。マネージャーの業務にも役立つ知識が多そうですし……教師になる方法、教えて下さい」"
voice "Takako0119"
t "「ええ、私でよければ、できる限りサポートしていくわ」"
voice "Kaede_0519"
k "「貴子先生……ありがとうございます！！」"

#//SE：メール着信音
#♀SE012
play sound "sound/SE012.ogg"


"その時、携帯が鳴った。"
"メールの着信音だ。"
voice "Takako0120"
t "「楓さん、携帯が鳴っているわよ……出なくて良いの？」"
voice "Kaede_0520"
k "「ええ、メールですから、確認は後でします。それより貴子先生……」"
"私はメールをスルーして、貴子先生と話の続きをした。"


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
jump S094



