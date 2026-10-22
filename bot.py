import os
import discord
from discord.ext import commands
import random
# uprawnienia
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
intents.guilds = True
intents.bans = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}!")

# --- Powitaj ---
@bot.command()
async def powitaj(ctx):
    await ctx.send(f"Witajcie @everyone jak wam dzien mija mam nadzieje ze swietnie HPRBot górą")



# czesc
@bot.command()
async def cześć(ctx):
    await ctx.send(f"Cześć {ctx.author.name}")

# --- PA ---
@bot.command()
async def papa(ctx):
    await ctx.send(f"Papa {ctx.author.name}")

# --- REPO ---
@bot.command()
async def repo(ctx):
    await ctx.send(f"Link Do Repo HPRBota: https://github.com/tojaPOBO/HPRBot-V1.00")

# --- SHIP ---
@bot.command()
async def ship(ctx, member1: discord.Member, member2: discord.Member = None):
        
    procent = random.randint(0, 100)
    await ctx.send(f"Komena zrobiona dla żartu NIE BRAĆ NA POWAŻNIE")
    await ctx.send(f"Ship **{member1.display_name}** Z **{member2.display_name}** ma: **{procent}%**!")




# --- BAN ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Brak powody"):
    # Poprawiono powód na reason (zgodnie z parametrem funkcji)
    await member.ban(reason=reason)
    await ctx.send(f"Dostał Bana: **{member.name}** | Powód: {reason}")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do banowania!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Przykład użycia: `!ban @Użytkownik [powód]`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Nie znaleziono takiego użytkownika.")


# --- UNBAN ---
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, uzytkownik: str):
    bany = await ctx.guild.bans()

    for wpis in bany:
        user = wpis.user
        if user.name.lower() == uzytkownik.lower() or str(user.id) == uzytkownik:
            await ctx.guild.unban(user)
            await ctx.send(f"Użytkownik **{user.name}** został odbanowany.")
            return

    await ctx.send(f"Nie znaleziono zbanowanego użytkownika: `{uzytkownik}`")


# --- KICK ---
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Brak powody"):
    await member.kick(reason=reason)
    await ctx.send(f"Użytkownik **{member.name}** został wyrzucony | Powód: {reason}")


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do wyrzucania!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Przykład użycia: `!kick @Użytkownik [powód]`")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Nie znaleziono takiego użytkownika.")


# włąćzenie bota
TOKEN = os.getenv("DISCORD_TOKEN", "wklej tu swoj token bota")
bot.run(TOKEN)
