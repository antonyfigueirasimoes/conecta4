def crea_tablero(columnas,filas):

  matrix = []
  for i in range(filas):
    lists = []
    for j in range(columnas):
      lists.append(0)
    matrix.append(lists)

  return matrix

def juega(tablero, columna, valor_ficha):

  '''
  elegir la columna del tablero
  recorrer la columna desde atras hacia delante
    al encontrar el primer cero, lo sustituyo por valor_ficha
  '''

  c = tablero[columna]
  indice = len(c)-1
  while indice >= 0:
    if c[indice] == 0:
      c[indice] = valor_ficha
      break
    indice -= 1

      
  