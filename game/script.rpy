#########################################
# Defines 功能区，用于定义今后游戏所需要到的各种文件、效果、对象等。
define dis = dissolve
define Dis = Dissolve(1.0)
define r = Character('璃　紗', color="#ffffff")
define m = Character('美　夜', color="#ffffff")
define n = Character('七　海', color="#fff")
define y = Character('優　菜', color="#fff")
define re = Character('玲　緒',color="#fff")
define ma = Character('麻　衣', color="#fff")
define s = Character('沙　雪', color="#fff")
define rk = Character('六　夏', color="#fff")
define k = Character('楓', color="#fff")
define sr = Character('紗　良', color="#fff")
define e = Character('エリス', color="#fff")
define sk = Character('雫', color="#fff")
define rn = Character('瑠　奈', color="#fff")
define t = Character('貴　子', color="#fff")
define ren = Character('麗　奈', color="#fff")
define mobA = Character('女子A', color="#ffffff")
define mobB = Character('女子B', color="#ffffff")
define mobC = Character('女子C', color="#ffffff")
define mobD = Character('女子D', color="#ffffff")
define mobE = Character('女子E', color="#ffffff")
define j = Character('教　師', color="#fff")
define x = Character('？？？', color="#ffffff")
image black = "#000"
image white = "#fff"
#########################################

# 定义原krkr2脚本中lrotate和rrotate对应的转场效果。因为Ren'py本身并不带有这样的转场，
# 所以必须使用转场特效的mask文件配合ImageDissolve命令实现。
init:
    $ lrotate = ImageDissolve("data/mask/mask_rotateright.png", 2.0, 20)
    $ rrotate = ImageDissolve("data/mask/mask_rotateleft.png", 2.0, 20)
    define lr = lrotate
    define rr = rrotate

# 导入游戏OP视频，在进入程序时自动播放。
label splashscreen:

    $ renpy.movie_cutscene('data/op.avi')
    return

# 为方便移植，此脚本除Defines等非脚本功能以外将不再使用，此处直接使用jump命令跳过。
label start:
jump S001