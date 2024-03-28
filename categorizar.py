internacionales = ["LIL", "RAK", "VCE"]
nacionales = ["OVD", "MAD", "ZAZ"]

def categorizar(entrada):
    resultado = "Interinsular"
    
    for destino in entrada:
        if destino in internacionales:
            return "Internacional"
        elif destino in nacionales:
            resultado = "Nacional"
    
    return resultado

#Pruebas    
print(categorizar(["LPA", "VCE"]))
print(categorizar(["ZAZ", "LPA", "RAK"]))
print(categorizar(["LPA", "TFN"]))
print(categorizar(["LPA", "TFN", "OVD"]))