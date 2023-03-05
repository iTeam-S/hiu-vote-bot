from os import environ as env


class Configuration:
    """
    Retrieves the value from the environment.
    Takes the default value if not defined.
    """

    ADAPTER = env.get("ADAPTER")

    DB_FILE = env.get("DB_FILE")

    DB_HOST = env.get("DB_HOST", "localhost")
    DB_USER = env.get("DB_USER", "root")
    DB_PASSWORD = env.get("DB_PASSWORD", "")
    DB_PORT = env.get("DB_PORT")
    DB_NAME = env.get("DB_NAME")
    SRV_PROTOCOL = env.get("SRV_PROTOCOL")

    ACCESS_TOKEN = env.get("AMP_ACCESS_TOKEN")
    VERIF_TOKEN = env.get("AMP_VERIF_TOKEN")

    APP_HOST = env.get("AMP_HOST", "0.0.0.0")
    APP_PORT = int(env.get("AMP_PORT", 4555))
    APP_URL = env.get("AMP_URL")
    ADMIN_ENABLE = env.get("ADMIN_ENABLE")

    ADMIN_EMAIL = env.get("ADMIN_EMAIL", "")
    ADMIN_PASSWORD = env.get("ADMIN_PASSWORD", "")
    POCKET_URL = env.get("POCKET_URL", "http://localhost:8090")
