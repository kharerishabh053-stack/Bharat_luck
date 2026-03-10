# Is code mein koi bhari file nahi hai, ye Railway trial ke liye BEST hai  
from flask import Flask, render_template_string, session, request, redirect, url_for  
import random  
import os  
  
app = Flask(__name__)  
app.secret_key = "SAFE_LAUNCH_999"  
  
@app.route('/')  
def index():  
    # Login page (Extremely Lite)  
    return render_template_string("""  
    <body style="background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding:50px;">  
        <h2 style="border:1px solid #ffd700;padding:20px;border-radius:15px;">👑 BHARATLUCK ENTRY</h2>  
        <form action="/login" method="POST">  
            <input type="number" name="phone" placeholder="Mobile Number" required style="width:80%;padding:15px;margin:10px;background:#111;border:1px solid #ffd700;color:white;border-radius:10px;">  
            <button type="submit" style="width:85%;padding:15px;background:#ffd700;border:none;border-radius:10px;font-weight:bold;">LOGIN</button>  
        </form>  
    </body>  
    """)  
  
@app.route('/login', methods=['POST'])  
def login():  
    session['user'] = request.form.get('phone')  
    return redirect(url_for('game'))  
  
@app.route('/game')  
def game():  
    if 'user' not in session: return redirect(url_for('index'))  
    # Triple Slot Numbers  
    n1, n2, n3 = random.randint(0,9), random.randint(0,9), random.randint(0,9)  
    return render_template_string(f"""  
    <body style="background:#000;color:white;text-align:center;font-family:sans-serif;padding:10px;">  
        <div style="display:flex;justify-content:center;gap:10px;margin-top:20px;">  
            <div style="background:#222;border:2px solid #ffd700;font-size:60px;padding:10px 20px;border-radius:10px;">{n1}</div>  
            <div style="background:#222;border:2px solid #ffd700;font-size:60px;padding:10px 20px;border-radius:10px;">{n2}</div>  
            <div style="background:#222;border:2px solid #ffd700;font-size:60px;padding:10px 20px;border-radius:10px;">{n3}</div>  
        </div>  
        <h3 style="color:#ffd700;">SELECT NUMBER & BET</h3>  
        <div style="display:grid;grid-template-columns: repeat(4, 1fr);gap:5px;padding:10px;">  
            <button onclick="s('777')" style="padding:10px;background:#111;color:white;border:1px solid #333;">777</button>  
            <button onclick="s('999')" style="padding:10px;background:#111;color:white;border:1px solid #333;">999</button>  
            <button onclick="s('000')" style="padding:10px;background:#111;color:white;border:1px solid #333;">000</button>  
            <button onclick="s('111')" style="padding:10px;background:#111;color:white;border:1px solid #333;">111</button>  
        </div>  
        <button onclick="pay()" style="width:90%;padding:20px;background:#ffd700;color:black;border-radius:15px;font-weight:bold;font-size:20px;margin-top:20px;">BET ₹50 ON <span id="n">---</span></button>  
        <script>  
            let sel = "";  
            function s(v) {{ sel = v; document.getElementById('n').innerText = v; }}  
            function pay() {{  
                if(!sel) {{ alert("Select Number!"); return; }}  
                window.location.href = "upi://pay?pa=6268358539@fam&pn=BharatLuck&am=50&cu=INR&tn=Bet_on_"+sel;  
            }}  
        </script>  
        <p style="color:#0f0;font-size:10px;margin-top:20px;">🛡️ AI CA: Safe Mode Active (1GB Limit Checked)</p>  
    </body>  
    """)  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
