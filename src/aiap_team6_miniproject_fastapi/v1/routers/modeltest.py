from fileinput import filename
import os
import logging
import fastapi
import uuid
#from fastapi.responses import FileResponse

# import aiap_team6_miniproject_fastapi as team6_miniproject_fapi
# import aiap_team6_miniproject.data_prep.process_image as process_image
from PIL import Image
# from utils import read_imagefile
from fastapi import UploadFile, File, Form, Response
from io import BytesIO
import shutil
import shutil
import uuid
from pathlib import Path
from typing import List
from infer import Inference

# logger = logging.getLogger(__name__)
ROUTER = fastapi.APIRouter()
# PRED_MODEL = team6_miniproject_fapi.deps.PRED_MODEL
#################################Julia working codes########################
  
@ROUTER.post("/preprocess/image", status_code=fastapi.status.HTTP_200_OK)
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
    WORK_DIR = os.getcwd()
    # UUID to prevent file overwrite
    # 'beautiful' path concat instead of WORK_DIR + '/' + REQUEST_ID
    WORKSPACE = WORK_DIR
    if not os.path.exists(WORKSPACE):
        # recursively create workdir/unique_id
        os.makedirs(WORKSPACE)
    # iterate through all uploaded files
    file.filename = f"{uuid.uuid4()}.jpg"
    FILE_PATH = Path(file.filename)
    WRITE_PATH = WORK_DIR / FILE_PATH
    with open(str(WRITE_PATH) ,'wb') as myfile:
        contents = await file.read()
        myfile.write(contents)
    # return local file paths
    a = Inference()
    result_dir = a.infer(weights='YOLOMODEL/full_10epoch.pt',project="YOLOMODEL/runs/detect",imgsz=[1280,900], source=WRITE_PATH)
    print(WRITE_PATH)
    return {"filepath": result_dir}
    results = Inference.get_results(result_dir)
    # return local file paths
    bytes_io = BytesIO()
    results.save(bytes_io, format='PNG')
    return Response(bytes_io.getvalue(), media_type="image/png")
    return {"filepath": str(WRITE_PATH), "source": WORK_DIR}
