from myapp import app

if __name__ == '__main__':
    app.debug = True
#    app.run()
    app.run(host='0.0.0.0', port=5000)
