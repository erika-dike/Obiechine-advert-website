import os
import sys
import sqlalchemy import Column, ForeignKey, Integer, String
import sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm import relationship
import sqlalchemy import create_engine

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
	img = Column(String(100))

class FeaturedMerchants(Base):
	__tablename__ = 'featuredmerchants'
	id = Column(Integer, primary_key=True)
	merchant_id = Column(Integer, ForeignKey('merchant.id'))
	merchant = relationship(Merchant)
	
class MerchantViewsCount(Base):
	__tablename__ = 'merchantviewscount'
	id = Column(Integer, primary_key=True)
	views = Column(Integer)
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
	ipaddress = Column(String(50))
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
	