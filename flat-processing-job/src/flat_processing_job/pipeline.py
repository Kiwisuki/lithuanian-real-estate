import pandas as pd
from flat_processing_job.settings import TRANSLATED_FEATURE_MAPPINGS


def clean_price(price: str) -> int:
    """Remove currency symbols and spaces, then converts to an integer."""
    return int(price.replace("€", "").replace(" ", ""))


def clean_area(area: str) -> float:
    """Remove measurement symbols and converts to a float."""
    return float(area.replace("m²", "").replace(",", "."))


def split_and_strip(value: str) -> list[str]:
    """Split string values by newline and strips extra spaces."""
    return [item.strip() for item in value.split("\n")] if isinstance(value, str) else []


def apply_feature_mappings(data: pd.DataFrame) -> pd.DataFrame:
    """Apply feature mappings to the dataset by creating boolean columns."""
    for col, values in TRANSLATED_FEATURE_MAPPINGS.items():
        for feature, value in values.items():
            data[feature] = data[col].apply(lambda x: value in x)
    return data.drop(columns=TRANSLATED_FEATURE_MAPPINGS.keys())


def extract_coordinates(data: pd.DataFrame) -> pd.DataFrame:
    """Extract latitude and longitude from the coordinates column."""
    data[["latitude", "longitude"]] = data["coordinates"].apply(pd.Series).astype(float)
    return data.drop(columns=["coordinates"])


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean and processes the data according to predefined rules."""
    data["price"] = data["price"].apply(clean_price)
    data["area"] = data["area"].apply(clean_area)
    data[["room_count", "floor", "total_floors"]] = data[["room_count", "floor", "total_floors"]].astype(int)
    
    # Fill missing values
    data["energy_class"] = data["energy_class"].fillna("Unknown")
    fill_none_cols = ["features", "additional_rooms", "additional_equipment", "security"]
    data[fill_none_cols] = data[fill_none_cols].fillna("None")
    
    # Apply transformations
    for col in fill_none_cols:
        data[col] = data[col].apply(split_and_strip)
    
    data = apply_feature_mappings(data)
    data = extract_coordinates(data)
    
    # Drop unnecessary columns
    drop_columns = ["images", "nearest_kindergarten", "nearest_school", "nearest_store"]
    data = data.drop(columns=drop_columns)
    
    return data

