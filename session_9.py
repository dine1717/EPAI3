from faker import Faker
from collections import namedtuple
from collections import Counter
from datetime import datetime
import random
import math
import re


#  Timer decorator to time functions with number of iterations
def timer_factory(repeat):
    """
    find average time to execute a function while running it for n times.
    """
    def time_it(func):
        from time import perf_counter
        from functools import wraps
        @wraps(func)
        def timer(*args, **kwargs):
            total_elapsed = 0
            for i in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / repeat
            print(f'Function {func.__name__} takes average run time of {avg_run_time} for {repeat} iterations')
            return result, avg_run_time
        return timer
    return time_it


def get_fake_profiles_nt(num):
    """
    function to create fake profiles library
    Generates a database of fake profiles
    based on user input  using named tuples
    It has one parameter:
        1) num ->  int no. of fake profiles to be created
    
    """
    fake = Faker()
    FakePrf= namedtuple('FakePrf', fake.profile().keys())
    FakePrfDb = namedtuple('FakePrfDb', 'FakePrf_0')

    for i in range(num):
        f_prfl = fake.profile()
        fake_profile = FakePrf(**f_prfl)
        if i==0:
            faker_db = FakePrfDb(fake_profile)
        else:
            FakePrfDb = namedtuple('FakePrfDb', FakePrfDb._fields + ('FakePrf_'+str(i),))
            faker_db = FakePrfDb._make(faker_db + (fake_profile,))

    return(faker_db)

@timer_factory(100)
def get_largest_blood_group(faker_db):
    """
    Return the most common blood group
    of fake profile db as named tuple
    It has one parameter:
        1) faker_db ->  db of fake profiles (1000)
    """
    count = len(faker_db)
    bl_grp = []
    for i in range(count):
        bl_grp.append(faker_db[i][5])
    return Counter(bl_grp).most_common(1)[0][0]

@timer_factory(100)
def get_mean_current_location(faker_db):
    """
    Return the mean-current_location
    of fake profile db as named tuple
    It has one parameter:
        1) faker_db ->  db of fake profiles (1000)
    """
    count = len(faker_db)
    lat = []
    long = []
    for i in range(count):
        lat.append(faker_db[i][4][0])
        long.append(faker_db[i][4][1])
    return sum(lat)/count,sum(long)/count

@timer_factory(100)
def get_oldest_person_age(faker_db):
    """
    Return the oldest person's age
    of fake profile db as named tuple
    It has one parameter:
        1) faker_db ->  db of fake profiles (1000)
    """
    size = len(faker_db)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(size):
        age.append((today - faker_db[i][12]).days / days_in_year)
    return max(age)

@timer_factory(100)
def get_average_age(faker_db):
    """
    Return the average age
    of fake profile db as named tuple
    It has one parameter:
        1) faker_db ->  db of fake profiles (1000)
    """
    count = len(faker_db)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(count):
        age.append((today - faker_db[i][12]).days / days_in_year)
    return sum(age)/count


def get_fake_profiles_dict(num):
    """
    function to create fake profiles library
    Generates a database of fake profiles
    based on user input  using dict
    It has one parameter:
        1) num ->  int no. of fake profiles to be created
    """
    fake = Faker()
    faker_db_dict = {}

    for i in range(num):
        f_prfl = fake.profile()
        key = 'fk_pr_' + str(i+1)
        faker_db_dict[key] = f_prfl

    return(faker_db_dict)

@timer_factory(100)
def get_largest_blood_group_dict(faker_db_dict):
    """
    Return the most common blood group for
    fake profile db as dictionary
    It has one parameter:
        1) faker_db_dict ->  db of fake profiles (1000)
    """
    count = len(faker_db_dict)
    bl_grp = []
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        bl_grp.append(faker_db_dict[key]['blood_group'])
    return Counter(bl_grp).most_common(1)[0][0]


@timer_factory(100)
def get_mean_current_location_dict(faker_db_dict):
    """
    Return the mean-current_location
    of fake profile db as dictionary
    It has one parameter:
        1) faker_db_dict ->  db of fake profiles (1000)
    """
    count = len(faker_db_dict)
    lat = []
    long = []
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        lat.append(faker_db_dict[key]['current_location'][0])
        long.append(faker_db_dict[key]['current_location'][1])
    return sum(lat)/count,sum(long)/count

@timer_factory(100)
def get_oldest_person_age_dict(faker_db_dict):
    """
    Return the oldest person's age
    of fake profile db as dictionary
    It has one parameter:
        1) faker_db_dict ->  db of fake profiles (1000)
    """
    size = len(faker_db_dict)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(size):
        key = 'fk_pr_' + str(i+1)
        age.append((today - faker_db_dict[key]['birthdate']).days / days_in_year)
    return max(age)

@timer_factory(100)
def get_average_age_dict(faker_db_dict):
    """
    Return the average age
    of fake profile db as dictionary
    It has one parameter:
        1) faker_db_dict ->  db of fake profiles (1000)
    """
    count = len(faker_db_dict)
    age = []
    days_in_year = 365.2425
    today = datetime.date(datetime.today())
    for i in range(count):
        key = 'fk_pr_' + str(i+1)
        age.append((today - faker_db_dict[key]['birthdate']).days / days_in_year)
    return sum(age)/count



def compare_time(nt_db, dict_db):
    """
    function to compare the performance
    of named tuple vs dict
    """
    
    nt_func_list = [get_largest_blood_group,get_mean_current_location,get_oldest_person_age,get_average_age]
    nt_timer = 0
    for i in range(len(nt_func_list)):
        _, time = nt_func_list[i](nt_db)
        nt_timer += time

    print('\n',"========================")

    dict_func_list = [get_largest_blood_group_dict,get_mean_current_location_dict,get_oldest_person_age_dict,get_average_age_dict]
    dict_timer = 0
    for i in range(len(dict_func_list)):
        _, time = dict_func_list[i](dict_db)
        dict_timer += time

    print('\n',"========================")

    print('\n',"========================")
    print(f"{'Named Tuple'if dict_timer > nt_timer else 'Dictionory'} performed {round(dict_timer/nt_timer) if dict_timer > nt_timer else round(nt_timer/dict_timer)} times faster")
    print('\n',"========================")

    return(nt_timer, dict_timer)

# Create a fake data (you can use Faker for company names) for imaginary
def create_stock_exchange(num_of_listed_comp = 100):
    """
    function to create fake company profiles and list
    them on a fake stock exchange.
    """
    Weights = namedtuple('Weights', ['wgt'+str(i) for i in range(num_of_listed_comp)])
    weight = Weights(*[round(random.random(),2) for _ in range(num_of_listed_comp)])
    wght_sum = sum(weight)
    norm_weight = Weights(*[wght/wght_sum for wght in weight])
    assert round(sum(norm_weight),2) == 1

    FakeComp = namedtuple('FakeComp', ['company_name', 'symbol', 'value', 'open', 'high', 'low', 'close'])
    StkXchange = namedtuple('StkXchange', 'fake_comp_0')
    fake = Faker()

    # Create fake companies and stock exchange
    for i in range(num_of_listed_comp):
        comp_name = fake.company()
        symbol = comp_name[0].upper() + random.choice(re.sub('\W+','', comp_name[1:-1])).upper() + comp_name[-1].upper()
        value = random.randint(3000,5000)
        open_ = round(value*norm_weight[i],2)
        high = round(open_*(random.randint(80,130)/100),2)
        low = random.randint(math.floor(open_*100*.5),math.floor(high*100))/100
        close = random.randint(math.floor(low*100),math.floor(high*100))/100

        # Create Fake Company
        fake_comp = FakeComp(comp_name,symbol,value, open_,high,low,close)
        # List the Fake company in Fake stock exchange
        if i==0:
            stock_exchange = StkXchange(fake_comp)
        else:
            StkXchange = namedtuple('StkXchange', StkXchange._fields + ('fake_comp_'+str(i),))

            stock_exchange = StkXchange._make(stock_exchange + (fake_comp,))

    return(stock_exchange)

# Calculate the days open, low, high and closing for stock exchange
def stock_exchange_details(stock_exchange):
    """
    Returns stock exchange details
    """
    day_open=0
    day_high=0
    day_low=0
    day_close=0
    for i in range(100):
        day_open  += stock_exchange[i].open
        day_high  += stock_exchange[i].high
        day_low   += stock_exchange[i].low
        day_close += stock_exchange[i].close

    return(round(day_open,2),round(day_high,2),round(day_low,2),round(day_close,2))
