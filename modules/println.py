from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import MatchContent, DetectSuffix
import BotCoreManager

channel = Channel.current()
su = BotCoreManager.bot_global('su_id')
disable = 1



@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("enable_println -g")]
    )
)
async def println(app: Ariadne, group: Group, event: GroupMessage):
    
    if event.sender.id  == su:
        global disable
        disable=0
        await app.send_message(group,MessageChain(At(event.sender.id)," 已全局启用println模块"),
    
    )    
    else:
         await app.send_message(group,MessageChain(At(event.sender.id)," 抱歉亲爱的，你的权限不足")),                                            
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("disable_println -g")]
    )
)
async def println(app: Ariadne, group: Group, event: GroupMessage):
    
    if event.sender.id  == su:
        global disable
        disable=1
        await app.send_message(group,MessageChain(At(event.sender.id)," 已全局禁用println模块"),
    
    )
    else:
         await app.send_message(group,MessageChain(At(event.sender.id)," 抱歉亲爱的，你的权限不足")),
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def println(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain):
    global disable
    if disable == 1:
        
     if message.display.startswith("println "):
        await app.send_message(
            group,
           MessageChain(f"非常抱歉，此模块当前已被禁用")
        )
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def println(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain):
    global disable
    if disable == 0:
     if message.display.startswith("println "):
        await app.send_message(
            group,
            MessageChain(f"{message.display[8:]}"),
        )