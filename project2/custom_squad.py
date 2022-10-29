import re
import os


# Read and clean the context file
def clean_context(filename):
    with open(filename, 'r', encoding="utf8") as f:
        text = f.read()
    text = re.sub("\n", r' ', text)
    text = re.sub(r"\s{2,}", r' ', text)
    text = re.sub(r"“|”", r'"', text)
    text = re.sub(r"‘|’", r"'", text)
    text = re.sub(r"\"", '\\"', text)
    text = re.sub(r"_", r'', text, re.ASCII)
    text = re.sub(r"\s{2,}", r' ', text)
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
                               question='What is the guests occupation?',
                               answer='practitioner'
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='How did Sherlock Holmes see Watson?',
                               answer='well-polished, silver-plated coffee-pot'
                               )
    samples = add_squad_sample(samples,
                                 title="The Hound of the Baskervilles",
                                    context=context,
                                    question='What did Holmes and Watson inspect?',
                                    answer="visitor's stick"
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="Where was Sherlock Holmes sitting?",
                                    answer='at the breakfast table'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="When does Sherlock Holmes usually wake up?",
                                    answer='very late in the mornings'
                                    )

    ########################################################################
    # Crime Scene Questions
    context = clean_context(os.path.join('text', 'crimescene.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What habit does Sir Charles of Baskerville have?',
                               answer='in the habit every night before going to bed of walking down the famous yew '
                                      'alley of Baskerville Hall'
                               )
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What was Sir Charles doing the night of his murder?',
                               answer='That night he went out as usual for his nocturnal walk, in the course of which '
                                      'he was in the habit of smoking a cigar'
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
                                      "distortion"
                               )
    context = clean_context(os.path.join('text', 'crimescene2.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='How did Sir Charles die?',
                               answer='affection of the heart'
                               )
    samples = add_squad_sample(samples,
                                 title="The Hound of the Baskervilles",
                                    context=context,
                                    question='Who died?',
                                    answer='Sir Charles'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question='Was there any sign of foul play?',
                                    answer='no reason whatever to suspect foul play'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="Who corroborated the doctor's findings?",
                                    answer='several friends'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="What did the doctor say about the body?",
                                    answer='natural causes'
                                    )
    ########################################################################
    # Antagonist Questions
    context = clean_context(os.path.join('text', 'stapleton.txt'))
    samples = add_squad_sample(samples,
                               title="The Hound of the Baskervilles",
                               context=context,
                               question='What ideology does Stapleton follow?',
                               answer='naturalist.'
                               )
    samples = add_squad_sample(samples,
                                 title="The Hound of the Baskervilles",
                                    context=context,
                                    question='How did Stapleton know Sherlock Holmes?',
                                    answer='I have been calling on Mortimer, and he pointed you out to me'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question='Who did Stapleton ask about?',
                                    answer='Sir Henry'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="What did Stapleton know about Sir Charles?",
                                    answer='his heart was weak'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="What house did Stapleton live in?",
                                    answer='Merripit House'
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
                                      'victim.'
                               )
    samples = add_squad_sample(samples,
                                 title="The Hound of the Baskervilles",
                                    context=context,
                                    question='Who did Stapleton hope would lure Sir Charles out?',
                                    answer='his wife'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question='What did Stapleton do to the hound?',
                                    answer='treat it with his infernal paint'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question='How did the hound get to the victim?',
                                    answer='sprang over the wicket-gate and pursued'
                                    )
    samples = add_squad_sample(samples,
                                    title="The Hound of the Baskervilles",
                                    context=context,
                                    question="What did Stapleton do at first?",
                                    answer='lurked about with his hound, but without avail'
                                    )
    return samples
