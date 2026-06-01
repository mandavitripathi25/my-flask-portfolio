from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dynamic Data for the template
    profile_data = {
        "name": "Mandavi Tripathi",
        "title": "Data Scientist & Analytics Specialist",
        "about": "Hi, I'm Mandavi. I turn complex, chaotic data into actionable insights and predictive models. With a strong foundation in statistics, machine learning, and data storytelling, I love building data-driven solutions that solve real-world problems.",
        "github": "https://github.com/your-username",      # Replace with your GitHub link
        "linkedin": "https://linkedin.com/in/your-username", # Replace with your LinkedIn link
        "email": "mandavi.tripathi@email.com",              # Replace with your Email
        "location": "India",
        "projects": [
            {
                "title": "Predictive Customer Churn Model",
                "desc": "Built an end-to-end ML pipeline using XGBoost to predict customer churn with 92% accuracy.",
                "tech": "Python, Scikit-Learn, XGBoost"
            },
            {
                "title": "Automated Financial Dashboard",
                "desc": "Created an interactive Tableau/PowerBI dashboard tracking real-time company KPIs and financial health.",
                "tech": "SQL, Tableau, Python"
            },
            {
                "title": "NLP Sentiment Analyzer",
                "desc": "Developed a deep learning model using Transformers to analyze product reviews and sentiment trends.",
                "tech": "PyTorch, HuggingFace, Flask"
            }
        ]
    }
    return render_template('index.html', data=profile_data)

if __name__ == '__main__':
    app.run(debug=True)