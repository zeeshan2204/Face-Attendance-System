import cv2
import face_recognition
import numpy as np
import pandas as pd
import os
import pickle
from datetime import datetime

ENCODINGS_PATH = 'encodings.pkl'
ATTENDANCE_CSV = 'attendance.csv'


def load_encodings():
    if not os.path.exists(ENCODINGS_PATH):
        print('❌ Run trainfaces.py first')
        exit()

    with open(ENCODINGS_PATH, 'rb') as f:
        data = pickle.load(f)

    return data['encodings'], data['names']


def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')

    if os.path.exists(ATTENDANCE_CSV):
        df = pd.read_csv(ATTENDANCE_CSV)
    else:
        df = pd.DataFrame(columns=['Name', 'Date', 'Time', 'Status'])

    if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
        new_row = pd.DataFrame([[name, date_str, time_str, 'Present']],
                               columns=['Name', 'Date', 'Time', 'Status'])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(ATTENDANCE_CSV, index=False)
        print(f"✅ Marked: {name}")


def main():
    known_encodings, known_names = load_encodings()

    cap = cv2.VideoCapture(0)
    recently_marked = {}
    COOLDOWN_SECONDS = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        locs = face_recognition.face_locations(rgb)
        encs = face_recognition.face_encodings(rgb, locs)

        for (top, right, bottom, left), enc in zip(locs, encs):
            top *= 2; right *= 2; bottom *= 2; left *= 2

            name = "Unknown"
            color = (0, 0, 255)

            distances = face_recognition.face_distance(known_encodings, enc)
            if len(distances) > 0:
                best = np.argmin(distances)

                if distances[best] < 0.6:
                    name = known_names[best]
                    color = (0, 255, 0)

                    now = datetime.now()
                    last = recently_marked.get(name)

                    if last is None or (now - last).total_seconds() > COOLDOWN_SECONDS:
                        mark_attendance(name)
                        recently_marked[name] = now

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()