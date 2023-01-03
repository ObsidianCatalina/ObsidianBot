from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain,Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("特别鸣谢")]
    )
)
async def love(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(f"感谢他们为制作机器人提供的帮助\n"
                     f"Hantools:\n"
                     f"Github主页:https://github.com/daizihan233\n"
                     f"Windows2000:\n"
                     f"Github主页:https://github.com/Abjust\n"
                     f"我（ObsidianCatalina）:\n"
                     f"Github主页:https://github.com/ObsidianCatalina"
                     ),
    )
