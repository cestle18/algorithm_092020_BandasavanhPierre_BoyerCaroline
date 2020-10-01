class FibonacciHeap:
    def __init__(self):
        # A l'initialisation, notre liste contient un élément: 0
        # Comme on a rien inséré, sa taille vaut 0
        self.heap_list = [0]
        self.current_size = 0

    def shift_up(self, child_index):
        # shift_up permet de placer un élément au bon endroit dans la heap
        # l'index d'un parent est le quotient de l'index de l'enfant divisé par deux (lien de l'article a inserer)
        parent_index = child_index // 2

        # Nous sommes certains que l'élément est bien placé lorsqu'il se trouve à la racine
        # ou sur le premier élément de gauche
        # Cela se traduit par son index étant négatif ou nul

        # Pour chaque niveau de la heap tant que nous ne sommes par surs du placement de l'élément
        while parent_index > 0:

            # on prend les valeurs de ce niveau
            parent_index = child_index // 2
            child_value = self.heap_list[child_index]
            parent_value = self.heap_list[parent_index]

            # Si la valeur de l'enfant est inférieure à celle de son parent
            if child_value < parent_value:
                # alors nous inversons leur place
                print("swapping index {} (value {}) with index {} (value {})".format(child_index, child_value, parent_index, parent_value))
                self.heap_list[child_index], self.heap_list[parent_index] = parent_value, child_value

            # Et nous passons au niveau supérieur
            child_index = parent_index

        print(self.heap_list)
 
    def insert(self, k):
        print("=========\ninserting {} to the heap".format(k))
        # doc: https://docs.python.org/3/library/array.html?highlight=append#array.array.append
        # .append ajoute l'élément k à la fin de la liste heap_list
        self.heap_list.append(k)
        # Comme k a été ajouté, la taille augmente de 1
        self.current_size += 1
        # k a été inséré arbitrairement tout en bas de la heap, il n'est donc pas nécessairement au bon endroit
        # on appelle la fonction shift_up pour le placer correctement
        self.shift_up(self.current_size)
 
    def shift_down(self, root_index):
        current_node_index = root_index

        # Si le double de l'index de l'élément courant et inférieur ou égal à la taille totale
        # Alors l'élément courant à au moins un enfant
        while (current_node_index * 2) <= self.current_size:
            current_node_value = self.heap_list[current_node_index]

            # On cherche à connaitre la valeur du plus petit enfant pour savoir si l'élément est bien placé
            min_child_index = self.min_child(current_node_index)
            min_child_value = self.heap_list[min_child_index]

            # Si la valeur de l'élément est supérieure à celle de son plus petit enfant,
            # alors il faut les inverser de place
            if current_node_value > min_child_value:
                self.heap_list[current_node_index], self.heap_list[min_child_index] = min_child_value, current_node_value

            # On passe ensuite au prochain niveau
            current_node_index = min_child_index
 
    def min_child(self, parent_index):
        # On calcule les index potentiels des deux enfants
        left_child_index = parent_index * 2
        right_child_index = parent_index * 2 + 1

        # L'enfant de droite n'existe pas si son index dépasse de la taille du tableau
        if right_child_index > self.current_size:
            # Alors le seul enfant est celui de gauche, il est l'enfant avec la valeur la plus basse
            return left_child_index
        else:
            # Ici nous savons qu'il y a deux enfants, nous prenons leur valeurs
            left_child_value = self.heap_list[left_child_index]
            right_child_value = self.heap_list[right_child_index]
            # Et nous retournons l'index du plus petit des deux
            if left_child_value < right_child_value:
                return left_child_index
            else:
                return right_child_index
 
    def delete_min(self):
        # delete_min permet de connaitre la valeur minimale de la heap et de la retirer de celle-ci
        # Si la liste est vide, alors il n'y a plus de valeur minimale
        if len(self.heap_list) == 1:
            return None

        # On sauvegarde la valeur de la racine
        root_index = 1
        root = self.heap_list[root_index]
 
        # On écrase la racine avec le dernier élément de la heap (le plus grand)
        self.heap_list[root_index] = self.heap_list[self.current_size]
 
        # doc: https://docs.python.org/3/library/array.html?highlight=pop#array.array.pop
        # on retire le dernier élément de la heap comme il a été copié sur l'élément racine
        self.heap_list.pop()
 
        # Comme on a retiré un élément, on retire 1 à la taille
        self.current_size -= 1
 
        # Le dernier élément de la heap a été placé arbitrairement à la racine de la heap, il n'est donc pas nécessairement au bon endroit
        # on appelle la fonction shift_down pour le placer correctement
        self.shift_down(root_index)
 
        # La racine est désormais le nombre le plus petit de la heap
        return root
