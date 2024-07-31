from flask import Flask, render_template, request, jsonify
import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
chemin_parent = r"D:\Engineering\GPM4"
sys.path.append(chemin_parent)
from model.Head_Of_Model.GPM4 import GPM4_Head

def mon_programme(mot, lgh, level_c, temperature, mode_model, auto_apce):
    if mode_model == "Completion":
        reaction = 0
    else:
        reaction = 1
    if auto_apce == "Automatic":
        auto_apce = True
    else:
        auto_apce = False
    configure_GPM = {   "prompt": mot,
                        "temperature" : temperature,
                        "maximum lenght" : lgh,
                        "reaction" : reaction,
                        "retroaction" : 1,
                        "reward" : 1,
                        "Level C" : level_c,
                        "space" : auto_apce,
                        "training_on_context" : "False",
                        "text_add" : "False",
                        "correction" : "",
                        "recursion" : 0,
                        "RL" : False
                        }

    configure_GPM = {   "prompt": mot,
                        "temperature" : temperature,
                        "maximum lenght" : lgh,
                        "reaction" : 0,
                        "retroaction" : 1,
                        "reward" : 1,
                        "Level C" : level_c,
                        "space" : auto_apce,
                        "training_on_context" : "False",
                        "text_add" : "False",
                        "correction" : "",
                        "recursion" : 0,
                        "RL" : False,
                        "recursivite": True,
                        "EngineState" : True
                        
                        

                    }
    
                        

                    
    result = GPM4_Head(configure_GPM)
    print(result)
    return result

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        mot = request.form.get('mot')  # Récupérer le mot à partir du formulaire
        lg = request.form.get('lg')
        print(lg)

        level_C = request.form.get('compOfModel')
        auto_space = request.form.get("space")
        mode_Model = request.form.get('mode')
        temperature = request.form.get("tempOfModel")
        temperature = int(temperature)
        if temperature >= 10:
            temperature = temperature / 100
            temperature = round(temperature, 1)
        else:
            temperature = 0.1
            
        data = mon_programme(mot, int(lg), float(level_C), float(temperature), mode_Model, auto_space)
        return jsonify(result=data)  # Retourne le résultat sous forme JSON
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
