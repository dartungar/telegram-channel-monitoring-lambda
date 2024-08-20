import os
from telethon import TelegramClient
from telethon.sessions import StringSession


# Lambda handler
def lambda_handler(event, context):
    # Retrieve API ID and hash from environment variables
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    string_session = os.getenv('string_session')

    # Define the list of channels to monitor and keywords
    channels = event['channels'] if 'channels' in event else ['baraholka_tbi', 'tbilisio', 'tbilisiw', 'tbilisy_batumy', 'baraholka_tbilisi_home', 'avito_baraholka_tbilisi', 'tbilisi_baraxolka', 'baraholka_tbilisi_ge']
    keywords = event['keywords'] if 'keywords' in event else ['ноутбук', 'кресло'] 
    stopwords = event['stopwords'] if 'stopwords' in event else ['куплю']

    # Create the client
    client = TelegramClient(StringSession(string_session), api_id, api_hash)

    msg_count = 0;

    async def main():
        # Connect to the client
        await client.start()

        dialogs = await client.get_dialogs()
        channel_to_forward = await client.get_entity('https://t.me/+jNtkTIzX8NhlNWEy')  # Replace with your channel username/ID

        # TODO: pass keywords & channels to lambda

        existing_messages = client.iter_messages(channel_to_forward);
        existing_message_ids = [message.id async for message in existing_messages]
        existing_message_texts = [message.message.lower() async for message in existing_messages]
        messages_to_forward = []
        message_ids = set()
        message_texts = set()
        
        # Iterate through the channels
        for channel in channels:
            # Fetch the latest messages from the channel
            async for message in client.iter_messages(channel, limit=100):
                #print(message.message)
                if message.message and any(keyword in message.message.lower() for keyword in keywords) and not any(stopword in message.message.lower() for stopword in stopwords):
                    # Forward the message to the specified channel
                    if message.id not in message_ids and message.id not in existing_message_ids:
                        if message.message.lower() not in message_texts and message.message.lower() not in existing_message_texts:
                            messages_to_forward.append(message)
                            message_ids.add(message.id)
                            message_texts.add(message.message.lower())

        msg_count = len(messages_to_forward);
        await client.forward_messages(channel_to_forward, messages_to_forward)
        # Disconnect the client
        await client.disconnect()

    # Run the client within an asyncio event loop
    with client:
        client.loop.run_until_complete(main())

    return {
        'statusCode': 200,
        'body': f'Forwarded {msg_count} new messages.'
    }

if __name__ == "__main__":
    event = []
    context = []
    # api_id = os.getenv('API_ID')
    # api_hash = os.getenv('API_HASH')
    # with TelegramClient(StringSession(), api_id, api_hash) as client:
    #     print(client.session.save())
    lambda_handler(event, context)