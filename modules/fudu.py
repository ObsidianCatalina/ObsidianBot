from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def fudu(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "6":
         await app.send_message(
            group,
            MessageChain(f"6"),
         )
    if message.display == "9":
         await app.send_message(
            group,
            MessageChain(f"9"),
         )
    if message.display == "c":
         await app.send_message(
            group,
            MessageChain(f"c"),
         )
    if message.display == "tcl":
         await app.send_message(
            group,
            MessageChain(f"tcl"),
         )
    if message.display == "666":
         await app.send_message(
            group,
            MessageChain(f"666"),
         )
    if message.display == "ccc":
         await app.send_message(
            group,
            MessageChain(f"ccc"),
             )     
             