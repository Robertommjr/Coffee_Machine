# start a RockBand here
class RockBand:
    genre: str = "rock"
    n_members: int = 4
    key_instruments: list = ["electric guitar", "drums"]


band = RockBand()
print(band.genre)
print(band.n_members)
print(band.key_instruments)
