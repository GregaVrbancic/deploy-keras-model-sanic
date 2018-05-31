from sanic import Sanic
from sanic import response
from keras.models import load_model
import numpy as np
import tensorflow as tf

app = Sanic(__name__)

# Preload our diabetes model
print('Loading diabetes model...')
diabetes_model = load_model('./model/diabetes_model.h5')
diabetes_graph = tf.get_default_graph()

def predict_diabetes(features):
    with diabetes_graph.as_default():
        prediction = diabetes_model.predict(np.array([features]))
        print('prediction: ', prediction[0,0])
        return np.float64(prediction[0,0])

@app.route('/diabetes/predict', methods=['POST'])
async def predict_diabetes_ctrl(request):
    features = request.json['features']
    print(features)
    return response.json({'prediction': predict_diabetes(features)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
