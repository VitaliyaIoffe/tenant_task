import argparse
import logging
import os

from src.database import DatabaseManager
from src.models import TenantPortal
from src.portals import ClickPayPortalRetriever, PortalRetriever


logger = logging.getLogger(__file__)
logger.setLevel(level=logging.INFO)


def parse_args() -> argparse.Namespace:
    logging.info("Parsing arguments")
    parser = argparse.ArgumentParser(
        description="Retrieve tenant data from a portal and store it in a database."
    )
    parser.add_argument(
        "tenant_portal", type=str, help="The name of the tenant portal (e.g., click_pay)"
    )
    parser.add_argument(
        "username", type=str, help="The username or email for the portal login"
    )
    return parser.parse_args()


def get_portal(tenant_portal: str, username: str, password: str) -> PortalRetriever:
    logger.info("Getting portal")
    portal = None
    if tenant_portal == TenantPortal.CLICK_PAY.value:
        logger.info(f"Retrieving data from {tenant_portal} for user {username}...")
        portal = ClickPayPortalRetriever(TenantPortal.CLICK_PAY)
        logger.info("Data successfully inserted into the database.")
    else:
        raise NotImplementedError(f"Portal '{args.tenant_portal}' is not supported.")

    return portal


if __name__ == "__main__":
    logger.info("Starting app")
    args = parse_args()
    # password = getpass.getpass(prompt="Enter your password: ")
    password = os.getenv("PASSWORD", "myydefaultpassword")
    if not password:
        raise ValueError("Password not set. Use the PASSWORD environment variable.")

    database_manager = DatabaseManager()
    portal = get_portal(tenant_portal=args.tenant_portal, username=args.username, password=password)
    data = portal.retrieve_data()
    database_manager.insert_tenant(data)
    logger.info("Finished")
