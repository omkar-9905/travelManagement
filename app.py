from flask import Flask, flash, render_template, request, redirect, session
import requests
import json
import mysql.connector
import csv
import yaml


API_KEY = '2mV1iX6Fd8Fx87j_3PDsUz5p9JjNDRfvZRqoijC4wbzF_QeXe9xReZ8TMmSjp22CQtF_WCRyzt08KHKla30wMFVOSnPqTkakoVO0_tf2oH_BCyW_FQgNgKjyoTA3Y3Yx'
SEARCH_PATH = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % API_KEY}



# crsr.execute("select * from Persons;")
# print(crsr.fetchall())
app = Flask(__name__)

def db_call(plan_data):
    conn = mysql.connector.connect(user="root", password="e~oJ^vNcTm5^.2BD", host="34.28.144.64", database="cloud-computing-db")
    new_data = yaml.safe_load(plan_data['msg'])
    new_data_address = str(new_data['location']['display_address'])
    sql = f"INSERT into Places (planid,bizid, bizname, bizurl, price, ratings, address, phone, imgurl) values (31,{new_data['id']},'{new_data['name']}','{new_data['url']}','{new_data['price']}',{new_data['rating']},{new_data_address},'{new_data['phone']}','{new_data['image_url']}'))"
    print(sql)
    c1 = conn.cursor()
    c1.execute(sql)
    # conn.commit()
    # conn.close()
    
    print("ADDED SUCCESSFULLY")
    

@app.route("/", methods=['GET','POST'])

def index():

    return render_template('index.html')

@app.route("/addTODB", methods=['GET','POST'])
def addTODB():
    if request.method == 'POST':
        data = request.json
        db_call(data)
        return data['msg']


@app.route("/createPlan", methods=['GET','POST'])
def createPlan():

    if request.method == 'POST':

        if 'city' in request.form :
            city = request.form["city"]
            term = request.form["name"]

            PARAMETERS = {'location':city,
                            'term':term,
                            'limit':10}

            response = requests.get(url=SEARCH_PATH, 
                                    params=PARAMETERS, 
                                    headers=HEADERS)
            
            business_data = response.json()
            businesses=business_data['businesses']
            return render_template('createPlan.html', biz_json = business_data['businesses'])

        elif 'addTODB' in request.form:
            id = request.form['addTODB']
            print(id)

        return render_template('createPlan.html')
    


if __name__ == '__main__':
    app.run(debug=True)
