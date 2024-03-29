import argparse

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="path to output video file")


def record_video():
    args = vars(ap.parse_args())

    print('File: ', args['file'])

    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(args['file'],
                          fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = vars(ap.parse_args())
    record_video(args)
