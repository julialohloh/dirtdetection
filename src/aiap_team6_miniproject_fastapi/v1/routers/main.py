import os
# import logging
import fastapi

# import aiap_team6_miniproject_fastapi as team6_miniproject_fapi
# import aiap_team6_miniproject.data_prep.process_image as process_image
from PIL import Image
# from utils import read_imagefile
from fastapi import UploadFile, File, Form
from io import BytesIO

# logger = logging.getLogger(__name__)


app = fastapi.APIRouter()
# PRED_MODEL = team6_miniproject_fapi.deps.PRED_MODEL

def read_imagefile(file):
    """Takes in jpg and png file and Read it

    Parameters
    ----------

    file: Image file with extension jpg or png

    Returns
    -------

    array
        Image array data
    """
    image = Image.open(BytesIO(file))
    
    return image
    
@app.post("/preprocess/image", status_code=fastapi.status.HTTP_200_OK)
async def preprocess_api(file: UploadFile=File(...)): # place holder for image preprocessing 
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
    print("here reached")

    image = read_imagefile(await file.read())

    print("image read")

    print(file)
    print(file.filename)
    print(image)
    print("Separated")
    

    image.save(file.filename + r".jpg")
    # image.save(str(os.getcwd()) + r"\\" + file.filename + r".jpg")

    wk_dir = str(os.getcwd())
    print(wk_dir)

    # print prints starlette.datastructure.UploadFile object at 0x0000015A7920E2B0 


    return {"address": wk_dir} # placeholder for processed image address


# @ROUTER.get("/download/", status_code=fastapi.status.HTTP_200_OK)
# def download_image_api():
#     """
#     """
#     # need to figure out how to download processed image.
#     pass


# @ROUTER.delete("/delete/", status_code=fastapi.status.HTTP_200_OK)
# def delete_image(file):
#     """
#     """

#     # Need to figure out what goes here

#     return {"deleted_file": str} # place holder for deleted image file name.





##############################################################################
# Ryzal Template below

# @ROUTER.post("/predict", status_code=fastapi.status.HTTP_200_OK)
# def predict_sentiment(movie_reviews_json: team6_miniproject_fapi.schemas.MovieReviews):
#     """Endpoint that returns sentiment classification of movie review
#     texts.

#     Parameters
#     ----------
#     movie_reviews_json : team6_miniproject_fapi.schemas.MovieReviews
#         'pydantic.BaseModel' object detailing the schema of the request
#         body

#     Returns
#     -------
#     dict
#         Dictionary containing the sentiments for each movie review in
#         the body of the request.

#     Raises
#     ------
#     fastapi.HTTPException
#         A 500 status error is returned if the prediction steps
#         encounters any errors.
#     """
#     result_dict = {"data": []}

#     try:
#         logger.info("Generating sentiments for movie reviews.")
#         movie_reviews_dict = movie_reviews_json.dict()
#         review_texts_array = movie_reviews_dict["reviews"]
#         for review_val in review_texts_array:
#             curr_pred_result = PRED_MODEL.predict([review_val["text"]])
#             sentiment = ("positive" if curr_pred_result > 0.5
#                         else "negative")
#             result_dict["data"].append(
#                 {"review_id": review_val["id"], "sentiment": sentiment})
#             logger.info(
#                 "Sentiment generated for Review ID: {}".
#                 format(review_val["id"]))

#     except Exception as error:
#         print(error)
#         raise fastapi.HTTPException(
#             status_code=500, detail="Internal server error.")

#     return result_dict


# @ROUTER.get("/version", status_code=fastapi.status.HTTP_200_OK)
# def get_model_version():
#     """Get version (UUID) of predictive model used for the API.

#     Returns
#     -------
#     dict
#         Dictionary containing the UUID of the predictive model being
#         served.
#     """
#     return {"data": {"model_uuid": team6_miniproject_fapi.config.SETTINGS.PRED_MODEL_UUID}}
