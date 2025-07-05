from starlette.config import Config

config = Config(".env")

VERSION = "0.1.0"
PROJECT_NAME: str = "Cnote"

DEBUG: bool = config("DEBUG", cast=bool, default=False)


# logging configuration
# LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
# logging.basicConfig(
#     handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
# )
# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
