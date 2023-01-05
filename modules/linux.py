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
su = BotCoreManager.su('su')
knowledge = BotCoreManager.linux_knowledge('r')


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[]
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("linux芝士")):
    if not message:  # 因为如果没有参数则 message 为空，可以直接取反判断是否有值
        await app.send_message(
            group,
            MessageChain(random.choice(knowledge))
        )
    elif str(message).endswith('-l'):  # 防止你把空格忘了（？
        if event.sender.id == su:
            await app.send_message(
                group,
                MessageChain(
                    [
                        Plain(
                            "\n".join(
                                [
                                    f"{x + 1}、{knowledge[x]}" for x in range(len(knowledge))
                                ]
                            )
                        )
                    ]
                )
            )
