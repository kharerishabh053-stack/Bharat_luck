from flask import Flask, render_template_string  
import os  
  
app = Flask(__name__)  
  
# --- VIP INTERFACE CODE ---  
HTML = """  
<!DOCTYPE html>  
<html>  
<head>  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <style>  
        body { background: #000; color: #ffd700; font-family: sans-serif; text-align: center; margin: 0; }  
        .card { background: #111; margin: 20px; padding: 25px; border: 1px solid #ffd700; border-radius: 20px; box-shadow: 0 0 20px rgba(255,215,0,0.5); }  
        .btn { background: linear-gradient(180deg, #ffd700, #b8860b); color: #000; border: none; padding: 15px; border-radius: 12px; font-weight: bold; width: 90%; cursor: pointer; font-size: 18px; }  
        .header { padding: 20px; border-bottom: 1px solid #222; font-size: 24px; font-weight: bold; }  
    </style>  
</head>  
<body>  
    <div class="header">👑 BHARATLUCK VIP</div>  
    <div class="card">  
        <p style="color:#888;">CURRENT ASSETS</p>  
        <h1 style="font-size: 50px; margin: 10px 0;">₹500.00</h1>  
        <button class="btn">DEPOSIT NOW</button>  
    </div>  
    <p style="color: #444;">Live on Railway Cloud</p>  
</body>  
</html>  
"""  
  
@app.route('/')  
def home():  
    return render_template_string(HTML)  
  
if __name__ == "__main__":  
    port = int(os.environ.get("PORT", 8080))  
    app.run(host='0.0.0.0', port=port)
