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

#program version in .env and for git. if they're not matching, the program will quit. 
#if its a -dev version, it will load anyway but with a warning.
#make sure to change the version when updated!
VERSION = os.getenv('VERSION')
GIT_VERSION = "v0.3.8"
GIT_VERSION_DATE = "28/02/2021"

#dev mode is when i run the bot locally
devmode = False

#nurture time is for the countdown in #nurture
NURTURE_TIME = os.getenv('NURTURE_TIME')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.event
async def on_ready():
    try:
        global devmode
        now = datetime.now()

        if str(VERSION).endswith("-dev"):
            devmode = True

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

        #version mismatch check
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

        #bot version to be changed here for now - v major.minor.bugfix-dev
        init_message_embed = discord.Embed(title="bot has successfully booted up.", description="*bot version: " + VERSION + "*", color=0x00aeff)
        init_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))

        bot.loop.create_task(status_task())
        bot.loop.create_task(countdown())

        #full boot sequence successfully completed
        await bot.get_channel(772219545082396692).send(embed=init_message_embed)
        await bot.get_guild(186610204023062528).get_member(307932112294772737).edit(nick="Rin | " + VERSION)
        
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
async def info(ctx):
    try:
        now = datetime.now()
        kyllian_user = bot.get_user(171000921927581696)
        info_message_embed = discord.Embed(title="Rin-bot by " + str(kyllian_user.name) + "#" + str(kyllian_user.discriminator), description="*bot version " + VERSION + "*", url="https://github.com/kyllian1212/Rin", color=0x00aeff)
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
        lastversion = GIT_VERSION + " - " + GIT_VERSION_DATE
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
async def days_to_nurture(ctx):
    try:
        now = datetime.now()
        nowdate = datetime.now().date().strftime("%Y-%m-%d")
        d1 = datetime.strptime(nowdate, "%Y-%m-%d")
        d2 = datetime.strptime("2021-04-23", "%Y-%m-%d")
        diff = abs((d2 - d1).days)
        changelog_message_embed = discord.Embed(title="There are " + str(diff) + " days left before Nurture releases (in the GMT timezone)", color=0x00aeff)
        changelog_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await ctx.channel.send(embed=changelog_message_embed)
    except:
        await crash_handler()
        raise

async def days_to_nurture_auto():
    try:
        now = datetime.now()
        channel_nurture = bot.get_channel(671792848135389184)
        nowdate = datetime.now().date().strftime("%Y-%m-%d")
        d1 = datetime.strptime(nowdate, "%Y-%m-%d")
        d2 = datetime.strptime("2021-04-23", "%Y-%m-%d")
        diff = abs((d2 - d1).days)
        if diff > 1:
            changelog_message_embed = discord.Embed(title="There are " + str(diff) + " days left before Nurture releases (in the GMT timezone)", color=0x00aeff)
        elif diff == 1:
            changelog_message_embed = discord.Embed(title="There is " + str(diff) + " days left before Nurture releases (in the GMT timezone)", color=0x00aeff)
        elif diff == 0:
            changelog_message_embed = discord.Embed(title="NURTURE IS OUT NOW!! (in the GMT timezone)", color=0x00aeff)
        changelog_message_embed.set_footer(text=str(now.strftime("%d/%m/%Y - %H:%M:%S")))
        await channel_nurture.send(embed=changelog_message_embed)
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
                                if role == mod_role:
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

#rin presence
async def status_task():
    try:
        await bot.wait_until_ready()
        while True:
            variable = random.randint(0, (len(sl.song_library)-1))
            #code for playing it the right order when nurture is released is commented
            #variable = 0
            if str(VERSION).endswith("-dev"):
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="[DEV MODE] " + sl.song_library[variable][0] + " by " + sl.song_library[variable][1]))
            else:
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=sl.song_library[variable][0] + " by " + sl.song_library[variable][1]))
            #if variable == 13:
            #   variable = 0
            #else:
            #   variable += 1
            #DONT FORGET TO AWAIT A ASYNCIO.SLEEP() COMMAND!!!!!
            await asyncio.sleep(sl.song_library[variable][2])
    except:
        await crash_handler()
        raise

#countdown post
async def countdown():
    try:
        await bot.wait_until_ready()
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            if current_time == NURTURE_TIME:
                await days_to_nurture_auto()
                await asyncio.sleep(1)
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