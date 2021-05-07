import requests
from bs4 import BeautifulSoup
import discord


client = discord.Client()


# When the bot declares itself as 'ready' for use
@client.event
async def on_ready():
    # Print to the console that the bot is logged on
    print("We have logged in as {0.user}".format(client))


# When a message is sent
@client.event
async def on_message(message):
    # Don't run any commands if the command is the bot itself
    if message.author == client.user:
        return

    # If the message (when converted to lower case) is !bbc, run the command
    if message.content.lower() == "!bbc":
        # Request BBC homepage and news for later use
        bbchome = requests.get("https://www.bbc.co.uk")
        bbchomesoup = BeautifulSoup(bbchome.text, "html.parser")
        bbcnews = requests.get("https://www.bbc.co.uk/news")
        bbcnewssoup = BeautifulSoup(bbcnews.text, "html.parser")

        # Scrape homepage to find the top story, and then assign variables
        topheadline = bbchomesoup.find(class_="ssrcss-egasky-Promo ett16tt0").find("p").find("span")
        topheadline = topheadline.text
        toplink = bbchomesoup.find(class_="ssrcss-egasky-Promo ett16tt0").find("a")
        toplink = toplink.get("href")

        # Scrape BBC News to find the most-read story, and then assign variables
        mostreadheadline = bbcnewssoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold"
                   " gs-u-pl-@xs").find("span")
        mostreadheadline = mostreadheadline.text
        mostreadlink = bbcnewssoup.find(
            class_="gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold"
                   " gs-u-pl-@xs")
        mostreadlink = "https://www.bbc.co.uk" + mostreadlink.get("href")

        # Send messages to channel where command was called
        await message.channel.send(f"**TOP STORY:** {topheadline}\n"
                                   f"{toplink}")
        await message.channel.send(f"**MOST READ STORY:** {mostreadheadline}\n"
                                   f"{mostreadlink}")

    # If the message (when converted to lower case) is !sport, run the command
    if message.content.lower() == "!sport":
        # Request BBC sports page for later use
        bbcsport = requests.get("https://www.bbc.co.uk/sport")
        bbcsportsoup = BeautifulSoup(bbcsport.text, "html.parser")

        # Scrape BBC Sports to find the top story, and then assign variables
        topsportheadline = bbcsportsoup.find(class_="gel-layout__item gel-3/4@xxl sp-o-keyline sp-o-no-keyline@m").find("h3")
        topsportheadline = topsportheadline.text
        topsportlink = bbcsportsoup.find(class_="gel-layout__item gel-3/4@xxl sp-o-keyline sp-o-no-keyline@m").find("a")
        topsportlink = "https://www.bbc.co.uk" + topsportlink.get("href")

        # Send message to where command was called
        await message.channel.send(f"**TOP SPORT STORY:** {topsportheadline}\n"
                                   f"{topsportlink}")

# Actually runs the bot with the unique token
client.run("TOKEN")
