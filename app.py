from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Obtener el mensaje del cuerpo JSON de la solicitud
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Solicitud incorrecta, falta el campo "message"'}), 400

    user_input = str(data.get('message', '')).strip()
    respuesta = ""

    if user_input == '1':
        respuesta = ("Nutralie Energy Complex: Suplemento con ginseng, guaraná, L-carnitina y vitaminas B. "
                     "Ayuda a reducir el cansancio y mejora la concentración. "
                     "Ideal para quienes buscan mantener alto rendimiento físico y mental.")
    elif user_input == '2':
        respuesta = ("Nutralie Digestive Biprotics Complex: Mejora la digestión, alivia hinchazón e indigestión. "
                     "Con probióticos, enzimas, cúrcuma y aloe vera. "
                     "Apoya la salud intestinal y absorción de nutrientes. "
                     "Para personas con digestiones pesadas.")
    elif user_input == '3':
        respuesta = ("Nutralie Ashwagandha Complex: Con ashwagandha KSM-66, rhodiola rosea y vitaminas B6-B12. "
                     "Reduce el estrés, mejora el sueño y aporta energía. "
                     "Propiedades adaptógenas que ayudan al equilibrio emocional.")
    elif user_input == '4':
        respuesta = ("Nutralie Collagen Complex: Contiene colágeno hidrolizado, ácido hialurónico, biotina, zinc y vitaminas A, C, D y B12. "
                     "Mejora elasticidad de la piel, fortalece cabello y uñas, y apoya articulaciones.")
    elif user_input == '5':
        respuesta = ("Nutralie Magnesium Complex: Magnesio bisglicinato y citrato + vitaminas B5, B6 y C. "
                     "Reduce el cansancio, favorece músculos y huesos sanos, mejora el sistema nervioso y energía.")
    elif user_input == '6':
        respuesta = ("Nutralie Immunity Booster Complex: Refuerza el sistema inmune con vitaminas C, B6, B9, B12, minerales "
                     "(zinc, hierro, selenio, cobre) y extractos de reishi, propóleo y equinácea.")
    else:
        respuesta = "Lo siento, no he entendido tu elección. Por favor, elige un número del 1 al 6."

    return jsonify({'response': respuesta})

if __name__ == '__main__':
    app.run(debug=True)

