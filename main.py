from flask import Flask, render_template_string  
  
app = Flask(__name__)  
  
@app.route('/')  
def home():  
    html_code = """  
    <!DOCTYPE html>  
    <html lang="en">  
    <head>  
        <meta charset="UTF-8">  
        <meta name="viewport" content="width=device-width, initial-scale=1.0">  
        <title>BHARATLUCK VIP</title>  
        <style>  
            body { background-color: #1a1a1a; color: white; font-family: Arial, sans-serif; text-align: center; padding: 50px; }  
            .card { background: linear-gradient(135deg, #ffd700, #b8860b); color: black; padding: 20px; border-radius: 15px; display: inline-block; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }  
            h1 { margin: 0; font-size: 24px; }  
            .balance { font-size: 40px; font-weight: bold; margin: 20px 0; }  
        </style>  
    </head>  
    <body>  
        <div class="card">  
            <h1>👑 BHARATLUCK VIP</h1>  
            <p>Welcome, Player!</p>  
            <div class="balance">₹500.00</div>  
            <p>Status: Active</p>  
        </div>  
    </body>  
    </html>  
    """  
    return render_template_string(html_code)  
  
if __name__ == '__main__':  
    import os  
    # Railway ke liye ye line sabse zaruri hai  
    port = int(os.environ.get('PORT', 8080))  
    app.run(host='0.0.0.0', port=port)
