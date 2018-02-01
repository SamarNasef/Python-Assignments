import random
import os
if __name__ == '__main__':
    l=['www.google.com','www.youtube.com','www.facebook.com','www.twitter.com']
    random_index = random.randint(0,3)
    os.system('firefox '+l[random_index])