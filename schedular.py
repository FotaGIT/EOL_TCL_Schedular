"""
TCU = Project
"""
import datetime
import json
import math
import os
from datetime import date

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EOL_TCL_Schedular.settings")

application = get_wsgi_application()
from tcl_chedular.models import CorePurchaseaddon, EolCertClientTelematics

purchase_obj = CorePurchaseaddon.objects.using('rds_aws').filter().values()

for i in purchase_obj:
    ID = i.pop("id")
    created_on = i.pop("created_on")
    modified_on = i.pop("modified_on")




# update_obj = EolCertClientTelematics.objects.update(iccid=)