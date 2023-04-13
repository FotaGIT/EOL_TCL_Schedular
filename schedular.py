"""
TCU = scheduler
"""
import logging
import datetime
import json
import math
import os
from datetime import date

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EOL_TCL_Schedular.settings")

application = get_wsgi_application()
# ------------------------------- strat from here ---------------------------------

from tcl_chedular.models import CorePurchaseaddon, EolCertClientTelematics
from pytz import timezone 
logging.basicConfig(filename='TCL_schedular_logs.log', level=logging.INFO)

timestamp = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %p')

level = 'INFO'
message = 'This is an example log message.'
logging.info(f"{timestamp} - {message}")


purchase_obj = CorePurchaseaddon.objects.using('rds_aws').filter().values()

d = {}
for i in purchase_obj:
    try:
        ID = i.pop("id")
        created_on = i.pop("created_on")
        EolCertClientTelematics.objects.filter(
            iccid=i.get("iccid")
        ).update(sim_exp_date=)
        # EolCertClientTelematics.objects.filter(
        #     iccid=i.get("iccid")
        # ).update(**i)
        d.update(**i)
        print(i)

    except Exception as e:
        pass
