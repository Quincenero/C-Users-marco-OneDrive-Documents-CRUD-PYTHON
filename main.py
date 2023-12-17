
import PersonaDatos as per
persona = {
    "dni":"123456",
    "edad":"werr",
    "nombre":"Marco",
    "apellido":"Espinoza",
    "direccion":"Buernos Aires",
    "correo":"marc1.@per.co"
    
}
res = per.save(persona)
print(res)