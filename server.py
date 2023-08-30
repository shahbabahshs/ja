from tiktokdown import ssstik
from igdown import sssig
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
  return '/api/tiktok?url='

@app.route('/api/tiktok', methods=["GET"])
def tiktok():
  url = request.args.get('url')
  if not url:
    return jsonify({"error": "URL is required"}), 400
  
  ssstik_result = ssstik(url)
  return jsonify({'video': {ssstik_result[2]}})

  
@app.route('/api/instagram', methods=["GET"])
def ig():
  url = request.args.get('url')
  if not url:
    return jsonify({"error": "URL is required"}), 400
  
  ig_result = sssig(url)
  return jsonify({"video": ig_result[0],"thumbnail": ig_result[1]}), 200

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port="8080")
