import class_data
import discord
import nice_data
from discord.ext import commands
import asyncio
import os
from keep_alive import keep_alive
import datetime as DT
import paginator

client = commands.Bot(command_prefix=">")
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug", "Sep", "Oct", "Nov", "Dec"]


List = class_data.nice_data()


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def list(ctx):
    cnt = 0

    embed = discord.Embed(
        title="Future Contests", color=discord.Color.blue()
    )
    pages = []
    pagecnt =1
    for x in List:
        cnt += 1
        cur = nice_data.lets_go(x.start)
        zx = DT.datetime.fromtimestamp(cur).strftime('%Y-%m-%d %H:%M:%S')
            # zx = d + DT.timedelta(hours=5,minutes=30)
        xx = int(zx[11:13])
        s = ''
        if(xx>12):
          s = " pm"
        else:
          s = " am"
        ans = str(xx%12)
        var = month[int(zx[5:7])-1] +" "+ zx[8:10] +", "+ zx[0:4]+" | "+ ans+zx[13:16]+s 
        per = x.duration
        hr = per//3600
        per = per % 3600
        mn = per//60
        mn = str(mn)
        if(len(mn) == 1):
          mn = '0'+mn
        ret = str(hr) + 'h ' + str(mn) + 'm'

        value=x.href
        em = '\N{EN SPACE}'
        sq = '\N{WHITE SQUARE WITH UPPER RIGHT QUADRANT}'
        desc = (f'`{em}{var}{em}|'
            f'{em}{ret}{em}|'
            f'{em}`[`link {sq}`]({value} "Link to contest page")')
        embed.add_field(
            name=x.event, value=desc, inline=False)



        if(cnt == 5):
            pagecnt+=1
            pages.append(embed)
            embed = discord.Embed(
                title="Future Contests", color=discord.Color.blue()
            )
            cnt = 0
    cnt = 1
    for x in pages:
      x.set_footer(text="Page "+str(cnt)+'/'+str(pagecnt-1))
      cnt+=1
    paginator.paginate(client,ctx.channel,pages)

@client.event
async def on_ready():
    # activity = discord.Game(name="codeforces.com", type=3)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="clist.by"))

keep_alive()
client.run(os.getenv('BOT_TOKEN'))
