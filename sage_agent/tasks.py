# from crewai import Task
# from textwrap import dedent

# class HandlePaymentTasks:
#     def get_(self, agent, var1, var2):
#         return Task(
#             description=dedent(
#                 f"""
#             Do something as part of task 1
            
#             {self.__tip_section()}
    
#             Make sure to use the most recent data as possible.
    
#             Use this variable: {var1}
#             And also this variable: {var2}
#         """
#             ),
#             agent=agent,
#         )

#     def task_2_name(self, agent):
#         return Task(
#             description=dedent(
#                 f"""
#             Take the input from task 1 and do something with it.
                                       
#             {self.__tip_section()}

#             Make sure to do something else.
#         """
#             ),
#             agent=agent,
#         )
