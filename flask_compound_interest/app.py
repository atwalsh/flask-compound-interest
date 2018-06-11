from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    result = None
    if request.method == 'POST':
        result = calculate_compound_interest(
            p=int(request.form['principal']),
            i=float(request.form['interest']),
            t=int(request.form['times_per_year']),
            n=int(request.form['years'])
        )
    # Pass the result to the front end
    return render_template('form.html', result=result)


def calculate_compound_interest(p: int, i: float, t: int, n: int):
    """
    Calculate compound interest.

    :param p: The principal investment amount.
    :param i: The annual interest rate (decimal form).
    :param t: Number of years the money is invested for.
    :param n: Number of times that interest is compounded per year.
    :return: The future value of the investment.
    """
    return p * ((1 + ((i / 100) / t)) ** (n * t))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
