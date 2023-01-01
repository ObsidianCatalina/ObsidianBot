from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def overview(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "简介":
         await app.send_message(
            group,
            MessageChain(f"作者简介:一个沙批\n机器人简介:\n名字:Type-Release10.3\n来源:出自她的沙批开发者ObsidianCatalina\n功能:不知道\n配料表:答辩,依托史" ),
         )
    if message.display=="Bot-version":
         await app.send_message(
         group,
         MessageChain(f"当前装载版本:1.03b")
         )