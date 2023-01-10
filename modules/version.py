from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain,At
from graia.ariadne.message.parser.base import DetectSuffix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import BotCoreManager

channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def version(app: Ariadne, group: Group,event: GroupMessage,message: MessageChain = DetectSuffix(" -v")):
    await app.send_message(
        group,
        MessageChain(At(event.sender.id),Plain(BotCoreManager.ver(str(message))))
    )




