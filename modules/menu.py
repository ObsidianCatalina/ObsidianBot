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
            f"菜单（开发中）\n"
            f"1.简介：作者&这个机器人的简介\n"
            f"2.unix知识：随机发送一条有关Unix系统的知识\n"
            f"3.更新日志：无描述\n"
            f"4.特别鸣谢：无描述\n"
            f"5.获取源代码：了解如何获取ObsidianBot的源码\n"
            f"6.答辩：随机一条答辩出来\n"
            f"7.来份涩图：随机发一张涩图/二次元图\n"
            f"8.println：用法：println <文字>，查看版本请输入:'println_moudle -v'\n"
            f"9.上菜：随机八种菜品（也有可能是别的东西）"
            )
    )
