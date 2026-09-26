import os

import discord
import random

sad_words = ["sad", "depressed", "angry", "hurting", "stressed"]

encouragements = [
    "Cheer up! 😁🤗",
    "Hang in there 😉",
    "You are a great person! 👍",
    "Come on! You can do it! 💪",
    "Stay strong 🥰 "
]

happy_words = ["happy", "glad", "joyfull", "satisfied", "blessed"]

responses = [
    "There you go 👏",
    "Keep up the good work 👍",
    "Keep it up 🙌",
    "Good job 👍",
    "I’m so proud of you! 🥰"
]

songs = [
    f"https://www.youtube.com/watch?v=suwfJMiXauU",
    f"https://www.youtube.com/watch?v=DR43SQx8Ybc"
]

permissions = discord.Intents.default()
permissions.message_content = True
bot = discord.Client(intents=permissions)


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!hi"):
        await message.channel.send(f"Hello!")

    if message.content.startswith("w!hello"):
        await message.channel.send(
            f"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXJrYm02OWN4d29rZTRqNDA2YmRnaGlmNXI1a3A2ZXhqb2J3a3ozbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wkPBxvetT2UUqSukUE/giphy.gif"
        )

    if any(word in message.content for word in sad_words):
        response = random.choice(encouragements)
        await message.channel.send(response)

    if any(word in message.content for word in happy_words):
        response2 = random.choice(responses)
        await message.channel.send(response2)

    if message.content.startswith("!random song"):
        await message.channel.send(random.choice(songs))




bot.run(os.environ["TOKEN"])
