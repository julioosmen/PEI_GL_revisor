import pandas as pd
from modules.utilidades import leer_excel_seguro

def extraer_tablas(archivo):
    """
    Extrae las tablas OEI y AEI desde el archivo subido (Word o PDF).
    Retorna un diccionario con DataFrames, por ejemplo:
    {"OEI": df_oei, "AEI": df_aei}
    """
    # TODO: Aquí va tu lógica actual de extracción (ya la tienes implementada)
    # El resultado debe ser un diccionario con dataframes.
    tablas_extraidas = {
        "OEI": pd.DataFrame(),  # Reemplazar con el real
        "AEI": pd.DataFrame()   # Reemplazar con el real
    }
    return tablas_extraidas


def comparar_elementos(tablas_extraidas):
    """
    Compara los elementos extraídos con los estándares internos.
    Retorna:
        resultado_comparacion (dict),
        oei_extraidos (DataFrame),
        aei_extraidos (DataFrame)
    """
    estandar = leer_excel_seguro("data/tablas_estandar.xlsx")

    oei_std = estandar.get("OEI", pd.DataFrame())
    aei_std = estandar.get("AEI", pd.DataFrame())

    oei_extraidos = tablas_extraidas.get("OEI", pd.DataFrame())
    aei_extraidos = tablas_extraidas.get("AEI", pd.DataFrame())

    # Comparación simple por código (puedes afinar según tus columnas reales)
    resultado_oei = oei_extraidos.merge(
        oei_std, on="Codigo OEI", how="left", indicator=True
    )
    resultado_aei = aei_extraidos.merge(
        aei_std, on="Codigo AEI", how="left", indicator=True
    )

    resultado = {"OEI": resultado_oei, "AEI": resultado_aei}
    return resultado, oei_extraidos, aei_extraidos
