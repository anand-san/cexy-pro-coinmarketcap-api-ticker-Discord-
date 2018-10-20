#remove all discord lines if you do not want to use it in discord
#Author : seanjin17
#feel free to contact me if you need any help

import requests
import json
import random
import asyncio
import aiohttp
from discord.ext.commands import Bot
import discord
from DiscordHooks import Hook, Embed, EmbedAuthor, Color
from datetime import datetime
BOT_PREFIX = ("?")
TOKEN = "Your Discord Token"
client = Bot(command_prefix=BOT_PREFIX)
api_key = 'Your CMC PRO API KEY'
def get_data(inp):
	url2='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol='+str(inp).upper()
	get_data.headers = {
           'X-CMC_PRO_API_KEY' : api_key,
           }
	try:
		r1 = requests.get(url2, headers=get_data.headers).json()
		get_data.h1=(r1["data"][str(inp).upper()]["quote"]["USD"]["percent_change_1h"])
		get_data.h24=(r1["data"][str(inp).upper()]["quote"]["USD"]["percent_change_24h"])
		get_data.d7=(r1["data"][str(inp).upper()]["quote"]["USD"]["percent_change_7d"])
		get_data.rank=(r1["data"][str(inp).upper()]["cmc_rank"])
		get_data.name=(r1["data"][str(inp).upper()]["name"])
		get_data.av_supply=("{:,.2f}".format(float((r1["data"][str(inp).upper()]["circulating_supply"]))))
		get_data.cap=("${:,.2f}".format(float((r1["data"][str(inp).upper()]["quote"]["USD"]["market_cap"]))))
		get_data.price=("{:,.3f}".format(float((r1["data"][str(inp).upper()]["quote"]["USD"]["price"]))))
		return "Valid"
	except:
		return "Invalid"
@client.command(pass_context=True)
async def longCommand(ctx):
   await client.send_typing(ctx.channel)
   await asyncio.sleep(10)
   await client.say("Done!")
@client.event
async def on_message(message):
	errmsg="```This part is still under development, You'll be notified when it'll be done```"
	out=str(message.content)
	outp=get_data(str(out[1:]))
	if message.content.startswith('?help'):
		helpmsg="```Coinmarketcap.com calls\n ?symbol \t - Displays Information about the symbol      \n ?info symbol \t - Get Additional data about the symbol provided \n\n Example : ?eth / ?info eth   \n Exchange Specific Call\n\n ?exchangename coinname \t - Displays Information about the symbol on the exchange provided\n\n Example : ?binance nano\n\nThe bot is still under development, Expect all features to work after the development is complete```"
		await client.send_message(message.channel, helpmsg)
	elif message.content.startswith('?'):
		if(outp=="Valid"):
			if(out[1:].upper()=="BTC"):
				logo="https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol="+(str(out[1:].upper()))
				embed = discord.Embed(title="**#"+str(get_data.rank)+" "+str(get_data.name)+"**", description="", color=0x00ff00)
				embed.add_field(name="Price USD : **$"+str(get_data.price)+"**", value="**\n\nPercent Change (1H) : **"+str(get_data.h1)+"%**\nPercent Change (24H) : **"+str(get_data.h24)+"%**\nPercent Change (7D) : **"+str(get_data.d7)+"%**\n\nAvailable Supply : **"+str(get_data.av_supply)+"**\n\nMarket Cap (USD) : **"+str(get_data.cap)+"**\n", inline=True)
				embed.set_thumbnail(url="https://s2.coinmarketcap.com/static/img/coins/64x64/1.png")			
				embed.set_footer(text="Type ?help to know what else i can do")									
				await client.send_message(message.channel, embed=embed)				
			else:
				btc="https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC"
				btc = requests.get(btc, headers=get_data.headers).json()
				pricebtc=str("{0:.8f}".format(float(get_data.price)/(float((btc["data"]["BTC"]["quote"]["USD"]["price"])))))
				logo="https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol="+(str(out[1:].upper()))
				logo=requests.get(logo, headers=get_data.headers).json()
				embed = discord.Embed(title="**#"+str(get_data.rank)+" "+str(get_data.name)+"**", description="", color=0x00ff00)
				embed.add_field(name="Price USD : **$"+str(get_data.price)+"**", value="Price BTC : **"+pricebtc+" BTC**\n\nPercent Change (1H) : **"+str(get_data.h1)+"%**\nPercent Change (24H) : **"+str(get_data.h24)+"%**\nPercent Change (7D) : **"+str(get_data.d7)+"%**\n\nAvailable Supply : **"+str(get_data.av_supply)+"**\n\nMarket Cap (USD) : **"+str(get_data.cap)+"**\n", inline=True)
				embed.set_thumbnail(url=str(logo["data"][out[1:].upper()]["logo"]))			
				embed.set_footer(text="Type ?help to know what else i can do")									
				await client.send_message(message.channel, embed=embed)
		else:
			embed = discord.Embed(title="Search Results", description="", color=0x00ff00)
			embed.add_field(name="404", value="No results Found for "+out[1:], inline=True)
			embed.set_thumbnail(url="https://cdn3.iconfinder.com/data/icons/web-development-41/512/17-512.png")
			embed.set_footer(text="Type ?help to know what else i can do")						
			await client.send_message(message.channel, embed=embed)
print("Cexy is Online")
client.run(TOKEN)
