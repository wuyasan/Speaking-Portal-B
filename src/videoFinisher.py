import argparse
import os.path
import os
import subprocess
import pathlib
from scheduler import frame_schedule
localpath = pathlib.Path(__file__).parent.resolve().parent.resolve()
print("VideoFinisher.py localpath: "+str(localpath))

def emptyFolder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                print()  # shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    try:
        os.rmdir(folder)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (folder, e))

def generate_video(audioPath, textPath):
    frame_schedule(textPath)
    os.system("python videoDrawer.py")

    parser = argparse.ArgumentParser(description='blah')
    parser.add_argument('--input_file', type=str,  help='the script')
    parser.add_argument('--keep_frames', type=str,
                        help='do you want to keep the thousands of frame still images, or delete them?')
    args = parser.parse_args()
    INPUT_FILE = args.input_file
    KEEP_FRAMES = args.keep_frames


    command = "ffmpeg -r 30 -f image2 -s 1920x1080 -i "+str(localpath)+"/generatedVideo/ev_frames/f%06d.png -i "+str(
        audioPath) + " -vcodec libx264 -b 4M -c:a aac -strict -2 -pix_fmt yuv420p "+str(localpath)+"/Vid_final.mp4 -y"
    subprocess.call(command, shell=True)
    emptyFolder(str(localpath)+"/generatedVideo/ev_frames")
    return