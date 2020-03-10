import os
import time
from loguru import logger
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl.query import MultiMatch, Match
from elasticsearch_dsl import Search


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class ElasticSearchSingle(Singleton):
    def __init__(self, host, port, user, passwd, index, doc_type='_doc'):
        self.es = Elasticsearch([host], http_auth=(user, passwd), port=port)
        self.index = index
        self.doc_type = doc_type

    def creat_by_id(self, doc_dic):
        """create的方法如果id已经存在，会报409"""
        result = self.es.create(
                index=self.index,
                doc_type=self.doc_type,
                id=doc_dic["id"],
                body=doc_dic)
        return result

    def build_actions(self, data_list):
        actions = []
        for obj in data_list:
            action = {
                "_index": self.index,
                "_type": self.doc_type,
                "_id": obj["id"],  # _id 也可以不赋值,默认生成
                "_source": obj
            }
            actions.append(action)
        return actions

    def bulk_index_actions(self, actions):
        success, _ = bulk(self.es, actions, index=self.index)
        return success, _

    def bulk_index_list(self, data_list):
        actions = self.build_actions(data_list)
        return self.bulk_index_actions(actions)

    def get_by_id(self, idx):
        result = self.es.get(
                    index=self.index,
                    doc_type=self.doc_type,
                    id=idx)
        return result

    def search_by_query(self, query, size):
        result = self.es.search(
                    index=self.index,
                    doc_type=self.doc_type,
                    size=size,
                    body=query)
        return result

    def search_by_string(self, string, size):
        query = self.build_query(string)
        result = self.search_by_query(query, size)
        return result

    @staticmethod
    def build_query(string):
        query = {
            "query": {
                "match": {"audio_info": string}
            }
        }
        return query

