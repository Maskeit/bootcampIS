import mediapipe as mp
import cv2

cap = cv2.VideoCapture(1) #cambiar si no se abre

while True:
    ret, img = cap.read()
    if ret == False:
        break

    H, W, _ = img.shape
    #detect faces
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detection:

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out = face_detection.process(img_rgb)
        if out.detections is not None:
            for detection in out.detections:
                location_data = detection.location_data
                bbox = location_data.relative_bounding_box

                x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                x1 = int(x1 * W)
                y1 = int(y1 * H)
                w = int(w * W)
                h = int(h * H)

                #blur face
                #img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
                ksize = (50,50)
                img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], ksize)
                img[y1:y1 + h, x1:x1 + w, :] = 255 - img[y1:y1 + h, x1:x1 + w, :]
        cv2.imshow("Deteccion de rostro", img)
        if cv2.waitKey(1) == 27:
            break