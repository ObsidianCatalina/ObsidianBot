from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.element import  Image
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def overview(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "杏并":
         await app.send_message(
            group,
           MessageChain(f"我杏并犯了，拉我去炼人炉！")
         )