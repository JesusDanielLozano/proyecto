import json
import os

Data_Base_especialistas = 'Data/especialistas.json'

def NewFile(*param):
    with open(Data_Base_especialistas,"w") as wf:
        json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
    with open(Data_Base_especialistas,'w') as fw:
        json.dump(param[0],fw,indent=4)

def AddData(*param):
    data = list(param)
    with open(Data_Base_especialistas,"r+") as rwf:
        data_file=json.load(rwf)
        if(len(param) > 1):
            data_file[data[0]].update({data[1]:data[2]})
        else:
            data_file.update({param[0]})
        #data_file[llaveprincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def Readfile():
    with open(Data_Base_especialistas,"r") as rf:
        return json.load(rf)

def chekFile(*param):
    data = list(param)
    if(os.path.isfile(Data_Base_especialistas)):
        if(len(param)):
            data[0].update(Readfile())
    else:
        if(len(param)):
            NewFile(data[0])