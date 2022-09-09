import argparse
import pandas as pd
from word_count import read_topics

TOPICS = read_topics()
SENTIMENTS = ['positive','neutral','negative']

def load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--start',required = True)
    parser.add_argument('-i','--input', required = True)
    parser.add_argument('-o','--output', required = True)
    args = parser.parse_args()
    return args

def load_data(filename):
    data = pd.read_csv(filename)

def print_loop_directions():
    print("\t\t~Press ENTER DIRECTLY to keep annotating or ENTER ANY OTHER KEY to exit.~\n" )

def print_encoding_directions(encoding):
    print("ENTER the number corresponding to the following encoding:")
    for i, e in enumerate(encoding):
        print(f"{i} - {e}")
        
def get_annotation(encoding):
    print("ENTER value:",end = " ")
    try:
        i = int(input())
        return encoding[i]
    except:
        print(f"\nERROR: invalid topic, try again.\n")
        return get_annotation(encoding)
    
def annotate(tweets,index):
    print(f"TWEET {index}:")
    print(f"{tweets.iloc[index]['text']}\n")
    
    print_encoding_directions(TOPICS)
    tweets.at[index,'topic'] = get_annotation(TOPICS)
    print()
    print_encoding_directions(SENTIMENTS)
    tweets.at[index,'sentiment'] = get_annotation(SENTIMENTS)
    print()
    
       
def main():
    args = load_args()
    tweets = pd.read_csv(args.input)
    tweets['topic'] = tweets['topic'].astype(str)
    tweets['sentiment'] = tweets['sentiment'].astype(str)
    index = int(args.start)
    
    print_loop_directions()
    STOP = input()
    while not STOP and index < len(tweets):
        annotate(tweets,index)
        index += 1
        print_loop_directions()
        STOP = input()
        
    tweets.to_csv(args.output,index=False)
    
if __name__ == '__main__':
    main()
