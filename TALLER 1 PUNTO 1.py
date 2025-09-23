def menu():
    """Muestra el menú principal."""
    print("\n Menú Lista de Reproduccion ")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Mostrar lista")
    print("4. Buscar canción")
    print("5. Salir")


def normalizar(texto):
    """Convierte texto a minúsculas y elimina espacios extras."""
    return texto.strip().lower()


def agregar_cancion(playlist):
    cancion = input("Ingrese el nombre de la canción: ").strip()
    if not cancion:
        print(" No se puede agregar un nombre vacío.")
        return

    if normalizar(cancion) in [normalizar(song) for song in playlist]:
        print(f" La canción '{cancion}' ya está en la playlist.")
    else:
        playlist.append(cancion)
        playlist.sort() 
        print(f" '{cancion}' fue agregada a la playlist.")
      


def eliminar_cancion(playlist):
    cancion = input("Ingrese el nombre de la canción a eliminar: ").strip()
    for song in playlist:
        if normalizar(song) == normalizar(cancion):
            playlist.remove(song)
            print(f" '{song}' fue eliminada de la playlist.")
            mostrar_playlist(playlist)  # Mostrar lista tras eliminar
            return
    print(f"La canción '{cancion}' no está en la playlist.")


def mostrar_playlist(playlist):
    if playlist:
        playlist.sort()  
        print(" Tu playlist actual:")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")
    else:
        print(" La playlist está vacía.")



def buscar_cancion(playlist):
    buscar = input("Ingrese el nombre de la canción a buscar: ").strip()
    for song in playlist:
        if normalizar(song) == normalizar(buscar):
            print(f" La canción '{song}' está en la playlist.")
            return
    print(f"La canción '{buscar}' no está en la playlist.")


def main():
    playlist = []

    while True:
        menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            agregar_cancion(playlist)
        elif opcion == "2":
            eliminar_cancion(playlist)
        elif opcion == "3":
            mostrar_playlist(playlist)
        elif opcion == "4":
            buscar_cancion(playlist)
        elif opcion == "5":
            print("Gracias por usar la playlist. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")


if __name__ == "__main__":
    main()
