from flask import Flask, request, jsonify
from prompt import site_overview_prompt
from ml_model import generate_text
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)



@app.route('/generate', methods=['POST'])
def generate_endpoint():
    """
    Expects JSON payload with 'input' and 'prompt'.
    Returns JSON with 'result'.
    """
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input' in request body."}), 400

    user_input = data['input']
    prompt = site_overview_prompt
    try:
        result = generate_text(user_input, prompt)
        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)