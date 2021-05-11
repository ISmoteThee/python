from ipaddress import ip_address
class Interface:
    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._validStates = ['Up', 'Down']
        self._state = "Down"
        

    @property
    def address(self):
        return f"IP address is {self._address}"

    @address.setter
    def address(self, value):
        if not ip_address(value):
            raise ValueError(f">> {value} is not a valid address")
        self._address = value

    @property
    def state(self):
        return f"{self._name} is {self._state}."

    @state.setter
    def state(self, desiredState):
        if type(desiredState) == str:
            if desiredState.lower().capitalize() in self._validStates:
                self._state = desiredState.lower().capitalize()
            else:
                raise ValueError("Invalid State: Please enter 'Up' or 'Down'")
        else:
            raise ValueError("Invalid Type: Please enter 'Up' or 'Down'")

    def __repr__(self):
        return str(vars(self))