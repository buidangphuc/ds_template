# Data Science Project Template

This repository contains a template for building data science projects with standardized structure and workflow.

## Requirements

- Docker and Docker Compose
- Python 3.12+
- Poetry (Python dependency management tool)
- Common DS libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter

## Repository Structure

```plaintext
project/
│
├── artifacts/
│   ├── data_ingestion/        # Stores raw input data collected from various sources.
│   ├── data_transformation/    # Contains scripts and modules for data processing, e.g., normalization or transformations.
│   ├── data_validation/        # Stores the results of data validation, ensuring data quality and consistency.
│   └── model_evaluation/       # Contains evaluation results of models, including performance metrics and charts.
│   └── model_trainer/          # Stores trained models, weights, and information related to the training process.
│
├── config/
│   ├── config.yaml             # Configuration file containing project parameters such as file paths and settings.
│   ├── params.yaml             # Configuration for training and preprocessing parameters.
│   └── schema.yaml             # Describes the schema of the input data and any validation rules.
│
├── research/
│   ├── 1_data_ingestion.ipynb  # Jupyter notebook for collecting and preprocessing input data.
│   ├── 2_data_validation.ipynb # Jupyter notebook for data validation and quality checks.
│   ├── 3_data_transformation.ipynb # Jupyter notebook for transforming the data into a usable format for the model.
│   ├── 4_model_trainer.ipynb   # Jupyter notebook for training models using the processed data.
│   └── 5_model_evaluation.ipynb # Jupyter notebook for evaluating the model’s performance.
│
├── scripts/
│
├── src/
│   └── datascience/            # Source code for the data science pipeline.
│       ├── components/         # Individual modules that represent parts of the data science pipeline (e.g., feature engineering, model evaluation).
│       ├── config/             # Configuration files for pipeline setup.
│       ├── constants/          # Contains constant values or parameters used throughout the pipeline.
│       ├── entity/             # Defines the data entities used in the model (e.g., data schemas, models).
│       ├── pipeline/           # Main pipeline for data ingestion, transformation, and model training.
│       └── utils/              # Utility functions or scripts to support various parts of the project.
│
├── templates/              # API View for testing
├── .gitignore              # Git ignore file to exclude certain files and directories from version control.
├── app.py                  # Main application file for running the project.
├── main.py                 # Entry point to the application or main logic of the project.
├── README.md               # Project documentation explaining the setup, usage, and purpose.
├── requirements.txt        # A list of dependencies required to run the project.
```

## Running the Application

### Using Docker Compose (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Start the development environment:
```bash
docker-compose -f docker-compose.local.yml up -d
```

This will start all necessary services (Jupyter, database, etc.) in development mode.

3. Access the services:
   - Jupyter Lab: http://localhost:8888
   - API: http://localhost:8000
   - MLflow UI (if configured): http://localhost:5000

4. Stop the services:
```bash
docker-compose -f docker-compose.local.yml down
```

### Manual Setup

1. Install Poetry:
```bash
pip install poetry
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Start Jupyter Lab:
```bash
poetry run jupyter lab
```

### Environment Variables

Key environment variables include:

- `MODEL_REGISTRY`: Path to model registry
- `MLFLOW_TRACKING_URI`: URI for MLflow tracking server
