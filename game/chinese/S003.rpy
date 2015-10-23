# 七海的音频文件名没有下划线！
# 本章第一次出现选择肢
# 由于Ren'py使用Python语言编写，对多平台通用性很强，
# 因此它对空格和文件名大小写要求也非常严格。
# 编写选择肢时，menu命令的格式如下：
# menu:
#     （空4格）"（选择肢1内容）":
#      （空5格）jump choice1
#     （空4格）"（选择肢2内容）":
#      （空5格）jump choice2
# label choice1:
# 内容
# jump choice1_done
###############################
# 如上，其中choice1是选择后跳到的脚本分支的名称，可随意命名，choice1_done是选择肢分支剧情结束后
# 跳到的共通文本，也可随意命名。
# 
# 同时，S003也开始出现三个立绘同屏的场景。
# 在这里再次强调定义方法：最左的用show char xx at sleft as l，中间的保持show char xx，最右用show char xx at sright as sr
# 同时，若之前存在立绘，则必须要用hide命令先隐藏立绘后再进行显示，否则会出现新旧立绘层叠的问题。

#「１年生会あらため、２年生会」

label S003:
$ save_name = "◇一年级同学会，升到二年级"


#**並木道・昼
scene bg bg18a
with Dis



#mes on
#system on


#♂MP02
play music "sound/BGM02.ogg"


show char tna01s2
with dis



voice "Nanami0000"
n "「璃纱同学，久等了～」"


show char tna01s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0067"
r "「那我们就出发吧」"
voice "Nanami0001"
n "「一直以来的咖啡厅可以吧」"
voice "Risa_0068"
r "「嗯」"
"给七海同学发了邮件的第二天。"
"我们及早地汇合，一起去喝了茶。"
"七海同学也对『新一年级学生的最佳情侣』很感兴趣，还说有很多想和我聊的。"
voice "Risa_0069"
r "「嗯……话说今天纱良同学呢？」"
voice "Nanami0002"
n "「我虽然也邀请她了，但是她回了邮件说有工作来不了……她可是很想来的呢」"
voice "Risa_0070"
r "「虽然很可惜……但这也说明纱良很有人气啊」"
voice "Nanami0003"
n "「所以今天就我们两个人开一年级同学会了」"
voice "Risa_0071"
r "「嗯，不对哦，七海同学」"


show char tna03s2 at left
with dis



voice "Nanami0004"
n "「咦……有什么不对的？」"
voice "Risa_0072"
r "「我们已经是二年级了吧……所以现在开始，就是二年级同学会了哦」"


show char tna05s2 at left
with dis



voice "Nanami0005"
n "「诶，说的也是啊」"
"当选最佳情侣的我和织田七海同学，以及北嶋纱良同学。"
"我们三个人去年结成了『一年级同学会』。"
"名字虽然是这么叫，其实并没有什么了不起的，也就是聚在咖啡馆里聊聊天而已。"
"因为大家都有恋人，所以可以愉快而且放开来商谈和闲聊那些恋爱的话题。"
"我们在有什么事的时候，经常会聚在一起。"
"但是今年，纱良同学就经常不能露面，变成只有我和七海同学两个人了。"
"虽然纱良本身就有着模特这个工作，已经很忙了。"
"自从和她的恋人枫学姐合作以后，工作变得比以前更忙。"
"似乎是因为模特和拍广告还有唱歌的工作，让她们抽不出时间来……"


show char tna01s2 at left
with dis



voice "Nanami0006"
n "「话说回来，璃纱同学你知道吗？　据说纱良同学都已经收到拍电影的邀请了」"


show char tri04s2 at right as r
with dis



voice "Risa_0073"
r "「嘿～，这样啊，真厉害」"
voice "Nanami0007"
n "「以后要越来越忙了呢……纱良同学」"


show char tri01s2 at right as r
with dis



voice "Risa_0074"
r "「嗯，是啊……」"
"纱良同学一讲到自己的恋人枫学姐，就越来越停不下来。"
"这个同学会中担任暖场人的纱良同学一不在，总觉得少了些什么。"
"七海同学似乎也是这么觉得的……我们俩都有些沉默。"


#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis


scene bg bg17a
with dis


#mes on
#system on


"东想西想着，不知不觉间就已经到咖啡厅门口了。"


show char tna02s2
with dis


voice "Nanami0008"
n "「今天推荐的蛋糕是什么呢？」"
"就像要冲破这份寂寞，七海兴趣盎然地望了望店面的菜单。"
"我也学着她，指着菜单笑着说这个很好吃啊。"


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


show char tri01s2
with dis



voice "Risa_0075"
r "「那么……现在开始二年级同学会」"


show char tna02s2 at left
show char tri01s2 at right as r
with dis



voice "Nanami0009"
n "「呼呼，干杯♪」"


show char tri02s2 at right as r
with dis



voice "Risa_0076"
r "「干杯♪」"
"我们踮起茶杯杯端，互相干杯。"
"虽然不是在喝酒，但这已经成为我们聚会的『老项目』了。"


show char tna01s2 at left
show char tri01s2 at right as r
with dis



voice "Nanami0010"
n "「虽然都差不多到要喝冰饮的时候了……」"
voice "Risa_0077"
r "「还是会不自觉地点热的呢～」"


show char tna03s2 at left
with dis



voice "Nanami0011"
n "「然后每次都会点蛋糕……明明不得不减肥的」"


show char tri03s2 at right as r
with dis



voice "Risa_0078"
r "「我也是啊……明明这世上还有不用减肥的人」"
voice "Nanami0012"
n "「就是就是，明明吃了那么多」"
voice "Risa_0079"
r "「为什么就是不胖呢」"
voice "Nanami0013"
n "「对吧」"
voice "Risa_0080"
r "「对吧」"


show char tna02s2 at left
show char tri02s2 at right as r
with dis



"两个人异口同声，然后都笑了出来。"
"我们俩肯定是都在想着自己怎么吃都不会胖的恋人。"
voice "Nanami0014"
n "「呵呵，璃纱比以前能更自然地聊到美夜的话题了呢」"


show char tri04s2 at right as r
with dis



voice "Risa_0081"
r "「诶，是吗……」"


show char tna01s2 at left
with dis



voice "Nanami0015"
n "「嗯。以前都是一脸羞涩，不肯说出口的」"


show char tri05s2 at right as r
with dis



voice "Risa_0082"
r "「也，也许……是吧……」"
"她这样一说，也许还真没错。"
"但要说害羞，到现在也是一样的。"
"我趁着这个话题越说越大之前，赶紧转换掉。"


show char tri01s2 at right as r
with dis



voice "Risa_0083"
r "「关于一年级的最佳情侣……七海同学，你知道什么吗？」"
"刚说完，七海同学就如『你这问题问得好』了一样，滔滔不绝了起来。"


show char tna02s2 at left
with dis



voice "Nanami0016"
n "「当然了。一年级同学之间甚至都在说已经决定是那两人了」"
voice "Risa_0084"
r "「嗬～……这么有名的吗？」"


show char tna01s2 at left
with dis



voice "Nanami0017"
n "「璃纱同学，你一点都不知道吗？」"


show char tri03s2 at right as r
with dis



voice "Risa_0085"
r "「嗯，其实呢……就连一年级学生正在热烈讨论这个，也是昨天刚知道的」"
voice "Nanami0018"
n "「是吗。那两人似乎都已经被高年级学生知道了」"
"是吗，还真厉害啊。"
"我还是跟往常一样对这种话题比较陌生啊。"
"自己总是在自己喜好的东西里陷得太深，都无暇关注四周了，虽然这不是在说美夜。"
"我的眼里只有美夜……之类的。"
voice "Risa_0086"
r "「……我也不太能说出美夜的事吧」"
voice "Nanami0019"
n "「嗯，怎么了？」"


show char tri01s2 at right as r
with dis



voice "Risa_0087"
r "「没，没事。然后，刚才说的那两人是怎样的？」"
voice "Nanami0020"
n "「咳咳，那就由我来解说吧。一年级最佳情侣候选人其中之一就是『白河沙雪』同学」"
voice "Nanami0021"
n "「她是继承了武士家族血统的名媛，据说是继丽奈老师之后又一被称为『究极淑女』的人」"
voice "Risa_0088"
r "「听，听起来好厉害……」"
"丽奈老师是之前到春季为止担任我班主任、米卡女校的毕业学姐（OG）。"
"似乎以前甚至能被称作『究极淑女』，她就是这么个厉害的角色。"
"与她的名字相呼应，老师本人也是非常的漂亮和魅力四射，在同学之间非常有人气。"
"那人竟然能和这样的丽奈老师相媲美……"
voice "Nanami0022"
n "「她是更相貌端庄，善良，什么都会的完美超人。听说她的外号是取自名字的一部分，叫『白雪公主』呢」"
voice "Risa_0089"
r "「白雪公主，啊……还真是个可爱的名字呢」"
"这种可爱的外号，我也想有一个。"
voice "Nanami0023"
n "「而且姿容和性格也非常像个大小姐哦」"
"大小姐一般的性格……那是怎样的呢。"
"我越来越感兴趣了。"
voice "Nanami0024"
n "「然后呢，还是一年级呢就在『环境整备委员会』中大放异彩了」"
voice "Risa_0090"
r "「是这样啊……」"
"难怪七海同学会这样清楚。"
"和她同样是环境整备委员啊。"
voice "Nanami0025"
n "「真的很优秀哦……非常优秀」"
"听着这些话，我回想起之前在校内听到的七海同学的牢骚……"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（回想シーン）

#**新校舎廊下・昼
scene bg bg05a
with rr


#mes on
#system on


show char tna04s2
with dis



voice "Nanami0026"
n "「总之，沙雪同学就是厉害……太厉害了啊！」"


show char tna04s2 at left
show char tri03s2 at right as r
with dis



voice "Risa_0091"
r "「沙雪同学？」"


show char tna01s2 at left
with dis



voice "Nanami0027"
n "「最近成为环境整备委员的，一年级的同学啊」"


show char tri01s2 at right as r
with dis



voice "Risa_0092"
r "「是七海同学的后辈啊。但是能成为环境整备委员的人，不都很厉害的吗」"
voice "Nanami0028"
n "「完全不在一个水平上。沙雪同学可是被称作『优菜学姐二世』或者『丽奈老师二世』之类的啊」"
"说道优菜学姐和米卡女校的毕业学姐丽奈老师，给人的印象就是淑女中的淑女。"
"如果能和那两位相提并论的话……"
voice "Risa_0093"
r "「所以，她非常的优秀吧……」"


show char tna03s2 at left
with dis



voice "Nanami0029"
n "「就是啊！　上边下边都有这么优秀的人在，我很难办的～」"
voice "Risa_0094"
r "「还真是多灾多难呢，七海同学」"
voice "Nanami0030"
n "「你懂我的吧？」"


show char tri03s2 at right as r
with dis



voice "Risa_0095"
r "「嗯嗯，我也是啊……」"


#**暗転
#mes off
#mes clear
#system off
scene black
#allClear:
#lastBG:
#scene black
with Dis



#（回想シーン終了）
#mes on
#system on


"那之后，我也发牢骚说道自己跟不上美夜那个天才的思想呢。"
"因为那时候只听到了一遍名字，现在都忘了。"
"让七海同学叹气的原因，是那位沙雪同学啊……"


#**カフェ・昼
scene bg bg36a
with lr


"今天也一直在说着沙雪同学的七海同学，音调一点点地降了下来。"


show char tna03s2
with dis



voice "Nanami0031"
n "「我明明还在接受作为优菜学姐的继任者的斯巴达教育……沙雪同学竟然比我还要优秀啊」"


show char tna03s2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0096"
r "「七海同学……」"
voice "Nanami0032"
n "「说不定沙雪同学更适合做优菜学姐的继任者……」"
"她的声音越来越小，似乎都有些厌恶自己了。"
"这样的朋友，我也想尽可能去鼓励。"
voice "Risa_0097"
r "「但是七海同学不也是从一年级就开始当选环境整备委员了吗」"
voice "Nanami0033"
n "「那是姐姐……不，优菜学姐在关照我而已」"
voice "Risa_0098"
r "「那之后，你不也是好好完成了毕业相册整理委员的工作吗。七海同学是很棒的继任者啊」"


show char tna01s2 at left
with dis



voice "Nanami0034"
n "「璃纱同学……谢谢你，有璃纱同学你这么优秀的人鼓励我，总算有勇气了」"
"太好了，她看上去总算有点精神了。"
voice "Nanami0035"
n "「啊，我还得再加一把劲呢，就像璃纱同学一样」"


show char tri03s2 at right as r
with dis



voice "Risa_0099"
r "「我也不是那种自信满满的人啦」"


show char tna04s2 at left
with dis



voice "Nanami0036"
n "「诶……是吗？」"


show char tri01s2 at right as r
with dis



voice "Risa_0100"
r "「是啊。所以为了增加自信，也要经常努力呢」"


show char tna01s2 at left
with dis



voice "Nanami0037"
n "「诶……就是这种地方，璃纱真的是和我不一样啊」"
voice "Risa_0101"
r "「有吗？」"
"七海同学边看着我笑，边继续说。"


show char tna02s2 at left
with dis



voice "Nanami0038"
n "「然后，关于另一个人……那位沙雪同学的对象呢，就是『篠崎六夏』同学哦」"


show char tri03s2 at right as r
with dis



voice "Risa_0102"
r "「………………六夏？？」"


#★★★選択肢　ここから
#++選択肢（１）
#１．『聞いた事のない……名前ね』×
#２．『どこかで……聞いたような……』○
menu:
 "这名字好像……没听说过":
  jump select01_1
 "这名字……好像在哪听过……":
  jump select01_2



label select01_1:
#１．『聞いた事のない名前ね……』


voice "Risa_0103"
r "「这名字好像……没听说过」"
"脑海中闪过了什么念头。"
"但果然，还是没听说这个名字……"
"总之，现在还是要认真听七海同学说话。"


jump select01_end


label select01_2:
#２．『どこかで……聞いたような……』○


"听到这个名字的一刹那，脑海中念头一闪。"
voice "Risa_0104"
r "「嗯，感觉在哪听说过……」"
"………………但是不行，果然还是想不起来。"


show char tna01s2 at left
with dis



voice "Nanami0039"
n "「璃纱同学，难道你认识她吗？」"
voice "Risa_0105"
r "「嗯，感觉认识又不认识的……」"
voice "Nanami0040"
n "「因为她很有名啦，说不定在哪听说过也不奇怪呢」"
voice "Risa_0106"
r "「是啊，说不准呢」"
"但是，还是有点在意。"
"我想回忆起来……但是，还是得听七海同学说话。"


#set f1 f1+1


#++選択肢終了
#★★★選択肢　ここまで
label select01_end:


voice "Nanami0041"
n "「听说六夏同学是从外校过来的转学生，成绩是中上水平哦」"


show char tri01s2 at right as r
with dis



voice "Risa_0107"
r "「是吗……挺普通的嘛。那，是外貌方面很出众之类的？」"
voice "Nanami0042"
n "「厉害的倒不是这方面，而是体能。长得高，体育又好，据说在田径赛场上拥有非常厉害的纪录呢」"
voice "Risa_0108"
r "「嗬……这位单听你说，也觉得很厉害呢」"
voice "Nanami0043"
n "「她还跟枫学姐有共同点，是个有王子形象的人呢。所以，外号就叫『白雪骑士』」"


show char tri04s2 at right as r
with dis



voice "Risa_0109"
r "「白雪……骑士！？」"
voice "Nanami0044"
n "「很有意思吧？　因为是保护白雪公主的骑士，就这么称呼了」"
"公主，接着是骑士啊……感觉都是充满浪漫气息的词语。"
"脑海中浮现了我一直在家读的言情小说的一个场景。"
"骑士果然会对公主说『请让我守护你一生』之类的吧。"


show char tri02s2 at right as r
with dis



voice "Risa_0110"
r "「……呵呵，这种关系还真好{image=image/exch001.png}」"


show char tna03s2 at left
with dis



voice "Nanami0045"
n "「璃纱同学，你怎么了？　笑呵呵的」"


show char tri05s2 at right as r
with dis



voice "Risa_0111"
r "「啊！　没没没，没什么哦……」"
"真是的，太羞人了……在七海同学的面前就沉醉于妄想之中。"


show char tri01s2 at right as r
with dis



voice "Risa_0112a"
r "「咳咳……但是他们两位都很厉害呢」"


show char tna01s2 at left
with dis



voice "Nanami0046"
n "「嗯。要是那两人，也加入我们最佳情侣……会是什么样子呢」"
voice "Risa_0113"
r "「谁知道呢……至少对我来说，总算是有晚辈了」"


show char tna02s2 at left
with dis



voice "Nanami0047"
n "「呵呵，说的没错」"
"因为现在只是一年级在热烈讨论这个话题，她们究竟能不能加入我们还是个未知数。"
"但要说不感兴趣，那是骗人的。"
"还尽可能想在近期亲自和她们见面……"


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


"在那之后，我们俩继续以交换情报为理由交谈着。"
"太阳开始西斜的时候，我们从店里出来了。"


#**繁華街・昼
scene bg bg17a
with Dis



"结完账，刚刚走出店门口。"
"就看见一张喘着气的熟悉的脸孔。"


show char tsa03f2
with dis



voice "Sara_0000"
sr "「はぁ、はぁ、久等了～……咦，难道你们已经要走了吗？」"


show char tsa03f2 at left
show char tri01s2 at right as r
with dis



voice "Risa_0114"
r "「纱良同学……」"

hide char tsa03f2 at left
hide char tri01s2 at right as r
show char tna03s2 at sleft as l
show char tsa03f2
show char tri01s2 at sright as sr
with dis



voice "Nanami0048"
n "「今天你不是有工作的吗？」"


show char tsa02f2
with dis



voice "Sara_0001"
sr "「嗯。纱良翘班过来的啊。那我们来开同学会吧♪」"
voice "Nanami0049"
n "「那个……同学会刚刚才结束的……」"


show char tsa04f2
with dis



voice "Sara_0002"
sr "「诶诶，怎么这样～」"


show char tna02s2 at sleft as l
show char tri02s2 at sright as sr
with dis



voice "Risa_0115"
r "「ふふふっ」"
voice "Nanami0050"
n "「ふふふっ」"


show char tsa03f2
with dis



voice "Sara_0003"
sr "「等下等下，你们两个笑什么呢？」"
voice "Risa_0116"
r "「因为啊……んふ、ふふふっ」"
"我和七海同学忍俊不禁。"
"纱良同学自从成了偶像，因为很忙，渐渐和我们疏远了……虽然是这么想的。"
"但她还是这样一如既往地和我们在一起啊。"
"担心什么的，都是白费。"


show char tna01s2 at sleft as l
with dis



voice "Nanami0051"
n "「纱良同学，你马上就要回去了？」"


show char tsa01f2
with dis



voice "Sara_0004"
sr "「嗯……我只是空出了一段时间而已」"
voice "Nanami0052"
n "「那就让我送你到车站吧。还有好多话要和你说呢」"


show char tsa02f2
with dis



voice "Sara_0005"
sr "「七海酱{image=image/exch001.png}　好温柔♪」"


show char tri01s2 at sright as sr
with dis



voice "Risa_0117"
r "「我也陪你们到半路吧」"
voice "Sara_0006"
sr "「也谢谢璃纱酱了♪　那我们就边去车站边开同学会吧」"
"虽然这样有些绕远路了。"
"但是毕竟三个人久违地开一次二年级同学会。"
"我们就这样欢声笑语地一起走去车站。"
"路上一跟纱良同学说起一年级新最佳情侣的事情……"


show char tsa09f2
with dis



voice "Sara_0007"
sr "「不行的啊，米卡女校里才没有比枫酱更厉害的王子角色呢」"
"纱良同学如此断言道。"
"我试着再次回忆这个似乎听说过的『白雪骑士』的名字……"
"但是无论如何都想不起来。"


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
jump S004



