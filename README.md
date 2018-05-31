# Deploy Keras model using Sanic framework

An example of deploying Keras model as API using Sanic framework.

## Requirements

- [Python](https://www.python.org/downloads/) >= 3.6 (should also work with version >= 2.7)
- [pip](https://pip.pypa.io/en/stable/installing/)
- pipenv: ```pip install pipenv```

## Installation

Install all the required dependencies with following command: ```pipenv shell```.

## Run

Firstly enter ```pipenv shell``` and then execute ```python app.py```.

Test the API with following cURL command:

```shell
curl -X POST \
  http://localhost:5000/diabetes/predict \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
	"features": [4,148,60,27,318,30.9,0.15,79]
}'
```

> The feature array in cURL request represent values for:
> - Pregnancies
> - Glucose
> - Blood Pressure
> - Skin Thickness
> - Insulin
> - BMI
> - Diabetes Pedigree Function
> - Age

The response should be similar to this:

```json
{
    "prediction": 0.7101869583129883
}
```

### Docker

Build Docker image with command ```docker build -t deploy-keras-model-sanic .```

Run built Docker image with ```docker run --name keras-sanic -p 5555:5000 deploy-keras-model-sanic```.

To test the API use the cURL command from above, changing the *localhost* with the *IP* and *port* with port number binded to docker host port.
