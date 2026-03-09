from flask import Flask, render_template_string, request, redirect, url_for  
  
app = Flask(__name__)  
  
# --- HTML TEMPLATES (Sab ek hi file mein) ---  
  
# 1. LOGIN PAGE  
LOGIN_HTML = """  
<!DOCTYPE html>  
<html>  
<head>  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>BharatLuck Login</title>  
    <style>  
        body { background: #121212; color: white; font-family: sans-serif; text-align: center; padding-top: 100px; }  
        .login-card { background: #1e1e1e; padding: 30px; border-radius: 15px; display: inline-block; border: 1px solid #ffd700; width: 80%; max-width: 350px; }  
        input { width: 90%; padding: 12px; margin: 10px 0; border-radius: 5px; border: none; }  
        button { background: #ffd700; color: black; padding: 12px; width: 95%; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }  
    </style>  
</head>  
<body>  
    <div class="login-card">  
        <h2 style="color:#ffd700">👑 BHARATLUCK VIP</h2>  
        <p>Login with Phone Number</p>  
        <form action="/login" method="POST">  
            <input type="text" name="phone" placeholder="Phone Number" required>  
            <input type="password" name="otp" placeholder="Enter PIN" required>  
            <button type="submit">LOGIN NOW</button>  
        </form>  
    </div>  
</body>  
</html>  
"""  
  
# 2. GAME PAGE  
GAME_HTML = """  
<!DOCTYPE html>  
<html>  
<head>  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Dashboard</title>  
    <style>  
        body { background: #0f0f0f; color: white; font-family: sans-serif; text-align: center; margin: 0; }  
        .header { background: #1e1e1e; padding: 20px; border-bottom: 2px solid #ffd700; }  
        .balance-card { background: linear-gradient(135deg, #ffd700, #b8860b); color: black; margin: 20px auto; padding: 20px; border-radius: 15px; width: 85%; }  
        .btn-grid { display: flex; justify-content: space-around; padding: 20px; }  
        .btn { padding: 20px 40px; border-radius: 10px; border: none; font-weight: bold; font-size: 20px; color: white; cursor: pointer; }  
        .big { background: #2ecc71; }  
        .small { background: #ff4d4d; }  
    </style>  
</head>  
<body>  
    <div class="header"><h3>👑 VIP DASHBOARD</h3></div>  
    <div class="balance-card">  
        <p>Total Balance</p>  
        <h1 id="balance">₹500.00</h1>  
    </div>  
    <div style="background:#1e1e1e; padding: 20px; margin: 10px; border-radius: 10px;">  
        <p style="color:#aaa">NEXT PREDICTION</p>  
        <h2 style="color:#ffd700; font-size: 40px;">BIG</h2>  
    </div>  
    <div class="btn-grid">  
        <button class="btn big" onclick="alert('Bet Placed on BIG!')">BIG</button>  
        <button class="btn small" onclick="alert('Bet Placed on SMALL!')">SMALL</button>  
    </div>  
</body>  
</html>  
"""  
  
@app.route('/')  
def index():  
    return render_template_string(LOGIN_HTML)  
  
@app.route('/login', methods=['POST'])  
def login():  
    # Abhi ke liye koi bhi phone/pin chal jayega  
    return render_template_string(GAME_HTML)  
  
if __name__ == '__main__':  
    import os  
    port = int(os.environ.get('PORT', 8080))  
    app.run(host='0.0.0.0', port=port)
