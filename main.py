import argparse
import glob

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Trains and executes a given detector over a set of testing images')
    parser.add_argument(
        '--detector', type=str, nargs="?", default="", help='Detector string name')
    parser.add_argument(
        '--train_path', default="", help='Select the training data dir')
    parser.add_argument(
        '--test_path', default="", help='Select the testing data dir')

    args = parser.parse_args()

    # Load training data

    # Create the detector

    # Load testing data

    # Evaluate sign detections

'''for strinentradaimg in sorted (glob.glob("./train_10_ejemplos/*")):
    finnombre = strinentradaimg[-3:]
    for strinentradaim in sorted(glob.glob(strinentradaimg)):
        if finnombre !="txt" and (finnombre=="jpg" or finnombre=="ppm"):'''



