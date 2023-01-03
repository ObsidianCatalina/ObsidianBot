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
r = json.load(open("./jsons/version.json", "r", encoding='utf-8'))
b = json.load(open("./jsons/su.json", "r", encoding='utf-8'))
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux芝士 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['linuxv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("被戳 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['getupv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("菜单 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['menuv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("答辩 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['shit.py']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("突发恶疾 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['esuv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("更新日志 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['updatev']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("复读 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['fuduv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("特别鸣谢 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['thankslistv']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("获取源代码 -v")]
    )
)
async def shit(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(Plain(r[0]['sourcecodev']))
    )
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("ver -l")]
    )
)
async def shit(app: Ariadne, group: Group,event:GroupMessage):
  if event.sender.id == b[0]['su']:
    await app.send_message(
        group,
        MessageChain(f"linux芝士:",{r[0]['linuxv']},"\n",
                     f"被戳:",{r[0]['getupv']},"\n",
                     f"菜单:",{r[0]['menuv']},"\n",
                     f"更新日志:",{r[0]['updatev']},"\n",
                     f"获取源代码:",{r[0]['sourcecodev']},"\n",
                     f"特别鸣谢:",{r[0]['thankslistv']},"\n",
                     f"突发恶疾:",{r[0]['esuv']},"\n", 
                     f"复读:",{r[0]['fuduv']},"\n",
                     f"答辩:",{r[0]['shit.py']},
  
        )
    )         