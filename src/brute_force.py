# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
    def __init__(self, instance) -> None:
        super().__init__(instance)


    def _all_solutions(n: int) -> list[tuple[int, ...]]:
    
        solutions = [None] * (2 ** n)
        
        for i in range(0, 2 ** n):
            bits: str = bin(i)[2:]
            k = n - len(bits)
            bits = k * '0' + bits
            solutions[i] = tuple([int(b) for b in bits])
        
        return solutions

    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        n = self._inst.size
        
        # générer toutes les solutions
        solutions: list[tuple[int, ...]] = self._all_solutions()
        
        # éliminer toutes les solutions non faisables
        # trouver la meilleure solution
        
        current_max: int = 0
        
        for sol in solutions:
            if self.value(sol) > current_max and self.weight(sol) <= self._inst.C:
                current_max = self.value(sol)
        
        return sol
    
try:
    import doctest

    doctest.testmod()
except:
    print("Unable to load doctests")