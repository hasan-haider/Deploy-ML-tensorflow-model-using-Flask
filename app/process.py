from imageai.Prediction import ImagePrediction
import os
from app import APP_ROOT
import tensorflow

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

static_loc=os.path.join(APP_ROOT,'static/')
def predict_img(filename):
    tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)
    target=os.path.join(APP_ROOT,'temp/'+filename) #location of image present in temp directory
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()

    tensorflow.compat.v1.logging.set_verbosity(tensorflow.compat.v1.logging.ERROR)

    prediction.setModelPath(os.path.join(static_loc, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
    prediction.loadModel()
    predictions, probabilities = prediction.predictImage(target, result_count=1)
    d={} #dictionary that will save results
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        d[eachPrediction]=eachProbability #prediction output
        #print(eachPrediction , " : " , eachProbability)

    os.remove(target) #delete temporary file

    return d