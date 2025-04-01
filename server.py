from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="public") # Especifica que las plantillas están en la carpeta 'public'

@app.route('/')
def index():
    return render_template("index.html")  # Busca el HTML en /public

@app.route('/sumar', methods=['POST'])
def sumar():
    datos = request.get_json()
    matriz1 = datos.get("matriz1")
    matriz2 = datos.get("matriz2")

    if not matriz1 or not matriz2:
        return jsonify({"error": "Datos inválidos"}), 400

    resultado = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
