import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="GenZlation",
    page_icon="🧠",
    layout="centered"
)

def traducir_jerga_genz(frase_original):
    # Diccionario base con los significados principales
    diccionario_jerga = {
        "pec": "estar riquísimo o ser excelente",
        "basado": "con opiniones muy acertadas y firmes",
        "cringe": "vergüenza ajena",
        "ghostear": "desaparecer y dejar de responder de repente",
        "hype": "mucha emoción o altas expectativas",
        "red flag": "una señal de peligro o comportamiento alarmante",
        "servir": "lucir espectacular o hacer algo increíblemente bien",
        "funar": "cancelar o criticar públicamente a alguien",
        "npc": "una persona predecible o que no destaca",
        "bro": "amigo",
        "literal": "exactamente así",
        "random": "aleatorio o imprevisto",
        "chill": "tranquilo o relajado", 
        "glow up": "una gran transformación física o de estilo para mejor",
        "padreado": "una respuesta magistral o dominio absoluto de la situación",
        "crush": "un flechazo o amor platónico",
        "shippear": "desear que dos personas formen una pareja",
        "flexear": "presumir o alardear de algo",
        "delulu": "vivir en una fantasía o ser demasiado iluso",
        "vibe check": "evaluar la energía o la actitud de alguien",
        "simp": "alguien que hace demasiado por complacer a la persona que le gusta",
        "impactrueno": "quedarse completamente en shock o sorprendido",
        "era": "una etapa o fase específica de la vida",
        "flopar": "fracasar estrepitosamente",
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
        "basada": "persona que da su opinión sincera sin miedo a las críticas",
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
        "touch grass": "salir a la realidad y despejar la mente fuera de las pantallas e internet"
    }

    # Mapa de conjugaciones y variaciones frecuentes en presente para los verbos y adjetivos Gen Z
    # Esto ayuda a redirigir palabras flexionadas a su término original en el diccionario
    mapeo_variaciones = {
        # Verbo: servir
        "sirve": "servir", "sirven": "servir", "sirvo": "servir", "servimos": "servir", "sirves": "servir", "sirviendo": "servir",
        # Verbo: ghostear
        "ghostea": "ghostear", "ghostean": "ghostear", "ghosteo": "ghostear", "ghosteamos": "ghostear", "ghosteas": "ghostear", "ghosteando": "ghostear",
        # Verbo: funar
        "funa": "funar", "funan": "funar", "funo": "funar", "funamos": "funar", "funas": "funar", "funando": "funar",
        # Verbo: shippear
        "shippea": "shippear", "shippean": "shippear", "shippeo": "shippear", "shippeamos": "shippear", "shippeas": "shippear", "shippeando": "shippear",
        # Verbo: flexear
        "flexea": "flexear", "flexean": "flexear", "flexeo": "flexear", "flexeamos": "flexear", "flexeas": "flexear", "flexeando": "flexear",
        # Verbo: flopar
        "flopa": "flopar", "lopan": "flopar", "flopo": "flopar", "flopamos": "flopar", "flopando": "flopar",
        # Verbo: cocinar
        "cocina": "cocinar", "cocinan": "cocinar", "cocino": "cocinar", "cocinamos": "cocinar", "cocinas": "cocinar", "cocinando": "cocinar",
        # Verbo: devorar
        "devora": "devorar", "devoran": "devorar", "devoro": "devorar", "devoramos": "devorar", "devoras": "devorar", "devorando": "devorar",
        # Verbo: gaslightear
        "gaslightea": "gaslightear", "gaslightean": "gaslightear", "gaslighteo": "gaslightear", "gaslighteando": "gaslightear",
        # Verbo: stalkear
        "stalkea": "stalkear", "stalkean": "stalkear", "stalkeo": "stalkear", "stalkeamos": "stalkear", "stalkeas": "stalkear", "stalkeando": "stalkear",
        # Verbo: manifestar
        "manifiesta": "manifestar", "manifiestan": "manifestar", "manifiesto": "manifestar", "manifestamos": "manifestar", "manifestando": "manifestar",
        # Variaciones de género/número comunes
        "basada": "basado", "basados": "basado", "basadas": "basado",
        "coquettes": "coquette", "haters": "hater", "simps": "simp", "clowns": "clown", "normies": "normie", "gymbros": "gymbro"
    }

    frase_analisis_subrayado = frase_original
    terminos_compuestos = [k for k in diccionario_jerga.keys() if " " in k]
    mapa_reemplazos_subrayado = {}
    
    # 1. Procesar primero los términos compuestos (ej: "no cap", "plot twist")
    for i, termino in enumerate(terminos_compuestos):
        definicion = diccionario_jerga[termino]
        idx = frase_analisis_subrayado.lower().find(termino)
        
        while idx != -1:
            palabra_real = frase_analisis_subrayado[idx:idx+len(termino)]
            marca = f"[[_COMPUESTO_{i}_]]"
            mapa_reemplazos_subrayado[marca] = f"<u>{palabra_real}</u> [{definicion}]"
            frase_analisis_subrayado = frase_analisis_subrayado[:idx] + marca + frase_analisis_subrayado[idx+len(termino):]
            idx = frase_analisis_subrayado.lower().find(termino)

    # 2. Procesar palabras individuales y formas conjugadas
    palabras_subrayado = frase_analisis_subrayado.split()
    resultado_subrayado_lista = []
    
    for p_sub in palabras_subrayado:
        if "[[_COMPUESTO_" in p_sub:
            resultado_subrayado_lista.append(p_sub)
            continue
            
        # Extraer la palabra limpia de signos de puntuación
        palabra_limpia_dict = p_sub.lower()
        for signo in [".", ",", "!", "¡", "?", "¿", ":", ";"]:
            palabra_limpia_dict = palabra_limpia_dict.replace(signo, "")
            
        # Determinar el término clave (ya sea directo o mediante su conjugación/variación)
        clave_encontrada = None
        if palabra_limpia_dict in diccionario_jerga:
            clave_encontrada = palabra_limpia_dict
        elif palabra_limpia_dict in mapeo_variaciones:
            clave_encontrada = mapeo_variaciones[palabra_limpia_dict]
            
        if clave_encontrada and " " not in clave_encontrada:
            definicion = diccionario_jerga[clave_encontrada]
            
            # Aislar los signos originales que puedan estar pegados al principio o al final
            if p_sub.lower().startswith(palabra_limpia_dict):
                parte_palabra = p_sub[:len(palabra_limpia_dict)]
                parte_signos = p_sub[len(palabra_limpia_dict):]
                formato_subrayado = f"<u>{parte_palabra}</u> [{definicion}]{parte_signos}"
            else:
                formato_subrayado = p_sub.replace(palabra_limpia_dict, f"<u>{palabra_limpia_dict}</u> [{definicion}]")
                
            resultado_subrayado_lista.append(formato_subrayado)
        else:
            resultado_subrayado_lista.append(p_sub)
            
    texto_subrayado = " ".join(resultado_subrayado_lista)
    
    # 3. Restaurar los términos compuestos guardados
    for marca, reemplazo in mapa_reemplazos_subrayado.items():
        texto_subrayado = texto_subrayado.replace(marca, reemplazo)
        
    return texto_subrayado

# --- Interfaz Gráfica (Streamlit UI) ---
st.title("GenZlation")
st.subheader("Diccionario en tiempo real para no quedarte fuera de la conversación")
st.write("Introduce aquí tus frases más delulu o confusas y te diremos qué significa realmente.")

st.write("")

# Caja de texto para el usuario
texto_usuario = st.text_area(
    "Escribe o pega aquí tu texto:",
    placeholder="Ejemplo: Ese outfit sirve demasiado, estás basado pero eres un poco delulu..."
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
        res_subrayado = traducir_jerga_genz(texto_usuario)
        
        st.success("¡Traducción realizada!")
        st.markdown("📝 **Texto Traducido y Analizado:**")
        st.write(res_subrayado, unsafe_allow_html=True)
        