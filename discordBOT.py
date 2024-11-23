import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 


embed = Embed(
    color= 0x499957,
    timestamp='now'
)

hook.send('@everyone This is a notification for all members!')


embed.add_field(name='SIP bot', value='[installed]')
embed.set_footer(text='by og._.njen')


hook.send(embed=embed)
