# Tuples and Named Tuples

1. Use the Faker (Links to an external site.)library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings). - 250 (including 5 test cases)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)
4. Please write a readme file that can help me understand your code. If you don't write a readme properly, I would not be evaluating that piece of the code. 
5. Add the notebook as well to your github where logs can be visible. Your github code must have cleared all the 20 tests that you're writing (these 20 cannot be any of the ones you can already find in the code we shared earlier).


Solutions

1. Generate 10000 random  profiles using named tuple.

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
  
 1.1 Calculate the largest blood type

      def get_largest_blood_group(faker_db):
          """
          Return the most common blood group
          of fake profile db as named tuple
          It has one parameter:
              1) faker_db ->  db of fake profiles (10000)
          """
          count = len(faker_db)
          bl_grp = []
          for i in range(count):
              bl_grp.append(faker_db[i][5])
          return Counter(bl_grp).most_common(1)[0][0]
          

   
 1.2 Mean-current_location
 
     def get_mean_current_location(faker_db):
        """
        Return the mean-current_location
        of fake profile db as named tuple
        It has one parameter:
            1) faker_db ->  db of fake profiles (10000)
        """
        count = len(faker_db)
        lat = []
        long = []
        for i in range(count):
            lat.append(faker_db[i][4][0])
            long.append(faker_db[i][4][1])
        return sum(lat)/count,sum(long)/count
 
 1.3 Oldest_person_age
 
     def get_oldest_person_age(faker_db):
        """
        Return the oldest person's age
        of fake profile db as named tuple
        It has one parameter:
            1) faker_db ->  db of fake profiles (10000)
        """
        size = len(faker_db)
        age = []
        days_in_year = 365.2425
        today = datetime.date(datetime.today())
        for i in range(size):
            age.append((today - faker_db[i][12]).days / days_in_year)
        return max(age)
        
  
  1.4 Average Age 
  
        def get_average_age(faker_db):
          """
          Return the average age
          of fake profile db as named tuple
          It has one parameter:
              1) faker_db ->  db of fake profiles (10000)
          """
          count = len(faker_db)
          age = []
          days_in_year = 365.2425
          today = datetime.date(datetime.today())
          for i in range(count):
              age.append((today - faker_db[i][12]).days / days_in_year)
          return sum(age)/count

    
    
    
  2. Generate 10000 random  profiles using dict.

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
  
 2.1 Calculate the largest blood type

    def get_largest_blood_group_dict(faker_db_dict):
        """
        Return the most common blood group for
        fake profile db as dictionary
        It has one parameter:
            1) faker_db_dict ->  db of fake profiles (10000)
        """
        count = len(faker_db_dict)
        bl_grp = []
        for i in range(count):
            key = 'fk_pr_' + str(i+1)
            bl_grp.append(faker_db_dict[key]['blood_group'])
        return Counter(bl_grp).most_common(1)[0][0]
          

   
 2.2 Mean-current_location
 
    def get_mean_current_location_dict(faker_db_dict):
        """
        Return the mean-current_location
        of fake profile db as dictionary
        It has one parameter:
            1) faker_db_dict ->  db of fake profiles (10000)
        """
        count = len(faker_db_dict)
        lat = []
        long = []
        for i in range(count):
            key = 'fk_pr_' + str(i+1)
            lat.append(faker_db_dict[key]['current_location'][0])
            long.append(faker_db_dict[key]['current_location'][1])
        return sum(lat)/count,sum(long)/count
 
 2.3 Oldest_person_age
 
    def get_oldest_person_age_dict(faker_db_dict):
        """
        Return the oldest person's age
        of fake profile db as dictionary
        It has one parameter:
            1) faker_db_dict ->  db of fake profiles (10000)
        """
        size = len(faker_db_dict)
        age = []
        days_in_year = 365.2425
        today = datetime.date(datetime.today())
        for i in range(size):
            key = 'fk_pr_' + str(i+1)
            age.append((today - faker_db_dict[key]['birthdate']).days / days_in_year)
        return max(age)
        
  
  2.4 Average Age 

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



3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close)


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

  3.1 Calculate the days open, low, high and closing for stock exchange
  
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
