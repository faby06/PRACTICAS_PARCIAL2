class Grafo: #Se crea una clase llamada grafo 
    def __init__(self, vertices):
        # Constructor de la clase Grafo
        self.V = vertices
        self.grafo = []  # Inicializamos la lista de aristas

    def agregar_arista(self, u, v, w):
        # M�todo para agregar una arista al grafo
        self.grafo.append([u, v, w])

    def buscar(self, padre, i):
        # Funci�n para encontrar el representante de un conjunto en Union-Find
        if padre[i] == i:
            return i
        return self.buscar(padre, padre[i])

    def union(self, padre, rango, x, y):
    # Funci�n para unir dos conjuntos en Union-Find
      raiz_x = self.buscar(padre, x)  # Encontrar la ra�z del conjunto que contiene x
      raiz_y = self.buscar(padre, y)  # Encontrar la ra�z del conjunto que contiene y

      if raiz_x != raiz_y:
        # Si las ra�ces son diferentes, x y y no est�n en el mismo conjunto y no formar�n un ciclo
        if rango[raiz_x] < rango[raiz_y]:
            # Si el conjunto de raiz_x tiene un rango (altura del �rbol) menor que el conjunto de raiz_y
            padre[raiz_x] = raiz_y  # Hacemos que raiz_x sea el padre de raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            # Si el conjunto de raiz_x tiene un rango mayor que el conjunto de raiz_y
            padre[raiz_y] = raiz_x  # Hacemos que raiz_y sea el padre de raiz_x
        else:
            # Si ambos conjuntos tienen el mismo rango
            padre[raiz_y] = raiz_x  # Hacemos que raiz_y sea el padre de raiz_x
            rango[raiz_x] += 1  # Incrementamos el rango de raiz_x para equilibrar el �rbol


    def kruskal_minimo(self):
        # Algoritmo de Kruskal para encontrar el �rbol de M�nimo Costo
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        padre = []
        rango = []
        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar(padre, u)
            y = self.buscar(padre, v)
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.union(padre, rango, x, y)

        # Imprimir el �rbol de M�nimo Costo
        print("�rbol de M�nimo Costo:")
        for u, v, peso in resultado:
            print(f"{u} - {v}: {peso}")

    def kruskal_maximo(self):
    # Algoritmo de Kruskal para encontrar el �rbol de M�ximo Costo

     resultado = []  # Inicializamos una lista para almacenar las aristas del �rbol de M�ximo Costo
     i, e = 0, 0  # Inicializamos contadores para controlar las aristas y v�rtices agregados al �rbol
     self.grafo = sorted(self.grafo, key=lambda item: -item[2])  # Ordenamos las aristas en orden descendente de peso
     padre = []  # Inicializamos una lista para representar a los padres de los conjuntos
     rango = []  # Inicializamos una lista para mantener el rango de cada conjunto

     for nodo in range(self.V):
        padre.append(nodo)  # Inicializamos a cada nodo como su propio padre al principio
        rango.append(0)     # Inicializamos el rango de cada conjunto en 0

     while e < self.V - 1:
        u, v, w = self.grafo[i]  # Tomamos la arista con el siguiente peso m�ximo
        i = i + 1
        x = self.buscar(padre, u)  # Encontramos el representante del conjunto que contiene el v�rtice u
        y = self.buscar(padre, v)  # Encontramos el representante del conjunto que contiene el v�rtice v

        if x != y:
            e = e + 1  # Incrementamos el contador de aristas agregadas al �rbol
            resultado.append([u, v, w])  # Agregamos la arista al �rbol de M�ximo Costo
            self.union(padre, rango, x, y)  # Unimos los conjuntos que contienen los v�rtices u y v

    # Imprimir el �rbol de M�ximo Costo
     print("�rbol de M�ximo Costo:")
     for u, v, peso in resultado:
      print(f"{u} - {v}: {peso}")




vertices = 4  # Definimos el n�mero de v�rtices en el grafo de ejemplo

grafo = Grafo(vertices)  # Creamos una instancia de la clase Grafo con 4 v�rtices

grafo.agregar_arista(0, 1, 10)  # Agregamos una arista entre el v�rtice 0 y el v�rtice 1 con peso 10
grafo.agregar_arista(0, 2, 6)   # Agregamos una arista entre el v�rtice 0 y el v�rtice 2 con peso 6
grafo.agregar_arista(0, 3, 5)   # Agregamos una arista entre el v�rtice 0 y el v�rtice 3 con peso 5
grafo.agregar_arista(1, 3, 15)  # Agregamos una arista entre el v�rtice 1 y el v�rtice 3 con peso 15
grafo.agregar_arista(2, 3, 4)   # Agregamos una arista entre el v�rtice 2 y el v�rtice 3 con peso 4

# Encontrar y mostrar el �rbol de M�nimo Costo
grafo.kruskal_minimo()

# Encontrar y mostrar el �rbol de M�ximo Costo
grafo.kruskal_maximo()

# Encontrar y mostrar el �rbol de M�nimo Costo
grafo.kruskal_minimo()

# Encontrar y mostrar el �rbol de M�ximo Costo
grafo.kruskal_maximo()

