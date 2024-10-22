from src.models import TenantPortal, Tenant


class PortalRetriever:
    """Handles data retrieval from tenant portals."""

    def __init__(self, portal: TenantPortal):
        self.name = portal

    def retrieve_data(self):
        """Retrieve data based on the portal name."""
        raise NotImplementedError(f"Portal '{self.name.value}' is not supported.")


class ClickPayPortalRetriever(PortalRetriever):

    def __init__(self, portal: TenantPortal):
        super().__init__(portal)

    def retrieve_data(self) -> Tenant:
        return self._mock_clickpay_data()

    @staticmethod
    def _mock_clickpay_data() -> Tenant:
        """Simulate data retrieval from ClickPay."""
        return Tenant(
            address="Example address 123",
            email="example@example.com",
            phone_number="1234567890",
            company="Ocean Prime"
        )