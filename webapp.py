from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/Map")
def render_page1():
    return render_template('Map.html')

@app.route("/activities")
def render_page2():
    return render_template('activities.html')

@app.route("/Ticket-and-Prices")
def render_page3():
    return render_template('Ticket-and-Prices.html')

@app.route("/store")
def render_page4():
    return render_template('store.html')

@app.route("/Resturant1")
def render_page5():
    return render_template('Resturant1.html')

@app.route("/resturant2")
def render_page6():
    return render_template('resturant2.html')

@app.route("/locations")
def render_page7():
    return render_template('locations.html')

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
