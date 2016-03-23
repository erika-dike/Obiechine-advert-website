from flask import Flask, render_template, request, url_for, redirect, \
    flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model import Base, Merchant, MerchantViewsCount, MerchantLikesCount, \
    VisitorsHistory, VisitorsCount, CategoryClicksCount

app = Flask(__name__)

engine = create_engine('sqlite:///app.db')
Base.metadata.bine = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
    """ Displays HomePage to user

    """
    return "Hello Peeps"

@app.route('/login')
def login():
    """ Logs the admin in

    """
    return "Log that admin"

@app.route('/admin')
def admin():
    """ Gives the admin controls for manipulating database

    """
    return "Give that admin chance"

@app.route('/detail/<int:merchant_id>')
def detail(merchant_id):
    """ Display details of particular merchant

    """
    return "Heyo"

@app.route('/request', methods=['GET', 'POST'])
def request():
    """ Send User specific request to database to be viewed by admin

    """
    return "Your wish is my command"

@app.route('/search', methods=['GET', 'POST'])
def search():
    """ Search database for records that meet search criteria

    """
    return "Wetinn you dey look for"

@app.route('/logout')
def logout():
    """ Log out the admin

    """
    return "Log me out abeg"

@app.route('/admin/view-all-merchants')
def showMerchants():
    """ Show all merchants to admin

    """
    return "Show me the merchants"

@app.route('/admin/add-new-merchant', methods=['GET', 'POST'])
def newMerchant():
    """ Add a new merchant to database

    """
    return "Add new Merchant"

@app.route('/admin/edit-merchant/<int:merchant_id>', methods=['GET', 'POST'])
def editMerchant(merchant_id):
    """ Edit merchant in the merchant table

    """
    return "Edit a merchant"

@app.route('/admin/delete-merchant/<int:merchant_id', methods=['GET', 'POST'])
def deleteMerchant(merchant_id):
    """ Delete merchant from database

    """
    return "Delete a merchant"

@app.route('/admin/add-to-carousel', methods=['GET', 'POST'])
def newCarousel():
    """ Add merchant to carousel only if there are less than five items

    """
    return "carousel"

@app.route('/admin/edit-carousel/<int:merchant_id>', methods=['GET', 'POST'])
def editCarousel(merchant_id):
    """ Edit a carousel

    """
    return "Edit carousel"

@app.route('/admin/delete-carousel/<int:merchant_id', methods=['GET', 'POST'])
def deleteCarousel(merchant_id):
    """ Delete a carousel

    """
    return "Delete a carousel"

if __name__ == '__main__':
    app.secret_key = "that_uyona_boy_wanna_do_good"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)