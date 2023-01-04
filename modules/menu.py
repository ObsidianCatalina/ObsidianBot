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
        decorators=[MatchContent("菜单")]
    )
)
async def menu(app: Ariadne, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"菜单（开发中）\n1，简介：作者&这个机器人的简介\n2，linux知识：随机发送一条有关Unix/Linux系统的知识\n3，更新日志：无描述\n4，特别鸣谢：无描述\n5，获取源代码：了解如何获取ObsidianBot的源码\n6，答辩：随机一条答辩出来")
    )
