
import re
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import pandas as pd

data = pd.read_csv('C:\\Users\\Admin\\OneDrive - BDO Kosovo Tenant\\Desktop\\Python\\sales_data.csv', encoding='latin-1')

model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break

    # Generate a response using GPT-2
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    if 'maximum' in response:
        match = re.search(r"(?<=maximum of )\w+", response)
        if match:
            column_name = match.group()
            if column_name in data.columns:
                max_value = data[column_name].max()
                result = f"The maximum value in the '{column_name}' column is {max_value}."
            else:
                result = f"Column '{column_name}' not found in the CSV."
        else:
            result = "Unable to determine the column name."

        print("ChatGPT: " + result)

    elif 'minimum' in response:
        match = re.search(r"(?<=minimum of )\w+", response)
        if match:
            column_name = match.group()
            if column_name in data.columns:
                min_value = data[column_name].min()
                result = f"The minimum value in the '{column_name}' column is {min_value}."
            else:
                result = f"Column '{column_name}' not found in the CSV."
        else:
            result = "Unable to determine the column name."

        
        print("ChatGPT: " + result)

    elif 'average' in response:
        
        match = re.search(r"(?<=average of )\w+", response)
        if match:
            column_name = match.group()
            if column_name in data.columns:
                avg_value = data[column_name].mean()
                result = f"The average value in the '{column_name}' column is {avg_value}."
            else:
                result = f"Column '{column_name}' not found in the CSV."
        else:
            result = "Unable to determine the column name."

        print("ChatGPT: "+ result)



    elif "total sum of values in the" in user_input:
        match = re.search(r"'([^']+)'", user_input)
        if match:
            column_name = match.group(1)
            if column_name in data.columns:
                sum_value = data[column_name].sum()
                result = f"The total sum of values in the '{column_name}' column is {sum_value}."
            else:
                result = f"Column '{column_name}' not found in the CSV."
        else:
            result = "Unable to determine the column name."

        print("ChatGPT: " + result)

    elif 'number of rows' in user_input:
        num_rows=len(data)
        result=f"The dataset contains {num_rows} rows"

        print("ChatGPT: " + result)

    elif 'column names' in user_input:
        column_names=data.columns.tolist()
        result = "The column names in the dataset are: " + ", ".join(column_names)
        print("ChatGPT: " + result)
    else:
        print("ChatGPT: " + response)


#1.What is the maximum value in a specific column?
#2.What is the minimum value in a specific column?
#3.What is the average value in a specific column?
#4.What is the total sum of values in a specific column?
#5.How many rows are there in the dataset?
#6.What are the column names in the dataset?

