from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Varun Sahu - DevOps Enthusiast</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
            }
            .container {
                text-align: center;
                background: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .social-links a {
                margin: 0 10px;
                text-decoration: none;
                color: #333;
                font-size: 1.5rem;
            }
            .social-links a:hover {
                color: #0077b5;
            }
            .github-icon, .linkedin-icon {
                width: 24px;
                height: 24px;
                vertical-align: middle;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, I'm Varun Sahu</h1>
            <p>DevOps Enthusiast | Content Creator</p>
            <div class="social-links">
                <a href="https://github.com/vaarunnsahu" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" class="github-icon">
                    GitHub
                </a>
                <a href="https://www.linkedin.com/in/vaarunsahu/" target="_blank">
                    <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn" class="linkedin-icon">
                    LinkedIn
                </a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
