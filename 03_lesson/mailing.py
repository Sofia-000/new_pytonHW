from address import Address


class Mailing:
    def __init__(self, track: int, to_address: Address,
                 from_adress: Address, cost: int):
        self.track = track
        self.to_address = to_address
        self.from_address = from_adress
        self.cost = cost

    def __str__(self):
        return (
            f"{self.track} из {self.from_address} в {self.to_address}"
            f"Стоимость {self.cost} руб"
        )
