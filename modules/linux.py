from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("linux知识")]
    )
)
async def linux(app: Ariadne, group: Group):
    knowledge = [
        'usr不等于user哦，而是"Unix Software Resource"的缩写',
        "/etc目录存放的主要是配置文件，如用户信息、服务的启动脚本、常用服务的配置文件等",
        "/bin目录存放的主要是系统命令，如sudo，普通用户和root用户都可以执行",
        "rm是一个神奇的命令，用于删除文件，文件夹，目录，甚至是/,-rf参数表示的是强制执行，如果想删除一个或者大多个文件（文件夹），可以使用:"
        "sudo rm -rf file1 file2 file3或者sudo rm -rf folder1 folder2 folder3等",
        "不同的系统拥有不同的包管理，如deb系统的包管理为apt，dpkg RHEL系统为yum，dnf（openSUSE为zypper），Arch系统主要为pacman等"
    ]
    await app.send_message(
        group,
        MessageChain(random.choice(knowledge))
    )
