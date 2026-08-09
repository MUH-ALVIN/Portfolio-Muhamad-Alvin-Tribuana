from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/project-listrik")
def project_listrik():
    return render_template("project_listrik.html")

@app.route("/project/notes")
def project_notes():
    return render_template("Project_Note.html")


@app.route("/project/todo")
def project_todo():
    return render_template("Project_Todo List.html")

@app.route("/Project_Landing Page")
def landing():
    return render_template("Project_Landing Page.html")

if __name__ == "__main__":
    app.run(debug=True)