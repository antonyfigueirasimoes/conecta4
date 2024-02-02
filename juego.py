def crea_tablero(columnas,filas):

  matrix = []
  for i in range(filas):
    lists = []
    for j in range(columnas):
      lists.append(0)
    matrix.append(lists)

  return matrix

tablero = crea_tablero(7, 6)

#crea 2 jugadores, a los que se asigna ficha

#ir jugando por turnos
#input columna
#jugar en la columna, jugador activo
def busca_hueco(columna):
  '''
  Buscar la ultima posición vacía de la columna del tablero
  '''
  res = []
  
  for element in reversed(range(len(columna))):
    if element == 0:
      res.append[element]
  
  return res
