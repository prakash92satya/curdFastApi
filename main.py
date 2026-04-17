from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Satya123',
    database='mydatabase'
)


@app.route('/addStudent',methods=['POST']) # working
def add_student():
    data=request.get_json()
    id=data.get('id')
    name=data.get('name')
    mark=data.get('mark')

    cursor = db.cursor()
    query = "UPDATE students SET name=%s, mark=%s WHERE id=%s"
    cursor.execute(query, (name, mark, id))
    db.commit()
    return jsonify({"message": "Student added successfully"}),200

@app.route('/update',methods=['PUT'])  
def update_data():
    id=request.json.get('id')
    name=request.json.get('name')
    mark=request.json.get('mark')
    cursor = db.cursor()
    query = "UPDATE students SET name=%s, mark=%s WHERE id=%s"
    cursor.execute(query,(name,mark,id))
    db.commit()
    cursor.close()
    return jsonify({"message":"update !!"}),200



@app.route('/delete/<int:id>',methods=['DELETE'])  # working
def delete_data(id):
    cursor=db.cursor()
    query="DELETE FROM students WHERE id=%s"
    cursor.execute(query,(id,))
    db.commit()
    cursor.close()
    return jsonify({"message":"deleted !!!"}),200

@app.route('/fetchAll', methods=['GET']) # working
def fetch_all():
    cursor=db.cursor( dictionary=True )
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)

@app.route('/postList', methods=['POST']) # working
def post_list():
    reqData=request.json
    cursor=db.cursor()
    query="INSERT INTO students (name,mark) VALUES (%s,%s)"
    for student in reqData:
        name=student.get('name')
        mark=student.get('mark')
        cursor.execute(query,(name,mark))
    db.commit()
    cursor.close()
    return jsonify({"message": "List posted !!"})


@app.route('/fetchbyid/<int:id>',methods=['GET']) # working
def fetchById(id):
    cursor=db.cursor( dictionary=True )
    cursor.execute("select * from students WHERE id=%s", (id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)





if __name__ == '__main__':
    print("connecting to db ........")
    app.run()
