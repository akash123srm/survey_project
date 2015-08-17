import os, sys
import logging
import site
import django

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey_project.settings")
django.setup()

# your imports, e.g. Django models

from survey_app.models import Website, Post

if __name__ == '__main__':
    # here is the place where the script starts


    # open .csv file with information for URLs and Websites
    # Assumption:
    # CSV Format:
    # Website name,Category of the website, URL_of_acticle

    f = open("static/test_data_revised.csv","r")
    content = f.read()
    f.close()
    lines = content.split("\n")
    for line in lines[1:]:
        token = line.split(",")
        if len(token[0]) == 0:
            continue

        # assumption: token[0] = Website
        #             token[1] = Category of the website
        #             token[2] = Url
        # Now: create Post and Website model instances
        print token
        w,created = Website.objects.get_or_create(name=token[0],category=token[1])
        print(token[1])
        w.save()
        p,created = Post.objects.get_or_create(url=token[2],website=w)
        p.save()
