# Ffrom fastapi import FastAPI
from src.api.pydantic_models import CreditApplication  # Your input data model
from mlflow.pyfunc import PythonModel # For loading your MLflow model

app = FastAPI(
    title="Bati Bank Credit Scoring API",
    description="API to predict credit risk and assign credit scores.",
    version="0.1.0"
)

# Global variable to hold the loaded ML model
# It's better to load this once at startup, not per request
model = None

@app.on_event("startup")
async def load_model():
    """Load the MLflow model when the FastAPI application starts."""
    global model
    # Replace with your actual MLflow model URI (e.g., from Task 5)
    # You'll need to know the model name and version you registered
    model_uri = "models:/CreditScoringModel_RandomForest/Production" # Or a specific version number
    model = mlflow.pyfunc.load_model(model_uri)
    print(f"MLflow model loaded from {model_uri}")


@app.get("/")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict")
async def predict_credit_risk(data: CreditApplication):
    """
    Predicts credit risk probability for a new customer.
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded yet.")

    # Convert Pydantic model to a Pandas DataFrame/Series matching model's expected input
    input_df = pd.DataFrame([data.dict()]) # .dict() converts Pydantic model to dict

    # Ensure the order and type of columns match the training data
    # This is CRITICAL. You might need to save feature columns from training
    # and reorder/re-process here.
    # Example: if your model expects specific column order after preprocessing
    # input_df = preprocess_inference_data(input_df, trained_scaler, trained_encoder, feature_order)

    # Make prediction
    # For classification, get probability of the positive class (high risk = 1)
    risk_probability = model.predict(input_df)[0] # Assuming model.predict returns a single value or array of probabilities

    # In a real scenario, you'd also convert this probability to a credit score
    # credit_score = calculate_credit_score(risk_probability)

    return {
        "predicted_risk_probability": float(risk_probability),
        # "credit_score": credit_score,
        "message": "Prediction successful"
    }
