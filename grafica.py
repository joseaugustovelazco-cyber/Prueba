import streamlit as st
import matplotlib.pyplot as plt



def obtener_edades_y_promedios(edad, promedios):
    """
    Devuelve dos listas:
    - edades: la edad seleccionada ±2 (si existen en el diccionario)
    - dias: los promedios correspondientes a esas edades
    """
    edades = []
    dias = []
    for e in range(edad - 2, edad + 3):   # recorre desde edad-2 hasta edad+2
        if e in promedios:                # chequea que la edad exista en el diccionario
            edades.append(e)              # agrega la edad válida
            dias.append(promedios[e])     # agrega el promedio correspondiente
    return edades, dias

def mostrar_grafico_recuperacion(edad,promedios):
    edades,dias = obtener_edades_y_promedios(edad,promedios)

    # Crear gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(edades, dias, color="#32CD32")

    # Resaltar la barra seleccionada en otro color
    ax.bar(edad, promedios[edad], color="#DC143C")

    # Título y etiquetas
    ax.set_facecolor("#708090")   # fondo del área del gráfico
    fig.patch.set_facecolor("#191970")   # cambia el fondo de la figura completa

    ax.set_title(f"Promedio de días de recuperación: edad {edad}",color="white")
    ax.set_xlabel("Edad",color="white")
    ax.set_ylabel("Promedio de días",color="white")

    # Límites de referencia
    ax.set_ylim(14, 30)
    return fig

# Mostrar en Streamlit
st.pyplot(fig)