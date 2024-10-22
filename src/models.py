from enum import Enum


class TenantPortal(Enum):
    CLICK_PAY = "click_pay"
    ACTIVE_BUILDING = "activebuilding"
    RENT_CAFE = "rentcafe"


class Tenant:

    def __init__(self, address: str, email: str, phone_number: str, company: str) -> None:
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.mgmt_company = company

    def to_db_tuple(self) -> tuple[str, ...]:
        return self.address, self.email, self.phone_number, self.mgmt_company
