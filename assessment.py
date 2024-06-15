from base import BaseClass
from openai_client import OpenAIClient
from pdfparser import Parser
import ast
import concurrent.futures

class Assesor(BaseClass):

    def __init__(self, file):
        
        super().__init__(file)
        self.pdf_parser = Parser(self.file)
        self.pdf_parser.parser()
        self.text = self.pdf_parser.text
    
    def get_response(self, criteria):

        openai_client = OpenAIClient()
        prompt = openai_client.generate_prompt(self.text, criteria)
        reponse = openai_client.generate_completion(prompt)
        output = ast.literal_eval(reponse)

        if criteria == 'award': 
            if len(output['International']) != 0:
                self.assesment['award']['rating'] = 'high'
                self.assesment['award']['evidence'] = output['International']
            else:
                if len(output['National']) >= 2:
                    self.assesment['award']['rating'] = 'high'
                elif  len(output['National']) >= 1 and len(output['National']) < 2:
                    self.assesment['award']['rating'] = 'medium'
                else:
                    self.assesment['award']['rating'] = 'low'
                self.assesment['award']['evidence'] = output['National']
        else:
            if len(output) >= 2:
                self.assesment[criteria]['rating'] = 'high'
            elif  len(output) >= 1 and len(output) < 2:
                self.assesment[criteria]['rating'] = 'medium'
            else:
                self.assesment[criteria]['rating'] = 'low'
            self.assesment[criteria]['evidence'] = output

        return self.assesment
    
    def run_parallel_responses(self):
        criteria_list = ["award", "membership", "press", "judge", "original_contribution", "paper", "job_title"]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.get_response, criteria): criteria for criteria in criteria_list}
            for future in concurrent.futures.as_completed(futures):
                criteria = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"{criteria} generated an exception: {e}")

    
    def calculate_final_score(self):
        # Count the ratings
        high_count = 0
        medium_count = 0
        for category in self.assesment.values():
            if category["rating"] == 'high':
                high_count += 1
            elif category["rating"] == 'medium':
                medium_count += 1
        
        rating = ''
        # Apply the scoring logic
        if high_count >= 2 and medium_count >= 1:
            rating =  'high'
        elif medium_count >= 2:
            rating = 'medium'
        else:
            rating = 'low'
        
        evidence = []
        for criteria in self.assesment.keys():
            if self.assesment[criteria]['evidence'] != '':
                evidence += self.assesment[criteria]['evidence']
        
        return rating, evidence
    

    
# pdf_path = 'cv.pdf'
# assesor = Assesor(pdf_path)

# # print(assesor.run_parallel_responses())
# print(assesor.run_parallel_responses())
# print(assesor.assesment)
# print(assesor.calculate_final_score())