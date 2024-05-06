import json
import os
import funciones.globales as gf
import modules.corefile as cf
import ui.uicitas as uic
def Newcitas():
    title ="""
    **********************************
    *    agendar citas medicas       *
    **********************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input('ingrese el numero del identificacion : ')
    codpaciente = input('ingrese codigo del paciente : ')
    nombrepaciente = input('ingrese nombre del pacientee : ')
    telefono = input('ingrese numero celular :')
    correoelectronico = input('ingrese el correo electronico : ')
    pacientes ={
        'identificacion': identificacion,
        'codpaciente': codpaciente,
        'nombrepaciente': nombrepaciente,
        'telefono' : telefono,
        'correo electronico':correoelectronico
}
    cf.AddData('data',identificacion,pacientes,codpaciente,telefono,correoelectronico)
    gf.centro_medico_AL.get('data').update({identificacion:pacientes})
    if(bool(input('desea registar otro oaciente s(si) o enter (no)'))):
      Newcitas()
    else:
        uic.MenuPacientes(0)
def SearchData():
    criterio = input('Ingrese el Nro Identificacion del paciente: ')
    data=gf.centro_medico_AL.get('data').get(criterio)
    return data
    

def ModifyData():
    print (gf.centro_medico_AL())
    datapacientes = SearchData()
    identificacion,pacientes,codpaciente,telefono,correoelectronico = datapacientes.values()
    for key in datapacientes.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                datapacientes[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.centro_medico_AL.get('data').update({identificacion:datapacientes})
    cf.updatefile(gf.centro_medico_AL)
    uic.Menucitas(0)