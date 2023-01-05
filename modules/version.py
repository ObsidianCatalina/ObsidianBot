import json

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import BotCoreManager
channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux芝士 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('linuxv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("被戳 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('getupv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("菜单 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('menuv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("答辩 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('shit.py')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("突发恶疾 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('esuv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("更新日志 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain([BotCoreManager.ver('updatev')]))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("复读 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('fuduv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("特别鸣谢 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('thankslistv')))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("获取源代码 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('sourcecodev')))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("来份涩图 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver(BotCoreManager.ver('setuv'))))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("main -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('mainv')))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("version -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver('versionv')))
    )

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("BCM -v")]
    )
)
async def shit(app: Ariadne, group: Group, event: GroupMessage):
    if event.sender.id == b:
        await app.send_message(
            group,
            MessageChain(Plain(BotCoreManager.ver('bcmv')))
        )
