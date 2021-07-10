import pytest
import random
import string
import session_9
import os
import inspect
import re
from functools import reduce
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from decimal import Decimal
import pandas as pd


fake_profiles_nt = session_9.get_fake_profiles_nt(5)
fake_profiles_dict = session_9.get_fake_profiles_dict(5)

def test_create_fake_profiles():
    fake_profiles_nt = session_9.get_fake_profiles_nt(5)
    assert 5== len(fake_profiles_nt),"5 profiles created"


def test_get_fake_profiles_named_tuple_largest_blood_group():
	assert type(session_9.get_largest_blood_group(fake_profiles_nt)) == tuple,"did not give tuple of blodd group and count"

def test_get_fake_profiles_named_tuple_oldest_person_age():
	assert type(session_9.get_oldest_person_age(fake_profiles_nt)) == tuple,"did not give tuple of oldest person age"

def test_get_fake_profiles_named_tuple_get_mean_current_location():
	assert type(session_9.get_mean_current_location(fake_profiles_nt)) == tuple,"did not give mean of current location"

def test_get_fake_profiles_named_tuple_get_average_age():
	assert type(session_9.get_average_age(fake_profiles_nt)) == tuple,"did not give  average age"


def test_create_fake_profiles_dict():
    fake_profiles_dict = session_9.get_fake_profiles_dict(5)
    assert 5 == len(fake_profiles_dict),"5 profiles created"

def test_get_fake_profiles_dict_largest_blood_group():
	assert type(session_9.get_largest_blood_group_dict(fake_profiles_dict)) == tuple,"did not give tuple of blodd group and count"

def test_get_fake_profiles_dict_oldest_person_age():
	assert type(session_9.get_oldest_person_age_dict(fake_profiles_dict)) == tuple,"did not give tuple of oldest person age"

def test_get_fake_profiles_dict_get_mean_current_location():
	assert type(session_9.get_mean_current_location_dict(fake_profiles_dict)) == tuple,"did not give mean of current location"

def test_get_fake_profiles_dict_get_average_age():
	assert type(session_9.get_average_age_dict(fake_profiles_dict)) == tuple,"did not give  average age"



def test_compare_perforamce():
    faker_db = session_9.get_fake_profiles_nt(10)
    faker_db_dict = session_9.get_fake_profiles_dict(10)
    ntup, dict = session_9.compare_time(faker_db, faker_db_dict)
    assert ntup<dict, "Implementation is not correct"



def test_create_stock_exchange_profiles():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    assert 100==len(stock_exchange), "100 Companies created"


def test_check_data_type_of_company_name():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    assert type(stock_exchange.fake_comp_0.company_name)==str, "Company name should be string"


def test_check_data_type_of_company_name():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    assert type(stock_exchange.fake_comp_0.company_name)==str, "Company name should be string"

def test_create_stock_exchange_deatils():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert type(session_9.stock_exchange_details(stock_exchange)) ==tuple, "100 Companies created"


def test_stock_exchange_low_high():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert day_low<=day_high, "Implementation of Stock Exchange is not correct"

def test_stock_exchange_close_high():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert day_close<=day_high, "Implementation of Stock Exchange is not correct"

def test_stock_exchange_day_open_float():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert type(day_open)==float, "day_open should return float"

def test_stock_exchange_day_high_float():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert type(day_high)==float, "day_high should return float"

def test_stock_exchange_day_low_float():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert type(day_low)==float, "day_low should return float"

def test_stock_exchange_day_close_float():
    stock_exchange = session_9.create_stock_exchange(num_of_listed_comp = 100)
    day_open,day_high,day_low,day_close = session_9.stock_exchange_details(stock_exchange)
    assert type(day_close)==float, "day_close should return float"

