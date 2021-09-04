'''
This program contains reading CustomerWatchTime.csv file and validating each field.
'''
import os


class ReadCustomerWatchTimeFile:

    incorrect_message = ""
    def __init__(self, path_name, file_name):
        self.path_Name = path_name
        self.file_Name = file_name
        print("Class constructor1")

    def file_reading(self):

        Entry_ID = 0
        Customer_ID = 1
        Customer_First_Name = 2
        Customer_Last_Name = 3
        Start_Watch_Time = 4
        End_Watch_Time = 5
        Channel_Number = 6
        Customer_Age = 7

        Correct_Row = ""
        inCorrect_Row = ""
        correct_count =0
        incorrect_count = 0
        global incorrect_message

        # path name to write the correct customer watch time file
        Correct_Row_Path = "C:/Users/sarav/OneDrive/Desktop/SEDAP/tempdir/Customer_CorrectWatchTime.csv"
        if os.path.exists(Correct_Row_Path):
            os.remove(Correct_Row_Path)
        # open the correct customer watch time file to write all the correct entries
        correct_file = open(Correct_Row_Path, 'a')

        # path name to write the Incorrect customer watch time file
        InCorrect_Row_Path = "C:/Users/sarav/OneDrive/Desktop/SEDAP/tempdir/Customer_InCorrectWatchTime.csv"
        if os.path.exists(InCorrect_Row_Path):
            os.remove(InCorrect_Row_Path)

        # open the In-correct customer watch time file to write all the Incorrect entries
        incorrect_file = open(InCorrect_Row_Path, 'a')

        # This is the main Customer_WatchTime file from where we validate each and every record
        file = open(self.path_Name+self.file_Name, 'r')

        #first_line = file.readline()[0:]  #Read just first line from file
        next(file)  # to skip the title first line in the file

        #opening the for loop to read each row by row record.
        for eachRow in file:

            if len(str(eachRow).strip()) > 0:
                row = eachRow.split(',')

                self.incorrect_message = ""
                EntryID_Flag =  self.validate_EntryID(row[Entry_ID], self.incorrect_message)
                Cust_ID_Flag = self.validate_Customer_ID(row[Customer_ID],self.incorrect_message)
                Cust_FName_Flag = self.validate_Customer_FName(row[Customer_First_Name], self.incorrect_message)
                Cust_LName_Flag = self.validate_Customer_LName(row[Customer_Last_Name], self.incorrect_message)
                StartWatchTime_Flag = self.validate_StartWatchTime(row[Start_Watch_Time], self.incorrect_message)
                EndWatchTime_Flag = self.validate_EndWatchTime(row[End_Watch_Time], self.incorrect_message )
                Channel_Number_Flag = self.validate_Channel_Num(row[Channel_Number], self.incorrect_message)
                Cust_Age_Flag = self.validate_Customer_Age(row[Customer_Age], self.incorrect_message)


                # If all flag returns True then the correct watchtime file is written. Else: Incorrect watchtime file is written
                if EntryID_Flag and Cust_ID_Flag and Cust_FName_Flag and Cust_LName_Flag and StartWatchTime_Flag and EndWatchTime_Flag and Channel_Number_Flag and Cust_Age_Flag:
                    result = row[Entry_ID]+","+row[Customer_ID]+","+ row[Customer_First_Name]+","+row[Customer_Last_Name]+","+row[Start_Watch_Time]+","+row[End_Watch_Time]+","+row[Channel_Number]+","+row[Customer_Age]+"\n"
                    #print(" Corret Result  : ", result )
                    self.correct_file_writing(correct_file, result)
                    correct_count = correct_count +1

                else:
                    result1 = row[Entry_ID]+","+row[Customer_ID]+","+ row[Customer_First_Name]+","+row[Customer_Last_Name]+","+row[Start_Watch_Time]+","+row[End_Watch_Time]+","+row[Channel_Number]+","+row[Customer_Age]
                    result1 = result1+","+ self.incorrect_message+"\n"
                    self.incorrect_file_writing(incorrect_file, result1)
                    incorrect_count = incorrect_count + 1


        file.close()
        correct_file.close()
        incorrect_file.close()
        print("No. of Correct Rows  :  ", correct_count)
        print("No. of In-Correct Rows  :  ", incorrect_count)

    # Validation methods start for each and every item in the row.

    def validate_EntryID(self, EID, incorrect_message):
        if EID.isdigit() and int(EID) > 0:
            EntryID_Flag = True
        else:
            self.incorrect_message = self.incorrect_message+"Invalid Entry ID"
            EntryID_Flag = False
        return EntryID_Flag

    def validate_Customer_ID(self, Cust_id, incorrect_message):
        if Cust_id.isdigit() and int(Cust_id) > 0:
            Cust_ID_Flag = True
        else:
            self.incorrect_message = self.incorrect_message + "Invalid Customer ID"
            Cust_ID_Flag = False
        return Cust_ID_Flag

    def validate_Customer_FName(self,CFName, incorrect_message):
        if len(str(CFName).strip()) <= 30 and str(CFName).isalpha():
            Cust_FName_Flag = True
        else:
            self.incorrect_message = self.incorrect_message + "Invalid Customer First Name"
            Cust_FName_Flag = False
        return Cust_FName_Flag

    def validate_Customer_LName(self, CLName, incorrect_message):
        if len(str(CLName).strip())<=30 and str(CLName).isalpha():
            Cust_LName_Flag = True
        else:
            self.incorrect_message = self.incorrect_message + "Invalid Last Name"
            Cust_LName_Flag = False
        return Cust_LName_Flag

    def validate_Channel_Num(self, Ch_Num, incorrect_message):
        if int(Ch_Num) >= 100:
            Channel_Number_Flag = True
        else:
            Channel_Number_Flag = False
            self.incorrect_message = self.incorrect_message + "Invalid Channel Number"
        return Channel_Number_Flag

    def validate_hour_time(self, Hours_Time):
        if int(Hours_Time) >= 0 and int(Hours_Time) <= 23:
            Hours_Flag = True
        else:
            Hours_Flag = False
        return Hours_Flag

    def validate_minutes_time(self, Minutes_Time):
        if int(Minutes_Time) >= 0 and int(Minutes_Time) <= 59:
            Minutes_Flag = True
        else:
            Minutes_Flag = False
        return Minutes_Flag

    def validate_StartWatchTime(self, startwatchtime, incorrect_message):

        if len(startwatchtime)<=3:
            hours_time = startwatchtime[:1]
            minutes_time = startwatchtime[1:]
        else:
            hours_time = startwatchtime[:2]
            minutes_time = startwatchtime[2:]

        if self.validate_hour_time(hours_time) and self.validate_minutes_time(minutes_time):
            StartWatchTime_Flag = True
        else:
            StartWatchTime_Flag = False
            self.incorrect_message = self.incorrect_message + "Invalid hour"

        return StartWatchTime_Flag


    def validate_EndWatchTime(self,endwatchtime, incorrect_message):
        #slicing the whole time into hours and minutes
        if len(endwatchtime) <= 3:
            hours_time = endwatchtime[:1]
            minutes_time = endwatchtime[1:]
        else:
            hours_time = endwatchtime[:2]
            minutes_time = endwatchtime[2:]

        if self.validate_hour_time(hours_time) and self.validate_minutes_time(minutes_time):
            EndWatchTime_Flag = True
        else:
            EndWatchTime_Flag = False
            self.incorrect_message = self.incorrect_message + "Invalid minutes"
        return EndWatchTime_Flag

    def validate_Customer_Age(self, cust_age, incorrect_message):
        if str(int(cust_age)).isdigit():
            Cust_Age_Flag = True
        else:
            Cust_Age_Flag = False
            self.incorrect_message = self.incorrect_message + "Invalid Customer Age"

        return Cust_Age_Flag


    # if all flags are true from all methods then this correct watch time file is written.
    def correct_file_writing(self, correct_file, correct_row):
        #print(correct_row," : Correct rows")
        correct_file.write(correct_row)

    # if either one of the flags is true from the above methods then this In-correct watch time file is written.
    def incorrect_file_writing(self, incorrect_file, incorrect_row):
       incorrect_file.write(incorrect_row)


# Setting File location, File name Creating instance of the class

file_location = "C:/Users/sarav/OneDrive/Desktop/SEDAP/"
file_name ="CustomerWatchTime.CSV"
watchtimefile = ReadCustomerWatchTimeFile(file_location,file_name)
watchtimefile.file_reading()




