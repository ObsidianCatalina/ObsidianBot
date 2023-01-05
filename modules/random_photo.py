from aiohttp import ClientSession
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image,At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import BotCoreManager
channel = Channel.current()
url = BotCoreManager.url_config('setuapi')
ban_group =BotCoreManager.settings('ban_group_id')
ban_user =BotCoreManager.settings('ban_user_id')
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("来份涩图")],
    )
)
async def setu(app: Ariadne, group: Group,event:GroupMessage):
   if group.id in (ban_group):
    await app.send_message(
        group,
        MessageChain(At(event.sender.id)," 非常抱歉，应开发者要求，本群已禁止涩图功能"))
   elif event.sender.id in (ban_user):
        await app.send_message(group, MessageChain(At(event.sender.id), " 对不起，应开发者要求，您已被禁止使用此功能"))
   else:
    async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
    await app.send_group_message(group, MessageChain(Image(data_bytes=data)))

