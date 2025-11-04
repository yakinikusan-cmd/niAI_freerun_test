from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# index.html を返す
@app.route("/")
def index():
    return send_from_directory("Build", "index.html")

# Build フォルダ内の静的ファイル
@app.route("/Build/<path:filename>")
def build_files(filename):
    return send_from_directory(os.path.join("Build"), filename)

# TemplateData フォルダ内の静的ファイル
@app.route("/TemplateData/<path:filename>")
def template_files(filename):
    return send_from_directory(os.path.join("TemplateData"), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem","key.pem"))
