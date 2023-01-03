from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.message.element import Plain
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random
import json
channel = Channel.current()
r = json.load(open("./jsons/rand_sentence.json", "r", encoding='utf-8'))
#版本号随机句子的参数
txt="当前装载版本:1.1.0\n"
@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Bot-version")]
    )
)
async def bot_version(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(txt,"------------\n",Plain(random.choice((r['r'])))
                     )
    )