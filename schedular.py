"""
TCU = scheduler
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EOL_TCL_Schedular.settings")

application = get_wsgi_application()
# ------------------------------- strat from here ---------------------------------

import logging
import datetime
import json
from datetime import date

from tcl_chedular.models import CorePurchaseaddon, EolCertClientTelematics
from logging.handlers import RotatingFileHandler
from pytz import timezone
import logging.handlers


TCL_handler = RotatingFileHandler('TCL_schedular_logs.log', mode='a', maxBytes=5 * 1024 * 1024, backupCount=2, encoding=None, delay=0)

timestamp = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %p')

logger = logging.basicConfig(
    # filename='TCL_schedular_logs.log',
    level=logging.DEBUG,
    datefmt="%y-%m-%d %H:%M:%S %p",
    format="%(asctime)s %(name)-15s %(levelname)-8s %(message)s",
    handlers=[
        TCL_handler
    ]
)
logger = logging.getLogger('''"TCL_Schedule"''')

purchase_obj = CorePurchaseaddon.objects.using('rds_aws').filter(is_transfer=False).order_by('-created_on').values('iccid', 'expirationdate','created_on')

for i in purchase_obj:
    sim_exp_date = i.get("expirationdate", None)
    iccid = i.get("iccid", None)
    try:
        if not sim_exp_date:
            logger.info(f"| {iccid} - sim_exp_date field value is not available")
            continue

        pass
        # EolCertClientTelematics.objects.filter(
        #     iccid=iccid
        # ).update(sim_exp_date=sim_exp_date)
    except Exception as e:
        logging.error(f"{timestamp} - {e}")
        print(e)

# k = {
#     'modified_on': datetime.datetime(2022, 6, 21, 7, 5, 44, 16552, tzinfo=datetime.timezone.utc),
#     'iccid': '893107061604825000',
#     'entitytype': 'Subscription',
#     'tenancyid': 'SECS_38790_00001',
#     'eventtimestamp': None,
#     'eventname': 'ProductPurchaseAddOn',
#     'eventcode': 'Success',
#     'transactionid': '66145e83-aea8-4f01-ba32-42ba65a4ef63',
#     'transaction': 'SECS_38790_00001',
#     'resourceid': '494fbdde-1629-e811-bea7-005056a6a7d6',
#     'addonname': '500 MB EUS RECURRING',
#     'msisdn': '31687763510',
#     'subscriptiontype': 'EUS',
#     'startdate': '2018-10-03T10:08:22.019Z',
#     'is_transfer': False
# }
