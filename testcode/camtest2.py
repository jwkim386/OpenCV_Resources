import numpy as np
import cv2
import time
import jetson.utils

import argparse
import sys


# parse command line
parser = argparse.ArgumentParser(description="View various types of video streams", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv)

n = 1
# capture frames until user exits
while output.IsStreaming():
  st = time.perf_counter()
  image = input.Capture()
  #print(image)
  output.Render(image)
  print(n, ' = ', time.perf_counter() - st, "Video Viewer | {:d}x{:d} | {:.1f} FPS".format(image.width, image.height, output.GetFrameRate()))
  time.sleep(0.03)
  n = n+1
