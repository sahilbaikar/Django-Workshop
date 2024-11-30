from django.db import models

# Transactions Table
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated ID
    sendername = models.CharField(max_length=255, default='admin')  # Text field with default
    receivername = models.CharField(max_length=255, default='admin')  # Text field with default
    amount = models.IntegerField(default=0)  # Integer field with default
    timestamp = models.DateField(auto_now_add=True)  # Automatically set to current date on creation

    def __str__(self):
        return f"Transaction {self.id}: {self.sendername} to {self.receivername} amount= {self.amount}"

# Users Table
class Userprofile(models.Model):
    uid = models.AutoField(primary_key=True)  # Auto-generated ID
    username = models.CharField(max_length=255)  # Text field for the user's name
    amount_balance = models.IntegerField(default=0)  # Integer field with default
    created_date = models.DateField(auto_now_add=True)  # Automatically set to current date on creation

    def __str__(self):
        return f"{self.uid}: {self.username} amount balance= {self.amount_balance}"