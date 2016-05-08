from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Merchant(Base):
	__tablename__ = 'merchant'
	id = Column(Integer, primary_key=True)
	name = Column(String (100), nullable=False)
	address = Column(String(255), nullable=False)
	lga = Column(String(120), nullable=False)
	state = Column(String(25), nullable=False)
	category = Column(String(50), nullable=False)
	website = Column(String(80))
	short_desc = Column(String(100))
	long_desc = Column(String(255))
	open_time = Column(String(5))
	close_time = Column(String(5))
	img = Column(String(255))

class Images(Base):
	__tablename__ = 'images'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	img_url = Column(String(255))
	merchant = relationship(Merchant)

class PhoneNos(Base):
	__tablename__ = 'phonenos'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	phone_no = Column(String(15))
	merchant = relationship(Merchant)

class Email(Base):
	__tablename__ = 'email'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	email = Column(String(50))
	merchant = relationship(Merchant)

class FeaturedMerchants(Base):
	__tablename__ = 'featuredmerchants'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	merchant = relationship(Merchant)
	
class MerchantViewsCount(Base):
	__tablename__ = 'merchantviewscount'
	id = Column(Integer, primary_key=True)
	viewsCount = Column(Integer)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	merchant = relationship(Merchant)
	
class MerchantLikesCount(Base):
	__tablename__ = 'merchantlikescount'
	id = Column(Integer, primary_key=True)
	likes = Column(Integer)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	merchant = relationship(Merchant)
	
class VistorsHistory(Base):
	__tablename__ = 'visitorshistory'
	id = Column(Integer, primary_key=True)
	geolocation = Column(String(100))
	ipaddress = Column(String(50), nullable=True)
	datetime = Column(Date)
	page = Column(String(255))
	
class VisitorsCount(Base):
	__tablename__ = 'visitorscount'
	id = Column(Integer, primary_key=True)
	count = Column(Integer)
	
class CategoryClicksCount(Base):
	__tablename__ = 'categoryclickscount'
	id = Column(Integer, primary_key=True)
	""" This table should contain fields for each category where it records
		the number of times that category has been clicked
	"""
	name = Column(String(50))
	count = Column(Integer)

class Message(Base):
	__tablename__ = 'message'
	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	email = Column(String(50))
	subject = Column(String(150))
	body = Column(String)


engine = create_engine('sqlite:///app.db')

Base.metadata.create_all(engine)