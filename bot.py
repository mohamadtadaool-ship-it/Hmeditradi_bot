from telethon import TelegramClient, events

# بيانات الحساب
api_id = '26470215'
api_hash = '15330e201289196b668037666f2c3d5e'

# إعدادات القنوات
input_channels = [-1002237890538]  # القناة المصدر
output_channel = -1002360341775    # قناتك الوجهة

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=input_channels))
async def job(event):
    try:
        await client.send_message(output_channel, event.message)
        print("✅ تم تحويل رسالة جديدة!")
    except Exception as e:
        print(f"❌ خطأ في التحويل: {e}")

print("🚀 BOT IS LIVE ON SERVER...")
client.start()
client.run_until_disconnected()
