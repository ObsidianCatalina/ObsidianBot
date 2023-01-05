from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random
import json
import BotCoreManager
channel = Channel.current()
# 读取json
su = BotCoreManager.su('su')
knowledge = BotCoreManager.linux_knowledge('r')

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux芝士")]
    )
)
async def linux(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(random.choice((knowledge)))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        
        decorators=[MatchContent("linux芝士 -l")]
    )
)
async def linux_list(app: Ariadne, group: Group, event: GroupMessage):
    # 使用json
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