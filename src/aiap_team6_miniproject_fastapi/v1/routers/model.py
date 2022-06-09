import logging
import fastapi

import aiap_team6_miniproject_fastapi as team6_miniproject_fapi

from fastapi import UploadFile

logger = logging.getLogger(__name__)


ROUTER = fastapi.APIRouter()
PRED_MODEL = team6_miniproject_fapi.deps.PRED_MODEL
PROCESS_IMAGE = team6_miniproject_fapi.deps.PROCESS_IMAGE # To call in deps.py
# need to create PROCESS_IMAGE.py in data_prep.py

# Streamlit uploaded the image instead.

# @ROUTER.post("/uploadfile/", status_code=fastapi.status.HTTP_200_OK)
# def upload_image(file: UploadFile):
#     """
#     """
#     # Need to figure out what goes here

#     return {"filename": file.filename}

# @ROUTER.delete("/delete/", status_code=fastapi.status.HTTP_200_OK)
# def delete_image(file):
#     """
#     """

#     # Need to figure out what goes here

#     return {"deleted_file": str} # place holder for deleted image file name.

@ROUTER.post("/preprocess", status_code=fastapi.status.HTTP_200_OK)
def preprocess(image_data): # place holder for image preprocessing 
    """Endpoint that takes in the image from user upload and preprocess it for
    training or inference.

    Parameters
    ----------
    image : Image that user upload for training or inference.

    Returns
    -------
    str
        address of the preprocessed image
    """
    
    try:
        logger.info("Preprocessing uploaded image")
        image = image_data
        processed_image = PROCESS_IMAGE.process(image)

        # Figure a way to save to polyaxon persistent data
        # Create the address of the saved image

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(
            status_code=500, detail="Internal server error.")

    return {"address": str} # placeholder for processed image address

# Template below

@ROUTER.post("/predict", status_code=fastapi.status.HTTP_200_OK)
def predict_sentiment(movie_reviews_json: team6_miniproject_fapi.schemas.MovieReviews):
    """Endpoint that returns sentiment classification of movie review
    texts.

    Parameters
    ----------
    movie_reviews_json : team6_miniproject_fapi.schemas.MovieReviews
        'pydantic.BaseModel' object detailing the schema of the request
        body

    Returns
    -------
    dict
        Dictionary containing the sentiments for each movie review in
        the body of the request.

    Raises
    ------
    fastapi.HTTPException
        A 500 status error is returned if the prediction steps
        encounters any errors.
    """
    result_dict = {"data": []}

    try:
        logger.info("Generating sentiments for movie reviews.")
        movie_reviews_dict = movie_reviews_json.dict()
        review_texts_array = movie_reviews_dict["reviews"]
        for review_val in review_texts_array:
            curr_pred_result = PRED_MODEL.predict([review_val["text"]])
            sentiment = ("positive" if curr_pred_result > 0.5
                        else "negative")
            result_dict["data"].append(
                {"review_id": review_val["id"], "sentiment": sentiment})
            logger.info(
                "Sentiment generated for Review ID: {}".
                format(review_val["id"]))

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(
            status_code=500, detail="Internal server error.")

    return result_dict


@ROUTER.get("/version", status_code=fastapi.status.HTTP_200_OK)
def get_model_version():
    """Get version (UUID) of predictive model used for the API.

    Returns
    -------
    dict
        Dictionary containing the UUID of the predictive model being
        served.
    """
    return {"data": {"model_uuid": team6_miniproject_fapi.config.SETTINGS.PRED_MODEL_UUID}}
