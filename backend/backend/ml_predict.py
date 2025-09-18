def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    import pandas as pd
    model_data = pickle.load(open("titanic_model.sav", "rb"))
    model = model_data["model"]
    features = model_data["features"]
    input_df = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked,
        "Title": title
    }])[features]

    prediction = model.predict(input_df)[0]
    if prediction == 1:
        return "Survived!!"
    else :
        return "Sorry"