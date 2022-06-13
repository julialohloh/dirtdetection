# import os
# import logging
# import hydra
# import streamlit as st

# import aiap_team6_miniproject as team6_miniproject

# @st.cache(allow_output_mutation=True)
# def load_model(model_path):
#     return team6_miniproject.modeling.utils.load_model(model_path)

# @hydra.main(config_path="../conf/base", config_name="pipelines.yml")
# def main(args):
#     """This main function does the following:
#     - load logging config
#     - loads trained model on cache
#     - gets string input from user to be loaded for inferencing
#     - conducts inferencing on string
#     - outputs prediction results on the dashboard
#     """

#     logger = logging.getLogger(__name__)
#     logger.info("Setting up logging configuration.")
#     logger_config_path = os.path.\
#         join(hydra.utils.get_original_cwd(),
#             "conf/base/logging.yml")
#     team6_miniproject.general_utils.setup_logging(logger_config_path)

#     logger.info("Loading the model...")
#     pred_model = load_model(args["inference"]["model_path"])

#     logger.info("Loading dashboard...")
#     title = st.title('AIAP Team 6 Mini Project')

#     text_input = st.text_area("Review",
#         placeholder="Insert your review here")

#     if st.button("Get sentiment"):
#         logger.info("Conducting inferencing on text input...")
#         curr_pred_result = float(pred_model.predict([text_input])[0])
#         sentiment = ("positive" if curr_pred_result > 0.5
#                     else "negative")
#         logger.info(
#             "Inferencing has completed. Text input: {}. Sentiment: {}"
#             .format(text_input, sentiment))
#         st.write("The sentiment of the review is {}."
#             .format(sentiment))
#     else:
#         st.write("Awaiting a review...")

# import os
# import logging
import streamlit as st
import requests
# import aiap_team6_miniproject as a6
from PIL import Image
# import fastapi
# import io

# interact with FastAPI endpoint
test_url = "http://127.0.0.1:8080/preprocess/image"


# @st.cache(allow_output_mutation=True)
# def load_model(model_path):
#     return a6.modeling.utils.load_model(model_path)

@st.cache(allow_output_mutation=True)
def load_image(image_file):
    img = Image.open(image_file)
    return img

#@hydra.main(config_path="../conf/base", config_name="pipelines.yml")
def main():
    """This main function does the following:
    - load logging config
    - loads trained model on cache
    - gets string input from user to be loaded for inferencing
    - conducts inferencing on string
    - outputs prediction results on the dashboard
    """

    # logger = logging.getLogger(__name__)
    # logger.info("Setting up logging configuration.")
    # logger_config_path = os.path.\
    #     join(hydra.utils.get_original_cwd(),
    #         "conf/base/logging.yml")
    # a6.general_utils.setup_logging(logger_config_path)

    # logger.info("Loading the model...")
    # pred_model = load_model(args["inference"]["model_path"])

    # logger.info("Loading dashboard...")

    st.subheader("AIAP Team 6")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
        
        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                            "filesize":image_file.size}
        st.write(file_details)
        # To View Uploaded Image

        st.image(load_image(image_file))

        test_file = image_file.read()
        #test_file = open(image_file)
        test_response = requests.post(
            test_url, files = {"file": test_file}
            )
        st.write(test_response)

        # p1 = requests.post(url=test_url, data={'d':'d'}, json={'j':'j'})
        # st.write(p1)


        # if test_response.ok:
        #     print("Upload completed successfully!")
        #     print(test_response.text)
        # else:
        #     print("Something went wrong!")
    
        # Push image to fastapi so that you guys can do preprocessing
        # Get preprocessed img from fastapi

        # To change this
        # if st.button("Predictions"):
        #     logger.info("Conducting inferencing on text input...")
        #     curr_pred_result = float(pred_model.predict([image_file])[0])
        #     sentiment = ("positive" if curr_pred_result > 0.5
        #                 else "negative")
        #     logger.info(
        #         "Inferencing has completed. Text input: {}. Sentiment: {}"
        #         .format(image_file, sentiment))
        #     st.write("The sentiment of the review is {}."
        #         .format(sentiment))
        # else:
        #     st.write("Awaiting a review...")

        st.download_button(
        label="Download image", 
        data=image_file,
        file_name="imagename.png",
        mime="image/png")

if __name__ == "__main__":
    main()
