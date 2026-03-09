from flask import Flask, render_template_string  
import random  
import time  
  
app = Flask(__name__)  
  
# --- SINGLE MACHINE ENGINE ---  
@app.route('/')  
def machine_game():  
    # Machine logic: Random number 0-9  
    num = random.randint(0, 9)  
    # 0-4 Small, 5-9 Big  
    result = "BIG" if num >= 5 else "SMALL"  
    color = "#2ecc71" if result == "BIG" else "#ff4d4d"  
  
    html_code = f"""  
    <!DOCTYPE html>  
    <html>  
    <head>  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <title>BHARATLUCK MACHINE</title>  
        <style>  
            body {{ background: #0a0a0a; color: white; font-family: 'Courier New', monospace; text-align: center; margin: 0; }}  
            .machine-body {{ border: 4px solid #ffd700; margin: 20px auto; width: 90%; max-width: 400px; border-radius: 20px; padding: 20px; background: #1a1a1a; box-shadow: 0 0 30px #ffd70055; }}  
            .screen {{ background: #000; border: 2px inset #444; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}  
            .number {{ font-size: 80px; color: #ffd700; text-shadow: 0 0 15px #ffd700; }}  
            .prediction {{ font-size: 30px; color: {color}; font-weight: bold; border-top: 1px solid #333; padding-top: 10px; }}  
            .timer {{ color: #00ff00; font-size: 18px; margin-top: 10px; }}  
            .btn {{ background: #ffd700; color: black; padding: 15px 30px; border: none; border-radius: 50px; font-weight: bold; cursor: pointer; font-size: 18px; box-shadow: 0 5px #b8860b; }}  
            .btn:active {{ transform: translateY(3px); box-shadow: none; }}  
        </style>  
    </head>  
    <body>  
        <h2 style="color:#ffd700; margin-top:30px;">👑 BHARATLUCK AI MACHINE</h2>  
        <div class="machine-body">  
            <div class="screen">  
                <div class="timer" id="timer">NEXT DRAW IN: 15s</div>  
                <div class="number" id="num">{num}</div>  
                <div class="prediction">{result}</div>  
            </div>  
            <p style="color:#888;">Wallet Balance: <span style="color:#fff;">₹500.00</span></p>  
            <button class="btn" onclick="location.reload()">SPIN MACHINE</button>  
        </div>  
        <p style="font-size:12px; color:#444; margin-top:20px;">Powered by BharatLuck AI Engine v1.0</p>  
          
        <script>  
            // Chota sa timer script  
            let timeLeft = 15;  
            setInterval(() => {{  
                if(timeLeft > 0) {{  
                    timeLeft--;  
                    document.getElementById('timer').innerHTML = "NEXT DRAW IN: " + timeLeft + "s";  
                }} else {{  
                    location.reload(); // Time khatam hote hi machine apne aap ghumegi  
                }}  
            }}, 1000);  
        </script>  
    </body>  
    </html>  
    """  
    return render_template_string(html_code)  
  
if __name__ == '__main__':  
    import os  
    port = int(os.environ.get('PORT', 8080))  
    app.run(host='0.0.0.0', port=port)
