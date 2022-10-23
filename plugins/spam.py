# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Perintah Tersedia -
• `{i}spam <no of msgs> <your msg>`
  `{i}spam <no of msgs> <reply message>`
    obrolan spam, batas saat ini adalah dari 1 hingga 99.

• `{i}bigspam <no of msgs> <your msg>`
  `{i}bigspam <no of msgs> <reply message>`
    Obrolan spam, batas saat ini di atas 100.

• `{i}delayspam <delay time> <count> <msg>`
    Obrolan spam dengan penundaan..

• `{i}tspam <text>`
    Obrolan Spam dengan Karakter Satu-Satu..
"""

import asyncio

from . import *


@ultroid_cmd(pattern="tspam")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@ultroid_cmd(pattern="spam")
async def spammer(e):
    message = e.text
    if e.reply_to:
        if not len(message.split()) >= 2:
            return await eod(e, "`Use in Proper Format`")
        spam_message = await e.get_reply_message()
    else:
        if not len(message.split()) >= 3:
            return await eod(e, "`Reply to a Message or Give some Text..`")
        spam_message = message.split(maxsplit=2)[2]
    counter = message.split()[1]
    try:
        counter = int(counter)
        if counter >= 100:
            return await eod(e, "`Use bigspam cmd`")
    except BaseException:
        return await eod(e, "`Use in Proper Format`")
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()


@ultroid_cmd(pattern="bigspam", fullsudo=True)
async def bigspam(e):
    message = e.text
    if e.reply_to:
        if not len(message.split()) >= 2:
            return await eod(e, "`Use in Proper Format`")
        spam_message = await e.get_reply_message()
    else:
        if not len(message.split()) >= 3:
            return await eod(e, "`Reply to a Message or Give some Text..`")
        spam_message = message.split(maxsplit=2)[2]
    counter = message.split()[1]
    try:
        counter = int(counter)
    except BaseException:
        return await eod(e, "`Use in Proper Format`")
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()


@ultroid_cmd(pattern="delayspam ?(.*)")
async def delayspammer(e):
    try:
        args = e.text.split(" ", 3)
        delay = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit(f"**Usage :** {HNDLR}delayspam <delay time> <count> <msg>")
    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await e.respond(f"**Error :** `{u}`")
