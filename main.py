# Powered by @Darkranger00 | TELE:- @aadillllll
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by Aadil Shiekh
import logging
import re
import os
import sys, platform
# import functie as S
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime

#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = 10738943
API_HASH = "da61e3a08b5ac78ce28b4a4cd854aeec"
BOT_TOKEN = "5654391796:AAF1uSjWbkicVT4vmWtwf2I0S2jMzkzdgcU"
OWNER_ID = "5206048155"
SUDO_ID = "5206048155"
LUCIFER = "5206048155"
COWNER_ID = "5206048155"
OP  = [ int(OWNER_ID), int(SUDO_ID), int(COWNER_ID), int(LUCIFER)]
#TelegramClient..
sree = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "aadillllll"
repo = "https://github.com/Mokye789/Banall-1"
@sree.on(events.NewMessage(pattern="^ريكا مبضونه"))
async def bun(event):
  if event.sender.id in OP:
   if not event.is_group:
        Rep = f"__Brush Are You Serious 🙄.\nUse This Command In Any Group!!__"
        await event.reply(Rep)
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__I Don't Have Sufficient Rights To Do This.__")
           return
       hmm =  await event.reply("__Ye Bilek Migic Begins🥳...__")
       await sleep(18)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__Wait Restarting...__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__Wait Leaving...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__Wait Leaving...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await z.edit(str(e))

@sree.on(events.NewMessage)
async def ver(events):
    events = S
    await events.main(str(e))


print("Your Bot  Deployed Successfully ✅")
print("Join @crushbot_support if you facing any kind of issue!!")



sree.run_until_disconnected()
