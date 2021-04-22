# main.py
import os

import discord
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import bot
import sys
import asyncio
import traceback
import random

import song_library as sl

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#make sure to change the version when updated!
version = "v0.3.16"
version_date = "21/04/2021"

#dev mode is when i run the bot (dont forget to disable it!!!)
devmode = False

#nurture time is for the countdown in #nurture
NURTURE_TIME = os.getenv('NURTURE_TIME')
NURTURE_TIME_2 = os.getenv('NURTURE_TIME_2')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.event
async def on_ready():
    try:
        global devmode
        global version
        now = datetime.now()

        for guild in bot.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

        membercount = 0
        for member in guild.members:
            membercount = membercount+1

        print(f'Guild Member Count: {membercount}')

        #version mismatch check (deprecated)
        '''
        if VERSION != GIT_VERSION:
            if devmode:
                versionmismatch_message_embed = discord.Embed(title="warning: versions aren't matching", description="*the bot is in dev mode, so it will boot anyways.*", color=0xffae42)
            else:
                versionmismatch_message_embed = discord.Embed(title="error: versions aren't matching!!", color=0xff0000)
                versionmismatch_message_embed.add_field(name="reason", value="this error can happen because:\n " + 
                "- the .env value for 'version' isn't correctly set\n" +
                "- the bot is running on the previous commit\n " +
                "- the bot is in dev mode, but there's an issue with the devmode variable\n " +
                "\nplease check the .env values or make sure the next commit is built. the bot will now shutdown."
                , inline=False)
            versionmismatch_message_embed.add_field(name=".env version", value="*"+VERSION+"*", inline=True)
            versionmismatch_message_embed.add_field(name="git version", value="*"+GIT_VERSION+"*", inline=True)
            versionmismatch_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))

            await bot.get_channel(772219545082396692).send(embed=versionmismatch_message_embed)

            if not devmode:
                await os._exit(-1)
        '''

        #devmode check for versioning indication
        if devmode:
            version = version + "-dev"

        #bot version to be changed here for now - v major.minor.bugfix-dev
        init_message_embed = discord.Embed(title="bot has successfully booted up.", description="*bot version: " + version + "*", color=0x00aeff)
        init_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))

        bot.loop.create_task(status_task())
        bot.loop.create_task(countdown())

        #full boot sequence successfully completed
        await bot.get_channel(772219545082396692).send(embed=init_message_embed)
        await bot.get_guild(186610204023062528).get_member(307932112294772737).edit(nick="Rin | " + version)
        
    except:
        await crash_handler()
        await os._exit(-1)
        raise

@bot.command()
async def quit(ctx):
    try:
        now = datetime.now()
        guild = bot.get_guild(186610204023062528)
        mod_role = guild.get_role(219977258453041152)
        message_author = ctx.author
        is_mod = False
        for role in message_author.roles:
            if role == mod_role:
                is_mod = True
        if is_mod:
            await ctx.channel.send("bot has been shutdown.")
            quit_message_embed = discord.Embed(title="bot has successfully shutdown.", color=0x00aeff)
            quit_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
            await bot.get_channel(772219545082396692).send(embed=quit_message_embed)
            await bot.loop.stop()
            await os._exit(1)
        else:
            await mod_only_command(ctx)
    except:
        await crash_handler()
        raise

@bot.command()
async def say(ctx, *, arg):
    try:
        guild = bot.get_guild(186610204023062528)
        mod_role = guild.get_role(219977258453041152)
        message_author = ctx.author
        is_mod = False
        for role in message_author.roles:
            if role == mod_role:
                is_mod = True
        if is_mod:
            await ctx.message.delete()
            await ctx.channel.send(arg)
    except:
        await crash_handler()
        raise

@bot.command()
async def saytts(ctx, *, arg):
    try:
        guild = bot.get_guild(186610204023062528)
        mod_role = guild.get_role(219977258453041152)
        message_author = ctx.author
        is_mod = False
        for role in message_author.roles:
            if role == mod_role:
                is_mod = True
        if is_mod:
            await ctx.message.delete()
            await ctx.channel.send(arg, tts=True)
    except:
        await crash_handler()
        raise

@bot.command()
async def info(ctx):
    try:
        now = datetime.now()
        kyllian_user = bot.get_user(171000921927581696)
        info_message_embed = discord.Embed(title="Rin-bot by " + str(kyllian_user.name) + "#" + str(kyllian_user.discriminator), description="*bot version " + version + "*", url="https://github.com/kyllian1212/Rin", color=0x00aeff)
        info_message_embed.set_thumbnail(url=kyllian_user.avatar_url)
        info_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")) + "  •  source code available by clicking the link above", icon_url=bot.user.avatar_url)
        await ctx.channel.send(embed=info_message_embed)
    except:
        await crash_handler()
        raise

@bot.command()
async def october18(ctx):
    try:
        dad_message_embed = discord.Embed(title="To: Rin", description="**From: Dad**", color=0x00aeff)
        dad_message_embed.set_thumbnail(url=bot.user.avatar_url)
        dad_message_embed.add_field(name="Message", value="There was just so little time left after you were born. \nI don't know how much love I managed to pour into raising you after your mother died... \nBut your smile kept me going. (^_^) \n\nI would like to have come with you, but I couldn't. \nI wanted you to forget everything and move on... \nI knew you'd be alright. But you'll get lonely, and remember. \n\nI know you'll grow strong, and read this letter some day. \nI really wish we could have spent more time together. I'm sorry. \nYou were so young back then, too young to understand what they meant. So let me repeat... \n\nMy final words to you.", inline=False)
        dad_message_embed.set_footer(text="19/10/2016 - 04:00:00 (JST)")
        await ctx.channel.send(embed=dad_message_embed)
    except:
        await crash_handler()
        raise

@bot.command()
async def changelog(ctx):
    try:
        now = datetime.now()
        lastversion = version + " - " + version_date
        changelog = open('lastchange_bot.txt', 'r').read()
        changelog_message_embed = discord.Embed(title="hello i've updated the bot :) | " + lastversion, description=changelog, url="https://github.com/kyllian1212/Rin/blob/master/changelog.md", color=0x00aeff)
        changelog_message_embed.set_thumbnail(url=bot.user.avatar_url)
        changelog_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")) + "  •  full changelog available by clicking the link above")
        await ctx.channel.send(embed=changelog_message_embed)
    except:
        await crash_handler()
        raise

@bot.command()
async def roll(ctx):
    try:
        random_variable = random.randint(1, 6)
        await ctx.channel.send("1d6 roll result: **" + str(random_variable) + "**")
    except:
        await crash_handler()
        raise

@bot.command()
async def fiftyfifty(ctx):
    try:
        random_variable = random.randint(0, 999)
        if 0 <= random_variable <= 499:
            await ctx.channel.send("50/50 choice: **YES**")
        if 500 <= random_variable <= 999:
            await ctx.channel.send("50/50 choice: **NO**")
    except:
        await crash_handler()
        raise

@bot.command()
async def nurture(ctx):
    try:
        now = datetime.now()
        d1 = datetime.now()
        d2 = datetime(2021, 4, 22, 12, 0, 0)
        diff = d2-d1
        diffd = int((diff.total_seconds())/60/60/24)+1
        diffh = int((diff.total_seconds()+1)/60/60)
        diffm = int((diff.total_seconds()+1)/60)
        diffs = int((diff.total_seconds()+1))
        diffs_float = float((diff.total_seconds()+1))
        if diffs_float <= 1:
            nurture_release_embed = discord.Embed(title="Nurture is out!!", color=0x00aeff)
            nurture_release_embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/0/07/Porter_Robinson_-_Nurture.png")
            nurture_release_embed.add_field(name="Reminder", value="Please talk about the album itself *only* in <#821895682709389313> until the embargo ends! Talks about the album anywhere else in the server, even with spoiler tags, aren't allowed (only exception being the singles and remixes that were already released).", inline=False)
        elif diffm <= 1:
            nurture_message_embed = discord.Embed(title="There are " + str(diffs) + " seconds left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh <= 2:
            nurture_message_embed = discord.Embed(title="There are " + str(diffm) + " minutes (" + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh < 100:
            nurture_message_embed = discord.Embed(title="There are " + str(diffh) + " hours (" + str(diffm) + " minutes, " + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh >= 100:
            nurture_message_embed = discord.Embed(title="There are " + str(diffd) + " days (" + str(diffh) + " hours, " + str(diffm) + " minutes, " + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        nurture_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await ctx.channel.send(embed=nurture_message_embed)
    except:
        await crash_handler()
        raise

#CHANGE TO NZST WHEN YOU CAN INSTEAD OF UTC
#scheduling:
#pre-month of release: every 24hrs
#month of release (30 days before): every 12hrs
#week of release (7 days before): every 6hrs
#3 days before release: every 3hrs
#12hrs before release: every hour
#followed by rin indicating the release in every timezone
async def days_to_nurture_auto():
    try:
        now = datetime.now()
        channel_nurture = bot.get_channel(671792848135389184)
        d1 = datetime.now()
        d2 = datetime(2021, 4, 22, 12, 0, 0)
        diff = d2-d1
        diffd = int((diff.total_seconds())/60/60/24)+1
        diffh = int((diff.total_seconds()+1)/60/60)
        diffm = int((diff.total_seconds()+1)/60)
        diffs = int((diff.total_seconds()+1))
        diffs_float = float((diff.total_seconds()+1))
        await nurture_release_check()
        if diffs_float <= 1:
            print("a")
        elif diffm <= 1:
            nurture_auto_message_embed = discord.Embed(title="There are " + str(diffs) + " seconds left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh <= 2:
            nurture_auto_message_embed = discord.Embed(title="There are " + str(diffm) + " minutes (" + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh < 100:
            nurture_auto_message_embed = discord.Embed(title="There are " + str(diffh) + " hours (" + str(diffm) + " minutes, " + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        elif diffh >= 100:
            nurture_auto_message_embed = discord.Embed(title="There are " + str(diffd) + " days (" + str(diffh) + " hours, " + str(diffm) + " minutes, " + str(diffs) + " seconds) left before Nurture releases (in the NZST timezone)", color=0x00aeff)
        nurture_auto_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await channel_nurture.send(embed=nurture_auto_message_embed)
    except:
        await crash_handler()
        raise

async def nurture_release_check():
    try:
        embargo = True
        nowwithms = str(datetime.now())
        nowstrp = datetime.strptime(nowwithms, "%Y-%m-%d %H:%M:%S.%f")
        nowfooter = nowstrp.strftime("%Y-%m-%d %H:%M:%S")
        channel_nurture = bot.get_channel(671792848135389184)
        nurture_release_embed = discord.Embed(title="Nurture is out!!", color=0x00aeff)
        nurture_release_embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/0/07/Porter_Robinson_-_Nurture.png")
        if str(nowfooter) == str(datetime(2021, 4, 22, 12, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- New Zealand \n(im sorry in advance, i wont be able to quote every single country the album is out at but i will quote the most important ones/those who i think represent porter's demographic the most!)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 14, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- Australia \n(and more)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 15, 7, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- South Korea \n- Japan (!) \n- Indonesia \n(and more)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 16, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- China \n- Taiwan \n- Philippines \n- Singapore \n(and more)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 19, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- India \n(and more)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 21, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="Many countries in the UTC+3 timezone (Finland, Ukraine, Greece, many more...)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 22, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="Many countries in the UTC+2 timezone (France, Germany, Belgium, Spain, Italy, many many more...)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 22, 23, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- United Kingdom \n-Ireland \n- Portugal \n(and more)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 23, 0, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- Iceland", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 23, 3, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- Brazil \n- Argentina \n- Chile", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 23, 4, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- Canada \n- United States of America", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 23, 5, 0, 0)):
            nurture_release_embed.add_field(name="The album is now out in, for example, those countries:", value="- Mexico \n(the album is pretty much out everywhere now)", inline=False)
        elif str(nowfooter) == str(datetime(2021, 4, 23, 12, 0, 0)):
            embargo = False
        
        if embargo == True:
            nurture_release_embed.add_field(name="Reminder", value="Please talk about the album itself *only* in <#821895682709389313> until the embargo ends! Talks about the album anywhere else in the server, even with spoiler tags, aren't allowed (only exception being the singles and remixes that were already released).", inline=False)
        else:
            nurture_release_embed.add_field(name="The album is now out everywhere.", value="The embargo has been lifted; you can talk about the album everywhere in the server now! ~~my countdown job is done. goodbye~~", inline=False)
        nurture_release_embed.set_footer(text=str(nowfooter))
        await channel_nurture.send(embed=nurture_release_embed)
    except:
        await crash_handler()
        raise


@bot.event
async def on_reaction_add(reaction, user):
    try:
        now = datetime.now()
        reacted_message = reaction.message
        reacted_message_content = reacted_message.content
        reacted_message_author = reaction.message.author
        reacted_message_author_roles = None
        guild = bot.get_guild(186610204023062528)
        mod_role = guild.get_role(219977258453041152)
        temp_mod_role = guild.get_role(816596360064532501)

        if reaction.count == 1:
            if devmode:
                channel_report = bot.get_channel(775080183602085899)
            else:
                channel_report = bot.get_channel(413488194819194891)
            long_message = False
            mod_report = False
            description = ""

            #checks if the user is a webhook/deleted and doesnt report if so
            if reacted_message_author.discriminator != '0000':
                if user.guild == guild:
                    for role in reacted_message_author.roles:
                        if role.name != '@everyone':
                            if reacted_message_author_roles is None:
                                reacted_message_author_roles = str(role)
                            else:
                                reacted_message_author_roles = str(reacted_message_author_roles) + ", " + str(role)

                    
                    if reaction.emoji == '🚫':
                        #if a user auto reacts 🚫 to their message, it just deletes it without reporting it
                        if user == reacted_message_author:
                            await reacted_message.delete()
                        else:
                            for role in user.roles:
                                if role == mod_role or role == temp_mod_role:
                                    #report_confirmation_embed = discord.Embed(title="The message has been reported.", color=0xff0000)
                                    await reacted_message.delete()
                                    mod_report = True
                                    description = "*The message has been deleted as it has been reported by an admin.*"
                                    #report_confirmation_message = await reacted_message.channel.send(embed=report_confirmation_embed)
                                    #await asyncio.sleep(2)
                                    #await report_confirmation_message.delete()

                            reported_message_embed = discord.Embed(title="Reported Message - ID: " + str(reacted_message.id), description=description, color=0xff0000)
                            reported_message_embed.set_thumbnail(url=reacted_message_author.avatar_url)
                            reported_message_embed.add_field(name="Username", value=reacted_message_author.name, inline=True)
                            reported_message_embed.add_field(name="Nickname", value=reacted_message_author.nick, inline=True)
                            reported_message_embed.add_field(name="User ID", value="<@" + str(reacted_message_author.id) + ">", inline=True)
                            reported_message_embed.add_field(name="Channel", value="<#" + str(reacted_message.channel.id) + ">", inline=True)
                            reported_message_embed.add_field(name="User Roles", value=str(reacted_message_author_roles), inline=True)
                            #if the message is too long
                            if len(reacted_message_content) >= 1000:
                                long_message = True
                                message_length = len(reacted_message_content)
                                reacted_message_content_part2 = reacted_message_content[999:message_length]
                                reacted_message_content = reacted_message_content[0:999]
                                reported_message_embed.add_field(name="Message", value=reacted_message_content, inline=False)
                                reported_message_part2_embed = discord.Embed(description="*The message is over 1000 characters, so it has been split into 2 Discord embeds.*", color=0xff0000)
                                reported_message_part2_embed.add_field(name="Message (part 2)", value=reacted_message_content_part2, inline=False)
                                reported_message_part2_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator) + "  •  " + str(now.strftime("%d/%m/%Y - %H:%M:%S")), icon_url=user.avatar_url)
                            else:
                                #if the message only contains an attachment
                                if len(reacted_message_content) != 0:
                                    reported_message_embed.add_field(name="Message", value=reacted_message_content, inline=False)
                                else:
                                    reported_message_embed.add_field(name="Attachment", value="*The reported message only contained an attachment; make sure to have it saved before reporting it as the bot cannot currently save (deleted) pictures. You can also give out a description of the attachment below*", inline=False)
                                reported_message_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator) + "  •  " + str(now.strftime("%d/%m/%Y - %H:%M:%S")), icon_url=user.avatar_url)

                            await channel_report.send(embed=reported_message_embed)
                            if long_message == True:
                                await channel_report.send(embed=reported_message_part2_embed)
        elif reaction.count > 1:
            if reaction.emoji == '🚫':
                #if a user auto reacts 🚫 to their message, it just deletes it without reporting it
                if user == reacted_message_author:
                    await reacted_message.delete()
                else:
                    for role in user.roles:
                        if role == mod_role:
                            await reacted_message.delete()

    #put crash handler in another function   
    except:
        await crash_handler()
        raise

@bot.event
async def mod_only_command(message):
    await message.channel.send("you cannot do this action as you are not a mod!")

variable = 0
#rin presence
async def status_task():
    try:
        await bot.wait_until_ready()
        while True:
            #variable = random.randint(0, (len(sl.song_library)-1))
            global variable
            if str(version).endswith("-dev"):
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="[DEV MODE] " + sl.song_library_nurture[variable][0] + " by " + sl.song_library_nurture[variable][1]))
            else:
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=sl.song_library_nurture[variable][0] + " by " + sl.song_library_nurture[variable][1]))
            #DONT FORGET TO AWAIT A ASYNCIO.SLEEP() COMMAND!!!!!
            await asyncio.sleep(sl.song_library_nurture[variable][2])
            if variable == 14:
               variable = 0
            else:
               variable = variable + 1
    except:
        await crash_handler()
        await status_task()
        raise

#countdown post
async def countdown():
    try:
        await bot.wait_until_ready()
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            dc1 = datetime.now()
            dc2 = datetime(2021, 4, 23, 12, 0, 0)
            diffc = dc2-dc1
            diffch = int((diffc.total_seconds()+1)/60/60)
            NURTURE_TIME_DICT=[
                "00:00:00", "01:00:00", "02:00:00",
                "03:00:00", "04:00:00", "05:00:00",
                "06:00:00", "07:00:00", "08:00:00",
                "09:00:00", "10:00:00", "11:00:00",
                "12:00:00", "13:00:00", "14:00:00",
                "15:07:00", "16:00:00", "17:00:00",
                "18:00:00", "19:00:00", "20:00:00",
                "21:00:00", "22:00:00", "23:00:00"
            ]
            if diffch < 24:
                if current_time in NURTURE_TIME_DICT:
                    await days_to_nurture_auto()
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(0.5)
            elif diffch < 72:
                if current_time == NURTURE_TIME_DICT[0] or current_time == NURTURE_TIME_DICT[3] or current_time == NURTURE_TIME_DICT[6] or current_time == NURTURE_TIME_DICT[9] or current_time == NURTURE_TIME_DICT[12] or current_time == NURTURE_TIME_DICT[15] or current_time == NURTURE_TIME_DICT[18] or current_time == NURTURE_TIME_DICT[21]:
                    await days_to_nurture_auto()
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(0.5)
            elif diffch < 168:
                if current_time == NURTURE_TIME_DICT[0] or current_time == NURTURE_TIME_DICT[6] or current_time == NURTURE_TIME_DICT[12] or current_time == NURTURE_TIME_DICT[18]:
                    await days_to_nurture_auto()
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(0.5)
            elif diffch >= 168:
                if current_time == NURTURE_TIME_DICT[0] or current_time == NURTURE_TIME_DICT[12]:
                    await days_to_nurture_auto()
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(0.5)
            else:
                await asyncio.sleep(0.5)
    except:
        await crash_handler()
        raise

#crash handler
async def crash_handler():
    try:
        now = datetime.now()
        crash_traceback = traceback.format_exc()
        crash_message_embed = discord.Embed(title="it crashed :(", description=crash_traceback, color=0xff0000)
        crash_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await bot.get_channel(772219545082396692).send(embed=crash_message_embed)
    except:
        try:
            now = datetime.now()
            crash_traceback = traceback.format_exc()
            crash_message_embed = discord.Embed(title="the crash handler crashed!! D:", description=crash_traceback, color=0xff0000)
            crash_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
            await bot.get_channel(772219545082396692).send(embed=crash_message_embed)
        except:
            raise

#launch bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except:
        raise

#bot log: tmux a -t [number]