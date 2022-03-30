import cv2 as cv
cap = cv.VideoCapture('http://192.168.188.58:4747/video')

while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        print(frame.shape)
        cv.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break