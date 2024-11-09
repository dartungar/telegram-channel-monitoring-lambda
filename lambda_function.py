import os
from telethon import TelegramClient
from telethon.sessions import StringSession


# Lambda handler
def lambda_handler(event, context):
    # Retrieve API ID and hash from environment variables
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    string_session = os.getenv('string_session')

    if not all([api_id, api_hash, string_session]):
        raise ValueError("API_ID, API_HASH, and string_session must be set in environment variables.")

    # Define the list of channels to monitor and keywords
    channels = event.get('channels', [
        'baraholka_tbi', 'tbilisio', 'tbilisiw', 'tbilisy_batumy',
        'baraholka_tbilisi_home', 'avito_baraholka_tbilisi',
        'tbilisi_baraxolka', 'baraholka_tbilisi_ge'
    ])
    keywords = event.get('keywords', ['ноутбук', 'лэптоп', "laptop"])
    stopwords = event.get('stopwords', ['куплю'])

    # Create the client
    client = TelegramClient(StringSession(string_session), api_id, api_hash)

    async def main():
        # Connect to the client
        await client.start()

        channel_to_forward = await client.get_entity('https://t.me/+jNtkTIzX8NhlNWEy')  # Replace with your channel username/ID

        existing_messages = client.iter_messages(channel_to_forward)
        existing_message_ids = {message.id async for message in existing_messages}
        existing_message_texts = {message.message.lower() if message.message else None async for message in existing_messages}

        messages_to_forward = []
        message_ids = set()
        message_texts = set()

        # Iterate through the channels
        for channel in channels:
            # Fetch the latest messages from the channel
            async for message in client.iter_messages(channel, limit=100):
                if message.message:
                    message_lower = message.message.lower()
                    matched_keywords = [keyword for keyword in keywords if keyword in message_lower]
                    if matched_keywords and not any(stopword in message_lower for stopword in stopwords):
                        if message.id not in message_ids and message.id not in existing_message_ids:
                            if message_lower not in message_texts and message_lower not in existing_message_texts:
                                message_texts.add(message_lower)
                                message_ids.add(message.id)
                                messages_to_forward.append((message, matched_keywords))

        msg_count = len(messages_to_forward)
        for msg, matched_keywords in messages_to_forward:
            tags = ' '.join(f'#{keyword.replace(" ", "_")}' for keyword in matched_keywords)
            link_msg = f"{msg.message[:100]}...\nlink:\nhttps://t.me/c/{msg.peer_id.channel_id}/{msg.id}\nTags: {tags}"
            await client.forward_messages(channel_to_forward, msg)
            await client.send_message(channel_to_forward, link_msg)

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