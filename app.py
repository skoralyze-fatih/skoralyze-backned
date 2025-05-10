
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Skoralyze AI Backend Çalışıyor"

@app.route('/tahmin', methods=['GET'])
def tahmin():
    # Basit örnek tahmin kuralları
    ev_sahibi_form = request.args.get('ev_form', default=3, type=int)
    deplasman_form = request.args.get('dep_form', default=1, type=int)

    if ev_sahibi_form > deplasman_form:
        tahmin = "Maç Sonucu: 1"
    elif deplasman_form > ev_sahibi_form:
        tahmin = "Maç Sonucu: 2"
    else:
        tahmin = "Beraberlik"

    return jsonify({
        "tahmin": tahmin,
        "ev_sahibi_form": ev_sahibi_form,
        "deplasman_form": deplasman_form
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
