from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "GET":
        pclass = int(request.GET["pclass"])
        sex = int(request.GET["sex"])
        age = int(request.GET["age"])
        sibsp = int(request.GET["sibsp"])
        parch = int(request.GET["parch"])
        fare = (request.GET["fare"])
        embarked = int(request.GET["embarked"])
        title = int(request.GET["title"])
        prediction = ml_predict.prediction_model(
            pclass, sex, age, sibsp, parch, fare, embarked, title
        )
        return render(request, 'result.html', {
            'prediction': prediction,
            'age': age,
            'sex': sex,
            'pclass': pclass
        })
