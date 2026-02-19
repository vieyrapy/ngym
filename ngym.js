import React, { useState } from 'react';
import { 
  Dumbbell, 
  CheckCircle2, 
  Clock, 
  MapPin, 
  Phone, 
  Calendar, 
  Flame, 
  Target, 
  Users, 
  ArrowRight,
  ShieldCheck,
  ChevronDown,
  ChevronUp,
  Menu, 
  X,
  Plus,
  Minus,
  Bike,
  Activity,
  HelpCircle
} from 'lucide-react';

const FAQItem = ({ question, answer }) => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="border-b border-slate-200">
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className="w-full py-6 flex justify-between items-center text-left hover:text-[#ff9933] transition-colors"
      >
        <span className="text-lg font-bold text-slate-800">{question}</span>
        {isOpen ? <Minus className="text-[#ff9933]" /> : <Plus className="text-[#ff9933]" />}
      </button>
      {isOpen && (
        <div className="pb-6 animate-in fade-in slide-in-from-top-2 duration-300">
          <p className="text-slate-600 leading-relaxed whitespace-pre-line">{answer}</p>
        </div>
      )}
    </div>
  );
};

const App = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Colores y Configuración
  const primaryColor = "#ff9933";
  
  const scrollTo = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMenuOpen(false);
    }
  };

  const Logo = () => (
    <div className="flex items-center gap-2 group cursor-pointer">
      <div className="relative">
        <div className="w-10 h-10 bg-[#ff9933] rounded-lg flex items-center justify-center transform group-hover:rotate-12 transition-transform">
          <span className="text-white font-black text-2xl italic">N</span>
        </div>
        <Dumbbell className="absolute -bottom-1 -right-1 w-5 h-5 text-gray-900 bg-white rounded-full p-0.5" />
      </div>
      <span className="font-black text-xl tracking-tighter text-gray-900">Nacho<span className="text-[#ff9933]">GYM</span></span>
    </div>
  );

  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-900">
      {/* Navegación */}
      <nav className="fixed top-0 w-full bg-white/90 backdrop-blur-md z-50 border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            <Logo />
            
            <div className="hidden md:flex items-center gap-8">
              <button onClick={() => scrollTo('programas')} className="font-semibold text-sm hover:text-[#ff9933] transition-colors uppercase tracking-wider">Programas</button>
              <button onClick={() => scrollTo('planes')} className="font-semibold text-sm hover:text-[#ff9933] transition-colors uppercase tracking-wider">Planes</button>
              <button onClick={() => scrollTo('clases')} className="font-semibold text-sm hover:text-[#ff9933] transition-colors uppercase tracking-wider">Clases Socios</button>
              <button onClick={() => scrollTo('faq')} className="font-semibold text-sm hover:text-[#ff9933] transition-colors uppercase tracking-wider">Dudas</button>
              <button 
                onClick={() => scrollTo('contacto')}
                className="bg-[#ff9933] text-white px-6 py-2.5 rounded-full font-bold text-sm hover:bg-[#e68a2e] transition-all shadow-lg shadow-orange-200 uppercase tracking-wider"
              >
                ¡Empezar ahora!
              </button>
            </div>

            <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}>
              {isMenuOpen ? <X /> : <Menu />}
            </button>
          </div>
        </div>

        {/* Menú Móvil */}
        {isMenuOpen && (
          <div className="md:hidden bg-white border-t border-slate-100 p-4 space-y-4 shadow-xl">
            <button onClick={() => scrollTo('programas')} className="block w-full text-left font-bold p-2">PROGRAMAS</button>
            <button onClick={() => scrollTo('planes')} className="block w-full text-left font-bold p-2">PLANES</button>
            <button onClick={() => scrollTo('clases')} className="block w-full text-left font-bold p-2 text-[#ff9933]">CLASES SOCIOS</button>
            <button onClick={() => scrollTo('faq')} className="block w-full text-left font-bold p-2">PREGUNTAS</button>
            <button onClick={() => scrollTo('contacto')} className="block w-full text-center bg-[#ff9933] text-white p-3 rounded-xl font-bold">¡LO NECESITO!</button>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4">
        <div className="max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
          <div className="space-y-8 animate-in fade-in slide-in-from-left duration-700">
            <div className="inline-flex items-center gap-2 bg-orange-100 text-[#ff9933] px-4 py-2 rounded-full font-bold text-sm tracking-wide uppercase">
              <Flame className="w-4 h-4" /> Matrícula 100% Gratis - Solo esta semana
            </div>
            <h1 className="text-5xl md:text-7xl font-black leading-[1.1] tracking-tight text-slate-900 uppercase italic">
              Transforma tu cuerpo en <span className="text-[#ff9933]">Montilla.</span>
            </h1>
            <p className="text-xl text-slate-600 max-w-lg leading-relaxed">
              Entrenamiento personalizado, tecnología InBody y los mejores programas de pérdida de grasa en Córdoba.
            </p>
            
            <div className="space-y-6">
              <div className="flex flex-col sm:flex-row gap-4">
                <button 
                  onClick={() => scrollTo('planes')}
                  className="bg-[#ff9933] text-white px-10 py-5 rounded-2xl font-black text-xl hover:scale-105 transition-all shadow-2xl shadow-orange-300 flex items-center justify-center gap-2 uppercase italic"
                >
                  ¡Lo necesito! <ArrowRight />
                </button>
                <button 
                  onClick={() => scrollTo('clases')}
                  className="bg-white text-slate-900 border-2 border-slate-200 px-10 py-5 rounded-2xl font-black text-xl hover:bg-slate-50 transition-all flex items-center justify-center gap-2 uppercase italic"
                >
                  Soy Socio
                </button>
              </div>

              <div className="bg-slate-100 border-l-4 border-[#ff9933] p-4 rounded-r-2xl max-w-md flex items-center gap-4 group cursor-pointer hover:bg-white transition-all shadow-sm" onClick={() => scrollTo('contacto')}>
                <div className="bg-white p-2 rounded-full shadow-sm text-[#ff9933]">
                  <HelpCircle className="w-6 h-6" />
                </div>
                <div>
                  <p className="text-slate-800 font-bold leading-tight uppercase italic tracking-tighter">
                    ¿Aún tienes dudas? <span className="text-[#ff9933]">No te preocupes.</span>
                  </p>
                  <p className="text-slate-500 font-semibold text-sm">
                    Ven a probar <span className="text-slate-900 font-black">1 día GRATIS</span> sin compromiso.
                  </p>
                </div>
                <ArrowRight className="w-5 h-5 text-[#ff9933] ml-auto group-hover:translate-x-1 transition-transform" />
              </div>
            </div>

            <div className="flex items-center gap-6 pt-4">
              <div className="flex -space-x-3">
                {[1,2,3,4].map(i => (
                  <div key={i} className="w-12 h-12 rounded-full border-4 border-white bg-slate-200 overflow-hidden">
                    <img src={`https://i.pravatar.cc/100?img=${i+10}`} alt="usuario" />
                  </div>
                ))}
              </div>
              <p className="text-sm font-medium text-slate-500">
                Más de <span className="text-slate-900 font-bold">500+ socios</span> activos en Montilla
              </p>
            </div>
          </div>
          <div className="relative">
            <div className="absolute -inset-4 bg-[#ff9933]/20 rounded-3xl blur-3xl"></div>
            <img 
              src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800" 
              alt="Entrenamiento Gym" 
              className="relative rounded-3xl shadow-2xl grayscale hover:grayscale-0 transition-all duration-500 object-cover aspect-square md:aspect-video lg:aspect-square"
            />
            <div className="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl hidden md:block border border-slate-100">
              <div className="flex items-center gap-4">
                <div className="bg-green-100 p-3 rounded-full">
                  <ShieldCheck className="text-green-600 w-6 h-6" />
                </div>
                <div>
                  <p className="text-sm font-bold text-slate-500 uppercase">Sede Montilla</p>
                  <p className="text-lg font-black italic uppercase">Abierto 07:00 - 22:00</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Programas Especiales */}
      <section id="programas" className="py-24 bg-slate-900 text-white overflow-hidden">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-black mb-4 uppercase italic tracking-tighter">Retos de <span className="text-[#ff9933]">Alto Impacto</span></h2>
            <p className="text-slate-400 text-lg">Programas focalizados con resultados garantizados.</p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-slate-800 rounded-3xl p-8 border border-slate-700 relative overflow-hidden group hover:border-[#ff9933] transition-all">
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-6">
                  <div className="bg-[#ff9933] text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest italic">
                    6 Semanas Intensivas
                  </div>
                  <div className="text-right">
                    <span className="block text-slate-400 line-through text-sm italic">Antes 150€</span>
                    <span className="text-4xl font-black text-[#ff9933]">99€</span>
                  </div>
                </div>
                <h3 className="text-3xl font-black mb-4 uppercase italic tracking-tighter">Reduce la Barriga</h3>
                <p className="text-slate-300 mb-8 leading-relaxed">
                  Elimina la grasa visceral y subcutánea del abdomen. No es cardio genérico, es trabajo focalizado en el Core.
                </p>
                <ul className="space-y-4 mb-10">
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> 3 Sesiones presenciales / semana</li>
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Guía nutricional "Anti-Inflamación"</li>
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Medición de perímetros semanal</li>
                </ul>
                <a 
                  href="https://marketingparagimnasios.com/contacto" 
                  className="block text-center bg-white text-slate-900 py-4 rounded-xl font-black text-lg hover:bg-[#ff9933] hover:text-white transition-all shadow-lg uppercase italic"
                >
                  Quiero acceder al programa
                </a>
              </div>
              <Target className="absolute -bottom-10 -right-10 w-48 h-48 text-slate-700/20 group-hover:text-[#ff9933]/10 transition-colors" />
            </div>

            <div className="bg-slate-800 rounded-3xl p-8 border border-slate-700 relative overflow-hidden group hover:border-[#ff9933] transition-all">
              <div className="relative z-10">
                <div className="flex justify-between items-start mb-6">
                  <div className="bg-blue-500 text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest italic">
                    3 Meses Total
                  </div>
                  <div className="text-right">
                    <span className="block text-slate-400 line-through text-sm italic">Antes 199€</span>
                    <span className="text-4xl font-black text-[#ff9933]">109€</span>
                  </div>
                </div>
                <h3 className="text-3xl font-black mb-4 uppercase italic tracking-tighter">Adiós Grasa Total</h3>
                <p className="text-slate-300 mb-8 leading-relaxed">
                  Pérdida de peso general y acondicionamiento físico total. Para quienes buscan un cambio integral definitivo.
                </p>
                <ul className="space-y-4 mb-10">
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> 5 Sesiones presenciales / semana</li>
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Guía nutricional "Quema Grasa Total"</li>
                  <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Seguimiento mensual progresivo</li>
                </ul>
                <a 
                  href="https://marketingparagimnasios.com/" 
                  className="block text-center bg-[#ff9933] text-white py-4 rounded-xl font-black text-lg hover:bg-orange-600 transition-all shadow-lg shadow-orange-900/20 uppercase italic"
                >
                  ¡Lo necesito ahora!
                </a>
              </div>
              <Flame className="absolute -bottom-10 -right-10 w-48 h-48 text-slate-700/20 group-hover:text-[#ff9933]/10 transition-colors" />
            </div>
          </div>
        </div>
      </section>

      {/* Planes de Membresía */}
      <section id="planes" className="py-24 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-black text-slate-900 mb-4 tracking-tighter italic uppercase">Elige tu <span className="text-[#ff9933]">Plan</span></h2>
            <p className="text-slate-500 text-lg font-medium tracking-tight">Matrícula GRATIS en todos nuestros planes por tiempo limitado.</p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col hover:shadow-2xl transition-all">
              <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Anual OneClub</h4>
              <div className="mb-6 text-slate-900">
                <span className="text-4xl font-black">16,33€</span>
                <span className="text-slate-500 font-bold">/mes</span>
                <p className="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Pago único anual 196€</p>
              </div>
              <ul className="space-y-4 mb-10 flex-grow">
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> 1 Mes de regalo para ti + 1 Amigo</li>
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> Entrenamiento Personalizado</li>
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> Evaluación Inbody Incluida</li>
                <li className="flex items-center gap-2 text-sm font-semibold text-[#ff9933] font-bold">Matrícula 100% GRATIS</li>
              </ul>
              <a href="https://www.energyclub.cl/checkout" className="w-full py-4 border-2 border-slate-200 rounded-xl font-black text-center hover:bg-slate-900 hover:text-white transition-all uppercase italic">Adquirir plan</a>
            </div>

            <div className="bg-white rounded-3xl p-8 border-4 border-[#ff9933] flex flex-col relative scale-105 shadow-2xl shadow-orange-100">
              <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#ff9933] text-white px-6 py-1.5 rounded-full font-black text-xs uppercase tracking-widest italic">El más recomendado</div>
              <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Anual MultiClub</h4>
              <div className="mb-6 text-slate-900">
                <span className="text-4xl font-black">26,33€</span>
                <span className="text-slate-500 font-bold">/mes</span>
                <p className="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Pago único anual 296€</p>
              </div>
              <ul className="space-y-4 mb-10 flex-grow">
                <li className="flex items-center gap-2 text-sm font-bold"><CheckCircle2 className="w-5 h-5 text-[#ff9933]" /> Acceso a TODA la red de clubes</li>
                <li className="flex items-center gap-2 text-sm font-bold"><CheckCircle2 className="w-5 h-5 text-[#ff9933]" /> 1 Mes de regalo para ti + 1 Amigo</li>
                <li className="flex items-center gap-2 text-sm font-bold"><CheckCircle2 className="w-5 h-5 text-[#ff9933]" /> Entrenamiento Personalizado</li>
                <li className="flex items-center gap-2 text-sm font-bold"><CheckCircle2 className="w-5 h-5 text-[#ff9933]" /> Evaluación física + InBody</li>
                <li className="flex items-center gap-2 text-sm font-bold text-[#ff9933]">Matrícula GRATIS</li>
              </ul>
              <a href="https://www.energyclub.cl/checkout" className="w-full py-4 bg-[#ff9933] text-white rounded-xl font-black text-center hover:bg-orange-600 transition-all uppercase shadow-lg shadow-orange-200 italic">¡Lo necesito!</a>
            </div>

            <div className="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col hover:shadow-2xl transition-all">
              <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Mensual PAC</h4>
              <div className="mb-6 text-slate-900">
                <span className="text-4xl font-black">15,66€</span>
                <span className="text-slate-500 font-bold">/mes</span>
                <p className="text-xs text-slate-400 font-bold mt-1 uppercase italic tracking-wider">Renovación automática</p>
              </div>
              <ul className="space-y-4 mb-10 flex-grow">
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> Sin permanencia obligatoria</li>
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> 1 Sesión Personal Trainer Gratis</li>
                <li className="flex items-center gap-2 text-sm font-semibold"><CheckCircle2 className="w-4 h-4 text-[#ff9933]" /> Congelamiento 30 días / año</li>
                <li className="flex items-center gap-2 text-sm font-semibold text-[#ff9933] font-bold">Matrícula GRATIS</li>
              </ul>
              <a href="https://www.energyclub.cl/checkout" className="w-full py-4 border-2 border-slate-200 rounded-xl font-black text-center hover:bg-slate-900 hover:text-white transition-all uppercase italic">Apuntarme ahora</a>
            </div>
          </div>
        </div>
      </section>

      {/* Clases Exclusivas */}
      <section id="clases" className="py-24 bg-slate-900 text-white">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex flex-col md:flex-row justify-between items-end mb-12 gap-8">
            <div className="max-w-2xl">
              <div className="inline-block bg-[#ff9933] text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest mb-4 italic">
                Solo para Clientes Activos
              </div>
              <h2 className="text-4xl md:text-5xl font-black mb-4 uppercase italic tracking-tighter">Clases <span className="text-[#ff9933]">Grupales Exclusivas</span></h2>
              <p className="text-slate-400 text-lg leading-relaxed">
                Potencia tus resultados con nuestras sesiones dirigidas. <span className="text-white font-bold italic underline">Importante:</span> Para reservar tu cupo es obligatorio proporcionar tus datos en el agendamiento.
              </p>
            </div>
            <div className="flex flex-col gap-3">
              <div className="bg-slate-800 border border-slate-700 p-4 rounded-2xl flex items-center gap-4">
                <Clock className="text-[#ff9933] w-6 h-6" />
                <div>
                  <p className="text-xs font-bold text-slate-500 uppercase tracking-widest">Mañana</p>
                  <p className="text-lg font-black italic">08:00 AM | 09:00 AM</p>
                </div>
              </div>
              <div className="bg-slate-800 border border-slate-700 p-4 rounded-2xl flex items-center gap-4">
                <Clock className="text-[#ff9933] w-6 h-6" />
                <div>
                  <p className="text-xs font-bold text-slate-500 uppercase tracking-widest">Tarde / Noche</p>
                  <p className="text-lg font-black italic">18:00 PM (06:00 PM)</p>
                </div>
              </div>
            </div>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            <div className="group relative h-[450px] rounded-[3rem] overflow-hidden bg-slate-800 border border-slate-700 shadow-2xl">
              <img 
                src="https://images.unsplash.com/photo-1534258936925-c58bed479fcb?auto=format&fit=crop&q=80&w=800" 
                className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:scale-110 transition-transform duration-1000" 
                alt="Clase Cycling"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent p-12 flex flex-col justify-end">
                <div className="flex items-center gap-3 mb-4">
                  <Bike className="text-[#ff9933] w-8 h-8" />
                  <h3 className="text-4xl font-black uppercase italic tracking-tighter">Cycling</h3>
                </div>
                <p className="text-slate-300 text-lg mb-8 max-w-sm leading-relaxed font-medium">
                  Ciclismo indoor con intervalos de intensidad variable. Mejora fuerza, potencia y resistencia cardiovascular.
                </p>
                <div className="flex flex-col sm:flex-row gap-4">
                  <a 
                    href="#"
                    className="bg-[#ff9933] text-white px-8 py-4 rounded-2xl font-black text-sm uppercase italic hover:bg-orange-600 transition-all text-center flex items-center justify-center gap-2"
                  >
                    Apuntarme a la clase <ArrowRight className="w-4 h-4"/>
                  </a>
                </div>
              </div>
            </div>

            <div className="group relative h-[450px] rounded-[3rem] overflow-hidden bg-slate-800 border border-slate-700 shadow-2xl">
              <img 
                src="https://images.unsplash.com/photo-1544033527-b192daee1f5b?auto=format&fit=crop&q=80&w=800" 
                className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:scale-110 transition-transform duration-1000" 
                alt="Clase TRX"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent p-12 flex flex-col justify-end">
                <div className="flex items-center gap-3 mb-4">
                  <Activity className="text-[#ff9933] w-8 h-8" />
                  <h3 className="text-4xl font-black uppercase italic tracking-tighter">TRX Core</h3>
                </div>
                <p className="text-slate-300 text-lg mb-8 max-w-sm leading-relaxed font-medium">
                  Entrenamiento en suspensión. Enfocado totalmente en fortalecer el Core, integrando espalda, hombros y piernas.
                </p>
                <div className="flex flex-col sm:flex-row gap-4">
                  <a 
                    href="#"
                    className="bg-white text-slate-900 px-8 py-4 rounded-2xl font-black text-sm uppercase italic hover:bg-slate-100 transition-all text-center flex items-center justify-center gap-2"
                  >
                    Agendar mi lugar <ArrowRight className="w-4 h-4"/>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Sección Completa */}
      <section id="faq" className="py-24 bg-slate-50 px-4">
        <div className="max-w-3xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-black italic uppercase tracking-tighter">Preguntas <span className="text-[#ff9933]">Frecuentes</span></h2>
            <p className="text-slate-500 mt-2 font-medium tracking-tight">Todo lo que necesitas saber sobre NachoGYM Montilla.</p>
          </div>
          
          <div className="bg-white rounded-[2.5rem] p-8 md:p-12 shadow-xl border border-slate-100">
            <FAQItem 
              question="¿Cuáles son las formas de pago?" 
              answer="Presencial: Aceptamos tarjetas de crédito/débito directamente en la recepción del gimnasio en Montilla.\nOnline: Aceptamos pagos a través de nuestros enlaces oficiales y plataforma web.\nNota: Para las ofertas trimestrales, se debe abonar el total al iniciar para congelar el precio promocional." 
            />
            <FAQItem 
              question="¿Hay que pagar matrícula de inscripción?" 
              answer="¡Oferta Actual!: Estamos de oferta y actualmente TODA la matrícula es 100% GRATIS." 
            />
            <FAQItem 
              question="¿Tienen permanencia o contrato obligatorio?" 
              answer="Planes Mensuales: No tienen permanencia. Puedes darte de baja avisando antes del día 25 del mes.\nPlanes Trimestrales: No son reembolsables, ya que el descuento especial se otorga por el compromiso de tiempo adquirido." 
            />
            <FAQItem 
              question="¿Tienen duchas y taquillas?" 
              answer="Duchas: Sí, contamos con vestuarios completos y duchas con agua caliente.\nTaquillas (Lockers): Sí. Es obligatorio traer tu propio candado por seguridad para utilizarlas." 
            />
            <FAQItem 
              question="¿Puedo ir solo a probar antes de pagar?" 
              answer="Sí, ofrecemos un 'Pase de Día' o una primera clase de valoración gratuita (exclusivo para residentes de Montilla). Es necesario agendar cita previa para que un monitor pueda atenderte." 
            />
            <FAQItem 
              question="¿Cuáles son los horarios del gimnasio?" 
              answer="Lunes a Viernes: 06:30 AM a 10:00 PM.\nSábados y Domingos: Cerrado." 
            />
            <FAQItem 
              question="¿Ofrecen clases dirigidas?" 
              answer="Sí, contamos con Cycling y TRX. También contamos con programas exclusivos por tiempo limitado bajo consulta de disponibilidad." 
            />
            <FAQItem 
              question="¿Puedo cambiar de plan después de iniciar?" 
              answer="Mensual: Sí, puedes cambiar de plan avisando con al menos 5 días de anticipación.\nTrimestral: No, los planes trimestrales se mantienen con el mismo beneficio durante los 3 meses, sin cambios." 
            />
            <FAQItem 
              question="¿Los niños pueden acceder al gimnasio?" 
              answer="Por seguridad, solo mayores de 16 años pueden usar las instalaciones libres." 
            />
            <FAQItem 
              question="¿Ofrecen entrenamiento personal?" 
              answer="Sí, nuestros entrenadores ofrecen sesiones individuales o en parejas. El costo es adicional a la membresía y se agenda directamente con el personal." 
            />
            <FAQItem 
              question="¿Hay descuentos por familia o grupos?" 
              answer="Actualmente no contamos con descuentos por grupo estandarizados, pero puedes consultar en recepción para presentar tu caso específico." 
            />
            <FAQItem 
              question="¿Puedo suspender mi membresía temporalmente?" 
              answer="Sí, en planes mensuales puedes suspender hasta 1 mes máximo. Requiere aviso previo en recepción o plataforma y se aplica solo una vez cada 6 meses." 
            />
            <FAQItem 
              question="¿Tienen estacionamiento?" 
              answer="Sí, contamos con estacionamiento gratuito para socios por orden de llegada." 
            />
            <FAQItem 
              question="¿Ofrecen servicios de nutrición?" 
              answer="Sí, contamos con asesorías nutricionales personalizadas y planes alimenticios para complementar tu entrenamiento." 
            />
            <FAQItem 
              question="¿Puedo usar el gimnasio si me estoy recuperando de una lesión?" 
              answer="Dependerá del tipo de lesión y autorización médica. Recomendamos traer certificado médico. El entrenamiento adaptado estará bajo tu propia responsabilidad." 
            />
            <FAQItem 
              question="¿El gimnasio proporciona toallas o equipo personal?" 
              answer="Toallas: No proporcionamos toallas (traer la propia es obligatorio por higiene).\nEquipo: Todo el equipo de entrenamiento (pesas, bandas, colchonetas, etc.) está disponible para los socios." 
            />
            <FAQItem 
              question="¿Hay WiFi en el gimnasio?" 
              answer="Sí, contamos con red WiFi gratuita para nuestros socios." 
            />
            <FAQItem 
              question="¿Ofrecen bonos o promociones por referidos?" 
              answer="Sí, si traes un amigo que se inscriba, ¡ambos reciben un Regalo Sorpresa exclusivo!" 
            />
            <FAQItem 
              question="¿Cómo puedo cancelar mi membresía?" 
              answer="Opción A: Desde nuestra App cuando quieras.\nOpción B: En Recepción avisando al menos 5 días antes del cierre del ciclo de pago.\nNota: Membresías trimestrales no son reembolsables." 
            />
          </div>
        </div>
      </section>

      {/* CTA Final */}
      <section id="contacto" className="py-24 px-4 bg-white">
        <div className="max-w-5xl mx-auto bg-slate-900 rounded-[3rem] p-12 text-white relative overflow-hidden shadow-2xl">
          <div className="absolute top-0 right-0 w-1/3 h-full bg-[#ff9933] transform skew-x-12 translate-x-1/2 opacity-20"></div>
          
          <div className="relative z-10 grid md:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-5xl font-black mb-6 leading-tight italic uppercase tracking-tighter">Entrena Gratis <span className="text-[#ff9933]">Hoy</span></h2>
              <p className="text-slate-300 text-xl mb-8 leading-relaxed font-medium">Exclusivo para residentes de Montilla. Clase de valoración gratuita.</p>
              <div className="space-y-4 text-slate-400 font-bold uppercase tracking-wide text-sm">
                <div className="flex items-center gap-4"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Sin compromisos</div>
                <div className="flex items-center gap-4"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Con monitor asignado</div>
                <div className="flex items-center gap-4"><CheckCircle2 className="text-[#ff9933] w-5 h-5" /> Estacionamiento Gratis</div>
              </div>
            </div>
            
            <div className="bg-white rounded-3xl p-8 text-slate-900 shadow-2xl">
              <h4 className="text-2xl font-black mb-6 text-center italic uppercase">Reserva tu prueba</h4>
              <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                <input type="text" className="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-[#ff9933] outline-none font-semibold" placeholder="Nombre completo" />
                <input type="email" className="w-full bg-slate-50 border-2 border-slate-100 p-4 rounded-xl focus:border-[#ff9933] outline-none font-semibold" placeholder="Email" />
                <button className="w-full bg-[#ff9933] text-white py-5 rounded-2xl font-black text-xl hover:bg-orange-600 transition-all uppercase italic">
                  Agendar mi prueba
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-50 border-t border-slate-200 py-16 px-4">
        <div className="max-w-7xl mx-auto grid md:grid-cols-4 gap-12 text-slate-900">
          <div className="col-span-2">
            <Logo />
            <p className="mt-6 text-slate-500 max-w-sm font-medium leading-relaxed">
              El gimnasio líder en Montilla. Especialistas en transformación física, nutrición y entrenamiento de alta intensidad.
            </p>
          </div>
          
          <div>
            <h5 className="font-black mb-6 uppercase tracking-widest text-sm italic">Ubicación</h5>
            <ul className="space-y-4 text-slate-500 font-bold text-sm uppercase">
              <li className="flex items-center gap-3"><MapPin className="text-[#ff9933] w-5 h-5" /> Montilla, Córdoba</li>
              <li className="flex items-center gap-3"><Phone className="text-[#ff9933] w-5 h-5" /> +34 612 345 678</li>
              <li className="flex items-start gap-3">
                <Clock className="text-[#ff9933] w-5 h-5 mt-1" /> 
                <span>Lun - Vie<br/>06:30 - 22:00 hs</span>
              </li>
            </ul>
          </div>

          <div>
            <h5 className="font-black mb-6 uppercase tracking-widest text-sm italic">Accesos</h5>
            <ul className="space-y-4 text-slate-500 font-black text-xs uppercase tracking-wider">
              <li><button onClick={() => scrollTo('programas')} className="hover:text-[#ff9933]">Programas</button></li>
              <li><button onClick={() => scrollTo('planes')} className="hover:text-[#ff9933]">Planes</button></li>
              <li><button onClick={() => scrollTo('clases')} className="hover:text-[#ff9933]">Clases Grupales</button></li>
              <li><button onClick={() => scrollTo('faq')} className="hover:text-[#ff9933]">Ayuda / FAQ</button></li>
            </ul>
          </div>
        </div>
        
        <div className="max-w-7xl mx-auto mt-16 pt-8 border-t border-slate-200 flex flex-col md:row justify-between items-center gap-4">
          <p className="text-slate-400 text-sm font-bold">© 2027 NachoGYM Montilla. Todos los derechos reservados.</p>
        </div>
      </footer>
    </div>
  );
};

export default App;