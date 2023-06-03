# Fill in this file with the code from parsing JSON exercise
import urllib.parse
import requests
import googletrans



main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "dfoihUUVeX6cb9OY5QEscv5EB4dIRO6Y"

#Aqui se ingresa el origen y el destino
while True:
    orig = input("Ciudad de origen: ")
    if orig == "exit":
        break
    
    dest = input("Ciudad de destino: ")
    if dest == "exit":
        break

#Aqui muestra la url y verifica si es unarespuesta exitosa

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

  
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    


    if json_status == 0 :
        print("API Status: " + str(json_status) + "= una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Ciudad de origen " + (orig) + " hasta " + (dest))
        print("Duracion  del viaje:	" + (json_data["route"]["formattedTime"])) 
        print("Millas:	" + str(json_data["route"]["distance"]))
        print("=============================================") 
        print("Kilometros:	" + str("{:.4f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
    

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
            print("=============================================\n")
    elif json_status == 402: 
        print("**********************************************")
        print("Status del codigo: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n") 
    else:
        print("************************************************************************") 
        print("Para el estado del codigo: " + str(json_status) + "; ver:") 
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") 
        print("************************************************************************\n")



