# 注：从S002开始出现两个立绘同时出现的场景，根据Ren'py官方文档的要求，
# 同一个show命令出现两次时，如果它们的Tag都一样，那么新一行的show将会覆盖旧的。
# 因此，在使用at left、at right时，需要在其中一个后面加上as命令，
# 将其中一个show命令赋予Tag，使其与另一个立绘区分开，这样才不会被游戏覆盖显示。
# 因此，可以看见代码中使用了show char tri08s2 at right as r这样的代码，
# 也就是说，通过as r，对char tri08s2这张立绘赋予了“r”这个Tag，另外Tag名称可随意。
# 执行时，show char tmi01s2 at left将之前的show char tri08s2覆盖，因为他们的Tag都是相同的（空白）。
# 如果同一个背景要换回一人或两人的，那么需要使用hide命令将原先被赋予了Tag的立绘先隐藏，
# 注意是所有赋予了Tag的立绘才需要hide，本来没有赋予Tag的不用，直接用下一个show命令覆盖，
# 然后再继续正常使用show命令，并根据实际情况添加Tag。
# 如果需要更换背景，那么直接使用scene命令即可清除屏幕上所有图像而无需hide。
# 如果两个立绘中需要单独替换其中一个人的立绘，那么只需要按照设定的Tag来使用show命令即可。

#「新１年生のベストカップル」

label S002:


$ save_name = "◇新１年级学生的最佳情侣"


#**アトリエ・昼
scene bg bg29a
with Dis



#mes on
#system on


#♂MP17
play music "sound/BGM17.ogg"


show char tri08s2
with dis



voice "Risa_0023"
r "「美夜……你在的吧？　我进去了哦」"
"结果，今天在教室也没有看见美夜的身影。"
"就这样拖到了放学之后。"
"白天明明还不在的，一上完课，她就回到了画室。"
voice "Risa_0024"
r "「真是的……你绝对是明知故犯」"
"我在她回答之前，就打开了门。"
"私只有我和美夜才知道的，这间秘密画室的门。"


show char tmi01s2 at left
show char tri08s2 at right as r
with dis



voice "Miya_0000"
m "「啊，欢迎观临，璃纱。我正好泡了茶哦」"
"她就好像等着我来似的，房间里飘满了红茶的香气。"
"嘛，我也不是不知道。"
voice "Risa_0025"
r "「美夜，这茶我会喝的……但是，在这之前」"


show char tmi02s2 at left
with dis



voice "Miya_0001"
m "「一直以来的责备吗，呵呵呵」"


show char tri07s2 at right as r
with dis



voice "Risa_0026"
r "「真是！　既然你知道就别老让我说啊。今天你又没去上课吧」"


show char tmi01s2 at left
with dis



voice "Miya_0002"
m "「是啊，逃掉了」"


show char tri08s2 at right as r
with dis



voice "Risa_0027"
r "「我找遍了学校都没发现你，你到底跑哪去了啊？」"


show char tmi08s2 at left
with dis



voice "Miya_0003"
m "「……在你的身后，哦」"


show char tri04s2 at right as r
with dis



voice "Risa_0028"
r "「呀！　这种说法，听着挺可怕的……就像那个都市传说一样」"


show char tmi01s2 at left
with dis



voice "Miya_0004"
m "「那个都市传说……你说的哪个？」"


show char tri03s2 at right as r
with dis



voice "Risa_0029"
r "「就是那个啊。玩偶给你打电话那个」"
voice "Risa_0030"
r "「现在，我正在去你家……现在，我到了玄关……就这样，越来越接近你」"
voice "Risa_0031"
r "「接着，到最后………………」"
voice "Miya_0005"
m "「在你的身后……？」"
voice "Risa_0032"
r "「是啊……很可怕对吧」"
voice "Miya_0006"
m "「璃纱，你明明喜欢可爱的东西，还会怕这种传说吗？　要是去了你的房间，身后不也有一大堆玩偶吗」"


show char tri01s2 at right as r
with dis



voice "Risa_0033"
r "「你这例子总感觉有点不对……嗯，今天的红茶还真好喝呢{image=image/exch001.png}」"


show char tmi02s2 at left
with dis



voice "Miya_0007"
m "「呵呵，太好了……再来一杯吧」"


show char tri02s2 at right as r
with dis



voice "Risa_0034"
r "「谢谢……味道真好闻♪」"
"我呆呆地看着从茶壶往杯子里注入的红茶。"
"放学以后一边聊天一边享受喝茶时间，果然很享受。"
"就好像要把一整天的疲惫都给吹散了……"


show char tri09s2 at right as r
with dis



voice "Risa_0035"
r "「不对！　我这是在干什么啊，放学以后明明不是来喝茶，而是要教训美夜的」"


show char tmi03s2 at left
with dis



voice "Miya_0008"
m "「听着真讨厌呢」"
voice "Risa_0036"
r "「讨厌也要给我听。你要是再这样逃着课进入暑假的话，我可不允许啊」"


show char tmi01s2 at left
with dis



voice "Miya_0009"
m "「哎……现在才六月呢。现在就说什么暑假，璃纱还真是急性子」"


show char tri08s2 at right as r
with dis



voice "Risa_0037"
r "「因为你非常有可能会这样做啊」"
voice "Risa_0038"
r "「气候潮湿的时候，你说提不起劲来所以逃课。天气晴好的时候，你又说太热了不想上课……我看你八成会这样子做」"
"然后就这样进入暑假。"
"啊，我能预料到……"
voice "Risa_0039"
r "「美夜的逃课之路，我可是看得一清二楚」"


show char tmi02s2 at left
with dis



voice "Miya_0010"
m "「呵呵呵，璃纱你真是的……还真是了解我呢」"


show char tri03s2 at right as r
with dis



voice "Risa_0040"
r "「……诶？」"
"美夜那张漂亮的脸蛋，忽地接近了我。"
voice "Miya_0011"
m "「真不愧是我的恋人呢……亲{image=image/exch001.png}」"


show char tri04s2 at right as r
with dis



voice "Risa_0041"
r "「嗯！？　讨，讨厌……美夜……」"
"美夜的嘴唇和我的嘴唇，一同往常地贴在一起。"


show char tmi11s2 at left
show char tri11s2 at right as r
with dis



voice "Miya_0012"
m "「呼呼呼……璃纱，真可爱……ちゅるる{image=image/exch001.png}」（译注：往后绝大多数拟声词将不予翻译，大家听懂就行）"
voice "Risa_0042"
r "「んあっ……んちゅ……ちゅ{image=image/exch001.png}」"
"我感受着美夜甘甜的气息，仅此而已我的头脑就已经一片空白。"
"然后一脸遗憾地离开了她的嘴唇。"


show char tmi01s2 at left
show char tri05s2 at right as r
with dis



voice "Miya_0013"
m "「璃纱，对不起我逃课了……所以，请原谅我吧」"
voice "Risa_0043"
r "「……唔，真是的……真狡猾啊……ちゅっ{image=image/exch001.png}」"
"我的身上还残留着亲吻的余韵，我渴求着美夜……于是我红着脸，自己亲了上去。"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#**アトリエ・昼
scene bg bg29a
with Dis



#mes on
#system on


show char tmi01s2
with dis



voice "Miya_0014"
m "「璃纱，吃这个吗？」"


show char tmi01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0044"
r "「嗯，我不客气了。这松饼看着真好吃呢，又是在哪儿订的？」"
voice "Miya_0015"
m "「不，这是在玲绪学姐告诉我的店里买的哦」"
voice "Risa_0045"
r "「玲绪学姐她……」"
voice "Miya_0016"
m "「璃纱是喜欢牛奶糖还是巧克力？」"
voice "Risa_0046"
r "「………………」"


show char tmi03s2 at left
with dis



voice "Miya_0017"
m "「……璃纱？」"
voice "Risa_0047"
r "「……啊，不好意思。我选牛奶糖吧」"
"不好，我又发呆了。"


show char tmi01s2 at left
with dis



voice "Miya_0018"
m "「嗯嗯，你在想什么呢，璃纱？　是想着要换大一号罩杯了吗……」"


show char tri09s2 at right as r
with dis



voice "Risa_0048"
r "「我才没有像这种东西，真是的」"
voice "Miya_0019"
m "「要不，我来帮你测量也行哦……就用我的手」"
voice "Risa_0049"
r "「都说不是了」"
voice "Miya_0020"
m "「是吗，真可惜……我明明能把误差给你控制到一厘米以内的」"


show char tri08s2 at right as r
with dis



"虽然现在的文胸确实有些紧了。"
voice "Miya_0021"
m "「那要说璃纱还能考虑别的什么的话……」"


show char tri01s2 at right as r
with dis



voice "Risa_0050"
r "「所以你别胡乱妄想啊。我只是……一下子听到美夜口中说出了玲绪学姐的名字，太高兴了」"


show char tmi03s2 at left
with dis



voice "Miya_0022"
m "「诶……？」"
voice "Risa_0051"
r "「最佳情侣的这些伙伴，已经很平常地成为了美夜的朋友……」"


show char tmi01s2 at left
with dis



voice "Miya_0023"
m "「什么嘛，原来你说这个」"


show char tri02s2 at right as r
with dis



voice "Risa_0052"
r "「对我来说很重要的……美夜能和大家搞好关系，我很高兴」"


show char tmi02s2 at left
with dis



voice "Miya_0024"
m "「呵呵呵，谢谢你了，认真的班长」"


show char tri03s2 at right as r
with dis



voice "Risa_0053"
r "「又，又来……说这种话」"
"不过，我清楚这样说话只是美夜在掩饰自己的羞涩而已。"
"所以我决定不再说下去。"
"虽然美夜还没融入班级，但和最佳情侣的各位都已经搞好关系了。"
"如果还能像去年一样大家来一次合宿……这回美夜也能好好享受了吧……啊！！"
"说起最佳情侣，我又想起刚才那件事了。"


show char tri01s2 at right as r
with dis



voice "Risa_0054"
r "「那个，美夜。我在找美夜的时候，听到几个一年级的学生说了点事……」"


show char tmi01s2 at left
with dis



voice "Miya_0025"
m "「什么事？」"
voice "Risa_0055"
r "「现在要不要竞选『新一年级的最佳情侣』，讨论得热闹着呢。不觉得很有意思吗？」"


show char tmi03s2 at left
with dis



voice "Miya_0026"
m "「……我对这个没兴趣」"


show char tri04s2 at right as r
with dis



voice "Risa_0056"
r "「呃，是吗？　我们可能要有后辈了哦」"
voice "Miya_0027"
m "「所以呢？」"


show char tri03s2 at right as r
with dis



"就算你这么问啊……"
"美夜似乎真的是不感兴趣，没有接下我的话茬来。"


show char tmi01s2 at left
with dis



voice "Miya_0028"
m "「我最感兴趣的是……璃纱，是你哦」"


show char tri01s2 at right as r
with dis



voice "Risa_0057"
r "「美夜……」"
voice "Miya_0029"
m "「难道说璃纱比起我来更关心一年级的学妹吗？」"
voice "Risa_0058"
r "「才没有这种事……对我来说美夜也是最……」"
voice "Miya_0030"
m "「我也是最……什么？」"
"美夜正用娇艳的眼神望着我。"
"我的心脏正砰砰地不停吵闹着。"


show char tri05s2 at right as r
with dis



voice "Risa_0059"
r "「啊，真是的，你明明知道的」"
"面对我通红的脸，美夜继续嗤嗤笑着。"


show char tmi02s2 at left
with dis



voice "Miya_0031"
m "「嗯，我当然知道了。璃纱，你也是对我喜欢得不得了吧」"
voice "Risa_0060"
r "「呜呜呜」"
"这是真的，我没法否定。"
voice "Miya_0032"
m "「璃纱困扰的表情，真的很可爱。让我一边欣赏这个表情，一边吃松饼吧」"
voice "Risa_0061"
r "「………………」"
"她最感兴趣的人是我……美夜能这么说，我是很高兴。"


show char tri01s2 at right as r
with dis



"『新一年级的最佳情侣』我果然还是很在意……"
"虽然像去年那样，自己处于话题的中心会感到十分头疼。"
"但如果不是自己的事了，果然还是很有趣的……别人的恋爱话题还有活动什么的，女孩子毕竟会在意这种事呢。"
"究竟会是什么人当选呢……"
voice "Risa_0062"
r "「是可爱的孩子呢，还是高雅的……」"


show char tmi03s2 at left
with dis



voice "Miya_0033"
m "「……璃纱，吃吗？」"
voice "Risa_0063"
r "「嗯，好的，确实挺好吃的」"
"我一边吃着松饼一边想着要讨论最佳情侣这件事，十分坐立不安。"
"呜呜，好想和别人说啊！！"
"要说谁会喜欢这种话题……"
voice "Risa_0064"
r "「……啊，对了！」"
voice "Miya_0034"
m "「怎么了，璃纱？」"
voice "Risa_0065"
r "「没，没什么……美夜的巧克力松饼我也想尝尝呢，可以试一个吗？」"


show char tmi01s2 at left
with dis



voice "Miya_0035"
m "「嗯，还有很多不用客气」"
"美夜拿出的袋子里，还装着几十个松饼。"


show char tri03s2 at right as r
with dis



voice "Risa_0066"
r "「喂，等等，你这是不是买得太多了？」"
voice "Miya_0036"
m "「是吗？　每个都挺小的，我觉得这很平常吧」"
"明明不小的松饼，瞬间在美夜的嘴里消失了。"
"我看着美夜一大口一大口吃的样子，偷偷地开始写起了邮件。"
"新一年级学生的最佳情侣，要是这个人，就一定有共同话题。"
"如果是同跟我一样，当选了最佳情侣的同级生――织田七海同学说的话，一定会的。"


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
jump S003
