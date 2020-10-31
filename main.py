# main.py
import os

import discord
from dotenv import load_dotenv
from datetime import date

import sys
import asyncio

today = date.today()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    #allow to quit only if a mod is doing this
    guild = client.get_guild(186610204023062528)
    mod_role = guild.get_role(219977258453041152)
    message_author = message.author
    is_mod = False
    if message.content.startswith("!!quit"):
        for role in message_author.roles:
            if role == mod_role:
                is_mod = True
        if is_mod:
            await message.channel.send("bot has been shutdown.")
            await exit()
        else:
            await mod_only_command(message)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.count == 1:
        channel_report = client.get_channel(771121618260852776)
        guild = client.get_guild(186610204023062528)
        mod_role = guild.get_role(219977258453041152)
        reacted_message = reaction.message
        reacted_message_content = reacted_message.content
        reacted_message_author = reaction.message.author
        reacted_message_author_roles = None
        long_message = False
        mod_report = False
        description = ""

        for role in reacted_message_author.roles:
            if role.name != '@everyone':
                if reacted_message_author_roles is None:
                    reacted_message_author_roles = str(role)
                else:
                    reacted_message_author_roles = str(reacted_message_author_roles) + ", " + str(role)

        try:
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
                        reported_message_part2_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator), icon_url=user.avatar_url)
                    else:
                        #if the message only contains an attachment
                        if len(reacted_message_content) != 0:
                            reported_message_embed.add_field(name="Message", value=reacted_message_content, inline=False)
                        else:
                            reported_message_embed.add_field(name="Attachment", value="*The reported message only contained an attachment; make sure to have it saved before reporting it as the bot cannot currently save (deleted) pictures. You can also give out a description of the attachment below*", inline=False)
                        reported_message_embed.set_footer(text="Reported by " + str(user.name) + "#" + str(user.discriminator) + " • " + str(today.strftime("%d/%m/%Y")), icon_url=user.avatar_url)

                    await channel_report.send(embed=reported_message_embed)
                    if long_message == True:
                        await channel_report.send(embed=reported_message_part2_embed)
                
        except:
            await channel_report.send("it crashed :(")
            raise

@client.event
async def mod_only_command(message):
    await message.channel.send("you cannot do this action as you are not a mod!")


client.run(TOKEN)