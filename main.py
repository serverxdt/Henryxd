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
    <title>(HENRY-X) 2.0</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #9932CC, #FF00FF);
            color: #fff;
        }

        nav {
            background-color: #000;
            color: #ffcc00;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            position: relative;
        }

        nav .logo {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
        }

        nav .menu-icon {
            display: flex;
            flex-direction: column;
            cursor: pointer;
            align-items: center;
        }

        nav .menu-icon div {
            width: 30px;
            height: 4px;
            background-color: #ffcc00;
            margin: 4px 0;
            transition: all .3s ease;
        }

        nav .menu-icon:hover div {
            background-color: #fff;
        }

        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
        }

        nav ul li {
            margin-left: 25px;
        }

        nav ul li a {
            color: #ffcc00;
            text-decoration: none;
            font-size: 18px;
            font-weight: 500;
            transition: color .3s ease;
        }

        nav ul li a:hover {
            color: #fff;
        }

        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 30px;
            background: linear-gradient(to right, #9932CC, #FF00FF);
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(255, 204, 0, 0.3);
        }

        h1 {
            text-align: center;
            color: #e0e0e0;
            font-size: 100px;
        }

        .service-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .service-item {
            flex: 1;
            margin: 50px;
            padding: 30px;
            background: linear-gradient(to right, #9932CC, #FF00FF);
            text-align: center;
            border: 2px solid #000000;
            border-radius: 10px;
            transition: transform .3s ease, box-shadow .3s ease;
            cursor: pointer;
            color: #ffcc00;
        }

        .service-item h2 {
            color: #ffcc00;
        }

        .service-item p {
            color: #e0e0e0;
        }

        .service-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 25px 50px rgba(255, 204, 0, 0.5);
        }

        footer {
            background-color: #000;
            color: #ffcc00;
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.2);
        }

        footer p {
            margin: 0;
            font-size: 14px;
        }

        @media (max-width: 768px) {
            nav ul {
                display: none;
                flex-direction: column;
                position: absolute;
                background-color: #000;
                top: 60px;
                left: 0;
                width: 100%;
                text-align: left;
            }

            nav ul.active {
                display: flex;
            }

            nav ul li {
                margin: 0;
                padding: 15px 20px;
            }

            nav ul li a {
                display: block;
            }

            .service-section {
                flex-direction: column;
            }

            .service-item {
                margin: 10px 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Dwonload App</h1>
        <section class="service-section">
            <img src="" style="width: 100%; height: auto; border-radius: 12px;">
            <div class="service-item" onclick="window.location.href='https://my-app-production-50e3.up.railway.app/'">
                <img src="https://i.imgur.com/iJ8mZjV.jpeg" style="width: 800px; height: 1000; border-radius: 12px;">
                <h1>(HENRYX) 2.0</h1>
                <p> This App Create By Henry God Abuser And Haters Fucked By Henry. </p>
            </div>
        </section>
    </div>

    </footer>

    <script>
        function toggleMenu() {
            var menu = document.getElementById("nav-menu");
            menu.classList.toggle("active");
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
  
