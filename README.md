# Python common utils

## async lrc cache

LRU cache for asyncio

[async_lru 1.0.3](https://pypi.org/project/async-lru/)

```python
from al_utils.alru import alru_cache

@alru_cache(maxsize=128, typed=False)
def test():
    pass
```

## sync to async

Make sync function as async

```python
from al_utils.async_util import async_wrap

@async_wrap
def test():
    pass

# equals to
async_wrap(test())

# equals to
async def test():
    pass
```

## async to sync

Make async function as sync

```python
from al_utils.async_util import run_async
@run_async
async def test():
    pass

# equals to
run_async(test())

# equals to
def test():
    pass
```

## logger

Create logger easier to print log to console and save logs at the same time.

Logger name is current package name split by dot.

It contains a default logger config.

It will save infos to `./logs/info/` and errors to `./logs/error/`. Log files split in each week.

```py
from al_utils.logger import Logger

logger = Logger(class_name='').logger
```

## singleton

Singleton container.

Support multiple container.

```py
from al_utils.singleton import Singleton

# set class to container
class Test(Singleton):
    pass


from al_utils.singleton import resolve

test = resolve(Test)
```

If meta class conflict, using `merge_meta` to resolve it.

```py
from al_utils.singleton import Singleton
from al_utils.meta import merge_meta

class Test(merge_meta(Singleton, AnothClass)):
    pass
```

Or, without extends, add class or instance in low-level functions.

```py
from al_utils.singleton import add, add_type

class Test1:
    pass

test1 = Test1()
add(test1)

class Test2:
    pass

add_type(Test2)
```

## print colored messages

Print message to console with custome color(text color, background color) and style(light, normal, bold, ...)

```py
from al_utils.console import ColoredConsole

# light
ColoredConsole.debug('This is a debug.')
# green
ColoredConsole.success('This is a success.')
# yellow
ColoredConsole.warn('This is a warning.')
# red, stderr
ColoredConsole.error('This is a error.')

# custome colored text

# set io(stdout or stderr) start colored.
ColoredConsole.set(style, text_color, bg_color, io)

# print custome colored text
ColoredConsole.print('Costome color text.')

# unset, clear all style and color sets.
ColoredConsole.unset(io)
```
