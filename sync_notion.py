from sync_types import SourceReader, SourceWriter, BearerAuth
from dataset import COLUMN_TYPE, DataSet
import requests

class NotionWriter(SourceWriter):
    '''Write records to Notion.'''

class NotionReader(SourceReader):
    '''Read records from Notion.'''
    def __init__(self) -> None:
        self.type_map = {
            "title": COLUMN_TYPE.TEXT,
            "rich_text": COLUMN_TYPE.TEXT,
            "multi_select": COLUMN_TYPE.MULTI_SELECT,
            "date": COLUMN_TYPE.DATE,
            "created_time": COLUMN_TYPE.DATE
        }
        self.read_strategies = {
            'title': self._map_notion_text,
            'rich_text': self._map_notion_text,
            'multi_select': self._map_notion_multiselect,
            'date': self._map_notion_date,
            'created_time': self._map_notion_created_time
        }

    def get_databases(self, api_key):
        data = { "filter": {"property": "object", "value": "database"} }
        res = requests.post("https://api.notion.com/v1/search", json=data, auth=BearerAuth(api_key), headers={"Notion-Version": "2021-05-13"})
        json = res.json()
        return [self._parse_database_result(x) for x in json["results"]]

    def get_records(self, api_key: str, id: str, column_info: dict, number=100, iterator=None) -> DataSet:
        url = f"https://api.notion.com/v1/databases/{id}/query"
        data = {"page_size": number}
        if iterator is not None: data["start_cursor"] = iterator
        res = requests.post(url, json=data, auth=BearerAuth(api_key), headers={"Notion-Version": "2021-05-13"})
        json = res.json()
        it = json["next_cursor"]
        records = [ self._map_record(record, column_info) for record in json["results"] ]
        return DataSet(column_info, records, it)

    def get_record_types(self):
        pass

    def get_columns(self, api_key, id):
        url = f"https://api.notion.com/v1/databases/{id}"
        res = requests.get(url, auth=BearerAuth(api_key), headers={"Notion-Version": "2021-05-13"})
        json = res.json()
        return [ self._map_column(k,json["properties"][k]) for k in json["properties"] ]

    def _parse_database_result(self, result):
        return {'name': result["title"][0]["text"]["content"], 'id': result["id"]}

    def _map_column(self, column_name, column):
        if column["type"] in self.type_map:
            col_type = self.type_map[column["type"]]
        else:
            col_type = COLUMN_TYPE.TEXT
        return {"type": col_type, "name": column_name}
    
    def _map_record(self, record:dict, columns:list):
        out_dict = {}
        column_names = [ col['name'] for col in columns ]
        for k in column_names:
            if k in record["properties"]:
                v = record["properties"][k]
                prop_type = v["type"]
                if prop_type in self.read_strategies:
                    # print (f"{prop_type} is in read strategies.")
                    out_dict[k] = self.read_strategies[prop_type](v)
                else: out_dict[k] = None # If we don't know how to handle the type, just return null.
            else:
                out_dict[k] = None
        return out_dict

    def _map_notion_text(self, prop):
        # Database text properties might be of different types (title etc), so 
        # we get the type before looking for the content; database properties only
        # ever contain a single block, so we're safe to look at index [0]
        type = prop["type"] 
        if (len(prop[type]) > 0):
            return prop[type][0]["plain_text"]
        else: return ""

    def _map_notion_date(self, prop):
        return prop["date"]

    def _map_notion_multiselect(self, prop):
        return [ r["name"] for r in prop["multi_select"] ]

    def _map_notion_created_time(self, prop):
        return prop["created_time"]