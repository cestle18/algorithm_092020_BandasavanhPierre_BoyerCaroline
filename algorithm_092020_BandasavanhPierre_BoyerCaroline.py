class FibonacciHeap:
    def __init__(self):
        # A l'initialisation, notre liste contient un élément: 0
        # Comme on a rien inséré, sa taille vaut 0
        self.heap_list = [0]
        self.current_size = 0