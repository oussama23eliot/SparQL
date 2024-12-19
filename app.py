from flask import Flask, render_template, request, jsonify
from SPARQLWrapper import SPARQLWrapper, JSON
import requests

app = Flask(__name__)

# Fonction pour exécuter des requêtes SPARQL dynamiques
def execute_sparql_query(query):
    sparql = SPARQLWrapper("https://dbpedia.org/sparql")  # Endpoint SPARQL de DBpedia
    sparql.setQuery(query)  # Requête dynamique
    sparql.setReturnFormat(JSON)  # Format JSON
    results = sparql.query().convert()  # Exécuter la requête et convertir les résultats
    return results

# Route pour l'accueil
@app.route('/')
def home():
    return render_template('index.html')

# Route pour les requêtes SPARQL
@app.route('/sparql', methods=['POST'])
def sparql():
    query = request.form['query']  # Récupérer la requête de l'utilisateur
    try:
        results = execute_sparql_query(query)  # Exécuter la requête
        return jsonify(results)  # Retourner les résultats en JSON
    except Exception as e:
        return jsonify({"error": str(e)})


# Lancer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
