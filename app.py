from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', title='Akhil Sodari - Portfolio', contact_info='asodari@stevens.edu',about="This is Akhil Sodari")

@app.route('/test')
def test():
    # Add your education details here
    return render_template('blog.html')

@app.route('/education')
def education():
    # Add your education details here
    return render_template('education.html')

@app.route('/skills')
def skills():
    # Add your skills details here
    return render_template('skills.html')

@app.route('/work_experience')
def work_experience():
    # Add your work experience details here
    return render_template('work_experience.html')


@app.route('/virtual_mouse')
def projects():
    # Add your project details here
    return render_template('virtual_mouse.html')


@app.route('/facial_attendance')
def facial_attendance():
    # Add your project details here
    return render_template('facial_attendance.html')

@app.route('/LLM_Fico')
def LLM_Fico():
    # Add your project details here
    return render_template('LLM_FICO.html')

if __name__ == '__main__':
    app.run(debug=True)
