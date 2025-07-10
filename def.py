productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],                       
            "2175HD": ["Acer", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"], 
            "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"], 
            "fgdxFHD": ["HP", 15.6, "12GB", "DD", "1T", "Intel Core i3", "integrada"], 
            "GF75HD": ["Asus", 15.6, "12GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],                      
            "123FHD": ["Acer", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"], 
            "342FHD": ["Acer", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
            "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
         }

stock = {"8475HD": [387990,10], "2175HD": [327990,4], "JjfFHD": [424990,1],               
         "fgdxFHD": [664990,21], "123FHD": [290890,32], "342FHD": [444990,7], 
         "GF75HD": [749990,2], "UWU131HD": [349990,1], "FS1230HD": [249990,0],
        }


def stock_marca (marca):
    total=0
    for m,d in productos.items():
            if (m[0]).lower() == (marca[0]).lower():
                 total += stock.get(d[0, 1])
    print(f"el stock es de: {total}")

def búsqueda_precio(p_min, p_max):
    for i in  stock.items():
        if i[0] > p_max or i [0] < p_min:
            print("")
              

def eliminar_producto(Modelo):
     for e in productos.items():
          if e[0].lower() == Modelo[0].lower():
               e.pop(modelo)

opcion = 0 
while opcion !=4:
    print("1. Stock marca.  ")
    print("2. Búsqueda por precio.  ")
    print("3. Eliminar producto.  ")
    print("4. Salir.  ")
    opcion=int(input("ingrese una opcion : "))
    match opcion:
        case 1:
            marca=input("Consulte el stock de su marca ")
            stock_marca (marca)
                 
        case 2:
              precio=input("precio a consultar")
        case 3:     
            modelo=input("ingrese el modelo que desea eliminar: ")
            if modelo in productos:
                 eliminar_producto(modelo)
                 print("ha eliminado con exito")
            else:
                 print("no se ha encontrado")
        case 4:
              break