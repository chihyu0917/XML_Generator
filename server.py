from flask import Flask, request
from flask_cors import CORS
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/updateXML', methods=['POST'])
def update_xml():
    new_order = request.form['newOrder']
    tree = ET.parse('data.xml')
    root = tree.getroot()

    new_order_element = ET.fromstring(new_order)
    root.append(new_order_element)

    tree.write('../data.xml')
    return "XML updated successfully"

if __name__ == '__main__':
    app.run(debug=True)
