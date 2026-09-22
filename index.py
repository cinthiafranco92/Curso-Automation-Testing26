from productos import (
     mostrar_productos,
    agregar_producto,
    mostrar_producto,
    buscar_producto,
    eliminar_producto,
    buscar_por_precio,
    mostrar_estadisticas
    )
from menu import mostrar_menu

#import productos


def index():
     while True:
          mostrar_menu()

          op = input("Seleccionar: ").strip()

          match op:
               case "1":
                    agregar_producto()

                    








if __name__ == "__main__":
     index()

