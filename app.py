from flask import Flask, jsonify
from models import db, RKE #Country, Regulator
from flask_cors import CORS
import yaml

config_path = 'config.yml'

with open(config_path) as credential:
    config = yaml.load(credential,Loader = yaml.FullLoader)
    
    
app = Flask(__name__)
CORS(app)

# Replace these with your actual data
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config["conn"]["user"]}:{config["conn"]["password"]}@{config["conn"]["host"]}/{config["conn"]["database"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



# @app.route('/api/countries', methods=['GET'])
# def get_countries():
#     countries = Country.query.all()
#     output = []
    
#     for country in countries:
#         country_data = {'country_id': country.country_id, 'country_name': country.country_name, 'country_iso_a2': country.country_iso_a2}
#         output.append(country_data)
#     return jsonify(output)

# @app.route('/api/regulators', methods=['GET'])
# def get_regulators():
#     regulators = Regulator.query.all()
#     output = []
#     for regulator in regulators:
#         regulator_data = {'response_id': regulator.response_id, 'organization_name': regulator.organization_name, 'respondent_name': regulator.respondent_name,
#                           'country_code':regulator.country_code, 'regulator_type':regulator.regulator_type,'a1_priority_change':regulator.a1_priority_change,
#                           'region_wb':regulator.region_wb, 'a3_consumer_protection':regulator.a3_consumer_protection}
#         output.append(regulator_data)
#     return jsonify(output)

# @app.route('/api/countries/<id>', methods=['GET'])
# def get_country(id):
#     country = Country.query.get(id)
#     if country is None:
#         return {"error": "not found"}
#     return {'country_id': country.country_id, 'country_name': country.country_name, 'country_iso_a2': country.country_iso_a2}

@app.route('/api/rke', methods = ['GET'])
def get_rke():
    rke = RKE.query.all()
    output = []
    for member in rke:
        member_data = {'user_id':member.user_id, 'name':member.name, 'organisation':member.organisation,
                       'email':member.email, 'join_group' : member.join_group, 'market_themes': member.market_themes,
                        'gender':member.gender, 'regulatory_initiatives': member.regulatory_initiatives,  
                        'platform_features': member.platform_features, 'area_of_work': member.area_of_work,
                         'introduce_to_users' :member.introduce_to_users, 'country_iso_a3':member.country_iso_a3,
                        'authority_type' : member.authority_type, 'seniority':member.seniority}
        output.append(member_data)
    return jsonify(output)




if __name__ == '__main__':
    app.run()
