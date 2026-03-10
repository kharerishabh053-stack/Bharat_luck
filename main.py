from flask import Flask, render_template_string, request, session  
import random  
import os  
  
app = Flask(__name__)  
app.secret_key = "BHARAT_LUCK_GHOST_KEY_777" # Security Key  
  
# --- AI CA & ENGINE LOGIC ---  
def get_game_result(bet_amount):  
    num = random.randint(0, 9)  
    res = "BIG" if num >= 5 else "SMALL"  
    # GST Calculation (28%)  
    gst = round(bet_amount * 0.28, 2)  
    play_amt = bet_amount - gst  
    return num, res, gst, play_amt  
  
@app.route('/')  
def login_page():  
    return """  
    <body style="background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding-top:100px;-webkit-user-select:none;">  
        <div style="border:2px solid #ffd700;display:inline-block;padding:40px;border-radius:20px;background:#111;box-shadow:0 0 20px #ffd70033;">  
            <h1 style="letter-spacing:2px;">👑 BHARATLUCK VIP</h1>  
            <p style="color:#888;">AI Ghost Engine v1.0 | Secured</p>  
            <input type="text" placeholder="Mobile Number" style="width:90%;padding:12px;margin:15px 0;background:#222;border:1px solid #ffd700;color:white;border-radius:8px;">  
            <button onclick="window.location.href='/machine'" style="width:95%;padding:15px;background:#ffd700;color:black;font-weight:bold;border:none;border-radius:8px;cursor:pointer;font-size:16px;">ENTER SECURE ZONE</button>  
            <p style="font-size:10px;margin-top:20px;color:#444;">© MSME Registered Gaming Consultancy</p>  
        </div>  
    </body>  
    """  
  
@app.route('/machine')  
def machine():  
    # Dummy data for the AI Machine  
    num, res, gst, play_amt = get_game_result(50) # Default view for ₹50 bet  
    return f"""  
    <head>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <style>  
            body {{ background:#050505;color:white;text-align:center;font-family:sans-serif;-webkit-user-select:none; }}  
            .card {{ background:#111;border:1px solid #333;margin:15px;padding:20px;border-radius:20px; }}  
            .num-box {{ font-size:80px;color:#ffd700;text-shadow:0 0 15px #ffd700;margin:20px 0; }}  
            .gst-tag {{ font-size:10px;background:#222;padding:5px;border-radius:5px;color:#0f0; }}  
            .btn-tier {{ padding:10px;width:30%;margin:5px;background:none;border:1px solid #ffd700;color:#ffd700;border-radius:5px;font-size:11px; }}  
            @media print {{ body {{ display:none; }} }} /* Anti-Screenshot Hack */  
        </style>  
    </head>  
    <body oncontextmenu="return false;">  
        <div class="card">  
            <h2 style="color:#ffd700;margin:0;">🎰 GHOST ENGINE</h2>  
            <p style="font-size:12px;color:#888;">Session ID: {random.randint(10000,99999)}</p>  
            <div class="num-box">{num}</div>  
            <div style="font-size:24px;font-weight:bold;margin-bottom:15px;">{res}</div>  
            <div class="gst-tag">✓ 28% GST PAID TO GOVT (₹{gst})</div>  
            <hr style="border:0.1px solid #222;margin:20px 0;">  
            <p style="font-size:12px;color:#ffd700;">SELECT ACTIVE TIER</p>  
            <button class="btn-tier">₹50 (Min)</button>  
            <button class="btn-tier">₹500 (Mid)</button>  
            <button class="btn-tier">₹5000 (VIP)</button>  
        </div>  
        <div style="font-size:10px;color:#333;">Anti-Screenshot Protection: ACTIVE</div>  
    </body>  
    """  
  
# --- SECRET ADMIN AI CA (Only for You) ---  
@app.route('/ai_ca_dashboard_777')  
def admin_ca():  
    return """  
    <body style="background:#000;color:#0f0;font-family:monospace;padding:20px;">  
        <h2>📊 BHARATLUCK AI CA REPORT</h2>  
        <hr border="1" color="#0f0">  
        <p>[+] Status: Operational</p>  
        <p>[+] Total Virtual GST Vault: ₹XX,XXX (Saved for Future)</p>  
        <p>[+] Net Clean Profit: ₹XX,XXX</p>  
        <p>[+] Loss Protection: ₹10 Auto-Refund Active</p>  
        <p>[+] Active Users: 0 (Live Tracking...)</p>  
        <button onclick="alert('Syncing with UPI...')">SYNC WITH BANK</button>  
    </body>  
    """  
  
if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 8080))  
    app.run(host='0.0.0.0', port=port)
