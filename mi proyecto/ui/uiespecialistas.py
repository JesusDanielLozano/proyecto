import modules.corefileSp as cfsp
import funciones.globales as gf
import funciones.especialistas as uisp
import main

def MenuEspecialistas(op : int):
    title ="""
    *****************************
    *  Modulo admin del medico  *
    *****************************
    """
    MenuEspecialistasOp ='1. agregar\n2. editar\n3. eliminar\n4. salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(MenuEspecialistasOp)
        try:
            op = int(input(':'))
        except ValueError:
            print('opcion no tiene formato adecuado')
            gf.pausar_pantalla()
            MenuEspecialistas(0)
        else:
            match (op):
                case 1:
                    uisp.NewSpecialistas()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    main.mainMenu(0)
                case _:
                    print('la opcion ingresada no esta disponible en las opciones')
                    gf.pausar_pantalla()
