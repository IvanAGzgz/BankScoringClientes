from codigo_de_ejecucion import *
import streamlit as st

#CONFIGURACION DE LA PÁGINA
st.set_page_config(
     page_title = 'Prediccion clientes',
     page_icon = 'images.png',
     layout = 'wide')

#SIDEBAR
with st.sidebar:
    image_path = 'finanzas-integradas.jpg'

     try:
         st.image(image_path)
     except FileNotFoundError:
         st.error(f"No se encontró el archivo {image_path}")
     except Exception as e:
         st.error(f"Error al cargar la imagen: {e}")


    canal_contacto = st.selectbox('canal_contacto', ['cellular','telephone'])
    dia_semana = st.selectbox('dia_semana', ['mon','tue','wed','thu','fri'])
    edad = st.number_input('edad', 17, 81)
    estado = st.selectbox('estado', ['married','single','divorced','unknown'])
    mes = st.selectbox('mes', ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
       'nov','dec'])
    prestamo_hipotecario = st.selectbox('prestamo_hipotecario', ['yes','no'])
    trabajo = st.selectbox('trabajo', ['technician', 'blue-collar', 'services', 'unemployed',
       'management', 'entrepreneur', 'admin.', 'retired', 'self-employed',
       'housemaid', 'student', 'unknown'])
    variacion_tasa_empleo = st.slider('variacion_tasa_empleo', -3.4, 1.4)


#MAIN
st.title('¿CONTRATARÁ FONDOS EL CLIENTE?')


#CALCULAR

#Crear el registro
registro = pd.DataFrame({'canal_contacto':canal_contacto,
                         'dia_semana':dia_semana,
                         'edad':edad,
                         'estado':estado,
                         'mes':mes,
                         'prestamo_hipotecario':prestamo_hipotecario,
                         'trabajo':trabajo,
                         'variacion_tasa_empleo':variacion_tasa_empleo}
                        ,index=[0])



#CALCULAR RIESGO
if st.sidebar.button('¿CONTRATA FONDOS?'):
    #Ejecutar el scoring
    scoring = ejecutar_modelos(registro)

    scoring_porcentaje = scoring.round(2) * 100

    scoring_porcentaje_final = f"{scoring_porcentaje[0]}%"

    st.metric(label = 'Probabilidad de que el cliente adquiera fondos:', value = scoring_porcentaje_final)

    #MAL CLIENTE
    if scoring_porcentaje <= 15:
        col1, col2 = st.columns(2)
        with col1:
            st.image('x.png')
        with col2:
            st.subheader("Mal Cliente")
            st.write("""
            1. **Restricción de Créditos**: Limitar el acceso a nuevos productos crediticios hasta que el cliente demuestre mejoras significativas en su comportamiento financiero.
            2. **Recuperación y Cobranza**: Implementar estrategias de recuperación de deuda y cobro de morosidades de manera proactiva, como planes de pago estructurados para facilitar el cumplimiento de las obligaciones financieras del cliente.
            """)

# Cliente Dudoso
    if 15 < scoring_porcentaje < 25:
        col1, col2 = st.columns(2)
        with col1:
            st.image('interrogante.png')
        with col2:
            st.subheader("Cliente Dudoso")
            st.write("""
            1. **Condiciones Controladas**: Ofrecer productos financieros con condiciones más restrictivas, como préstamos con montos más bajos y mayores garantías.
            2. **Monitoreo y Asesoría**: Proporcionar servicios de asesoría financiera y programas de educación para ayudar al cliente a mejorar su historial crediticio y su gestión de finanzas personales.
            """)

    # Buen Cliente
    if scoring_porcentaje >= 25:
        col1, col2 = st.columns(2)
        with col1:
            st.image('tick_verde.png')
        with col2:
            st.subheader("Buen Cliente")
            st.write("""
            1. **Ofertas Personalizadas**: Ofrecer productos financieros adicionales con tasas de interés preferenciales y condiciones favorables, como tarjetas de crédito con mayores límites o préstamos personales a tasas reducidas.
            2. **Programa de Fidelización**: Incorporar al cliente en programas de fidelización con beneficios exclusivos, como asesoría financiera gratuita o recompensas por uso frecuente de productos financieros.
            """)

else:
    st.write('DEFINE LOS PARÁMETROS DEL CLIENTE Y HAZ CLICK EN CALCULAR RIESGO')
