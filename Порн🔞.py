#░█░█░█▀▀░█▀█░█▀▀░▀█▀░█▀▄░█▀▀
#░▄▀▄░█▀▀░█░█░▀▀█░░█░░█░█░█▀▀
#░▀░▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀

# 🔒 Licensed under the AGPL-3.0
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @XenSideMOD
# scope: hikka_only
# scope: hikka_min 1.3.0

import random
from ..inline.types import InlineCall
from telethon.tl.types import Message
from .. import loader


@loader.tds
class ПорнMod(loader.Module):
    """Порн"""

    strings = {"name": "Порн кнопки"}

    @loader.command()
    async def тыкcmd(self, message: Message):
        """→Инлайн порн"""
        self.chat_id = message.chat_id
        self.reply_porn = await message.get_reply_message()
        await self.inline.form(
            message=message,
            text="🔞<b>Точно хочеш подтверить что в чате разрешено 18+? Если нет удали сообщение.</b>🛌",
            reply_markup=[[{"text": "ДА", "callback": self.porn}]],
        )

    async def sticker_porn(self, *_):
        m = random.choice(await self._client.get_messages("@sticksformod", limit=10))
        if self.reply_porn:
            await self.client.send_message(
                self.chat_id, file=m, reply_to=self.reply_porn
            )
        else:
            await self.client.send_message(self.chat_id, file=m)

    async def porn(self, call: InlineCall):
        await call.edit(
            text="<b>🔞Нажми на кнопку и я скину порнуху!</b>",
            reply_markup=[
                [
                    {"text": "🔞", "callback": self.sticker_porn},
                ],
            ],
        )