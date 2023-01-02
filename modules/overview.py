from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.message.element import Plain
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random
channel = Channel.current()
r = [
"三十功名尘与土，八千里路云和月   ——岳飞《满江红》",
"莫等闲，白了少年头，空悲切   ——岳飞《满江红》",
"哪里有压迫，哪里就有反抗！  ——毛泽东",
"北国风光，千里冰封，万里雪飘   ——毛泽东《沁园春·雪》",
"自由就是人权在所有地方高于一切   ——罗斯福《论四大自由》",
"人需要理想，但是需要人的符合自然的理想，而不是超自然的理想  ——列宁",
"要立志做大事，不要立志当大官  ——孙中山",
"再长的路，一步步也能走完，再短的路，不迈开双脚也无法到达  ——孙中山",
"你们不要拿我当古董，我是来工作的，你们要拿我当一挺机枪来使用  ——白求恩",
"双兔傍地走，安能辨我是雄雌？  ——《木兰辞》",
"及时当勉励，岁月不待人  ——陶渊明",
"采菊东篱下，悠然见南山  ——陶渊明《饮酒（其五）》",
"得道多助，失道寡助  ——孟子",
"不义富且贵，于我如浮云  ——孔子",
"人生自古谁无死，留取丹心照汗青  ——文天祥《过零丁洋》",
"学而不思则罔，思而不学则殆  ——《论语·为政》"
]
txt="当前装载版本:1.06b\n"
@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Bot-version")]
    )
)
async def bot_version(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(txt,"------------\n",Plain(random.choice(r))
                     )
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("简介")]
    )
)
async def brief_introduction(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"作者简介:一个沙批\n"
            f"机器人简介:\n"
            f"名字:Type-Release10.3\n"
            f"来源:出自她的沙批开发者ObsidianCatalina\n"
            f"功能:不知道\n"
            f"配料表:答辩,依托史"),
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("菜单")]
    )
)
async def menu(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"菜单（开发中）\n1，爱你：会回复“我也爱你”\n2，简介：作者&这个机器人的简介\n3，linux知识：随机发送一条有关Unix/Linux系统的知识\n4，更新日志：无描述\n5，特别鸣谢：无描述\n6，获取源代码：了解如何获取ObsidianBot的源码")
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("爱你")]
    )
)
async def love(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(f"我也爱你"),
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("更新日志")]
    )
)
async def love(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(f"1.04b更新日志:\n"
                     f"更新时间:2023/1/1\n"
                     f"更新内容:\n"
                     f"更新了“linux知识”命令\n"
                     f"移除了Him\n"
                     f"1.05b更新日志:\n"
                     f"更新时间:2023/1/1\n"
                     f"更新内容:\n"
                     f"紧急修复机器人会复读其他机器人的bug\n"
                     f"移除了Him\n",
                     f"1.06b更新日志:\n",
                     f"更新内容:\n",
                     f"Bot-version增加了随机名人名言\n",
                     f"增加了特别鸣谢\n",
                     f"增加了源代码拉取",),
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("特别鸣谢")]
    )
)
async def love(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(f"感谢他们为制作机器人提供的帮助\n"
                     f"Hantools:\n"
                     f"Github主页:https://github.com/daizihan233\n"
                     f"Windows2000:\n"
                     f"Github主页:https://github.com/Abjust\n"
                     f"我（ObsidianCatalina）:\n"
                     f"Github主页:https://github.com/ObsidianCatalina"
                     ),
    )
