from login import Login


if __name__ == "__main__":
    print("Hola mundo desde Python")
    
    logear = Login()
    logear.idLogin          = 1
    logear.correo           = "logear90@gmail.com"
    logear.contraseña       = "log45.lo"
    
    print(vars(logear))