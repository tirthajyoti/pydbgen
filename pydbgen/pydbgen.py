class pydb():
    
    def __init__(self,seed=None):
        """
        Initiates the class and creates a Faker() object for later data generation by other methods
        seed: User can set a seed parameter to generate deterministic, non-random output
        """
        from faker import Faker
        import pandas as pd
        from random import randint,choice
        
        self.fake=Faker()
        self.seed=seed
        self.randnum=randint(1,9)


    def simple_ph_num(self,seed=None):
        """
        Generates 10 digit US phone number in xxx-xxx-xxxx format
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        """
        import random
        from random import randint,choice
        random.seed(self.seed)

        result = str(randint(1,9))
        for _ in range(2):
            result+=str(randint(0,9))
        result+='-'
        for _ in range(3):
            result+=str(randint(0,9))
        result+='-'
        for _ in range(4):
            result+=str(randint(0,9))
        return result


    def license_plate(self,seed=None,style=None):
        """
        Generates vehicle license plate number in 3 possible styles
        Style can be 1, 2, or 3.
        - 9ABC123 format
        - ABC-1234 format
        - ABC-123 format
        If style is not specified by user, a random style is chosen at runtime
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        """
        import random
        from random import randint,choice
        random.seed(self.seed)

        if style==None:
            style = choice([1,2,3])
        
        if style==1:
            result = str(randint(1,9))
            for _ in range(3):
                result+=chr(randint(65,90))
            for _ in range(3):
                result+=str(randint(1,9))
            return result
        elif style==2:
            result=''
            for _ in range(3):
                result+=chr(randint(65,90))
            result+='-'
            for _ in range(4):
                result+=str(randint(0,9))
            return result
        else:
            result=''
            for _ in range(3):
                result+=chr(randint(65,90))
            result+='-'
            for _ in range(3):
                result+=str(randint(0,9))
            return result


    def realistic_email(self,name,seed=None):
        '''
        Generates realistic email from first and last name and a random domain address
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        '''
        import random
        from random import randint,choice
        random.seed(self.seed)

        name=str(name)
        result=''
        f_name = name.split()[0]
        l_name = name.split()[-1]
        
        choice_int = choice(range(10))
        
        path = "Domains.txt"
        
        domain_list = []
        fh = open(path)
        for line in fh.readlines():
            domain_list.append(str(line).strip())

        domain = choice(domain_list)
        fh.close()       
        
        name_choice = choice(range(8))
        
        if name_choice==0:
            name_combo=f_name[0]+l_name
        elif name_choice==1:
            name_combo=f_name+l_name
        elif name_choice==2:
            name_combo=f_name+'.'+l_name[0]
        elif name_choice==3:
            name_combo=f_name+'_'+l_name[0]
        elif name_choice==4:
            name_combo=f_name+'.'+l_name
        elif name_choice==5:
            name_combo=f_name+'_'+l_name
        elif name_choice==6:
            name_combo=l_name+'_'+f_name
        elif name_choice==7:
            name_combo=l_name+'.'+f_name
        
        if (choice_int<7):
            result+=name_combo+'@'+str(domain)
        else:
            random_int = randint(11,99)
            result+=name_combo+str(random_int)+'@'+str(domain)

        return result

    def city_real(self,seed=None):
        '''
        Picks and returns a random entry out of 385 US cities
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        '''
        import os
        from six import moves
        import ssl
        import random
        from random import randint,choice
        random.seed(self.seed)

        path = "US_Cities.txt"
        if not os.path.isfile(path):
            context = ssl._create_unverified_context()
            moves.urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path)
        
        city_list = []
        fh = open(path)
        for line in fh.readlines():
            city_list.append(str(line).strip())    
        
        fh.close() 

        return (choice(city_list))        

    def gen_data_series(self,num=10,data_type='name',seed=None):
        """
        Returns a pandas series object with the desired number of entries and data type
        
        Data types available: 
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN 
        - Company, Job title, phone number, license plate
        
        Phone number can be two types: 
        'phone_number_simple' generates 10 digit US number in xxx-xxx-xxxx format
        'phone_number_full' may generate an international number with different format

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        if type(data_type)!=str:
            print("Data type not understood. No series generated")
            return None
        try:
            num=int(num)
        except:
            print('Number of samples not understood, terminating...')
            return None
        if num<=0:
            print("Please input a positive integer for the number of examples")
            return None
        else:
            import pandas as pd
            num=int(num)
            fake=self.fake
            fake.seed(self.seed)
            lst = []
            
            # Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
            if data_type=='name':
                for _ in range(num):
                    lst.append(fake.name())
                return pd.Series(lst)
            if data_type=='country':
                for _ in range(num):
                    lst.append(fake.country())
                return pd.Series(lst)
            if data_type=='street_address':
                for _ in range(num):
                    lst.append(fake.street_address())
                return pd.Series(lst)
            if data_type=='city':
                for _ in range(num):
                    lst.append(fake.city())
                return pd.Series(lst)
            if data_type=='real_city':
                for _ in range(num):
                    lst.append(self.city_real())
                return pd.Series(lst)
            if data_type=='state':
                for _ in range(num):
                    lst.append(fake.state())
                return pd.Series(lst)
            if data_type=='zipcode':
                for _ in range(num):
                    lst.append(fake.zipcode())
                return pd.Series(lst)
            if data_type=='latitude':
                for _ in range(num):
                    lst.append(fake.latitude())
                return pd.Series(lst)
            if data_type=='longitude':
                for _ in range(num):
                    lst.append(fake.longitude())
                return pd.Series(lst)
            
             
            # Month, weekday, year, time, date
            if data_type=='name_month':
                for _ in range(num):
                    lst.append(fake.month_name())
                return pd.Series(lst)
            if data_type=='weekday':
                for _ in range(num):
                    lst.append(fake.day_of_week())
                return pd.Series(lst)
            if data_type=='year':
                for _ in range(num):
                    lst.append(fake.year())
                return pd.Series(lst)
            if data_type=='time':
                for _ in range(num):
                    lst.append(fake.time())
                return pd.Series(lst)
            if data_type=='date':
                for _ in range(num):
                    lst.append(fake.date())
                return pd.Series(lst)
            
            # SSN
            if data_type=='ssn':
                for _ in range(num):
                    lst.append(fake.ssn())
                return pd.Series(lst)
            
            # Personal, official email
            if data_type=='email':
                for _ in range(num):
                    lst.append(fake.email())
                return pd.Series(lst)
            if data_type=='office_email':
                for _ in range(num):
                    lst.append(fake.company_email())
                return pd.Series(lst)
            
            # Company, Job title
            if data_type=='company':
                for _ in range(num):
                    lst.append(fake.company())
                return pd.Series(lst)
            if data_type=='job_title':
                for _ in range(num):
                    lst.append(fake.job())
                return pd.Series(lst)
            
            # Phone number, license plate (3 styles)
            if data_type=='phone_number_simple':
                for _ in range(num):
                    lst.append(self.simple_ph_num())
                return pd.Series(lst)
            if data_type=='phone_number_full':
                for _ in range(num):
                    lst.append(fake.phone_number())
                return pd.Series(lst)
            if data_type=='license_plate':
                for _ in range(num):
                    lst.append(self.license_plate())
                return pd.Series(lst)

    def gen_dataframe(self,num=10,fields=['name'], real_email=True, real_city=True, phone_simple=True, seed=None):
        """
        Generate a pandas dataframe filled with random entries. 
        User can specify the number of rows and data type of the fields/columns
        
        Data types available: 
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN 
        - Company, Job title, phone number, license plate

        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real US city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit US number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        try:
            num=int(num)
        except:
            print('Number of samples not understood, terminating...')
            return None
        if num <= 0:
            print("Please input a positive integer for the number of examples")
            return None
        else:
            import pandas as pd
            from random import randint,choice
            num_cols=len(fields)
            if num_cols==0:
                print("Please provide at least one type of data field to be generated")
                return None
            else:
                df = pd.DataFrame(data=self.gen_data_series(num,data_type=fields[0]),columns=[fields[0]])
                for col in fields[1:]:
                    if col=='phone': 
                        if phone_simple==True:
                            df['phone-number']=self.gen_data_series(num,data_type='phone_number_simple')
                        else:
                            df['phone-number']=self.gen_data_series(num,data_type='phone_number_full')
                    elif col=='license_plate':
                        df['license-plate']=self.gen_data_series(num,data_type=col)
                    elif col=='city' and real_city==True:
                        df['city']=self.gen_data_series(num,data_type='real_city')
                    else:
                        df[col]=self.gen_data_series(num,data_type=col)
                
                if ('email' in fields) and ('name' in fields) and (real_email==True):
                        df['email']=df['name'].apply(self.realistic_email)
                
                return df

    def gen_table(self,num=10,fields=['name'],db_file=None,table_name=None,primarykey=None,real_email=True, real_city=True, phone_simple=True, seed=None):
        """
        Attempts to create a table in a database (.db) file using Python's built-in SQLite engine.
        User can specify various data types to be included as database table fields.
        All data types (fields) in the SQLite table will be of VARCHAR type.
        
        Data types available: 
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate
        
        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real US city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit US number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.

        Default database and table name will be chosen if not specified by user.
        Primarykey: User can choose a PRIMARY KEY from among the data type fields. If nothing specified, the first data field will be made PRIMARY KEY.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        try:
            num=int(num)
        except:
            print('Number of samples not understood, terminating...')
            return None
        if num <= 0:
                print("Please input a positive integer for the number of examples")
                return None
        if len(fields)==0:
            print("Please provide at least one type of data field to be generated")
            return None

        import sqlite3
        if db_file==None:
            conn = sqlite3.connect('NewFakeDB.db')
            c=conn.cursor()
        else:
            conn = sqlite3.connect(str(db_file))
            c=conn.cursor()

        if type(primarykey)!=str and primarykey!=None:
            print("Primary key type not identified. Not generating any table")
            return None

        # If primarykey is None, designate the first field as primary key
        if primarykey==None:
            table_cols='('+str(fields[0])+' varchar PRIMARY KEY NOT NULL,' 
            for col in fields[1:-1]:
                table_cols+=str(col)+' varchar,'
            table_cols+=str(fields[-1])+' varchar'+')'
            #print(table_cols)
        else:
            pk = str(primarykey)
            if pk not in fields:
                print("Desired primary key is not in the list of fields provided, cannot generate the table!")
                return None
            
            table_cols='('+str(fields[0])+' varchar, ' 
            for col in fields[1:-1]:
                if col==pk:
                    table_cols+=str(col)+' varchar PRIMARY KEY NOT NULL,'
                else:
                    table_cols+=str(col)+' varchar, '
            table_cols+=str(fields[-1])+' varchar'+')'
            #print(table_cols)

        if table_name==None:
            table_name='Table1'
        else:
            table_name=table_name

        str_drop_table = "DROP TABLE IF EXISTS " + str(table_name) + ';'
        c.execute(str_drop_table)
        str_create_table = "CREATE TABLE IF NOT EXISTS " + str(table_name) + table_cols +';'
        #print(str_create_table)
        c.execute(str_create_table)

        # Create a temporary df
        temp_df = self.gen_dataframe(num=num,fields=fields,real_email=real_email,real_city=real_city,phone_simple=phone_simple)
        # Use the dataframe to insert into the table
        for i in range(num):
            str_insert="INSERT INTO "+table_name+ " VALUES "+ str(tuple(temp_df.iloc[i])) +';'
            c.execute(str_insert)

        # Commit the insertions and close the connection
        conn.commit()
        conn.close()

    def gen_excel(self,num=10, fields=['name'],filename=None,real_email=True, real_city=True, phone_simple=True, seed=None):
        """
        Attempts to create an Excel file using Pandas excel_writer function.
        User can specify various data types to be included as fields.
        
        Data types available: 
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate
        
        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real US city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit US number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.
        
        Default file name will be chosen if not specified by user.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        try:
            num=int(num)
        except:
            print('Number of samples not understood, terminating...')
            return None
        if num <= 0:
            print("Please input a positive integer for the number of examples")
            return None
        if len(fields)==0:
            print("Please provide at least one type of data to be generated")
            return None
        if filename==None:
            fname='NewExcel.xlsx'
        else:
            fname=filename
        
        # Create a temporary dataframe        
        temp_df=self.gen_dataframe(num=num,fields=fields,real_email=real_email,real_city=real_city,phone_simple=phone_simple)
         # Use the dataframe to write to an Excel file using Pandas built-in function
        temp_df.to_excel(fname)