from .db import add_prefix_for_prod, db, environment, SchemaMixin


class Review(db.Model, SchemaMixin):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    king_id = db.Column(
        db.Integer,
        db.ForeignKey(
            add_prefix_for_prod("king.id"), ondelete="CASCADE"
        ),
        nullable=False,
    )
    station_id = db.Column(
        db.Integer,
        db.ForeignKey(
            add_prefix_for_prod("station.id"), ondelete="CASCADE"
        ),
        nullable=False,
    )
    review = db.Column(db.Text, nullable=False)

    king = db.relationship("King", back_populates="review")
    station = db.relationship("Station", back_populates="review")

    def to_dict(self):
        return {
            "id": self.id,
            "king_id": self.king_id,
            "station_id": self.station_id,
            "review": self.review,
        }
