import cv2

faceCascade = cv2.CascadeClassifier('C:\Python27\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
image = cv2.imread('C:\Users\Travel_Express\Desktop\p.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
)

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
