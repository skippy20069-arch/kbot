from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/quote", methods=["GET", "POST"])
def quote():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        details = request.form.get("details")
        
        # Basic validation
        if not name or not email or not details:
            flash("All fields are required!", "error")
            return redirect(url_for("quote"))
        
        # Here you would typically send an email or save to database
        # For now, we'll just show a success message
        flash(f"Thank you {name}! We've received your quote request and will contact you at {email} soon.", "success")
        return redirect(url_for("home"))
    
    return render_template("quote.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
