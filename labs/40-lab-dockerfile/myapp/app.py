from flask import Flask
app = Flask(__name__)

@app.route('/')
#def hello():
#	return "This is a sfeir school about Docker !"

def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sfeir School Meme</title>
        <style>
            body { 
                font-family: 'Arial', sans-serif; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                flex-direction: column;
            }
            img { 
                max-width: 80%; 
                border-radius: 10px; 
                box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
            }
            .caption {
                margin-top: 20px;
                font-size: 20px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <img src="https://example.com/your-meme-image.jpg" alt="Sfeir School Meme">
        <div class="caption">This is Sfeir School... but with memes!</div>
    </body>
    </html>
    """
    return html_content


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9090)