import streamlit as st
import re

# Configuración de la página
st.set_page_config(
    page_title="GenZlation",
    page_icon="🧠",
    layout="centered"
)

def normalizar_palabra(palabra, diccionario):
    """
    Limpia la palabra quitando prefijos, manejando plurales, géneros y 
    conjugaciones en pretérito perfecto simple para que coincida con el diccionario.
    """
    palabra = palabra.lower().strip()
    
    # 1. Quitar prefijos comunes (super-, mega-)
    if palabra.startswith("super") and len(palabra) > 5:
        palabra = palabra[5:]
    elif palabra.startswith("mega") and len(palabra) > 4:
        palabra = palabra[4:]
        
    # Si tras quitar el prefijo ya existe directamente, la devolvemos
    if palabra in diccionario:
        return palabra

    # 2. Manejo de verbos: Pretérito Perfecto Simple -> Infinitivo (-ar, -ear)
    terminaciones_pasado = {
        'é': 'ar', 'aste': 'ar', 'ó': 'ar', 'amos': 'ar', 'asteis': 'ar', 'aron': 'ar',
        'í': 'er', 'iste': 'er', 'ió': 'er', 'imos': 'er', 'isteis': 'er', 'ieron': 'er'
    }
    
    for term, reemplazo in terminaciones_pasado.items():
        if palabra.endswith(term):
            posible_verbo = palabra[:-len(term)] + reemplazo
            if posible_verbo in diccionario:
                return posible_verbo
            # Caso especial para verbos terminados en -ear (ej: ghostear -> ghostió / ghosteó)
            posible_verbo_ear = palabra[:-len(term)] + 'ear'
            if posible_verbo_ear in diccionario:
                return posible_verbo_ear
            # Caso específico para "devoraste" -> "devorar"
            if palabra.endswith("aste"):
                posible_devorar = palabra[:-4] + "ar"
                if posible_devorar in diccionario:
                    return posible_devorar

    # 3. Quitar plurales en inglés y español (-s, -es)
    excepciones_s = ["vibes", "facts", "factos", "factores", "amix", "la queso", "en mi era", "bajar de la nube", "it girl", "vibe check"]
    if palabra not in excepciones_s:
        if palabra.endswith('es') and len(palabra) > 4:
            palabra_sin_plural = palabra[:-2]
            if palabra_sin_plural in diccionario: return palabra_sin_plural
        elif palabra.endswith('s') and len(palabra) > 3:
            palabra_sin_plural = palabra[:-1]
            if palabra_sin_plural in diccionario: return palabra_sin_plural

    # 4. Unificación de género (-a, -as, -os -> -o / -ado / -ada)
    if palabra.endswith('as') or palabra.endswith('os'):
        palabra = palabra[:-2] + 'o'
    elif palabra.endswith('a') and not palabra.endswith('era') and palabra != "funa" and palabra != "neta":
        if palabra.endswith('ada'):
            posible_masec = palabra[:-3] + 'ado'
            if posible_masec in diccionario: return posible_masec
        posible_masc = palabra[:-1] + 'o'
        if posible_masc in diccionario: return posible_masc

    # 5. Mapeos o alias directos solicitados (delu -> delulu, obvi -> obvio)
    if palabra == "delu":
        return "delulu"
    if palabra == "obvi":
        return "obvio"

    return palabra

def traducir_jerga_genz(frase_original):
    # Diccionario Generación Z limpio y sin duplicados
    diccionario_jerga = {
        "en plan": "como 'si fuera', 'o sea', expresión usada para explicar o matizar algo",
        "en shock": "sorprendido, impactado o sin palabras ante una situación",
        "shock cultural": "impacto o sorpresa extrema al notar una gran diferencia de costumbres o estilos de vida",
        "ex": "expareja, o por extensión, algo que ya forma parte del pasado y con lo que no hay vínculo",
        "chisme": "el cotilleo, rumor o drama del momento que resulta muy interesante contar",
        "onda": "vibración, estilo o actitud que transmite una persona o situación",
        "la neta": "la pura verdad o la realidad de las cosas",
        "outfit": "el conjunto de ropa, calzado y accesorios que alguien lleva puesto",
        "amix": "forma cariñosa, neutra o informal de referirse a un amigo o amiga",
        "tipo": "expresión equivalente a 'por ejemplo' o 'como si fuera'",
        "delulu": "estar delirando o crearse expectativas irreales sobre algo (derivado de 'delusional')",
        "obvio": "usado para confirmar algo que es totalmente evidente",
        "flow": "estilo, ritmo, carisma o actitud genial que tiene una persona",
        "la queso": "frase que significa 'la que soporte', usada para presumir el éxito propio ante los envidiosos",
        "en mi era": "etapa de la vida enfocada en un estilo, estética, actitud o interés muy específico",
        "bajar de la nube": "hacer que alguien aterrice en la realidad y deje de hacerse falsas ilusiones",
        "factores": "verdades indiscutibles o argumentos lógicos con los que es imposible debatir (del inglés 'facts')",
        "it girl": "chica que marca tendencia, tiene un estilo único y es un referente de moda o actitud",
        "pec": "estar riquísimo o ser excelente",
        "basado": "con opiniones muy acertadas y firmes",
        "cringe": "vergüenza ajena",
        "ghostear": "desaparecer y dejar de responder de repente",
        "hype": "mucha emoción o altas expectativas",
        "red flag": "una señal de peligro o comportamiento alarmante",
        "servir": "lucir spectacular o hacer algo increíblemente bien",
        "funar": "cancelar o criticar públicamente a alguien",
        "npc": "una persona predecible o que no destaca",
        "bro": "amigo o hermano",
        "literal": "exactamente así, sin exagerar",
        "random": "aleatorio, imprevisto o extraño",
        "chill": "tranquilo o relajado", 
        "glow up": "una gran transformación física o de estilo para mejor",
        "padreado": "una respuesta magistral o dominio absoluto de la situación",
        "crush": "un flechazo o amor platónico",
        "shippear": "desear que dos personas formen una pareja",
        "flexear": "presumir o alardear de algo",
        "vibe check": "evaluar la energía o la actitud de alguien",
        "simp": "alguien que hace demasiado por complacer a la persona que le gusta",
        "impactrueno": "quedarse completamente en shock o sorprendido",
        "flopear": "fracasar estrepitosamente",
        "hater": "una persona difamadora o que critica con malicia",
        "main character": "ser el centro de atención o actuar como el protagonista",
        "aura": "el carisma, respeto o magnetismo que proyecta una persona",
        "rizz": "el encanto natural o la habilidad para seducir y gustar",
        "cocinar": "dejar que alguien actúe porque va a hacer algo brillante",
        "sigma": "una persona independiente, exitosa y solitaria",
        "moggear": "eclipsar a los demás por ser físicamente superior o más elegante",
        "un 10": "alguien o algo absolutamente perfecto",
        "un 7": "alguien o algo promedio o aceptable pero sin destacar",
        "un 6": "alguien o algo regular o de nivel medio bajo",
        "devorar": "hacer algo de forma impecable y sobresaliente",
        "lore": "la historia pasada o el trasfondo de la vida de una persona",
        "factos": "verdades o argumentos totalmente indiscutibles",
        "f en el chat": "una muestra de solidaridad o lástima ante una pequeña desgracia",
        "bucle": "estar obsesionado con repetir la misma acción o pensamiento",
        "yapping": "hablar demasiado o divagar sin ir a ninguna parte",
        "coquette": "un estilo muy refinado, tierno y marcadamente femenino",
        "nepo baby": "alguien que tiene éxito gracias al renombre de sus padres",
        "gatekeep": "ocultar información o un lugar para que no se vuelva popular",
        "out of pocket": "un comentario o comportamiento totalmente fuera de lugar",
        "aesthetic": "un estilo visual muy cuidado y armónico",
        "pick me girl": "alguien que busca atención de forma desesperada",
        "broca": "amigo o compañero",
        "ghosting": "desaparecer de la vida de alguien sin dar explicaciones",
        "gaslightear": "manipular psicológicamente a alguien",
        "gymbro": "un entusiasta obsesivo del gimnasio",
        "normie": "una persona muy común que sigue las modas sin criterio propio",
        "tryhard": "alguien que se esfuerza en exceso de forma casi obsesiva",
        "no cap": "te lo digo totalmente en serio y sin mentiras",
        "periodt": "y no hay más que hablar sobre este asunto",
        "slay": "triunfar de manera espectacular",
        "goat": "el mejor de todos los tiempos en su campo",
        "tea": "un chisme o cotilleo muy jugoso",
        "beef": "una rivalidad o pelea abierta entre dos personas",
        "heavy": "una situación muy intensa o sorprendente",
        "rent free": "algo en lo que no puedes dejar de pensar",
        "plot twist": "un giro de los acontecimientos totalmente inesperado",
        "same": "me ocurre exactamente lo mismo",
        "mood": "así es exactamente como me siento ahora",
        "vibes": "la energía o sensaciones que transmite algo",
        "stalkear": "espiar o cotillear el perfil de alguien en internet",
        "shitpost": "humor absurdo de internet de baja calidad",
        "clickbait": "un titular engañoso para llamar la atención",
        "trend": "una moda pasajera que se ha vuelto viral",
        "funa": "un linchamiento o reproche público en redes sociales",
        "green flag": "una señal de comportamiento positivo, maduro o saludable en una persona",
        "lowkey": "discretamente, en secreto o de forma moderada",
        "highkey": "totalmente en serio, de manera muy evidente o abierta",
        "ick": "un pequeño detalle o actitud ajena que provoca un rechazo o desagrado instantáneo",
        "side eye": "una mirada de reojo que expresa sospecha, juicio o desaprobación",
        "banger": "una canción o tema musical que es increíblemente bueno y pegadizo",
        "sus": "abreviatura de sospechoso, utilizado para señalar algo que genera desconfianza",
        "fr": "abreviatura de 'for real', que sirve para asegurar que algo es totalmente verdad",
        "giving": "transmitir una vibra muy específica o recordar mucho a un concepto",
        "left no crumbs": "hacer algo de manera tan impecable que no se puede mejorar",
        "soft launch": "dar pistas sutiles sobre una nueva relación en redes sin anunciarla formalmente",
        "hard launch": "anunciar de golpe y de manera 100% oficial una relación sentimental",
        "manifestar": "atraer un objetivo o deseo mediante el pensamiento positivo constante",
        "clown": "quedar en ridículo o sentirse tonto por haber creído algo que no pasó",
        "mewing": "gesto facial para marcar la mandíbula que se usa como meme para guardar silencio",
        "valid": "algo que es completamente comprensible, lógico o aceptable",
        "bussin": "expresión utilizada para describir que algo, especialmente la comida, está delicioso",
        "womp womp": "expresión burlona usada para restar importancia a las quejas de alguien",
        "clean girl": "estética basada en el minimalismo, la comodidad, la naturalidad y un aspecto pulcro",
        "touch grass": "salir a la realidad y despejar la mente fuera de las pantallas e internet",
        "comfort person": "persona de confianza que transmite paz, seguridad y apoyo emocional"
    }
    
    # Expresiones compuestas prioritarias (se removió "bajar de la nube" de aquí)
    expresiones_compuestas = [
        "en plan", "en shock", "shock cultural", "la neta", "la queso", "en mi era", "it girl", "red flag", "glow up", "vibe check", "main character", "un 10", "un 7", "un 6", "f en el chat", "nepo baby", "out of pocket", "pick me girl", "no cap", "rent free", "plot twist", 
        "green flag", "side eye", "left no crumbs", "soft launch", "hard launch", "womp womp", 
        "clean girl", "touch grass", "comfort person"  
    ]
    
    frase_procesada = frase_original
    
    # --- Detección inteligente de "bajar de la nube" conjugado ---
    patron_bajar = re.compile(r'\b(baj[a-zéíóúáñ]*)\s+de\s+la\s+nube\b', re.IGNORECASE)
    match_bajar = patron_bajar.search(frase_procesada)
    if match_bajar:
        texto_detectado = match_bajar.group(0)
        definicion = diccionario_jerga["bajar de la nube"]
        frase_procesada = patron_bajar.sub(f"<u>{texto_detectado}</u> [{definicion}]", frase_procesada)
    # --------------------------------------------------------------
    
    # Buscamos y traducimos las demás frases compuestas fijas
    for compuesta in expresiones_compuestas:
        patron = re.compile(r'\b' + re.escape(compuesta) + r'\b', re.IGNORECASE)
        if patron.search(frase_procesada):
            definicion = diccionario_jerga[compuesta]
            def reemplazar(match):
                return f"<u>{match.group(0)}</u> [{definicion}]"
            frase_procesada = patron.sub(reemplazar, frase_procesada)
            
    # Separamos el resto de palabras por espacios
    palabras_originales = frase_procesada.split()
    frase_traducida = []
    
    for palabra_or in palabras_originales:
        # Si ya contiene etiquetas HTML de las compuestas, saltarla
        if "<u>" in palabra_or:
            frase_traducida.append(palabra_or)
            continue
            
        # Extraemos los signos de puntuación del inicio y del final
        match = re.match(r'^([¡¿?!(,.:;)]*)(.*?)([!?,.:;)]*)$', palabra_or)
        if match:
            signos_inicio, palabra_core, signos_fin = match.groups()
        else:
            signos_inicio, palabra_core, signos_fin = "", palabra_or, ""
            
        # Normalizamos el núcleo de la palabra
        palabra_limpia = normalizar_palabra(palabra_core, diccionario_jerga)
            
        if palabra_limpia in diccionario_jerga:
            definicion = diccionario_jerga[palabra_limpia]
            palabra_formateada = f"{signos_inicio}<u>{palabra_core}</u> [{definicion}]{signos_fin}"
            frase_traducida.append(palabra_formateada)
        else:
            frase_traducida.append(palabra_or)
            
    resultado = " ".join(frase_traducida)
    return resultado

# --- Interfaz Gráfica (Streamlit UI) ---
st.title("GenZlation")
st.subheader("Diccionario en tiempo real para no quedarte fuera de la conversación")
st.write("Introduce aquí tus frases más delulu o confusas y te diremos qué significa realmente.")

st.write("")

# Caja de texto para el usuario
texto_usuario = st.text_area(
    "Escribe o pega aquí tu texto:",
    placeholder="Ejemplo: Megaghosteé a mi amix porque estaba superbasada y me dio cringe..."
)

# Contador y validación de palabras máximo 100
num_palabras = len(texto_usuario.split())
if texto_usuario.strip() != "":
    st.caption(f"Palabras introducidas: {num_palabras} / 100")

st.write("")

# Botón de acción
if st.button("✨ Traducir"):
    if texto_usuario.strip() == "":
        st.warning("Por favor, escribe algo primero.")
    elif num_palabras > 100:
        st.error(f"¡Has superado el límite! Tu texto tiene {num_palabras} palabras. El máximo permitido son 100.")
    else:
        resultado = traducir_jerga_genz(texto_usuario)
        
        st.success("¡Traducción realizada!")
        st.markdown("📝 **Texto Traducido:**")
        
        # Usamos st.write con unsafe_allow_html=True para procesar etiquetas <u>
        st.write(resultado, unsafe_allow_html=True)
