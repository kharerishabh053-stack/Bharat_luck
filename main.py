from flask import Flask, render_template_string, session, request, redirect, url_for  
import random  
import os  
  
app = Flask(__name__)  
app.secret_key = "BHARATLUCK_GLOBAL_LAUNCH"  
  
# CONFIG  
MY_UPI = "6268358539@fam"  
  
@app.route('/')  
def index():  
    # SEO Friendly Head with Meta Tags  
    return render_template_string(f"""  
    <head>  
        <title>BharatLuck | India's #1 AI Jackpot</title>  
        <meta name="description" content="Play BharatLuck - The most secure AI-powered Lucky Draw and Jackpot game.">  
        <meta name="keywords" content="BharatLuck, Lucky Draw, Online Jackpot India, Earn Money">  
    </head>  
    <body style="background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding-top:80px;">  
        <div style="border:2px solid #ffd700;display:inline-block;padding:30px;border-radius:20px;background:#111;box-shadow:0 0 20px #ffd70033;">  
            <h1 style="letter-spacing:2px;">👑 BHARATLUCK VIP</h1>  
            <p style="color:#888;">Global Testing Phase (Alpha)</p>  
            <form action="/login" method="POST">  
                <input type="text" name="name" placeholder="Tester Name" required style="width:90%;padding:12px;margin:10px 0;background:#222;border:1px solid #ffd700;color:white;border-radius:8px;">  
                <input type="number" name="phone" placeholder="Mobile Number" required style="width:90%;padding:12px;margin:10px 0;background:#222;border:1px solid #ffd700;color:white;border-radius:8px;">  
                <button type="submit" style="width:95%;padding:15px;background:#ffd700;color:black;font-weight:bold;border:none;border-radius:8px;cursor:pointer;">ENTER ENGINE</button>  
            </form>  
        </div>  
    </body>  
    """)  
  
@app.route('/login', methods=['POST'])  
def login():  
    session['user'] = request.form.get('name')  
    return redirect(url_for('game'))  
  
@app.route('/game')  
def game():  
    if 'user' not in session: return redirect(url_for('index'))  
    n1, n2, n3 = random.randint(0,9), random.randint(0,9), random.randint(0,9)  
    return render_template_string(f"""  
    <body style="background:#050505;color:white;text-align:center;font-family:sans-serif;">  
        <p style="color:#ffd700;margin-top:10px;">🛡️ Alpha Tester: {session['user']}</p>  
          
        <div style="display:flex;justify-content:center;gap:15px;margin:30px 0;">  
            <div id="s1" style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;color:#fff;">{n1}</div>  
            <div id="s2" style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;color:#fff;">{n2}</div>  
            <div id="s3" style="background:#111;border:2px solid #ffd700;font-size:70px;width:70px;border-radius:15px;color:#fff;">{n3}</div>  
        </div>  
  
        <div style="background:#111;margin:15px;padding:20px;border-radius:20px;border:1px solid #333;">  
            <p>Select Number: <span id="target" style="color:#ffd700;font-weight:bold;">---</span></p>  
            <div style="display:grid;grid-template-columns: repeat(3, 1fr);gap:10px;">  
                <button onclick="sel('777')" style="padding:10px;background:#222;color:white;border:1px solid #444;">777</button>  
                <button onclick="sel('999')" style="padding:10px;background:#222;color:white;border:1px solid #444;">999</button>  
                <button onclick="sel('000')" style="padding:10px;background:#222;color:white;border:1px solid #444;">000</button>  
            </div>  
            <br>  
            <button onclick="pay()" style="background:#ffd700;color:black;padding:18px;width:100%;border:none;border-radius:12px;font-weight:bold;font-size:18px;">BET ₹50</button>  
            <p style="font-size:10px;margin-top:10px;color:#888;">*Testers use 'Manual Verify' after bet</p>  
        </div>  
  
        <script>  
            let selected = "";  
            function sel(val) {{ selected = val; document.getElementById('target').innerText = val; }}  
            function pay() {{  
                if(!selected) {{ alert("Chose Number!"); return; }}  
                // UPI Link  
                window.location.href = "upi://pay?pa={MY_UPI}&pn=BharatLuck&am=50&cu=INR&tn=Alpha_Test_"+selected;  
            }}  
        </script>  
        <p style="color:#0f0;font-size:10px;">© BHARATLUCK GHOST ENGINE v3.1</p>  
    </body>  
    """)  
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
