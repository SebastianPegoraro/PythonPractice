def pruebaException():
    try: 
        number=10
        string="hola"
        print(number + string)
        print(number/2)
    except ZeroDivisionError:
        print("Div 0")
    except (ValueError, TypeError):
        print("error")



pruebaException()
