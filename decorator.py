from ipaddress import ip_address
class Interface:
    def __init__(self, name, address):
        self.name = name
        self.address(address) = address
        self.state = "Down"

    @property
    def address(self):
        return f"IP address is {self._address}"

    @address.setter
    def address(self, value):
        if not ip_address(value):
            raise ValueError(f">> {value} is not a valid address")
        self._address = value

    def __repr__(self):
        return str(vars(self))