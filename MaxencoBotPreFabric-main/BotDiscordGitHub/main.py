import discord
from discord.ext import commands

token = "Veuillez mettre le token de votre bot ici"

bot = commands.Bot(command_prefix="#" ,description = "Pré-terminé")
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Bot by Maxenco----------------------------Bot démarré avec succés ! (token: {token}")
    await bot.change_presence(activity=discord.Game(name="Bot By Maxenco | #help"))

@bot.command()
async def bonjour(ctx):
	await ctx.send("Bonjour ! :wave:")

@bot.command()
async def repeat(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def style(ctx, *text):
	chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))

@bot.command()
async def clear(ctx, nombre : int):
    await ctx.channel.purge(limit = nombre + 1)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f"{member} à été kick avec succés avec comme raison: {reason}")
	print(f"{member} à été kick pour la raison: {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f"{member} à été unban avec succés")
			return
	await ctx.send(f"{member} n'est pas dans la liste de bans")

		


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f"{member} à été banni avec succés avec comme raison: {reason}")
	print(f"{member} à été banni pour la raison: {raison}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Muted")

		for channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

	await member.add_roles(mutedRole, reason=reason)
	await ctx.send(f"{member} à été mute avec succés avec comme raison: {reason}")
	await member.send(f"Vous avez été mute dans le serveur Pc server pour comme raison {reason}. Réfléchissez la prochaine fois...")
	await member.remove_roles(memberRole)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
	memberRole = discord.utils.get(ctx.guild.roles, name="Membre")

	await member.remove_roles(mutedRole)
	await member.add_roles(memberRole)
	await ctx.send(f"{member} à été unmute")
	await member.send(f"Vous avez été unmute du server Pc server")

@bot.command()
async def serverinfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Ce serveur ({serverName}) contient {numberOfPerson} personnes. \n La description du serveur {serverName} est: {serverDescription}. \n Ce serveur possède {numberOfTextChannels} salons écrit ainsi que {numberOfVoiceChannels} vocaux"
	await ctx.send(message)

@bot.command(pass_context=True)
async def credit(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.set_author(name='Crédits :')
	embed.add_field(name='Développeur :', value="Maxenco (<maxenco/>#5303)", inline=False)
	embed.add_field(name='Crée en :', value="Python (discord.py)", inline=False)
	embed.add_field(name='Avec des idées de :', value="Arion", inline=False)
	embed.add_field(name='Logiciels utilisés :', value="Sublime Text 3 et Visual Studio Code", inline=False)
	embed.add_field(name='Chaine Youtube Développeur :', value="https://www.youtube.com/channel/UC0aPZGrfkHAM2zEf_UN7ONQ", inline=False)
	embed.add_field(name='Chaine Youtube Arion :', value="https://www.youtube.com/channel/UCms-zMqD0M7hU70F6Ty6_jw", inline=False)

	await ctx.send(author, embed=embed)	

@bot.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.red()
	)

	embed.set_author(name='Commandes du bot :')
	embed.add_field(name='#bonjour', value="Il  te dira bonjour", inline=False)
	embed.add_field(name='#repeat', value="Il répetera ce que tu diras", inline=False)
	embed.add_field(name='#style', value="Il répétera ce que tu diras mais en caractères spéciaux", inline=False)
	embed.add_field(name='#clear', value="(ADMIN) Il effacera le nombre de message demandé", inline=False)
	embed.add_field(name='#kick', value="(ADMIN) Cette commande kick une personne", inline=False)
	embed.add_field(name='#ban', value="(ADMIN) Cette commande ban une personne", inline=False)
	embed.add_field(name='#unban', value="(ADMIN) Cette commande unban une personne", inline=False)
	embed.add_field(name='#mute', value="(ADMIN) Cette commande mute une personne", inline=False)
	embed.add_field(name='#unmute', value="(ADMIN) Cette commande unmute une personne", inline=False)
	embed.add_field(name='#serverinfo', value="Cette commande donne les stats du serveur", inline=False)
	embed.add_field(name='#credit', value="Cette commande montre les credits du bot", inline=False)

	await ctx.send(author, embed=embed)

bot.run(token)