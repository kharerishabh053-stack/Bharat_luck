from flask import Flask, render_template_string, request, session, redirect, url_for  
import random  
import os  
  
app = Flask(__name__)  
app.secret_key = "BHARATLUCK_ULTIMATE_SECRET"  
  
# --- CONFIGURATION ---  
MY_UPI_ID = "6268358539@fam"  
  
@app.route('/')  
def login():  
    # Pehle Account Banane ka Page  
    return render_template_string("""  
    <body style="background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding-top:100px;">  
        <div style="border:2px solid #ffd700;display:inline-block;padding:30px;border-radius:20px;background:#111;">  
            <h1>👑 BHARATLUCK VIP</h1>  
            <p>Create Your Player Account</p>  
            <form action="/set_user" method="POST">  
                <input type="text" name="username" placeholder="Full Name" required style="width:90%;padding:10px;margin:10px;background:#222;border:1px solid #ffd700;color:white;"><br>  
                <input type="number" name="phone" placeholder="Mobile Number" required style="width:90%;padding:10px;margin:10px;background:#222;border:1px solid #ffd700;color:white;"><br>  
                <button type="submit" style="width:95%;padding:15px;background:#ffd700;font-weight:bold;border:none;border-radius:10px;cursor:pointer;">CREATE ACCOUNT</button>  
            </form>  
        </div>  
    </body>  
    """)  
  
@app.route('/set_user', methods=['POST'])  
def set_user():  
    session['user'] = request.form.get('username')  
    return redirect(url_for('game_table'))  
  
@app.route('/game_table')  
def game_table():  
    if 'user' not in session: return redirect(url_for('login'))  
      
    # Lucky Triple Number Result  
    n1, n2, n3 = random.randint(0,9), random.randint(0,9), random.randint(0,9)  
      
    return render_template_string(f"""  
    <!DOCTYPE html>  
    <html>  
    <head>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <style>  
            body {{ background:#050505;color:#fff;text-align:center;font-family:sans-serif; }}  
            .slot-container {{ display:flex;justify-content:center;gap:10px;margin:20px 0; }}  
            .slot {{ background:#222;border:3px solid #ffd700;font-size:80px;width:80px;border-radius:10px;text-shadow:0 0 15px #ffd700; }}  
            .bet-table {{ display:grid;grid-template-columns: repeat(5, 1fr);gap:5px;margin:20px;padding:10px;background:#111;border-radius:10px; }}  
            .num-btn {{ padding:10px;background:#333;border:1px solid #555;color:white;cursor:pointer;border-radius:5px; }}  
            .num-btn.active {{ background:#ffd700;color:black;font-weight:bold; }}  
            .confirm-btn {{ width:90%;padding:20px;background:#ffd700;color:black;border:none;border-radius:15px;font-weight:bold;font-size:18px; }}  
        </style>  
    </head>  
    <body>  
        <p style="color:#ffd700;">Welcome, {session['user']} 👑</p>  
          
        <div class="slot-container">  
            <div class="slot">{n1}</div>  
            <div class="slot">{n2}</div>  
            <div class="slot">{n3}</div>  
        </div>  
  
        <h3>STEP 1: SELECT YOUR LUCKY NUMBER</h3>  
        <div class="bet-table">  
            <button class="num-btn" onclick="selectNum('777')">777</button>  
            <button class="num-btn" onclick="selectNum('999')">999</button>  
            <button class="num-btn" onclick="selectNum('000')">000</button>  
            <button class="num-btn" onclick="selectNum('123')">123</button>  
            <button class="num-btn" onclick="selectNum('555')">555</button>  
        </div>  
  
        <h3>STEP 2: PLACE YOUR BET</h3>  
        <button class="confirm-btn" onclick="pay()">BET ₹50 ON NUMBER <span id="sel_num">---</span></button>  
  
        <script>  
            let selected = "";  
            function selectNum(n) {{  
                selected = n;  
                document.getElementById('sel_num').innerText = n;  
                // Highlight logic can be added here  
            }}  
            function pay() {{  
                if(selected == "") {{ alert("Pehle number select karo bhai!"); return; }}  
                window.location.href = "upi://pay?pa={MY_UPI_ID}&pn=BharatLuck&am=50&cu=INR&tn=Bet_on_"+selected;  
            }}  
        </script>  
          
        <div style="color:#0f0;font-size:12px;margin-top:20px;border:1px dashed #0f0;padding:10px;">  
            AI CA: "Bhai, agar {n1}{n2}{n3} match nahi hua toh ₹5 refund pakka!"  
        </div>  
    </body>  
    </html>  
    """)  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
