from django.db import models
from datetime import datetime

# SELECT state_accounts.ACCOUNT_NO, state_person.ACCOUNT_NAME
# FROM state_accounts
# INNER JOIN state_person ON state_accounts.ACCOUNT_NO=state_person.ACCOUNT_NO

class Accounts(models.Model):
    ACCOUNT_NO = models.CharField(primary_key=True, max_length=100)
    ACTIVE_TRANSACTION_ID = models.CharField(max_length=100)
    TRANSACTION_ID = models.CharField(max_length=100)
    PART_TRAN_ID = models.CharField(max_length=100)
   
    TRANSACTION_AMOUNT = models.CharField(max_length=100)
    TRANSACTION_TYPE = models.CharField(max_length=100)
    TRANSACTION_SOURCE = models.CharField(max_length=100)
    
    ACTIVE_TRANSACTION_ID = models.CharField(max_length=100)
    TRANSACTION_CATEGORY = models.CharField(max_length=100)
    NARRATION = models.CharField(max_length=100)
    RECONCILIATION_REMARKS = models.CharField(max_length=100)
    TRAN_DATE = models.DateField(blank=True)
    TRAN_TIME = models.DateTimeField(default=datetime.now)
    VALUE_DATE = models.DateField(blank=True)

    VALUE_TIME = models.DateTimeField(default=datetime.now)
    POSTED_TIME = models.DateTimeField(default=datetime.now)
    
    POSTED_BY = models.CharField(max_length=100)
    APPROVED_DATE = models.DateField(blank=True)
    APPROVED_TIME = models.DateTimeField(default=datetime.now)
    APPROVED_BY = models.CharField(max_length=100)
    HASH_VALUE = models.BinaryField()
    DELETED_FLAG = models.CharField(max_length=100)
    # lga = models.CharField(max_length=100)

    def __str__(self):
        return self.ACCOUNT_NO
    
class Person(models.Model):
    ACCOUNT_ID = models.CharField(primary_key=True, max_length=100)
    CREATED_BY = models.CharField(max_length=100)
    DATE_CREATED = models.DateField(blank=True)
    TIME_CREATED = models.DateTimeField(default=datetime.now)
    UPDATED_BY = models.CharField(max_length=100)
   
    DATE_UPDATED = models.DateField(blank=True)
    TIME_UPDATED = models.DateTimeField(default=datetime.now)
    TRANSACTION_SOURCE = models.CharField(max_length=100)
    
    APPROVED_BY = models.CharField(max_length=100)
    DATE_APPROVED = models.DateField(blank=True)
    TIME_APPROVED = models.DateTimeField(default=datetime.now)
    STATUS = models.CharField(max_length=100)

    HASH_VALUE = models.BinaryField()
    DELETED_FLAG = models.CharField(max_length=100)
    ROW_VERSION = models.CharField(max_length=100)
    CUSTOMER_ID = models.CharField(max_length=100)
   
    DATE_UPDATED = models.DateField(blank=True)
    ACCOUNT_CODE_ID = models.CharField(max_length=100)
    ACCOUNT_NO = models.CharField(max_length=100)
    
    ACCOUNT_NAME = models.CharField(max_length=100)
    ACCOUNT_NO_ALIAS = models.CharField(max_length=100)
    ACCOUNT_NO_ALIAS_INDEX = models.CharField(max_length=100)
    CLEARED_BALANCE = models.CharField(max_length=100)

    UNCLEARED_BALANCE = models.CharField(max_length=100)
    LIEN_AMOUNT = models.CharField(max_length=100)
    OVERDRAFT_LIMIT = models.CharField(max_length=100)
    
    FREEZE_CODE = models.CharField(max_length=100)
    CURRENCY = models.CharField(max_length=100)
    ENABLE_SMS_ALERT = models.CharField(max_length=100)
    ENABLE_EMAIL_ALERT = models.CharField(max_length=100)

    MONTHLY_STATEMENT = models.CharField(max_length=100)
    ANNUAL_STATEMENT = models.CharField(max_length=100)
    CURRENT_INTEREST_RATE = models.CharField(max_length=100)
    
    LAST_TRANSACTION_DATE = models.DateField(blank=True)
    LAST_TRANSACTION_TIME = models.DateTimeField(default=datetime.now)
    LAST_INTEREST_RUN_DATE = models.DateField(blank=True)
    LAST_INTEREST_RUN_TIME = models.DateTimeField(default=datetime.now)

    LAST_CHARGES_RUN_DATE = models.DateTimeField()
    LAST_CHARGES_RUN_TIME = models.DateTimeField()
    CUSTOMER_DETAIL_ID = models.CharField(max_length=100)
    
    LAST_TRANSACTION_DATE = models.DateField(blank=True)
    LAST_TRANSACTION_TIME = models.DateTimeField(default=datetime.now)
    LAST_INTEREST_RUN_DATE = models.DateField(default=datetime.now)
    LAST_INTEREST_RUN_TIME = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.ACCOUNT_ID

# class Entry(models.Model):
#     blog = models.CharField(max_length=222)
#     headline = models.CharField(max_length=200)
    
#     # objects = models.DjongoManager()
    
#     def __str__(self):
#         return self.blog

# class NewTB(models.Model):
#     note = models.CharField(max_length=100)
#     loc = models.CharField(max_length=100)

#     # objects = models.DjongoManager()

#     def __str__(self):
#         return self.note
# # from django.db import models



# # class NewTable(models.Model):
# #     name = models.CharField(max_length=100)
# #     title = models.CharField(max_length=50)
# #     objects = models.Manager()
# #     def __str__(self):
# #         return self.name
