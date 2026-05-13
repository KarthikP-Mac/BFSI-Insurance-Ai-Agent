#!/bin/bash
# Start the backend API
uvicorn backend.api.main:app --host 0.0.0.0 --port 8000 &
API_PID=$!

# Wait a moment for the backend to start
sleep 2

# Start the Streamlit UI
streamlit run ui/app.py --server.port 8501 --server.address 0.0.0.0 &
UI_PID=$!

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
