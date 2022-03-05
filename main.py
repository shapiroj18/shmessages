import os
from dotenv import load_dotenv
from db.general import DB
from client.ui import UI

load_dotenv()

messages = DB()
ui = UI()

messages.setup_attached_databases()

total_join = messages.query_db(
    """
    SELECT
        contacts.ZABCDRECORD.ZFIRSTNAME as first_name,
        contacts.ZABCDRECORD.ZLASTNAME as last_name,
        main.handle.id as phone,
        main.message.text as text_body, 
        main.message.date as date
        
    FROM main.message
    LEFT JOIN main.handle ON main.message.handle_id = main.handle.ROWID
    LEFT JOIN contacts.ZABCDPHONENUMBER ON substr_phone(main.handle.id) = substr_phone(contacts.ZABCDPHONENUMBER.ZFULLNUMBER)
    LEFT JOIN contacts.ZABCDRECORD ON contacts.ZABCDPHONENUMBER.ZOWNER = contacts.ZABCDRECORD.Z_PK
    ORDER BY main.message.date desc
    limit 10;
    """
)

# print(total_join)
ui.main(total_join)