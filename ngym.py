import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA (Centrada para mejor lectura y conversión)
st.set_page_config(
    page_title="NachoGYM Montilla - Transforma tu cuerpo",
    page_icon="🏋️‍♂️",
    layout="centered", # <-- Cambiado a 'centered' para que no abarque toda la pantalla
    initial_sidebar_state="collapsed"
)

# 2. ESTILOS CSS PERSONALIZADOS
st.markdown("""
    <style>
        /* Ocultar menú de Streamlit para efecto Landing Page */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Títulos principales */
        .brand-text { color: #ff9933; font-style: italic; font-weight: 900; text-transform: uppercase; }
        .hero-title { font-size: 3rem; line-height: 1.1; font-weight: 900; text-transform: uppercase; font-style: italic;}
        .section-title { font-size: 2.2rem; text-align: center; margin-top: 2rem; margin-bottom: 2rem; font-weight: 900; text-transform: uppercase; font-style: italic;}
        
        /* Botones personalizados para Anclajes (Scroll al formulario) */
        .btn-primary {
            display: inline-block;
            background-color: #ff9933;
            color: white !important;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            width: 100%;
            transition: background-color 0.3s, transform 0.2s;
            text-transform: uppercase;
            font-style: italic;
        }
        .btn-primary:hover {
            background-color: #e68a2e;
            transform: scale(1.02);
            color: white !important;
        }
        
        .btn-secondary {
            display: inline-block;
            background-color: white;
            color: #1e293b !important;
            border: 2px solid #e2e8f0;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            padding: 0.75rem 2rem;
            border-radius: 8px;
            width: 100%;
            transition: background-color 0.3s;
            text-transform: uppercase;
            font-style: italic;
        }
        .btn-secondary:hover {
            background-color: #f8fafc;
            border-color: #cbd5e1;
        }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA SUPERIOR (Logo)
st.markdown("### <span style='color: white; background-color: #ff9933; padding: 5px 10px; border-radius: 5px; font-style: italic;'>NACHO</span> <span class='brand-text' style='color: #1e293b;'>GYM</span>", unsafe_allow_html=True)
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
        # Enlace con ancla al formulario
        st.markdown("<a href='#reserva' class='btn-primary'>¡LO NECESITO!</a>", unsafe_allow_html=True)
    with btn_col2:
        st.markdown("<a href='#reserva' class='btn-secondary'>1 Día Gratis</a>", unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **¿Aún tienes dudas?** Ven a probar **1 día GRATIS** sin compromiso. Exclusivo para residentes de Montilla.")

with col2:
    st.image("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800", use_container_width=True, caption="Sede Montilla | Lunes a Viernes 07:00 - 22:00 hs")

st.divider()

# 5. PROGRAMAS EXCLUSIVOS (Botones dirigen al Formulario)
st.markdown("<div class='section-title'>Retos de <span style='color: #ff9933;'>Alto Impacto</span></div>", unsafe_allow_html=True)

prog1, prog2 = st.columns(2, gap="large")

with prog1:
    st.markdown("### <span class='brand-text'>REDUCE LA BARRIGA</span>", unsafe_allow_html=True)
    st.caption("⏱️ 6 Semanas Intensivas | Lunes a Viernes 15:00 hs")
    st.write("Elimina la grasa visceral y subcutánea del abdomen. No es cardio genérico; es trabajo focalizado en el core.")
    st.write("✔️ 3 Sesiones presenciales / semana")
    st.write("✔️ Guía nutricional 'Anti-Inflamación'")
    st.write("✔️ Medición de perímetros semanal")
    st.metric(label="Inversión única", value="99€", delta="Antes 150€", delta_color="normal")
    st.markdown("<br><a href='#reserva' class='btn-primary'>Quiero acceder al programa</a>", unsafe_allow_html=True)

with prog2:
    st.markdown("### <span class='brand-text'>ADIÓS GRASA TOTAL</span>", unsafe_allow_html=True)
    st.caption("⏱️ 3 Meses Intensivos | Lunes a Viernes 10:00 AM")
    st.write("Pérdida de peso general y acondicionamiento físico total. Para quienes buscan un cambio integral definitivo.")
    st.write("✔️ 5 Sesiones presenciales / semana")
    st.write("✔️ Guía nutricional 'Quema Grasa Total'")
    st.write("✔️ Seguimiento mensual progresivo")
    st.metric(label="Inversión única", value="109€", delta="Antes 199€", delta_color="normal")
    st.markdown("<br><a href='#reserva' class='btn-primary'>¡Lo necesito ahora!</a>", unsafe_allow_html=True)

st.divider()

# 6. PLANES DE MEMBRESÍA (Enlaces Externos Oficiales)
st.markdown("<div class='section-title'>Planes de <span style='color: #ff9933;'>Membresía</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Matrícula GRATIS en todos nuestros planes por tiempo limitado.</p>", unsafe_allow_html=True)

plan1, plan2, plan3 = st.columns(3, gap="medium")

with plan1:
    st.subheader("ANUAL ONECLUB")
    st.markdown("## 16,33€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Pago único anual 196€")
    st.write("✅ 1 Mes de regalo (tú + 1 amigo)")
    st.write("✅ Entrenamiento Personalizado")
    st.write("✅ InBody y Programa")
    st.success("Matrícula GRATIS")
    # Link externo
    st.link_button("Adquirir plan", "https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000457283253", use_container_width=True)

with plan2:
    st.warning("⭐ EL MÁS COMPLETO")
    st.subheader("ANUAL MULTICLUB")
    st.markdown("## 26,33€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Pago único anual 296€")
    st.write("✅ Acceso a TODA la red")
    st.write("✅ 1 Mes de regalo (tú + 1 amigo)")
    st.write("✅ Entrenamiento + InBody")
    st.success("Matrícula GRATIS")
    # Link externo
    st.link_button("¡Lo necesito!", "https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000457283171", type="primary", use_container_width=True)

with plan3:
    st.subheader("MENSUAL PAC")
    st.markdown("## 15,66€ <span style='font-size:1rem; color:gray;'>/mes</span>", unsafe_allow_html=True)
    st.caption("Renovación automática")
    st.write("✅ Sin permanencia")
    st.write("✅ 1 Sesión Personal Trainer")
    st.write("✅ Congelamiento 30 días/año")
    st.success("Matrícula GRATIS")
    # Link externo
    st.link_button("Apuntarme ahora", "https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000748390030", use_container_width=True)

st.divider()

# 7. CLASES EXCLUSIVAS (Enlaces Externos de LeadConnector)
st.markdown("<div class='section-title'>Clases Grupales <span style='color: #ff9933;'>Incluidas</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Solo para clientes activos. Reserva obligatoria previa a la clase.</p>", unsafe_allow_html=True)

clase1, clase2 = st.columns(2, gap="large")

with clase1:
    st.image("https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&q=80&w=800", use_container_width=True)
    st.markdown("### 🚴 <span class='brand-text'>CYCLING</span>", unsafe_allow_html=True)
    st.write("**Horarios:** Mañana (08:00 | 09:00) - Tarde (18:00 hs)")
    st.write("Clase de ciclismo indoor con intervalos de intensidad variable. Mejora fuerza, potencia y resistencia cardiovascular.")
    st.link_button("Reservar mi bici", "https://api.leadconnectorhq.com/widget/bookings/clases-cycling", use_container_width=True)

with clase2:
    st.image("https://images.unsplash.com/photo-1544033527-b192daee1f5b?auto=format&fit=crop&q=80&w=800", use_container_width=True)
    st.markdown("### 🏃 <span class='brand-text'>TRX CORE</span>", unsafe_allow_html=True)
    st.write("**Horarios:** Mañana (08:00 | 09:00) - Tarde (18:00 hs)")
    st.write("Entrenamiento en suspensión utilizando el peso del propio cuerpo. Enfocado totalmente en fortalecer el Core.")
    st.link_button("Reservar cupo", "https://api.leadconnectorhq.com/widget/bookings/clases-trx", use_container_width=True)

st.divider()

# 8. PREGUNTAS FRECUENTES
st.markdown("<div class='section-title'>Preguntas <span style='color: #ff9933;'>Frecuentes</span></div>", unsafe_allow_html=True)

faqs = [
    ("¿Cuáles son las formas de pago?", "Presencial: Aceptamos tarjetas de crédito/débito directamente en la recepción.\n\nOnline: Aceptamos pagos a través de nuestros enlaces oficiales.\n\nNota: Para ofertas trimestrales, se debe abonar el total al iniciar para congelar el precio promocional."),
    ("¿Hay que pagar matrícula de inscripción?", "¡Oferta Actual!: Estamos de oferta y actualmente TODA la matrícula es 100% GRATIS."),
    ("¿Tienen permanencia o contrato obligatorio?", "Planes Mensuales: No tienen permanencia. Puedes darte de baja avisando antes del día 25 del mes.\n\nPlanes Trimestrales: No son reembolsables, ya que el descuento especial se otorga por el compromiso de tiempo."),
    ("¿Tienen duchas y taquillas?", "Duchas: Sí, contamos con vestuarios completos con agua caliente.\n\nTaquillas (Lockers): Sí. Es obligatorio traer tu propio candado por seguridad."),
    ("¿Puedo ir solo a probar antes de pagar?", "Sí, ofrecemos un 'Pase de Día' o primera clase de valoración gratuita (exclusivo residentes Montilla). Es necesario agendar cita previa."),
    ("¿Cuáles son los horarios del gimnasio?", "Lunes a Viernes: 07:00 a 22:00 hs.\n\nSábados y Domingos: Cerrado."),
    ("¿Ofrecen clases dirigidas?", "Sí, contamos con Cycling y TRX. También programas exclusivos bajo consulta."),
    ("¿Puedo cambiar de plan después de iniciar?", "Mensual: Sí, avisando con 5 días de anticipación.\n\nTrimestral: No, se mantienen con el mismo beneficio durante los 3 meses."),
    ("¿Los niños pueden acceder al gimnasio?", "Por seguridad, solo mayores de 16 años pueden usar las instalaciones libres."),
    ("¿Ofrecen entrenamiento personal?", "Sí, ofrecemos sesiones individuales o en parejas. El costo es adicional a la membresía."),
    ("¿Puedo suspender mi membresía temporalmente?", "Sí, en planes mensuales puedes suspender hasta 1 mes máximo (una vez cada 6 meses) avisando previamente."),
    ("¿Tienen estacionamiento?", "Sí, contamos con estacionamiento gratuito para socios por orden de llegada."),
    ("¿Ofrecen servicios de nutrición?", "Sí, contamos con asesorías nutricionales personalizadas y planes alimenticios."),
    ("¿El gimnasio proporciona toallas o equipo?", "Toallas: No proporcionamos, es obligatorio traer la tuya por higiene.\n\nEquipo: Todo el equipo está disponible para los socios."),
    ("¿Hay WiFi en el gimnasio?", "Sí, contamos con red WiFi gratuita para nuestros socios."),
    ("¿Cómo puedo cancelar mi membresía?", "Opción A: Desde nuestra App.\n\nOpción B: En Recepción avisando al menos 5 días antes del cierre del ciclo.\n\nNota: Membresías trimestrales no son reembolsables.")
]

for q, a in faqs:
    with st.expander(f"**{q}**"):
        st.write(a)

st.divider()

# 9. SECCIÓN DE CONTACTO Y CONVERSIÓN
# El div con id='reserva' permite que los botones html viajen hasta aquí
st.markdown("<div id='reserva'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Agenda tu <span style='color: #ff9933;'>Prueba Gratis</span></div>", unsafe_allow_html=True)

cont1, cont2 = st.columns(2, gap="large")

with cont1:
    st.write("Exclusivo para residentes de Montilla o interesados en los **Retos de Alto Impacto**.")
    st.write("✔️ **Sin compromisos**")
    st.write("✔️ **Monitor asignado para guiarte**")
    st.write("✔️ **Estacionamiento Gratis**")
    st.write("Déjanos tus datos y confirmaremos la disponibilidad de tu cita en breve.")

with cont2:
    with st.form("contacto_form"):
        st.subheader("Completa tus datos")
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono (Móvil)") # Campo añadido por requisito
        email = st.text_input("Correo Electrónico")
        
        submit = st.form_submit_button("AGENDAR MI CITA", type="primary", use_container_width=True)
        
        if submit:
            if nombre and telefono and email:
                st.success(f"¡Reserva solicitada, {nombre}! Nos comunicaremos al {telefono} pronto para confirmar.")
            else:
                st.warning("Por favor, completa los tres campos obligatorios.")

st.divider()

# 10. FOOTER
footer1, footer2, footer3 = st.columns(3)
with footer1:
    st.markdown("### <span style='color: white; background-color: #ff9933; padding: 5px; border-radius: 5px; font-style: italic;'>NACHO</span> <span class='brand-text' style='color: #1e293b;'>GYM</span>", unsafe_allow_html=True)
    st.caption("El gimnasio líder en Montilla. Especialistas en transformación física y entrenamiento de alta intensidad.")
with footer2:
    st.write("**Ubicación y Contacto**")
    st.write("📍 Montilla, Córdoba")
    st.write("📞 +34 612 345 678")
with footer3:
    st.write("**Horarios de Atención**")
    st.write("Lunes a Viernes: 07:00 - 22:00 hs")
    st.write("Sábados y Domingos: Cerrado")

st.markdown("<p style='text-align: center; color: gray; margin-top: 2rem;'>© 2026 NachoGYM Montilla. Todos los derechos reservados.</p>", unsafe_allow_html=True)