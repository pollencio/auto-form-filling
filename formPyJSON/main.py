import json

header = '''
[
  { "project" : "Proyecto+El%C3%A9ctrica",
    "meetingType" : "Reunión",
    "meetingPlaceLink" : "https://meet.google.com/qkm-huuu-ngz"
  }
]'''

asistentes = '''
[
  {
    "Celular": "3134565945",
    "Correo": "jparrar@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1019149202",
    "Facultad": "Ingeniería",
    "Genero": "Hombre",
    "Nombre": "Juan Felipe Parra Runceria",
    "Programa": "Ingeniería Mecánica",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3002806139",
    "Correo": "agochoad@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1090388349",
    "Facultad": "Ingeniería",
    "Genero": "Hombre",
    "Nombre": "Alexei Gabriel Ochoa Duarte",
    "Programa": "Doctorado en Ingeniería - Industria y Organizaciones",
    "Tipo": "Estudiante de Postgrado"
  },
  {
    "Celular": "3058893762",
    "Correo": "izarater@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1014258629",
    "Facultad": "Ingeniería",
    "Genero": "Hombre",
    "Nombre": "Isaac Zarate Reyes",
    "Programa": "Ingeniería de Sistemas y Computación",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3004522632",
    "Correo": "Dteranf@unal.edu.co ",
    "Discapacidad": "No",
    "Documento": "1019153786",
    "Facultad": "Ingeniería ",
    "Genero": "Hombre",
    "Nombre": "Daniel Alejandro Teran Fernandez",
    "Programa": "Ingeniería electrica",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3003460990",
    "Correo": "bgaleanom@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1000725766",
    "Facultad": "Ingeniería",
    "Genero": "Hombre",
    "Nombre": "Brandon Alexis Galeano Martinez",
    "Programa": "Ing. Electrónica ",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3015462386",
    "Correo": "yatorresm@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1032501894",
    "Facultad": "Ingeniería",
    "Genero": "Mujer",
    "Nombre": "Yeliana Andrea Torres Medina",
    "Programa": "Ingeniería de Sistemas y Computación",
    "Tipo": "Egresado"
  },
  {
    "Celular": "3204699182",
    "Correo": "lkserratot@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1013674836",
    "Facultad": "Ingeniería",
    "Genero": "Mujer",
    "Nombre": "Leidy Katherine Serrato Triviño",
    "Programa": "Ingeniería química",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3144864938",
    "Correo": "sabrilg@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1016093109",
    "Facultad": "Ingenieria",
    "Genero": "Hombre",
    "Nombre": "Sebastian Abril Gonzalez",
    "Programa": "Ingenieria electrica",
    "Tipo": "Egresado"
  },
  {
    "Celular": "3196988470",
    "Correo": "jipmorenoch@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1015473551",
    "Facultad": "Medicina",
    "Genero": "Mujer",
    "Nombre": "Jimena del Pilar Moreno Chaves",
    "Programa": "Medicina",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3203269157",
    "Correo": "bdquinteror@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1070967970",
    "Facultad": "Ingeniería",
    "Genero": "Hombre",
    "Nombre": "Brayan David Quintero Ramos",
    "Programa": "Ingeniería electrónica",
    "Tipo": "Estudiante de pregrado"
  },
  {
    "Celular": "3194404172",
    "Correo": "Caprietog@unal.edu.co",
    "Discapacidad": "No",
    "Documento": "1000364337",
    "Facultad": "Ingenieria",
    "Genero": "Hombre",
    "Nombre": "Camilo Prieto Gomez",
    "Programa": "Ingenieria electrica ",
    "Tipo": "Estudiante de pregrado"
  }
]'''

reuniones = '''
[
  {
    "Fecha": "February 10, 2022",
    "Participantes": "Juan Felipe Parra Runceria, Isaac Zarate Reyes, Sebastian Abril Gonzalez, Brayan David Quintero Ramos"
  },
  {
    "Fecha": "January 19, 2022",
    "Participantes": "Alexei Gabriel Ochoa Duarte, Juan Felipe Parra Runceria, Isaac Zarate Reyes, Yeliana Andrea Torres Medina"
  },
  {
    "Fecha": "November 26, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Daniel Alejandro Teran Fernandez, Alexei Gabriel Ochoa Duarte, Yeliana Andrea Torres Medina"
  },
  {
    "Fecha": "November 20, 2021",
    "Participantes": "Yeliana Andrea Torres Medina, Alexei Gabriel Ochoa Duarte, Juan Felipe Parra Runceria, Isaac Zarate Reyes"
  },
  {
    "Fecha": "November 19, 2021",
    "Participantes": "Yeliana Andrea Torres Medina, Alexei Gabriel Ochoa Duarte, Juan Felipe Parra Runceria, Isaac Zarate Reyes"
  },
  {
    "Fecha": "November 16, 2021",
    "Participantes": "Isaac Zarate Reyes, Alexei Gabriel Ochoa Duarte, Yeliana Andrea Torres Medina, Juan Felipe Parra Runceria"
  },
  {
    "Fecha": "November 13, 2021",
    "Participantes": "Isaac Zarate Reyes, Brandon Alexis Galeano Martinez, Daniel Alejandro Teran Fernandez, Juan Felipe Parra Runceria, Yeliana Andrea Torres Medina"
  },
  {
    "Fecha": "November 12, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Yeliana Andrea Torres Medina, Isaac Zarate Reyes"
  },
  {
    "Fecha": "November 12, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Isaac Zarate Reyes, Alexei Gabriel Ochoa Duarte, Sebastian Abril Gonzalez, Daniel Alejandro Teran Fernandez"
  },
  {
    "Fecha": "November 12, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Isaac Zarate Reyes, Alexei Gabriel Ochoa Duarte"
  },
  {
    "Fecha": "November 11, 2021",
    "Participantes": "Isaac Zarate Reyes, Daniel Alejandro Teran Fernandez, Juan Felipe Parra Runceria"
  },
  {
    "Fecha": "November 6, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Daniel Alejandro Teran Fernandez, Camilo Prieto Gomez, Isaac Zarate Reyes"
  },
  {
    "Fecha": "November 5, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Isaac Zarate Reyes, Daniel Alejandro Teran Fernandez, Alexei Gabriel Ochoa Duarte, Yeliana Andrea Torres Medina"
  },
  {
    "Fecha": "October 29, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Alexei Gabriel Ochoa Duarte, Daniel Alejandro Teran Fernandez, Yeliana Andrea Torres Medina"
  },
  {
    "Fecha": "October 19, 2021",
    "Participantes": "Juan Felipe Parra Runceria, Isaac Zarate Reyes, Yeliana Andrea Torres Medina, Daniel Alejandro Teran Fernandez"
  },
  {
    "Fecha": "October 5, 2021",
    "Participantes": "Alexei Gabriel Ochoa Duarte, Isaac Zarate Reyes, Sebastian Abril Gonzalez, Daniel Alejandro Teran Fernandez"
  }
]'''


def convertir(fecha, mesesNum):
    resultado = []

    filtro_1 = fecha.split(",")
    filtro_2 = filtro_1[0].split(" ")
    anio = filtro_1[1]
    mes, dia = filtro_2[0], filtro_2[1]
    resultado.append(anio)

    for i in mesesNum:
        mesNombre = i[0]
        if (mesNombre == mes):
            resultado.append(i[1])
            break

    resultado.append(dia)
    resultado = "-".join(resultado)

    for x in resultado:
        resultado = resultado.replace(" ", "")

    return resultado


mesesNum = [["January", "01"], ["February", "02"], ["March", "03"], ["April", "04"], ["May", "05"], ["June", "06"],
            ["July", "07"], ["August", "08"], ["September", "09"], ["October", "10"], ["November", "11"],
            ["December", "12"]]

def imprimir_Inicio(header):
    head = json.loads(header)
    for item in head:
        with open('data.txt', 'a') as f:
            f.write("{"+'project:'+ '"' + item['project'] + '",'+'meetingType:'+ '"' + item['meetingType'] + '",'+'meetingPlaceLink:'+ '"' + item['meetingPlaceLink'] + '",')

        print("{")
        print('project:', '"' + item['project'] + '",')
        print('meetingType:', '"' + item['meetingType'] + '",')
        print('meetingPlaceLink:', '"' + item['meetingPlaceLink'] + '",')

gente = json.loads(asistentes)
reus = json.loads(reuniones)
#print('User count:', len(info))

print("[")
for item in reus:
    arreglo = list()
    arreglo = item['Participantes'].split(", ")
    '''print (arreglo)'''
    for registro in arreglo:
        for persona in gente:
            '''print(persona['Nombre'])
            print(registro)'''
            if (persona['Nombre'] == registro):
                imprimir_Inicio(header)
                print('date:'+ '"' + convertir(item['Fecha'], mesesNum) + '",')
                print('fullName:'+ '"' + persona['Nombre'] + '",')
                print('documentId:' + '"' + persona['Documento'] + '",')
                print('email:' + '"' + persona['Correo'] + '",')
                print('gender:' + '"' + persona['Genero'] + '",')
                print('disability:' + '"' + persona['Discapacidad'] + '",')
                print('cellphone:' + '"' + persona['Celular'] + '",')
                print('userType:' + '"' + persona['Tipo'] + '",')
                print('academicProgram:' + '"' + persona['Programa'] + '",')
                print('faculty:' + '"' + persona['Facultad'] + '"')
                print("},")
                with open('data.txt', 'a') as f:
                    f.write('date:'+ '"' + convertir(item['Fecha'], mesesNum) + '",'+'fullName:'+ '"' + persona['Nombre'] + '",'+'documentId:' + '"' + persona['Documento'] + '",'+'email:' + '"' + persona['Correo'] + '",'+'gender:' + '"' + persona['Genero'] + '",'+'disability:' + '"' + persona['Discapacidad'] + '",'+'cellphone:' + '"' + persona['Celular'] + '",'+'userType:' + '"' + persona['Tipo'] + '",'+'academicProgram:' + '"' + persona['Programa'] + '",'+'faculty:' + '"' + persona['Facultad'] + '"'+"},")
                    f.close()


print("]")

'''print('date:', "2021-09-28")'''
