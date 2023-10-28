import argparse
import autogen
import sys   

from agent import LMStudioAgent
SEED = 234911001

# Create a parser and add the --design argument
parser = argparse.ArgumentParser()
parser.add_argument("--design", help="Design name", required=True)
args = parser.parse_args()

# Store the value of the --design argument in a variable
design_name = args.design


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


assistants_configuration = {"config_list": config_list, "seed": SEED}


# llm_config = {
#     "request_timeout": 160,
#     "config_list": config_list,
#      "seed": 22,
#     "use_cache": True,  # Use False to explore LLM non-determinism.
# }

def check_termination(x):
    if "content" in x and x["content"] is not None:
        if x["content"].endswith("TERMINATE"):
            return True
    return False


user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    code_execution_config={"last_n_messages": 10, "work_dir": f"groupchat", "use_docker": False,},
    human_input_mode="NEVER",
    default_auto_reply="default_auto_reply",
    max_consecutive_auto_reply=5,
    is_termination_msg=check_termination
)



assistant = LMStudioAgent(
    name="Google Software Engineer",
    system_message="""You are a Google Software Engineer.
      You are giving a mock interview to Facebook. 
      You are suppose to answer the system design interview question and you can answer from your knowledge.""",
    llm_config=assistants_configuration,
    default_auto_reply="default_auto_reply",
)



autogen.ChatCompletion.start_logging()
task1 = f'''
<begin recipe>
**Recipe Name:** System design 

**Steps:**
1. Define functional and non-functional requirements.
2. Identify possible questions to ask the interviewer for more information.
3. Give the estimates for  Requests Per Second, Storage, and Bandwidth requirements assuming 1 Million DAUs.
4. Create a high-level design (HLD) with top-level components, data flow and write the mermaid code.
5. Design the Low-level design components:
   - Entity-Relationship (ER) diagram in mermaid code with detailed database schema.
   - Sample APIs with data types and major services involved.
   - Low-level design of critical services and explain core algorithms involved.
6. Identify potential single points of failure and their respective solutions.
7. Write down the above data to a file
</end recipe>


Here is a new task:
Give me system design for: {design_name} system design
'''

def initiate_chat_with_message(message):
    completed_task = user_proxy.initiate_chat(assistant, message=message)
    print(f"\n\n\n\n\nCompleted Tak:")
    print(completed_task)

# Save the original stdout
original_stdout = sys.stdout

# Open a file in write mode
with open(f"{design_name.replace(' ', '_')}.md", "w") as file:
    # Redirect stdout to the file
    sys.stdout = file

    # Run the function that prints to the terminal
    print(design_name, task1)
    initiate_chat_with_message(task1)

# Reset stdout to its original value
sys.stdout = original_stdout
