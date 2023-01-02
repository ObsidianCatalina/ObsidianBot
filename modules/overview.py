from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


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
        decorators=[MatchContent("Bot-version")]
    )
)
async def bot_version(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(f"当前装载版本:1.05b")
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
        MessageChain(f"菜单（开发中）\n1，爱你：会回复“我也爱你”\n2，简介：作者&这个机器人的简介\n3，linux知识：随机发送一条有关Unix/Linux系统的知识\n4，更新日志：无描述")
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
                     f"移除了Him"),
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
                     f"Github主页:https//:github.com/Abjust"
                     f"我（ObsidianCatalina）:"
                     f"Github主页:https//github.com/ObsidianCatalina"
                     ),
    )
    

