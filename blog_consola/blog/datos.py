estados_post = ["Borrador", "Publicado", "Archivado"]
etiquetas_blog = ["Tecnología", "Programación", "Python", "Desarrollo", "Tutorial"]

perfil_autor = {
    "nombre": "Ana García",
    "email": "ana.garcia@example.com",
    "rol": "Administrador"
}

posts = [
    {
        "titulo": "Introducción a Python",
        "contenido": "Python es un lenguaje de programación de alto nivel...",
        "autor": perfil_autor,
        "tags": ["Python", "Programación", "Tutorial"],
        "estado": "Publicado"
    },
    {
        "titulo": "Estructuras de datos básicas",
        "contenido": "Las listas y diccionarios son fundamentales en el desarrollo...",
        "autor": perfil_autor,
        "tags": ["Programación", "Desarrollo"],
        "estado": "Publicado"
    },
    {
        "titulo": "Errores comunes en programación",
        "contenido": "", 
        "autor": {"email": "sin.nombre@example.com"}, 
        "tags": "Errores", 
        "estado": "Invalido"
    }
]