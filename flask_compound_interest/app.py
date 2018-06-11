from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    result = None
    if request.method == 'POST':
        # Get the result of the compound interest function
        pass
    # Pass the result to the front end
    return render_template('form.html')


#
# Write a compound interest function.
#

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
