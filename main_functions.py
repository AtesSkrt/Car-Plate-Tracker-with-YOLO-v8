import cv2
import torch  # PyTorch for GPU acceleration (optional for image processing)
from ultralytics import YOLO  # YOLO object detection model
import easyocr  # EasyOCR for license plate recognition
import string
from functions import plate_complies_format, read_plate, check_user_login, add_penalty
import logging  # For logging events
from datetime import datetime  # For handling date and time
import logging

from gui_son_main import Ui_MainWindow
from login_page import Ui_Form
import resources_rc_2
import login_rc
import pyodbc
from pyodbc import connect
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from camera_deneme import Ui_MainWindow2
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtGui import QImage, QPixmap
#from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#    QFont, QFontDatabase, QGradient, QIcon,
#    QImage, QKeySequence, QLinearGradient, QPainter,
#    QPalette, QPixmap, QRadialGradient, QTransform)
import PySide6
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QMessageBox)


server = 'DESKTOP-EIPQ2PJ'
database = 'gate_system'
driver = '{SQL Server}'
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};"




class LoginWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Car Tracker")

        # Connect the button's clicked signal to the open_main_window method
        self.pushButton_2.clicked.connect(self.check_user)  # Assuming pushButton_2 is the button name

        # Show the login window (this might be done automatically by the UI loader)
        self.show()

    def check_user(self):
        try:
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            # Connect to the database
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()

                # Execute the SQL query to check user credentials
                cursor.execute("SELECT * FROM user_data WHERE user_name = ? AND user_password = ?", (username, password))
                result = cursor.fetchone()

                if result:  # User found
                    is_admin = result[1] == "admin"  # Check if username is "admin"
                    self.current_user = username
                    self.open_main_window(username, is_admin)  # Pass username and admin status
                else:
                    QMessageBox.warning(self, "Invalid Login", "The username or password is incorrect.")
        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", f"An error occurred while connecting to the database: {ex}")


    def open_main_window(self, username, is_admin):
        # Create an instance of your main window class
        self.main_window = GuiSon(username, is_admin)  # Pass username as an argument

        # Close the current login window
        self.close()

        # Show the main window
        self.main_window.show()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get formatted current time
        logging.info("User '%s' successfully logged in at %s.", username, current_time)
class GuiSon(QMainWindow, Ui_MainWindow):
    current_user = None

    def __init__(self, username, is_admin=False):
        super().__init__()
        self.process_frame_signal = pyqtSignal()  # Use pyqtSignal
        self.setupUi(self)
        self.setWindowTitle("Car Tracker")

        # Initialize camera capture (called once)
        self.cap = cv2.VideoCapture(0)

        self.widget.setHidden(True)
        self.is_admin = is_admin  # Flag to track admin status

        self.current_user.setText(f"{username}".upper())

        self.watc_screen_sidebar_opened.clicked.connect(self.swich_to_watch_screen)
        self.watc_screen_sidebar_closed.clicked.connect(self.swich_to_watch_screen)

        self.add_penalty_sidebar_closed_2.clicked.connect(self.swich_to_add_penalty)
        self.add_penalty_sidebar_closed.clicked.connect(self.swich_to_add_penalty)

        self.inspect_database_sidebar_closed_2.clicked.connect(self.swich_to_inpect_database)
        self.inspect_database_sidebar_closed.clicked.connect(self.swich_to_inpect_database)

        self.staff_operations_sidebar_opened.clicked.connect(self.swich_to_staff_actions)
        self.staff_operations_sidebar_closed.clicked.connect(self.swich_to_staff_actions)


        self.logout_sidebar_opened.clicked.connect(self.open_login_window)
        self.logout_sidebar_closed.clicked.connect(self.open_login_window)

        self.add_staff_button.clicked.connect(self.add_staff_user)
        self.delete_staff_button.clicked.connect(self.delete_staff_user)

        self.update_staff_table()
        self.add_penalty_button.clicked.connect(self.add_penalty)

        self.show_and_search_penalties()

        self.pushButton.clicked.connect(self.delete_penalty)
        self.pushButton_2.clicked.connect(self.refresh_table)
        self.start_camera_button.clicked.connect(self.start_camera)
        self.read_plate_button.clicked.connect(self.check_button_state)  # Connect button toggle to function

        self.add_penalty_button_2.clicked.connect(self.set_plate_and_switch_screen)

        logging.basicConfig(filename='car_tracker.log', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def set_plate_and_switch_screen(self):

        selected_row = self.database_table.currentRow()
        if selected_row >= 0:
            selected_plate = self.database_table.item(selected_row, 0).text()
            self.penalty_plate_input.setText(selected_plate)
            self.stackedWidget.setCurrentIndex(1)  # Switch to Add Penalty screen
        else:
            QMessageBox.warning(self, "No Plate Selected", "Please select a plate number from the table.")


    def check_button_state(self):
        """
        Checks the state of the "Read Plate" button and triggers frame processing if clicked.
        """
        if self.read_plate_button.isChecked():
            # Simulate spacebar press to trigger frame processing in watching_screen
            cv2.waitKey(1)




    def start_camera(self):
        """
        Starts the watching screen functionality when the button is clicked.
        """
        try:
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                current_user = self.current_user.text()  # Assuming username is retrieved from current_user

                logging.info("%s started camera at %s.", current_user, current_time)

                # Call the watching_screen function with database connection
                self.watching_screen(cursor, conn)
        except Exception as e:
            logging.error(f"Error during watching screen: {e}")
            # Handle errors appropriately, e.g., display a message box to the user

    def watching_screen(self, cursor, conn):
        model = YOLO("best.pt")

        # Use the existing 'self.cap' instance
        if not self.cap.isOpened():
            logging.error("Error: Could not open camera.")
            return

        while True:
            ret, frame = self.cap.read()

            if not ret:
                logging.error("Error: Could not read frame.")

            cv2.imshow('Press Space to Take Image or Click "Read Plate" Button', frame)

            # Capture image on spacebar press OR read_plate_button click
            key = cv2.waitKey(1)
            if key == 32 or self.read_plate_button.isChecked():  # Spacebar key code or button click
                try:
                    # Process the current frame
                    detections = model(frame)[0]
                    detections_ = []
                    try:
                        for i in range(5):
                            # Extract detection coordinates
                            detection = detections.boxes.data.tolist()[i]
                            x1, y1, x2, y2, score, class_id = detection
                            if class_id == 0:  # Assuming plate class index is 0 in YOLO model
                                print("Plate detected")
                                break
                    except:
                        print("No plate detected.")

                    try:
                        # Crop the detected plate region
                        plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
                    except:
                        print("No detections")
                        continue

                    # Preprocess for OCR (optional)
                    try:
                        plate_crop_gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGRA2GRAY)

                        # Apply adaptive thresholding
                        plate_crop_thresh = cv2.adaptiveThreshold(plate_crop_gray, 255,
                                                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                                                  cv2.THRESH_BINARY_INV, 11, 2)

                        # Function to calculate resized dimensions while maintaining aspect ratio
                        def get_resized_dimensions(image, max_width, max_height):
                            height, width = image.shape[:2]
                            ratio_w = max_width / float(width)
                            ratio_h = max_height / float(height)
                            ratio = min(ratio_w, ratio_h)
                            new_width = int(width * ratio)
                            new_height = int(height * ratio)
                            return new_width, new_height

                        # Resize images with aspect ratio preservation
                        new_width, new_height = get_resized_dimensions(plate_crop, 640,
                                                                       480)  # Adjust max dimensions as needed
                        plate_crop_resized = cv2.resize(plate_crop, (new_width, new_height),
                                                        interpolation=cv2.INTER_AREA)
                        plate_crop_thresh_resized = cv2.resize(plate_crop_thresh, (new_width, new_height),
                                                               interpolation=cv2.INTER_AREA)

                        # Display resized images in separate windows
                        cv2.namedWindow('Original Cropped Image', cv2.WINDOW_NORMAL)
                        cv2.imshow('Original Cropped Image', plate_crop_resized)

                        cv2.namedWindow('Thresholded Cropped Image', cv2.WINDOW_NORMAL)
                        cv2.imshow('Thresholded Cropped Image', plate_crop_thresh_resized)
                    except:
                        print("error post processing cropped plate.")

                    plate_text, plate_score = read_plate(plate_crop)
                    if plate_text is not None:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        current_user = self.current_user.text()
                        # Check if plate exists in database
                        cursor.execute("SELECT penalty_amount, status FROM plates_penalties WHERE plate_number = ?",
                                       (plate_text,))
                        row = cursor.fetchone()

                        if row:
                            penalty_amount, status = row
                            info_text = f"Plate: {plate_text}, Penalty: {penalty_amount}"

                            if penalty_amount < 100 and status == 'active':
                                info_text += ", Status: Allowed"
                                logging.info("%s read plate number %s at %s. Status: Allowed",
                                             current_user, plate_text, current_time)
                            else:
                                info_text += ", Status: Restricted"
                                logging.info("%s read plate number %s at %s. Status: Restricted",
                                             current_user, plate_text, current_time)

                        else:
                            # Add new plate to database
                            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            cursor.execute("""
                                                                INSERT INTO plates_penalties (plate_number, added_date, penalty_amount, status)
                                                                VALUES (?, ?, 0, 'active')
                                                                """, (plate_text, current_date))
                            conn.commit()
                            info_text = f"Plate: {plate_text}, Penalty: 0, Status: Allowed"

                            logging.info("%s read plate number %s at %s. New plate added to database.",
                                         current_user, plate_text, current_time)

                        self.watch_screen_info_label.setText(info_text)

                except Exception as e:  # Catch any exception
                    print("Error while pressing space or button:", e)

    def refresh_table(self):
        """Refreshes the database_table with the latest data from the plates_penalties table."""

        try:
            self.show_and_search_penalties()  # Refetch and display data
            QMessageBox.information(self, "Success", "Table refreshed successfully.")
        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", str(ex))

    def show_and_search_penalties(self):
        """Shows all data from the plates_penalties table in the database_table
           and highlights matching rows based on user search input."""

        try:
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT plate_number, penalty_amount, added_date, status FROM plates_penalties")
                rows = cursor.fetchall()

                self.database_table.setRowCount(0)  # Clear any existing data
                self.database_table.setColumnCount(4)  # Set column count for headers (including status)
                self.database_table.setHorizontalHeaderLabels(["Plate Number", "Penalty", "Creation Date", "Status"])

                for row_number, row_data in enumerate(rows):
                    self.database_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        self.database_table.setItem(row_number, column_number, item)

                # Connect the search button signal
                self.database_search_button.clicked.connect(self.search_penalties)

                self.previously_highlighted_items = []

        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", str(ex))

    def delete_penalty(self):
        """Deletes the selected penalty from the database_table. Updates the database table's
           status to 'inactive' instead of removing the entire row. If a specific cell (penalty amount)
           is selected, set penalty to 0 instead of deleting the entire row.
        """

        selected_row = self.database_table.currentRow()
        if selected_row >= 0:
            plate_number = self.database_table.item(selected_row, 0).text()
            penalty_amount_before = self.database_table.item(selected_row, 1).text()

            try:
                with pyodbc.connect(connection_string) as conn:
                    cursor = conn.cursor()

                    selected_column = self.database_table.currentColumn()
                    if selected_column == 1:  # Penalty amount column
                        cursor.execute("UPDATE plates_penalties SET penalty_amount = 0 WHERE plate_number = ?",
                                       plate_number)
                        conn.commit()
                        self.database_table.item(selected_row, 1).setText("0")

                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        current_user = self.current_user.text()  # Assuming username is retrieved from current_user
                        logging.info("%s set penalty for plate number %s to 0 at %s. Previous amount: %s",
                                     current_user, plate_number, current_time, penalty_amount_before)

                    else:
                        # Update status to 'inactive' instead of deleting
                        cursor.execute("UPDATE plates_penalties SET status = 'inactive' WHERE plate_number = ?",
                                       plate_number)
                        conn.commit()

                        # Update status in the table
                        self.database_table.item(selected_row, 3).setText("inactive")

                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        current_user = self.current_user.text()
                        logging.info("Plate number %s marked inactive by %s at %s.",
                                     plate_number, current_user,current_time)

                    QMessageBox.information(self, "Success", "Penalty updated successfully.")
            except pyodbc.Error as ex:
                QMessageBox.critical(self, "Database Error", str(ex))
        else:
            QMessageBox.warning(self, "No Penalty Selected", "Please select a penalty to delete.")

    def search_penalties(self):
        search_text = self.database_search_bar.text()
        for row in range(self.database_table.rowCount()):
            for column in range(self.database_table.columnCount()):
                item = self.database_table.item(row, column)
                if item:  # Check if item exists
                    item.setBackground(QColor(255, 255, 255))

        # Reset previously highlighted items **before** the new search
        for item in self.previously_highlighted_items:
            item.setBackground(self.database_table.palette().base().color())
        self.previously_highlighted_items = []  # Clear the list for new items

        for row in range(self.database_table.rowCount()):
            for column in range(self.database_table.columnCount()):
                item = self.database_table.item(row, column)
                if item and search_text.lower() in item.text().lower():
                    # Highlight matching item
                    item.setBackground(QColor(255, 255, 153))  # Adjust highlight color as needed
                    self.previously_highlighted_items.append(item)  # Store for the next reset
                else:
                    # Reset previously highlighted items
                    if item in self.previously_highlighted_items:
                        item.setBackground(self.database_table.palette().base().color())  # Restore default background

        self.previously_highlighted_items = []  # Clear for the next search

    def add_penalty(self):
        plate_number = self.penalty_plate_input.text()
        penalty_amount_str = self.penalty_amount_input.text()
        penalty_reason = self.lineEdit.text()

        try:
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()

                # Check for existing plate number
                cursor.execute("SELECT * FROM plates_penalties WHERE plate_number = ?", plate_number)
                existing_penalty = cursor.fetchone()

                if existing_penalty:  # Plate exists, update penalty
                    current_penalty = existing_penalty[2]  # Access penalty_amount from existing record
                    new_penalty_amount = float(current_penalty) + float(penalty_amount_str)
                    cursor.execute(
                        "UPDATE plates_penalties SET penalty_amount = ? WHERE plate_number = ?",
                        (new_penalty_amount, plate_number))
                    conn.commit()
                    self.add_penalty_info.setText(
                        f"Plate: {plate_number}, Added: {penalty_amount_str}, Current Penalty: {new_penalty_amount}"
                    )

                    # Log info message for adding penalty
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    current_user = self.current_user.text()  # Assuming username is retrieved from lineEdit
                    logging.info("%s added %s penalty points to plate number %s at %s. Reason: %s",
                                 current_user, penalty_amount_str, plate_number, current_time, penalty_reason)

                else:  # Plate doesn't exist, insert new record
                    current_date = datetime.now()
                    formatted_date_time = current_date.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute(
                        "INSERT INTO plates_penalties (plate_number, penalty_amount, added_date, status) VALUES (?, ?, ?, ?)",
                        (plate_number, penalty_amount_str, formatted_date_time, 'active'))
                    conn.commit()

                    # Ensure info message is updated after successful insertion

                    self.add_penalty_info.setText(
                        f"New Plate: {plate_number}, Added: {penalty_amount_str}, Current Penalty: {penalty_amount_str}"
                    )
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    current_user = self.current_user.text()  # Assuming username is retrieved from lineEdit
                    # Log info message for creating new penalty record
                    logging.info("%s added new plate %s with %s penalty points at %s. Reason: %s",
                                 current_user, plate_number, penalty_amount_str, current_time, penalty_reason)

        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", str(ex))

    def open_login_window(self):
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()
            print("Camera closed.")
            self.main_window = LoginWindow()
            self.close()
            self.main_window.show()

            username = self.current_user.text()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info("User '%s' logged out at %s.", username, current_time)
    def swich_to_watch_screen(self):
        self.stackedWidget.setCurrentIndex(2)

    def swich_to_add_penalty(self):
        self.stackedWidget.setCurrentIndex(1)

    def swich_to_inpect_database(self):
        self.stackedWidget.setCurrentIndex(0)

    def swich_to_staff_actions(self):
        # Only allow access if admin
        if self.is_admin:
            self.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.warning(self, "Restricted Access", "You don't have permission to access staff management.")

    def add_staff_user(self):
        username = self.staff_name_input.text()
        password = self.staff_password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Missing Information", "Please fill in both username and password.")
            return

        try:
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()

                # Log info message before database operation
                from datetime import datetime
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                current_user = self.current_user.text()  # Assuming username is retrieved from lineEdit
                logging.info("User '%s' added new staff named '%s' at %s.", current_user, username, current_time)

                # Insert staff user data
                cursor.execute(
                    "INSERT INTO user_data (user_name, user_password, status, creation_date) VALUES (?, ?, 'active', GETDATE())",
                    (username, password))
                conn.commit()
                QMessageBox.information(self, "Success", "New user added successfully.")
                self.update_staff_table()
                self.staff_name_input.setText("")
                self.staff_password_input.setText("")
        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", str(ex))

    def update_staff_table(self):
        try:
            with pyodbc.connect(connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT user_id, user_name, user_password, status FROM user_data")
                rows = cursor.fetchall()

                self.staff_table.setRowCount(0)
                for row_number, row_data in enumerate(rows):
                    self.staff_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.staff_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except pyodbc.Error as ex:
            QMessageBox.critical(self, "Database Error", str(ex))

    def delete_staff_user(self):
        selected_row = self.staff_table.currentRow()
        if selected_row >= 0:
            try:
                with pyodbc.connect(connection_string) as conn:
                    cursor = conn.cursor()
                    user_id = self.staff_table.item(selected_row, 0).text()

                    # Get staff username before deactivating (assuming username is in another column)
                    username = self.staff_table.item(selected_row,1).text()  # Modify based on column index for username

                    # Log info message before database operation
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    current_user = self.current_user.text()  # Assuming username is retrieved from lineEdit
                    logging.info("User '%s' deactivated staff named '%s' at %s.", current_user, username, current_time)

                    # Update user status to inactive
                    cursor.execute("UPDATE user_data SET status = 'inactive' WHERE user_id = ?", user_id)
                    conn.commit()
                    QMessageBox.information(self, "Success", "User status changed to inactive.")
                    self.update_staff_table()
            except pyodbc.Error as ex:
                QMessageBox.critical(self, "Database Error", str(ex))
        else:
            QMessageBox.warning(self, "No User Selected", "Please select a user to delete.")