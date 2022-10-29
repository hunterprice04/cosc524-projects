import sys

def qa(pipeline, sample, verbose=True):
    context = sample['context']
    q = sample['question']
    a = sample['answers']['text'][0]
    a_hat = pipeline(context=context, question=q)

    if verbose:
        print(f'QUESTION: "{q}"')
        print(f'GROUND TRUTH: "{a}"')
        print(f"PREDICTED: \"{a_hat['answer']}\"")
        print(f"SCORE: \"{a_hat['score']}\"")
    return a_hat


def print_answer(i, answer, n=None, file=sys.stdout):
    sample, pred = answer
    print('*'*100, file=file)
    print(f"\nQUESTION #{i}:", file=file)
    print(f"\"{sample['question']}\"\n", file=file)
    print(f"GROUND TRUTH ANSWER:", file=file)
    print(f"\"{sample['answers']['text'][0]}\"\n", file=file)
    print(f"PREDICTED ANSWER (score={pred['score']}):", file=file)
    print(f"\"{pred['answer']}\"\n", file=file)
    if n is not None and i >= n-1:
        print('*'*100, file=file)

