import scipy
import scipy.misc
import scipy.cluster
from scipy.cluster.vq import vq, kmeans
import Image
import webcolors

LOG_LEVEL_REGULAR = 0
LOG_LEVEL_DEBUG = 1

class ColorDetector:

    NUM_OF_CLUSTERS = 10

    log_level =0

    def log(self, msg, log_level = LOG_LEVEL_DEBUG):
        if log_level == self.log_level:
            print msg

    def readImage(self, imagepath):
        image = Image.open(imagepath)
        return image

    def analyzeImage(self, image):
        color_band = scipy.misc.fromimage(im)
        shape = color_band.shape
        color_band = color_band.reshape(scipy.product(shape[:2]), shape[2])

        self.log('generating clusters')
        codes, dist = kmeans(ar, NUM_OF_CLUSTERS)
        self.log('Here are the cluster centres:')
        self.log(codes)

        vecs, dist = vq(color_band, codes)         # assign codes
        counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

        return (codes, counts)

    def print_color(self, color_code):
        print webcolors.hex_to_name(color_code)

    def getDominantColors(self, image, num_dominant_colors):
        (codes, counts) = analyzeImage(image)

        if num_dominant_colors > len(codes):
            num_dominant_colors = len(codes)

        for in range(0,num_dominant_colors):
            index_max = scipy.argmax(counts)                    # find most frequent
            peak = codes[index_max]
            colour_code = ''.join(chr(c) for c in peak).encode('hex')
            print_color(colour_code)
