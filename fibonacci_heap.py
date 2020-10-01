class Heap(object):

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value: int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass

class Node:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.order = 0


    # La fonction append permet d'ajouter un nouvel élément à la fin de l'arbre
def add_at_end(self, t):
    self.children.append(t)
    self.order = self.order + 1


class FibonacciHeap(Heap):

    ## On créé notre arbre de taille 0
    def __init__(self):
        self.nodes: list = []
        self.min_node = None
        self.count = 0

    ## On va insérer nos valeurs
    def insert(self, value: int) -> None:
        new_node = Node(value)
    
    ## Append est la fonction pour ajouter, on va ajouter un node à self
        self.nodes.append(new_node)
   
        if self.min_node is None or self.min_node.value > new_node.value:
            self.min_node = new_node

    ## On va chercher la valeur minimum
    def find_min(self) -> int:
        if self.min_node is None :
            return None
        return self.min_node.value

    def consolidate(self):
        pass
    # aux = (a(self.count) + 1) [None]

    #    def consolidate(self):
    #   aux = (floor_log2(self.count) + 1)*[None]

    def delete_min(self):
        min_node = self.min_node
        if min_node is not None:
            for child in min_node.children:
                self.nodes.append(child)
                self.nodes.remove(min_node)
                if self.nodes == []:
                    self.min_node = Node
                else:
                    self.min_node = self.nodes[0]
                    self.consolidate()
                    self.count = self.count - 1
                return min_node.key

    def merge(self, fibonnaci_heap: Heap) -> None:
            heap2 = []
            for value in heap2:
                self.nodes.append(value)
