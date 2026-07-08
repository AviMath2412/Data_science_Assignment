from agent.validator import Validator
from agent.router import Router
from agent.verifier import Verifier
from agent.logger import Logger
import time
from tools.calculator import Calculator
from tools.keyword_extractor import KeywordExtractor
from tools.text_statistics import TextStatistics
from agent.memory import Memory

class Agent:
    def __init__(self):
        self.validator = Validator()
        self.router = Router()
        self.verifier = Verifier()
        self.logger = Logger()
        self.calculator = Calculator()
        self.keyword_extractor = KeywordExtractor()
        self.text_statistics = TextStatistics()
        self.memory = Memory()
    def process(self, query: str):
        start_time = time.perf_counter()
        valid, validation_message = self.validator.validate(query)
        if not valid:
            print(validation_message)
            return
        if query.lower() == "history":
            return self.memory.get_history()
        intent = self.router.route(query)
        if intent == "calculator":
            expression = (
                query.lower()
                .replace("calculate", "")
                .strip()
            )
            output = self.calculator.evaluate(expression)
            tool_name = "Calculator"
        elif intent == "keywords":
            output = self.keyword_extractor.extract(query)
            tool_name = "Keyword Extractor"
        elif intent == "statistics":
            output = self.text_statistics.analyze(query)
            tool_name = "Text Statistics"
        else:
            output = "Sorry, I don't have a suitable tool for this request."
            tool_name = "General Response"
        success, verification_message = self.verifier.verify(output)
        execution_time = round(time.perf_counter() - start_time, 4)
        self.logger.log_execution(
            query=query,
        validation_status=validation_message,
        intent=intent,
        tool_name=tool_name,
        output=str(output),
        verification_status=verification_message,
        execution_time=execution_time
        )
        self.memory.add(query, output)
        return output
if __name__ == "__main__":
    agent = Agent()
    while True:
        print("\n==============================")
        query = input("Enter your query (type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.process(query)
        print("\nFinal Response:")
        print(response)