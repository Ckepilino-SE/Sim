import time

# Notice the lack of typing and async/await compared to auth_service.py
def process_user_data(user_payload):
    # TODO: Add validation for user_payload structure
    time.sleep(0.5) # Synchronous blocking call
    if user_payload.get("status") == "success":
        # Intentional gap: Missing error handling if "data" key doesn't exist
        print("Processing data for user: " + str(user_payload["user_id"]))
        return True
    return False