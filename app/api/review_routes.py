from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..models import db, Review
from ..forms import ReviewForm

# establish a blueprint for review routes
review_routes = Blueprint("review", __name__)


# #Create Review
@review_routes.route("/", methods=["POST"])
@login_required
def create_review():
    created_form = ReviewForm()
    created_form["csrf_token"].data = request.cookies["csrf_token"]

    created_form['user_id'].data = current_user.id

    if created_form.validate_on_submit():
      
        station_id = created_form.data.get("station_id")
        review_text = created_form.data.get("text")  


        if not review_text or not station_id:
            return (
                jsonify(
                    {
                        "message": "bad request",
                        "error": {
                            "text": "text is required",
                            "station_id": "station id is required",
                            "user_id": "user id is required",
                        },
                    }
                ),
                400,
            )

        review = Review(
            station_id=station_id,
            user_id=current_user.id,
            text=review_text,
        )

        db.session.add(review)
        db.session.commit()

        return {"review": {str(review.id): review.to_dict()}}, 200
    return created_form.errors, 401


# Read one review
@review_routes.route("/<int:review_id>", methods=["GET"])
def read_review(review_id):
    try:
        review = Review.query.filter(Review.id == review_id).first()

        # failure
        if not review:
            return {"error": f"text {review.id} not found"}, 404

        return {"text": {str(review.id): review.to_dict()}}, 200

    except Exception as e:
        return {"error": str(e)}, 500


# Read All Review
@review_routes.route("/", methods=["GET"])
def read_reviews():
    try:
        reviews = Review.query.all()
        return {
            "text": {
                str(review.id): review.to_dict() for review in reviews
            }
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500


# Edit a review(require user login)
@review_routes.route("/<int:review_id>", methods=["PUT"])
@login_required
def update_review(review_id):
    try:
        updated_form = ReviewForm()
        updated_form["csrf_token"].data = request.cookies[
            "csrf_token"
        ]

        if updated_form.validate_on_submit():
            review = Review.query.filter(
                Review.id == review_id
            ).first()

        # failure
        if not review:
            # TODO: return only messages that apply
            return (
                jsonify(
                    {
                        "message": "bad request",
                        "error": {
                            "text": "text is required",
                            "station_id": "station id is required",
                            "user_id": f"{review.id}",
                        },
                    }
                ),
                400,
            )

        # unathorized
        if not current_user.id == review.user_id:
            return {"error": {"message": "Unauthorized"}}, 401

        review.user_id = updated_form.data["user_id"]
        review.station_id = updated_form.data["station_id"]
        review.text = updated_form.data["text"]

        # change to the database
        db.session.commit()

        # success
        return jsonify(review.to_dict()), 200

    except Exception as e:
        return {"error": str(e)}, 500


# Delete a review(require user login)
@review_routes.route("/<int:review_id>", methods=["DELETE"])
@login_required
def deleted_review(review_id):
    try:
        review = Review.query.filter(Review.id == review_id).one()

        # unathorized
        if not current_user.id == review.user_id:
            return {"error": {"message": "Unauthorized"}}, 401

        # failure
        if not review:
            return {"error": f"text {review.id} is not found"}

        db.session.delete(review)
        db.session.commit()

        # success
        return {
            "message": f"deleted text {review.id} successfully",
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500
