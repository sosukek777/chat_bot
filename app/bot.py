from twitchio.ext import commands
from twitchio.client import Client
import os

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    #nick='fortnite_bot',
    prefix='!',
    initial_channels=[os.environ['CHANNEL']],
)


# client = Client(
#     client_id=os.environ['TWITCH_CLIENT_ID'],
#     client_secret=os.environ['TWITCH_CLIENT_SECRET'],
# )


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("this is a test response")

if __name__ == '__main__':
    bot.run()