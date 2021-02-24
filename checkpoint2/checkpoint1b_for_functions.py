"""
Checkpoint 1b

*First complete the steps in checkpoint1a.pdf

Here you will create a script to preprocess the data given in starbucks.csv. You may want to use
a jupyter notebook or python terminal to develop your code and test each function as you go... 
you can import this file and its functions directly:

    - jupyter notebook: include the lines `%autoreload 2` and `import checkpoint1b`
                        then just call checkpoint1b.remove_percents(df) to test
                        
    - python terminal: run `from importlib import reload` and `import preprocess`
                       each time you modify this file, run `reload(preprocess)`

Once you are finished with this program, you should run `python preprocess.py` from the terminal.
This should load the data, perform preprocessing, and save the output to the data folder.

"""
import pandas as pd

def give_back_one(a):
    return 2  
  
def remove_percents(df, col): 
    for j in range(df[col].size):
        if(isinstance(df.at[j, col], str)):
            a = int(float(df.at[j, col].replace('%','')))
            df.at[j, col] = a
    return df


def fill_zero_iron(df):
    col = 'Iron (% DV)'
    length = df[col].size
    for i in range(length):
         if(df.isnull().at[i, col]):
            df.at[i, col] = 0
    return df
 
def fix_caffeine(df):
    col = 'Caffeine (mg)'
    length = df[col].size
    total = 0
    num = 0
    for i in range(length):
        if(not(df.at[i, col] == 0 or df.at[i, col] == 'Varies' or df.at[i, col] == 'varies' or df.isnull().at[i, col])):
            total += int(df.at[i, col])
            num += 1
    ave = total/num
    for i in range(length):
        if(df.at[i, col] == '0' or df.at[i, col] == 'Varies' or df.at[i, col] == 'varies' or df.isnull().at[i, col]):
            df.at[i, col] = ave
    return df

def standardize_names(df):
    mod = (df.columns).to_numpy()
    for i in range(len(mod)):
        string = mod[i].casefold()
        string = string.split('(')[0]
        mod[i] = string
    df.columns = mod
    return df

def fix_strings(df, col):
    for i in range(df[col].size):
        string = (df.at[i, col]).casefold()
        remove = []
        for j in range(len(string)):
            if(not((ord(string[j]) >= 97) and (ord(string[j]) <= 122))):
                remove.append(string[j])
        remove.reverse()
        for k in range(len(remove)):
            string = string.replace(remove[k],'')
        df.at[i, col] = string
    return df


def main():
    
    # first, read in the raw data
    df = pd.read_csv('../data/starbucks.csv')
    
    # the columns below represent percent daily value and are stored as strings with a percent sign, e.g. '0%'
    # complete the remove_percents function to remove the percent symbol and convert the columns to a numeric type
   
    pct_DV = ['Vitamin A (% DV)', 'Vitamin C (% DV)', 'Calcium (% DV)', 'Iron (% DV)']
    for col in pct_DV:
        df = remove_percents(df, col)
    
    # the column 'Iron (% DV)' has missing values when the drink has no iron
    # complete the fill_zero_iron function to fix this
    
    df = fill_zero_iron(df)

    # the column 'Caffeine (mg)' has some missing values and some 'varies' values
    # complete the fix_caffeine function to deal with these values
    # note: you may choose to fill in the values with the mean/median, or drop those values, etc.
    
    df = fix_caffeine(df)
    
    # the columns below are string columns... starbucks being starbucks there are some fancy characters and symbols in their names
    # complete the fix_strings function to convert these strings to lowercase and remove non-alphabet characters
    
    names = ['Beverage_category', 'Beverage']
    for col in names:
        df = fix_strings(df, col)
    
    # the column names in this data are clear but inconsistent
    # complete the standardize_names function to convert all column names to lower case and remove the units (in parentheses)
    
    df = standardize_names(df)
    
    # now that the data is all clean, save your output to the `data` folder as 'starbucks_clean.csv'
    # you will use this file in checkpoint 2
    
    

if __name__ == "__main__":
    main()
