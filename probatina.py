def tablero(columnas,filas):

  matrix = []
  for i in range(filas):
    lists = []
    for j in range(columnas):
      lists.append(0)
    matrix.append(lists)

  return matrix

salida = [

  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],

]
print(tablero(7,6))

assert tablero(7, 6) == salida, "No son iguales"