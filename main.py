import pkgutil
from creart import create 
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.broadcast import Broadcast
from graia.saya import Saya
saya=create(Saya)
bcc = create(Broadcast)
app = Ariadne(
    connection=config(
        2946761346,  # 你的机器人的 qq 号
        "GraiaxVerifyKey",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
     
    ),
)


@bcc.receiver(GroupMessage)
async def main(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "爱你":
        await app.send_message(
            group,
           MessageChain(f"我也爱你"),
        )
    if message.display== "菜单":
         await  app.send_message(
        group,
        MessageChain(f"菜单（开发中）\n1，爱你:会回复“我也爱你”\n2，简介:作者&这个机器人的简介")
    )
with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        if module_info.name.startswith("_"):
            continue
        saya.require(f"modules.{module_info.name}")
app.launch_blocking()