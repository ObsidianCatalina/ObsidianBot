# 本部分示例不完整，请自行补充
# 本部分示例需使用 Saya 进行加载

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain,Plain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema# from graia.ariadne.event.message import GroupMessage
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.element import At
channel = Channel.current()
# 此处注释的意思是用法类比，不是说这里可以用 GroupMessage
# @channel.use(ListenerSchema(listening_events=[GroupMessage]))

@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def getup(app: Ariadne, event: NudgeEvent):

    if event.context_type == "group":
        await app.send_group_message(
            event.group_id,
            MessageChain(MessageChain(At(event.supplicant),Plain(" 再戳老娘就把你手指头掰断！！！！！！！！")))
        )
    elif event.context_type == "friend":
        await app.send_friend_message(
            event.friend_id,
            MessageChain("再戳打死你！")
        )
    else:
        return
