import requests
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET'])
def home():
        
    return render_template("home.html")

@views.route('/dane-synoptyczne', methods=['GET', 'POST'])
def synop():
    data = requests.get('https://danepubliczne.imgw.pl/api/data/synop').json()
    
    result = []
    if request.method == 'POST':
        serchedCity = request.form.get('city').lower()
        
        for city in data:
            
            if serchedCity in city['stacja'].lower():
                result.append(city)
    else:
        result = data
    
    return render_template("synop.html", data=result)