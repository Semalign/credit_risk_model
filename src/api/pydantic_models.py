# Pydantic models for API
from pydantic import BaseModel, Field
from typing import Optional

class CreditApplication(BaseModel):
    # These fields MUST match the features your trained model expects as input
    # Add all your engineered features here with their correct types
    # Example features (replace with your actual features):
    total_transaction_amount: float = Field(..., description="Sum of all transaction amounts for the customer.")
    average_transaction_amount: float = Field(..., description="Average transaction amount for the customer.")
    transaction_count: int = Field(..., description="Number of transactions for the customer.")
    last_transaction_days_ago: int = Field(..., description="Recency: Days since last transaction.")
    product_category_encoded: str = Field(..., description="Encoded product category (e.g., 'Loans', 'Investments').")
    channel_id_encoded: str = Field(..., description="Encoded channel ID (e.g., 'Web', 'Android').")
    # ... add all other relevant features derived from your feature engineering

    # Example of optional field
    customer_age: Optional[int] = Field(None, ge=18, le=120, description="Age of the customer.")

    class Config:
        # Example for Swagger UI/OpenAPI documentation
        schema_extra = {
            "example": {
                "total_transaction_amount": 1500.75,
                "average_transaction_amount": 50.0,
                "transaction_count": 30,
                "last_transaction_days_ago": 7,
                "product_category_encoded": "Electronics",
                "channel_id_encoded": "Android",
                "customer_age": 35
            }
        }