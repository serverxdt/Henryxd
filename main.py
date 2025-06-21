from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Henry Server</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Popins, sans-serif;
            background-color: cream;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: white;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #fff;
            font-size: 20px;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #000;
        }

        /* Blinking Sukhi Server heading */
        .sukhi-server {
            font-size: 32px;
            color: #ff5e5e;
            animation: blink 1.5s infinite;
            font-weight: bold;
            margin-bottom: 20px;
        }

        @keyframes blink {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0;
            }
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            background-color: rgba(255, 255, 255, 0.9);
        }

        form {
        display: flex;
        flex-direction: column; /* Arrange children in a column */
        align-items: center;    /* Center items horizontally */
        }
        
        button {
        width: auto;            /* Change to auto for centered width */
        padding: 12px 20px;     /* Adjust padding for better appearance */
        background-color: #007bff;
        color: #fff;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        margin-top: 15px;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        .admin-contact {
            margin-top: 20px;
            color: #fff;
        }

        .admin-contact a {
            color: #00ff00;
            font-weight: bold;
            text-decoration: none;
        }

        .error-message {
            color: red;
            font-size: 14px;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
    </nav>
    </header>
    <br />
    <h2>𝗚𝗘𝗧 𝗙𝗥𝗘𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 ➤ 𝙃𝙚𝙣𝙧𝙮 𝙓 𝙎𝙖𝙢𝙖𝙧</h2>
    <br />
    
               <div class="content">
        <body>
  <video class="video" autoplay loop muted>
    <source src="https://giphy.com/gifs/y1Qs82E2FmlAPvkBir.mp4" type="video/mp4">
  </video>
  </body>
 <h1>╰┈➤ 🩷 𝗙𝗿𝗲𝗲 𝗦𝗲𝗿𝘃𝗲𝗿 𝗔𝗽𝗽 𝗕𝘆 𝗛𝗲𝗻𝗿𝘆 𝗫 𝗦𝗮𝗺𝗮𝗿 ᯓ★</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://www.mediafire.com/file/dotpunuezc9ji5p/HENRY+X+SAMAR+APK+.apk/file'">⊲ DOWNLOAD ⊳</button>
    <br />
    <br />

    <div class="footer">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <a href="/terms" class="hover:text-primary">Terms</a>
        <span class="mx-2">|</span>
        <a href="/privacy" class="hover:text-primary">Privacy</a>
      </div>
      
      <div id="links" class="flex space-x-4">
        <a href="https://www.facebook.com/henry.inxide" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
        <a href="https://wa.me/+919235741670" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
        <a href="https://github.com/Henryinxid3/" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
      </div>
      
      <div class="mt-4 md:mt-0 text-center">
        <p>© 2024 Henry Dwn. All Rights Reserved.</p>
        <p>Made with ❤️ by <a href="">HENRY INXIDE</a></p>
      </div>
        <br />
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
