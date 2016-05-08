from flask import Flask, render_template, request, url_for, redirect, \
    flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from model import *

app = Flask(__name__)

engine = create_engine('sqlite:///app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def home():
    """ Displays HomePage to user

    """
    # Get merchants to be shown under featured merchants
    featuredMerchants = session.query(FeaturedMerchants).all()
    merchants = []
    for merchant in featuredMerchants:
        merchants.append(merchant.merchant)

    # Get merchants to be shown under other merchants
    otherMerchants = session.query(Merchant).all()

    return render_template('index.html', 
                            featuredMerchants=merchants,
                            otherMerchants=otherMerchants)

@app.route('/category/<category_name>')
def category(category_name):
    """ Get all merchants of a particular category
    """
    merchantsInCategory = session.query(Merchant).filter_by(category = \
        category_name).all()

    return render_template('category.html',
                            category_name=category_name,
                            merchants=merchantsInCategory)

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
    record = session.query(Merchant).filter_by(id = merchant_id).first()
    emails = session.query(Email).filter_by(id = merchant_id).all()
    phoneNos = session.query(PhoneNos).filter_by(id = merchant_id).all()
    images = session.query(Images).filter_by(id = merchant_id).all()
    merchantsInSameCategory = session.query(Merchant).filter_by(category = \
     record.category).all()
    categoryCount = session.query(CategoryClicksCount).filter_by(name = \
        record.category).first()
    categoryCount.count += 1
    session.add(categoryCount)
    viewsCount = session.query(MerchantViewsCount).filter_by(id = \
        merchant_id).first()
    viewsCount.viewsCount += 1
    session.add(viewsCount)
    session.commit()

    return render_template('merchant-details.html',
                            selectedMerchant=record,
                            emails=emails,
                            phoneNos=phoneNos,
                            images=images,
                            merchantsInSameCategory=merchantsInSameCategory)

@app.route('/contact-us', methods=['GET', 'POST'])
def contactUs():
    """ Send User specific request to database to be viewed by admin"""
    if request.method == 'POST':
        newItem = Message(name=request.form['name'], 
                          email=request.form['email'],
                          subject=request.form['subject'],
                          body=request.form['body'])
        session.add(newItem)
        session.commit()
        flash("Your message has been posted!")
        return redirect(url_for('home'))
    else:
        return render_template('contact-us.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """ Search database for records that meet search criteria

    """
    if request.method == 'POST':
        searchVar = request.form['search']
        searchResult = session.query(Merchant).filter_by(or_(name.like(searchVar),
            address.like(searchVar), lga.like(searchVar),
            state.like(searchVar), category.like(searchVar),
            website.like(searchVar), short_desc.like(searchVar)))
        return render_template('search-result.html',
                                searchResult=searchResult)
    else:
        return redirect(url_for('home'))

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

@app.route('/admin/delete-merchant/<int:merchant_id>', methods=['GET', 'POST'])
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

@app.route('/admin/delete-carousel/<int:merchant_id>', methods=['GET', 'POST'])
def deleteCarousel(merchant_id):
    """ Delete a carousel

    """
    return "Delete a carousel"

if __name__ == '__main__':
    app.secret_key = "that_uyona_boy_wanna_do_good"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)