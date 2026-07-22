"""
main.py
Flujo ETL: carga, inspección, clasificación y exportación de declaraciones IVA.
Sesión 6: Pandas I — Python Intermedio para Análisis de Datos · DIAN 2026
"""

# =============================================================================
# IMPORTS
# Todos los imports van aquí, al inicio del archivo, antes de cualquier otra
# línea de código. Nunca dentro de funciones ni distribuidos a lo largo del
# código. A medida que implementas cada módulo, descomenta el import
# correspondiente.
import numpy as np
import pandas as pd
from datetime import date

# Sección 3:
from src.data_loader import cargar_declaraciones
#
# Sección 4 — agrega las dos funciones nuevas al import de data_loader:
from src.data_loader import cargar_declaraciones, inspeccionar_datos, validar_nulos
#
# Sección 5:
from src.data_transformer import clasificar_por_valor, agregar_identificador_periodo, preparar_columnas_salida
#
# Sección 6:
from src.data_exporter import exportar_csv, exportar_excel_por_categoria
# =============================================================================


# =============================================================================
# CONFIGURACIÓN
# =============================================================================

RUTA_DATOS = "data/inputs/declaraciones_iva_2025.csv"
CARPETA_RESULTADOS = "data/outputs"
COLUMNAS_CRITICAS = ["nit", "valor_declarado", "estado"]
COLUMNAS_SALIDA = [
    "identificador_periodo",
    "nit",
    "razon_social",
    "municipio",
    "periodo",
    "valor_declarado",
    "nivel_riesgo",
    "estado",
]


# =============================================================================
# MENÚ
# Esta función ya está implementada. Ejecútala, lee el código y úsala como
# referencia para entender el ciclo del programa.
# =============================================================================

def mostrar_menu():
    """Muestra el menú principal y retorna la opción elegida por el usuario."""
    print("\n" + "=" * 45)
    print("  Pipeline — Declaraciones IVA 2025")
    print("=" * 45)
    print("  1. Cargar datos")
    print("  2. Inspeccionar datos")
    print("  3. Transformar datos")
    print("  4. Exportar resultados")
    print("  5. Ejecutar pipeline completo")
    print("  0. Salir")
    print("=" * 45)
    return input("  Opción: ").strip()


# =============================================================================
# PIPELINE
# __main__ solo llama a main(). La lógica vive en funciones, no a nivel de
# módulo: así puedes importar main.py desde otros scripts sin efectos.
# =============================================================================

def main():
    """Ejecuta el pipeline interactivo de declaraciones IVA."""

    # df y df_salida se declaran aquí para que todas las opciones del menú
    # puedan leerlas y modificarlas. Arrancan en None hasta que se ejecute
    # la carga.
    df = None
    df_salida = None

    opcion = mostrar_menu()

    while opcion != "0":

        # -----------------------------------------------------------------
        # OPCIÓN 1: CARGA
        # El import ya está en el bloque de arriba, solo descoméntalo.
        # Completa los espacios marcados con ___ y ejecuta.
        # -----------------------------------------------------------------
        if opcion == "1":
            # df = cargar_declaraciones(___)
            # print(f"Filas cargadas: {___}")
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 2: INSPECCIÓN
        # Tienes los nombres de las funciones. Escribe las llamadas completas.
        # Antes de llamar a inspeccionar_datos(), verifica que df no sea None;
        # si lo es, muestra un mensaje y vuelve al menú.
        # Funciones disponibles: inspeccionar_datos(), validar_nulos()
        # -----------------------------------------------------------------
        elif opcion == "2":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 3: TRANSFORMACIÓN
        # - Clasificar cada registro en nivel de riesgo (Alto / Medio / Bajo)
        #   con umbral_alto=10_000_000 y umbral_medio=5_000_000.
        # - Agregar la columna identificador_periodo.
        # - Guardar en df_salida solo las columnas de COLUMNAS_SALIDA.
        # Verifica que df no sea None antes de transformar.
        # -----------------------------------------------------------------
        elif opcion == "3":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 4: EXPORTACIÓN
        # Genera un CSV y un Excel en data/outputs/.
        # -----------------------------------------------------------------
        elif opcion == "4":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 5: PIPELINE COMPLETO
        # Ejecuta las cuatro etapas anteriores en secuencia.
        # -----------------------------------------------------------------
        elif opcion == "5":
            pass

        else:
            print("  Opción no válida. Intenta de nuevo.")

        opcion = mostrar_menu()

    print("  Hasta luego.")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
def probar_acceso_diccionario():
    declaracion = {"nit": "800234567-0", "estado": "Pendiente"}
    print(declaracion["valor_declarado"])

#Recorrer todos los pares con .items() e imprimir cada campo en una línea.
#Cambiar "estado" a "Revisada" e imprimir solo ese campo para confirmar el cambio.
def revisar_declaracion(declaracion):    
    for clave, valor in declaracion.items():
        print(clave, ":", valor)
    declaracion["estado"] = "Revisada"
    print(declaracion["estado"])

def probar_acceso_serie():
    serie = pd.Series([100, 200, 300])
    print(serie[5])

# Escribe una función explorar_dataframe() que construya un DataFrame con datos de cuatro contribuyentes, cada fila con los campos nit, razon_social, municipio y valor_declarado, e imprima .index, .columns y .shape
def explorar_dataframe():
    datos = {
    "nit": ["900123456-1", "800234567-0", "700345678-9","800333444-5"],
    "razon_social": ["Bancolombia", "Davivienda", "BBVA", "Banco Occidente"],
    "municipio": ["Huila", "Bogotá", "Cali", "Medellín"],
    "valor_declarado": [4_500_000, 12_300_000, 2_100_000, 8_750_000],    
    }
    df = pd.DataFrame(datos)
    print(df.shape)   
    print(df.index)    
    print(df.columns) 

#  Escribe una función analizar_serie(nits, valores) que reciba una lista de NITs y una lista de valores declarados, construya una Serie usando los NITs como índice, e imprima la media, el máximo, el mínimo y el NIT con el valor más alto usando las funciones que la liberería tiene definidas
def analizar_serie(nits, valores):
    serie = pd.Series(valores, index=nits)
    print("Media:", serie.mean())
    print("Mínimo:", serie.max())
    print("Máximo:", serie.min())
    print("NIT con mayor valor:", serie.idxmax())

#def probar_atributo_shape():
    #df = pd.read_csv("data/inputs/declaraciones_iva_2025.csv")
    #print(df.shape())
#probar_atributo_shape()

#def probar_np_where():
    #df = pd.read_csv("data/inputs/declaraciones_iva_2025.csv")
    #df["categoria"] = np.where(df["valor_declarado"] >= 5_000_000, "Alto", "Bajo", "Medio")
#probar_np_where()

#def probar_exportar_excel():
    #df = pd.DataFrame({"a": [1, 2]})
    #df.to_excel("data/outputs/prueba.xlsx", index=False)
#probar_exportar_excel()

if __name__ == "__main__":
     #probar_acceso_diccionario()
    declaracion = {
    "nit": "900123456-1",
    "razon_social": "Comercializadora Andina S.A.S",
    "valor_declarado": 4_500_000,
    "estado": "Presentada",
    "municipio": "Bogotá",
    }   
    #revisar_declaracion(declaracion)
    #probar_acceso_serie()
    #explorar_dataframe()
    nits   = ["900111222-0", "800333444-5", "700555666-1", "600777888-2", "500999000-3"]
    valores = [4_500_000, 12_300_000, 2_100_000, 8_750_000, 15_200_000]
    #analizar_serie(nits, valores)
    #cargar_declaraciones("data/input/declaraciones_iva_2025.csv")

    #df = cargar_declaraciones("data/inputs/declaraciones_iva_2025.csv")
    #inspeccionar_datos(df)
    #validar_nulos(df, ["nit", "valor_declarado", "estado"])

    #df = pd.read_csv(
        #"data/inputs/declaraciones_iva_2025.csv",
        #dtype={"nit": str, "codigo_municipio": str},
    #)
    #df = clasificar_por_valor(df, umbral_alto=10_000_000, umbral_medio=5_000_000)
    #print(df[["nit", "valor_declarado", "nivel_riesgo"]].head(10))
    #print(df["nivel_riesgo"].value_counts())

    #df = agregar_identificador_periodo(df)
    #columnas = [
        #"identificador_periodo", "nit", "razon_social",
        #"municipio", "periodo", "valor_declarado", "nivel_riesgo", "estado",
    #]

    #df_salida = preparar_columnas_salida(df, columnas)
    #print(df_salida.head())
    #print(df["nivel_riesgo"].value_counts())

    df = pd.read_csv(
        "data/inputs/declaraciones_iva_2025.csv",
        dtype={"nit": str, "codigo_municipio": str},
    )
    exportar_csv(df, "data/outputs", "declaraciones_prueba")


    #main()

