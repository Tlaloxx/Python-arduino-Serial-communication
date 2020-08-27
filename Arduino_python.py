from arduino_python_library import SerialToExcel

serialToExcel = SerialToExcel("/dev/ttyACM0",9600)

columnas = ["Lectura","Valor"]

serialToExcel.setColumns(["Lectura","Valor"])
serialToExcel.setRecordsNumber(1000)
serialToExcel.readPort()

serialToExcel.writeFile("arduino_data.xls") 

