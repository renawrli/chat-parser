import sqlalchemy
import pandas as pd

def get_members_in_group_chat(chat_name, connection):
    try:
        chat = pd.read_sql_query(f'select * from chat where display_name="{chat_name}"', connection)
        chat_id = chat['ROWID']
        if (len(chat_id) != 1):
            chat_id = chat_id[0]
    except:
        raise ValueError(f'Chat with name {chat_name} does not exist')

    handles = pd.read_sql_query(f'select * from handle', connection)
    handles.rename(columns={'ROWID' : 'handle_id'}, inplace=True)

    chat_handle_ids = pd.read_sql_query(f'select * from chat_handle_join where chat_id={int(chat_id)}', connection)

    chat_handles = chat_handle_ids.join(handles.set_index('handle_id'), on='handle_id')

    return chat_handles

# don't truncate columns/rows when printing to stdout
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

username = 'Rena'
connection = sqlalchemy.create_engine(f'sqlite:////Users/{username}/Library/Messages/chat.db')

# print(pd.read_sql_query(f'select * from chat where display_name !="None" and display_name != ""', connection))

messages = get_members_in_group_chat(str('bzzzzzzzzz💦🔥👌😳'), connection)
print(messages)
print(messCaages.columns.values)
