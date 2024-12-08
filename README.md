# FastAPI Project

This project is a FastAPI application that requires a pre-trained Random Forest model to function. The model file, `random_forest_model.joblib`, can be generated using the training data code available in the same Git repository.

## Setup

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

  ```bash
  .\venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Ensure the `random_forest_model.joblib` file is in the models directory. If not, generate it using the training data code in the repository.

## Running the Application

1. Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Additional Information

- The service to generate `random_forest_model.joblib` is available at `https://github.com/raulhenrique-x3/random-forest-youtube-prediction`.
- For more details on how to generate the `random_forest_model.joblib` file, refer to the training data code in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
