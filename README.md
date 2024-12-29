# Sales Prediction

This project focuses on predicting sales for retail stores using machine learning models. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, and evaluation. The goal is to provide actionable insights for businesses to optimize inventory and promotional strategies.

## Features

- Predicts sales based on key factors such as promotions, customer count, and day of the week.
- Includes data preprocessing and visualization for exploratory analysis.
- Employs multiple machine learning models, including Linear Regression and XGBoost.
- Deployment-ready model for real-world usage with options for web or API-based interfaces.
- Additional analysis of weekday vs weekend sales comparison.

## Dataset

The dataset contains the following features:
- Date: The date of the sales.
- Sales: Total sales for the day.
- Customers: Number of customers visiting the store.
- Promo: Whether a promotion was active (1 = Yes, 0 = No).
- DayOfWeek: The day of the week.


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Coder-093/sales-prediction.git
    cd sales_prediction-project
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebook for training and evaluation:
    ``bash
    jupyter notebook notebooks/SalesPrediction.ipynb
    ```

4. Run the additional analysis notebook:
    ```bash
    jupyter notebook notebooks/WeekdayVsWeekendSales.ipynb
    ```

## Usage

1. Train the Model: Use the Jupyter notebook to preprocess the data and train the model.

2. Predict Sales: Load the saved models (linear-regression_model.pkl, xgbboost_model.pkl) and use it to predict sales for new data.

3. Analyze Sales Patterns: Use the WeekdayVsWeekendAnalysis notebook to understand sales trends.

4. Deploy the Model: Use app.py for deploying the model with Streamlit.

## Results

The model achieved the following results:

Mean Absolute Error (MAE): 985.43 using Linear Regression Model and 673.87 using XGBoost Model
Best Performing Model: XGBoost

Why XGBoost?

The XGBoost model was selected as the best-performing model based on its superior performance compared to other models. The evaluation was conducted using the Mean Absolute Error (MAE) metric, where a lower value indicates better accuracy. Below are the results for comparison:

Linear Regression MAE: 985.43

XGBoost MAE: 673.87

XGBoost's ability to handle complex relationships and provide better accuracy on the test dataset made it the ideal choice for this project.

## Project Structure

sales_prediction_project/
├── data/                              # Folder for datasets
│   └── train.csv                      # Dataset
├── notebooks/                         # Jupyter notebooks
│   ├── SalesPrediction.ipynb          # Notebook for exploration and modeling
│   └── WeekdayVsWeekendSales.ipynb    # Notebook for weekday vs weekend analysis
├── models/                            # Folder for saved models
│   └── linear_regression_model.pkl
│   └── xgbboost_model.pkl    # Saved ML model
├── app.py                             # Deployment script
├── requirements.txt                   # List of dependencies
├── README.md                          # Project documentation

## Future Work

- Incorporate external data such as weather and holiday schedules to improve predictions.
- Experiment with advanced models like ARIMA or LSTMs for time-series forecasting.
- Deploy the model as a cloud-based API or interactive web app.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Dataset: [Source of the dataset -> Kaggle] Rossmann Sales Dataset

Libraries: Scikit-learn, XGBoost, Pandas, Seaborn, Matplotlib
