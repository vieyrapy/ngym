import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IA GYM Montilla - Transforma tu cuerpo",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inyección de CSS (Tailwind + Animaciones + Interactividad)
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
        
        html { scroll-behavior: smooth; }
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; }
        .stApp { background-color: #f8fafc; }

        /* Ocultar elementos de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Animaciones */
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.8s ease-out forwards; }
        
        /* FAQ Acordeón */
        details summary::-webkit-details-marker { display:none; }
        summary { list-style: none; outline: none; }
        details[open] summary i { transform: rotate(45deg); color: #ff9933; }
        summary i { transition: transform 0.3s ease; }
        
        /* Estilos de tarjetas */
        .card-hover:hover {
            transform: translateY(-8px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        /* Streamlit Input Fix */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
            background: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN ---
st.markdown("""
    <nav class="fixed top-0 w-full bg-white/90 backdrop-blur-md z-[100] border-b border-slate-200 py-4">
        <div class="max-w-7xl mx-auto px-6 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <div class="w-10 h-10 bg-[#ff9933] rounded-lg flex items-center justify-center">
                    <span class="text-white font-black text-xl italic uppercase">IA</span>
                </div>
                <span class="font-black text-xl tracking-tighter text-gray-900">IA<span class="text-[#ff9933]">GYM</span></span>
            </div>
            <div class="hidden md:flex items-center gap-8 font-bold text-xs uppercase tracking-wider">
                <a href="#programas" class="hover:text-[#ff9933] transition-colors">Programas</a>
                <a href="#planes" class="hover:text-[#ff9933] transition-colors">Planes</a>
                <a href="#clases" class="hover:text-[#ff9933] transition-colors">Clases Socios</a>
                <a href="#faq" class="hover:text-[#ff9933] transition-colors">Dudas</a>
                <a href="#contacto" class="bg-[#ff9933] text-white px-6 py-2.5 rounded-full hover:bg-[#e68a2e] transition-all shadow-lg shadow-orange-200">¡Empezar ahora!</a>
            </div>
        </div>
    </nav>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
    <section class="pt-40 pb-20 px-6">
        <div class="max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
            <div class="space-y-8 animate-fade-in">
                <div class="inline-flex items-center gap-2 bg-orange-100 text-[#ff9933] px-4 py-2 rounded-full font-bold text-sm tracking-wide uppercase">
                    <i class="fas fa-fire"></i> Matrícula 100% Gratis - Solo esta semana
                </div>
                <h1 class="text-5xl md:text-7xl font-black leading-[1.1] tracking-tight text-slate-900 uppercase italic">
                    Transforma tu cuerpo en <span class="text-[#ff9933]">Montilla.</span>
                </h1>
                <p class="text-xl text-slate-600 max-w-lg leading-relaxed">
                    Entrenamiento personalizado, tecnología InBody y los mejores programas de pérdida de grasa en Córdoba.
                </p>
                
                <div class="space-y-6">
                    <div class="flex flex-col sm:flex-row gap-4">
                        <a href="#planes" class="bg-[#ff9933] text-white px-10 py-5 rounded-2xl font-black text-xl hover:scale-105 transition-all shadow-2xl shadow-orange-300 flex items-center justify-center gap-2 uppercase italic text-center">
                            ¡Lo necesito! <i class="fas fa-arrow-right"></i>
                        </a>
                        <a href="#clases" class="bg-white text-slate-900 border-2 border-slate-200 px-10 py-5 rounded-2xl font-black text-xl hover:bg-slate-50 transition-all flex items-center justify-center gap-2 uppercase italic text-center">
                            Soy Socio
                        </a>
                    </div>

                    <div class="bg-slate-100 border-l-4 border-[#ff9933] p-4 rounded-r-2xl max-w-md flex items-center gap-4 group cursor-pointer hover:bg-white transition-all shadow-sm">
                        <div class="bg-white p-2 rounded-full shadow-sm text-[#ff9933]">
                            <i class="fas fa-question-circle fa-lg"></i>
                        </div>
                        <div>
                            <p class="text-slate-800 font-bold leading-tight uppercase italic tracking-tighter">
                                ¿Aún tienes dudas? <span class="text-[#ff9933]">No te preocupes.</span>
                            </p>
                            <p class="text-slate-500 font-semibold text-sm">
                                Ven a probar <span class="text-slate-900 font-black">1 día GRATIS</span> sin compromiso.
                            </p>
                        </div>
                        <i class="fas fa-arrow-right text-[#ff9933] ml-auto group-hover:translate-x-1 transition-transform"></i>
                    </div>
                </div>

                <div class="flex items-center gap-6 pt-4">
                    <div class="flex -space-x-3">
                        <img src="https://i.pravatar.cc/100?img=11" class="w-12 h-12 rounded-full border-4 border-white shadow-sm">
                        <img src="https://i.pravatar.cc/100?img=12" class="w-12 h-12 rounded-full border-4 border-white shadow-sm">
                        <img src="https://i.pravatar.cc/100?img=13" class="w-12 h-12 rounded-full border-4 border-white shadow-sm">
                        <img src="https://i.pravatar.cc/100?img=14" class="w-12 h-12 rounded-full border-4 border-white shadow-sm">
                    </div>
                    <p class="text-sm font-medium text-slate-500">
                        Más de <span class="text-slate-900 font-bold">500+ socios</span> activos en Montilla
                    </p>
                </div>
            </div>
            <div class="relative">
                <div class="absolute -inset-4 bg-[#ff9933]/20 rounded-3xl blur-3xl"></div>
                <div class="relative rounded-3xl overflow-hidden shadow-2xl grayscale hover:grayscale-0 transition-all duration-500">
                    <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800" class="w-full h-auto aspect-square object-cover">
                </div>
                <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl hidden md:block border border-slate-100">
                    <div class="flex items-center gap-4">
                        <div class="bg-green-100 p-3 rounded-full text-green-600">
                            <i class="fas fa-shield-alt fa-lg"></i>
                        </div>
                        <div>
                            <p class="text-sm font-bold text-slate-500 uppercase">Sede Montilla</p>
                            <p class="text-lg font-black italic uppercase">Abierto 07:00 - 22:00</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
""", unsafe_allow_html=True)

# --- PROGRAMAS ---
st.markdown("""
    <section id="programas" class="py-24 bg-slate-900 text-white overflow-hidden">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-black mb-4 uppercase italic tracking-tighter">Retos de <span class="text-[#ff9933]">Alto Impacto</span></h2>
                <p class="text-slate-400 text-lg">Programas focalizados con resultados garantizados.</p>
            </div>
            <div class="grid md:grid-cols-2 gap-8">
                <!-- Programa 1 -->
                <div class="bg-slate-800 rounded-3xl p-8 border border-slate-700 relative overflow-hidden group hover:border-[#ff9933] transition-all card-hover">
                    <div class="relative z-10">
                        <div class="flex justify-between items-start mb-6">
                            <div class="bg-[#ff9933] text-white px-4 py-1 rounded-full text-xs font-black uppercase italic tracking-widest">6 Semanas Intensivas</div>
                            <div class="text-right">
                                <span class="block text-slate-400 line-through text-sm italic">Antes 150€</span>
                                <span class="text-4xl font-black text-[#ff9933]">99€</span>
                            </div>
                        </div>
                        <h3 class="text-3xl font-black mb-4 uppercase italic tracking-tighter">Reduce la Barriga</h3>
                        <p class="text-slate-300 mb-8 leading-relaxed">Elimina la grasa visceral y subcutánea del abdomen. Trabajo focalizado en el Core.</p>
                        <ul class="space-y-4 mb-10 text-sm font-semibold">
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> 3 Sesiones presenciales / semana</li>
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Guía nutricional "Anti-Inflamación"</li>
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Medición de perímetros semanal</li>
                        </ul>
                        <button class="w-full py-4 bg-white text-slate-900 rounded-xl font-black hover:bg-[#ff9933] hover:text-white transition-all uppercase italic">Quiero acceder</button>
                    </div>
                    <i class="fas fa-bullseye absolute -bottom-10 -right-10 text-slate-700/20 text-[12rem] group-hover:text-[#ff9933]/10 transition-all"></i>
                </div>
                <!-- Programa 2 -->
                <div class="bg-slate-800 rounded-3xl p-8 border border-slate-700 relative overflow-hidden group hover:border-[#ff9933] transition-all card-hover">
                    <div class="relative z-10">
                        <div class="flex justify-between items-start mb-6">
                            <div class="bg-blue-500 text-white px-4 py-1 rounded-full text-xs font-black uppercase italic tracking-widest">3 Meses Total</div>
                            <div class="text-right">
                                <span class="block text-slate-400 line-through text-sm italic">Antes 199€</span>
                                <span class="text-4xl font-black text-[#ff9933]">109€</span>
                            </div>
                        </div>
                        <h3 class="text-3xl font-black mb-4 uppercase italic tracking-tighter">Adiós Grasa Total</h3>
                        <p class="text-slate-300 mb-8 leading-relaxed">Pérdida de peso general y acondicionamiento integral definitivo.</p>
                        <ul class="space-y-4 mb-10 text-sm font-semibold">
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> 5 Sesiones presenciales / semana</li>
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Guía nutricional "Quema Grasa Total"</li>
                            <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Seguimiento mensual progresivo</li>
                        </ul>
                        <button class="w-full py-4 bg-[#ff9933] text-white rounded-xl font-black hover:bg-orange-600 transition-all uppercase italic shadow-lg shadow-orange-900/20">¡Lo necesito ya!</button>
                    </div>
                    <i class="fas fa-fire absolute -bottom-10 -right-10 text-slate-700/20 text-[12rem] group-hover:text-[#ff9933]/10 transition-all"></i>
                </div>
            </div>
        </div>
    </section>
""", unsafe_allow_html=True)

# --- PLANES ---
st.markdown("""
    <section id="planes" class="py-24 px-6 bg-white">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16">
                <h2 class="text-4xl md:text-5xl font-black text-slate-900 mb-4 tracking-tighter italic uppercase">Elige tu <span class="text-[#ff9933]">Plan</span></h2>
                <p class="text-slate-500 text-lg font-medium">Matrícula GRATIS en todos nuestros planes por tiempo limitado.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8 items-stretch">
                <!-- OneClub -->
                <div class="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col card-hover">
                    <h4 class="text-xl font-black mb-2 uppercase italic">Anual OneClub</h4>
                    <div class="mb-6">
                        <span class="text-4xl font-black">16,33€</span><span class="text-slate-500 font-bold">/mes</span>
                        <p class="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Pago único anual 196€</p>
                    </div>
                    <ul class="space-y-4 mb-10 flex-grow text-sm font-semibold">
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> 1 Mes de regalo para ti + 1 Amigo</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Entrenamiento Personalizado</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Evaluación Inbody Incluida</li>
                        <li class="text-[#ff9933] font-bold">Matrícula 100% GRATIS</li>
                    </ul>
                    <button class="w-full py-4 border-2 border-slate-200 rounded-xl font-black hover:bg-slate-900 hover:text-white transition-all uppercase italic">Adquirir plan</button>
                </div>
                <!-- MultiClub -->
                <div class="bg-white rounded-3xl p-8 border-4 border-[#ff9933] flex flex-col relative scale-105 shadow-2xl shadow-orange-100">
                    <div class="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#ff9933] text-white px-6 py-1.5 rounded-full font-black text-xs uppercase italic tracking-widest">El más recomendado</div>
                    <h4 class="text-xl font-black mb-2 uppercase italic">Anual MultiClub</h4>
                    <div class="mb-6">
                        <span class="text-4xl font-black">26,33€</span><span class="text-slate-500 font-bold">/mes</span>
                        <p class="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Pago único anual 296€</p>
                    </div>
                    <ul class="space-y-4 mb-10 flex-grow text-sm font-bold">
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Acceso a TODA la red de clubes</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> 1 Mes de regalo para ti + 1 Amigo</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Entrenamiento Personalizado</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Evaluación física + InBody</li>
                        <li class="text-[#ff9933]">Matrícula GRATIS</li>
                    </ul>
                    <button class="w-full py-4 bg-[#ff9933] text-white rounded-xl font-black hover:bg-orange-600 transition-all uppercase italic shadow-lg shadow-orange-200">¡Lo necesito!</button>
                </div>
                <!-- PAC -->
                <div class="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col card-hover">
                    <h4 class="text-xl font-black mb-2 uppercase italic">Mensual PAC</h4>
                    <div class="mb-6">
                        <span class="text-4xl font-black">15,66€</span><span class="text-slate-500 font-bold">/mes</span>
                        <p class="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Renovación automática</p>
                    </div>
                    <ul class="space-y-4 mb-10 flex-grow text-sm font-semibold">
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Sin permanencia obligatoria</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> 1 Sesión Personal Trainer Gratis</li>
                        <li><i class="fas fa-check-circle text-[#ff9933] mr-2"></i> Congelamiento 30 días / año</li>
                        <li class="text-[#ff9933] font-bold">Matrícula GRATIS</li>
                    </ul>
                    <button class="w-full py-4 border-2 border-slate-200 rounded-xl font-black hover:bg-slate-900 hover:text-white transition-all uppercase italic">Apuntarme ahora</button>
                </div>
            </div>
        </div>
    </section>
""", unsafe_allow_html=True)

# --- CLASES ---
st.markdown("""
    <section id="clases" class="py-24 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-6">
            <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-8">
                <div class="max-w-2xl">
                    <div class="inline-block bg-[#ff9933] text-white px-4 py-1 rounded-full text-xs font-black uppercase italic tracking-widest mb-4">Solo para Socios</div>
                    <h2 class="text-4xl md:text-5xl font-black mb-4 uppercase italic tracking-tighter">Clases <span class="text-[#ff9933]">Grupales Exclusivas</span></h2>
                    <p class="text-slate-400 text-lg leading-relaxed">Potencia tus resultados con sesiones dirigidas. <span class="text-white font-bold italic underline">Aviso:</span> Reserva obligatoria mediante la App.</p>
                </div>
                <div class="flex flex-col gap-3">
                    <div class="bg-slate-800 border border-slate-700 p-4 rounded-2xl flex items-center gap-4">
                        <i class="fas fa-clock text-[#ff9933] text-2xl"></i>
                        <div><p class="text-xs font-bold text-slate-500 uppercase">Mañana</p><p class="text-lg font-black italic">08:00 AM | 09:00 AM</p></div>
                    </div>
                    <div class="bg-slate-800 border border-slate-700 p-4 rounded-2xl flex items-center gap-4">
                        <i class="fas fa-clock text-[#ff9933] text-2xl"></i>
                        <div><p class="text-xs font-bold text-slate-500 uppercase">Tarde / Noche</p><p class="text-lg font-black italic">18:00 PM (06:00 PM)</p></div>
                    </div>
                </div>
            </div>
            <div class="grid md:grid-cols-2 gap-8">
                <!-- Cycling -->
                <div class="group relative h-[450px] rounded-[3rem] overflow-hidden bg-slate-800 border border-slate-700 shadow-2xl">
                    <img src="https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&q=80&w=800" class="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:scale-110 transition-transform duration-1000">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent p-12 flex flex-col justify-end">
                        <div class="flex items-center gap-3 mb-4"><i class="fas fa-bicycle text-[#ff9933] text-3xl"></i><h3 class="text-4xl font-black uppercase italic">Cycling</h3></div>
                        <p class="text-slate-300 text-lg mb-8 max-w-sm">Ciclismo indoor con intervalos de intensidad variable. Mejora fuerza y potencia.</p>
                        <button class="bg-[#ff9933] text-white px-8 py-4 rounded-2xl font-black text-sm uppercase italic hover:bg-orange-600 transition-all text-center">Apuntarme</button>
                    </div>
                </div>
                <!-- TRX -->
                <div class="group relative h-[450px] rounded-[3rem] overflow-hidden bg-slate-800 border border-slate-700 shadow-2xl">
                    <img src="https://images.unsplash.com/photo-1544033527-b192daee1f5b?auto=format&fit=crop&q=80&w=800" class="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:scale-110 transition-transform duration-1000">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent p-12 flex flex-col justify-end">
                        <div class="flex items-center gap-3 mb-4"><i class="fas fa-running text-[#ff9933] text-3xl"></i><h3 class="text-4xl font-black uppercase italic">TRX Core</h3></div>
                        <p class="text-slate-300 text-lg mb-8 max-w-sm">Entrenamiento en suspensión enfocado en fortalecer el Core, espalda y piernas.</p>
                        <button class="bg-white text-slate-900 px-8 py-4 rounded-2xl font-black text-sm uppercase italic hover:bg-slate-100 transition-all text-center">Agendar mi lugar</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
""", unsafe_allow_html=True)

# --- FAQ SECCIÓN COMPLETA (19 PREGUNTAS) ---
faqs = [
    ("¿Cuáles son las formas de pago?", "Presencial: Aceptamos tarjetas de crédito/débito directamente en la recepción del gimnasio en Montilla.\nOnline: Aceptamos pagos a través de nuestros enlaces oficiales y plataforma web.\nNota: Para las ofertas trimestrales, se debe abonar el total al iniciar para congelar el precio promocional."),
    ("¿Hay que pagar matrícula de inscripción?", "¡Oferta Actual!: Estamos de oferta y actualmente TODA la matrícula es 100% GRATIS."),
    ("¿Tienen permanencia o contrato obligatorio?", "Planes Mensuales: No tienen permanencia. Puedes darte de baja avisando antes del día 25 del mes.\nPlanes Trimestrales: No son reembolsables, ya que el descuento especial se otorga por el compromiso de tiempo."),
    ("¿Tienen duchas y taquillas?", "Duchas: Sí, contamos con vestuarios completos y duchas con agua caliente.\nTaquillas: Sí. Es obligatorio traer tu propio candado por seguridad."),
    ("¿Puedo ir solo a probar antes de pagar?", "Sí, ofrecemos un 'Pase de Día' o una primera clase de valoración gratuita (exclusivo para residentes de Montilla). Es necesario agendar cita previa."),
    ("¿Cuáles son los horarios del gimnasio?", "Lunes a Viernes: 06:30 AM a 10:00 PM.\nSábados y Domingos: Cerrado."),
    ("¿Ofrecen clases dirigidas?", "Sí, contamos con Cycling y TRX. También contamos con programas exclusivos por tiempo limitado bajo consulta de disponibilidad."),
    ("¿Puedo cambiar de plan después de iniciar?", "Mensual: Sí, avisando con al menos 5 días de anticipación.\nTrimestral: No, se mantienen con el mismo beneficio durante los 3 meses."),
    ("¿Los niños pueden acceder al gimnasio?", "Por seguridad, solo mayores de 16 años pueden usar las instalaciones libres."),
    ("¿Ofrecen entrenamiento personal?", "Sí, sesiones individuales o en parejas. El costo es adicional y se agenda directamente con el personal."),
    ("¿Hay descuentos por familia o grupos?", "Actualmente no contamos con descuentos por grupo estandarizados, consulta en recepción para tu caso específico."),
    ("¿Puedo suspender mi membresía temporalmente?", "Sí, en planes mensuales puedes suspender hasta 1 mes máximo avisando previamente. Aplicable una vez cada 6 meses."),
    ("¿Tienen estacionamiento?", "Sí, contamos con estacionamiento gratuito para socios por orden de llegada."),
    ("¿Ofrecen servicios de nutrición?", "Sí, contamos con asesorías nutricionales personalizadas y planes alimenticios."),
    ("¿Puedo usar el gimnasio tras una lesión?", "Dependerá de la autorización médica. Recomendamos traer certificado. El entrenamiento adaptado es bajo tu responsabilidad."),
    ("¿El gimnasio proporciona toallas?", "No proporcionamos toallas (traer la propia es obligatorio por higiene).\nEquipo: Todo el equipo (pesas, bandas, etc.) está disponible."),
    ("¿Hay WiFi en el gimnasio?", "Sí, contamos con red WiFi gratuita para nuestros socios."),
    ("¿Ofrecen promociones por referidos?", "¡Sí! Si traes un amigo que se inscriba, ¡ambos reciben un Regalo Sorpresa exclusivo!"),
    ("¿Cómo puedo cancelar mi membresía?", "Opción A: Desde nuestra App.\nOpción B: En Recepción avisando al menos 5 días antes del cierre del ciclo.")
]

faq_html = "".join([f"""
    <details class="border-b border-slate-200 py-2">
        <summary class="w-full py-6 flex justify-between items-center text-left hover:text-[#ff9933] cursor-pointer font-bold text-lg text-slate-800">
            {q} <i class="fas fa-plus text-[#ff9933]"></i>
        </summary>
        <div class="pb-6 text-slate-600 leading-relaxed whitespace-pre-line">{a}</div>
    </details>
""" for q, a in faqs])

st.markdown(f"""
    <section id="faq" class="py-24 bg-slate-50 px-6">
        <div class="max-w-3xl mx-auto">
            <div class="text-center mb-16"><h2 class="text-4xl font-black italic uppercase tracking-tighter">Preguntas <span class="text-[#ff9933]">Frecuentes</span></h2></div>
            <div class="bg-white rounded-[2.5rem] p-8 md:p-12 shadow-xl border border-slate-100">{faq_html}</div>
        </div>
    </section>
""", unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown("""
    <section id="contacto" class="py-24 px-6 bg-white">
        <div class="max-w-5xl mx-auto bg-slate-900 rounded-[3rem] p-12 text-white relative overflow-hidden shadow-2xl">
            <div class="absolute top-0 right-0 w-1/3 h-full bg-[#ff9933] transform skew-x-12 translate-x-1/2 opacity-20"></div>
            <div class="relative z-10 grid md:grid-cols-2 gap-12 items-center">
                <div>
                    <h2 class="text-5xl font-black mb-6 leading-tight italic uppercase tracking-tighter">Entrena Gratis <span class="text-[#ff9933]">Hoy</span></h2>
                    <p class="text-slate-300 text-xl mb-8 font-medium leading-relaxed">Exclusivo para residentes de Montilla. Clase de valoración gratuita.</p>
                    <div class="space-y-4 text-slate-400 font-bold uppercase tracking-wide text-sm">
                        <p><i class="fas fa-check-circle text-[#ff9933] mr-3"></i> Sin compromisos</p>
                        <p><i class="fas fa-check-circle text-[#ff9933] mr-3"></i> Monitor asignado</p>
                        <p><i class="fas fa-check-circle text-[#ff9933] mr-3"></i> Estacionamiento Gratis</p>
                    </div>
                </div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="bg-white rounded-3xl p-8 text-slate-900 shadow-2xl relative z-20">', unsafe_allow_html=True)
    st.markdown('<h4 class="text-2xl font-black mb-6 text-center italic uppercase">Reserva tu prueba</h4>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        nombre = st.text_input("Nombre completo")
        email = st.text_input("Email")
        submit = st.form_submit_button("AGENDAR MI PRUEBA")
        if submit:
            if nombre and email: st.success(f"¡Reserva lista, {nombre}!")
            else: st.warning("Completa los campos.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""</div></div></section>""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <footer class="bg-slate-50 border-t border-slate-200 py-16 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-12 text-slate-900">
            <div class="col-span-2">
                <div class="flex items-center gap-2 mb-6">
                    <div class="w-8 h-8 bg-[#ff9933] rounded flex items-center justify-center text-white font-black italic">IA</div>
                    <span class="font-black text-lg uppercase tracking-tighter">IA<span class="text-[#ff9933]">GYM</span></span>
                </div>
                <p class="text-slate-500 max-w-sm font-medium">El gimnasio líder en Montilla. Especialistas en transformación física y nutrición.</p>
            </div>
            <div>
                <h5 class="font-black mb-6 uppercase text-sm italic tracking-widest">Ubicación</h5>
                <p class="text-slate-500 font-bold text-sm uppercase"><i class="fas fa-map-marker-alt text-[#ff9933] mr-2"></i> Montilla, Córdoba</p>
                <p class="text-slate-500 font-bold text-sm uppercase mt-4"><i class="fas fa-phone text-[#ff9933] mr-2"></i> +34 612 345 678</p>
            </div>
            <div>
                <h5 class="font-black mb-6 uppercase text-sm italic tracking-widest">Accesos</h5>
                <ul class="space-y-2 text-slate-500 font-black text-xs uppercase">
                    <li><a href="#programas" class="hover:text-[#ff9933]">Programas</a></li>
                    <li><a href="#planes" class="hover:text-[#ff9933]">Planes</a></li>
                    <li><a href="#faq" class="hover:text-[#ff9933]">Ayuda</a></li>
                </ul>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-slate-200 text-center">
            <p class="text-slate-400 text-sm font-bold">© 2027 IA GYM Montilla. Todos los derechos reservados.</p>
        </div>
    </footer>
""", unsafe_allow_html=True)