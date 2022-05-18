from main import app

if __name__ == '__main__':

    #app.run(debug=True if os.getenv('FLASK_ENV') == 'development' else False)
    # app.run(host="192.168.137.1", port=8080)
    app.run(host="0.0.0.0", debug=True)
    #app.run(host="0.0.0.0", debug=True)
