def tablero(filas,columnas):

  matrix = []
  for i in range(columnas):
    lists = []
    for j in range(filas):
      lists.append(0)
    matrix.append(lists)

  return matrix

salida = [

  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0]

]
print(tablero(6,7))

assert tablero(6,7) == salida, "No son iguales"