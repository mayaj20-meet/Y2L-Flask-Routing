from flask import Flask, request, redirect, render_template
from flask import session as login_session
app= Flask ("Gucci")
@app.route("/")
def return_home():
	return render_template("home.html")
if __name__ == '__main__':
	app.run(debug=True)