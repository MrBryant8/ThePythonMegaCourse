import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img=cv2.imread("photo.jpg")
img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img,
                                      scaleFactor=1.1,
                                      minNeighbors=7)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 137, 182), 3)

print(type(faces))
print(faces)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
