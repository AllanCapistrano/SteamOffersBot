# Mensagens para quando não existem promoções ou jogos em destaque.
def noOffers():
    msgList = []

    msgList.append(
        "😟 **Nenhum destaque encontrado no momento, tente novamente mais tarde!**")
    msgList.append(
        "😟 **Nenhuma promoção encontrada no momento, tente novamente mais tarde!**")

    return msgList

# Mensagem para as promoções que são enviadas para o privado.
def checkDm():
    return "** Cheque sua DM** 😃"

# Títulos das embeds.
def title():
    titleList = []

    titleList.append("Aqui está o link para o convite:")
    titleList.append("🎮 Jogo/Evento em Destaque 🎮")
    titleList.append("🕹️ Oferta do Dia 🕹️")
    titleList.append("📊 Informações 📊")

    return titleList

# Alerta dos valores exibidos.
def currencyAlert():
    return "⚠️Atenção, os preços estão em Dólar"

# Conteúdo do comando $help.
def helpValues():
    msgList = []

    msgList.append(
        "**Exibe quais jogos estão na promoção diária da Steam ou gratuitos por um tempo limitado.**")
    msgList.append(
        "**Exibe os eventos que estão em destaque na Steam, ou os jogos em promoção que estão em destaque na loja.**")
    msgList.append(
        "**Exibe quais jogos da categoria \"Novidades Populares\" estão em promoção na loja.**")
    msgList.append(
        "**Exibe quais jogos da categoria \"Mais Vendidos\" estão em promoção na loja.**")
    msgList.append(
        "**Exibe quais jogos da categoria \"Mais Jogados\" estão em promoção na loja.**")
    msgList.append(
        "**Exibe quais jogos da categoria \"Pré-compra\" estão em promoção na loja.**")
    msgList.append(
        "**Gera o convite para que o Bot possa ser adicionado em outros servidores.**")
    msgList.append("**Exibe as informações do Bot.**")

    return msgList

# Conteúdo do comando $botinfo.
def infoValues():
    msgList = []

    msgList.append("**3.8.5**")
    msgList.append("**1.4.1**")
    msgList.append("**Bot feito para notificar os jogos que estão em promoção," 
      "sem a necessidade de abrir a Steam ou sair do Discord. Criado por ArticZ#1081**")

    return msgList