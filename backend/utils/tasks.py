import asyncio

from faker import Faker


fake = Faker()

async def distribution(*args):
    client = args[0]
    counter = 0
    contacts = await client.get_contacts()
    for contact in contacts:
        await client.send_message(contact.id, fake.text())
        await asyncio.sleep(0.3)
        counter += 1
        if counter == 10500:
            break