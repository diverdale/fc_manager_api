from db import db


class TeamModel(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    league = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"), nullable=False)
    club = db.relationship("ClubModel", back_populate="teams")
    managers = db.Column(db.Integer, nullable=False)
    players = db.relationship("PlayersModel", back_populate="team", lazy="dynamic")