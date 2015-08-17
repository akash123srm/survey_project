import os
import sys
import logging
import django

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "survey_project.settings")
django.setup()

# your imports, e.g. Django models

from survey_app.models import Website, Post, WebsiteEvaluation

if __name__ == '__main__':
    # here is the place where the script starts


    # open .csv file with information for URLs and Websites
    # Assumption:
    # CSV Format:
    # Website name,Category of the website, URL_of_acticle

    f = open("static/thesis_data.csv", "r")
    content = f.read()
    f.close()
    lines = content.split("\n")
    for line in lines:
        token = line.split(",")
        if len(token[0]) == 0:
            continue

        # assumption: token[0] = Website
        #             token[1] = Category of the website
        #             token[2] = Url
        # Now: create Post and Website model instances
        """print token"""
        w,created = Website.objects.get_or_create(name=token[0],category=token[1])
        w.save()
        p,created = Post.objects.get_or_create(url=token[2],website=w)
        p.save()
        e,created = WebsiteEvaluation.objects.get_or_create(post_url=p,time_constraint=token[3],
                    answer_validity=token[4], generality_applicability=token[5],location_constraint=token[6],
                    degree_knowledge=token[7],costs_parameters=token[8],info_provider_layman=token[9],info_provider_operator=token[10],
                    info_provider_expert=token[11],mobile_context=token[12],spatial_coordinates=token[13],
                    ask_questions=token[14],suggestions=token[15],comment=token[16],personal_profile=token[17],
                    others_information_need=token[18],contact_user=token[19],user_id=token[20])
        e.save()

