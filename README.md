## How to Run the Project

### Prerequisites
- Python 3.13.2 installed on your system.
- `uv` package installed globally. You can install it using:
  ```bash
  pip install uv
  ```

### Setup Instructions
1. **Initialize the Virtual Environment**:
   ```bash
   uv venv .venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install Project Dependencies**:
   ```bash
   uv sync
   ```

### Running the Project
To start the application, use the following command:
```bash
fastapi dev main.py
```
This will start the development server, and you can access the application at `http://127.0.0.1:8000`.

### Environment Variables
Ensure you have all necessary environment variables configured. The project requires the following environment variables:

- `SUPABASE_URL`: The URL of your Supabase instance.
- `SUPABASE_PUBLISHABLE_KEY`: The public key for accessing Supabase.
- `SUPABASE_SECRET_KEY`: The secret key for accessing Supabase.