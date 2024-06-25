GUILD_ID = 1254990539762303180 # for emojis
CATS_GUILD_ID = False # alternative guild purely for cattype emojis (use for christmas/halloween etc), False to disable
BACKUP_ID = 1254990539762303180 # channel id for db backups, private extremely recommended

# discord bot token, use os.environ for more security
TOKEN = os.environ['token']
# TOKEN = "token goes here"

# top.gg voting key
# set to False to disable
WEBHOOK_VERIFY = os.environ["webhook_verify"]

# top.gg api token because they use ancient technology and you need to post server count manually smh
# set to False to disable
TOP_GG_TOKEN = os.environ["top_gg_token"]

# this will automatically restart the bot if message in GITHUB_CHANNEL_ID is sent, you can use a github webhook for that
# set to False to disable
GITHUB_CHANNEL_ID = 1254992994495627294

# all messages in this channel will be interpreted as user ids to give premium access to
# set to False to disable
DONOR_CHANNEL_ID = 1249343008890028144

# whether you use pm2 for running it or not
# that will just silently kill it on autoupdate and let pm2 restart it instead of manually restarting it
USING_PM2 = True

BANNED_ID = [] # banned from using /tiktok

WHITELISTED_BOTS = [] # bots which are allowed to catch cats

# what to do when there is a crash
CRASH_MODE = "RAISE"
