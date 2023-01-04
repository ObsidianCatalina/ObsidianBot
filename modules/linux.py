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

channel = Channel.current()
# 读取json
r = json.load(open("./jsons/su.json", "r", encoding='utf-8'))
knowledge = json.load(open("./jsons/linux_knowledge.json", "r", encoding='utf-8'))


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux芝士")]
    )
)
async def linux(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(random.choice((knowledge['r'])))
    )


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux芝士 -l")]
    )
)
async def linux_list(app: Ariadne, group: Group, event: GroupMessage):
    # 使用json
    if event.sender.id == r[0]['su']:
        await app.send_message(
            group,
            MessageChain(
                [
                    Plain(
                        "\n".join(
                            [
                                f"{x + 1}、{knowledge['r'][x]}" for x in range(len(knowledge['r']))
                            ]
                        )
                    )
                ]
            )
        )
