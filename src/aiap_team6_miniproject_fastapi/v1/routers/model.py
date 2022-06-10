import logging
from xxlimited import Str
import fastapi

import aiap_team6_miniproject_fastapi as team6_miniproject_fapi


logger = logging.getLogger(__name__)


ROUTER = fastapi.APIRouter()
PRED_MODEL = team6_miniproject_fapi.deps.PRED_MODEL


@ROUTER.post("/infer", status_code=fastapi.status.HTTP_200_OK)
def predict_model(processed_file_path: str):
    """Endpoint that returns dirty classification of floor image.

    Parameters
    ----------
    processed_file_path : str

    Returns
    -------
    dict
        Dictionary containing the prediction for processed image of the request.

    Raises
    ------
    fastapi.HTTPException
        A 500 status error is returned if the prediction steps
        encounters any errors.
    """

    try:
        logger.info("Generating sentiments for floor image.")
        curr_pred_result, output_file_path = PRED_MODEL.predict(processed_file_path)
        dirt_prediction = "Dirty" if curr_pred_result == 1 else "Clean"

        logger.info("Prediction generated for Image ID: {}".format(dirt_prediction))

    except Exception as error:
        print(error)
        raise fastapi.HTTPException(status_code=500, detail="Internal server error.")

    return {
        "data": {"prediction": dirt_prediction, "image_file_path": output_file_path}
    }


@ROUTER.get("/version", status_code=fastapi.status.HTTP_200_OK)
def get_model_version():
    """Get version (UUID) of predictive model used for the API.

    Returns
    -------
    dict
        Dictionary containing the UUID of the predictive model being
        served.
    """
    return {
        "data": {"model_uuid": team6_miniproject_fapi.config.SETTINGS.PRED_MODEL_UUID}
    }
