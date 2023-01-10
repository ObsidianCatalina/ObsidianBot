import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain, At, Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import BotCoreManager

channel = Channel.current()
a=BotCoreManager.bot_global('bot_admin_id')

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("突发恶疾")]
    )
)
# 一个Hantols特供的恶疾（）
async def esu(app: Ariadne, group: Group, event: GroupMessage):
    if event.sender.id == a:
          await app.send_message(
            group,
            MessageChain(At(event.sender.id), Plain(random.choice(BotCoreManager.eji('private'))))
        )
    else:
        await app.send_message(
            group,
            MessageChain(At(event.sender.id), Plain(random.choice(BotCoreManager.eji('public'))))
        )
