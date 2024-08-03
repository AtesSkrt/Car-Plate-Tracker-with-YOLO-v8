import string
import easyocr
import torch
from ultralytics import YOLO
import cv2
import datetime
#if __name__ == '__deneme__':
#model = YOLO("best.pt")
#results = model.predict(source="0", show=True)

reader = easyocr.Reader(['en'], gpu = False)
dict_char_to_int = {'O':'0',
                    'I':'1',
                    'J':'3',
                    'A':'4',
                    'G':'6',
                    's':'5'}
dict_int_to_char = {'0':'O',
                    '1':'I',
                    '3':'J',
                    '4':'A',
                    '6':'G',
                    '5':'S'}


def plate_complies_format(text):
    try:
        if len(text)<6 and len(text)>8:
            return False
        if      (text[0] in ['0','1','2','3','4','5','6','7','8','9'] or text[0] in dict_char_to_int.keys()) and \
            (text[1] in ['0','1','2','3','4','5','6','7','8','9'] or text[1] in dict_char_to_int.keys()) and \
            (text[-1] in ['0','1','2','3','4','5','6','7','8','9'] or text[1] in dict_char_to_int.keys()) and \
            (text[-2] in ['0','1','2','3','4','5','6','7','8','9'] or text[1] in dict_char_to_int.keys()) and \
            (text[2] in string.ascii_uppercase or text[2] in dict_int_to_char.keys()):
            return True
        else:
            return False
    except:
        print("a")
def format_plate(text):
    formatted = text



def read_plate(plate_crop):
    detections = reader.readtext(plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')
        if plate_complies_format(text):
            return text, score
    return None, None

def check_user_login(conn, cursor, user_name, user_password):
    cursor.execute("SELECT COUNT(*) FROM user_data WHERE user_name = ? AND user_password = ?",
                   (user_name, user_password))
    user_count = cursor.fetchone()[0]

    # Return True if a user is found, False otherwise
    return user_count > 0

def add_penalty(conn, cursor, plate_number, penalty_description, penalty_amount):
    # Get current penalty information (if any)
    cursor.execute("SELECT penalty_description, penalty_amount FROM plates_penalties WHERE plate_number = ?",
                   (plate_number,))
    existing_data = cursor.fetchone()
    while True:
        if existing_data:
            # Plate number exists, update information
            current_description, current_amount = existing_data

            # Handle potential None values for current_description and current_amount
            updated_description = (current_description or "") + "\n" + penalty_description  # Use empty string if None
            updated_amount = (current_amount or 0) + penalty_amount  # Use 0 if None

            # Get current date
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')

            # Update penalty details
            update_penalty_sql = """
             UPDATE plates_penalties
             SET penalty_description = ?, penalty_amount = ?, penalty_date = ?
             WHERE plate_number = ?
           """
            cursor.execute(update_penalty_sql, (updated_description, updated_amount, current_date, plate_number))
            conn.commit()

            print(f"Penalty for plate number {plate_number} updated successfully.")
            break
        else:
            print(f"Plate number {plate_number} not found in the database.")
