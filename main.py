import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os
from settings import token
import subprocess

intents = discord.Intents.all()
prefix = '$'
client = commands.Bot(command_prefix=prefix, intents=intents)
token = token()

@client.event
async def on_ready():
  print(f'Zalogowano jako {client.user.name}#{client.user.discriminator}')

@client.command()
@has_permissions(administrator=True)
async def ls(ctx):
  resp = os.popen('ls').read()
  await ctx.send(f'```{resp}```')

@client.command()
@has_permissions(administrator=True)
async def cd(ctx, lokacja='None'):
  if lokacja == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $cd <scieżka>')
  else:
    os.system(f'cd {lokacja}')
    await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} **>>** Przeniosłeś do {lokacja}")

@client.command()
@has_permissions(administrator=True)
async def mkdir(ctx, lokacja='None'):
  if lokacja == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $mkdir <nazwa>')
  else:
    os.system(f'mkdir {lokacja}')
    await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} **>>** Stworzyłeś/aś folder {lokacja}")

@client.command()
@has_permissions(administrator=True)
async def ofile(ctx, file='None'):
  if file == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $ofile <nazwa>')
  else:
    f = open(file, "r")
    await ctx.send(f'```py\n{f.read()}\n```')


@client.command()
@has_permissions(administrator=True)
async def cat(ctx, file='None'):
  if file == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $cat <nazwa>')
  else:
    await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} **>>** Stworzyłeś plik {file}")
    os.system(f'touch -m {file}')


@client.command()
@has_permissions(administrator=True)
async def rm(ctx, file='None'):
  if file == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $rm <nazwa>')
  else:
    await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} **>>** Usunełeś plik/folder {file}")
    os.system(f'rm {file}')
    os.system(f'rm -r {file}')

@client.command()
@has_permissions(administrator=True)
async def wget(ctx, file='None'):
  if file == 'None':
    await ctx.send(f'{ctx.author.name}#{ctx.author.discriminator} **>>** Poprawne użycie: $wget <link>')
  else:
    await ctx.send(f"{ctx.author.name}#{ctx.author.discriminator} **>>** Pobrałeś/aś plik z linku!")
    os.system(f'wget {file}')
client.run(token)
