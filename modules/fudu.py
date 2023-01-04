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
async def fudu(app: Ariadne, group: Group, message: MessageChain, event: GroupMessage):
    # 不被此复读的人（机器人）的QQ号
    if event.sender.id not in [2810482259, 2265453790, 3594648576, 748029973, 3131016892, 3573523379, 1707416843]:
        if message.display in ["6", "9", "c", "tcl", "666", "ccc", "？", "?", "sb"]:
            await app.send_message(
                group,
                MessageChain(message.display),
            )
