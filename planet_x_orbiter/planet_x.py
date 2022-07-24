import discord
import random
from discord.ext import commands
# import webbrowser
import urllib.request
import re
import datetime
import pytz
import asyncio
import typing

with open('token.txt', 'r') as tk:
    hidden_token = tk.read()
TOKEN = hidden_token
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('in Orbit'))
    print('Bot in Orbit')


@client.event
async def on_user_join(member):
    print(f'{member} has joined Planet X')


@client.event
async def on_user_leave(member):
    print(f'{member} has left Planet X')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send('Pass all required arguments. For help try `$commands`')

    elif isinstance(error, discord.ext.commands.MissingPermissions):
        await ctx.send('Nice try, you don\'t have permissions for this command')

    elif isinstance(error, discord.ext.commands.TooManyArguments):
        await ctx.send('You gave too many arguments. For help try `$commands`')

    elif isinstance(error, discord.ext.commands.CommandNotFound):
        await ctx.send('Invalid command. For help try `$commands`')


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'`{member}` has been kicked from Planet X')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'`{member}` has been banned from Planet X')


@client.command()
async def hello(ctx):
    user = ctx.message.author
    user_name = user.name
    await ctx.send(f'Hello, {user_name}👋')


@client.command()
async def latency(ctx):
    await ctx.send(f'📡pinged! `{round(client.latency * 1000)}ms`')


@client.command()
async def search(ctx):
    await ctx.send('Currently under maintenance')
# async def search(ctx, search_query):
#     await ctx.send(f'Redirecting to {search_query}')
#     await ctx.send(webbrowser.open_new_tab(search_query), delete_after=0.1)


@client.command()
async def video(ctx, *, video_query):
    vid_name = video_query.replace(' ', '+')
    url = urllib.request.urlopen(
     'https://www.youtube.com/results?search_query=' + vid_name)
    vid_id = re.findall(r"watch\?v=(\S{11})", url.read().decode())
    final_vid_url = 'https://www.youtube.com/watch?v=' + vid_id[0]
    await ctx.send(f'Showing result for -> `{video_query}`\n{final_vid_url}')


@client.command()
async def profilepic(ctx, member: discord.Member = None):
    profile_pic_url = member.avatar_url
    await ctx.send(f'Successfully fetched profile picture of -> `{member}`')
    await ctx.send(profile_pic_url)


@client.command()
async def mute(ctx):
    await ctx.send('Currently under maintenance')
# async def mute(ctx, *, member: discord.Member):
#     muted = discord.ext.utils.get(ctx.guild.roles, name="Muted")
#     await member.add_roles(muted)
#     await ctx.send(f'User -> {member} has been muted')


@client.command()
async def unmute(ctx):
    await ctx.send('Currently under maintenance')
# async def unmute(ctx, *, member: discord.Member):
#     muted = discord.ext.utils.get(ctx.guild.roles, name="Muted")
#     await member.remove_roles(muted)
#     await ctx.send(f'User -> {member} has been unmuted')


@client.command()
async def time(ctx, timezone_arg):
    all_tz = pytz.all_timezones
    py_tz = pytz.timezone(timezone_arg)
    if timezone_arg in all_tz:
        date_time = datetime.datetime.now(py_tz)
        f_date = date_time.strftime('%d/%m/%Y')  # date/month/year
        f_time = date_time.strftime('%H:%M:%S')  # Hour:Minute:Second
        await ctx.send(f'Current Date for `{timezone_arg}` -> `{f_date}`')
        await ctx.send(f'Current Time for `{timezone_arg}` -> `{f_time}`')
    else:
        await ctx.send('Invalid time zone, for help visit `https://en.wikipedia.org/wiki/List_of_tz_database_time_zones`')


@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, amount: typing.Union[int, str]):
    if isinstance(amount, int):
        amount_int = int(amount) + 1
        await ctx.channel.purge(limit=amount_int)
    elif isinstance(amount, str):
        await ctx.send(f'`{amount}` is an invalid amount')


@client.command()
async def nuke(ctx):
    if ctx.author == ctx.guild.owner:
        await ctx.send('☢️Nuke Deployed☢️')
        await asyncio.sleep(1)
        await ctx.send('Nuking in...3')
        await asyncio.sleep(1)
        await ctx.send('Nuking in...2')
        await asyncio.sleep(1)
        await ctx.send('Nuking in...1')
        await asyncio.sleep(1)
        await ctx.send('Boom💥')
        await ctx.channel.purge()
    else:
        await ctx.send('You haven\'t been given authority to use Planet X\'s nuclear arsenal')


@client.command()
async def creator(ctx):
    await ctx.send('I was built by albjon')


@client.command()
async def coinflip(ctx):
    coin_list = ['Heads', 'Tails',
                 'Heads', 'Tails',
                 'Heads', 'Tails',
                 'Heads', 'Tails']
    await ctx.send(f'Result -> `{random.choice(coin_list)}`')


@client.command(aliases=['timemachine'])
async def seer(ctx, *, question):
    responses = ['Yes',
                 'No',
                 'Maybe',
                 'Never',
                 'Probably',
                 'Who knows',
                 'If you work hard',
                 'Impossible',
                 'I\'m neutral',
                 'Certainly',
                 'I\'ll think about it, try again in a minute']
    await ctx.send(f'`Question:` {question}\n`Answer:` {random.choice(responses)}')


@client.command()
async def youtube(ctx):
    await ctx.send('Currently under maintenance')
    # embed = discord.Embed(
    #     title='Cronos',
    #     description='Subscribe to my YouTube channel! '
    #                 ''
    #                 'https://www.youtube.com/channel/UCKaUDYaQeX0JKkvXrDaqAuw',
    #     colour=discord.Colour.dark_purple()
    # )
    #
    # embed.set_footer(text='Planet X')
    # embed.set_image(url='https://i.pinimg.com/originals/09/0c/06/090c0658afb2350efff9c2ac705d5fe9.jpg')
    # embed.set_thumbnail(url='https://i.imgur.com/bQCF3FZ.gif')
    # embed.set_author(name='Cronos',
    #                  icon_url='https://yt3.ggpht.com/yti/ANoDKi4byPqSvGPjGSQAss5CpBaOcdb'
    #                           'lhFKR03_-RO0LSg=s88-c-k-c0x00ffffff-no-rj-mo')
    # # <Add Names and Values later>
    # # embed.add_field(name='Field Name', value='Field Value', inline=False)
    # # embed.add_field(name='Field Name', value='Field Value', inline=True)
    # # embed.add_field(name='Field Name', value='Field Value', inline=True)
    # await ctx.send(embed=embed)


@client.command()
async def twitch(ctx):
    await ctx.send('Currently under maintenance')
    # embed = discord.Embed(
    #     title='Cronos',
    #     description='Follow my Twitch channel! '
    #                 ''
    #                 'https://www.twitch.tv/icronolog',
    #     colour=discord.Colour.dark_purple()
    #     )
    #
    # embed.set_footer(text='Planet X')
    # embed.set_image(url='https://blog.twitch.tv/assets/uploads/03-glitch.jpg')
    # embed.set_thumbnail(url='https://media1.tenor.com/images/ca1508b577a1a952905fdefba1deb186/tenor.gif?itemid=17064308'
    #                     )
    # embed.set_author(name='Cronolog',
    #                  icon_url='https://yt3.ggpht.com/yti/ANoDKi4byPqSvGPjGSQAss5CpBaOcdb'
    #                          'lhFKR03_-RO0LSg=s88-c-k-c0x00ffffff-no-rj-mo')
    # # <Add Names and Values later>
    # # embed.add_field(name='Field Name', value='Field Value', inline=False)
    # # embed.add_field(name='Field Name', value='Field Value', inline=True)
    # # embed.add_field(name='Field Name', value='Field Value', inline=True)
    # await ctx.send(embed=embed)


@client.command()
async def commands(ctx):
    with open('commands.txt', 'r') as cmd:
        cmd_file_content = cmd.read()
    await ctx.send(cmd_file_content)

client.run(TOKEN)
