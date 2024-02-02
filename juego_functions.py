def crea_tablero(columnas,filas):

  matrix = []
  for i in range(filas):
    lists = []
    for j in range(columnas):
      lists.append(0)
    matrix.append(lists)

  return matrix
