from flask import Flask, jsonify
from models import db, RKE #Country, Regulator
from flask_cors import CORS
import yaml

config_path = 'config.yml'

with open(config_path) as credential:
    config = yaml.load(credential,Loader = yaml.FullLoader)
    


app = Flask(__name__)
CORS(app)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config["conn"]["user"]}:{config["conn"]["password"]}@{config["conn"]["host"]}/{config["conn"]["database"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# create api endpoint
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
