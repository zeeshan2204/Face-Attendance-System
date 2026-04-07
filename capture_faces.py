import cv2
import os

DATASET_DIR = 'faces'


def capture_faces():
    if not os.path.exists(DATASET_DIR):
        os.makedirs(DATASET_DIR)

    name = input('Enter the name of the person: ').strip()
    if not name:
        print('❌ Name cannot be empty.')
        return

    person_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(person_dir, exist_ok=True)

    existing = len([f for f in os.listdir(person_dir) if f.endswith('.jpg')])
    print(f"📁 Existing images for {name}: {existing}")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('❌ Could not open camera.')
        return

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    count = 0
    print("📸 Press SPACE to capture | Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Capture Faces', frame)
        key = cv2.waitKey(1)

        if key % 256 == 32:  # SPACE
            if len(faces) == 0:
                print('⚠️ No face detected')
            else:
                for (x, y, w, h) in faces:
                    face_img = frame[y:y+h, x:x+w]
                    img_name = os.path.join(person_dir, f"{name}_{existing + count + 1}.jpg")
                    cv2.imwrite(img_name, face_img)
                    print(f"✅ Saved: {img_name}")
                    count += 1

        elif key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ Done! Captured: {count}")


if __name__ == '__main__':
    capture_faces()