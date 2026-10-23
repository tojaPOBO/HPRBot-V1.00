import os
import discord
from discord.ext import commands
import random
import time
from discord import app_commands
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



# ----------------------- KOMENDY FOR FUN ------------------------
@bot.command()
async def cześć(ctx):
    await ctx.send(f"Cześć {ctx.author.name}")

@bot.command()
async def czesc(ctx):
    await ctx.send(f"Cześć {ctx.author.name}")
#PA 
@bot.command()
async def papa(ctx):
    await ctx.send(f"Papa {ctx.author.name}")

# REPO
@bot.command()
async def repo(ctx):
    await ctx.send(f"Link Do Repo HPRBota: https://github.com/tojaPOBO/HPRBot-V1.00")

#Fortune
@bot.command()
async def fortune(ctx):
    wybor = random.randint(0, 9)
    await ctx.send(f"OSOBY 1.Pobo 2.Hoper 3.Kuba 4.olek 5.kajtek 6.swiatas 7.wika 8.kinga 9.majka")
    time.sleep(3)
    await ctx.send(f"Losuje...")
    time.sleep(4)
    await ctx.send(f"Wybrano Osobe... {wybor} Brawo")
    
    

# SHIP
@bot.command()
async def ship(ctx, member1: discord.Member, member2: discord.Member = None):
        
    procent = random.randint(0, 101)
    await ctx.send(f"Komena zrobiona dla żartu NIE BRAĆ NA POWAŻNIE")
    await ctx.send(f"Ship **{member1.display_name}** Z **{member2.display_name}** ma: **{procent}%**!")

# --------------------------------------------------------


#--------------- KOMENDY MODERATORSKIE --------------

# BAN
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Brak powody"):
    
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


# UNBAN
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, uzytkownik: str):
    try:
        # Pobieramy bany jako generator asynchroniczny i zamieniamy je na listę
        bany = [wpis async for wpis in ctx.guild.bans()]
    except Exception as e:
        await ctx.send(f"❌ Błąd podczas pobierania banów: `{e}`")
        return

    uzytkownik = uzytkownik.strip()

    for wpis in bany:
        # Obsługa w zależności od struktury wpisu w tej wersji
        user = wpis.user if hasattr(wpis, 'user') else wpis[1]
        
        if str(user.id) == uzytkownik or user.name.lower() == uzytkownik.lower():
            try:
                await ctx.guild.unban(user)
                await ctx.send(f"Użytkownik **{user.name}** został odbanowany.")
                return
            except Exception as e:
                await ctx.send(f"❌ Wystąpił błąd przy odbanowywaniu: `{e}`")
                return

    await ctx.send(f"Nie znaleziono zbanowanego użytkownika: `{uzytkownik}`")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do odbanowywania użytkowników! (Wymagane: Ban Members)")



# KICK
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Brak powody"):
    await member.kick(reason=reason)
    await ctx.send(f"Użytkownik **{member.name}** został wyrzucony | Powód: {reason}")

# CLEAR

@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ilosc: int):
    if ilosc < 1:
        await ctx.send("Musisz usunąć 1 wiadomość", delete_after=5)
        return
        
    
    usniete = await ctx.channel.purge(limit=ilosc + 1)
    
    
    await ctx.send(f"Usunąlem {len(usniete) - 1} wiadomości.", delete_after=5)

@clear.error
async def clear_error(ctx, errord):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Musisz podać liczbę wiadomości do usuniecia Przykład: !clear 1`", delete_after=5)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie mozesz uzyc tej komendy", delete_after=5)



#-------------------------------------------------------------

# ------------------ OPCJE BOTA --------------------
TOKEN = os.getenv("DISCORD_TOKEN", "Daj tu token swojego bota")
bot.run(TOKEN)
