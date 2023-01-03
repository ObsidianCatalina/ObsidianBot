from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain,Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.message.element import Plain
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import json
channel = Channel.current()
r = json.load(open("./jsons/update_log.json", "r", encoding='utf-8'))
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("更新日志")]
    )
)
async def love(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(''.join(r['update_log'])
)),
    )