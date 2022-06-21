import pandas as pd

names = [1,2,3,4,5,6,7,8,9]

orig_file = pd.read_csv("TwitterBot\TwitTrainTexts\leftist_1.txt", names=names, header=None)

orig_file.replace(to_replace="<|startoftext|>", value="", inplace=True)
orig_file.replace(to_replace="<|endoftext|>", value="", inplace=True)
orig_file.replace(to_replace="====================", value="", inplace=True)

orig_file.to_csv("cleaned_leftist.csv", index=False, sep=">")