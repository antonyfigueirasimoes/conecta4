from juego_functions import crea_tablero, juega, esta_llena

def test_crear_tablero():
  tab = crea_tablero(4,3)

  assert tab == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def test_add_ficha_a_tablero():
  tab = crea_tablero(4,3)
  juega(tab, 2, 1)

  assert tab == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]

def test_comprobar_columna_llena():
  tab = crea_tablero(4,3)
  juega(tab,2,'x')
  juega(tab,2,'x')
  juega(tab,2,'x')
  juega(tab,2,'x')

  assert esta_llena(tab, 2) == True
