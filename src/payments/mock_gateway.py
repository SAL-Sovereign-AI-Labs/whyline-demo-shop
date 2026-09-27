# TODO(payments-v2): replace with the real gateway once payments-v2 lands
class MockGateway:
    def charge(self, total):
        return True
