import heapq

def entrada(grafo):
    lista = []  # Creamos una lista vacia para almacenar las aristas 
    visitar = set()  # Inicializamos un conjunto vacio para llevar un registro de los nodos que hemos visitado
    #A medida que avanzamos en el grafo, agregaremos nodos a este conjunto para asegurarnos de que no los visitemos más de una vez
    nodo = list(grafo.keys())[0]  # Comenzamos desde el primer nodo
    
    # Establece el nodo inicial desde el cual comenzará el algoritmo
    cola = [(0, nodo, None)]

    while cola: # Mientras la cola no esté vacía
        peso, nodo_actual, nodo_padre = heapq.heappop(cola)# Extraer la arista con el peso mínimo

        if nodo_actual not in  visitar: #Se hace para asegurarnos de que el grafo solo se visite 1 vez
            visitar.add(nodo_actual) #Si el nodo actual no lo hemos visitado lo agregamos 
            if nodo_padre is not None:# Si el nodo actual tiene un nodo padre (excepto en el primer paso)
               lista .append((nodo_padre, nodo_actual, peso))# Agregar la arista al Árbol Parcial Mínimo

            for vecino, peso_arista in grafo[nodo_actual]:# Iterar a traves de los vecinos y pesos de las aristas
                if vecino not in  visitar: # Verificar si el vecino no ha sido visitado
                    heapq.heappush(cola, (peso_arista, vecino,nodo_actual ))# Agregar la arista a la cola 

    return lista  # Devolver la lista de aristas del Árbol Parcial Mínimo

#Creamos el grafo 
grafo = {
    'A': [('B', 2), ('D', 5)],
    'B': [('A', 2), ('D', 3), ('E', 1)],
    'C': [('E', 4)],
    'D': [('A', 5), ('B', 3), ('E', 2)],
    'E': [('B', 1), ('C', 4), ('D', 2)]
}

# Se llama a la funcion "entrada" para encontrar el Árbol Parcial Mínimo en el grafo
minimum_spanning_tree = entrada(grafo)

# Itera a travs de las aristas del Arbol Parcial Minimo y las imprime en el formato especificado
for edge in minimum_spanning_tree:
    print(f'{edge[0]} - {edge[1]}: {edge[2]}')

