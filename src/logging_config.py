import logging
import logging.config


def setup_logging(default_path='logging.conf', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration."""
    import os
    import configparser

    # Load configuration from the logging configuration file
    if os.path.exists(default_path):
        config = configparser.ConfigParser()
        config.read(default_path)

        logging.config.fileConfig(default_path)
    else:
        logging.basicConfig(level=default_level)
        logging.warning("Logging configuration file not found. Default logging level set to INFO.")


# Setup logging
setup_logging()

# Create a logger for this module
logger = logging.getLogger('app')