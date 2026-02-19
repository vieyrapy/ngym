import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser la primera línea)
st.set_page_config(
    page_title="IA GYM Montilla - Transforma tu cuerpo",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ESTILOS CSS PERSONALIZADOS (Ligeros y seguros para Streamlit)
st.markdown("""
    <style>
        /* Ocultar menú de Streamlit para efecto Landing Page */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Títulos principales con el color de marca */
        .brand-text { color: #ff9933; font-style: italic; font-weight: 900; text-transform: uppercase; }
        .hero-title { font-size: 3.5rem; line-height: 1.1; font-weight: 900; text-transform: uppercase; font-style: italic;}
        .section-title { font-size: 2.5rem; text-align: center; margin-bottom: 2rem; font-weight: 900; text-transform: uppercase; font-style: italic;}
        
        /* Ajuste de botones primarios */
        div.stButton > button[kind="primary"] {
            background-color: #ff9933;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 2rem;
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #e68a2e;
        }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA SUPERIOR (Logo)
st.markdown("### <span style='color: white; background-color: #ff9933; padding: 5px 10px; border-radius: 5px; font-style: italic;'>IA</span> <span class='brand-text' style='color: #1e293b;'>GYM</span> Montilla", unsafe_allow_html=True)
st.divider()

# 4. HERO SECTION
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<p style='color: #ff9933; font-weight: bold;'>🔥 Matrícula 100% Gratis - Solo esta semana</p>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>Transforma tu cuerpo en <span style='color: #ff9933;'>Montilla.</span></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Entrenamiento personalizado, tecnología InBody y los mejores programas de pérdida de grasa en Córdoba.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.button("¡LO NECESITO AHORA!", type="primary", use_container_width=True)
    with btn_col2:
        st.button("Soy Socio", use_container_width=True)
        
    st.info("💡 **¿Aún tienes dudas?** Ven a probar **1 día GRATIS** sin compromiso.")

with col2:
    st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800", use_container_width=True, caption="Sede Montilla | Abierto 07:00 - 22:00")

st.divider()

# 5. PROGRAMAS ESPECIALES
st.markdown("<div class='section-title'>Retos de <span style='color: #ff9933;'>Alto Impacto</span></div>", unsafe_allow_html=True)

prog1, prog2 = st.columns(2, gap="large")

with prog1:
    st.markdown("### <span class='brand-text'>REDUCE LA BARRIGA</span>", unsafe_allow_html=True)
    st.caption("⏱️ 6 Semanas Intensivas")
    st.write("Elimina la grasa visceral y subcutánea del abdomen. No es cardio genérico, es trabajo focalizado en el Core.")
    st.write("✔️ 3 Sesiones presenciales / semana")
    st.write("✔️ Guía nutricional 'Anti-Inflamación'")
    st.write("✔️ Medición de perímetros semanal")
    st.metric(label="Inversión única", value="99€", delta="Antes 150€", delta_color="normal")
    st.button("Quiero acceder al programa", key="btn_prog1")

with prog2:
    st.markdown("### <span class='brand-text'>ADIÓS GRASA TOTAL</span>", unsafe_allow_html=True)
    st.caption("⏱️ 3 Meses Total")
    st.write("Pérdida de peso general y acondicionamiento físico total. Para quienes buscan un cambio integral definitivo.")
    st.write("✔️ 5 Sesiones presenciales / semana")
    st.write("✔️ Guía nutricional 'Quema Grasa Total'")
    st.write("✔️ Seguimiento mensual progresivo")
    st.metric(label="Inversión única", value="109€", delta="Antes 199€", delta_color="normal")
    st.button("¡Lo necesito ahora!", type="primary", key="btn_prog2")

st.divider()

# 6. PLANES DE MEMBRESÍA
st.markdown("<div class='section-title'>Elige tu <span style='color: #ff9933;'>Plan</span></div>", unsafe_allow_html=True)

plan1, plan2, plan3 = st.columns(3, gap="medium")

with plan1:
    st.subheader("ANUAL ONECLUB")
    st.markdown("## 16,33€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Pago único anual 196€")
    st.write("✅ 1 Mes de regalo para ti + 1 Amigo")
    st.write("✅ Entrenamiento Personalizado")
    st.write("✅ Evaluación Inbody Incluida")
    st.success("Matrícula 100% GRATIS")
    st.button("Adquirir plan", key="plan1", use_container_width=True)

with plan2:
    st.warning("⭐ EL MÁS RECOMENDADO")
    st.subheader("ANUAL MULTICLUB")
    st.markdown("## 26,33€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Pago único anual 296€")
    st.write("✅ Acceso a TODA la red de clubes")
    st.write("✅ 1 Mes de regalo para ti + 1 Amigo")
    st.write("✅ Entrenamiento Personalizado")
    st.write("✅ Evaluación física + InBody")
    st.success("Matrícula GRATIS")
    st.button("¡Lo necesito!", type="primary", key="plan2", use_container_width=True)

with plan3:
    st.subheader("MENSUAL PAC")
    st.markdown("## 15,66€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Renovación automática")
    st.write("✅ Sin permanencia obligatoria")
    st.write("✅ 1 Sesión Personal Trainer Gratis")
    st.write("✅ Congelamiento 30 días / año")
    st.success("Matrícula GRATIS")
    st.button("Apuntarme ahora", key="plan3", use_container_width=True)

st.divider()

# 7. CLASES EXCLUSIVAS
st.markdown("<div class='section-title'>Clases Grupales <span style='color: #ff9933;'>Exclusivas</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Solo para clientes activos. Reserva mediante app.</p>", unsafe_allow_html=True)

clase1, clase2 = st.columns(2, gap="large")

with clase1:
    st.image("https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&q=80&w=800", use_container_width=True)
    st.markdown("### 🚴 <span class='brand-text'>CYCLING</span>", unsafe_allow_html=True)
    st.write("**Horarios:** Mañana (08:00 | 09:00) - Tarde (18:00)")
    st.write("Ciclismo indoor con intervalos de intensidad variable. Mejora fuerza, potencia y resistencia cardiovascular.")

with clase2:
    st.image("https://images.unsplash.com/photo-1544033527-b192daee1f5b?auto=format&fit=crop&q=80&w=800", use_container_width=True)
    st.markdown("### 🏃 <span class='brand-text'>TRX CORE</span>", unsafe_allow_html=True)
    st.write("**Horarios:** Mañana (08:00 | 09:00) - Tarde (18:00)")
    st.write("Entrenamiento en suspensión. Enfocado totalmente en fortalecer el Core, integrando espalda, hombros y piernas.")

st.divider()

# 8. PREGUNTAS FRECUENTES (Utilizando st.expander nativo)
st.markdown("<div class='section-title'>Preguntas <span style='color: #ff9933;'>Frecuentes</span></div>", unsafe_allow_html=True)

faqs = [
    ("¿Cuáles son las formas de pago?", "Presencial: Aceptamos tarjetas de crédito/débito directamente en la recepción del gimnasio en Montilla.\n\nOnline: Aceptamos pagos a través de nuestros enlaces oficiales y plataforma web.\n\nNota: Para las ofertas trimestrales, se debe abonar el total al iniciar para congelar el precio promocional."),
    ("¿Hay que pagar matrícula de inscripción?", "¡Oferta Actual!: Estamos de oferta y actualmente TODA la matrícula es 100% GRATIS."),
    ("¿Tienen permanencia o contrato obligatorio?", "Planes Mensuales: No tienen permanencia. Puedes darte de baja avisando antes del día 25 del mes.\n\nPlanes Trimestrales: No son reembolsables, ya que el descuento especial se otorga por el compromiso de tiempo adquirido."),
    ("¿Tienen duchas y taquillas?", "Duchas: Sí, contamos con vestuarios completos y duchas con agua caliente.\n\nTaquillas (Lockers): Sí. Es obligatorio traer tu propio candado por seguridad para utilizarlas."),
    ("¿Puedo ir solo a probar antes de pagar?", "Sí, ofrecemos un 'Pase de Día' o una primera clase de valoración gratuita (exclusivo para residentes de Montilla). Es necesario agendar cita previa para que un monitor pueda atenderte."),
    ("¿Cuáles son los horarios del gimnasio?", "Lunes a Viernes: 06:30 AM a 10:00 PM.\n\nSábados y Domingos: Cerrado."),
    ("¿Ofrecen clases dirigidas?", "Sí, contamos con Cycling y TRX. También contamos con programas exclusivos por tiempo limitado bajo consulta de disponibilidad."),
    ("¿Puedo cambiar de plan después de iniciar?", "Mensual: Sí, puedes cambiar de plan avisando con al menos 5 días de anticipación.\n\nTrimestral: No, los planes trimestrales se mantienen con el mismo beneficio durante los 3 meses, sin cambios."),
    ("¿Los niños pueden acceder al gimnasio?", "Por seguridad, solo mayores de 16 años pueden usar las instalaciones libres."),
    ("¿Ofrecen entrenamiento personal?", "Sí, nuestros entrenadores ofrecen sesiones individuales o en parejas. El costo es adicional a la membresía y se agenda directamente con el personal."),
    ("¿Hay descuentos por familia o grupos?", "Actualmente no contamos con descuentos por grupo estandarizados, pero puedes consultar en recepción para presentar tu caso específico."),
    ("¿Puedo suspender mi membresía temporalmente?", "Sí, en planes mensuales puedes suspender hasta 1 mes máximo. Requiere aviso previo en recepción o plataforma y se aplica solo una vez cada 6 meses."),
    ("¿Tienen estacionamiento?", "Sí, contamos con estacionamiento gratuito para socios por orden de llegada."),
    ("¿Ofrecen servicios de nutrición?", "Sí, contamos con asesorías nutricionales personalizadas y planes alimenticios para complementar tu entrenamiento."),
    ("¿Puedo usar el gimnasio si me estoy recuperando de una lesión?", "Dependerá del tipo de lesión y autorización médica. Recomendamos traer certificado médico. El entrenamiento adaptado estará bajo tu propia responsabilidad."),
    ("¿El gimnasio proporciona toallas o equipo personal?", "Toallas: No proporcionamos toallas (traer la propia es obligatorio por higiene).\n\nEquipo: Todo el equipo de entrenamiento (pesas, bandas, colchonetas, etc.) está disponible para los socios."),
    ("¿Hay WiFi en el gimnasio?", "Sí, contamos con red WiFi gratuita para nuestros socios."),
    ("¿Ofrecen bonos o promociones por referidos?", "Sí, si traes un amigo que se inscriba, ¡ambos reciben un Regalo Sorpresa exclusivo!"),
    ("¿Cómo puedo cancelar mi membresía?", "Opción A: Desde nuestra App cuando quieras.\n\nOpción B: En Recepción avisando al menos 5 días antes del cierre del ciclo de pago.\n\nNota: Membresías trimestrales no son reembolsables.")
]

# Usar el componente nativo expansible de Streamlit evita cualquier bug de código HTML
for q, a in faqs:
    with st.expander(f"**{q}**"):
        st.write(a)

st.divider()

# 9. SECCIÓN DE CONTACTO
cont1, cont2 = st.columns(2, gap="large")

with cont1:
    st.markdown("<div class='hero-title'>Entrena Gratis <span style='color: #ff9933;'>Hoy</span></div>", unsafe_allow_html=True)
    st.write("Exclusivo para residentes de Montilla. Clase de valoración gratuita.")
    st.write("✔️ **Sin compromisos**")
    st.write("✔️ **Monitor asignado**")
    st.write("✔️ **Estacionamiento Gratis**")

with cont2:
    with st.form("contacto_form"):
        st.subheader("Reserva tu prueba")
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Email")
        submit = st.form_submit_button("AGENDAR MI PRUEBA", type="primary", use_container_width=True)
        
        if submit:
            if nombre and email:
                st.success(f"¡Reserva completada con éxito, {nombre}! Nos pondremos en contacto contigo pronto.")
            else:
                st.warning("Por favor, completa todos los campos requeridos.")

st.divider()

# 10. FOOTER
footer1, footer2, footer3 = st.columns(3)
with footer1:
    st.markdown("### <span style='color: white; background-color: #ff9933; padding: 5px; border-radius: 5px; font-style: italic;'>IA</span> <span class='brand-text' style='color: #1e293b;'>GYM</span>", unsafe_allow_html=True)
    st.caption("El gimnasio líder en Montilla. Especialistas en transformación física, nutrición y entrenamiento.")
with footer2:
    st.write("**Ubicación**")
    st.write("📍 Montilla, Córdoba")
    st.write("📞 +34 612 345 678")
with footer3:
    st.write("**Horarios**")
    st.write("Lunes a Viernes: 06:30 - 22:00 hs")
    st.write("Sábados y Domingos: Cerrado")

st.markdown("<p style='text-align: center; color: gray; margin-top: 2rem;'>© 2027 IA GYM Montilla. Todos los derechos reservados.</p>", unsafe_allow_html=True)