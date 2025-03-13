from src.dtw_lab.lab2 import get_statistic 
import pandas as pd
import pytest
from dtw_lab.lab1 import (
    read_csv_from_google_drive,
    encode_categorical_vars,
    calculate_statistic,
    clean_data ,
)

def test_calculate_statistic():
    df = pd.DataFrame({"Charge_Left_Percentage": [39, 60, 30, 30, 41]})
    assert calculate_statistic("mean", df["Charge_Left_Percentage"]) == 40
    assert calculate_statistic("median", df["Charge_Left_Percentage"]) == 39
    assert calculate_statistic("mode", df["Charge_Left_Percentage"]) == None

def test_encoder():
    df = pd.DataFrame({
        'Manufacturer': ['Duracell', 'Energizer'],
        'Battery_Size': ['D', 'AAA'],
        'Discharge_Speed': ['Fast', 'Slow']
    })

    encoded_df = encode_categorical_vars(df)

    # Check if categorical mapping is applied correctly
    assert encoded_df['Battery_Size'].tolist() == [4, 1]  # D -> 4, AAA -> 1
    assert encoded_df['Discharge_Speed'].tolist() == [3, 1]  # Fast -> 3, Slow -> 1


# def test_api_call(mocker): # Setup the mock
#     mock_get = mocker.patch('mymodule.requests.get') 
#     mock_get.return_value.json.return_value = {'data': 'ake_response'}
#     # Run the function
#     result = my_function_that_calls_api()
#     # Assertions
#     assert result == 'fake_response'
#     assert mock_get.called
#     mock_get.assert_called_once() # Can use more specific assertions