from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Review


# establish a blueprint for review routes
review_routes = Blueprint("review", __name__)


# #Create Review(login user require)
@review_routes.route("/", methods=["POST"])
@login_required
def create_review():
    
    data = request.get_json()
    required_fields = [
        column.name
        for column in Review.__table__.columns
        if not column.nullable
        and column.name not in ["id", "user_id"]
    ]

    missing_fields = [
        field for field in required_fields if field not in data
    ]
    if missing_fields:
        return {
            "error": f"missing required fields: {missing_fields}"
        }, 400


    review = Review(
        station_id=data["station_id"],
        user_id=current_user.id,
        review=data["review"],
    )

    db.session.add(review)
    db.session.commit()

    return {"review": {review.id: review.to_dict()}}

# Read All Review
@review_routes.route("/", methods=["GET"])
def read_reviews():
    try:
        reviews = Review.query.all()
        return {"review": {review.id: review.to_dict() for review in reviews}}

    except Exception as e:
        return {"error": str(e)}, 500
    

# Read one review by review id
@review_routes.route("/<int:review_id>", methods=["GET"])
def read_review(review_id):
    try:
        review = Review.query.get(review_id)
        return {'review': {review.id: review.to_dict()}}

    except Exception as e:
        return {"error": str(e)}, 500


# Edit a review(require user login)
@review_routes.route("/<int:review_id>", methods=["PUT"])
@login_required
def update_review(review_id):
    try:
        user_id = current_user.id
        review = Review.query.get(review_id)

        #unathorized
        if not review.user_id == user_id:
            return {"message": "forbidden"}, 403

        # change to the database
        data = request.get_json()
        for key, value in data.items():
            setattr(review, key, value)
        
        db.session.commit()

        # success
        return {"review": {str(review_id): review.to_dict()}}

    except Exception as e:
        return {"error": str(e)}, 500


# Delete a review(require user login)
@review_routes.route("/<int:review_id>", methods=["DELETE"])
@login_required
def deleted_review(review_id):
    try:
        user_id = current_user.id
        review = Review.query.get(review_id)

        # failure
        if not review:
            return {"message" "review not found"}
        
        # unathorized
        if not review.user.id == user_id:
            return {"message": "Unauthorized"}, 401


        db.session.delete(review)
        db.session.commit()

        # success
        return {
            "message": f"deleted review {review.id} successfully",
        }

    except Exception as e:
        return {"error": str(e)}, 500
