import modules.corefile as cf
import funciones.globales as gf
import funciones.pacientes as uipc
import main

def MenuPacientes(op : int):
    title ="""
     
     ➖Modulo administrador del paciente ➖
    
    """
    MenupacientesOp ='1. agregar nuevo paciente\n2. editar\n3. eliminar cita\n4. salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(MenupacientesOp)
        try:
            op = int(input(':'))
        except ValueError:
            print('opcion no tiene formato adecuado')
            gf.pausar_pantalla()
            MenuPacientes(0)
        else:
            match (op):
                case 1:
                    uipc.Newpacientes()
                case 2:
                    print
                    uipc.ModifyData()
                case 3:
                   pass
                case 4:
                    main.mainMenu(0)
                case _:
                    print('la opcion ingresada no esta disponible en las opciones')
                    gf.pausar_pantalla()
