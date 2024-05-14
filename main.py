import lightbulb, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(os.getenv("TOKEN"))

bot = lightbulb.BotApp(token=TOKEN, prefix="~", default_enabled_guilds=1240037367549661284)

@bot.command
@lightbulb.command("ping", "checks if the bot is still alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx:lightbulb.Context) -> None:
    await ctx.respond(f"Pong!")




bot.load_extensions_from("extensions")
bot.run()