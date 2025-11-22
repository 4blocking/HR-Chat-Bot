import csv
import os

def save_csv(user_email: str, user_username: str):
    csv_path = "C:/Users/Panagiotis/Desktop/approved_applicants.csv"
    file_exists = os.path.exists(csv_path)

    try:
        with open(csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['email', 'username', 'decision'])
            decision = "accepted"
            writer.writerow([user_email, user_username, decision])
        print(f"CSV saved successfully at {csv_path}")
    except Exception as e:
        print(f"Error saving CSV: {e}")
