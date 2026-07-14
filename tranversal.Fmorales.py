print("Bienvenido a la tienda de ropa StyleShop")
prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon',True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester',True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon',True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon',False],
    ...
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
    ...
}

def validar_menu(menu):                                                                                                                      

    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoria")
    print("2. Busqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True
        try:
        opcion = int(input("ingrese una opcion, valida que el valor ingresado sea un numero entero y que este dentro del rango de opciones válidas del menu"))
        if 1 < opcion <=6
            return
        else:
            print("Error: debes ingresar una opcion valida")
        except Valueerror:
            print ("Error: debes ingresar una opcion valida")

def variable_texto(texto):
    return texto.strip()!=""

def validar_entero_mayor_cero(numero):
    return numero > 0 

def validar_entero_mayor_igual_cero(numero):
    return numero >= 0

def validar_opcion_sn(opcion):
    return opcion.lower() in ["s", "n"]

def buscar_codigo(codigo, prendas):
    return codigo.upper() in prendas

#opcion numero 1    

def unidades_categoria(categoria):
    total_unidades = 0 
    categoria_buscada = marca.lower()
    for codigo, datos in prendas.items():
        categoria_prenda = datos [1].lower ()
        if categoria_prenda == categoria_buscada:
            total_unidades += bodega[codigo][1]
            print(f" total de prendas {categoria}{total_unidades}")

def busqueda_precio(p_min, p_max, prendas, bodega)
    return []
    for codigo, datos_bodega in bodega.items():
        precio = datos_bodega [0]
        Unidades = datos_bodega[1]

        if p_min <= precio <= p_max and Unidades > 0:
            modelo = prendas [codigo][0]
            resultado.append (f"{modelo}--{codigo}")
    if len (resultado) > 0:
        for item in sorted (resultado) :
            print(item)
    else:
        print("no hay prendas en este rango de precios")
        