import cv2
import numpy as np
import smtplib
import playsound
import threading

Alarm_Status = False
Email_Status = False
Fire_Reported = 0
Stop_Alarm = False  # Control flag for stopping the alarm


def play_alarm_sound_function():
    global Stop_Alarm
    while not Stop_Alarm:
        playsound.playsound(r"./alarm-sound.mp3", True)


def send_mail_function():
    recipientEmail = "harshsaini00025@gmail.com"
    sender_email = "sainiharsh1704@gmail.com"
    app_password = "bxxe dzty xjrx woqu"  # Replace with your actual app password.

    subject = "Fire Alert"
    body = "Warning: A Fire Accident has been reported at Your Company/Home.\n\nPlease take immediate action!"
    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipientEmail, message)
        print(f"Email sent to {recipientEmail}")
        server.close()
    except Exception as e:
        print(f"Email Error: {e}")


video = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path.

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        print("No frame captured.")
        break

    frame = cv2.resize(frame, (960, 540))
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Fire color range
    lower = np.array([18, 50, 50], dtype="uint8")  # Adjust based on fire hues
    upper = np.array([35, 255, 255], dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask=mask)

    # Contour detection for fire-like shapes
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    fire_detected = False  # Reset flag for each frame

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 5000:  # Fire threshold by area size
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Fire Detected!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            fire_detected = True

    cv2.imshow("Output", frame)

    if fire_detected:
        Fire_Reported += 1
        if not Alarm_Status:
            Stop_Alarm = False
            threading.Thread(target=play_alarm_sound_function).start()
            Alarm_Status = True

        if not Email_Status:
            threading.Thread(target=send_mail_function).start()
            Email_Status = True
    else:
        Fire_Reported = 0
        if Alarm_Status:
            Stop_Alarm = True
            Alarm_Status = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        Stop_Alarm = True
        break

cv2.destroyAllWindows()
video.release()
