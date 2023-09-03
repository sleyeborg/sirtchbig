import requests
from flask import Blueprint, Response, request, jsonify
from flask import Blueprint, render_template
from utils.scrape_products import scrape_products
specify_bp = Blueprint('specify', __name__)
@specify_bp.route('/specify')
def specify():
    print('begin specify_results.html AKA ape4Prod')
    tomogatchi = request.args.get('tomogatchi')
    specOrFuncC = request.args.get('specOrFuncC')
    queri = request.args.get('q')
    print('tomogatchi',tomogatchi,'specOrFuncC',specOrFuncC ,' ...queri',queri)    

    g = scrape_products(queri)
    
    






    return render_template('specify_results.html', links=g, relWordi="sharmoota")
