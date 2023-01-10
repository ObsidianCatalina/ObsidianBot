import random

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain,At
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.parser.base import MatchContent
import BotCoreManager

channel = Channel.current()
# 读取json
menu = BotCoreManager.take_menu('menu')
ban_group = BotCoreManager.settings('ban_takemenu_group_id')
ban_user = BotCoreManager.settings('ban_takemenu_id')
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("上菜")],
    )
)
async def setu(app: Ariadne, group: Group, event: GroupMessage):
    if group.id in ban_group:
        await app.send_message(
            group,
            MessageChain(At(event.sender.id), " 非常抱歉，应开发者要求，本群已禁止上菜功能"))
    elif event.sender.id in ban_user:
        await app.send_message(group, MessageChain(At(event.sender.id), " 对不起，应开发者要求，您已被禁止使用此功能"))
    else:
        await app.send_message(
            group,
            MessageChain("菜单:\n"
            "1,",random.choice(menu),"\n"
            "2,",random.choice(menu),"\n"
            "3,",random.choice(menu),"\n"
            "4,",random.choice(menu),"\n"
            "5,",random.choice(menu),"\n"
            "6,",random.choice(menu),"\n"
            "7,",random.choice(menu),"\n"
            "8,",random.choice(menu),"\n"
            "9,",random.choice(menu),"\n"
            "10,",random.choice(menu)
            )
        )
