# Import some libraries that we need for machine learning stuff
import unittest
import pandas as pd
from module import train_model, make_predictions
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Let's create a class for our tests. We're gonna test some machine learning functions.
class TestMachineLearning(unittest.TestCase):

    # First, we're gonna test if we can train the model. I think that's important.
    def test_train_model(self):
        # Let's get some data from a CSV file. It's about movies, I guess.
        data = pd.read_csv(r'data\Train.csv')

        # We want to predict movie ratings, so we get some features and the ratings
        X = data[['gross', 'genre', 'budget']]
        y = data['rating']

        # Now, we need to split our data into training and... non-training? Never mind.
        # We'll use 20% for non-training, I think that's a good number.
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        # Let's train our super-duper model
        model = train_model(X_train, y_train)  # Get the trained model

        # Now, we need to make sure the model is not empty. That would be bad, right?
        self.assertIsNotNone(model)  # Check that the model is not None

    # Next up, let's check if we can make predictions. I heard that's important in machine learning.
    def test_make_predictions(self):
        # We're back to reading the movie data again. Repetition is key, I guess.
        data = pd.read_csv(r'data\Train.csv')

        # Same movie features and ratings, as always.
        X = data[['gross', 'genre', 'budget']]
        y = data['rating']

        # More splitting, we love splitting, don't we?
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        # Let's train the model again, like we did before. Repetition is the mother of learning, right?
        model = train_model(X_train, y_train)  # Train the model

        # Time to predict stuff. We predict on the training data, because why not?
        y_train_pred = make_predictions(model, X_train)

        # We should make sure that predictions are not empty, just in case.
        self.assertIsNotNone(y_train_pred)

    # Now, let's test the model's performance. Is it good, bad, or something in between?
    def test_model_performance(self):
        # More movie data, but this time with single quotes. Python is picky.
        data = pd.read_csv('data\Train.csv')

        # We're still interested in movie features and ratings. Consistency is our middle name.
        X = data[['gross', 'genre', 'budget']]
        y = data['rating']

        # More splitting, it never gets old.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Let's train the model one more time. Training is our cardio.
        model = train_model(X_train, y_train)  # Train the model

        # Now, it's prediction time again. We predict on both training and test data.
        y_train_pred = make_predictions(model, X_train)
        y_test_pred = make_predictions(model, X_test)

        # Time to calculate the mean squared error (MSE) on both datasets.
        train_mse = mean_squared_error(y_train, y_train_pred)
        test_mse = mean_squared_error(y_test, y_test_pred)

        # And now, we decide if it's good, bad, or something else. I think math is involved.
        if test_mse < train_mse:
            performance = "Good (Model is generalizing well)"
        elif test_mse > train_mse:
            performance = "Overfitting (Model is fitting the training data too closely)"
        else:
            performance = "Underfitting (Model is not fitting the data well)"

        # Time to show the world our results. Printing is how we communicate, right?
        print(f"Training MSE: {train_mse}")
        print(f"Test MSE: {test_mse}")
        print(f"Performance: {performance}")

        # Finally, let's assert that the test MSE is less than or equal to the train MSE. Asserting is cool.
        self.assertTrue(test_mse <= train_mse)

# Now, we're gonna run our tests. Let's see if everything works.
if __name__ == '__main__':
    unittest.main()