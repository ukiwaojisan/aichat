# 外部ライブラリをインポート
import boto3, streamlit

# Bedrockクライアントを初期化
bedrock = boto3.client('bedrock-agent-runtime')

# フロントエンドを表示
streamlit.title("おしえて！Bedrock")
question = streamlit.text_input("質問を入力")
button = streamlit.button("質問する")

# ボタンが押されたらナレッジベースを呼び出し
if button:
  response = bedrock.retrieve_and_generate(
    input={'text': question},
    retrieveAndGenerateConfiguration={
      'type': 'KNOWLEDGE_BASE',
      'knowledgeBaseConfiguration': {
        'knowledgeBaseId': 'XXXXXXXXXX', # ナレッジベースID
        'modelArn': 'anthropic.claude-3-5-sonnet-20240620-v1:0'}})

  # 回答を表示
  streamlit.write(response['output']['text'])
# 外部ライブラリをインポート
import boto3, streamlit

# Bedrockクライアントを初期化
bedrock = boto3.client('bedrock-agent-runtime')

# フロントエンドを表示
streamlit.title("おしえて！Bedrock")
question = streamlit.text_input("質問を入力")
button = streamlit.button("質問する")

# ボタンが押されたらナレッジベースを呼び出し
if button:
  response = bedrock.retrieve_and_generate(
    input={'text': question},
    retrieveAndGenerateConfiguration={
      'type': 'KNOWLEDGE_BASE',
      'knowledgeBaseConfiguration': {
        'knowledgeBaseId': ENV['KNOWLEDGE_BASE_ID'], # ナレッジベースID
        'modelArn': 'anthropic.claude-3-5-sonnet-20240620-v1:0'}})

  # 回答を表示
  streamlit.write(response['output']['text'])
