import requests


class Category:
    def __init__(self, name):
        self.name = name
        self.url = "https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/{}".format(name)
        self.questions = []
        

    def download(self):
        response = requests.get(self.url)
        if not response.status_code == 200:
            exit("Category download failed. {}".format(response.status_code))
        else:
            print("Category download succeeded.")
        
        # Remove any extra empty space at the beginning or end of the text,
        # and split into questions
        raw_questions = response.text.strip().split("#Q")
        print("Downloaded {} questions.".format(len(raw_questions)))

        # Ignore the first question_string as it is empty, and process the rest
        for question_string in raw_questions[1:]:
            q_object = Question(question_string.strip())
            self.questions.append(q_object)
        
        print("Processed {} questions.".format(len(self.questions)))


    def random_question(self):
        pass



class Question:
    def __init__(self, question_string):
        # Slice the string from the beginning until the position of the ^ character
        # and removed the extra newline at the end
        text_end_index = question_string.index("^")
        self.text = question_string[:text_end_index].strip()
        
        def remove_two(string):
            return string[2:]
        
        # Extract the correct anwer and all answers from the question string
        answers_string = question_string[text_end_index:]
        # Remove the first two characters from each line, and then save into the
        # appropriate variables
        self.correct, *self.answers = map(remove_two, answers_string.splitlines())




# Quiz class with a data structure to hold all category objects




animals = Category("animals")
animals.download()
