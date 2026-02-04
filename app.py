from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple ML Input App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .box {
            background: white;
            padding: 25px;
            width: 350px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        label {
            display: block;
            text-align: left;
            margin-top: 10px;
            font-weight: bold;
        }

        select, button {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }

        button {
            margin-top: 15px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #0056b3;
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
    <div class="box">
        <h2>Food Decision Model</h2>

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

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        hungry = request.form.get("hungry")
        weekend = request.form.get("weekend")

        # 👉 Replace this logic with your ML model later
        if hungry == "Yes" and weekend == "Yes":
            result = "Order Food 🍕"
        elif hungry == "Yes":
            result = "Eat Something Light 🥪"
        else:
            result = "No Food Needed ❌"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
