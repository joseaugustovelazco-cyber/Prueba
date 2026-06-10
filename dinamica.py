def emparejar_datos






def purificar_archivo(archivo:str)->str:
  viejo_archivo = open(archivo)
  nuevo_archivo = open("archivo_limpio.txt", "w")
  for lineas in viejo_archivo:
    lineas = emparejar_datos(lineas)
    nuevo_archivo.write(lineas)
  viejo_archivo.close()
  nuevo_archivo.close()
  
