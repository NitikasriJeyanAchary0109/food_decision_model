from flask import Flask, request, render_template_string

app = Flask(__name__)

# =========================
# HTML + CSS (INLINE)
# =========================
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>KNN Prediction App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            padding: 25px;
            width: 360px;
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            text-align: center;
        }

        h2 {
            color: #333;
            margin-bottom: 20px;
        }

        label {
            display: block;
            text-align: left;
            margin-top: 12px;
            font-weight: bold;
            color: #444;
        }

        select, input {
            width: 100%;
            padding: 8px;
            margin-top: 6px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            margin-top: 18px;
            padding: 10px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #1e40af;
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            color: green;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Food Decision Predictor</h2>

        <form method="POST">
            <label>Are you hungry?</label>
            <select name="hungry" required>
                <option value="">-- Select --</option>
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>

            <label>Is it weekend?</label>
            <select name="weekend" required>
                <option value="">-- Select --</option>
                <option value="Yes">Yes</option>
                <option value="No">No</option>
            </select>

            <button type="submit">Predict</button>
        </form>

        {% if result %}
            <div class="result">Prediction: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

# =========================
# ROUTE
# =========================
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        hungry = request.form.get("hungry")
        weekend = request.form.get("weekend")

        # ---- TEMP LOGIC (replace with KNN model later) ----
        if hungry == "Yes" and weekend == "Yes":
            result = "Order Food 🍕"
        elif hungry == "Yes":
            result = "Eat Something Light 🥪"
        else:
            result = "No Food Needed ❌"

    return render_template_string(HTML, result=result)

# =========================
# SAFE RUN (NO SIGNAL ERROR)
# =========================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
