from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("获取源代码")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"你可以在https://github.com/ObsidianCatalina/ObsidianBot中手动下载\n"
            f"也可以使用git clone https://github.com/ObsidianCatalina/ObsidianBot.git获取源码")
    )
