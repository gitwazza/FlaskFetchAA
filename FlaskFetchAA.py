from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def t2():
    return render_template('t2.html')

# This function receives and returns data. This example tries to keep the code simple.
# However, it would be possible to modify this to achieve a range of other functions.
# For example the could could easily be updated to record all of the pounds to kilograms
# input and output in a data structure of file.
@app.route('/p2k', methods=['POST'])
def p2kfunc():
    pounds = int(request.get_json())
    kilograms = pounds * 0.453592
    data = {
        "Weight": kilograms,
        "Description": "Weight in kilograms"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()