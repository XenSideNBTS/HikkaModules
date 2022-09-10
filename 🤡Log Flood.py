__version__ = (6, 6, 6)


#░█░█░█▀▀░█▀█░█▀▀░▀█▀░█▀▄░█▀▀
#░▄▀▄░█▀▀░█░█░▀▀█░░█░░█░█░█▀▀
#░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀

# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @XenSideMOD

from .. import loader, utils

import asyncio
from telethon.tl.types import Message


@loader.tds
class LogFlooder(loader.Module):

    strings = {"name": "⚠️Log Flood🤡"}

    async def podkatcmd(self, message: Message):
        "💬Флудит логи чата💬 ⚠️МОЖНО ПОЛУЧИТЬ ФЛУДВЕЙТ!!!!⚠️"
        for _ in range(500):
            for anim in [".", ".."]:
                message = await utils.answer(message, anim)
                await asyncio.sleep(0.1)