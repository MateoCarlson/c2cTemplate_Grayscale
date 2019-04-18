from prettytable import PrettyTable
from flask import Flask, request, render_template
app = Flask(__name__)

x = PrettyTable() # Table to hold formatted output received from the user
x.field_names = ["Name", "Email", "Phone Number", "Message"]

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    # Get the input data from the form into variables
    name = request.form.get('inputFirstName', '')
    email = request.form.get('inputEmail', '')
    phoneNumber = request.form.get('inputPhoneNumber', '')
    message = request.form.get('inputMessage', '')

    # Calculate stress score based upon fixed fields.
    # score = calc_stress_score(name, sleep, homework, final_exams_to_take, freeform)

    # Log results to a file on the server using PrettyTable
    x.add_row([name, email, phoneNumber, message])
    #g = open('results.txt', 'w')  # clear the file and start over.
    g = open('web_results.txt', 'a')  # write to the end of the file so you don't lose data.
    g.write(str(x))
    g.close()

    return render_template("index.html")

if __name__ == '__main__':
    app.run()
