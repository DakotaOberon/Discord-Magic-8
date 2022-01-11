from random import choice

class Magic8:
    def __init__(self, message):
        self.message = message
        self.question_types = [Personal(), Who(), What(), Where(), When(), Why(), How()]

    def get_question_type(self):
        for qt in self.question_types:
            if qt.check(self.message.content):
                return qt

        return QuestionType()

    async def answer_question(self):
        type = self.get_question_type()
        await self.reply(type.get_answer())

    async def reply(self, reply):
        await self.message.reply(reply)

class QuestionType:
    def __init__(self, starts=[], contains=[]):
        self.startswith = starts
        self.contains = contains

    def check(self, content):
        content = content.lower()
        for x in self.startswith:
            if content.startswith(x):
                return True

        for y in self.contains:
            if y in content:
                return True

        return False

    def list_from_file(self, filename):
        r = []
        with open(f'Magic8/answers/{filename}') as f:
            for line in f:
                r.append(line)
        return r

    def get_answer(self, filename=''):
        if (len(filename) > 0):
            try:
                answers = self.list_from_file(filename)
                return choice(answers)
            except:
                return "I could not find anything on that"
        return "I'm not sure that was a real question"

class Personal(QuestionType):
    def __init__(self):
        super().__init__(contains=['you'])

    def get_answer(self):
        super().get_answer('personal')

class Who(QuestionType):
    def __init__(self):
        super().__init__(['who'])

    def get_answer(self):
        super().get_answer('who')

class What(QuestionType):
    def __init__(self):
        super().__init__(['what'])

    def get_answer(self):
        super().get_answer('what')

class Where(QuestionType):
    def __init__(self):
        super().__init__(['where'])

    def get_answer(self):
        super().get_answer('where')

class When(QuestionType):
    def __init__(self):
        super().__init__(['when'])

    def get_answer(self):
        super().get_answer('when')

class Why(QuestionType):
    def __init__(self):
        super().__init__(['why'])

    def get_answer(self):
        super().get_answer('why')

class How(QuestionType):
    def __init__(self):
        super().__init__(['how'])

    def get_answer(self):
        super().get_answer('how')

class Rhetorical(QuestionType):
    def __init__(self):
        pass
