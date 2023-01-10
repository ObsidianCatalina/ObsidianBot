import random

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
r = BotCoreManager.rand_sentence('rand_sentence')
# 版本号随机句子的参数
txt = "当前装载版本:1.4.2\n质量更新版本:0.9.0ab\n紧急更新补丁版本:Strict_0.4.0\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Bot-version")]
    )
)
async def bot_version(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain([txt, "------------\n", Plain(random.choice(r))])
    )
