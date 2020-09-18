import discord
import asyncio
from gtoken import retornatoken

comando = ["$turma entrar", "$turma sair", "$turma entrar", "$infos"]

client = discord.Client()

@client.event
async def on_ready():
    print('Rodando {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$turma add'):
        await message.channel.send('Esse comando permite que você adicione uma turma/cargo!')
    
    elif message.content.startswith('$exitTurma'):
        await message.channel.send('Esse comando permite que você  saia de uma turma/cargo que você está incluso!')
    
    elif message.content.startswith('$turma entrar'):
        embed1 = discord.Embed(
                    title="Escolha a turma que deseja entrar!",
                    color=0x690FC3,
                    description="- IHC = 🐤\n"
                        "- Grafos  =  📘 \n"
                        "- LIP-Rodrigo  = 📙",)

        botmsg = await message.channel.send(embed=embed1)
        await message   .add_reaction(botmsg, "🐤")
        await message.add_reaction("📘")
        await message.add_reaction("📙")

    elif message.content.startswith('$info'):
        await message.channel.send('O BODOC tem como objetivo reunir alunos das mesmas turmas ' +
        'facilitando assim a comunicação entre eles.')
        mensagem = "\nEsses são todos os comandos disponiveis:"
        for item in comando:
            if item == "$infos":
                mensagem += "\n" + item
            else:
                mensagem += "\n" + item + " nome_da_turma"
        await message.channel.send(mensagem)
        
client.run(retornatoken())