import pkgutil
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import config
from graia.broadcast import Broadcast
from graia.saya import Saya
import BotCoreManager
saya = create(Saya)
bcc = create(Broadcast)
app = Ariadne(
    connection=config(
        BotCoreManager.bot_global('bot_qq_id'),  # 你的机器人的 qq 号
        BotCoreManager.bot_global('verifykey'),  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口

    ),
)
print ("Type-Release10.3已启动")
with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        if module_info.name.startswith("_"):
            continue
        saya.require(f"modules.{module_info.name}")
app.launch_blocking()
