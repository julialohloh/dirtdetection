import YOLOMODEL.detect as infer


infer.run(weights="YOLOMODEL/weights/full_10epoch.pt",project="YOLOMODEL/runs/detect",imgsz=[640,640])