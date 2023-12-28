from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
import random

# Test
# cx_raw_data = Customer.objects.all().values()
# acc_raw_data = Account.objects.all().values()
# print(cx_raw_data, "\n\n", acc_raw_data)

# Account number should be 7 Digits
account_num_start = 1111111
account_num_end = 9999999


def home_page_view(request):

    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
        if user is not None:
            # login(request, user)
            # Redirect to a different page upon successful login
            # Change 'profile' to your desired URL
            return redirect(account_opening_view)
    return render(request, 'login.html')


def account_opening_view(request):
    if request.method == 'GET':
        existing_account_num = request.GET.get("account-number")
        if Account.objects.filter(account_number=existing_account_num).exists():
            return redirect(existing_customer_view, existing_account_num)
    if request.method == 'POST':
        data = request.POST

        first_name = data.get('first-name')
        last_name = data.get('last-name')
        date_of_birth = data.get('date-of-birth')
        address = data.get('address')
        gender = data.get('gender')
        account_type = data.get('account-type')
        initial_deposit = data.get('inital-deposit')

        customer = Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            address=address,
            gender=gender
        )

        # Generating Random account number in a given range
        def generate_random_number():
            temp = random.randrange(account_num_start, account_num_end, 1)
            return temp

        # Verifying account number doesn't already exists
        def generate_unique_random_number():
            while True:
                random_number = generate_random_number()
                if not Account.objects.filter(account_number=random_number).exists():
                    return random_number

        # Assigning new account number to the cx
        unique_random_number = generate_unique_random_number()
        account = Account.objects.create(
            customer=customer,
            account_number=unique_random_number,
            account_type=account_type,
            balance=initial_deposit
        )

        print(customer)
        print(account)

        # Inserting Data should be on two tables+

    return render(request, 'account_opening.html')


def existing_customer_view(request, existing_account_num):
    # ex_cx_acc = request.GET.get(existing_account_num)
    cx_id = Account.objects.filter(
        account_number=existing_account_num).values_list('customer_id', flat=True).get()
    print(cx_id)
    cx_info = Customer.objects.filter(id=cx_id).values()
    print(cx_info)
    # context = {'cx_info': cx_info, }
    # print(context)
    return render(request, 'existing_customer.html', {'cx_info': cx_info})
