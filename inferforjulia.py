from preprocess import Pipeline
import YOLOMODEL.detect as infer
import os
import pandas as pd


# Preprocess the image and return the directory in which the processed images are saved
# pipeline = Pipeline()
# # takes a image list
# imgs_to_detect = pipeline.process("PASS IN A LIST OF IMAGES")

# Refer to detect.py for info on the args
# result_dir = infer.run(weights="YOLOMODEL/weights/full_10epoch.pt",project="YOLOMODEL/runs/detect",imgsz=[1280,900],source="0")
# result_dir = infer.run(weights="YOLOMODEL/full_10epoch.pt",project="YOLOMODEL/runs/detect",imgsz=[1280,900],save_txt=True,save_conf=True)
# print(f"Result dir is {result_dir}")



class Inference():
    def __init__(self) -> None:
        self.result_dir = None
    def _run(self,weights,source,project,name="exp",imgsz=[1280,800],conf_thres=0.25,max_det=1000,device="",line_thicknes=3,hide_labels=False,hide_conf=False) -> str:
        """
        Wrapper for YOLOv3's detect.py
        Args:
            Refer to detect.py for info on the args

        Returns:
            str: directory in which the results of the inference are stored
        """
        self.result_dir = infer.run(weights=weights,source=source,project=project,name=name,imgsz=imgsz,conf_thres=conf_thres,max_det=max_det,device=device,line_thickness=line_thicknes,hide_labels=hide_labels,hide_conf=hide_conf)
        print(f"Result dir is {self.result_dir}")

    def get_results(self,result_dir:str)->list:
        """
        Returns a list of images that were ran through the inference

        Args:
            result_dir (str): Directory storing the inference results
        Returns:
            list: _description_
        """
        detected_images = []
        for root,dirs,files in os.walk(result_dir):
            for file in files:
                detected_images.append(file)
        return detected_images

    def get_conclusion(self,result_dir:str)->str:
        """
        Sums up the total number of detected dirt images and returns dirty/clean if the number of detected dirt objects if over/under 50% of the total number of detected images in the image.

        Args:
            result_dir (str): output file dir

        Returns:
            str: Dirty or not
        """

        for root,dirs,files in os.walk(result_dir):
            # for dir in dirs:
            #     if dir == "labels":
            #         print(dir)
            results = []
            for file in files:
                df = pd.read_csv(os.path.join(result_dir,file),delimiter=" ")
                total_objs = df.iloc[:,0].value_counts()
                total_dirt = 0
                total_others = 0
                # There is only 1 class of labels detected
                if len(total_objs) == 1:
                    # Check if the pure object class is dirt or others
                    if total_objs.index[0] == 1:
                        # Pure dirt labels
                        total_dirt = total_objs[1]
                    else:
                        # Pure others labels
                        total_others = total_objs[0]
                else:
                    # There are 2 classes detected
                    total_dirt = total_objs[1]
                    total_others = total_objs[0]
                # print(total_objs)
                # print(f"There are a total of {len(total_objs)} class labels")
                # print(f"There are a total of {total_dirt} dirt objects")
                # print(f"There are a total of {total_others} other objects")
                dirt_amount = total_dirt/(total_dirt + total_others)
                if dirt_amount >= 0.5:
                    # print(dirt_amount)
                    results.append((file,"dirty"))
                else:
                    # print(dirt_amount)
                    results.append((file,"clean"))
        # print(results)
        return results

    def infer(self,weights,source="YOLOMODEL/data/images",project="YOLOMODEL/runs/detect",name="exp",imgsz=[640,640],conf_thres=0.25,max_det=1000,device="",line_thickness=3,hide_labels=False,hide_conf=False) -> str:
        self._run(weights=weights,source=source,project=project,name=name,imgsz=imgsz,conf_thres=conf_thres,max_det=max_det,device=device,line_thickness=line_thickness,hide_labels=hide_labels,hide_conf=hide_conf)
        print(f"Result dir is {self.result_dir}")

# test_infer = Inference()
# result_dir = "YOLOMODEL/runs/detect/exp33/labels"
# test = test_infer.get_conclusion(result_dir)