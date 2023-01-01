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
        MessageChain(f"当前装载版本:1.04b")
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
        MessageChain(f"菜单（开发中）\n1，爱你:会回复“我也爱你”\n2，简介:作者&这个机器人的简介")
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
