import cloudpickle
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

def ejecutar_modelos(df):

    #6.CARGA PIPE DE EJECUCION

    with open('pipe_ejecucion.pickle', mode='rb') as file:
       pipe_ejecucion = cloudpickle.load(file)

    #7.EJECUCION
    scoring = pipe_ejecucion.predict_proba(df)[:, 1]

    return(scoring)
