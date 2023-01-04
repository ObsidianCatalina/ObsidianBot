from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
import random
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import json

channel = Channel.current()
shit = json.load(open("./jsons/shit.json", "r", encoding='utf-8'))


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("答辩")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(random.choice(shit['shit']))
    )
