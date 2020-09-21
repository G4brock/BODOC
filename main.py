import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from gtoken import retornatoken

comando = ["$turma entrar", "$turma sair", "$turma entrar", "$infos"]

client = discord.Client()

msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('Rodando {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fodase! turma add'):
        await message.channel.send('Esse comando permite que você adicione uma turma/cargo!')
    
    elif message.content.startswith('fodase! turma sair'):
        await message.channel.send('Esse comando permite que você  saia de uma turma/cargo que você está incluso!')
    
    elif message.content.startswith('fodase! turma entrar'):
        embed1 = discord.Embed(
                    title="Escolha a turma que deseja entrar!",
                    color=0x690FC3,
                    description="- IHC = 🐤\n"
                        "- Grafos  =  📘 \n"
                        "- LIP-Rodrigo  = 📙",)

        botmsg = await message.channel.send(embed=embed1)

        await message.add_reaction(botmsg, "🐤")
        await message.add_reaction("📘")
        await message.add_reaction("📙")

    elif message.content.startswith('fodase! info'):
        await message.channel.send('O BODOC tem como objetivo reunir alunos das mesmas turmas ' +
        'facilitando assim a comunicação entre eles.')
        mensagem = "\nEsses são todos os comandos disponiveis:"
        for item in comando:
            if item == "$infos":
                mensagem += "\n" + item
            else:
                mensagem += "\n" + item + " nome_da_turma"
        await message.channel.send(mensagem)
        
    global msg_id
    msg_id = botmsg.id
    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🐤" and msg.id == msg_id and user == msg_user:
        #role = discord.utils.find(lambda r: r.name == "IHC", msg.guild.roles)
        await user.add_roles(user,  (discord.role(id="IHC")))


    #elif reaction.emoji == "📘" and msg.id == msg.id and user == msg_user:
    #    role = discord.utils.find(lambda r: r.name == "Grafos", msg.server.roles)
    #    await client.add_roles(user, role)

    #elif reaction.emoji == "📙" and msg.id == msg.id and user == msg_user:
    #    role = discord.utils.find(lambda r: r.name == "LIP-Rodrigo", msg.server.roles)
    #    await client.add_roles(user, role)


#@client.event
#async def on_reaction_remove(reaction, user):
#    msg = reaction
#
#    if reaction.emoji == "🐤" and msg.id == msg.id and user == msg_user:
#        role = discord.utils.find(lambda r: r.name == "IHC", msg.server.roles)
#        await client.remove_roles(user, role)
#
#    elif reaction.emoji == "📘" and msg.id == msg.id and user == msg_user:
#        role = discord.utils.find(lambda r: r.name == "Grafos", msg.server.roles)
#        await client.remove_roles(user, role)
#
#    elif reaction.emoji == "📙" and msg.id == msg.id and user == msg_user:
#        role = discord.utils.find(lambda r: r.name == "LIP-Rodrigo", msg.server.roles)
#        await client.remove_roles(user, role)

client.run(retornatoken())