import os
import face_recognition
import pickle

DATASET_DIR = 'faces'
ENCODINGS_PATH = 'encodings.pkl'


def train_faces():
    if not os.path.exists(DATASET_DIR):
        print('❌ Run capture_faces.py first')
        return

    known_encodings = []
    known_names = []

    persons = [p for p in os.listdir(DATASET_DIR)
               if os.path.isdir(os.path.join(DATASET_DIR, p))]

    if not persons:
        print('❌ No data found')
        return

    print("🔄 Training...\n")

    for person_name in persons:
        person_dir = os.path.join(DATASET_DIR, person_name)
        images = [f for f in os.listdir(person_dir)
                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        for img_name in images:
            img_path = os.path.join(person_dir, img_name)

            try:
                image = face_recognition.load_image_file(img_path)
                face_locations = face_recognition.face_locations(image)

                if len(face_locations) == 0:
                    continue

                encoding = face_recognition.face_encodings(image, face_locations)[0]
                known_encodings.append(encoding)
                known_names.append(person_name)

            except:
                continue

    data = {'encodings': known_encodings, 'names': known_names}

    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(data, f)

    print("✅ Training complete!")


if __name__ == '__main__':
    train_faces()