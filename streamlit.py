import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a left sidebar for user options
st.sidebar.title('FlickBay App Options')

# Create file upload buttons for training and testing data in the sidebar
st.sidebar.write("### Upload Data Files")
train_data = st.sidebar.file_uploader("Upload Training Data (CSV)", type=["csv"])
test_data = st.sidebar.file_uploader("Upload Testing Data (CSV)", type=["csv"])

train_df = None
test_df = None

if train_data is not None:
    try:
        st.sidebar.write("#### Training Data Preview")
        train_df = pd.read_csv(train_data)
        st.sidebar.dataframe(train_df)
    except Exception as e:
        st.sidebar.write("Error reading training data. Please check the file format and try again.")

if test_data is not None:
    try:
        st.sidebar.write("#### Testing Data Preview")
        test_df = pd.read_csv(test_data)
        st.sidebar.dataframe(test_df)
    except Exception as e:
        st.sidebar.write("Error reading testing data. Please check the file format and try again.")

# Add a "Start Training" button
if st.sidebar.button("Start Training"):
    if train_df is not None and test_df is not None:
        # Proceed with the training process

        # Feature selection and preprocessing for training data
        X_train = train_df[['gross', 'genre', 'budget']]
        y_train = train_df['rating']

        # Feature selection and preprocessing for testing data
        X_test = test_df[['gross', 'genre', 'budget']]

        # Initialize and train the Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test data
        y_pred = model.predict(X_test)

        # Create a DataFrame with serial numbers and predicted ratings
        predictions_df = pd.DataFrame({
           'Serial': test_df['serial'],
           'Predicted_Rating': y_pred
        })

        # Display the predictions in the main app area
        st.title('FlickBay Movie Rating Prediction')
        st.dataframe(predictions_df)

        # Save the DataFrame to a CSV file
        st.markdown("### Download Predictions as CSV")
        st.write("You can download the predictions as a CSV file.")
        st.download_button("Download Predictions as CSV", predictions_df.to_csv(index=False), key='download_predictions')

    else:
        st.sidebar.write("Please upload both training and testing data files.")
