import discord


ID_APP = 569724616210382875 # from Discord developer portal
ID_GUILD = 970576952257835059 # Guild id which bot in



MY_GUILD = discord.Object(id=ID_GUILD)  # replace with your guild id




class MyClient(discord.Client):
 def __init__(self, *, intents: discord.Intents, application_id: int):
  super().__init__(intents=intents, application_id=application_id)

 # A CommandTree is a special type that holds all the application command
 # state required to make it work. This is a separate class because it
 # allows all the extra state to be opt-in.
 # Whenever you want to work with application commands, your tree is used
 # to store and work with them.
 # Note: When using commands.Bot instead of discord.Client, the bot will
 # maintain its own tree instead.
  self.tree = app_commands.CommandTree(self)

 # In this basic example, we just synchronize the app commands to one guild.
 # Instead of specifying a guild to every command, we copy over our global commands instead.
 # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
 async def setup_hook(self):
 # This copies the global commands over to your guild.
  self.tree.copy_global_to(guild=MY_GUILD)
  await self.tree.sync(guild=MY_GUILD)


intent = discord.Intents.default()
intent.reactions = True
intent.message_content = True
intent.typing = False
intent.presences = False

# In order to use a basic synchronization of the app commands in the setup_hook
client = MyClient(intents=intent, application_id=ID_APP)

