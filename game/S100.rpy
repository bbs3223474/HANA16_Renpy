#「紗良の演技指導は続く……」

label S100:
$ save_name = "◇紗良の演技指導は続く……"


#**貴子の部屋
scene bg bg26a
with Dis



#mes on
#system on


#♂MP22
play music "sound/BGM22.ogg"


show char tsa01f2
with dis



voice "Sara_0745"
sr "「なるほどなるほど～、これはお芝居の勉強になるねぇ～」"

#♀SE077
##se 0 SE077


"その後も、紗良は更にあちこちで、演技の勉強を続けていて。"
"メモ帳にペンを走らせていた。"
"真っ白だったノート部分は、あっという間に文字で埋め尽くされた。"
"かなり、頑張ったみたいね……"


show char tka03f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0752"
k "「ああ……勉強もそれくらい真剣にやれば、テストで良い成績がとれそうなのに」"


show char tsa03f2 at right as r
with dis



voice "Sara_0746"
sr "「それは無理な相談だよ～」"


show char tka02f2 at left
with dis



voice "Kaede_0753"
k "「ふふふっ」"


#allClear:
hide char tka02f2 at left
hide char tsa03f2 at right as r
#lastBG:
#scene bg bg26a
with dis


"そして今日は、貴子先生のマンションにコス衣装を返しに訪れたついでに。"
"貴子先生と瑠奈さんのお昼の風景を、何気なく見つめていた。"


show char tta08f2
with dis



voice "Takako0157"
t "「もう、瑠奈ったら……今日は楓さんと紗良さんが来てるんだから、わがままはなしでしょう！」"


show char tru01f2 at left
show char tta08f2 at right as r
with dis



voice "Runa_0123"
rn "「せんせい、わたしは誰がいても一緒よ。自分のしたいようにやるだけよ」"


show char tta03f2 at right as r
with dis



voice "Takako0158"
t "「だからってねぇ……ウィンナーをタコさん型に切らなかったからって、そんなにすねないで」"


show char tru08f2 at left
with dis



voice "Runa_0124"
rn "「こんな普通のウィンナーじゃイヤよ。食べないわ」"
voice "Takako0159"
t "「もう、味は一緒じゃない。そんなに子どもみたいなダダをこねないの」"
voice "Runa_0125"
rn "「ふん、せんせい……食べて欲しかったら、お願いすることね」"
voice "Takako0160"
t "「お、お願い？」"
voice "Runa_0126"
rn "「そうよ。『はい、あーん』ってしてくれたら、食べてあげないこともないわ」"
voice "Takako0161"
t "「そ、そんな……２人が見てる前で」"
voice "Runa_0127"
rn "「じゃあ、食べてあげない」"


show char tta05f2 at right as r
with dis



voice "Takako0162"
t "「もう、しょうがない子……ほら、口を開けて……あーん」"


show char tru01f2 at left
with dis



voice "Runa_0128"
rn "「最初から素直にそうしてくれれば良いのよ。あーん……もぐもぐ……」"


show char tta02f2 at right as r
with dis



voice "Takako0163"
t "「もう、瑠奈ったら……でも、そういうところも可愛いんだから{image=image/exch001.png}」"


#allClear:
hide char tru01f2 at left
hide char tta02f2 at right as r
#lastBG:
#scene bg bg26a
show char tsa01f2
with dis



voice "Sara_0747"
sr "「瑠奈ちゃんは、ツンデレの『ツン』が強いんだねぇ……これもアリだよね……ふむふむ」"


show char tka01f2 at left
show char tsa01f2 at right as r
with dis



voice "Kaede_0754"
k "「ツンデレにも、色々タイプがあるのね……奥が深いわ」"
"私たちは、貴子先生と瑠奈さんのカップルの食事風景を見て、しみじみとそう思ったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


show char tsa01s2
with dis



voice "Sara_0748"
sr "「こうなったら、もっと他のカップルも観察したいなぁ～」"
"勉強を続けているうちに、紗良はそんなことを言い始めた。"


show char tka03s2 at left
show char tsa01s2 at right as r
with dis



voice "Kaede_0755"
k "「他って？　もう大分、データは取れたんじゃないの？」"
voice "Sara_0749"
sr "「うん、でも……何かあともうひとつ、あっ……」"
"紗良は中庭の方に、何かを見つけたらしい。"
"私もそちらに、視線を動かすと……"


show char tka01s2 at left
with dis



voice "Kaede_0756"
k "「あれは……六夏さんと、沙雪さんね」"
"１年生カップルの２人が、仲が良さそうに話をしている。"
voice "Sara_0750"
sr "「紗良、あの２人にも頼んでみるね」"


hide char tsa01s2 at right as r
show char tka03s2 at left
with dis



voice "Kaede_0757"
k "「待ってよ、紗良」"


#allClear:
hide char tka03s2 at left
#lastBG:
#scene bg bg05a
with dis


"私も慌てて、紗良の後を追いかけて、中庭へと出ていった。"


#**中庭・昼
scene bg bg21a
with Dis



"私がなんとか、紗良に追いつくと。"
"もう紗良は、２人に協力のお願いをした後だった。"


show char trk04s2
with dis



voice "Rikka_1618"
rk "「ええっ……ワタシたちのことを、観察……ですか？」"


show char tsa03s2 at left
show char trk04s2 at right as r
with dis



voice "Sara_0751"
sr "「そうなの。できたてほやほやの新米カップルがどんな感じなのか、演技の勉強にしたくて……だからお願いっ」"

hide char tsa03s2 at left
hide char trk04s2 at right as r
show char tsa03s2 at sleft as l
show char trk04s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0897"
s "「私は……紗良さまのお役に立てるのでしたら、かまいませんが」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0752"
sr "「やったー！　沙雪ちゃん、ありがとう！！」"


show char trk03s2
with dis



voice "Rikka_1619"
rk "「で、でも、ワタシたちはリサ姉のような、ツンデレって感じではないですよ？」"


show char tsa01s2 at sleft as l
with dis



voice "Sara_0753"
sr "「それはわかっているけど、色々なカップルを参考にして、演技の幅を広げたいの」"
voice "Rikka_1620"
rk "「そうですか……でもワタシたちは、どうしたら良いんですか？」"
voice "Sara_0754"
sr "「あっ、それはいつも通り、イチャイチャしてくれればいいから」"


show char trk05s2
with dis



voice "Rikka_1621"
rk "「い、いつも通りに、イチャイチャって……」"
"六夏さんの顔が、かっと赤くなった。"
voice "Sara_0755"
sr "「紗良と楓ちゃんのことは、空気だとでも思ってくれれば良いよ～」"


show char tka01s2 at sleft as l
show char tsa01s2
show char trk05s2 at sright as sr
with dis



voice "Kaede_0758"
k "「ええ……無茶ぶりだとは思うけど、よろしくお願いします」"


show char trk04s2 at sright as sr
with dis



voice "Rikka_1622"
rk "「そそそそんなっ、先輩方……頭を下げないで下さいっ」"
"六夏さんは、頭を下げる私たちに、今度は顔を青くさせて、あわあわしていた。"


show char tsa01s2 at sleft as l
show char trk04s2
show char tsy01s2 at sright as sr
with dis



voice "Sayuki0898"
s "「六夏さん、先輩たちの為ですもの。できる限り協力してさしあげませんか？」"


show char trk01s2
with dis



voice "Rikka_1623"
rk "「沙雪さん……」"
voice "Sayuki0899"
s "「なるべく普段通りに、振舞えば良いのですね？」"


show char tsa02s2 at sleft as l
with dis



voice "Sara_0756"
sr "「うん、よろしくね～」"
voice "Sayuki0900"
s "「わかりました。六夏さん、始めましょう」"
voice "Rikka_1624"
rk "「は、はいっ、沙雪さん……」"
"沙雪さんの台詞に、生真面目に六夏さんが頷いた。"


#allClear:
hide char tsa02s2 at sleft as l
hide char trk01s2
hide char tsy01s2 at sright as sr
#lastBG:
#scene bg bg21a
show char trk01s2 at left
show char tsy01s2 at right as r
with dis



voice "Sayuki0901"
s "「六夏さん……私、カフェ、という所に行ってみたいです」"


show char trk03s2 at left
with dis



voice "Rikka_1625"
rk "「さ、沙雪さん？」"


show char tsy03s2 at right as r
with dis



voice "Sayuki0902"
s "「実は、私……そのカフェとやらに、まだ行ったことがありません」"
voice "Rikka_1626"
rk "「そ、そうなんですか？」"
voice "Sayuki0903"
s "「はい。ですから私と一緒に、行って頂けませんか？」"


show char trk01s2 at left
with dis



voice "Rikka_1627"
rk "「それはもちろん、はい、喜んで！」"


show char tsy01s2 at right as r
with dis



voice "Sayuki0904"
s "「ああ、嬉しい……六夏さん、わがままかもしれませんが私、映画も観に行ってみたいのですが」"
voice "Rikka_1628"
rk "「はい、わかりました。映画を観て、終わった後はカフェでゆっくりお話しましょう」"


show char tsy02s2 at right as r
with dis



voice "Sayuki0905"
s "「うふふ……嬉しいです。六夏さんとお付き合いをするようになってから、毎日が本当に新鮮です{image=image/exch001.png}」"


show char trk05s2 at left
with dis



voice "Rikka_1629"
rk "「さささっ、沙雪さんっ！？」"
"沙雪さんはその白くて細い指を、六夏さんの指にそっと絡ませた。"
"すると六夏さんが目に見えて、動揺しはじめた。"
"普段、手を繋ぐことも、滅多にないのかしら……"
"沙雪さんは私たちの為に頑張って、六夏さんに甘えてくれているみたい。"


show char tsy03s2 at right as r
with dis



voice "Sayuki0906"
s "「私と、こうやって……手を繋ぐのはイヤ、ですか？」"
voice "Rikka_1630"
rk "「イヤなんて、そんなことは全然ないです……だけど」"
voice "Sayuki0907"
s "「……何でしょうか？」"
voice "Rikka_1631"
rk "「とても、緊張します……はぁ、はぁ」"


show char tsy04s2 at right as r
with dis



voice "Sayuki0908"
s "「まあ……」"
voice "Rikka_1632"
rk "「ワタシは、沙雪さんと一緒にいるだけで、胸がドキドキするんですけど……触るともっと、ドキドキしてしまって」"


show char tsy05s2 at right as r
with dis



voice "Sayuki0909"
s "「私も……同じです」"


show char trk04s2 at left
with dis



voice "Rikka_1633"
rk "「さ、沙雪さんもですかっ！？」"
voice "Sayuki0910"
s "「ええ、他の方だと何とも思わないのに、好きな方に触れると、どうしてこんなに心臓がはちきれそうになってしまうのでしょう」"


show char trk02s2 at left
with dis



voice "Rikka_1634"
rk "「沙雪さん……{image=image/exch001.png}」"


show char tsy02s2 at right as r
with dis



voice "Sayuki0911"
s "「少しずつ、恥ずかしがらずに手を握るのに、慣れていければ……良いですね{image=image/exch001.png}」"
voice "Rikka_1635"
rk "「はい……はいっ！」"


#allClear:
hide char trk02s2 at left
hide char tsy02s2 at right as r
#lastBG:
#scene bg bg21a
with dis


"………………"
"六夏さんはものすごく照れていて、沙雪さんははにかんでいる。"
"沙雪さんと六夏さんの恋人繋ぎは、本当に不器用で……でもとっても、仲の良いカップルに思えた。"


show char tsa02s2
with dis



voice "Sara_0757"
sr "「ああ……ザ・青春、ですなぁ～」"


show char tka02s2 at left
show char tsa02s2 at right as r
with dis



voice "Kaede_0759"
k "「ええ、本当に……初々しいカップルね」"
voice "Sara_0758"
sr "「良いものを見せて貰いました……しっかり、メモメモ」"

#♀SE077
##se 0 SE077


"こうして紗良のメモ帳の１ページは、また埋まっていったのでした。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**新校舎廊下・昼
scene bg bg05a
with Dis



#mes on
#system on


show char tka01s2
with dis



voice "Kaede_0760"
k "「それで紗良……大分ツンデレについて、掴めてきた？」"


show char tka01s2 at left
show char tsa01s2 at right as r
with dis



voice "Sara_0759"
sr "「ツンデレも勉強になったけど……紗良は気付いたんだ、楓ちゃん」"


show char tka03s2 at left
with dis



voice "Kaede_0761"
k "「何に？」"
voice "Sara_0760"
sr "「今の紗良にとって『観察すること』が、何より勉強になるんだって」"


show char tka01s2 at left
with dis



voice "Kaede_0762"
k "「それは……そうかもしれないわね。色々なものを見つめて吸収することが、良い女優への道かもしれないわ」"
voice "Sara_0761"
sr "「うん。普段の自分ではわからない、他の人や考えや行動を学ぶことがすごく大事なんだね」"
voice "Kaede_0763"
k "「なんだか紗良、すっかり女優さんらしい顔になったわよ」"
voice "Sara_0762"
sr "「うーん……そうかなぁ？」"


show char tka02s2 at left
with dis



voice "Kaede_0764"
k "「ええ、良い女優さんになれるわ、きっと」"


show char tsa02s2 at right as r
with dis



voice "Sara_0763"
sr "「えへへっ……うん、お母さんのような女優に、いつかなりたいな」"
"女優である母の血が今、紗良の中でも目覚めつつあるようだった。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**楓の部屋・夜
scene bg bg12c
with Dis



#mes on
#system on


"紗良の取ったメモには、びっしりと色々なカップルについて、独自に付けたポイントが書かれている。"
"それを見ながら、紗良と一緒に家で復習することにした。"


show char tsa01s2
with dis



voice "Sara_0764"
sr "「えっと、玲緒さまくらいのツンデレだと、紗良がやるとちょっとわがままに見えちゃうかな」"


show char tka01f2 at left
show char tsa01s2 at right as r
with dis



voice "Kaede_0765"
k "「そうね、玲緒さんの可愛らしさと、紗良の可愛さはまた別だからね」"


show char tsa03s2 at right as r
with dis



voice "Sara_0765"
sr "「はうっ！　楓ちゃんが紗良を可愛いって……って、だめだめ、今は演技の勉強中」"
voice "Kaede_0766"
k "「余計なことに気を取られないで。ねぇ、ここにある璃紗さんのツンを取り入れてみたらどうかしら？」"


show char tsa02s2 at right as r
with dis



voice "Sara_0766"
sr "「あっ、それいいかも～」"
voice "Kaede_0767"
k "「璃紗さんのツンをいれて、玲緒さんのデレな可愛さを見せるのは、どうかしらね」"
voice "Sara_0767"
sr "「うんうん、ちょっと自分の中でこうしたら良いんじゃないかっていうイメージ、固まって来たよ」"
voice "Kaede_0768"
k "「本当に？」"


show char tsa01s2 at right as r
with dis



voice "Sara_0768a"
sr "「じゃあ楓ちゃん、一度……本読みに付き合ってくれない？」"


show char tka02f2 at left
with dis



voice "Kaede_0769"
k "「ええ、もちろんいいわよ」"
"私は台本を手に取り、それを見ながら、紗良の演技をチェックしてみた……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#※EV062
scene bg EV62
with Dis



#mes on
#system on


voice "Sara_0769"
sr "「もう……どうして私が、アナタの散歩に付き合わなくちゃいけないの！？」"
voice "Sara_0770"
sr "「こう見えても、紗良……じゃなくて私、すごく忙しいのよ。ヒマじゃないんだからね！」"
voice "Sara_0771"
sr "「えっ、だったら時間を作れ、ですって？　どこまで自分勝手なのよ、もう……」"
voice "Kaede_0770"
k "「紗良……うん、なんか今までより全然いいわ。『ツン』がつかめてきたっていうのも、うなずけるわ」"
"ちょっと偉そうに、上から目線で胸を張って。"
"ツリ目の加減と、口もとの尖らせ方も、なかなか良い感じで。"
"ムッとした雰囲気を保ちつつ、私を睨むように見つめていた。"
voice "Kaede_0771"
k "「さあ、次は『デレ』だけど……」"
"紗良は小さく、一呼吸ついて……そして表情を変えた。"
voice "Sara_0772"
sr "「なっ、何よ、誰も付き合わないとは、言ってない……でしょ、もう……」"
voice "Kaede_0772"
k "「あっ……なんかこの変化、いい……かも」"
voice "Sara_0773"
sr "「お前も本当は行きたいんだろう、って？　ちち、違うわよ、バカ……」"


#※EV062P2
scene bg EV62p1
with Dis



voice "Sara_0774"
sr "「そんなんじゃ、ないんだからね……勘違い、しないでよね……{image=image/exch001.png}」"
voice "Kaede_0773"
k "「ぁ……ああ、紗良………………」"
"なんか……今の、紗良……すごく、いい……かも\001"


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


#**楓の部屋・昼
scene bg bg12c
with Dis



show char tka01f2
with dis



voice "Kaede_0774"
k "「………………」"


show char tka01f2 at left
show char tsa03s2 at right as r
with dis



voice "Sara_0775"
sr "「ねぇ、楓ちゃん。今の……どうだった？」"
voice "Kaede_0775"
k "「………………」"
voice "Sara_0776"
sr "「……楓ちゃん？」"
voice "Kaede_0776"
k "「い……いい……」"
voice "Sara_0777"
sr "「えっ？？」"


show char tka02f2 at left
with dis



voice "Kaede_0777"
k "「いいわ、見違えるように良くなったわよ、紗良、この調子よ！　一瞬、本気で見惚れたわ」"


show char tsa02s2 at right as r
with dis



voice "Sara_0778"
sr "「ほ、ほんとっ？　やったー！」"
voice "Kaede_0778"
k "「みんなに協力して貰って、頑張った甲斐があったわね、紗良」"
voice "Sara_0779"
sr "「うん、本当にみんなには、感謝感謝だよ～」"
voice "Kaede_0779"
k "「もっともっと練習すれば、絶対もっと良くなるわ」"
voice "Sara_0780"
sr "「よぉし、紗良、頑張るから、楓ちゃんもよろしくね」"
voice "Kaede_0780"
k "「ええ、いくらでも付き合うわよ」"


#**夜空
#allClear:
hide char tka02f2 at left
hide char tsa02s2 at right as r
#lastBG:
#scene bg bg12c
scene bg bg42c
with Dis



"それからというもの、日々、紗良の腕は磨かれていって。"
"やがてそれを見ていた私も、紗良の演技にグッとくるようにまでなってきて……"
voice "Kaede_0781"
k "「ああ……紗良……こんな紗良、初めてよ……{image=image/exch001.png}」"


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
jump S101

