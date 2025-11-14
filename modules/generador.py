import pandas as pd

def generar_ruta_estrategica(oei_df, aei_df):
    """
    Genera la tabla de Ruta Estratégica combinando OEI y AEI extraídos
    con sus vínculos PGG (data/vinculacion_pgg.xlsx).
    """
    vinculos = pd.read_excel("data/vinculacion_pgg.xlsx", engine="openpyxl")

    # Asegurar columnas esperadas
    # Se espera que el archivo tenga columnas:
    # 'Codigo OEI', 'Vinculación OEI-PGG', 'Codigo AEI', 'Vinculación AEI-PGG'

    oei_df = oei_df.merge(
        vinculos[["Codigo OEI", "Vinculación OEI-PGG"]],
        on="Codigo OEI",
        how="left"
    )

    aei_df = aei_df.merge(
        vinculos[["Codigo AEI", "Vinculación AEI-PGG"]],
        on="Codigo AEI",
        how="left"
    )

    # Combinar OEI y AEI en una sola tabla
    ruta = pd.merge(
        oei_df,
        aei_df,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("_OEI", "_AEI")
    )

    columnas_finales = [
        "Codigo OEI", "Denominacion OEI", "Vinculación OEI-PGG",
        "Codigo AEI", "Denominacion AEI", "Vinculación AEI-PGG"
    ]
    ruta = ruta[[col for col in columnas_finales if col in ruta.columns]]

    return ruta
