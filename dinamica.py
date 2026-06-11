def fecha_tratamiento_pacientes(pacientes):
    fechas = []
    for datos in pacientes.values():
        fechas.append(datos["treatment_start_date"])
    fechas.sort()
    dicc_cant_fecha = {}
    for fecha in fechas:
        dicc_cant_fecha[fecha] = dicc_cant_fecha.get(fecha, 0) + 1
    return dicc_cant_fecha

def mostrar_grafico(dicc_fechas):
    primeras_10 = {k: dicc_fechas[k] for k in list(dicc_fechas.keys())[:10]}
    fig, ax = plt.subplots()
    ax.plot(list(primeras_10.keys()), list(primeras_10.values()), marker="o")
    ax.set_title("Inicio de Tratamientos")
    ax.set_xlabel("Fechas")
    ax.set_ylabel("Cantidad")
    return fig

def main():
    pacientes = leer_archivo()
    conteo_fechas = fecha_tratamiento_pacientes(pacientes)
    fig = mostrar_grafico(conteo_fechas)
    st.pyplot(fig)v