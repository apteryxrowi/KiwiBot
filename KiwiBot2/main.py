from typing import Final
from random import randint
import os
from dotenv import load_dotenv
import discord
from discord import Intents, Client, Message, app_commands
from responses import get_response

# Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup Bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)


# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('nuhuh, message empty, intents no enable')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# Handle Startup
@client.event
async def on_ready() -> None:
    await tree.sync(guild=discord.Object(id=1270019563785818214))
    print(f'{client.user} is ONLINE YEAHHHHH!')


# Commands
@tree.command(
    name="trigger",
    description="makes kiwi bot say something",
    guild=discord.Object(id=1270019563785818214)
)
async def trigger(interaction):
    await interaction.response.send_message(get_response('test'))


# @tree.command(
#     name="deletecommands",
#     description="deletus",
#     guild=discord.Object(id=1270019563785818214)
# )
# async def delete_commands(ctx):
#     tree.clear_commands(guild=None)
#     await tree.sync()
#     await ctx.response.send_message('Commands deleted.')


# Handle Incoming Messages
def no_punctuation(word: str) -> str:
    punc = '''!@#$%^&*(){}[]|?,.;'<>:"-=_+~`//\\'''
    for ele in word:
        if ele in punc:
            word = word.replace(ele, "")
    return word


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    with open('log.txt', 'a') as file:
        print(no_punctuation(user_message), file=file)
    if randint(1, 3) == 1:
        await send_message(message, user_message)


# Main Entry Point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
