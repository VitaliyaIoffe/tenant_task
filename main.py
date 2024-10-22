import argparse
from enum import Enum
import getpass


class TenantPortal(Enum):
    CLICK_PAY = "click_pay"
    ACTIVE_BUILDING = "activebuilding"
    RENT_CAFE = "rentcafe"


def parse_args() -> argparse.Namespace:
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


def main() -> None:
    """Main entry point of the program."""
    args = parse_args()
    password = getpass.getpass(prompt="Enter your password: ")

    if args.tenant_portal == TenantPortal.CLICK_PAY:
        print(f"Retrieving data from {args.tenant_portal.value} for user {args.username}...")
        pass
        # print("Data successfully inserted into the database.")
    else:
        raise NotImplementedError(f"Portal '{args.tenant_portal.value}' is not supported.")


if __name__ == "__main__":
    main()  # Run the main program
