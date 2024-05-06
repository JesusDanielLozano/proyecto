import json
import os
import funciones.globales as gf
import modules.corefileSp as cfsp
import ui.uiespecialistas as uisp
def NewSpecialistas():
    title ="""
    ************************************
    * 🧑‍⚕️ registro de especialistas 👩‍⚕️ *
    ************************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input('ingrese el numero Cedula : ')
    codespecialista = input('ingrese codigo del medico : ')
    nombreMedico = input('ingrese nombre del medico : ')
    especializacion = input('seleciones: ')
    Especialistas ={
        'identificacion': identificacion,
        'codpaciente': codespecialista,
        'nombrepaciente': nombreMedico,
        'especializacion':especializacion
}
    cfsp.AddData('data',identificacion,Especialistas)
    gf.centro_medico_AL.get('data').update({identificacion:Especialistas})
    if(bool(input('registar otro medico s(si) o enter (no)'))):
      NewSpecialistas()
    else:
        uisp.MenuEspecialistas(0)
def SearchData():
    criterio = input('Ingrese el Nro Identificacion del estudiante: ')
    data=gf.centro_medico_AL.get('data').get(criterio)
    return data
    

def ModifyData():
    dataespecialistas = SearchData()
    identificacion,codStudent,nombreStudent,notas = dataespecialistas.values()
    for key in dataespecialistas.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataespecialistas[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.centro_medico_AL.get('data').update({identificacion:dataespecialistas})
    cfsp.Updatafilesp(gf.centro_medico_AL)
    uisp.MenuEspecialistas(0)