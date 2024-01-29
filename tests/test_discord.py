import discord

client = discord.Client()


async def fix_get_build(*args, **kw):
    return 244594
discord.utils._get_build_number = fix_get_build


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

async def collect_messages(channel_id, limit=100):
    # Get the channel object
    channel = client.get_channel(channel_id)
    
    if not channel:
        print(f"Channel with ID {channel_id} not found.")
        return

    # Collect messages from the channel
    messages = []
    async for message in channel.history(limit=limit):
        messages.append(message.content)
    
    return messages

# Example usage:
@client.event
async def on_message(message):
    # Replace CHANNEL_ID with the actual channel ID you want to collect messages from
    channel_id = 267624335836053506
    collected_messages = await collect_messages(channel_id)

    # Do something with the collected messages (e.g., print them)
    print(collected_messages)

client.run('MjMwNzAxMDcyNjM5OTgzNjE3.GoTKMO.spgyb2cHbL85IbyPUY-h9Mu8ltGsLqURzDBGqc')