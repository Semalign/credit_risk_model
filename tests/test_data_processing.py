import pytest
import pandas as pd
from src.data_processing import process_categorical_column # Assuming this function exists

# Example helper function in src/data_processing.py
# def process_categorical_column(df, column_name):
#     # Simple example: convert to uppercase and then one-hot encode
#     df[column_name] = df[column_name].str.upper()
#     return pd.get_dummies(df, columns=[column_name], prefix=column_name)


def test_process_categorical_column_encoding():
    """
    Test if categorical column is correctly one-hot encoded.
    """
    data = {'col1': [1, 2, 3], 'category': ['A', 'B', 'A']}
    df = pd.DataFrame(data)
    processed_df = process_categorical_column(df.copy(), 'category') # Use .copy() to avoid modifying original

    assert 'category_A' in processed_df.columns
    assert 'category_B' in processed_df.columns
    assert processed_df['category_A'].iloc[0] == 1 # First row 'A' should have 1 for 'category_A'
    assert processed_df['category_B'].iloc[0] == 0
    assert processed_df['category_A'].iloc[1] == 0 # Second row 'B' should have 0 for 'category_A'
    assert processed_df['category_B'].iloc[1] == 1
    assert processed_df.shape[1] == 3 # original col1 + 2 new category cols

def test_process_categorical_column_input_immutability():
    """
    Test if the original DataFrame remains unchanged.
    """
    data = {'col1': [1, 2], 'category': ['A', 'B']}
    original_df = pd.DataFrame(data)
    
    # Pass a copy to the function if it modifies in place, otherwise ensure it returns a new DF
    processed_df = process_categorical_column(original_df.copy(), 'category') 

    # Verify original_df is still the same
    pd.testing.assert_frame_equal(original_df, pd.DataFrame(data))

def test_process_categorical_column_edge_case_empty():
    """
    Test with an empty DataFrame to ensure it handles gracefully.
    """
    df_empty = pd.DataFrame({'col1': [], 'category': []})
    processed_df = process_categorical_column(df_empty.copy(), 'category')
    assert processed_df.empty
    assert 'col1' in processed_df.columns # Make sure other columns are preserved even if empty


# Make sure to create a dummy `src/data_processing.py` with the `process_categorical_column` function
# for these tests to run.