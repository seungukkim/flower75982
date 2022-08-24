# -*- coding: utf-8 -*-

from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine("postgresql://oorbpqoyofkzzz:cf8f09e5eb71660cfca525b431d2029c9753ca80962c0f9f8241192dca533481@ec2-52-207-15-147.compute-1.amazonaws.com:5432/dejcqpc36a8hi6", echo = False)

engine.connect()

## DB 연결 
def db_create():
    
    engine.execute("""
        CREATE TABLE IF NOT EXISTS dreamspon(
            name varchar(90) NOT NULL,
            advantage varchar(10) NOT NULL,
            who varchar(40) NOT NULL,
            age int NOT NULL,
            where1 VARCHAR(30) NOT NULL,
            qualification VARCHAR(30) NOT NULL,
            url VARCHAR(70) NOT NULL,
            image VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/dreamspon.csv')
    print(data)
    data.to_sql(name='dreamspon', con=engine, schema = 'public', if_exists='replace', index=False)


def db_select(choice,choice1,choice2,choice3,choice4):
    list=[]
    # choice="\'%%생활비지원%%'"
    # choice1="\'%%대학생%%'"
    # choice2=25
    # choice3="\'%%서울%%'"
    # choice4="\'%%기초수급자%%'"
    result= engine.execute("SELECT name,url FROM dreamspon WHERE advantage LIKE {0} AND who like {1} AND (age IS null OR age < {2}) AND (where1 IS null or where1 LIKE {3}) AND (qualification IS null or qualification LIKE {4})".format(choice,choice1,choice2,choice3,choice4))
     
    for r in result: 
        list.append(str(r))

    return list

def db_select1():
    list=[]
    # choice="\'생활비지원'"
    # result= engine.execute("SELECT name,url FROM dreamspon WHERE who LIKE'%%대학생%%'")
    result= engine.execute("SELECT name,url,image FROM dreamspon WHERE (age IS null OR age < 25) AND who LIKE '%%대학생%%' AND (where1 LIKE '%%서울%%' OR where1 IS null) AND (qualification LIKE '%%기초수급자%%' OR qualification IS null) AND advantage LIKE '%%학비지원%%'")
    
    for r in result: 
        print(r)
             
        
    

app = Flask(__name__)

@app.route("/")
def index():
    # db_create()
    return "Hello World!"


if __name__ == "__main__":
    # db_create()
    # db_select()
    # db_select1()
    app.run()