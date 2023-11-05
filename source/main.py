import autogen

# config_list = autogen.config_list_from_json(
#     "OAI_CONFIG_LIST",
#     filter_dict={
#         "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
#     },
# )

config_list = [
    {
        'model': 'gpt-3.5-turbo-16k',
        'api_key': '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',
    }
]

llm_config={
    "request_timeout":600,
    "seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

user_proxy=autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
    system_message="Reply TERMINATE only if the output is successful, otherwise reply CONTINUE"
)

#Create a chart of Steel Pipes NPS numbers and their inner, outer diameter and wall thicknesses
task=input("Enter your task:")

user_proxy.initiate_chat(
    assistant,
    message=task,
)