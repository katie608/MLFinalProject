
""" Writing to an excel sheet using Python"""
import xlwt # allows writing to excel
import xlrd # allows reading excel
from xlwt import Workbook
import re
import os
import pandas as pd

unwanted_words = [
    "javascript",
    "google",
    "src",
    "cookies",
    "log in",
    "copyright",
    "notify me of",
    "you are commenting using",
    "your comment here",
    "twitterfacebook",
    "save my name, email, and website in this browser for the next time i comment",
    "by continuing to use this website",
    "nofity me of new",
    "wordpress"]

def get_sentences(filename):
    """
    Read all lines from `filename` and return a list of strings, with each
    string a sentence. Sentences are defined as being separated by ". "
    """
    print("Getting Sentences from: " + filename)
    sentence_list = []

    with open(filename) as fp:
        for line in fp:
            processed_line = line.strip('#$%&()*+-/:;""''<=>@[\]^_`{|}~')
            i=0
            j=0
            while i < len(processed_line):
                if processed_line[i] == ".":
                    sentence = processed_line[j:i]
                    sentence = sentence.strip('.')
                    sentence = sentence.lower()
                    if sentence != "":
                        sentence_list.append(sentence)
                        j = i
                    i+=1
                else:
                    i += 1
    return sentence_list


def make_spreadsheet(directory, label):
    """ Takes in a directory and a label (of either 1 or 0 now) and makes
    a spreadsheet where the first column is an id, the second is the label,
    and the third is a sentence from the text files in the directory
    """
    filenames_list = os.listdir(directory)
    print(filenames_list)

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    counter = 0;
    sheet1.write(counter, 0, "id")
    sheet1.write(counter, 1, "label")
    sheet1.write(counter, 2, "text")
    counter += 1;

    for i in range (len(filenames_list)):
        sentence_list = get_sentences(directory+"/"+filenames_list[i])
        for j in range (len(sentence_list)):
            # searches unwanted_words list for unwanted words
            containsUnwantedWord = bool([word for word in unwanted_words if(word in sentence_list[j])])
            if len(sentence_list[j]) > 5 and not containsUnwantedWord:
                if "javascript" in sentence_list[j]:
                    print(sentence_list[j])
                # code for writing to make_spreadsheet: write(row, column, text)
                sheet1.write(counter, 0, str(counter) + "_"+ str(label))
                sheet1.write(counter, 1, label)
                sheet1.write(counter, 2, sentence_list[j])
                counter += 1

    # save and close spreadsheet
    wb.save(directory+'-data.xls')


def mergeSpreadsheets(spreadsheet1, spreadsheet2, title):
    """Takes 2 spreadsheets and puts them togeteher"""
    # Read all three files into pandas dataframes
    wb1 = pd.read_excel(spreadsheet1)
    wb2 = pd.read_excel(spreadsheet2)

    # Create a list of the files in order you want them appended
    all_df_list = [wb1, wb2]

    # Merge all the dataframes in all_df_list
    # Pandas will automatically append based on similar column names
    appended_df = pd.concat(all_df_list)

    # Write the appended dataframe to an excel file
    # Add index=False parameter to not include row numbers
    appended_df.to_excel(title+".xls", index=False)




# Run this code when called from the command line
if __name__ == "__main__":
    import doctest
    make_spreadsheet("pro-recovery", 0)
    make_spreadsheet("pro-ana", 1)
    mergeSpreadsheets("pro-recovery-data.xls", "pro-ana-data.xls", "data")


    # Run all doctests in this file
    doctest.testmod()
