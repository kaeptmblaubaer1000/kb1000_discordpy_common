import functools
import logging

def force_async(coro):
    """\
    Small decorator to trick asyncio to identify Cython coroutines
    """
    @functools.wraps(coro)
    async def new_coro(*args, **kwargs):
        return await coro(*args, **kwargs)

    return new_coro

def log_exception(coro, exception=Exception, prefix=""):
    logger = logging.getLogger(prefix + coro.__module__)

    @functools.wraps(coro)
    async def new_coro(*args, **kwargs):
        try:
            return await coro(*args, **kwargs)
        except exception as e:
            logger.error(f"Exception caught during execution of {coro.__name__}", exc_info=e)

    return new_coro

def setup(bot):
    pass
