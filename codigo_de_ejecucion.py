import cloudpickle
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

def ejecutar_modelos(df):

    #6.CARGA PIPE DE EJECUCION

    ruta_proyecto = r'C:\Users\iagzg\Desktop\D4FB\D4FB\EstructuraDirectorio\03_MACHINE_LEARNING\06-MACHINE LEARNING PROJECT FRAMEWORK\CASOS\04_BANK\\'

    nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'

    ruta_pipe_ejecucion = ruta_proyecto + '/04_Modelos/' + nombre_pipe_ejecucion

    with open(ruta_pipe_ejecucion, mode='rb') as file:
       pipe_ejecucion = cloudpickle.load(file)

    #7.EJECUCION
    scoring = pipe_ejecucion.predict_proba(df)[:, 1]

    return(scoring)
