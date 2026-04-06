import streamlit as st

# --- DICCIONARIO AVANZADO (Extraído del PDF del CUR 2024) ---
# Esto es lo que le da valor comercial a tu consulta
REGLAS = {
    "USAA": {
        "altura_max": 31.20, 
        "morfologia": "PB + 9 pisos + 2 retiros",
        "LFI_LIB": "Afecta (Banda edificable varía según manzana)",
        "plusvalia": "Aplica (Ley 6062)",
        "nota": "Unidad de Sustentabilidad de Altura Alta. Máximo aprovechamiento."
    },
    "USAM": {
        "altura_max": 22.80, 
        "morfologia": "PB + 6 pisos + 2 retiros",
        "LFI_LIB": "Afecta (Banda edificable)",
        "plusvalia": "Aplica",
        "nota": "Unidad de Sustentabilidad de Altura Media."
    },
    "USAB2": {
        "altura_max": 11.20, 
        "morfologia": "PB + 2 pisos + 1 retiro",
        "LFI_LIB": "No aplica (se rige por FOS)",
        "plusvalia": "Exento",
        "nota": "Unidad de Sustentabilidad de Altura Baja 2."
    },
    "USAB1": {
        "altura_max": 9.00, 
        "morfologia": "PB + 2 pisos",
        "LFI_LIB": "No aplica",
        "plusvalia": "Exento",
        "nota": "Unidad de Sustentabilidad de Altura Baja 1."
    }
}

# --- CONFIGURACIÓN DE LA INTERFAZ ---
st.set_page_config(page_title="Asistente Normativo CABA", layout="centered")
st.title("🏗️ Asistente Normativo CABA (PRO)")
st.caption("Basado en el Código Urbanístico 2024")

# Entradas del usuario
zona = st.selectbox("Seleccioná la Unidad de Edificabilidad:", list(REGLAS.keys()))
altura = st.number_input("Altura proyectada de tu edificio (metros):", min_value=0.0, step=0.1)

if st.button("Verificar Factibilidad"):
    datos = REGLAS[zona]
    
    # Lógica de validación
    if altura > datos["altura_max"]:
        st.error(f"❌ ERROR: La altura de {altura}m supera los {datos['altura_max']}m permitidos.")
    else:
        st.success(f"✅ CUMPLE: La altura está dentro del límite de {datos['altura_max']}m.")
    
    # Informe detallado (Lo que hace que la app sea 'cobrable')
    st.markdown("---")
    st.subheader(f"Informe Técnico de Parcela: {zona}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🏢 **Morfología:** {datos['morfologia']}")
        st.write(f"💰 **Plusvalía Urbana:** {datos['plusvalia']}")
    with col2:
        st.write(f"📏 **LFI / LIB:** {datos['LFI_LIB']}")
        st.info(datos['nota'])

st.sidebar.write("Desarrollado para profesionales FADU/UBA")
