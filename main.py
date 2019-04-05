from flask import flask

app = Flask(__name__)
app.config['DEBUG']


form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>

       <form action="/form" method="POST">
        
        <label> Rotate by:  
            <input type="text" name="rot" value="0" />
        </label>
        <br />
        <textarea type="text">

        </textarea>
        <br />
        <input type="submit" value="Submit Query" />
      </form>


      
      <!-- create your form here -->
    </body>
</html>

"""
@app.route("/")
def index():
    return form

app.run()