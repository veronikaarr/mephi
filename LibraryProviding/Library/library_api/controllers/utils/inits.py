from library_api.controllers.utils.random_ import tickets_in_database, reader_to_register, storages

tickets_database = tickets_in_database
readers_register = reader_to_register
reader_register = readers_register[0]

storages_database = storages
ticket = tickets_database

# ticket_bpmn2 = tickets_database[3].unique_key
ticket_bpmn2 = None
# ticket_bpmn2 = tickets_database[2].unique_key
#ticket_bpmn2 = tickets_database[4].unique_key
# ticket_bpmn2 = tickets_database[5].unique_key

literature_bpmn2 = storages[1]

literature_bpmn3 = storages[2]