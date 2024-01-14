from flask import Flask, request, jsonify, render_template
import json
import os
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lekcije')
def lessons():
    return render_template('lekcije.html')


@app.route('/kvizovi')
def quizzes():
    return render_template('kvizovi.html')

@app.route('/projekti')
def projects(): 
    return render_template('projekti.html', zadaci=zadaci)


def load_zadaci():
    with open('resursi/zadaci.json', 'r', encoding='utf-8') as file:
        zadaci = json.load(file)
    return zadaci

zadaci = load_zadaci()

@app.route('/analyze_prolog_code', methods=['POST'])
def analyze_prolog_code():
    data = request.get_json()
    prolog_code = data['code']
    analysis = analyze_code_intent(prolog_code)
    return jsonify({"analysis": analysis})

def analyze_code_intent(prolog_code):
    if 'djedbaka' in prolog_code:
        return "Ovaj kod pokušava otkriti unuke od osobe."
    elif 'factorial' in prolog_code:
        return "Ovaj kod računa faktorijel broja."
    elif 'voli_pizzu' in prolog_code:
        return "Ovaj kod provjerava koja osoba voli pizzu."
    elif 'putanja' in prolog_code:
        return "Ovaj kod provjerava postoji li put između dva ruba na grafu."
    elif 'kombinacija' in prolog_code:
        return "Ovaj kod provjerava sve moguce kombinacije tri broja."
    else:
        return "Nije mi jasno što se u kodu traži."
    
if __name__ == '__main__':
    app.run(debug=True)