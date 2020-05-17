# press space to capture the image and esc to escape and get the image
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to get frame")
        break
    cv2.imshow("test", frame)

    D = cv2.waitKey(1)
    if D%256 == 27:
        print("closing...")
        break
    elif D%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# Displaying image in desktop

y= cv2.imread(img_name,)
cv2.imshow('name',y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# displaying image pixel in array
image = cv2.imread(img_name,)
pixel= image[200, 550]
print(pixel)