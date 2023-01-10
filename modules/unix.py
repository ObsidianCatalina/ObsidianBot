import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import BotCoreManager

channel = Channel.current()
# 读取json
su = BotCoreManager.bot_global('su_id')
linux_knowledge = BotCoreManager.linux_knowledge('linux_knowledge')


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[]
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("unix芝士")):
    if  message:  # 因为如果没有参数则 message 为空，可以直接取反判断是否有值
        await app.send_message(
            group,
            MessageChain(random.choice(linux_knowledge))
        )
