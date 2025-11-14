import pandas as pd

def leer_excel_seguro(ruta):
    """
    Lee un archivo Excel que puede tener múltiples hojas y devuelve un diccionario {nombre_hoja: df}.
    """
    try:
        datos = pd.read_excel(ruta, sheet_name=None, engine="openpyxl")
        return datos
    except Exception as e:
        print(f"Error leyendo {ruta}: {e}")
        return {}
