import streamlit as st
import streamlit.components.v1 as components

# Configuración de la pestaña del navegador
st.set_page_config(
    page_title="IA GYM Montilla | Transformación con Inteligencia",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo para ocultar los menús por defecto de Streamlit y que parezca una web pura
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stAppViewContainer"] {
                padding: 0;
            }
            [data-testid="stHeader"] {
                background-color: rgba(0,0,0,0);
            }
            iframe {
                border-radius: 0;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# El contenido completo de IA GYM (HTML + React + Tailwind)
HTML_CODE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
        body { font-family: 'Inter', sans-serif; scroll-behavior: smooth; background-color: #f8fafc; }
        .animate-in { animation: fadeIn 0.6s ease-out; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect } = React;

        const Icon = ({ name, className }) => {
            useEffect(() => { if (window.lucide) window.lucide.createIcons(); }, [name]);
            return <i data-lucide={name} className={className}></i>;
        };

        const FAQItem = ({ question, answer }) => {
            const [isOpen, setIsOpen] = useState(false);
            return (
                <div className="border-b border-slate-200">
                    <button onClick={() => setIsOpen(!isOpen)} className="w-full py-6 flex justify-between items-center text-left hover:text-[#ff9933] transition-colors">
                        <span className="text-lg font-bold text-slate-800">{question}</span>
                        <Icon name={isOpen ? "minus" : "plus"} className="text-[#ff9933]" />
                    </button>
                    {isOpen && <div className="pb-6 animate-in"><p className="text-slate-600 leading-relaxed whitespace-pre-line">{answer}</p></div>}
                </div>
            );
        };

        const App = () => {
            const [isMenuOpen, setIsMenuOpen] = useState(false);
            const scrollTo = (id) => { 
                const el = document.getElementById(id); 
                if(el) el.scrollIntoView({ behavior: 'smooth' });
                setIsMenuOpen(false);
            };

            return (
                <div className="min-h-screen">
                    <nav className="fixed top-0 w-full bg-white/90 backdrop-blur-md z-50 border-b border-slate-200 h-20">
                        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex justify-between items-center">
                            <div className="flex items-center gap-2 cursor-pointer" onClick={() => window.scrollTo(0,0)}>
                                <div className="w-10 h-10 bg-[#ff9933] rounded-lg flex items-center justify-center text-white italic font-black text-xl">IA</div>
                                <span className="font-black text-xl tracking-tighter">IA<span className="text-[#ff9933]">GYM</span></span>
                            </div>
                            <div className="hidden md:flex items-center gap-8 font-bold text-sm uppercase">
                                <button onClick={() => scrollTo('programas')} className="hover:text-[#ff9933]">Programas</button>
                                <button onClick={() => scrollTo('planes')} className="hover:text-[#ff9933]">Planes</button>
                                <button onClick={() => scrollTo('clases')} className="hover:text-[#ff9933]">Clases</button>
                                <button onClick={() => scrollTo('faq')} className="hover:text-[#ff9933]">Dudas</button>
                                <button onClick={() => scrollTo('contacto')} className="bg-[#ff9933] text-white px-6 py-2.5 rounded-full hover:bg-orange-600 transition-all shadow-lg">¡Empezar!</button>
                            </div>
                            <button className="md:hidden" onClick={() => setIsMenuOpen(!isMenuOpen)}><Icon name={isMenuOpen ? "x" : "menu"} /></button>
                        </div>
                    </nav>

                    <section className="pt-32 pb-20 px-4 max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-center">
                        <div className="space-y-8 animate-in">
                            <div className="inline-flex items-center gap-2 bg-orange-100 text-[#ff9933] px-4 py-2 rounded-full font-bold text-xs uppercase tracking-widest italic">Matrícula 100% GRATIS 2027</div>
                            <h1 className="text-5xl md:text-7xl font-black leading-tight uppercase italic">Transforma tu cuerpo en <span className="text-[#ff9933]">Montilla.</span></h1>
                            <p className="text-xl text-slate-600 max-w-lg">Entrenamiento inteligente, bioimpedancia InBody y nutrición de alto impacto en Córdoba.</p>
                            <div className="flex gap-4">
                                <button onClick={() => scrollTo('planes')} className="bg-[#ff9933] text-white px-10 py-5 rounded-2xl font-black text-xl shadow-xl hover:scale-105 transition-all uppercase italic flex items-center gap-2">¡Lo necesito! <Icon name="arrow-right"/></button>
                                <button onClick={() => scrollTo('contacto')} className="bg-white border-2 border-slate-200 px-10 py-5 rounded-2xl font-black text-xl hover:bg-slate-50 transition-all uppercase italic">Prueba Gratis</button>
                            </div>
                        </div>
                        <div className="relative">
                            <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&q=80&w=800" className="rounded-3xl shadow-2xl grayscale hover:grayscale-0 transition-all duration-500 aspect-square object-cover" />
                            <div className="absolute -bottom-6 -left-6 bg-white p-6 rounded-2xl shadow-xl border hidden md:block">
                                <p className="text-sm font-bold text-slate-500">SEDE MONTILLA</p>
                                <p className="text-lg font-black italic uppercase text-[#ff9933]">Abierto 06:30 - 22:00</p>
                            </div>
                        </div>
                    </section>

                    <section id="faq" className="py-24 bg-white px-4">
                        <div className="max-w-3xl mx-auto">
                            <h2 className="text-4xl font-black italic uppercase text-center mb-16">Preguntas <span className="text-[#ff9933]">Frecuentes</span></h2>
                            <div className="bg-slate-50 rounded-[2.5rem] p-8 md:p-12 border">
                                <FAQItem question="¿Cuáles son las formas de pago?" answer="Aceptamos tarjetas directamente en recepción y pagos online. Los planes anuales se abonan al inicio para asegurar el precio de oferta." />
                                <FAQItem question="¿Hay que pagar matrícula?" answer="¡Actualmente no! Estamos en promoción y la matrícula es 100% GRATIS." />
                                <FAQItem question="¿Tienen duchas y taquillas?" answer="Sí, vestuarios completos con agua caliente. Solo debes traer tu propio candado para las taquillas." />
                                <FAQItem question="¿Ofrecen planes de nutrición?" answer="Sí, incluimos pesaje InBody mensual y asesoría nutricional adaptada a tus objetivos." />
                                <FAQItem question="¿Cómo cancelo mi membresía?" answer="Puedes hacerlo desde nuestra App o avisando 5 días antes en recepción." />
                            </div>
                        </div>
                    </section>

                    <footer className="bg-slate-900 text-white py-16 px-4">
                        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8 border-b border-slate-800 pb-12">
                            <div>
                                <div className="font-black text-3xl italic mb-4">IA<span className="text-[#ff9933]">GYM</span></div>
                                <p className="text-slate-400 max-w-xs">El gimnasio líder en tecnología y resultados de Montilla.</p>
                            </div>
                            <div className="flex gap-8 text-sm font-bold uppercase italic text-slate-300">
                                <button onClick={() => scrollTo('planes')}>Planes</button>
                                <button onClick={() => scrollTo('faq')}>Dudas</button>
                                <button onClick={() => scrollTo('contacto')}>Prueba Gratis</button>
                            </div>
                        </div>
                        <p className="text-center mt-12 text-slate-500 font-bold">© 2027 IA GYM Montilla. Todos los derechos reservados.</p>
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

# Renderizar el componente
# El height se ajusta para que se vea toda la página sin scroll interno del iframe
components.html(HTML_CODE, height=3800, scrolling=False)