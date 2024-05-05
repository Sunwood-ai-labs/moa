import boto3
import json
import pprint
from termcolor import colored
from art import *
import os

def main():
    # スクリプト名を取得して出力
    script_name = os.path.basename(__file__)
    tprint(script_name)

    # Bedrockクライアントの作成
    region_name = "us-east-1"  # 指定可能なリージョンはバージニア北部（us-east-1）またはオレゴン（us-west-2）
    bedrock = create_bedrock_client(region_name)

    # ファウンデーションモデルの一覧を取得して出力
    foundation_models = get_foundation_models(bedrock)
    print_foundation_models(foundation_models)

def create_bedrock_client(region_name):
    """
    Bedrockクライアントを作成する関数
    
    :param region_name: リージョン名
    :return: Bedrockクライアント
    """
    return boto3.client("bedrock", region_name=region_name)

def get_foundation_models(bedrock):
    """
    ファウンデーションモデルの一覧を取得する関数
    
    :param bedrock: Bedrockクライアント
    :return: ファウンデーションモデルの一覧
    """
    return bedrock.list_foundation_models()["modelSummaries"]

def print_foundation_models(foundation_models):
    """
    ファウンデーションモデルの一覧を出力する関数
    
    :param foundation_models: ファウンデーションモデルの一覧
    """
    pprint.pprint(foundation_models)

if __name__ == "__main__":
    main()