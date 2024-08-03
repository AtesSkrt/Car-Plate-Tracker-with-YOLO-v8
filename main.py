#THIS IS NOT THE MAIN "MAIN" FILE. THE REAL MAIN IS  main_gui.py. This file the trial of camera functions.




import torch  # PyTorch for GPU acceleration (optional for image processing)
from ultralytics import YOLO  # YOLO object detection model
import cv2  # OpenCV for camera access and frame manipulation
import easyocr  # EasyOCR for license plate recognition
import string
from functions import plate_complies_format, read_plate, check_user_login, add_penalty
import logging  # For logging events
import pyodbc  # For connecting to Microsoft SQL Server database
from datetime import datetime  # For handling date and time

# SQL server connection details
server = 'DESKTOP-EIPQ2PJ'
database = 'gate_system'
driver = '{SQL Server}'
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};"

# Configure logger
logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == '__main__':
    # Connect to SQL server and create cursor
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # No table creation needed as the code assumes the table exists

    # Load the YOLO model
    model = YOLO("best.pt")


    def watching_screen(cursor, conn):
        """
        Runs the Watching Screen functionality, detecting license plates and adding them to the database.
        """
        # Open camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            logging.error("Error: Could not open camera.")
            return

        while True:
            ret, frame = cap.read()

            if not ret:
                logging.error("Error: Could not read frame.")

            cv2.imshow('Press Space to Take Image', frame)

            # Capture image on spacebar press
            key = cv2.waitKey(1)
            if key == 32:  # Spacebar key code
                detections = model(frame)[0]
                detections_ = []
                try:
                    for i in range(5):
                        # Extract detection coordinates
                        detection = detections.boxes.data.tolist()[i]
                        x1, y1, x2, y2, score, class_id = detection
                        if class_id == 0:  # Assuming plate class index is 0 in YOLO model
                            logging.info("Plate detected")
                            break
                except:
                    logging.info("No plate detected.")

                try:
                    # Crop the detected plate region
                    plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
                except:
                    print("No detections")
                    continue

                # Preprocess for OCR (optional)
                try:
                    plate_crop_gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGRA2GRAY)
                    _, plate_crop_thresh = cv2.threshold(plate_crop_gray, 200, 255, cv2.THRESH_BINARY_INV)

                    cv2.imshow('original_crop', plate_crop)  # Show original crop
                    cv2.imshow('thresholded_crop', plate_crop_thresh)  # Show thresholded crop
                except:
                    logging.error("Error occurred while cropping the plate.")

                # Read license plate using easyocr
                plate_text, plate_score = read_plate(plate_crop)  # Assuming read_plate is defined elsewhere
                print(plate_text)
                if plate_text is not None:
                    print(f"Plate number: {plate_text}  Plate confidence: {score:.2f}")

                    try:
                        # Check if plate exists in the database
                        cursor.execute("SELECT COUNT(*) FROM plates_penalties WHERE plate_number = ?", (plate_text,))
                        row_count = cursor.fetchone()[0]

                        if row_count == 0:
                            # Insert plate into database if it doesn't exist
                            insert_sql = """
                                            INSERT INTO plates_penalties (plate_number, added_date)
                                            VALUES (?, ?)
                                            """
                            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        print("skrt")








    while True:
        # Login section (replace with your preferred method)
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "admin":

            while True:
                main_menu = input("Press:\n"
                                  "1 - Watching Screen\n"
                                  "2 - Enter Penalty\n"
                                  "3 - Read Log\n"
                                  "4 - Read Database\n"
                                  "5 - Personnel Operations\n"
                                  "6 - Log Out\n")
                print(f"Loading {main_menu}..")

                if main_menu == "1":  # Watching Screen
                    # Open camera
                    cap = cv2.VideoCapture(0)
                    if not cap.isOpened():
                        logging.error("Error: Could not open camera.")

                    while True:
                        ret, frame = cap.read()

                        if not ret:
                            logging.error("Error: Could not read frame.")

                        cv2.imshow('Press Space to Take Image', frame)

                        # Capture image on spacebar press
                        key = cv2.waitKey(1)
                        if key == 32:  # Spacebar key code
                            detections = model(frame)[0]
                            detections_ = []
                            try:
                                for i in range(5):
                                    # Extract detection coordinates
                                    detection = detections.boxes.data.tolist()[i]
                                    x1, y1, x2, y2, score, class_id = detection
                                    if class_id == 0:  # Assuming plate class index is 0 in YOLO model
                                        print(detection)
                                        logging.info("Plate detected")
                                        break
                            except:
                                logging.info("No plate detected.")

                            try:
                                # Crop the detected plate region
                                plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
                            except:
                                print("No detections")
                                continue

                            # Preprocess for OCR (optional)
                            try:
                                plate_crop_gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGRA2GRAY)
                                _, plate_crop_thresh = cv2.threshold(plate_crop_gray, 200, 255, cv2.THRESH_BINARY_INV)

                                cv2.imshow('original_crop', plate_crop)  # Show original crop
                                cv2.imshow('thresholded_crop', plate_crop_thresh)  # Show thresholded crop
                            except:
                                logging.error("Error occurred while cropping the plate.")

                            # Read license plate using easyocr
                            plate_text, plate_score = read_plate(plate_crop)

                            if plate_text is not None:
                                logging.info(f"Plate number: {plate_text}  Plate confidence: {score:.2f}")

                                try:
                                    # Check if plate exists in the database
                                    cursor.execute("SELECT COUNT(*) FROM plates_penalties WHERE plate_number = ?", (plate_text,))
                                    row_count = cursor.fetchone()[0]

                                    if row_count == 0:
                                        #eğer plaka database'de yoksa database'e kaydet
                                        insert_sql = """
                                        INSERT INTO plates_penalties (plate_number, added_date)
                                        VALUES (?, ?)
                                        """
                                        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #anlık tarih ve saat
                                        cursor.execute(insert_sql, (plate_text, current_date))
                                        conn.commit()
                                        print(f"Plate number '{plate_text}' added to the table with current date '{current_date}'")
                                    else:
                                        print(f"Plate number '{plate_text}' already exists in the table")

                                except pyodbc.Error as e:
                                    print("Error:", e)


                                print(plate_text)
                        elif key == ord('q'):
                            cap.release()
                            cv2.destroyAllWindows()
                            break

                # Enter Penalty
                elif main_menu == "2":
                    p_number = input("Enter the plate number to add penalty points: \n")
                    p_description = input("Enter penalty description (reason of the penalty): \n")
                    p_amount = int(input("Enter penalty amount: \n"))

                    add_penalty(conn, cursor, p_number, p_description, p_amount)

                elif main_menu == "3": #Read Log
                    print("a")
                elif main_menu == "4": #Read database
                    print("a")
                elif main_menu == "5": #Personel operations
                    print("a")
                elif main_menu == "6": #Log out
                    print("a")
                    break
                else: print("invalid chose!")
        else: print("incorrect username or password!")