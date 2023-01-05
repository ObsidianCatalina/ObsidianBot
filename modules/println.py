from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import MatchContent
import BotCoreManager
channel = Channel.current()
su=BotCoreManager.su('su')
ban_group=BotCoreManager.settings('ban_println_group')
ban_user=BotCoreManager.settings('ban_println_user')
disable=1
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def println(app: Ariadne, group: Group, message: MessageChain,event:GroupMessage):
 if message.display.startswith("println "):
        if disable==1:
           await app.send_message(
                group,
                 
                    MessageChain(f"非常抱歉，此模块当前已被禁用"),
     
        )
 else:
    if message.display.startswith("println "):
        await app.send_message(
                group,
                    MessageChain(f"{message.display[8:]}"),
        )
             
    elif group.id in (ban_group):
        await app.send_message(
        group,
        MessageChain(At(event.sender.id)," 非常抱歉，应开发者要求，本群已禁止此功能"))
    elif event.sender.id in (ban_user):
        await app.send_message(group, MessageChain(At(event.sender.id), " 对不起，应开发者要求，您已被禁止使用此功能"))
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("enable_println -g")]
    
    )
)
          
async def println(app: Ariadne, group: Group, message: MessageChain,event:GroupMessage):

 if event.sender.id in [su]:
     disable==0,
 await app.send_message(
                group,
           
                    MessageChain(f"已全局启用println模块"),
     
        )
        
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("disable_println -g")]
    )
)
async def println(app: Ariadne, group: Group, message: MessageChain,event:GroupMessage):

 if event.sender.id in [su]:
     disable==1,
 await app.send_message(
                group,
                
                    MessageChain(f"已全局禁用println模块"),
     
        )
        
                    
