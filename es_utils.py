from consts import HOST, INDEX, MAPPINGS
from elasticsearch import Elasticsearch, NotFoundError

def get_es_connection():
    return Elasticsearch(hosts=[HOST])

def set_mappings():
    get_es_connection().indices.put_mapping(index=INDEX, body=MAPPINGS)

def delete_index():
    get_es_connection().indices.delete(INDEX)

def create_index():
    get_es_connection().indices.create(INDEX)

def reset_index():
    """
    Creates a new empty index with the relevant mappings
    """
    try:
        delete_index()
    except NotFoundError as e:
        print("No index to delete...")
    create_index()
    set_mappings()

def index_data(data):
    """
    Indexes a single data item into the DB.
    """
    get_es_connection().index(index=INDEX, body=data)
