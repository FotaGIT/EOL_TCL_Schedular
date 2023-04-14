"""
TCU = scheduler

# indian time zone
 -- from pytz import timezone
 -- timestamp = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %p')

# variable names
var = 'modified_on', 'iccid', 'entitytype', 'tenancyid', 'eventtimestamp', 'eventname', 'eventcode', 'transactionid', 'transaction', 'resourceid', 'addonname', 'msisdn', 'subscriptiontype', 'startdate', 'is_transfer',

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EOL_TCL_Schedular.settings")

application = get_wsgi_application()
# ------------------------------- start from here -------------------------------

import datetime
import logging
import logging.handlers

from tcl_chedular.models import CorePurchaseaddon, EolCertClientTelematics
from logging.handlers import RotatingFileHandler
from django.utils.dateparse import parse_datetime

TCL_handler = RotatingFileHandler('TCL_schedular_logs.log', mode='a', maxBytes=5 * 1024 * 1024, backupCount=2, encoding=None, delay=0)

logging.basicConfig(
    # filename='TCL_schedular_logs.log',
    level=logging.DEBUG,
    datefmt="%y-%m-%d %H:%M:%S %p",
    format="-" * 100 + "\n%(asctime)s %(name)-15s %(levelname)-8s %(message)s",
    handlers=[
        TCL_handler
    ]
)

tcl_logger = logging.getLogger('''"TCL_Schedule"''')

purchase_obj = CorePurchaseaddon.objects.using('rds_aws').filter(is_transfer=False).order_by('-created_on')

for i in purchase_obj:
    sim_exp_date = parse_datetime(i.expirationdate).date()
    iccid = i.iccid
    try:
        if not isinstance(sim_exp_date, datetime.date):
            tcl_logger.info(f"| {iccid} - sim_exp_date field value is not available\n" + '-' * 100)
            continue

        try:
            EolCertClientTelematics.objects.filter(iccid=iccid).update(sim_exp_date=sim_exp_date)
        except Exception as e:
            tcl_logger.error(f"| {iccid} - {e}")
        else:
            i.is_transfer = True
            i.save()

    except Exception as e:
        tcl_logger.error(f"| {iccid} - {e}\n" + '-' * 100, exc_info=True)
