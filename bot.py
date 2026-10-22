import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Wymagane do działania komend na użytkownikach

bot = commands.Bot(command_prefix="!", intents=intents)


# Uruchomienie bota
@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}!")


# Powitane
@bot.command()
async def cześć(ctx):
    await ctx.send(f"Cześć {ctx.author.name}")


# BAN
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(
    ctx, member: discord.Member, *, powód="Brak powodu"
):
    await member.ban(reason=powód)
    await ctx.send(
        f"Dostał Bana: **{member.name}**  Ponieważ: {powód}"
    )


# Obsługa błędów dla komendy ban
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie mam uprawnien")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "Przykład użycia: !ban @Użytkownik powód`"
        )

# Unban

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, uzytkownik: str):
    bany = await ctx.guild.bans()

    for wpis in bany:
        user = wpis.user


        if (
            user.name.lower() == uzytkownik.lower()
            or str(user.id) == uzytkownik
        ):
            await ctx.guild.unban(user)
            await ctx.send(f"Użytkownik **{user.name}** Ma Unbana")
            return  # Kończymy działanie komendy, bo znaleźliśmy i odbanowaliśmy osobę

    await ctx.send(
        f" Nie znaleziono zbanowanego użytkownika: `{uzytkownik}`"
    )

# Kick

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member, *, powód="nie ma")
   await member.kick(reason=powód)
   await ctx.send(f"Użytkownik **{member.name}** Ma Kicka bo: {powód}")
   



TOKEN = "MTU2MjgwNzUwMjYzMzA1MDE5NA.G2VoiC.BmstpQ8RHvRMoWNW3RZq0CTdMWQbMwDA0ycmOg"
bot.run(TOKEN)