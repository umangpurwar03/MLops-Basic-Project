from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):
    model = LinearRegression()  # Initialize a new model
    model.fit(X_train, y_train)
    return model  # Return the trained model

def make_predictions(model, X_test):
    y_pred = model.predict(X_test)
    return y_pred  # Return the predicted values
