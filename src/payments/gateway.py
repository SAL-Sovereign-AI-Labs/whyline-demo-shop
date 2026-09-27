class Gateway:
    def charge(self, total):
        # real provider call goes here
        return {"ok": True, "amount": total}
