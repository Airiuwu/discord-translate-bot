from discord.ext.commands import Bot
from translate import Translator

bot = Bot(command_prefix='.')

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')

@bot.command(pass_context=True)
async def translate(ctx):
    if ctx.author.id == bot.user.id:
        await ctx.message.delete()
        args = ctx.message.content.split(" ")[1:]
        translator = Translator(to_lang=args[0])
        args.pop(0)
        text = " ".join(args)
        translation = translator.translate(text)
        await ctx.send(translation)
    else:
        return

bot.run('')
