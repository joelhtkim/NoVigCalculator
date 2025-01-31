from flask import Flask, request, render_template

from functions import impliedProbability, probabilityToAmerican, novig

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    odds_a = request.form.get('odds_a', '')
    odds_b = request.form.get('odds_b', '')

    if request.method == 'POST':

        try:
            if not odds_a or not odds_b:
                raise ValueError("Both odds fields are required.")

            odds_a = float(odds_a)
            odds_b = float(odds_b)

            impliedProb1,impliedProb2,fairProb1,fairProb2,fairOdds1,fairOdds2 = novig(odds_a, odds_b)

            fairAmerican1 = probabilityToAmerican(fairProb1)
            fairAmerican2 = probabilityToAmerican(fairProb2)

            result = {
                'impliedProb1': impliedProb1,
                'impliedProb2': impliedProb2,
                'fairProb1': fairProb1,
                'fairProb2': fairProb2,
                'fairAmerican1': fairAmerican1,
                'fairAmerican2': fairAmerican2
            }

        except ValueError as e:
            result = {'error': f"Error: {str(e)}"}
        except Exception as e:
            result = {'error': f"Unexpected error: {str(e)}"}

    return render_template('index.html', result=result, odds_a=odds_a, odds_b=odds_b)

if __name__ == '__main__':
    app.run(debug=True)
