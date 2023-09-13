from tiktokdown import ssstik
from igdown import sssig
from flask import Flask, jsonify, request

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
  return f'{ssstik_result[2]}'

  
@app.route('/api/instagram', methods=["GET"])
def ig():
  url = request.args.get('url')
  if not url:
    return jsonify({"error": "URL is required"}), 400
  
  ig_result = sssig(url)
  return jsonify({"video": ig_result[0],"thumbnail": ig_result[1]})


@app.errorhandler(404)
def error_404(e):
    return 'Error 404', 404

@app.errorhandler(500)
def error_500(e):
    return 'Internal Server Error', 500
