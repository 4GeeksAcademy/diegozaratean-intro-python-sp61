print('hola')

## Javascritp  ===== python
## // /**/ ====== #
# console.log('hola') === print('hola')

# generoPelicula. ==== genero_pelicula
# integer string boolenos === integer string boolenos
# true === True
# undefined null isNan === none
# Objetos === Diccionarios
# Arrays ==== Listas y Tuplas


# name = 'diego'
# last_name = 'zarate'
# edad = 38
# esta_vivo = True
# print(name , last_name)
# print(name + last_name)
# print('hola mi nombre es '+ name)
# # cast int() str()
# print('hola mi edad es '+ str(edad))
# print('hola mi edad es ', edad)
# segundo_numero = "10"
# print(edad + int(segundo_numero))

# decalracion de diccionarios
# js const objeto = {}
# persona = {
#     "nombre": "diego",
#     "edad": 38,
# }
# print(persona)
# print(persona["nombre"])


# # declaracion de lista
# # js const array = [ele1,ele2]
# skills = ['js','react','python']
# print(skills)
# skills.append('bootstrap')
# print(skills)

# # declaracion de tupla
# cardinales = ('Norte','Sur','Este','Oeste')
# print(cardinales)
# # cardinales.append('noroeste')
# print(cardinales)



# people_list = [{"name":"Santiago"},{"name":"Johana"},{"name":"Diego"}]

# # map 
# # js array.map( (elemento)=> codigo iterativo )
# resultado = map(lambda elemento: elemento['name'] , people_list)
# print(resultado)
# print(list(resultado))

# frutas = ['manzana', 'pera','mango']
# print(frutas)
# frutas_plural = map(lambda fruta: fruta + 's', frutas)
# print(frutas_plural)
# print(list(frutas_plural))


# funciones
# function nombrFuncion(){
#   console.log('hola')
#}
# def numeros():
#     print('soy numeros')

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# numeros()

# def saludar(nombre):
#     print('hola ' + nombre)

# saludar('blondy')
# saludar('dany')
# saludar('juan')



# procesos iterativos / bucles / loops
# colores = ['amarillo','blanco', 'verde']
# for color in colores:
#     print(color) 

# # if / else
# edad = 5
# if edad < 18:
#     print('No puedes beber')
# elif edad > 65:
#     print('Puedes beber, pero no deberias')
# else:
#     print('Puedes beber')


# class
class Carro:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def serialize(self):
        return{
             'Marca':self.marca,
             'modelo':self.modelo,
             'color':self.color,
             }
    

coche_ares = Carro('toyota','corolla','negro')
coche_dany = Carro('volswaguen','golf','gris perla')
print(coche_ares.marca)
print(coche_ares.modelo)
print(coche_ares.color)
print(coche_ares)
# print(list(coche_ares))


print(coche_ares.serialize())
print(coche_dany.serialize())



class Soltero:
    def __init__(self,cualidades,hobbies,estado_civil,defectos,historial_amoroso):
        self.cualidades = cualidades
        self.hobbies = hobbies
        self.estado_civil = estado_civil
        self.defectos = defectos
        self.historial_amoroso = historial_amoroso

    def serialize(self):
        return{
             'cualidades':self.cualidades,
             'estado_civil':self.estado_civil,
             'hobbies':self.hobbies,
             "calificacion": 5
             }

laura = Soltero('deportias, cariñosa, inteligente, divertida', 'videojuegos, senderismo, gimnassio,','soltera','toxica, posesiva, mimada, mentirosa, cleptomaa','5 divorcios, 45 realciones falidas , una denucia en juzgado')

print(laura.serialize())


#paquetes
# Js npm ==== package.json
# python pip ==== pipfile
# pip ===== pipenv