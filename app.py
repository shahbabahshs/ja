from tiktokdown import ssstik
from igdown import sssig
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify({'/api/tiktok?url='})

@app.route('/api/tiktok', methods=["GET"])
def tiktok():
  url = request.args.get('url')
  if not url:
    return jsonify({"error": "URL is required"}), 400
  
  ssstik_result = ssstik(url)
  return jsonify({"video": ssstik_result[2],"mp3": ssstik_result[1]}), 200

  
@app.route('/api/instagram', methods=["GET"])
def ig():
  url = request.args.get('url')
  if not url:
    return jsonify({"error": "URL is required"}), 400
  
  ig_result = sssig(url)
  return jsonify({"video": ig_result[0],"thumbnail": ig_result[1]}), 200
