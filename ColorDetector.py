import scipy
import scipy.misc
import scipy.cluster
from scipy.cluster.vq import vq, kmeans
import Image
import webcolors
import numpy

LOG_LEVEL_REGULAR = 0
LOG_LEVEL_DEBUG = 1

class ColorDetector:

    NUM_OF_CLUSTERS = 10

    log_level =  LOG_LEVEL_REGULAR

    def log(self, msg, log_level=LOG_LEVEL_DEBUG):
        if log_level == self.log_level:
            print msg

    def readImage(self, imagepath):
        image = Image.open(imagepath)
        return image

    def analyzeImage(self, image):
        color_band = scipy.misc.fromimage(image)
        shape = color_band.shape
        color_band = color_band.reshape(scipy.product(shape[:2]), shape[2])

        self.log('generating clusters')
        codes, dist = kmeans(color_band, self.NUM_OF_CLUSTERS)
        self.log('Here are the cluster centres:')
        self.log(codes)

        vecs, dist = vq(color_band, codes)         # assign codes
        counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

        return (codes, counts)

    def print_color(self, color_code):
        try:
            print webcolors.hex_to_name(color_code)
        except:
            print color_code

    def getDominantColors(self, image, num_dominant_colors):
        (codes, counts) = self.analyzeImage(image)

        codesList = codes.tolist()
        countsList = counts.tolist()

        print "Approximate number of colors:" + str(len(codes))

        if num_dominant_colors > len(codes):
            num_dominant_colors = len(codes)

        for i in range(0,num_dominant_colors):
            index_max = scipy.argmax(countsList)                    # find most frequent
            peak = codesList[index_max]
            colour_code = ''.join(chr(c) for c in peak).encode('hex')
            colour_code = "#"+colour_code
            self.print_color(colour_code)
            codesList.pop(index_max)
            countsList.pop(index_max)
