import pickle
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

os.chdir('app_riesgos')

def ejecutar_modelos(df):
    # Ruta correcta al archivo pickle
    archivo_pipe = 'pipe_ejecucion.pickle'
    
    if not os.path.isfile(archivo_pipe):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {archivo_pipe}")

    try:
        with open(archivo_pipe, mode='rb') as file:
            pipe_ejecucion = pickle.load(file)
    except Exception as e:
        raise RuntimeError(f"Error al cargar el archivo pickle: {e}")

    #7.EJECUCION
    scoring = pipe_ejecucion.predict_proba(df)[:, 1]

    return scoring
