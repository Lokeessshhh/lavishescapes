from flask import Flask, request, render_template, jsonify
import boto3
import json

app = Flask(__name__)

aws_access_key = 'AKIAVTQN5VB2HIC5I2WE'
aws_secret_key = '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'
region = 'ap-south-1'

lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    data = {
        "destination": request.form['destination'],
        "people": request.form['people'],
        "checkin": request.form['checkin'],
        "checkout": request.form['checkout']
    }

    response = lambda_client.invoke(
        FunctionName='book_tour_or_vehicle',
        InvocationType='RequestResponse',
        Payload=json.dumps({"body": json.dumps(data)})
    )

    result = json.load(response['Payload'])
    return jsonify(result)

@app.route('/rent', methods=['POST'])
def rent():
    data = {
        "pickupLocation": request.form['pickupLocation'],
        "vehicleGuests": request.form['vehicleGuests'],
        "rentIn": request.form['rentIn'],
        "rentOut": request.form['rentOut']
    }

    response = lambda_client.invoke(
        FunctionName='book_tour',
        InvocationType='RequestResponse',
        Payload=json.dumps({"body": json.dumps(data)})
    )

    result = json.load(response['Payload'])
    return jsonify(result)

@app.route('/contact', methods=['POST'])
def contact():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "destination": request.form['destination'],
        "message": request.form['message'] 
    }

    response = lambda_client.invoke(
        FunctionName='contact',
        InvocationType='RequestResponse',
        Payload=json.dumps({"body": json.dumps(data)})
    )

    result = json.load(response['Payload'])
    return jsonify(result)

@app.route('/newsletter', methods=['POST'])
def newsletter():
    data = {
        "email": request.form['email']
    }

    response = lambda_client.invoke(
        FunctionName='newsletter',
        InvocationType='RequestResponse',
        Payload=json.dumps({"body": json.dumps(data)})
    )

    result = json.load(response['Payload'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
