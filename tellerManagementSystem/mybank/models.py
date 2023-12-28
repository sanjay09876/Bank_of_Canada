from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# Users table


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)  # Admin or Normal User
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return (self.role)


# Customers table


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address_line1 = models.TextField()
    address_line2 = models.TextField(null=True)
    city = models.TextField()
    province = models.TextField()
    postal_code = models.CharField(max_length=6)
    country = models.TextField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return (self.first_name + " " + self.last_name)


# Accounts table


class Account(models.Model):

    account_type_choices = (
        ('Checking', 'checking'),
        ('Savings', 'savings'),
        ('RRSP', 'RRSP'),
        ('TFSA', 'TFSA'),
        ('RESP', 'RESP'),
        ('USD', 'USD'),

    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.IntegerField(
        validators=[MinValueValidator(1111111), MaxValueValidator(9999999)], default=0)
    # Checking, Savings, etc.
    account_type = models.CharField(
        max_length=10, choices=account_type_choices)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return (self.account_type)

# Transactions table


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)  # Deposit or Withdrawal
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()

# AccountChanges table


class AccountChange(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # Name Correction, DOB Correction, etc.
    change_type = models.CharField(max_length=20)
    change_details = models.TextField()
    change_date = models.DateTimeField()

# Reports table


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Daily Transaction, Monthly Transaction, etc.
    report_type = models.CharField(max_length=20)
    report_content = models.TextField()
    report_date = models.DateTimeField()
