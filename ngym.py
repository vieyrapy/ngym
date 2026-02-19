import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="NA GYM Montilla - Transforma tu cuerpo",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. INYECCIÓN DEL CONTADOR FLOTANTE (JS Nativo)
# Esto crea una barra fija en la parte superior sin recargar Streamlit
components.html("""
<script>
    // Evitar duplicados si Streamlit recarga la interfaz
    if(!window.parent.document.getElementById('promo-banner-container')) {
        const banner = window.parent.document.createElement('div');
        banner.id = 'promo-banner-container';
        // Estilos de la barra flotante de urgencia
        banner.style.cssText = 'position:fixed; top:0; left:0; width:100%; background:linear-gradient(90deg,#ff7300,#dc2626); color:white; text-align:center; padding:12px 10px; font-weight:900; z-index:999999; font-family:"Montserrat",sans-serif; font-size:1rem; letter-spacing:1px; box-shadow:0 4px 20px rgba(0,0,0,0.6); text-transform:uppercase;';
        banner.innerHTML = '⏳ LA OFERTA DE MATRÍCULA GRATIS TERMINA EN: <span id="gym-countdown" style="background:rgba(0,0,0,0.2); padding:3px 10px; border-radius:6px; font-variant-numeric:tabular-nums; margin-left:8px; font-size:1.2rem;">15:00</span>';
        
        window.parent.document.body.prepend(banner);
        
        // Lógica del contador (Evergreen 15 minutos con memoria)
        let endTime = localStorage.getItem('gymPromoEnd');
        if(!endTime || parseInt(endTime) < Date.now()){
            endTime = Date.now() + 15 * 60000; // 15 minutos en milisegundos
            localStorage.setItem('gymPromoEnd', endTime);
        }
        
        setInterval(()=>{
            let el = window.parent.document.getElementById('gym-countdown');
            if(!el) return;
            let diff = parseInt(endTime) - Date.now();
            if(diff <= 0){ 
                el.innerText = "00:00"; 
                return; 
            }
            let m = Math.floor(diff / 60000);
            let s = Math.floor((diff % 60000) / 1000);
            el.innerText = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
        }, 1000);
    }
</script>
""", height=0, width=0)

# 3. ESTILOS CSS PREMIUM DARK MODE
# Sin líneas en blanco y con margen superior extra para la barra flotante
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,600;0,800;0,900;1,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
html, body, .stApp { font-family: 'Montserrat', sans-serif !important; background-color: #0b0f19 !important; color: #f8fafc !important; scroll-behavior: smooth; }
.stApp > header { display: none !important; }
.block-container { padding-top: 4rem !important; } /* Margen para no tapar el logo con el contador */
.gradient-text { background: linear-gradient(135deg, #ff7300 0%, #ffba00 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-style: italic; }
.hero-title { font-size: 3.5rem; line-height: 1.05; font-weight: 900; text-transform: uppercase; letter-spacing: -0.05em; text-align: center; margin-bottom: 1.5rem; color: #ffffff !important; }
.section-title { font-size: 2.5rem; text-align: center; margin: 4rem 0 2rem 0; font-weight: 900; text-transform: uppercase; font-style: italic; letter-spacing: -0.03em; color: #ffffff !important; }
.btn-premium { display: block; background: linear-gradient(135deg, #ff7300 0%, #ff9500 100%); color: white !important; font-weight: 800; text-align: center; text-decoration: none; padding: 1rem 2rem; border-radius: 12px; width: 100%; transition: all 0.3s ease; text-transform: uppercase; font-style: italic; font-size: 1.1rem; box-shadow: 0 10px 25px rgba(255, 115, 0, 0.3); border: none; }
.btn-premium:hover { transform: translateY(-3px); box-shadow: 0 15px 35px rgba(255, 115, 0, 0.5); filter: brightness(1.1); }
.btn-outline { display: block; background: rgba(255,255,255,0.05); color: #ffffff !important; border: 2px solid #334155; font-weight: 800; text-align: center; text-decoration: none; padding: 1rem 2rem; border-radius: 12px; width: 100%; transition: all 0.3s ease; text-transform: uppercase; font-style: italic; font-size: 1.1rem; }
.btn-outline:hover { border-color: #ff7300; background: rgba(255, 115, 0, 0.1); }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }
@media (max-width: 768px) { .grid-2, .grid-3 { grid-template-columns: 1fr; } .hero-title { font-size: 2.5rem; } }
.card { background: #111827; border-radius: 20px; padding: 2.5rem 2rem; box-shadow: 0 10px 40px rgba(0,0,0,0.5); border: 1px solid #1f2937; transition: all 0.3s ease; display: flex; flex-direction: column; justify-content: space-between; }
.card:hover { transform: translateY(-8px); box-shadow: 0 20px 50px rgba(255,115,0,0.15); border-color: #ff7300; }
.card-highlight { border: 3px solid #ff7300; transform: scale(1.05); position: relative; background: #1f2937; }
.card-highlight:hover { transform: scale(1.05) translateY(-8px); }
.badge { display: inline-block; background: rgba(255, 115, 0, 0.15); color: #ffba00; padding: 0.4rem 1rem; border-radius: 50px; font-weight: 800; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; border: 1px solid rgba(255, 115, 0, 0.3); }
.price-tag { font-size: 3rem; font-weight: 900; color: #ffffff; line-height: 1; margin: 1rem 0; }
.price-tag span { font-size: 1rem; color: #94a3b8; font-weight: 600; }
.list-check li { margin-bottom: 0.8rem; font-size: 0.95rem; font-weight: 600; display: flex; align-items: center; color: #e2e8f0; }
.list-check i { color: #ff7300; margin-right: 10px; font-size: 1.2rem; }
div[data-testid="stForm"] { border: 1px solid #1f2937 !important; padding: 2rem !important; background: #111827 !important; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); }
.stTextInput label p { color: #f8fafc !important; font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

# 4. TOP BAR
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0;">
<div style="font-weight: 900; font-size: 1.5rem; letter-spacing: -1px; color: #ffffff;">
<span style='background: #ff7300; color: white; padding: 4px 12px; border-radius: 8px; font-style: italic; margin-right: 5px;'>NA</span> GYM
</div>
<div style="font-weight: 700; font-size: 0.9rem; color: #cbd5e1;">
📍 Montilla, Córdoba
</div>
</div>
""", unsafe_allow_html=True)
st.divider()

# 5. HERO SECTION
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
<div style="display: inline-block; background: rgba(255,115,0,0.1); color: #ffba00; padding: 0.5rem 1.5rem; border-radius: 50px; font-weight: 800; margin-bottom: 1.5rem; border: 1px solid rgba(255,115,0,0.3); font-size: 0.9rem;">
🔥 MATRÍCULA 100% GRATIS EN TODOS LOS PLANES
</div>
<h1 class="hero-title" style="font-size: 5rem;" >El mejor GYM de <span class="gradient-text">Montilla</span></h1>
<p style="font-size: 1.2rem; color: #cbd5e1; font-weight: 500; max-width: 600px; margin: 0 auto 2.5rem auto;">
Deja de buscar excusas. Fusionamos entrenamiento de alta intensidad con tecnología para que cada gota de sudor cuente.
</p>
</div>
""", unsafe_allow_html=True)

col_h1, col_h2 = st.columns(2)
with col_h1:
    st.markdown("<a href='#reserva' class='btn-premium'>¡EMPEZAR AHORA! ➔</a>", unsafe_allow_html=True)
with col_h2:
    st.markdown("<a href='#reserva' class='btn-outline'>PROBAR 1 DÍA GRATIS</a>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-top: 1.5rem; color: #94a3b8; font-weight: 600; font-size: 1rem;">
⭐⭐⭐⭐⭐ Únete a más de <span style="color: #ffffff; font-weight: 800;">500+ socios</span> activos.
</div>
""", unsafe_allow_html=True)

# 6. PROGRAMAS EXCLUSIVOS
st.markdown("<div class='section-title'>Retos de <span class='gradient-text'>Alto Impacto</span></div>", unsafe_allow_html=True)

st.markdown("""
<div class="grid-2">
<div class="card">
<div>
<span class="badge">⏱️ 6 SEMANAS</span>
<h3 style="font-size: 2rem; font-weight: 900; font-style: italic; margin-bottom: 0; color: #ffffff;">REDUCE LA BARRIGA</h3>
<div class="price-tag">99€ <span style="text-decoration: line-through;">Antes 150€</span></div>
<p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 1.5rem;">Elimina la grasa visceral y subcutánea del abdomen. Trabajo focalizado en el core.</p>
<ul class="list-check" style="list-style: none; padding: 0;">
<li><i class="fas fa-check-circle"></i> Lunes a Viernes 15:00 hs</li>
<li><i class="fas fa-check-circle"></i> 3 Sesiones presenciales/semana</li>
<li><i class="fas fa-check-circle"></i> Guía "Anti-Inflamación"</li>
<li><i class="fas fa-check-circle"></i> Medición de perímetros semanal</li>
</ul>
</div>
<a href="#reserva" class="btn-premium" style="margin-top: 2rem;">QUIERO ACCEDER ➔</a>
</div>
<div class="card">
<div>
<span class="badge">⏱️ 3 MESES TOTAL</span>
<h3 style="font-size: 2rem; font-weight: 900; font-style: italic; margin-bottom: 0; color: #ffffff;">ADIÓS GRASA TOTAL</h3>
<div class="price-tag">109€ <span style="text-decoration: line-through;">Antes 199€</span></div>
<p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 1.5rem;">Pérdida de peso general y acondicionamiento físico. Para un cambio integral definitivo.</p>
<ul class="list-check" style="list-style: none; padding: 0;">
<li><i class="fas fa-check-circle"></i> Lunes a Viernes 10:00 AM</li>
<li><i class="fas fa-check-circle"></i> 5 Sesiones presenciales/semana</li>
<li><i class="fas fa-check-circle"></i> Guía "Quema Grasa Total"</li>
<li><i class="fas fa-check-circle"></i> Seguimiento progresivo mensual</li>
</ul>
</div>
<a href="#reserva" class="btn-premium" style="margin-top: 2rem;">¡LO NECESITO AHORA! ➔</a>
</div>
</div>
""", unsafe_allow_html=True)

# 7. PLANES DE MEMBRESÍA
st.markdown("<div class='section-title'>Planes de <span class='gradient-text'>Membresía</span></div>", unsafe_allow_html=True)

st.markdown("""
<div class="grid-3">
<div class="card">
<div>
<h4 style="font-weight: 900; font-size: 1.2rem; color: #ffffff; margin-bottom: 0;">ANUAL ONECLUB</h4>
<div class="price-tag">16,33€<span>/mes</span></div>
<p style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Pago único anual 196€</p>
<ul class="list-check" style="list-style: none; padding: 0; margin-top: 1.5rem;">
<li><i class="fas fa-check"></i> 1 Mes de regalo (tú + amigo)</li>
<li><i class="fas fa-check"></i> Entrenamiento Personalizado</li>
<li><i class="fas fa-check"></i> InBody y Programa</li>
<li style="color: #ff7300;"><i class="fas fa-gift"></i> Matrícula 100% GRATIS</li>
</ul>
</div>
<a href="https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000457283253" target="_blank" class="btn-outline" style="margin-top: 1.5rem;">Adquirir plan</a>
</div>
<div class="card card-highlight">
<div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #ff7300; color: white; padding: 5px 15px; border-radius: 20px; font-weight: 800; font-size: 0.8rem; letter-spacing: 1px;">EL MÁS COMPLETO</div>
<div>
<h4 style="font-weight: 900; font-size: 1.2rem; color: #ffffff; margin-bottom: 0;">ANUAL MULTICLUB</h4>
<div class="price-tag">26,33€<span>/mes</span></div>
<p style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Pago único anual 296€</p>
<ul class="list-check" style="list-style: none; padding: 0; margin-top: 1.5rem;">
<li><i class="fas fa-star"></i> Acceso a TODA la red</li>
<li><i class="fas fa-check"></i> 1 Mes de regalo (tú + amigo)</li>
<li><i class="fas fa-check"></i> Entrenamiento + InBody</li>
<li style="color: #ff7300;"><i class="fas fa-gift"></i> Matrícula 100% GRATIS</li>
</ul>
</div>
<a href="https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000457283171" target="_blank" class="btn-premium" style="margin-top: 1.5rem;">¡LO NECESITO!</a>
</div>
<div class="card">
<div>
<h4 style="font-weight: 900; font-size: 1.2rem; color: #ffffff; margin-bottom: 0;">MENSUAL PAC</h4>
<div class="price-tag">15,66€<span>/mes</span></div>
<p style="font-size: 0.8rem; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Renovación automática</p>
<ul class="list-check" style="list-style: none; padding: 0; margin-top: 1.5rem;">
<li><i class="fas fa-check"></i> Sin permanencia</li>
<li><i class="fas fa-check"></i> 1 Sesión Personal Trainer</li>
<li><i class="fas fa-check"></i> Congelamiento 30 días/año</li>
<li style="color: #ff7300;"><i class="fas fa-gift"></i> Matrícula 100% GRATIS</li>
</ul>
</div>
<a href="https://www.energyclub.cl/checkout?clubId=f1a6ccd9-e66a-4963-a61b-89777e9367a0&planId=4312902000748390030" target="_blank" class="btn-outline" style="margin-top: 1.5rem;">Apuntarme ahora</a>
</div>
</div>
""", unsafe_allow_html=True)

# 8. CLASES EXCLUSIVAS
st.markdown("<div class='section-title'>Clases Grupales <span class='gradient-text'>Incluidas</span><p style='text-align: center;  color: #94a3b8; font-weight: 600; font-size: 1rem;'>Únete a las clases grupales exclusivos para socios activos.</p></div>", unsafe_allow_html=True)

st.markdown("""
<div class="grid-2">
<div class="card" style="padding: 0; overflow: hidden; border: 1px solid #1f2937;">
<div style="height: 200px; background-image: url('https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&q=80&w=800'); background-size: cover; background-position: center;"></div>
<div style="padding: 2rem;">
<h3 style="font-weight: 900; font-size: 1.8rem; font-style: italic; margin-bottom: 0.5rem; color: #ffffff;">🚴 CYCLING</h3>
<p style="font-size: 0.9rem; font-weight: 700; color: #ff7300; margin-bottom: 1rem;">🕒 08:00 AM | 09:00 AM | 18:00 PM</p>
<p style="color: #cbd5e1; font-weight: 500; font-size: 0.95rem; margin-bottom: 1.5rem;">Clase de ciclismo indoor con intervalos de intensidad variable. Mejora fuerza, potencia y resistencia cardiovascular.</p>
<a href="https://api.leadconnectorhq.com/widget/bookings/clases-cycling" target="_blank" class="btn-outline">Reservar Bici</a>
</div>
</div>
<div class="card" style="padding: 0; overflow: hidden; border: 1px solid #1f2937;">
<div style="height: 200px; background-image: url('https://images.unsplash.com/photo-1544033527-b192daee1f5b?auto=format&fit=crop&q=80&w=800'); background-size: cover; background-position: center;"></div>
<div style="padding: 2rem;">
<h3 style="font-weight: 900; font-size: 1.8rem; font-style: italic; margin-bottom: 0.5rem; color: #ffffff;">🏃 TRX CORE</h3>
<p style="font-size: 0.9rem; font-weight: 700; color: #ff7300; margin-bottom: 1rem;">🕒 08:00 AM | 09:00 AM | 18:00 PM</p>
<p style="color: #cbd5e1; font-weight: 500; font-size: 0.95rem; margin-bottom: 1.5rem;">Entrenamiento en suspensión utilizando el peso del propio cuerpo. Enfocado totalmente en fortalecer el Core.</p>
<a href="https://api.leadconnectorhq.com/widget/bookings/clases-trx" target="_blank" class="btn-outline">Reservar Cupo</a>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# 9. PREGUNTAS FRECUENTES
st.markdown("<div class='section-title'>Preguntas <span class='gradient-text'>Frecuentes</span></div>", unsafe_allow_html=True)

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

# 10. SECCIÓN DE CONTACTO Y CONVERSIÓN
st.markdown("<div id='reserva'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>Agenda tu <span class='gradient-text'>Prueba Gratis</span></div>", unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; font-size: 1.1rem; color: #cbd5e1; font-weight: 500; max-width: 600px; margin: 0 auto 2rem auto;">
Déjanos tus datos si deseas probar <b>1 día GRATIS</b> (residentes de Montilla) o si estás interesado en reservar tu plaza para los <b>Retos de Alto Impacto</b>.
</p>
""", unsafe_allow_html=True)

with st.form("contacto_form"):
    st.markdown("<h3 style='text-align:center; font-weight:900; color:#ffffff; margin-bottom: 1.5rem; font-style: italic; text-transform: uppercase;'>Completa tus datos</h3>", unsafe_allow_html=True)
    nombre = st.text_input("👤 Nombre completo")
    telefono = st.text_input("📱 Teléfono (Móvil)")
    email = st.text_input("✉️ Correo Electrónico")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.form_submit_button("SOLICITAR MI PLAZA ➔", type="primary", use_container_width=True)
    
    if submit:
        if nombre and telefono and email:
            st.success(f"¡Solicitud enviada, {nombre}! Nos comunicaremos al {telefono} lo antes posible para confirmar.")
        else:
            st.warning("⚠️ Por favor, completa los tres campos obligatorios para poder contactarte.")

st.divider()

# 11. FOOTER
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
<h2 style="font-weight: 900; font-size: 1.5rem; letter-spacing: -1px; color: #ffffff; margin-bottom: 1rem;">
<span style='background: #ff7300; color: white; padding: 4px 12px; border-radius: 8px; font-style: italic; margin-right: 5px;'>NA</span> GYM
</h2>
<p style="color: #cbd5e1; font-weight: 600; font-size: 0.95rem;">
📍 Montilla, Córdoba | 📞 +34 612 345 678<br>
Lunes a Viernes: 07:00 - 22:00 hs
</p>
<p style="color: #64748b; font-weight: 500; font-size: 0.8rem; margin-top: 2rem;">
© 2026 NA GYM Montilla. Todos los derechos reservados.
</p>
</div>
""", unsafe_allow_html=True)