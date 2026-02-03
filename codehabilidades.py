import flet as ft
import random

estado_conversacion = {
    "esperando_detalle": False,
    "tema": None,
    "referencia": None,
    "cuentame_mas_dicho": False
}

PRIMERA_PERSONA = [
    "yo", "me", "me siento", "estoy", "siento", "tengo",
    "nosotros", "nosotras", "nos sentimos", "estamos", "sentimos"
]

PRONOMBRES_MASC = [
    "él", "ellos", "mi amigo", "mis amigos", "mi hermano",
    "mis hermanos", "mi novio", "unos amigos", "aquellos"
]

PRONOMBRES_FEM = [
    "ella", "ellas", "mi amiga", "mis amigas", "mi hermana",
    "mis hermanas", "mi novia", "unas amigas", "aquellas"
]

CONSEJOS = {
    "tristeza": [
        "Permítete sentir sin culparte. Estar triste no te hace débil.",
        "No tienes que tener todas las respuestas ahora mismo.",
        "A veces llorar también es una forma de sanar.",
        "Hablar con alguien de confianza puede aliviar más de lo que imaginas.",
        "Recuerda que este momento no define toda tu vida."
    ],
    "ansiedad": [
        "Respira lento: inhala 4 segundos, sostén 4 y exhala 6.",
        "La ansiedad miente, no todo lo que piensas es real.",
        "Concéntrate en lo que puedes controlar ahora.",
        "Reducir estímulos ayuda a calmar la mente.",
        "La ansiedad no te define."
    ],
    "estres": [
        "No todo tiene que resolverse hoy.",
        "Hacer pausas cortas ayuda más de lo que parece.",
        "Tu valor no depende de tu productividad.",
        "Dormir bien es una necesidad.",
        "A veces parar es avanzar."
    ],
    "enfado": [
        "Respira profundo antes de reaccionar.",
        "Alejarte de la situación puede ayudarte a calmarte.",
        "Es válido sentirse enojado, pero no actúes sobre impulsos dañinos.",
        "Hablar de lo que sientes reduce la tensión.",
        "Practicar la paciencia y la auto-compasión te ayuda a manejar la ira."
    ],
    "general": [
        "Cuidarte también es una responsabilidad.",
        "Pedir ayuda es valentía.",
        "Está bien no estar bien todo el tiempo.",
        "No todo problema necesita solución inmediata.",
        "Mereces tranquilidad."
    ],
    "suicidio": [
        "Si tienes pensamientos de lastimarte o quitarte la vida, por favor busca ayuda inmediatamente.",
        "No estás solo. Hablar con alguien profesional puede salvar tu vida.",
        "Respira profundo, no tomes decisiones en momentos de crisis.",
        "Contácta a alguien de confianza o un profesional de salud mental.",
        "Recuerda: tu vida importa y mereces apoyo."
    ],
    "violencia": [
        "Si sientes deseos de lastimar a alguien, aléjate y respira profundamente.",
        "Hablar con un profesional puede ayudarte a controlar estos impulsos.",
        "No actúes sobre la ira extrema, busca apoyo inmediatamente.",
        "Tu seguridad y la de los demás es lo más importante.",
        "Respira, calma tu mente y busca ayuda profesional."
    ],
    "miedo_extremo": [
        "El miedo intenso puede ser abrumador, respira y busca un lugar seguro.",
        "Habla con alguien de confianza sobre lo que sientes.",
        "Pequeños pasos de exposición gradual pueden ayudarte a manejarlo.",
        "No enfrentes situaciones peligrosas solo, pide ayuda.",
        "Recuerda que tus emociones son válidas, pero no tienes que enfrentarlas solo."
    ],
    "culpa_extrema": [
        "La culpa no siempre significa responsabilidad completa. Reflexiona y aprende.",
        "Hablar sobre tus errores con alguien puede aliviar la carga.",
        "Practica la auto-compasión, todos cometemos errores.",
        "Transforma la culpa en acciones positivas y aprendizaje.",
        "Recuerda: mereces perdonarte y seguir adelante."
    ],
    "frustracion_extrema": [
        "Toma un momento para respirar y alejarte de la situación.",
        "Dividir los problemas en pasos pequeños puede ayudarte.",
        "Hablar de lo que sientes reduce la tensión.",
        "Recuerda que tu valor no depende de un resultado.",
        "Practicar la paciencia y la auto-compasión es clave."
    ],
    "soledad": [
        "Buscar contacto con alguien de confianza puede aliviar la soledad.",
        "Hacer algo que disfrutes también ayuda a sentirte acompañado.",
        "No tienes que enfrentar todo solo, pedir ayuda es válido.",
        "Conectarte con un grupo o actividad puede ser positivo.",
        "Tus emociones son válidas, incluso la soledad."
    ],
    "aburrimiento": [
        "Probar algo nuevo puede ayudarte a salir del aburrimiento.",
        "Hacer pausas creativas o leer algo interesante puede motivarte.",
        "A veces descansar también es necesario, no lo ignores.",
        "Moverte o hacer ejercicio cambia tu energía y ánimo.",
        "Pequeñas metas o retos pueden hacer el día más entretenido."
    ],
    "felicidad": [
        "Disfruta estos momentos y celebra tus logros.",
        "Compartir tu alegría con otros la hace más grande.",
        "Registrar lo positivo ayuda a tu bienestar general.",
        "Agradecer por lo que tienes aumenta tu felicidad.",
        "Recuerda que está bien disfrutar de las cosas simples."
    ],
    "orgullo": [
        "Reconocer tus logros es importante, no te subestimes.",
        "Comparte tus éxitos con alguien que te apoye.",
        "Mantener la humildad y gratitud ayuda a seguir creciendo.",
        "El orgullo sano te impulsa a nuevos retos.",
        "Celebra lo que has conseguido, te lo mereces."
    ],
    "confusion": [
        "Tomarte un momento para reflexionar puede ayudar.",
        "Hacer preguntas o buscar información aclara dudas.",
        "Hablar con alguien de confianza puede dar perspectiva.",
        "No tienes que tener todas las respuestas ahora.",
        "Aceptar la confusión es el primer paso para entender."
    ],
    "sorpresa": [
        "Tómate un momento para procesar lo inesperado.",
        "Compartir lo que te sorprende con alguien puede ser divertido.",
        "La sorpresa también puede ser una oportunidad de aprendizaje.",
        "Disfruta lo inesperado cuando sea positivo.",
        "Reflexionar sobre la sorpresa puede ayudarte a adaptarte."
    ],
    "miedo": [
        "Respira profundo y analiza si hay acción inmediata que tomar.",
        "Compartir tus miedos con alguien de confianza ayuda a aliviarlos.",
        "Identificar exactamente qué te da miedo permite enfrentarlo paso a paso.",
        "No estás solo, tus emociones son válidas.",
        "Tomar pequeños pasos puede ayudarte a superar el miedo."
    ]
}

CONTACTO_PROFESIONAL = (
    "Si necesitas ayuda profesional inmediata, puedes contactar:\n"
    "- Línea de prevención del suicidio en Ecuador: 1800-333-889\n"
    "- Emergencias: 911\n"
    "- También puedes llamar a la Cruz Roja o a un psicólogo de confianza."
)

def detectar_nombre(mensaje):
    palabras = mensaje.split()
    for palabra in palabras:
        if palabra.istitle() and palabra.lower() not in ["hola", "mindly", "mi", "como", "cuando", "porque"]:
            return palabra
    return None

def detectar_referencia(mensaje, mensaje_original):
    mensaje = mensaje.lower()
    if any(p in mensaje for p in PRIMERA_PERSONA):
        if "nos" in mensaje:
            return "ustedes"
        return "tú"
    for p in PRONOMBRES_MASC:
        if p in mensaje:
            return "ellos" if "ellos" in p or "mis" in p or "unos" in p else "él"
    for p in PRONOMBRES_FEM:
        if p in mensaje:
            return "ellas" if "ellas" in p or "mis" in p or "unas" in p else "ella"
    nombre = detectar_nombre(mensaje_original)
    if nombre:
        return nombre
    return "esa persona"

def dar_consejo():
    tema = estado_conversacion["tema"]
    if tema in ["suicidio", "violencia"]:
        return random.choice(CONSEJOS[tema]) + "\n\n" + CONTACTO_PROFESIONAL
    if tema in CONSEJOS:
        return random.choice(CONSEJOS[tema])
    return random.choice(CONSEJOS["general"])

def analizar_mensaje(mensaje):
    global estado_conversacion
    mensaje_original = mensaje
    mensaje = mensaje.lower()
    referencia = detectar_referencia(mensaje, mensaje_original)

    if mensaje in ["gracias", "muchas gracias", "gracias mindly"]:
        return "Con gusto. Me alegra poder ayudarte. Aquí estaré si me necesitas."

    if "consejo" in mensaje:
        return dar_consejo()

    if estado_conversacion["esperando_detalle"]:
        estado_conversacion["esperando_detalle"] = False
        estado_conversacion["cuentame_mas_dicho"] = False
        if estado_conversacion["tema"] in ["tristeza", "ansiedad", "estres", "enfado",
                                           "soledad", "aburrimiento", "felicidad", "orgullo",
                                           "confusion", "sorpresa", "miedo"]:
            return "Gracias por contármelo. Entiendo cómo te sientes."
        if estado_conversacion["tema"] in ["suicidio", "violencia", "miedo_extremo",
                                           "culpa_extrema", "frustracion_extrema"]:
            return "Gracias por compartirlo conmigo. Recuerda que buscar apoyo profesional siempre ayuda."
        return "Gracias por confiarme eso."

    if mensaje in ["hola", "hola mindly", "buenas", "buenos dias", "buenas tardes", "buenas noches"]:
        return "Hola, estoy aquí contigo. ¿Cómo te sientes hoy?"

    if "triste" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "tristeza", "referencia": referencia})
        return "Siento que te sientas así. ¿Quieres contarme por qué?"
    if "ansiedad" in mensaje or "ansioso" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "ansiedad", "referencia": referencia})
        return "La ansiedad puede ser pesada. ¿Qué la está provocando?"
    if "estres" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "estres", "referencia": referencia})
        return "El estrés suele venir de mucha presión. ¿Qué lo causa?"
    if "enojado" in mensaje or "furioso" in mensaje or "rabia" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "enfado", "referencia": referencia})
        return "Veo que estás enojado. Respira profundo y cuéntame qué te hace sentir así."
    if "frustrado" in mensaje or "no puedo más" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "frustracion_extrema", "referencia": referencia})
        return "Veo que estás muy frustrado. ¿Quieres hablar más sobre lo que está pasando?"
    if "culpa" in mensaje or "me siento mal por" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "culpa_extrema", "referencia": referencia})
        return "Entiendo tu sentimiento de culpa. ¿Quieres contarme más sobre lo que pasó?"
    if "miedo" in mensaje and not ("extremo" in mensaje or "mucho" in mensaje):
        estado_conversacion.update({"esperando_detalle": True, "tema": "miedo", "referencia": referencia})
        return "Es normal sentir miedo a veces. ¿Quieres contarme qué te da miedo?"
    if "soledad" in mensaje or "solo" in mensaje or "sola" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "soledad", "referencia": referencia})
        return "Sentirse solo puede ser difícil. ¿Quieres hablar de ello?"
    if "aburrido" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "aburrimiento", "referencia": referencia})
        return "El aburrimiento puede ser pesado. ¿Qué te gustaría estar haciendo?"
    if "feliz" in mensaje or "contento" in mensaje or "alegre" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "felicidad", "referencia": referencia})
        return "¡Me alegra que te sientas así! ¿Qué te hace sentir feliz?"
    if "orgulloso" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "orgullo", "referencia": referencia})
        return "Es genial sentir orgullo por tus logros. Cuéntame más si quieres."
    if "confundido" in mensaje or "no entiendo" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "confusion", "referencia": referencia})
        return "A veces es normal sentirse confundido. ¿Quieres explicarme qué te tiene así?"
    if "sorprendido" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "sorpresa", "referencia": referencia})
        return "¡Vaya! Eso suena sorprendente. Cuéntame más si quieres."
    if "me quiero morir" in mensaje or "quiero morir" in mensaje or "suicid" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "suicidio", "referencia": referencia})
        return "Siento que te sientas así. Es muy importante hablar con alguien de confianza o un profesional.\n\n" + CONTACTO_PROFESIONAL + "\n\n¿Quieres contarme más sobre lo que estás sintiendo?"
    if "matar" in mensaje or "lastimar a alguien" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "violencia", "referencia": referencia})
        return "Parece que estás muy enfadado o con impulsos peligrosos.\n\n" + CONTACTO_PROFESIONAL + "\n\nPor favor aléjate y busca ayuda profesional inmediatamente. ¿Quieres contarme más sobre esto?"
    if "tengo mucho miedo" in mensaje or "temo" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "miedo_extremo", "referencia": referencia})
        return "Entiendo que tengas mucho miedo. Cuéntame más si quieres, estoy aquí para escucharte."
    if "me siento culpable" in mensaje:
        estado_conversacion.update({"esperando_detalle": True, "tema": "culpa_extrema", "referencia": referencia})
        return "Entiendo tu sentimiento de culpa. ¿Quieres contarme más sobre lo que pasó?"

    if mensaje in ["adios", "chao", "hasta luego", "me voy"]:
        estado_conversacion.update({"esperando_detalle": False, "tema": None, "referencia": None, "cuentame_mas_dicho": False})
        return "Gracias por hablar conmigo. Aquí estaré cuando lo necesites."

    if not estado_conversacion["cuentame_mas_dicho"]:
        estado_conversacion["cuentame_mas_dicho"] = True
        return "Cuéntame un poco más."

    return "Entiendo. Gracias por decírmelo."

def burbuja_bot(texto):
    return ft.Row(
        [ft.Container(content=ft.Text(texto), bgcolor=ft.Colors.BLUE_100, padding=10, border_radius=10, width=360)],
        alignment=ft.MainAxisAlignment.START
    )

def burbuja_usuario(texto):
    return ft.Row(
        [ft.Container(content=ft.Text(texto), bgcolor=ft.Colors.GREEN_100, padding=10, border_radius=10, width=360)],
        alignment=ft.MainAxisAlignment.END
    )

def main(page: ft.Page):
    page.title = "Mindly - Apoyo emocional"
    page.padding = 10

    header = ft.Row([ft.Icon(ft.Icons.SMART_TOY), ft.Text("Mindly", size=20, weight="bold")])
    chat_area = ft.Column(expand=True, scroll="auto")
    chat_area.controls.append(burbuja_bot("Hola, soy Mindly. Estoy aquí para escucharte."))

    input_box = ft.TextField(hint_text="Escribe tu mensaje...", expand=True)

    def enviar(e):
        mensaje = input_box.value.strip()
        if not mensaje:
            return
        chat_area.controls.append(burbuja_usuario(mensaje))
        respuesta = analizar_mensaje(mensaje)
        chat_area.controls.append(burbuja_bot(respuesta))
        input_box.value = ""
        page.update()

    send_button = ft.ElevatedButton("Enviar", on_click=enviar)
    input_row = ft.Row([input_box, send_button])
    page.add(header, chat_area, input_row)

ft.run(main)