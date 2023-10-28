import autogen
from agent import LMStudioAgent

SEED = 1110

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    file_location=".",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)
mistralAssistant = [{
    "api_type": "open_ai",
    "api_base": "http://localhost:1234/v1",
    "api_key": "NULL",
}]


# assistants_configuration = {"config_list": mistralAssistant, "seed": SEED}
assistants_configuration = {"config_list": config_list, "seed": SEED}


llm_config = {
    "request_timeout": 160,
    "config_list": config_list,
     "seed": 22,
    "use_cache": True,  # Use False to explore LLM non-determinism.
}

def check_termination(x):
    if "content" in x and x["content"] is not None:
        if x["content"].endswith("TERMINATE"):
            return True
    return False


user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    code_execution_config={"last_n_messages": 10, "work_dir": "systemdesign", "use_docker": False,},
    human_input_mode="NEVER",
    default_auto_reply="default_auto_reply",
    max_consecutive_auto_reply=1,
    is_termination_msg=check_termination
)


assistant = LMStudioAgent(
    name="Software Engineer",
    system_message="""You are a Software Engineer.
      You are planning to build a company from scratch. 
      You are suppose to include all possible requirements and you can answer from your knowledge.""",
    llm_config=assistants_configuration,
    default_auto_reply="default_auto_reply",
)


autogen.ChatCompletion.start_logging()
# Reqs gathering
task1 = """
Assume you are building a system deign for a company, give functional and non functional requirements 
and brainstorm on all possible stuffs to keep in mind(highlight main ones) and 
also write the content in a markdown file by name functions.md. Question: Flipkart backend system design
"""
user_proxy.initiate_chat(assistant, message=task1)

# Calcs 
task2 = """
 for the same, give me the Requests Per Second, storage, bandwidth requirements assuming 1 billion DAUs with explanation,
 also give a generic python code that takes in DAUs but dont execute it and prints other details 
 and also write the content in a markdown file by name calc.md"""
user_proxy.initiate_chat(assistant, message=task2, clear_history=False)

# HLD
task3 = """ 
 for the same, give simple intro of top level HLD with detailed data flow using latest technologies with mermaid code 
 and also write the content in a markdown file by name hld.md""" 
user_proxy.initiate_chat(assistant, message=task3, clear_history=False)

# LLD
task4 = """
 for the same,Create an Entity-Relationship (ER) diagram with detailed db schema with relationships, 
sample apis(with data types) and major services and also  write the content in a markdown file by name lld.md"""
user_proxy.initiate_chat(assistant, message=task4, clear_history=False)

# algos
task5 = """ 
 for the same, explain the  Low level design of critical services involved and possible algorithms 
   and also write the content in a markdown file by name algos.md"""
user_proxy.initiate_chat(assistant, message=task5, clear_history=False)

# failures
task6 = """ 
    for the same, list all possible single point of failures and solutions for the same and
      also write the content in a markdown file by name failures.md"""
user_proxy.initiate_chat(assistant, message=task6, clear_history=False)

task7 = """Reflect on the sequence and create a recipe containing all the above steps 
necessary and name for it. Suggest well-documented, generalized python function(s)
 to perform similar tasks for coding steps in future. Make sure coding steps and 
 non-coding steps are never mixed in one function. In the docstr of the function(s),
 clarify what non-coding steps are needed to use the language skill of the assistant.
"""
user_proxy.initiate_chat(assistant, message=task7, clear_history=False)


