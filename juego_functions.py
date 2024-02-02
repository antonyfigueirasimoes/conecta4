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

def esta_llena(tablero, columna):

  '''
  elegir la columna del tablero
  recorrer la columna desde atras hacia adelante
    verificamos si todas tienen una ficha o no
  # '''
  # res = False
  # c = tablero[columna]
  # indice = len(c)-1
  # while indice >= 0:
  #   if c[indice] == 1:
  #     res = True
  #   indice -=1

  # return res // FUNCIONA
  c = tablero[columna]
  return 0 not in c #Mucho mejor. Verifica cualquier valor que quiera se usado como "ficha de jugador"
      
      
      
  