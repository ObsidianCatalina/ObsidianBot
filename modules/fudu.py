from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def fudu(app: Ariadne, group: Group, message: MessageChain):
    if message.display in [
        "6", "9", "c", "tcl", "666", "ccc"
    ]:
        await app.send_message(
            group,
            MessageChain(message.display),
        )
