#ejemplo de uso de repositorio


print("datos personales")
print("<><><><><><><><><><><><><><><><>")
Vnom=input("ingrese su nombre:")
while True:
    try:
        
        VEdad= int(input("ingrese su edad:"))
        break
    except:
        print("dato no valido")
print("<><><><><><><><><><><><><><><><>")
print(f"Su nombre es:{Vnom}")
print(f"Su edad es:{VEdad} ")
print("fin el programa............")