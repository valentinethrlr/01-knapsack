class KPInstance:

    def __init__(self, W: list[int], V: list[int], C: int) -> None:
        self.W: list[int] = W
        self.V: list[int] = V
        self.C: int = C
        self.size: int = 0

    def load_from_file(self, filepath):
        '''
        Load the instance from the file `filepath`
        '''
        ...

    def __repr__(self):
        return f"{__class__.__name__}(W={self.W}, V={self.V}, C={self.C})"

