from openai import OpenAI

client = OpenAI()
import time

# JSONL training file path
jsonl_file_path = "toyota_vehicle_details.jsonl"  # Replace with your JSONL file

# Step 1: Upload the training file
def upload_training_file(file_path):
    try:
        print("Uploading training file...")
        with open(file_path, "rb") as file:
            response = client.files.create(file=file, purpose="fine-tune")
        print(f"Training file uploaded successfully. File ID: {response.id}")
        return response.id
    except Exception as e:
        print(f"Error during file upload: {e}")
        return None

# Step 2: Create a fine-tuning job
def create_fine_tune_job(file_id, model="gpt-3.5-turbo-1106"):
    try:
        print("Creating fine-tuning job...")
        response = client.fine_tuning.jobs.create(training_file=file_id,
        model=model)
        print(f"Fine-tuning job created successfully. Job ID: {response.id}")
        return response.id
    except Exception as e:
        print(f"Error during fine-tuning job creation: {e}")
        return None

# Step 3: Monitor the fine-tuning job
def monitor_fine_tuning(job_id):
    print("Monitoring fine-tuning job...")
    try:
        while True:
            response = client.fine_tuning.jobs.retrieve(job_id)
            status = response.status
            print(f"Job Status: {status}")
            if status in ["succeeded", "failed"]:
                return response
            time.sleep(10)  # Wait 10 seconds before checking again
    except Exception as e:
        print(f"Error monitoring fine-tuning job: {e}")
        return None

# Step 4: Use the fine-tuned model
def use_fine_tuned_model(model_name):
    try:
        print(f"Using fine-tuned model: {model_name}")
        response = client.chat.completions.create(model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the details of the 2022 Toyota Camry?"}
        ])
        print("Response from fine-tuned model:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error using fine-tuned model: {e}")

# Main Execution
def main():
    # Upload the training file
    file_id = upload_training_file(jsonl_file_path)
    if not file_id:
        return

    # Create the fine-tuning job
    job_id = create_fine_tune_job(file_id)
    if not job_id:
        return

    # Monitor the fine-tuning job
    result = monitor_fine_tuning(job_id)
    if result and result["status"] == "succeeded":
        fine_tuned_model = result["fine_tuned_model"]
        # Use the fine-tuned model
        use_fine_tuned_model(fine_tuned_model)
    else:
        print("Fine-tuning job failed or did not succeed.")

if __name__ == "__main__":
    main()
