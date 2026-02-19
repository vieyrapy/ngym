from flask import Flask, render_template_string

app = Flask(__name__)

# El contenido completo de IA GYM integrado en Flask
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IA GYM Montilla | Transformación con Inteligencia</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
        body { font-family: 'Inter', sans-serif; scroll-behavior: smooth; }
        .animate-in { animation: fadeIn 0.5s ease-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-900">
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        // Helper para iconos de Lucide en entorno sin bundler
        const Icon = ({ name, className }) => {
            useEffect(() => {
                if (window.lucide) window.lucide.createIcons();
            }, [name]);
            return <i data-lucide={name} className={className}></i>;
        };

        const FAQItem = ({ question, answer }) => {
            const [isOpen, setIsOpen] = useState(false);
            return (
                <div className="border-b border-slate-200">
                    <button 
                        onClick={() => setIsOpen(!isOpen)}
                        className="w-full py-6 flex justify-between items-center text-left hover:text-[#ff9933] transition-colors"
                    >
                        <span className="text-lg font-bold text-slate-800">{question}</span>
                        <Icon name={isOpen ? "minus" : "plus"} className="text-[#ff9933]" />
                    </button>
                    {isOpen && (
                        <div className="pb-6 animate-in">
                            <p className="text-slate-600 leading-relaxed whitespace-pre-line">{answer}</p>
                        </div>
                    )}
                </div>
            );
        };

        const App = () => {
            const [isMenuOpen, setIsMenuOpen] = useState(false);

            const scrollTo = (id) => {
                const element = document.getElementById(id);
                if (element) {
                    element.scrollIntoView({ behavior: 'smooth' });
                    setIsMenuOpen(false);
                }
            };

            const Logo = () => (
                <div className="flex items-center gap-2 group cursor-pointer" onClick={() => window.scrollTo(0,0)}>
                    <div className="relative">
                        <div className="w-10 h-10 bg-[#ff9933] rounded-lg flex items-center justify-center transform group-hover:rotate-12 transition-transform">
                            <span className="text-white font-black text-xl italic uppercase">IA</span>
                        </div>
                        <div className="absolute -bottom-1 -right-1 w-5 h-5 text-gray-900 bg-white rounded-full p-0.5 flex items-center justify-center border">
                            <Icon name="dumbbell" className="w-3 h-3" />
                        </div>
                    </div>
                    <span className="font-black text-xl tracking-tighter text-gray-900">IA<span className="text-[#ff9933]">GYM</span></span>
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
                                    <Icon name={isMenuOpen ? "x" : "menu"} />
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
                            <div className="space-y-8 animate-in">
                                <div className="inline-flex items-center gap-2 bg-orange-100 text-[#ff9933] px-4 py-2 rounded-full font-bold text-sm tracking-wide uppercase">
                                    <Icon name="flame" className="w-4 h-4" /> Matrícula 100% Gratis - Solo esta semana
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
                                            ¡Lo necesito! <Icon name="arrow-right" />
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
                                            <Icon name="help-circle" className="w-6 h-6" />
                                        </div>
                                        <div>
                                            <p className="text-slate-800 font-bold leading-tight uppercase italic tracking-tighter">
                                                ¿Aún tienes dudas? <span className="text-[#ff9933]">No te preocupes.</span>
                                            </p>
                                            <p className="text-slate-500 font-semibold text-sm">
                                                Ven a probar <span className="text-slate-900 font-black">1 día GRATIS</span> sin compromiso.
                                            </p>
                                        </div>
                                        <Icon name="arrow-right" className="w-5 h-5 text-[#ff9933] ml-auto group-hover:translate-x-1 transition-transform" />
                                    </div>
                                </div>
                            </div>
                            <div className="relative">
                                <img 
                                    src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800" 
                                    alt="Entrenamiento Gym" 
                                    className="relative rounded-3xl shadow-2xl grayscale hover:grayscale-0 transition-all duration-500 object-cover aspect-square md:aspect-video lg:aspect-square"
                                />
                                <div className="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl hidden md:block border border-slate-100">
                                    <div className="flex items-center gap-4">
                                        <div className="bg-green-100 p-3 rounded-full">
                                            <Icon name="shield-check" className="text-green-600 w-6 h-6" />
                                        </div>
                                        <div>
                                            <p className="text-sm font-bold text-slate-500 uppercase">Sede Montilla</p>
                                            <p className="text-lg font-black italic uppercase">Abierto 06:30 - 22:00</p>
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
                                            <div className="bg-[#ff9933] text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest italic">6 Semanas</div>
                                            <div className="text-right">
                                                <span className="block text-slate-400 line-through text-sm italic">Antes 150€</span>
                                                <span className="text-4xl font-black text-[#ff9933]">99€</span>
                                            </div>
                                        </div>
                                        <h3 className="text-3xl font-black mb-4 uppercase italic tracking-tighter">Reduce la Barriga</h3>
                                        <p className="text-slate-300 mb-8 leading-relaxed">Elimina la grasa visceral y abdominal con trabajo focalizado en el Core.</p>
                                        <ul className="space-y-4 mb-10">
                                            <li className="flex items-center gap-3"><Icon name="check-circle-2" className="text-[#ff9933] w-5 h-5" /> 3 Sesiones / semana</li>
                                            <li className="flex items-center gap-3"><Icon name="check-circle-2" className="text-[#ff9933] w-5 h-5" /> Guía nutricional Anti-Inflamación</li>
                                        </ul>
                                        <button className="w-full bg-white text-slate-900 py-4 rounded-xl font-black text-lg hover:bg-[#ff9933] hover:text-white transition-all uppercase italic">Quiero empezar</button>
                                    </div>
                                </div>
                                <div className="bg-slate-800 rounded-3xl p-8 border border-slate-700 relative overflow-hidden group hover:border-[#ff9933] transition-all">
                                    <div className="relative z-10">
                                        <div className="flex justify-between items-start mb-6">
                                            <div className="bg-blue-500 text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest italic">3 Meses</div>
                                            <div className="text-right">
                                                <span className="block text-slate-400 line-through text-sm italic">Antes 199€</span>
                                                <span className="text-4xl font-black text-[#ff9933]">109€</span>
                                            </div>
                                        </div>
                                        <h3 className="text-3xl font-black mb-4 uppercase italic tracking-tighter">Adiós Grasa Total</h3>
                                        <p className="text-slate-300 mb-8 leading-relaxed">Pérdida de peso general y acondicionamiento integral definitivo.</p>
                                        <ul className="space-y-4 mb-10">
                                            <li className="flex items-center gap-3"><Icon name="check-circle-2" className="text-[#ff9933] w-5 h-5" /> 5 Sesiones / semana</li>
                                            <li className="flex items-center gap-3"><Icon name="check-circle-2" className="text-[#ff9933] w-5 h-5" /> Seguimiento mensual InBody</li>
                                        </ul>
                                        <button className="w-full bg-[#ff9933] text-white py-4 rounded-xl font-black text-lg hover:bg-orange-600 transition-all uppercase italic">¡Lo necesito ahora!</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* Planes de Membresía */}
                    <section id="planes" className="py-24 bg-white px-4">
                        <div className="max-w-7xl mx-auto">
                            <div className="text-center mb-16">
                                <h2 className="text-4xl md:text-5xl font-black text-slate-900 mb-4 tracking-tighter italic uppercase">Elige tu <span className="text-[#ff9933]">Plan</span></h2>
                                <p className="text-slate-500 text-lg font-medium">Matrícula GRATIS por tiempo limitado.</p>
                            </div>
                            <div className="grid md:grid-cols-3 gap-8">
                                {/* Planes Simplificados */}
                                <div className="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col hover:shadow-2xl transition-all">
                                    <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Anual OneClub</h4>
                                    <div className="mb-6 text-slate-900">
                                        <span className="text-4xl font-black">16,33€</span><span className="text-slate-500 font-bold">/mes</span>
                                    </div>
                                    <ul className="space-y-4 mb-10 flex-grow">
                                        <li className="flex items-center gap-2 text-sm font-semibold"><Icon name="check-circle-2" className="w-4 h-4 text-[#ff9933]" /> Evaluación Inbody Incluida</li>
                                        <li className="flex items-center gap-2 text-sm font-semibold text-[#ff9933] font-bold">Matrícula GRATIS</li>
                                    </ul>
                                    <button className="w-full py-4 border-2 border-slate-200 rounded-xl font-black text-center hover:bg-slate-900 hover:text-white transition-all uppercase italic">Adquirir plan</button>
                                </div>
                                <div className="bg-white rounded-3xl p-8 border-4 border-[#ff9933] flex flex-col relative scale-105 shadow-2xl shadow-orange-100">
                                    <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-[#ff9933] text-white px-6 py-1.5 rounded-full font-black text-xs uppercase italic">Recomendado</div>
                                    <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Anual MultiClub</h4>
                                    <div className="mb-6 text-slate-900">
                                        <span className="text-4xl font-black">26,33€</span><span className="text-slate-500 font-bold">/mes</span>
                                    </div>
                                    <ul className="space-y-4 mb-10 flex-grow">
                                        <li className="flex items-center gap-2 text-sm font-bold"><Icon name="check-circle-2" className="w-5 h-5 text-[#ff9933]" /> Acceso a TODA la red</li>
                                        <li className="flex items-center gap-2 text-sm font-bold text-[#ff9933]">Matrícula GRATIS</li>
                                    </ul>
                                    <button className="w-full py-4 bg-[#ff9933] text-white rounded-xl font-black text-center hover:bg-orange-600 transition-all uppercase italic shadow-lg">¡Lo necesito!</button>
                                </div>
                                <div className="bg-slate-50 rounded-3xl p-8 border-2 border-slate-100 flex flex-col hover:shadow-2xl transition-all">
                                    <h4 className="text-xl font-black mb-2 uppercase tracking-tighter italic">Mensual PAC</h4>
                                    <div className="mb-6 text-slate-900">
                                        <span className="text-4xl font-black">15,66€</span><span className="text-slate-500 font-bold">/mes</span>
                                    </div>
                                    <ul className="space-y-4 mb-10 flex-grow">
                                        <li className="flex items-center gap-2 text-sm font-semibold"><Icon name="check-circle-2" className="w-4 h-4 text-[#ff9933]" /> Sin permanencia</li>
                                        <li className="flex items-center gap-2 text-sm font-semibold text-[#ff9933] font-bold">Matrícula GRATIS</li>
                                    </ul>
                                    <button className="w-full py-4 border-2 border-slate-200 rounded-xl font-black text-center hover:bg-slate-900 hover:text-white transition-all uppercase italic">Apuntarme</button>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* FAQ Sección */}
                    <section id="faq" className="py-24 bg-slate-50 px-4">
                        <div className="max-w-3xl mx-auto">
                            <div className="text-center mb-16">
                                <h2 className="text-4xl font-black italic uppercase tracking-tighter">Preguntas <span className="text-[#ff9933]">Frecuentes</span></h2>
                                <p className="text-slate-500 mt-2 font-medium">Todo lo que necesitas saber sobre IA GYM Montilla.</p>
                            </div>
                            
                            <div className="bg-white rounded-[2.5rem] p-8 md:p-12 shadow-xl border border-slate-100">
                                <FAQItem 
                                    question="¿Cuáles son las formas de pago?" 
                                    answer="Presencial: Tarjetas en recepción en Montilla.\nOnline: A través de enlaces oficiales.\nNota: Ofertas trimestrales se abonan al inicio." 
                                />
                                <FAQItem 
                                    question="¿Hay que pagar matrícula?" 
                                    answer="¡Oferta Actual!: Matrícula 100% GRATIS en todos nuestros planes hoy." 
                                />
                                <FAQItem 
                                    question="¿Tienen permanencia?" 
                                    answer="Planes Mensuales: Sin permanencia. Planes Anuales/Trimestrales: Compromiso por descuento." 
                                />
                                <FAQItem 
                                    question="¿Tienen duchas y taquillas?" 
                                    answer="Duchas: Sí, vestuarios completos con agua caliente. Taquillas: Sí, trae tu propio candado." 
                                />
                                <FAQItem 
                                    question="¿Puedo ir a probar?" 
                                    answer="Sí, Pase de Día gratuito exclusivo para residentes de Montilla con cita previa." 
                                />
                                <FAQItem 
                                    question="¿Ofrecen nutrición?" 
                                    answer="Sí, asesorías personalizadas y bioimpedancia InBody para complementar tu entrenamiento." 
                                />
                            </div>
                        </div>
                    </section>

                    {/* Footer */}
                    <footer className="bg-slate-50 border-t border-slate-200 py-16 px-4">
                        <div className="max-w-7xl mx-auto grid md:grid-cols-4 gap-12 text-slate-900">
                            <div className="col-span-2">
                                <Logo />
                                <p className="mt-6 text-slate-500 max-w-sm font-medium">
                                    El gimnasio inteligente líder en Montilla. Especialistas en transformación física y nutrición.
                                </p>
                            </div>
                            <div>
                                <h5 className="font-black mb-6 uppercase tracking-widest text-sm italic">Contacto</h5>
                                <ul className="space-y-4 text-slate-500 font-bold text-sm uppercase">
                                    <li className="flex items-center gap-3"><Icon name="map-pin" className="text-[#ff9933] w-5 h-5" /> Montilla, Córdoba</li>
                                    <li className="flex items-center gap-3"><Icon name="phone" className="text-[#ff9933] w-5 h-5" /> +34 612 345 678</li>
                                </ul>
                            </div>
                            <div>
                                <h5 className="font-black mb-6 uppercase tracking-widest text-sm italic">Horarios</h5>
                                <p className="text-slate-500 font-bold text-sm uppercase">Lun - Vie: 06:30 - 22:00</p>
                                <p className="text-slate-500 font-bold text-sm uppercase">Sáb - Dom: Cerrado</p>
                            </div>
                        </div>
                        <div className="max-w-7xl mx-auto mt-16 pt-8 border-t border-slate-200 text-center">
                            <p className="text-slate-400 text-sm font-bold">© 2027 IA GYM Montilla. Todos los derechos reservados.</p>
                        </div>
                    </footer>
                </div>
            );
        };

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_CONTENT)

if __name__ == "__main__":
    app.run(debug=True)