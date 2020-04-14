import pandas as pd
from pathlib import Path

def build_vocabulary_map():
    with open('vocabulary.txt', 'r') as vf:
        m = {v: i for i,v in enumerate(vf.read().splitlines())}
    return m

def extract_docId(key):
    split = key.split('_')
    doc, word = split[0], split[1]
    return doc

def extract_wordId(key, vocab):
    split = key.split('_')
    doc, word = split[0], split[1]
    return vocab.get(word, -1)

def process():
    data_path = Path('data/part.dat')
    df = pd.read_csv(data_path, header=0, names=['key','count'], sep='\t', index_col=False)
    vocab = build_vocabulary_map()
    df['docId'] = df['key'].apply(lambda r: extract_docId(r)).astype(str)
    df['wordId'] = df['key'].apply(lambda r: extract_wordId(r, vocab))
    print(df.head())
    df[['docId','wordId','count']].to_csv('processed.csv', index=False, header=False)
    df[['docId','wordId','count']].to_csv('processed_no_header.tsv', sep='\t', index=False, header=False)


if __name__ == '__main__':
    process()
