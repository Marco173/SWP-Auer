# Declarative-Variante wird hier benutzt
from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request
from sqlalchemy import Column, Integer, Text
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

import os
from flask_restful import Resource, Api

Base = declarative_base()  # Basisklasse aller in SQLAlchemy verwendeten Klassen
metadata = Base.metadata

# Welche Datenbank wird verwendet
engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()
app = Flask(__name__)  # Die Flask-Anwendung
api = Api(app)  # Die Flask API


@dataclass
class Statistics(Base):
    __tablename__ = 'statistics'  # Abbildung auf diese Tabelle

    id = Column(Integer, primary_key=True)
    playername = Column(Text)
    rock = Column(Text)
    paper = Column(Text)
    scissors = Column(Text)
    lizzard = Column(Text)
    spock = Column(Text)

    def serialize(self):
        return {'id': self.id,
                'playername': self.playername,
                'rock': self.rock, 'paper': self.paper, 'scissors': self.scissors, 'lizzard': self.lizzard,
                'spock': self.spock}


# when / is called the statistics are returned


@app.route('/')
def index():
    return jsonify([e.serialize() for e in Statistics.query.all()])


class StatisticsClass(Resource):
    def get(self, playername):
        print(playername)
        player = Statistics.query.filter(
            Statistics.playername == playername).first()
        if player:
            return jsonify(player.serialize())
        else:
            return {"Message": "Nicht gefunden"}

    def put(self, playername):
        # check if the playername already exists
        data = request.get_json()
        rock = data['rock']
        paper = data['paper']
        scissors = data['scissors']
        lizzard = data['lizzard']
        spock = data['spock']

        existing = Statistics.query.filter(
            Statistics.playername == playername).first()
        if existing:
            existing.rock = rock
            existing.paper = paper
            existing.scissors = scissors
            existing.lizzard = lizzard
            existing.spock = spock
            db_session.commit()

            return {"Message": "Überschrieben"}
        else:
            # get data from the request
            print(data)

            new = Statistics(playername=playername, rock=rock, paper=paper,
                             scissors=scissors, lizzard=lizzard, spock=spock)
            db_session.add(new)
            db_session.commit()
            return {"Message": "Neu hinzugefügt"}

    def delete(self):
        return {'param1': 'HELLO',
                'param2': 13}


api.add_resource(StatisticsClass, '/<string:playername>')

if __name__ == '__main__':
    app.run(debug=True)