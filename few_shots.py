import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/preprocessed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)


    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as file:
            posts = json.load(file)
            df = pd.json_normalize(posts)
            self.df = df
            
            df["length"]=df["line_count"].apply(self.new_Category)
            print(self.df)
            all_tags=self.df['tags'].apply(lambda x:x).sum()
            self.unique_tags = list(set(all_tags))
            print(self.unique_tags)

    
    def new_Category(self,line_count):
            if line_count < 12:
                return "Short"
            elif line_count < 25:
                return "Medium"
            else:
                return "Long"
        
    def get_filtered_posts(self, length, language, tag):
        filtered_posts = self.df[(self.df['length'] == length) & 
                                 (self.df['language'] == language) & 
                                 (self.df['tags'].apply(lambda tags: tag in tags))]
        print("___________this is output of fileterd posts ______________",filtered_posts)
        return filtered_posts.to_dict(orient="records")
    
    def get_tags(self):
        return self.unique_tags
        
if __name__ == "__main__":
    FewShots = FewShotPosts()
    posts = FewShots.get_filtered_posts("Long","English","#LLMs")
    print(posts)
