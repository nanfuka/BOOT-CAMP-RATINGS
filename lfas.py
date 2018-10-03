import datetime
class  LFAS(object):
    # Declaring variables

    lfas_options = []
    scores_list = []
    
    # Writting a constructor 

    def __init__ (self, options,  scores):
        self.scores_list = scores
        self.lfas_options = options


    def view_options(self):
        option_number = 0
        for specific_option in self.lfas_options:
            print(str(option_number) + ":" +specific_option )
            option_number += 1
        print("")
        print("")
        choosen_option = raw_input("Select Action To Perform By Number\n")

        if choosen_option == 0:
            lfa.view_scores
        print("Option not yet completed")
        

    def view_scores(self):
        for score in self.scores_list:
            print(score)


given_options = ["view scores ", "add scores", "edit candidates scores."]
candidate_score = [
    {
         "Date":datetime.datetime.today().strftime('%Y-%m-%d'),
         "name":"francis kiryowa",
         "score":70
    }
]
lfa = LFAS(given_options,candidate_score)

lfa.view_options()