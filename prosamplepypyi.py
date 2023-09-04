from proctoring.proctoring import get_analysis, yolov3_model_v3_path

# insert the path of yolov3 model [mandatory]
yolov3_model_v3_path("yolov3.weights_model_path")

# insert the image of base64 format
imgData = "base64_image_format"
proctorData = get_analysis(imgData, "shape_predictor_68_face_landmarks.dat_model_path")
print(proctorData)