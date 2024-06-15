class BaseClass:

    def __init__(self, file):

        self.file = file
        
        self.assesment = {

            "award":{"evidence":'', "rating":''},
            "membership":{"evidence":'', "rating":''},
            "press":{"evidence":'', "rating":''},
            "judge":{"evidence":'', "rating":''},
            "original_contribution":{"evidence":'', "rating":''},
            "paper":{"evidence":'', "rating":''},
            "job_title":{"evidence":'', "rating":''},
        }

        self.text = ''