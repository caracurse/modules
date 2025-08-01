#Name: Text2File
#Description: Module for convertation your text to file
#Author: @sansaramods
#Commands:
#.ttf
# ---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/exodiast
#-----------------------------------------------------------------------------------
# meta developer: @sansaramods
#-----------------------------------------------------------------------------------

__version__ = (1, 1, 2)

from .. import loader, utils
import logging
from herokutl.types import Message
import io

__version__ = (1, 0, 0)
logger = logging.getLogger(__name__)

@loader.tds
class Text2File(loader.Module):
    """Module for convertation your text to file"""
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "name",
                "file.txt",
                lambda:
                self.strings("cfg_name"),
            ),
        )

    strings = {
        "name": "Text2File",
        "no_args": "Don't have any args! Use .ttf text/code",
        "cfg_name": "You can change the extension and file name",
    }

    strings_ru = {
        "no_args": "Недостаточно аргументов! Используйте: .ttf текст/код",
        "cfg_name": "Вы можете выбрать расширение и название для файла",
    }

    @loader.command()
    async def ttfcmd(self, message: Message):
        """-> to create a file with your text or code"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_args"))
        else:
            text = args
            by = io.BytesIO(text.encode("utf-8"))
            by.name = self.config["name"]

            await utils.answer_file(message, by)
