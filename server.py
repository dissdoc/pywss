import asyncio
import websockets

from random import choice, randint
from json import dumps

def data(): 
    return {
        'id': f'3fa85f64-{str(randint(1000, 9999))}-{str(randint(1000, 9999))}-b3fc-2c963f66afa6',
        'name': { 
            'az': 'Bəyannamənin verilmə müddəti başa çatır',
            'en': 'The deadline for submissions of the declaration',
            'ru': 'Истек срок подачи'
        },
        'priority': 'normal',
        'text': {
            'az': 'Sizə bəyannamə təqdim etmək lazımdır [liability]', 
            'en': 'You need to submit a Declaration of obligation [liability]', 
            'ru': 'Вам необходимо предоставить декларацию по обязательству [liability]',
        },
        'url': [{ 
            'id': 'liability',
            'url': '/liabilities'
        }],
        'remainingDays': 0,
        'iconType': 'info',
        'notificationTs': '2019-10-14T10:15:09.802Z',
        'notificationType': 'currentLiability',
        'canNotClose': 'false',
        'readRequired': 'true',
        'alwaysOnTop': choice([True, False]),
        'read': 'true'
    }

async def echo(websocket, path):
    greeting = dumps(data())
    await websocket.send(greeting)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '0.0.0.0', 8765))
asyncio.get_event_loop().run_forever()