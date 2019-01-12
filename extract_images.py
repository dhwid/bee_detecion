import cv2
import os

WRITE_FRAME_STEP = 30 * 5  # 30 FRAMES PER SECOND


def extract_video(filepath, filename):
  filename = filename.split('.')[0]
  vidcap = cv2.VideoCapture(filepath)
  success, image = vidcap.read()
  count = 0
  while success:
    left = image[0:1080, 0:1080]
    right = image[0:1080, 1920 - 1080:1920]
    left = cv2.resize(left, (416, 416))
    right = cv2.resize(right, (416, 416))

    cv2.imwrite("dataset/%s_%dframes_%d_left.jpg" % (filename, WRITE_FRAME_STEP, count), left)  # save frame as JPEG file
    cv2.imwrite("dataset/%s_%dframes_%d_right.jpg" % (filename, WRITE_FRAME_STEP, count), right)  # save frame as JPEG file

    for _ in range(1, WRITE_FRAME_STEP):
      success, image = vidcap.read()

    count += 1


for file in os.listdir("videos"):
      print(file + ' is processing..')
      extract_video(os.path.join("videos", file), file)


