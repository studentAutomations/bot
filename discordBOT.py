import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_OTHER1')
hook = Webhook(WEBHOOK_URL) 


embed = Embed(
    color= 0x499957,
    timestamp='now'
)

hook.send('@everyone')


embed.add_field(name='BOT', value='[Updated]')
embed.set_footer(text='by og._.njen')


hook.send(embed=embed)
