from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").strip()

    respuesta = ""

    if mensaje == "1":
        respuesta = "🔋 Recomendación para Energía y vitalidad:<br><strong>Nutralie Energy Complex</strong><br>Con ginseng, guaraná, L-carnitina y vitaminas del grupo B. Ayuda a reducir el cansancio y mejora la concentración."
    elif mensaje == "2":
        respuesta = "🦠 Recomendación para Digestión:<br><strong>Nutralie Digestive Enzymes</strong><br>Contiene 7 enzimas digestivas que mejoran la absorción de nutrientes y reducen gases."
    elif mensaje == "3":
        respuesta = "🛌 Recomendación para Estrés y sueño:<br><strong>Nutralie Ashwagandha Complex</strong><br>Reduce el estrés y mejora el descanso gracias a la melisa y la vitamina B6."
    elif mensaje == "4":
        respuesta = "💅 Recomendación para Piel, cabello y colágeno:<br><strong>Nutralie Collagen Complex</strong><br>Con colágeno marino, ácido hialurónico, vitamina C y zinc. Mejora la elasticidad de la piel y fortalece uñas y cabello."
    elif mensaje == "5":
        respuesta = "💊 Recomendación para Dolor de cabeza:<br><strong>Nutralie Ashwagandha Complex</strong> y <strong>Nutralie Magnesium</strong><br>Combinación ideal para relajar el sistema nervioso y reducir la fatiga mental."
    elif mensaje == "6":
        respuesta = "🛡️ Recomendación para Inmunidad:<br><strong>Nutralie Immune Complex</strong><br>Con vitamina C, D3, zinc y equinácea para reforzar defensas y recuperación."
    else:
        respuesta = "❌ Por favor, escribe un número del 1 al 6."

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

