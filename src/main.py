import asyncio
import discord
import time

from myUtils.catch_offers import CatchOffers
from myUtils import messages
from myUtils import discordToken

AUTHOR_ICON = "https://cdn.discordapp.com/avatars/259443927441080330/a_b3fd4c5cfda6b7ad19bcf212a549fed5.png"
COLOR = 0xa82fd2
ICON = "https://cdn.discordapp.com/app-icons/714852360241020929/b8dcc72cfc7708a4efd31787dceb5350.png?size=64"
INVITE = "https://discord.com/oauth2/authorize?client_id=714852360241020929&scope=bot&permissions=485440"
URL = "https://store.steampowered.com/specials?cc=br#p=0&tab="
TOKEN = discordToken.myToken()

client = discord.Client()
catchOffers = CatchOffers()


@client.event
async def on_ready():
    numServers = len(client.guilds)

    print("\n{} está online em {} servidores".format(client.user.name, numServers))

    game = discord.Game("Online em {} Servidores".format(numServers))
    online = discord.Status.online

    await client.change_presence(status=online, activity=game)


@client.event
async def on_message(message):
    # Comando: $help ou $ajuda ou $comandos
    if(message.content.lower().startswith("$help") or message.content.lower().startswith("$ajuda") or message.content.lower().startswith("$comandos")):
        help_ = message.content.split(" ")

        if(len(help_) != 2):
            embedHelp = discord.Embed(
                color = COLOR
            )
            embedHelp.set_author(
                name = "SteamOffersBot lista de comandos:", icon_url=ICON)
            embedHelp.add_field(name="```$promocao``` ou ```$pr```",
                                value=messages.helpValues()[0], inline=False)
            embedHelp.add_field(name="```$destaque``` ou ```$dt```",
                                value=messages.helpValues()[1], inline=False)
            embedHelp.add_field(name="```$novidades``` ou ```$populares``` ou ```$np```",
                                value=messages.helpValues()[2], inline=False)
            embedHelp.add_field(name="```$maisvendidos``` ou ```$mv```",
                                value=messages.helpValues()[3], inline=False)
            embedHelp.add_field(name="```$maisjogados``` ou ```$mj```",
                                value=messages.helpValues()[4], inline=False)
            embedHelp.add_field(name="```$precompra``` ou ```$pc```",
                                value=messages.helpValues()[5], inline=False)
            embedHelp.add_field(name="```$convite```",
                                value=messages.helpValues()[6], inline=False)
            embedHelp.add_field(name="```$botinfo```",
                                value=messages.helpValues()[7], inline=False)
            embedHelp.add_field(name="```$game [nome do jogo]```",
                                value=messages.helpValues()[8], inline=False)
            embedHelp.add_field(name="```$genre [gênero do jogo]```",
                                value=messages.helpValues()[9], inline=False)

            await message.channel.send(embed=embedHelp)
        else:
            # $help genre
            if(help_[1] == "genre"):
                embedHelp = discord.Embed(
                    title = messages.title()[4],
                    color = COLOR,
                )
                embedHelp.add_field(name=messages.emojisGameGenres()[0], value=messages.gameGenres()[0], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[1], value=messages.gameGenres()[1], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[2], value=messages.gameGenres()[2], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[3], value=messages.gameGenres()[3], inline=False)
                embedHelp.add_field(name=messages.emojisGameGenres()[4], value=messages.gameGenres()[4], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[5], value=messages.gameGenres()[5], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[6], value=messages.gameGenres()[6], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[7], value=messages.gameGenres()[7], inline=False)
                embedHelp.add_field(name=messages.emojisGameGenres()[8], value=messages.gameGenres()[8], inline=True)
                embedHelp.add_field(name=messages.emojisGameGenres()[9], value=messages.gameGenres()[9], inline=True)
                embedHelp.set_footer(text="Utilize $genre [um dos gêneros acima]")

                await message.channel.send(embed=embedHelp)
            else:
                await message.channel.send(messages.commandAlert()[2])

    # Comando: $convite
    if(message.content.lower().startswith("$convite")):
        embedInvite = discord.Embed(
            title=messages.title()[0],
            color=COLOR,
            description='**{}**'.format(INVITE)
        )
        embedInvite.set_thumbnail(url=ICON)

        await message.channel.send(embed=embedInvite)

    # Comando: $destaque ou $dt
    if(message.content.lower().startswith("$destaque") or message.content.lower().startswith("$dt")):
        list_gamesURl, list_gamesIMG, list_H2 = catchOffers.getSpotlightOffers()
        x = len(list_gamesURl)

        if(x == 0):
            await message.channel.send(messages.noOffers()[0])

        else:
            while(x > 0):
                embedSpotlightGames = discord.Embed(
                    title=messages.title()[1],
                    color=COLOR
                )
                embedSpotlightGames.set_image(url=list_gamesIMG[x - 1])
                embedSpotlightGames.add_field(
                    name="**Link:**", value="**[Clique Aqui]({})**".format(list_gamesURl[x - 1]), inline=False)
                embedSpotlightGames.add_field(
                    name="**Descrição:**", value="**{}**".format(list_H2[x - 1]), inline=False)

                await message.channel.send(embed=embedSpotlightGames)

                x = x - 1

    # Comando: $promocao ou $pr
    if(message.content.lower().startswith("$promocao") or message.content.lower().startswith("$pr")):
        list_gamesURl, list_gamesIMG = catchOffers.getDailyGamesOffers()
        list_gamesOP, list_gamesFP = catchOffers.getDailyGamesOffersPrices()
        x = len(list_gamesURl)

        if(x == 0):
            await message.channel.send(messages.noOffers()[1])

        else:
            while(x > 0):
                embedDailyGames = discord.Embed(
                    title=messages.title()[2],
                    color=COLOR
                )
                embedDailyGames.set_image(url=list_gamesIMG[x - 1])
                embedDailyGames.add_field(
                    name="**Link:**", value="**[Clique Aqui]({})**".format(list_gamesURl[x - 1]), inline=False)
                embedDailyGames.add_field(
                    name="**Preço Original:**", value="**{}**".format(list_gamesOP[x - 1]), inline=True)
                embedDailyGames.add_field(
                    name="**Preço com Desconto:**", value="**{}**".format(list_gamesFP[x - 1]), inline=True)

                await message.channel.send(embed=embedDailyGames)
                x = x - 1

    # Comando: $botinfo
    if(message.content.lower().startswith("$botinfo")):
        embedBotInfo = discord.Embed(
            title=messages.title()[3],
            color=COLOR
        )
        embedBotInfo.set_thumbnail(url=ICON)
        embedBotInfo.add_field(name="Python", value=messages.infoValues()[0], inline=True)
        embedBotInfo.add_field(name="discord.py", value=messages.infoValues()[1], inline=True)
        embedBotInfo.add_field(name="Sobre SteamOffersBot", value=messages.infoValues()[2], inline=False)
        embedBotInfo.set_author(name="ArticZ#1081", icon_url=AUTHOR_ICON)
        embedBotInfo.set_footer(text="Criado em 26 de Maio de 2020! | Última atualização em {}."
            .format(messages.infoValues()[3]))

        await message.channel.send(embed=embedBotInfo)

    # Comando: $novidades ou $populares ou $np
    if(message.content.lower().startswith("$novidades") or message.content.lower().
      startswith("$populares") or message.content.lower().startswith("$np")):
        list_gamesNames, list_gamesURL, list_gamesOriginalPrice, list_gamesFinalPrice, list_gamesIMG = catchOffers.getTabContent(URL+'=NewReleases', 'NewReleasesRows')
        
        list_gamesNames.reverse(), list_gamesURL.reverse(
        ), list_gamesOriginalPrice.reverse(), list_gamesFinalPrice.reverse()
        num = x = len(list_gamesNames)

        if(x == 0):
            await message.channel.send(messages.noOffers()[1])

        else:
            messageConcat_1 = ''
            messageConcat_2 = ''
            member = message.author
            while(x > 0):
                if(x >= num/2):
                    messageConcat_1 = messageConcat_1 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                else:
                    messageConcat_2 = messageConcat_2 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                x = x - 1

            await message.channel.send(member.mention + messages.checkDm())
            await member.send(messageConcat_1)
            await member.send(messageConcat_2)

    # Comando: $maisvendidos ou $mv
    if(message.content.lower().startswith("$maisvendidos") or message.content.lower().startswith("$mv")):
        list_gamesNames, list_gamesURL, list_gamesOriginalPrice, list_gamesFinalPrice, list_gamesIMG = catchOffers.getTabContent(URL+'=TopSellers', 'TopSellersRows')
        
        list_gamesNames.reverse(), list_gamesURL.reverse(
        ), list_gamesOriginalPrice.reverse(), list_gamesFinalPrice.reverse()
        num = x = len(list_gamesNames)

        if(x == 0):
            await message.channel.send(messages.noOffers()[1])

        else:
            messageConcat_1 = ''
            messageConcat_2 = ''
            member = message.author
            while(x > 0):
                if(x >= num/2):
                    messageConcat_1 = messageConcat_1 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                else:
                    messageConcat_2 = messageConcat_2 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                x = x - 1

            await message.channel.send(member.mention + messages.checkDm())
            await member.send(messageConcat_1)
            await member.send(messageConcat_2)

    # Comando: $maisjogados ou $mj
    if(message.content.lower().startswith("$maisjogados") or message.content.lower().startswith("$mj")):
        list_gamesNames, list_gamesURL, list_gamesOriginalPrice, list_gamesFinalPrice, list_gamesIMG = catchOffers.getTabContent(URL+'=ConcurrentUsers', 'ConcurrentUsersRows')
        
        list_gamesNames.reverse(), list_gamesURL.reverse(
        ), list_gamesOriginalPrice.reverse(), list_gamesFinalPrice.reverse()
        num = x = len(list_gamesNames)

        if(x == 0):
            await message.channel.send(messages.noOffers()[1])

        else:
            messageConcat_1 = ''
            messageConcat_2 = ''
            member = message.author
            while(x > 0):
                if(x >= num/2):
                    messageConcat_1 = messageConcat_1 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                else:
                    messageConcat_2 = messageConcat_2 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                x = x - 1

            await message.channel.send(member.mention + messages.checkDm())
            await member.send(messageConcat_1)
            await member.send(messageConcat_2)

    # Comando: $precompra ou $pc
    if(message.content.lower().startswith("$precompra") or message.content.lower().startswith("$pc")):
        list_gamesNames, list_gamesURL, list_gamesOriginalPrice, list_gamesFinalPrice, list_gamesIMG = catchOffers.getTabContent(URL+'=ComingSoon', 'ComingSoonRows')
        
        list_gamesNames.reverse(), list_gamesURL.reverse(
        ), list_gamesOriginalPrice.reverse(), list_gamesFinalPrice.reverse()
        num = x = len(list_gamesNames)

        if(x == 0):
            await message.channel.send(messages.noOffers()[1])

        else:
            messageConcat_1 = ''
            messageConcat_2 = ''
            member = message.author
            while(x > 0):
                if(x >= num/2):
                    messageConcat_1 = messageConcat_1 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                else:
                    messageConcat_2 = messageConcat_2 + "**Nome: **" + list_gamesNames[x - 1] + "\n**Link:** <" + list_gamesURL[x - 1] + ">" + \
                        "\n**Preço Original: **" + \
                        list_gamesOriginalPrice[x - 1] + "\n**Preço com Desconto: **" + \
                        list_gamesFinalPrice[x - 1] + "\n\n"
                x = x - 1

            await message.channel.send(member.mention + messages.checkDm())
            await member.send(messageConcat_1)
            await member.send(messageConcat_2)

    # Comando: $game
    if(message.content.lower().startswith("$game")):
        gameName = message.content.split("$game ")

        if(len(gameName) == 1):
            await message.channel.send(messages.commandAlert()[0])
        else:
            gameName, gameURL, gameIMG, gamePrice, searchUrl = catchOffers.getSpecificGame(gameName[len(gameName) - 1])

            if(gameName != None):
                embedSpecificGame =  discord.Embed(
                    title="👾 Jogo: {} 👾".format(gameName),
                    color=COLOR
                )

                embedSpecificGame.set_image(url=gameIMG)
                embedSpecificGame.add_field(
                    name="**Link:**", value="**[Clique Aqui]({})**".format(gameURL), inline=False)

                if(len(gamePrice) > 1):
                    embedSpecificGame.add_field(
                        name="**Preço Original:**", value="**{}**".format(gamePrice[0]), inline=True)
                    embedSpecificGame.add_field(
                        name="**Preço com Desconto:**", value="**{}**".format(gamePrice[1]), inline=True)
                else:
                    embedSpecificGame.add_field(
                        name="**Preço:**", value="**{}**".format(gamePrice[0]), inline=False)

                embedSpecificGame.add_field(
                    name="**Obs:**", value=messages.wrongGame(searchUrl), inline=False)

                await message.channel.send(embed=embedSpecificGame)
            
            else:
                await message.channel.send(messages.noOffers()[2])

    # Comando: $genre
    if(message.content.lower().startswith("$genre")):
        gameGenre = message.content.split("$genre ")

        if(len(gameGenre) == 1):
            await message.channel.send(messages.commandAlert()[1])
        else:
            gameName, gameURL, gameOriginalPrice , gameFinalPrice, gameIMG = catchOffers.getGameRecommendationByGenre(gameGenre[1])

            if(gameName != None):
                embedGameRecommendation = discord.Embed(
                    title = messages.title(gameGenre[1])[5],
                    color = COLOR
                )
                embedGameRecommendation.set_image(url=gameIMG)
                embedGameRecommendation.add_field(
                    name="**Nome:**", value="**{}**".format(gameName), inline=False)
                embedGameRecommendation.add_field(
                    name="**Link:**", value="**[Clique Aqui]({})**".format(gameURL), inline=False)

                if(gameOriginalPrice == gameFinalPrice and gameOriginalPrice != "Gratuiro p/ Jogar"):
                    embedGameRecommendation.add_field(
                    name="**Preço:**", value="**{}**".format(gameOriginalPrice), inline=True)
                else:
                    if(gameOriginalPrice != "Gratuiro p/ Jogar"):
                        embedGameRecommendation.add_field(
                            name="**Preço Original:**", value="**{}**".format(gameOriginalPrice), inline=True)
                        embedGameRecommendation.add_field(
                            name="**Preço com Desconto:**", value="**{}**".format(gameFinalPrice), inline=True)
                    else:
                        embedGameRecommendation.add_field(
                            name="**Preço:**", value="**{}**".format(gameOriginalPrice), inline=True)

                await message.channel.send(embed = embedGameRecommendation)
            else:
                await message.channel.send(messages.noOffers()[3])


# Mudar o Status do bot automaticamente e de forma aleatória.
async def changeStatus():
    await client.wait_until_ready()
    await asyncio.sleep(20)
    
    while not client.is_closed():
        numServers = len(client.guilds)
        msgStatus = messages.status(numServers)
        randomStatus = messages.randomMessage(msgStatus, len(msgStatus))
        game = discord.Game(randomStatus)
        online = discord.Status.online

        await client.change_presence(status=online, activity=game)
        await asyncio.sleep(20)


client.loop.create_task(changeStatus())

client.run(TOKEN)