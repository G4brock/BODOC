import discord

comando = ["$turma entrar", "$turma sair", "$turma entrar", "$infos"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Turma'):
        await message.channel.send('Esse comando permite que você adicione uma turma/cargo!')
    
    elif message.content.startswith('$exitTurma'):
        await message.channel.send('Esse comando permite que você  saia de uma turma/cargo que você está incluso!')
    
    elif message.content.startswith('$turma entrar'):
        await message.channel.send('Esse comando permite que você entre em uma turma/cargo existente!')

    elif message.content.startswith('$info'):
        await message.channel.send('O BODOC tem como objetivo reunir alunos das mesmas turmas ' +
        'facilitando assim a comunicação entre eles.')
        mensagem = "Esses são todos os comandos disponiveis:"
        for item in comando:
            if item == "$infos":
                mensagem += "\n" + item
            else:
                mensagem += "\n" + item + " nome_da_turma"
        await message.channel.send(mensagem)

        
client.run('NzU2MjU5MDY2MTExNTkwNDMz.X2PPIw.y0J-AXu864Ro5gNmKmCiUxCYDv0')