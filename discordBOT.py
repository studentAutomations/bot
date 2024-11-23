import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = os.getenv('WEBHOOK_URL')
hook = Webhook(WEBHOOK_URL) 

embed = Embed(
    color= 0x499957,
    timestamp='now'
)

embed.add_field(name='Notify', value='@everyone')
embed.add_field(name='Botovi za Sip i CS', value='[installed]')
embed.set_footer(text='by og._.njen')


hook.send(embed=embed)
