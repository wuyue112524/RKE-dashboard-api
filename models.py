from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RKE(db.Model):
    __tablename__ = 'rke_forum'

    user_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    organisation = db.Column(db.String)
    email = db.Column(db.String)
    join_group = db.Column(db.String)
    market_themes = db.Column(db.String)
    gender = db.Column(db.String)
    regulatory_initiatives = db.Column(db.String)
    platform_features = db.Column(db.String)
    area_of_work = db.Column(db.String)
    introduce_to_users = db.Column(db.String)
    country_iso_a3 = db.Column(db.String)
    authority_type = db.Column(db.String)
    seniority = db.Column(db.String)
    

    


# class Regulator(db.Model):
#     __tablename__ = 'regulatory_survey'
#     __table_args__ = {'schema': 'reg'}
    
#     response_id = db.Column(db.Integer,primary_key = True)
#     organization_name = db.Column(db.String)
#     respondent_name = db.Column(db.String)
#     country_code = db.Column(db.String)
#     region_wb = db.Column(db.String)
#     regulator_type = db.Column(db.String)
#     a1_priority_change = db.Column(db.String)
#     a3_consumer_protection = db.Column(db.String)
    
    