import os
import csv

def run(detect_folder, test_images):
    out_file = "submission.csv"

    with open(out_file, 'w', newline='') as out:
        writer = csv.writer(out)

        labels = os.listdir(test_images)

        for label in labels:
            label_fname = detect_folder + label.split(".")[0] + ".txt"
            img_name = label

            if os.path.isfile(label_fname):
                with open(label_fname, 'r') as f:
                    lines = f.readlines()
                
                line = " ".join(lines)
                line = line.replace("\n", "")
                writer.writerow([img_name, line])
            else:
                writer.writerow([img_name, ""])



if __name__== "__main__":
    test_images = "C:/tools/RDD2022/RDD2022_all_countries/Norway/test/images"
    print(test_images)
    detect_folder = "C:/Programmering/yolov7/runs/detect/exp4/labels/"
    print(detect_folder)
    run(detect_folder, test_images)
