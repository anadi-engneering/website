from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def home():
=======
def index():
    # The function render_template looks for a file named index.html in the 'templates' folder
>>>>>>> f49e822 (Ready website)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
