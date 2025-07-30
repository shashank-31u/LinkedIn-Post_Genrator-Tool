
from helper import llm
from few_shots import FewShotPosts

fs=FewShotPosts()
def get_posts_length(length):
    if length=="short":
        return "1 to 12 lines"
    if length=="medium":
        return "12 to 25 lines"
    if length=="long":
        return "25 to 50 lines"
    
    
    
def genrateposts(length,language,tag):
     prompt=get_prompt(length,language,tag)
     response =llm.invoke(prompt)
     return response.content
    
def get_prompt(length, language, tag):
    length_str=get_posts_length(length)
    
    
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    
    examples = fs.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

        return prompt
    
if __name__=="__main__":
    print("---------------------This is the genrated posts-------------------------------",genrateposts("Long","English","#AI"))