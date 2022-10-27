import re
import os


# Read and clean the context file
def clean_context(filename):
    with open(filename, 'r', encoding="utf8") as f:
        text = f.read()
    text = re.sub("\\n", ' ', text, re.ASCII)
    text = re.sub("\s{2,}", ' ', text, re.ASCII)
    text = re.sub("“|”", '"', text, re.ASCII)
    text = re.sub("‘|’", "'", text, re.ASCII)
    text = re.sub("\"", '\\"', text, re.ASCII)
    text = re.sub("_", '', text, re.ASCII)
    text = re.sub("\s{2,}", ' ', text, re.ASCII)
    text = text.strip()
    return text


# Create a custom sample in the squad format
def add_squad_sample(samples, title, context, question, answer):
    if answer not in context:
        print(f'Could not find answer({answer}) in context')
        return samples
    answer_start = context.index(answer)
    id = "abcdefg"  # IDK what to do with the id here
    d = {
        'id': id,
        'title': title,
        'context': context,
        'question': question,
        'answers': {
            'text': [answer],
            'answer_start': [answer_start]
        }
    }
    samples.append(d)
    return samples


# takes a dataset and adds our custom samples
def create_custom_squad(dataset):
    samples = create_samples()
    for sample in samples:
        dataset = dataset.add_item(sample)
    return dataset


# creates a list of custom samples
def create_samples():
    samples = []

    ########################################################################
    # Protagonist Questions
    context = clean_context(os.path.join('text', 'protagonist-first-paragraph.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What is a characteristic of Sherlock Holmes?',
                               answer='usually very late in the mornings'
                               )

    ########################################################################
    # Crime Scene Questions
    context = clean_context(os.path.join('text', 'crimescene.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What habit does Sir Charles of Baskerville have?',
                               answer='in the habit every night before going to bed of walking down the famous yew '
                                      'alley of Baskerville Hall '
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What was Sir Charles doing the night of his murder?',
                               answer='That night he went out as usual for his nocturnal walk, in the course of which '
                                      'he was in the habit of smoking a cigar '
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question="How was Sir Charles's body found?",
                               answer="Charles's footmarks were easily traced down the alley."
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question="Did anyone hear what happened to Sir Charles?",
                               answer="heard cries but is unable to state from what direction they came"
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question="Was there anything interesting about the victims body?",
                               answer="No signs of violence were to be discovered upon Sir Charles's person, "
                                      "and though the doctor's evidence pointed to an almost incredible facial "
                                      "distortion "
                               )
    context = clean_context(os.path.join('text', 'crimescene2.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='How did Sir Charles die?',
                               answer='affection of the heart'
                               )
    ########################################################################
    # Antagonist Questions
    context = clean_context(os.path.join('text', 'stapleton.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What ideology doe Stapleton follow?',
                               answer='naturalist.'
                               )

    ########################################################################
    # Resolution Questions
    context = clean_context(os.path.join('text', 'stapleton-murder.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='How did Stapleton kill Sir Charles?',
                               answer='get his hound, to treat it with his infernal paint, and to bring the beast '
                                      'round to the gate at which he had reason to expect that he would find the old '
                                      'gentleman waiting. The dog, incited by its master, sprang over the wicket-gate '
                                      'and pursued the unfortunate baronet, who fled screaming down the yew alley. In '
                                      'that gloomy tunnel it must indeed have been a dreadful sight to see that huge '
                                      'black creature, with its flaming jaws and blazing eyes, bounding after its '
                                      'victim. '
                               )

    return samples
