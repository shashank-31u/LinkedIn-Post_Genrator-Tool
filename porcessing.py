import json


from helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def GeneratePosts(raw_file_path, preprocessed_file_path="data/preprocessed_file_posts.json"):
    converted_posts = []
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        print(posts)
        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata  
            converted_posts.append(post_with_metadata)
 
    with open(preprocessed_file_path,'w',encoding='utf-8') as outfile:
        json.dump(converted_posts, outfile, indent=4)
        

def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.and it should start with #.
    4. Language should be English or Hinglish (Hinglish means hindi + english)
    5.Preserve all special characters, emojis, and symbols exactly as they appear in the input text when generating the response.
    Here is the actual post on which you need to perform this task:  
    {post}
    '''
    prompt = PromptTemplate.from_template(template)
    
    
    chain = prompt | llm  # Fixed chain order
    response= chain.invoke(input={'post': post})
    
    
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse post.")
    return res

if __name__ == "__main__":
    GeneratePosts("data/raw_posts.json", "data/preprocessed_posts.json")
