from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import DetectSuffix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import BotCoreManager

channel = Channel.current()

# 如果你写出了这种代码建议remake  —— HanTools
# 面对这坨答辩，HanTools给出的惩罚事…… https://graiax.cn/guide/message_parser/base_parser.html


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def version(app: Ariadne, group: Group, message: MessageChain = DetectSuffix(" -v")):
    await app.send_message(
        group,
        MessageChain(Plain(BotCoreManager.ver(str(message))))
    )




