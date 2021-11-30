from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "TP Florian Marques"

@app.route('/means', methods=['GET'])
def meanOfList():
    list = request.args.getlist('int', type=int)

    if len(list) == 0:
        return "Given list is null"
    else:
        return "Mean of the list is : {}".format(sum(list)/len(list))