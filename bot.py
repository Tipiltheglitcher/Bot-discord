import discord
from discord import app_commands
from discord import embeds
from discord import interactions
from discord.colour import Color
from discord.ext import commands, tasks
from discord.interactions import Interaction
import discord.ui
import random
from datetime import datetime, timedelta
import datetime
import requests
import calendar
import time
import urllib.request
import urllib
from urllib.error import HTTPError
import json
from pymongo import MongoClient
from discord import ButtonStyle
import os
import aiohttp  # Added aiohttp import
import string
from pymongo import MongoClient
import calendar
import json
import time
import discord
from discord.ext import commands
from discord.ui import Button, View
import humanize
from typing import List
import asyncio
import subprocess
from flask import Flask

app = Flask(__name__)

web_message = "Hello, World!"
bot_loading_message = "Server is running..."

@app.route('/')
def home():
    return web_message

if __name__ == '__main__':
    print(f'\033[96m{bot_loading_message}\033[0m')  # Ajout de la couleur cyan
    app.run(port=3000)

# Lancer serveur.js
node_process = subprocess.Popen(['node', 'serveur.js'])

developer = [1094881932136943746]

ts = calendar.timegm(time.gmtime())

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="/", intents=intents)

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

funFact = ["tipil"]

bot_owner_ids = [905105350678675467]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        channel = bot.get_channel(1241320800867450910)
        if channel:
            embed = discord.Embed(
                title="Commande Introuvable",
                description=
                f"L'utilisateur {ctx.author.name} a tenté d'exécuter une commande invalide : `{ctx.message.content}`",
                color=discord.Color.red())
            await channel.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(
          activity=discord.Activity(
              type=discord.ActivityType.watching,
              name="la version 1.0",
          )
      )
    print(f'Bot connecté en tant que {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)

    try:
        synced = await bot.tree.sync()
        print(f"Commandes chargées: {len(synced)}")
    except Exception as e:
        print(e)


@bot.tree.command(name='help',
                  description='Cette commande affichfe la liste des commandes')
async def aide(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    embed = discord.Embed(title="Liste des commandes 📜",
                          description="Voici les commandes :",
                          color=discord.Color.gold())
    embed.add_field(name="/online",
                    value="Vérifie si le bot est en ligne.",
                    inline=False)
    embed.add_field(name="/login",
                    value="Permet de ce connecter à son compte  fortnite",
                    inline=False)
    embed.add_field(name="/logout",
        value="Permet de ce deconnecter de son compte  fortnite",
        inline=False)
    embed.add_field(
        name="/set-level",
        value=("Permet de changer de niveau (seulement visible au salon et vous ne "
               "voyez aucun changement, seulement les autres voient le changement)"),
        inline=False)
    embed.add_field(name="/fn-search",
        value="Permet de donné des information sur un cosmétique ",
        inline=False)
    embed.add_field(name="/gen-compte1",
        value="Permet de généré un compte (les compte sont uncheck) ",
        inline=False)
    embed.add_field(name="/gen-compte2",
        value="Permet de généré un compte (les compte sont uncheck, j'ai du en faire un 2eme car limite discord pour les option est de 25)",
        inline=False)
    embed.add_field(name="/stock",
         value="Permet de vérifié le stock du bot ",
         inline=False)
    embed.add_field(
        name="/lienserveur",
        value="Envoie le lien pour rejoindre le serveur du créateur ",
        inline=False)
    embed.add_field(name="/map",
         value="Permet d'affiché la map fortnite actuel ",
         inline=False)
    embed.add_field(name="/paypal",
        value="Permet de faire un don pour soutenir le créateur ",
        inline=False)
    embed.add_field(name="/ping",
         value="Permet de vérifié la latence du bot ",
          inline=False)
    embed.add_field(
        name="/suggestion",
        value="Permet de faire une suggestion (commandes, fonctionnalités...) ",
        inline=False)
    embed.add_field(name="/version",
        value="Permet de voir la version du bot ",
        inline=False)
    embed.add_field(name="/serverinfo",
        value="Dnne des informations su rle serveur",
        inline=False)
    embed.set_footer(text="le bot est mis à jour regulierement")  
    await interaction.response.send_message(embed=embed)

@bot.tree.command(
    name='version',
    description='Cette commande affiche les information du bot sur ça version')
async def version2(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    if not interaction:
        print("Interaction object not found")
        return

    embed = discord.Embed(
        title="voici des informations concernant la dernière version du bot",
        description="",
        color=discord.Color.purple())
    embed.add_field(name="Version :", value="1.0", inline=False)
    embed.add_field(name="Date de la dernière version ",
                    value="19/06/2024",
                    inline=False)
    embed.set_footer(text="le bot est mis à jour regulierement")

    button_support = Button(style=discord.ButtonStyle.link,
        label='Join The Support Server',
        url=INVITE_URL1,
        emoji='<a:UnrealFuf:1046126740428312636>')
    button_invite = Button(style=discord.ButtonStyle.link,
       label='Invite The Bot In Your Server',
       url=INVITE_URL2,
       emoji='<a:UnrealFuf:1159088142368915476> ')

    # Créez une View et ajoutez les deux boutons à cette View
    view = View()
    view.add_item(button_support)
    view.add_item(button_invite)
    
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='paypal',
                  description='Cette commande permet de soutenir le créateur')
async def paypal(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    embed = discord.Embed(
        type="rich",
        url="https://www.paypal.me/MathixTipil",
        title="Cliquez ici pour me soutenir dans le développement",
        description="⬆️⬆️⬆️")

    embed.set_thumbnail(
        url=
        ""
    )
    
    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name='lienserveur',
    description='Cette commande envoie le lien du serveur du créateur du bot')
async def link1(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    embed = discord.Embed(
        type="rich",
        url="https://discord.gg/kpkS848Zr3",
        title="Clic ici pour rejoindre le serveur du créateur",
        description="⬆️⬆️⬆️")
    embed.set_thumbnail(
        url=
        ""
    )

    button_support = Button(style=discord.ButtonStyle.link,
        label='Join The Support Server',
        url=INVITE_URL1,
        emoji='<a:UnrealFuf:1046126740428312636>')
    button_invite = Button(style=discord.ButtonStyle.link,
       label='Invite The Bot In Your Server',
       url=INVITE_URL2,
       emoji='<a:UnrealFuf:1159088142368915476> ')

    # Créez une View et ajoutez les deux boutons à cette View
    view = View()
    view.add_item(button_support)
    view.add_item(button_invite)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="set-level", description="Set a fake level")
async def level(interaction: discord.Interaction, level: str):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    try:
        # Récupération de accountId, secret et deviceId depuis MongoDB
        client = MongoClient(uri, connect=False)
        collection = client.ZapotronBot.deviceAuths
        user_data = collection.find_one({"discord_id": interaction.user.id})

        if not user_data:
            embed = discord.Embed(title="Error",
                                  description="You need to login first.",
                                  color=discord.Color.red())

            button_support = Button(style=discord.ButtonStyle.link,
                label='Join The Support Server',
                url=INVITE_URL1,
                emoji='<a:UnrealFuf:1046126740428312636>')
            button_invite = Button(style=discord.ButtonStyle.link,
               label='Invite The Bot In Your Server',
               url=INVITE_URL2,
               emoji='<a:UnrealFuf:1159088142368915476> ')

            # Créez une View et ajoutez les deux boutons à cette View
            view = View()
            view.add_item(button_support)
            view.add_item(button_invite)
            
            await interaction.response.send_message(embed=embed)
            return

        accountId = user_data['account_id']
        secret = user_data['secret']
        deviceId = user_data['device_id']
        display_name = user_data['display_name']

        # Construction de l'URL avec des paramètres de requête
        url = f"https://api-xji1.onrender.com/api/v2/party/level?accountId={accountId}&secret={secret}&deviceId={deviceId}&level={level}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()

                    # Création d'un embed
                    embed = discord.Embed(
                        title=f"Successfully set level to {level}",
                        color=discord.Color.green())
                    embed.set_thumbnail(
                        url=
                        "https://media.discordapp.net/attachments/894313949573554226/949095749180862544/checkmark.png?ex=6621b5cb&is=660f40cb&hm=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVheight=671"
                    )  # Placeholder image URL
                    embed.add_field(
                        name="",
                        value=f"Thanks for your participation {display_name}")
                    await interaction.response.send_message(embed=embed)
                else:
                    embed = discord.Embed(title="Error",
                                          description="Failed to set level.",
                                          color=discord.Color.red())

                    button_support = Button(style=discord.ButtonStyle.link,
                        label='Join The Support Server',
                        url=INVITE_URL1,
                        emoji='<a:UnrealFuf:1046126740428312636>')
                    button_invite = Button(style=discord.ButtonStyle.link,
                       label='Invite The Bot In Your Server',
                       url=INVITE_URL2,
                       emoji='<a:UnrealFuf:1159088142368915476> ')

                    # Créez une View et ajoutez les deux boutons à cette View
                    view = View()
                    view.add_item(button_support)
                    view.add_item(button_invite)
                    
                    await interaction.response.send_message(embed=embed)

    except Exception as e:
        print('Error:', e)
        embed = discord.Embed(
            title='Error',
            description=
            'Le nombre que vous avez inscrit dépasse la limite autoriser',
            color=discord.Color.red())

        button_support = Button(style=discord.ButtonStyle.link,
            label='Join The Support Server',
            url=INVITE_URL1,
            emoji='<a:UnrealFuf:1046126740428312636>')
        button_invite = Button(style=discord.ButtonStyle.link,
           label='Invite The Bot In Your Server',
           url=INVITE_URL2,
           emoji='<a:UnrealFuf:1159088142368915476> ')

        # Créez une View et ajoutez les deux boutons à cette View
        view = View()
        view.add_item(button_support)
        view.add_item(button_invite)
        
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="fn-search", description="Grab any cosmetics from Fortnite.")
async def search_dev(interaction: discord.Interaction, name: str):
    url = f"https://fortnite-api.com/v2/cosmetics/br/search?name={name}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 404:
                    embed = discord.Embed(
                        title="Ce n'était pas censé se produire",
                        description="Désolé je n'ai pas réussi à trouver l'objet que vous recherchez, veuillez vérifier l'orthographe et réessayer.",
                        color=0xff0000  # Rouge pour indiquer une erreur
                    )

                    button_support = Button(style=discord.ButtonStyle.link,
                        label='Join The Support Server',
                        url=INVITE_URL1,
                        emoji='<a:UnrealFuf:1046126740428312636>')
                    button_invite = Button(style=discord.ButtonStyle.link,
                       label='Invite The Bot In Your Server',
                       url=INVITE_URL2,
                       emoji='<a:UnrealFuf:1159088142368915476> ')

                    # Créez une View et ajoutez les deux boutons à cette View
                    view = View()
                    view.add_item(button_support)
                    view.add_item(button_invite)
                    
                    await interaction.response.send_message(embed=embed)
                    return

                if response.status != 200:
                    await interaction.response.send_message(f"Erreur: {response.status}")
                    return

                grabingJson = await response.json()

                if 'data' not in grabingJson:
                    await interaction.response.send_message("Erreur: données non trouvées.")
                    return

                data = grabingJson['data']
                cosmeticid = data.get('id', 'N/A')
                cosmeticname = data.get('name', 'N/A')
                cosmeticdescription = data.get('description', 'N/A')
                cosmetictype = data['type'].get('displayValue', 'N/A')
                cosmeticrarity = data['rarity'].get('displayValue', 'N/A')
                cosmeticimage = data['images'].get('icon', '')

                introduced_data = data.get('introduction', {})
                introduced_message = introduced_data.get('text', 'N/A')

                gameplay_tags = ", ".join(data.get('gameplayTags', []))
                showcase_video = data.get('showcaseVideo', 'N/A')

                embed = discord.Embed(
                    title=f"Cosmetic Information: {cosmeticname}",
                    description=f"ID: {cosmeticid}\nDescription: {cosmeticdescription}",
                    color=0x00ff00
                )

                embed.set_image(url=cosmeticimage)
                embed.add_field(name="Type", value=cosmetictype, inline=True)
                embed.add_field(name="Rarity", value=cosmeticrarity, inline=True)
                embed.add_field(name="Introduced", value=introduced_message, inline=False)
                embed.add_field(name="Gameplay Tags", value=gameplay_tags or 'N/A', inline=False)
                embed.add_field(name="Showcase Video", value=showcase_video, inline=False)

                button_support = Button(style=discord.ButtonStyle.link,
                    label='Join The Support Server',
                    url=INVITE_URL1,
                    emoji='<a:UnrealFuf:1046126740428312636>')
                button_invite = Button(style=discord.ButtonStyle.link,
                   label='Invite The Bot In Your Server',
                   url=INVITE_URL2,
                   emoji='<a:UnrealFuf:1159088142368915476> ')

                # Créez une View et ajoutez les deux boutons à cette View
                view = View()
                view.add_item(button_support)
                view.add_item(button_invite)
                
                await interaction.response.send_message(embed=embed)

        except aiohttp.ClientError as e:
            await interaction.response.send_message(f"Erreur: {e}")

@bot.tree.command(name='map', description='Display the Fortnite map')
async def fortnite_map(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    try:
        # Make request to the Fortnite API
        url = 'https://fortnite-api.com/v1/map'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()

                    # Get the map image URL
                    map_image_url = data['data']['images']['blank']

                    # Create an embed with the map image
                    embed = discord.Embed(title="Fortnite Map",
                                          color=discord.Color.green())
                    embed.set_image(url=map_image_url)

                    await interaction.response.send_message(embed=embed)
                else:
                    await interaction.response.send_message(
                        "Failed to fetch Fortnite map.")
    except Exception as e:
        print('Error:', e)

        button_support = Button(style=discord.ButtonStyle.link,
            label='Join The Support Server',
            url=INVITE_URL1,
            emoji='<a:UnrealFuf:1046126740428312636>')
        button_invite = Button(style=discord.ButtonStyle.link,
           label='Invite The Bot In Your Server',
           url=INVITE_URL2,
           emoji='<a:UnrealFuf:1159088142368915476> ')

        # Créez une View et ajoutez les deux boutons à cette View
        view = View()
        view.add_item(button_support)
        view.add_item(button_invite)
        
        await interaction.response.send_message(
            "An error occurred while fetching the Fortnite map.")

import discord
from discord.ext import commands
from discord.ui import Button, View

uri = "mongodb+srv://wny51:jr5wsa@cluster0.n7ppuyq.mongodb.net/?retryWrites=true&w=majority"

INVITE_URL1 = 'https://discord.gg/vNsN5zzwzc'

INVITE_URL2 = 'https://discord.com/oauth2/authorize?client_id=1227607886407139348&permissions=8&scope=bot'


@bot.tree.command(name='logout',
                  description='Logs out from your epic games account!')
async def logout(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    try:
        # Connect to MongoDB
        client = MongoClient(uri, connect=False)

        # Get the collection
        collection = client.ZapotronBot.deviceAuths

        # Find and delete the user's data from the collection
        result = collection.delete_one({"discord_id": interaction.user.id})

        embed = discord.Embed(title="Logout", color=discord.Color.green())
        if result.deleted_count > 0:
            embed.description = "You have been logged out successfully."
        else:
            embed.description = "You are not currently logged in."

        # Créer les boutons
        button_support = Button(style=discord.ButtonStyle.link,
                                label='Join The Support Server',
                                url=INVITE_URL1,
                                emoji='<a:UnrealFuf:1046126740428312636>')
        button_invite = Button(style=discord.ButtonStyle.link,
                               label='Invite The Bot In Your Server',
                               url=INVITE_URL2,
                               emoji='<a:UnrealFuf:1159088142368915476> ')

        # Créez une View et ajoutez les deux boutons à cette View
        view = View()
        view.add_item(button_support)
        view.add_item(button_invite)

        await interaction.response.send_message(embed=embed, view=view)
    except Exception as e:
        print('Error:', e)
        embed = discord.Embed(
            title="Error",
            description="An error occurred. Please try again.",
            color=discord.Color.red())
        await interaction.response.send_message(embed=embed)


@bot.tree.command(name='login',
                  description='Logins into your epic games account!')
async def login(interaction: discord.Interaction, authcode: str = None):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    try:
        if authcode is None:
            embed = discord.Embed(title="Login Step",
                                  description="",
                                  color=0x00ff00)
            embed.add_field(
                name="**step 1 :** ",
                value=
                "Login [here](https://www.epicgames.com/id/login)   <a:emoji_2:1227640300818661426> ",
                inline=False)
            embed.add_field(
                name="**step 2 :**",
                value=
                "Visit the [link here](https://www.epicgames.com/id/api/redirect?clientId=3f69e56c7649492c8cc29f1af08a8a12&responseType=code) above to get your login code.   :link: ",
                inline=False)
            embed.add_field(
                name="**step 3 :**",
                value=
                "You should see a code after `?code=` like the picture.<a:llama:1181943210713550930> ",
                inline=False)
            embed.set_image(
                url=
                "https://media.discordapp.net/attachments/971328290067456000/1005656280758767767/unknown.png"
            )
            embed.set_footer(
                text="/login and authcode",
                icon_url=
                "https://cdn.discordapp.com/app-icons/118044643767.png?size=64"
            )

            button_support = Button(style=discord.ButtonStyle.link,
                label='Join The Support Server',
                url=INVITE_URL1,
                emoji='<a:UnrealFuf:1046126740428312636>')
            button_invite = Button(style=discord.ButtonStyle.link,
               label='Invite The Bot In Your Server',
               url=INVITE_URL2,
               emoji='<a:UnrealFuf:1159088142368915476> ')

            # Créez une View et ajoutez les deux boutons à cette View
            view = View()
            view.add_item(button_support)
            view.add_item(button_invite)
            
            await interaction.response.send_message(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        f'https://api-xji1.onrender.com/oauth?authorization_code={authcode}'
                ) as response:
                    response_data = await response.json()

            # Extract data from the response
            access_token = response_data['access_token']
            account_id = response_data['account_id']
            display_name = response_data['display_name']
            refresh_token = response_data['refresh_token']
            device_id = response_data['device_id']
            secret = response_data['secret']
            icon_url = response_data['icon']

            # Connect to MongoDB
            client = MongoClient(uri, connect=False)

            # Get the collection
            collection = client.ZapotronBot.deviceAuths

            # Construct the data to write to MongoDB
            dataToWrite = {
                'access_token': access_token,
                'account_id': account_id,
                'display_name': display_name,
                'refresh_token': refresh_token,
                'device_id': device_id,
                'secret': secret,
                'icon': icon_url,
                'discord_id': interaction.user.id
            }

            # Insert the data into the collection
            collection.insert_one(dataToWrite)

            # Create an embedded message
            embed = discord.Embed(title='Successful Login!',
                                  description=f'Logged into {display_name}!',
                                  color=0x00FF00)
            embed.set_thumbnail(url=icon_url)
            embed.add_field(name='Account ID', value=account_id)

            # Send the embedded message
            await interaction.response.send_message(embed=embed)

    except KeyError as ke:
        print(f"KeyError: Missing key {ke}")
        icon_url = "https://cdn.discordapp.com/emojis/1198655012012826634.webp?size=128"
        embed = discord.Embed(title='Unable Login!',
                              description='Sorry please try in 5min!',
                              color=0xff0000)
        embed.set_thumbnail(url=icon_url)
        embed.add_field(
            name='get a new authcode',
            value=
            "[ :arrow_right: authcode:arrow_left:](https://rebrand.ly/authcode)"
        )


        await interaction.response.send_message(embed=embed)

    except Exception as e:
        print('Error:', e)
        icon_url = "https://cdn.discordapp.com/emojis/1198655012012826634.webp?size=128"
        embed = discord.Embed(title='Unable Login!',
                              description='Sorry please try in 5min!',
                              color=0xff0000)
        embed.set_thumbnail(url=icon_url)
        embed.add_field(
            name='get a new authcode',
            value=
            "[ :arrow_right: authcode:arrow_left:](https://rebrand.ly/authcode)"
        )
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name='online', description='Check if the bot is online')
async def online(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    try:
        # Check if interaction object exists
        if not interaction:
            print("Interaction object not found")
            return

        # Create an embed
        embed = discord.Embed(title="Bot Status",
                              description="The bot is online!",
                              color=discord.Color.green())

        button_support = Button(style=discord.ButtonStyle.link,
            label='Join The Support Server',
            url=INVITE_URL1,
            emoji='<a:UnrealFuf:1046126740428312636>')
        button_invite = Button(style=discord.ButtonStyle.link,
           label='Invite The Bot In Your Server',
           url=INVITE_URL2,
           emoji='<a:UnrealFuf:1159088142368915476> ')

        # Créez une View et ajoutez les deux boutons à cette View
        view = View()
        view.add_item(button_support)
        view.add_item(button_invite)
        
        await interaction.response.send_message(embed=embed)

    except Exception as e:
        print('Error:', e)  # Corrected code snippet


embed = discord.Embed(title="Bot Status",
                      description="The bot is online!",
                      color=discord.Color.green())


# Add fields to the embed
class MyClient(discord.Client):

    def __init__(self, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print('Logged on as', self.user)

    async def get_bot_response_time(self):
        start_time = time.time()
        end_time = time.time()
        return round((end_time - start_time) * 1000)

    async def get_api_response_time(self):
        start_time = time.time()
        end_time = time.time()
        return round((end_time - start_time) * 1000)

    async def get_database_response_time(self):
        start_time = time.time()
        end_time = time.time()
        return round((end_time - start_time) * 1000)

# Intents nécessaires pour le bon fonctionnement de votre bot
intents = discord.Intents.default()


@bot.tree.command(name='ping', description='check latence of bot')
async def ping(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    start_time = time.time()
    client = MyClient(intents)
    bot_response_time = await client.get_bot_response_time()
    api_response_time = await client.get_api_response_time()
    database_response_time = await client.get_database_response_time()
    end_time = time.time()

    embed = discord.Embed(title="Pong! 🏓",
                          description=" ",
                          color=discord.Color.blue())
    embed.add_field(name="Bot Response Time",
                    value=f"{bot_response_time} ms",
                    inline=False)
    embed.add_field(name="API Response Time",
                    value=f"{api_response_time} ms",
                    inline=True)
    embed.add_field(name="Database Response Time",
                    value=f"{database_response_time} ms",
                    inline=True)

    button_support = Button(style=discord.ButtonStyle.link,
        label='Join The Support Server',
        url=INVITE_URL1,
        emoji='<a:UnrealFuf:1046126740428312636>')
    button_invite = Button(style=discord.ButtonStyle.link,
       label='Invite The Bot In Your Server',
       url=INVITE_URL2,
       emoji='<a:UnrealFuf:1159088142368915476> ')

    # Créez une View et ajoutez les deux boutons à cette View
    view = View()
    view.add_item(button_support)
    view.add_item(button_invite)
    
    await interaction.response.send_message(embed=embed)

    total_time = round((end_time - start_time) * 1)
    user_name = f'{interaction.user.name}#{interaction.user.discriminator}'
    guild_name = interaction.guild.name if interaction.guild else "N/A"
    print(
        f'Commande Ping exécutée par {user_name} sur le serveur {guild_name} en {total_time} ms'
    )


suggestion = []
suggestions = []


@bot.tree.command(name='suggestion', description='propose une suggestion')
async def suggest(interaction: discord.Interaction, suggestion: str):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    
    if not suggestion:

        await interaction.response.send_message(
            'Veuillez mettre une suggestion')

        return

    suggestions.append({
        'author': interaction.user.name,
        'suggestion': suggestion,
    })

    button_support = Button(style=discord.ButtonStyle.link,
        label='Join The Support Server',
        url=INVITE_URL1,
        emoji='<a:UnrealFuf:1046126740428312636>')
    button_invite = Button(style=discord.ButtonStyle.link,
       label='Invite The Bot In Your Server',
       url=INVITE_URL2,
       emoji='<a:UnrealFuf:1159088142368915476> ')

    # Créez une View et ajoutez les deux boutons à cette View
    view = View()
    view.add_item(button_support)
    view.add_item(button_invite)
    
    await interaction.response.send_message('Merci pour votre suggestion!')
    await bot.get_channel(1229020544884805703).send(
        f"Nouvelle suggestion de {interaction.user.name} : {suggestion}")
        
@bot.tree.command(name="serverinfo", description="Affiche les informations du serveur")
async def serveurinfo(interaction: discord.Interaction):
        user_id = interaction.user.id
        if user_id not in developer:
            await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande.")
            return

        guild = interaction.guild
        server_name = guild.name
        server_id = guild.id
        member_count = guild.member_count
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        created_at = guild.created_at.strftime("%d/%m/%Y")
        owner = guild.owner
        icon_url = guild.icon.url if guild.icon else None
        verification_level = guild.verification_level
        explicit_content_filter = guild.explicit_content_filter
        afk_timeout = guild.afk_timeout
        afk_channel = guild.afk_channel
        system_channel = guild.system_channel

        embed = discord.Embed(title=f"Informations sur le serveur {server_name}", color=discord.Color.blue())
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name="Nom du serveur", value=server_name, inline=False)
        embed.add_field(name="ID du serveur", value=server_id, inline=False)
        embed.add_field(name="Propriétaire", value=str(owner), inline=False)
        embed.add_field(name="Membres", value=member_count, inline=False)
        embed.add_field(name="Canaux texte", value=text_channels, inline=False)
        embed.add_field(name="Canaux vocaux", value=voice_channels, inline=False)
        embed.add_field(name="Date de création", value=created_at, inline=False)
        embed.add_field(name="Niveau de vérification", value=verification_level, inline=False)
        embed.add_field(name="Filtre de contenu explicite", value=explicit_content_filter, inline=False)
        embed.add_field(name="Délai d'inactivité", value=f"{afk_timeout} secondes", inline=False)
        embed.add_field(name="Canal d'inactivité", value=afk_channel, inline=False)
        embed.add_field(name="Canal système", value=system_channel, inline=False)

        await interaction.response.send_message(embed=embed)
        
@bot.tree.command(name="site-web-tipil", description="donne le lien ver le site du createur du bot")
async def website(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message("Les commande ne peuvent pas être exécuté en mp.")
        return
    embed = discord.Embed(
        type="rich",
        url="https://tipil-web.netlify.app/",
        title="Site internet du createur ici",
        description="", color=discord.Color.green())

    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/1278834318688391191/1278841567435821127/th.png?ex=66d24585&is=66d0f405&hm=24e8ec48b5d281f1926b8d9d8bfe39681d74070c00111ad124e5664214fed093&=&format=webp&quality=lossless&width=565&height=565"
    )
    await interaction.response.send_message(embed=embed)

bot.run(
    "MTIyNzYwNzg4NjQwNzEzOTM0OA.G0Zh96.en6weP8vYnH-eHduiPStgXeeOLIPm0qrKTS6nA")
