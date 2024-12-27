from sqlalchemy import Column, Float, ForeignKey, Integer, String

from .db import add_prefix_for_prod, db, SchemaMixin


class Price(db.Model, SchemaMixin):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)

    price = Column(Float, nullable=False)
    station_id = Column(
        Integer,
        ForeignKey(
            add_prefix_for_prod("station.id"), ondelete="CASCADE"
        ),
        nullable=False,
    )
    fuel_type = Column(String)
    user_id = Column(
        Integer,
        ForeignKey(
            add_prefix_for_prod("user.id"), ondelete="CASCADE"
        ),
        nullable=False,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "station_id": self.station_id,
            "fuel_type": self.fuel_type,
            "user_id": self.user_id,
        }
