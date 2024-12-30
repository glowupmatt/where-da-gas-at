from sqlalchemy.orm import relationship

from .db import (
    add_prefix_for_prod,
    db,
    environment,
    SchemaMixin,
)


class Station(db.Model, SchemaMixin):
    __tablename__ = "station"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    uri = db.Column(db.Text, nullable=False)
    location_id = db.Column(db.String(255), nullable=False)

    king_id = db.Column(
        db.Integer,
        db.ForeignKey(
            add_prefix_for_prod("king.id"), ondelete="CASCADE"
        ),
        nullable=False,
    )

    king = db.relationship("King", back_populates="station")
    review = db.relationship("Review", back_populates="station")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng,
            "address": self.address,
            "uri": self.uri,
            "location_id": self.location_id,
            "king_id": self.king_id,
        }
