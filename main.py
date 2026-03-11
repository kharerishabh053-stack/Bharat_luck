from flask import Flask, render_template_string, session, request, redirect, url_for  
import random  
  
app = Flask(__name__)  
app.secret_key = "TESTER_FREE_MODE_777"  
  
@app.route('/')  
def index():  
    return render_template_string("""  
    <body style="background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding-top:80px;">  
        <div style="border:2px solid #ffd700;display:inline-block;padding:30px;border-radius:20px;background:#111;">  
            <h1>👑 BHARATLUCK (BETA)</h1>  
            <p style="color:#0f0;">FREE TESTER ACCESS ACTIVE</p>  
            <form action="/login" method="POST">  
                <input type="text" name="name" placeholder="Tester Name" required style="width:90%;padding:12px;margin:10px 0;background:#222;border:1px solid #ffd700;color:white;border-radius:8px;">  
                <button type="submit" style="width:95%;padding:15px;background:#ffd700;font-weight:bold;border:none;border-radius:10px;cursor:pointer;">START TESTING</button>  
            </form>  
        </div>  
    </body>  
    """)  
  
@app.route('/login', methods=['POST'])  
def login():  
    session['user'] = request.form.get('name')  
    session['balance'] = 500  # Sabko ₹500 free testing ke liye  
    return redirect(url_for('game'))  
  
@app.route('/game')  
def game():  
    if 'user' not in session: return redirect(url_for('index'))  
    n1, n2, n3 = random.randint(0,9), random.randint(0,9), random.randint(0,9)  
    return render_template_string(f"""  
    <body style="background:#050505;color:white;text-align:center;font-family:sans-serif;">  
        <div style="background:#222;padding:10px;display:flex;justify-content:space-between;">  
            <span>👤 {session['user']}</span>  
            <span style="color:#ffd700;">💰 Virtual Bal: ₹{session['balance']}</span>  
        </div>  
          
        <div style="display:flex;justify-content:center;gap:15px;margin:40px 0;">  
            <div style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;">{n1}</div>  
            <div style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;">{n2}</div>  
            <div style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;">{n3}</div>  
        </div>  
  
        <div style="background:#111;margin:15px;padding:20px;border-radius:20px;">  
            <p>Select Number: <span id="target" style="color:#ffd700;font-weight:bold;">---</span></p>  
            <button onclick="s('777')" style="padding:10px;background:#333;color:white;margin:5px;">777</button>  
            <button onclick="s('999')" style="padding:10px;background:#333;color:white;margin:5px;">999</button>  
            <button onclick="s('111')" style="padding:10px;background:#333;color:white;margin:5px;">111</button>  
            <br><br>  
            <button onclick="testBet()" style="background:#ffd700;color:black;padding:15px;width:100%;border-radius:10px;font-weight:bold;">PLACE TEST BET (₹50)</button>  
        </div>  
  
        <script>  
            let sel = "";  
            function s(v) {{ sel = v; document.getElementById('target').innerText = v; }}  
            function testBet() {{  
                if(!sel) {{ alert("Chose Number!"); return; }}  
                alert("TEST SUCCESS: Bet placed on " + sel + "\\n(No real money deducted in Beta)");  
                location.reload(); // Refresh to show new numbers  
            }}  
        </script>  
        <p style="color:#888;font-size:10px;">BETA MODE: Real Transactions are Disabled</p>  
    </body>  
    """)  
  
if __name__ == '__main__':  
    import os  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
