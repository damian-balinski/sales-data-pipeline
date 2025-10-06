"""
Tests for data extractor
"""
import pandas as pd
import pytest
from src.extract import extract_sales_data

def test_extract_sales_data():
    """Test basic extraction functionality"""
    result = extract_sales_data("test_db", "2025-01-01", "2025-01-31")
    assert result is not None
    assert isinstance(result, pd.DataFrame)
