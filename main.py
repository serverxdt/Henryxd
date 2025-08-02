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
  <meta charset="UTF-8" />
  <title>Convo Results</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;700&display=swap" rel="stylesheet" />
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet" />
  <style>
    body {
      margin: 0;
      background: linear-gradient(to right, #9932CC, #FF00FF);
      font-family: 'Be Vietnam Pro', sans-serif;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 40px 20px;
    }

    h1 {
      margin-bottom: 30px;
      font-size: 2rem;
      color: white;
      text-shadow: 0 0 10px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      width: 100%;
      max-width: 900px;
    }

    .card {
      background: #3D3C3A;
      border-radius: 15px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      box-shadow: 0 0 10px rgba(0,255,255,0.1);
      position: relative;
    }

    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 20px rgba(0,255,255,0.3);
    }

    .card img {
      width: 100%;
      height: 470px;
      object-fit: cover;
    }

    .card-title {
      padding: 15px;
      font-size: 1.2rem;
      font-weight: 600;
      text-align: center;
      color: linear-gradient(to right, #9932CC, #FF00FF);
      text-shadow: 0 0 5px;
    }

    .click-icon {
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(0, 255, 255, 0.1);
      border: 1px solid #3D3C3A;
      color: #0ff;
      font-size: 1rem;
      padding: 5px 7px;
      border-radius: 6px;
      text-shadow: 0 0 5px;
      animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
      0% { box-shadow: 0 0 5px #0ff; }
      50% { box-shadow: 0 0 15px #0ff; }
      100% { box-shadow: 0 0 5px #0ff; }
    }

    .social-icons {
      margin-top: 40px;
      display: flex;
      gap: 20px;
    }

    .social-icons a {
      color: #0ff;
      font-size: 24px;
      transition: transform 0.3s ease;
      text-shadow: 0 0 5px #0ff;
    }

    .social-icons a:hover {
      transform: scale(1.3);
      color: #5ff;
    }
  </style>
</head>
<body>
  <h1>Download App</h1>
  <div class="cards">
    <div class="card" onclick="window.open('https://evil-fay-zohan-21e195f3.koyeb.app/', '_blank')">
      <div class="click-icon"><i class="fas fa-user-secret"></i></div>
      <img src="https://i.imgur.com/tUVveK5.jpeg" alt="HENRY-X">
      <div class="card-title">(HENRY-X) 2.0</div>
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
  
