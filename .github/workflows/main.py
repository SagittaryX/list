from discord_webhook import DiscordWebhook as dw

webhook = dw(
    url="https://discord.com/api/webhooks/1154085805057376256/wDobSXgoFaNzCm74AJudfcEUmkoeimHyM-lYj04_P9cKT4c8X9mQ8wRYJVUwZv_YHzk7",
    content="De lijst is geüpdatet, ouwe smeerlap."
)
response = webhook.execute()
