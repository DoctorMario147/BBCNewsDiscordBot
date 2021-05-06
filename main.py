import requests
from bs4 import BeautifulSoup
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == ("!bbc"):
        bbcnews = requests.get("https://www.bbc.co.uk/news")
        bbcsoup = BeautifulSoup(bbcnews.text, 'html.parser')

        headline = bbcsoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs").find(
            "span")
        headline = headline.text
        link = bbcsoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs")
        link = "https://www.bbc.co.uk" + link.get("href")


        await message.channel.send(f"**{headline}:** {link}")

client.run("TOKEN")