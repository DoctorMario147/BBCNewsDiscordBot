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
        bbchome = requests.get("https://www.bbc.co.uk")
        bbchomesoup = BeautifulSoup(bbchome.text, "html.parser")
        bbcnews = requests.get("https://www.bbc.co.uk/news")
        bbcnewssoup = BeautifulSoup(bbcnews.text, "html.parser")

        topheadline = bbchomesoup.find(class_="ssrcss-egasky-Promo ett16tt0").find("p").find("span")
        topheadline = topheadline.text
        toplink = bbchomesoup.find(class_="ssrcss-egasky-Promo ett16tt0").find("a")
        toplink = toplink.get("href")

        mostreadheadline = bbcnewssoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs").find(
            "span")
        mostreadheadline = mostreadheadline.text
        mostreadlink = bbcnewssoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs")
        mostreadlink = "https://www.bbc.co.uk" + mostreadlink.get("href")


        await message.channel.send(f"**TOP STORY:** {topheadline}\n"
                                   f"{toplink}")
        await message.channel.send(f"**MOST READ STORY:** {mostreadheadline}\n"
                                   f"{mostreadlink}")

client.run("TOKEN")
