from .models import WebsiteEvaluation
from django.db.models.signals import post_save
from templated_email import send_templated_mail
from django.conf import settings
from django.utils.translation import ugettext as _

"""def notify_admin(sender, instance, created, raw, **kwargs):
    if all([instance.time_constraint,instance.answer_validity,instance. generality_applicability,
           instance.location_constraint,instance.degree_knowledge]) and (created and not raw):
           send_templated_mail(
            subject=_("Evaluation parameters for the post %s") % instance.post_url,
            template_name="admin_notify",
            from_email='',
            recipient_list=[settings.EMAIL_ADMIN],
            context={'instance': instance},
        )
post_save.connect(notify_admin, sender=WebsiteEvaluation,
                  dispatch_uid="notify_admin")"""

