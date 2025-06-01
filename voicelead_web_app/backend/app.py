
from flask import Flask, jsonify, request
from theory_engine import generate_exercise, check_voice_leading

app = Flask(__name__)

@app.route('/daily', methods=['GET'])
def get_daily():
    user_level = int(request.args.get('level', 1))
    progression = generate_exercise(user_level)
    return jsonify(progression)

@app.route('/check', methods=['POST'])
def check():
    user_input = request.json['chords']
    feedback = check_voice_leading(user_input)
    return jsonify({"feedback": feedback})

if __name__ == '__main__':
    app.run(debug=True)
