import argparse

import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="path to input video file")


def play_video(args):
    print('File: ', args['file'])

    cap = cv2.VideoCapture(args['file'])

    while (cap.isOpened()):
        ret, frame = cap.read()

        try:
            cv2.imshow('frame', frame)
        except:
            pass

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = vars(ap.parse_args())
    play_video(args)
