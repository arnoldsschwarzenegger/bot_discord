import discord
import random
from discord.ext import commands

komendy = ["?hello", "?heh", "?roll", "?help", "?kosze", "?zanieczyszczenia"] 

description = '''bot'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    """Bot introduction"""
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def help(ctx):
    await ctx.send(komendy)

async def on_message_edit(self, before, after):
        msg = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
        await before.channel.send(msg)

@bot.command()
async def kosze(ctx):
    await ctx.send(f'Żółty - metale i tworzywa sztuczne (puszki, butelki PET, opakowania plastikowe), Niebieski - papier (gazety, kartony, zeszyty), Brązowy - odpady biodegradowalne (resztki jedzenia, liście), Zielony - szkło (butelki, słoiki bez nakrętek), Czarny - odpady zmieszane (pozostałe śmieci nienadające się do recyklingu)')

@bot.command()
async def zanieczyszczenia(ctx):
    await ctx.send(f'ogrzewanie domów i innych budynków użytku publicznego - w tym wypadku mowa przede wszystkim o niskiej emisji, która związana jest z produkowaniem zanieczyszczeń przez domowe piece czy lokalne kotłownie. Spalanie niskiej jakości węgla, a także plastików i innych materiałów nieprzeznaczonych do tego powoduje przenikanie do atmosfery szkodliwych pyłów i gazów. Ta działalność człowieka w dużej mierze przyczynia się do powstawania smogu;, transport - duża ilość samochodów osobowych na drogach to kolejny czynnik przyczyniający się do zwiększonej ilości zanieczyszczeń powietrza. Warto również wspomnieć o transporcie lotniczym;  , przemysł chemiczny - chemia organiczna, czyli wytwarzanie produktów na bazie drewna, kauczuku, tłuszczów itp., a także chemia nieorganiczna, czyli wytwarzanie produktów powstałych z minerałów i rud,  przemysł rafineryjny - produkcja benzyny, paliw ropopochodnych i tworzyw sztucznych.')

bot.run("TOKEN")
