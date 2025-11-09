# synchronous
def main():
    print('Hello')
    print('Welcome to World!')

def name():
    print('Ahmad')

def sync():
    main()
    name()

sync()





#asynchronous
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
