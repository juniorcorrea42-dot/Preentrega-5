from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            listar_posts(posts)
            
        elif opcion == '2':
            termino = input("Ingresa el título a buscar: ")
            buscar_por_titulo(posts, termino)
            
        elif opcion == '3':
            tag = input("Ingresa el tag para filtrar: ")
            filtrar_por_tag(posts, tag)
            
        elif opcion == '4':
            print("\n--- VALIDACIÓN DE POSTS ---")
            for i, post in enumerate(posts, 1):
                titulo_post = post.get("titulo", f"Post {i}")
                es_valido, errores = validar_post(post)
                if es_valido:
                    print(f"[OK] El post '{titulo_post}' es válido.")
                else:
                    print(f"[ERROR] El post '{titulo_post}' tiene los siguientes errores:")
                    for error in errores:
                        print(f"  - {error}")
                        
        elif opcion == '5':
            print("\n¡Gracias por usar el sistema de blog! Hasta luego.")
            break
            
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()