from typing import Any, Dict
from progress import PersonalProgress
from asyncio import sleep
import re
from datetime import datetime

class ProgressBot:
     """
     Authorize bot in discord and gives instructions via discrod API. For simplicity we represent conversation inside as ConversationTree. Since this
     bot can be used on server with a lot of people we also need create unique ConversationTree for each user by their userid. Due to how Python
     works, we don't create new tree over and over again, we just create a lot of pointers to existing nodes, which means that our bot doesn't consume
     tremendous amounts of memory
     """
     def __init__(self, TOKEN, client, personal_progresses: Dict[str, PersonalProgress] = {}, save_threshold: int = 10) -> None:
          # personal progresses dictionary with userids as keys
          self.personal_progresses = personal_progresses 
          self.save_threshold = save_threshold
          self.attributes = {}
          
          # necessary info for running bot
          self.TOKEN = TOKEN 
          self.client = client

          self.id = client.user # id of bot

    
    
    #  async def get_conversation(self):
    #       userid = self.attributes['userid']

    #       if userid not in self.conversations.keys():
    #            self.conversations[userid] = ConversationTree(self.tree_root)
    #       return self.conversations[userid]
     
    #  async def handle_messages(self): 
    #        conversation = await self.get_conversation()
    #        user_reply = self.attributes['user_message']

    #        return conversation.get_answer(user_reply, self.attributes)

     async def handle_messages(self):
        message = self.attributes['user_message']
        message = message.split()
        ID = self.attributes['userid']
        if ID not in self.personal_progresses:
            self.personal_progresses[ID] = PersonalProgress(path= ID + '.json', ID=ID, save_threshold=self.save_threshold)
        progress = self.personal_progresses[ID]

        # scenarios = [ re.compile(r'show progress ')
        # ]

        if message[:2] == ['show', 'progress']:
            if len(message) == 4:
                since = datetime.strptime(message[2], '%Y-%m-%d').date()
                to = datetime.strptime(message[3], '%Y-%m-%d').date()
                df = progress.get_progress(since=since, to=to)
            elif len(message) == 2:
                df = progress.get_progress()
            else:
                return "Wrong timestamp"
            return '`' + df.to_markdown() + '`'
        
        elif message[:2] == ['update', 'progress']:
            new_progress = message[2]
            if re.match(r'^[+-][0-9]+-[0-9]+', new_progress):
                try:
                    progress.update_progress(new_progress=new_progress)
                    return 'Succesfully added progress'
                except Exception:
                    return 'Internal Error: Failed to add progress'
            else:
                return 'Progress is not in desired pattern'
    
     async def send_message(self):
        try:
            message = await self.handle_messages()
            channel = self.attributes['channel']
            await channel.send(message)
        except Exception as e:
                print(e)
        
     def run_bot(self):
        """
        Starts bot, after calling our becomes active and answers on questions
        """
        @self.client.event
        async def on_ready():
            print(f'{self.client.user} is running')

        @self.client.event
        async def on_message(message):
            nonlocal self
            
            # Storing all esential attributes
            self.attributes['username'] = str(message.author).split('#')[0]
            self.attributes['user_message'] = message.content.lower()
            self.attributes['userid'] = str(message.author)
            self.attributes['channel'] = message.channel
            print(f"{self.attributes['username']}: {self.attributes['user_message']}")

            if message.author == self.client.user:
                return

            await self.send_message()

        self.client.run(self.TOKEN)