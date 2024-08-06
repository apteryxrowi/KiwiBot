from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Setup Bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


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
    print(f'{client.user} is ONLINE YEAHHHHH!')


# Handle Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Main Entry Point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
