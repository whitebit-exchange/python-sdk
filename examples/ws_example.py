import asyncio
import logging
import time

from whitebit.stream.ws import WhitebitWsClient


class Bot(WhitebitWsClient):
    '''Can be used to create a custom trading strategy/bot'''

    def __init__(self):
        super().__init__(key="", secret="")

    async def on_message(self, event) -> None:
        '''receives the websocket events'''
        if 'result' in event:
            result = event['result']
            match result:
                case 'pong': return
            logging.info(event['result'])
            return
        else:
            method = event['method']
            match method:
                case WhitebitWsClient.DEALS_UPDATE:
                    logging.info(event['params'])
            return


async def main() -> None:
    bot = Bot()
    await bot.get_deals("BTC_USDT", 0, 100)
    await bot.subscribe_deals(["BTC_USDT"])
    while not bot.exception_occur:
        await asyncio.sleep(100)
    return


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
