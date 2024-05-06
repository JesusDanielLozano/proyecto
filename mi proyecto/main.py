import modules.corefileSp as cfsp
import modules.corefile as cf
import funciones.globales as fg
import ui.uipacientes as uipc
import ui.uiespecialistas as uisp
import ui.uicitas as uict

def main():
    cf.MY_DATABASE = 'data/pacientes.json'
    cf.chekFile(fg.centro_medico_AL)
    op = 0  # Opcional: Puedes definir la opción que desees enviar a la función mainMenu(op)
    mainMenu(op)

def mainMenu(op):
    fg.borrar_pantalla()
    title ="""
  
    🟩      🏥💉🩺 Centro Médico 🩺💉🏥   🟩
 
        """
    mainMenuOp = '1. medico\n2. pacientes\n3. agendar cita\n4. consultar cita\n5. salir '
    if (op != 3):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':)'))
        except ValueError:
            print('error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            match opcion:
                case 1:
                    uisp.MenuEspecialistas(0)
                case 2:
                    uipc.MenuPacientes(0)
                case 3:
                    uict.Menucitas(0)
                case 4:
                    print('opcion ingresada no PROGRAMADA AUN')
                    fg.pausar_pantalla()
                   
                case _:
                    print('opcion no valida, ingrese un numero de la lista')
                    fg.pausar_pantalla()
                    mainMenu(0)

if __name__ == '__main__':
    main()
    cf.centro_medico_AL = 'data/alumnos.json'
    cfsp.centro_medico_AL = 'data/alumnos.json'
    cf.checkFile(fg.centro_medico_AL)
    cfsp.checkFile(fg.centro_medico_AL)

    mainMenu(0)