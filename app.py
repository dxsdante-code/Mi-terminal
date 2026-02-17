from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("panel.html")

@app.route("/run/<script>")
def run(script):
    allowed = ["check_sat", "monitor_conavi"]
    if script not in allowed:
        return "Blocked"

    result = subprocess.check_output(f"python {script}.py", shell=True, text=True)
    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
