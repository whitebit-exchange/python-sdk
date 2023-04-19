## A Python SDK for [whitebit](https://www.whitebit.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

For best compatibility, please use Python >= 1.18

Please read [whitebit API document](https://whitebit-exchange.github.io/api-docs/) before continuing.

## API List

- [Private API](https://whitebit-exchange.github.io/api-docs/docs/category/private)
- [Public API](https://whitebit-exchange.github.io/api-docs/docs/category/public)
- [Private WS](https://whitebit-exchange.github.io/api-docs/private/websocket/)
- [Public WS](https://whitebit-exchange.github.io/api-docs/public/websocket/)

v4 is the preferred one to use

## Disclaimer
“You acknowledge that the software is provided “as is”. Author makes no representations or warranties with respect to
the software whether express or implied, including but not limited to, implied warranties of merchantability and fitness
for a particular purpose. author makes no representation or warranty that: (i) the use and distribution of the software
will be uninterrupted or error free, and (ii) any use and distribution of the software is free from infringement of any
third party intellectual property rights. It shall be your sole responsibility to make such determination before the use
of software. Author disclaims any liability in case any such use and distribution infringe any third party’s
intellectual property rights. Author hereby disclaims any warranty and liability whatsoever for any development created
by or for you with respect to your customers. You acknowledge that you have relied on no warranties and that no
warranties are made by author or granted by law whenever it is permitted by law.”

## REST API

### Setup

Init client for API services. Get APIKey/SecretKey from your whitebit account.

```python
account = MainAccountClient(api_key="", api_secret=""))
```

Following are some simple examples.

See the **examples** folder for full references.

#### Create Spot Limit Order

```python
# Create order/spot client
order = OrderClient(api_key="",
                    api_secret="")

# Call SDK function put_limit
print(order.put_limit("BTC_USDT", "sell", "0.1", "40000", True))
```

## Websocket API

### Setup

Init bot class and "on_message" method for work with ws responses. Get APIKey/SecretKey from your whitebit account.

```python
class Bot(WhitebitWsClient):
    def __init__(self):
        super().__init__(key="", secret="")

    async def on_message(self, event) -> None:
        logging.info(event)
        
```

Following are some simple examples.

See the **examples** folder for full references.

#### Subscribe on deals topic

```python
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
```
