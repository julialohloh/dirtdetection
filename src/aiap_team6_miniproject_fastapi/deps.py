import aiap_team6_miniproject as team6_miniproject
import aiap_team6_miniproject_fastapi as team6_miniproject_fapi
from aiap_team6_miniproject_fastapi.v1.routers.main import PRED_MODEL


PRED_MODEL = team6_miniproject.modeling.utils.load_model(
    team6_miniproject_fapi.config.SETTINGS.PRED_MODEL_PATH)
