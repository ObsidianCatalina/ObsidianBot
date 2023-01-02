from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain,At,Plain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random

channel = Channel.current()

f = [
        " Hantools我爱死你啦!!!❤",  
    ]
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("突发恶疾")]
    )
)
async def esu(app: Ariadne, group: Group, event: GroupMessage):
    knowledge = [
        " 爱你呦~❤",
        " 亲爱的快超死我呜呜呜~❤",
        " aaaaaaaaaaaaaaaaaaa~❤",
        " 最喜欢你了❤~"
    ]
    await app.send_message(
        group,
        MessageChain(At(event.sender.id), Plain(random.choice(knowledge)))
    )
async def esu(app: Ariadne, group: Group, event: GroupMessage):
 if event.sender.id == 183713750:
    await app.send_message(
        group,
         MessageChain(At(event.sender.id), Plain(random.choice(f)))
    )

