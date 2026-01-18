from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for notes
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")

        # Prevent empty notes
        if note:
            notes.append(note)

        # Redirect to avoid form resubmission on refresh
        return redirect(url_for("index"))

    return render_template("home.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)