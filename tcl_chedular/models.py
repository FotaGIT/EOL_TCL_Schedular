from django.db import models

# Create your models here.
from django.db import models

class CorePurchaseaddon(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    iccid = models.CharField(db_column='ICCID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    entitytype = models.CharField(db_column='entityType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tenancyid = models.CharField(db_column='tenancyID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    eventtimestamp = models.CharField(db_column='eventTimeStamp', max_length=500, blank=True, null=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='eventName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    eventcode = models.CharField(db_column='eventCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.CharField(db_column='TransactionId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    transaction = models.CharField(max_length=500, blank=True, null=True)
    resourceid = models.CharField(db_column='resourceID', max_length=500, blank=True, null=True)  # Field name made lowercase.
    addonname = models.CharField(db_column='addOnName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(max_length=500, blank=True, null=True)
    subscriptiontype = models.CharField(db_column='subscriptionType', max_length=500, blank=True, null=True)  # Field name made lowercase.
    startdate = models.CharField(db_column='startDate', max_length=500, blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.CharField(db_column='expirationDate', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_transfer = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'core_purchaseaddon'

class EolCertClientTelematics(models.Model):
    id = models.BigAutoField(db_column='ID')  # Field name made lowercase.
    serial_no = models.CharField(db_column='SERIAL_NO', primary_key=True, max_length=50)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vc_no = models.CharField(db_column='VC_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    container_no = models.CharField(db_column='CONTAINER_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hardware_no = models.CharField(db_column='HARDWARE_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iccid = models.CharField(db_column='ICCID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imei = models.CharField(db_column='IMEI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel_type = models.CharField(db_column='FUEL_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    client_cert = models.TextField(db_column='CLIENT_CERT', blank=True, null=True)  # Field name made lowercase.
    client_key = models.TextField(db_column='CLIENT_KEY', blank=True, null=True)  # Field name made lowercase.
    upload_timestamp = models.DateTimeField(db_column='UPLOAD_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    download_timestamp = models.DateTimeField(db_column='DOWNLOAD_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='UPDATE_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    provisioning_status = models.CharField(db_column='PROVISIONING_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provisioning_timestamp = models.DateTimeField(db_column='PROVISIONING_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    location_name = models.CharField(db_column='LOCATION_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    critical_device = models.CharField(db_column='CRITICAL_DEVICE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_type_name = models.CharField(db_column='DEVICE_TYPE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protocol_type_name = models.CharField(db_column='PROTOCOL_TYPE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_uid = models.CharField(db_column='DEVICE_UID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protocol_type_id = models.CharField(db_column='PROTOCOL_TYPE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_type_id = models.CharField(db_column='DEVICE_TYPE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_point_id = models.CharField(db_column='END_POINT_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location_id = models.CharField(db_column='LOCATION_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='ACCOUNT_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_security_code = models.CharField(db_column='DEVICE_SECURITY_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gw_scan_period = models.CharField(db_column='GW_SCAN_PERIOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    protocols = models.CharField(db_column='PROTOCOLS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_point_name = models.CharField(db_column='END_POINT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='ACCOUNT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved1 = models.CharField(db_column='RESERVED1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved2 = models.DateTimeField(db_column='RESERVED2', blank=True, null=True)  # Field name made lowercase.
    reserved3 = models.CharField(db_column='RESERVED3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tcu_firmware_version = models.CharField(db_column='TCU_FIRMWARE_VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l3_provision_status = models.CharField(db_column='L3_PROVISION_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l3_provision_timestamp = models.DateTimeField(db_column='L3_PROVISION_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    tcu_manu_timestamp = models.DateTimeField(db_column='TCU_MANU_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    bootstrap_exp_timestamp = models.DateTimeField(db_column='BOOTSTRAP_EXP_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    operator_vendor_location = models.CharField(db_column='OPERATOR_VENDOR_LOCATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendor_eol_test_result = models.CharField(db_column='VENDOR_EOL_TEST_RESULT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved4 = models.CharField(db_column='RESERVED4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved5 = models.CharField(db_column='RESERVED5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved6 = models.CharField(db_column='RESERVED6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reserved7 = models.CharField(db_column='RESERVED7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel_type_corrected = models.CharField(db_column='FUEL_TYPE_CORRECTED', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iccid_corrected = models.CharField(db_column='ICCID_CORRECTED', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vehicle_type = models.CharField(db_column='VEHICLE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_msisdn1 = models.CharField(db_column='SIM_MSISDN1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_operator1 = models.CharField(db_column='SIM_OPERATOR1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_msisdn2 = models.CharField(db_column='SIM_MSISDN2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_operator2 = models.CharField(db_column='SIM_OPERATOR2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    app_ready = models.CharField(db_column='APP_READY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sim_plan = models.CharField(db_column='SIM_PLAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sim_data_pack = models.CharField(db_column='SIM_DATA_PACK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_status = models.CharField(db_column='SIM_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_act_date = models.CharField(db_column='SIM_ACT_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_data_available = models.CharField(db_column='SIM_DATA_AVAILABLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_data_aval_date = models.CharField(db_column='SIM_DATA_AVAL_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim_acc_name = models.CharField(db_column='SIM_ACC_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active_tcu = models.CharField(db_column='ACTIVE_TCU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_updated_timestamp = models.DateTimeField(db_column='LAST_UPDATED_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    sim_isprocessed_transdata = models.IntegerField(db_column='SIM_ISPROCESSED_TRANSDATA', blank=True, null=True)  # Field name made lowercase.
    sim_isprocessed_masterdata = models.IntegerField(db_column='SIM_ISPROCESSED_MASTERDATA', blank=True, null=True)  # Field name made lowercase.
    device_make = models.CharField(db_column='DEVICE_MAKE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    device_model = models.CharField(db_column='DEVICE_MODEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_flag = models.CharField(db_column='CRM_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_vc = models.CharField(db_column='CRM_VC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_invoice_date = models.DateTimeField(db_column='CRM_INVOICE_DATE', blank=True, null=True)  # Field name made lowercase.
    crm_lob = models.CharField(db_column='CRM_LOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_pl = models.CharField(db_column='CRM_PL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_physical_status = models.CharField(db_column='CRM_PHYSICAL_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_logical_status = models.CharField(db_column='CRM_LOGICAL_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_customer_delivered_date = models.DateTimeField(db_column='CRM_CUSTOMER_DELIVERED_DATE', blank=True, null=True)  # Field name made lowercase.
    crm_dealer_region = models.CharField(db_column='CRM_DEALER_REGION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_invoice_cancellation_date = models.CharField(db_column='CRM_INVOICE_CANCELLATION_DATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_ppl = models.CharField(db_column='CRM_PPL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_vehicle_program_name = models.CharField(db_column='CRM_VEHICLE_PROGRAM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_customer_type = models.CharField(db_column='CRM_CUSTOMER_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_customer_ph_no = models.CharField(db_column='CRM_CUSTOMER_PH_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_updated_timestamp = models.DateTimeField(db_column='CRM_UPDATED_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    sap_vc = models.CharField(db_column='SAP_VC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_invoice_type = models.TextField(db_column='SAP_INVOICE_TYPE', blank=True, null=True)  # Field name made lowercase.
    sap_fuel = models.CharField(db_column='SAP_FUEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_colour = models.TextField(db_column='SAP_COLOUR', blank=True, null=True)  # Field name made lowercase.
    sap_transmission = models.CharField(db_column='SAP_TRANSMISSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_ac_type = models.TextField(db_column='SAP_AC_TYPE', blank=True, null=True)  # Field name made lowercase.
    sap_model = models.TextField(db_column='SAP_MODEL', blank=True, null=True)  # Field name made lowercase.
    sap_variant = models.TextField(db_column='SAP_VARIANT', blank=True, null=True)  # Field name made lowercase.
    sap_emmission_norms = models.TextField(db_column='SAP_EMMISSION_NORMS', blank=True, null=True)  # Field name made lowercase.
    sap_bookiing_time = models.DateTimeField(db_column='SAP_BOOKIING_TIME', blank=True, null=True)  # Field name made lowercase.
    sap_plant_yard = models.CharField(db_column='SAP_PLANT_YARD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_billing_status = models.CharField(db_column='SAP_BILLING_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_code = models.CharField(db_column='SAP_DEALER_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_name = models.TextField(db_column='SAP_DEALER_NAME', blank=True, null=True)  # Field name made lowercase.
    sap_dealer_address_1 = models.TextField(db_column='SAP_DEALER_ADDRESS_1', blank=True, null=True)  # Field name made lowercase.
    sap_dealer_address_2 = models.TextField(db_column='SAP_DEALER_ADDRESS_2', blank=True, null=True)  # Field name made lowercase.
    sap_dealer_address_3 = models.TextField(db_column='SAP_DEALER_ADDRESS_3', blank=True, null=True)  # Field name made lowercase.
    sap_dealer_city = models.CharField(db_column='SAP_DEALER_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_state = models.CharField(db_column='SAP_DEALER_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_phone_1 = models.CharField(db_column='SAP_DEALER_PHONE_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_phone_2 = models.CharField(db_column='SAP_DEALER_PHONE_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sap_dealer_email_id_1 = models.TextField(db_column='SAP_DEALER_EMAIL_ID_1', blank=True, null=True)  # Field name made lowercase.
    sap_dealer_email_id_2 = models.TextField(db_column='SAP_DEALER_EMAIL_ID_2', blank=True, null=True)  # Field name made lowercase.
    is_transferred_to_fota = models.CharField(db_column='IS_TRANSFERRED_TO_FOTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_transferred_to_sap = models.CharField(db_column='IS_TRANSFERRED_TO_SAP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    event_name = models.CharField(db_column='EVENT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    event_code = models.CharField(db_column='EVENT_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_time_event = models.DateTimeField(db_column='DATE_TIME_EVENT', blank=True, null=True)  # Field name made lowercase.
    reference_id = models.CharField(db_column='REFERENCE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_id = models.CharField(db_column='PRODUCT_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='COMPANY_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_number = models.CharField(db_column='CUSTOMER_NUMBER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    from_status = models.CharField(db_column='FROM_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    to_status = models.CharField(db_column='TO_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(db_column='MSISDN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imsis = models.TextField(db_column='IMSIS', blank=True, null=True)  # Field name made lowercase.
    tenancy_id = models.CharField(db_column='TENANCY_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    entity_type = models.CharField(db_column='ENTITY_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transaction_id = models.CharField(db_column='TRANSACTION_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resource_id = models.CharField(db_column='RESOURCE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    add_on_name = models.CharField(db_column='ADD_ON_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subscription_type = models.CharField(db_column='SUBSCRIPTION_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE', blank=True, null=True)  # Field name made lowercase.
    event_time_stamp = models.DateTimeField(db_column='EVENT_TIME_STAMP', blank=True, null=True)  # Field name made lowercase.
    expiration_date = models.DateTimeField(db_column='EXPIRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    sim_exp_date = models.DateField(db_column='SIM_EXP_DATE', blank=True, null=True)  # Field name made lowercase.
    fotaportalfwversion = models.CharField(db_column='FOTAPortalFWVersion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plan = models.CharField(db_column='PLAN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_status = models.CharField(db_column='CARD_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_state = models.CharField(db_column='CARD_STATE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_quota = models.CharField(db_column='DATA_QUOTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sms_quota = models.CharField(db_column='SMS_QUOTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operator_1 = models.CharField(db_column='OPERATOR_1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operator_2 = models.CharField(db_column='OPERATOR_2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    operator_3 = models.CharField(db_column='OPERATOR_3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    msisdn_1 = models.CharField(db_column='MSISDN_1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msisdn_2 = models.CharField(db_column='MSISDN_2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msisdn_3 = models.CharField(db_column='MSISDN_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_remaining = models.CharField(db_column='DATA_REMAINING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sms_remaining = models.CharField(db_column='SMS_REMAINING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kyc_status = models.CharField(db_column='KYC_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bs_expiry_date = models.DateTimeField(db_column='BS_EXPIRY_DATE', blank=True, null=True)  # Field name made lowercase.
    activation_date = models.DateTimeField(db_column='ACTIVATION_DATE', blank=True, null=True)  # Field name made lowercase.
    cs_expiry_date = models.DateTimeField(db_column='CS_EXPIRY_DATE', blank=True, null=True)  # Field name made lowercase.
    kyc_status_date = models.DateTimeField(db_column='KYC_STATUS_DATE', blank=True, null=True)  # Field name made lowercase.
    transmission_type = models.CharField(db_column='TRANSMISSION_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model_name = models.CharField(db_column='MODEL_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_dataemailed_to_crm = models.CharField(db_column='IS_DataEmailed_TO_CRM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    crmdataemailed_timestamp = models.DateTimeField(db_column='CRMDataEmailed_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    staging_id = models.BigIntegerField(db_column='Staging_id', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    chassis_number = models.CharField(max_length=500, blank=True, null=True)
    vc_number = models.CharField(max_length=500, blank=True, null=True)
    engine_type = models.CharField(max_length=500, blank=True, null=True)
    engine_number = models.CharField(max_length=500, blank=True, null=True)
    emission_norm = models.CharField(max_length=500, blank=True, null=True)
    customer_delivered_date = models.DateTimeField(blank=True, null=True)
    lob = models.CharField(max_length=500, blank=True, null=True)
    pl = models.CharField(max_length=500, blank=True, null=True)
    ppl = models.CharField(max_length=500, blank=True, null=True)
    physical_status = models.CharField(max_length=500, blank=True, null=True)
    logical_status = models.CharField(max_length=500, blank=True, null=True)
    dealer_name = models.CharField(max_length=500, blank=True, null=True)
    dealer_code = models.CharField(max_length=500, blank=True, null=True)
    dealer_region = models.CharField(max_length=500, blank=True, null=True)
    dealer_state = models.CharField(max_length=500, blank=True, null=True)
    dealer_city = models.CharField(max_length=500, blank=True, null=True)
    customer_name = models.CharField(max_length=500, blank=True, null=True)
    vehicle_account = models.CharField(max_length=500, blank=True, null=True)
    customer_type = models.CharField(max_length=500, blank=True, null=True)
    customer_ph_no = models.CharField(max_length=500, blank=True, null=True)
    customer_state = models.CharField(max_length=500, blank=True, null=True)
    customer_city = models.CharField(max_length=500, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    driver_name = models.CharField(max_length=500, blank=True, null=True)
    driver_contact = models.CharField(max_length=500, blank=True, null=True)
    data_received_date = models.DateTimeField(blank=True, null=True)
    invoice_cancle_date = models.DateTimeField(blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    invoice_number = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EOL_CERT_CLIENT_TELEMATICS'

class CoreProductstate(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    imsis = models.CharField(db_column='Imsis', max_length=500, blank=True, null=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='eventName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    eventcode = models.CharField(db_column='EventCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    iccid = models.CharField(db_column='Iccid', max_length=500, blank=True, null=True)  # Field name made lowercase.
    msisdn = models.CharField(max_length=500, blank=True, null=True)
    datetimeevent = models.CharField(db_column='DateTimeEvent', max_length=500, blank=True, null=True)  # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    productid = models.CharField(db_column='ProductId', max_length=500, blank=True, null=True)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    fromstatus = models.CharField(db_column='FromStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tostatus = models.CharField(db_column='ToStatus', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customernumber = models.CharField(db_column='CustomerNumber', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_productstate'
