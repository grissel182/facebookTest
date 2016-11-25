from usuario import Usuario

user = Usuario()
print(type(user))
print ("nombre de usuario antes de peticion")
print (user.nombre)

respuesta = user.obtenerInfo()
print("Respuesta es:")
print(type(respuesta))



