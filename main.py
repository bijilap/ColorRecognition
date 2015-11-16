import argparse
from ColorDetector import ColorDetector

def main():
    detector = ColorDetector()
    parser = argparse.ArgumentParser()
    # --k : number of clusters, --image: image path, --debug: debug level
    parser.add_argument("--k", nargs=1)
    parser.add_argument("--n", nargs=1)
    parser.add_argument("--image", nargs=1)
    parser.add_argument("--debug", nargs=1)
    args = parser.parse_args()

    img_name = None
    n = 4

    if args.k:
        detector.NUM_OF_CLUSTERS = int(args.k[0])

    if args.image:
        img_name = args.image[0]

    if args.debug:
        detector.log_level = int(args.debug[0])

    if args.n:
        n = int(args.n[0])

    image = detector.readImage(img_name)
    detector.getDominantColors(image, n)


if __name__ == "__main__":
    main()
