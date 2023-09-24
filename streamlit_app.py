import streamlit as st
import pandas
import requests

# タイトル。最もサイズが大きい。ページタイトル向け
st.title('Title')

# ヘッダ。２番目に大きい。項目名向け
st.header('Header')

# サブレベルヘッダ。３番目に大きい。小項目向け
st.subheader('Sub Header')

# 普通のテキスト。Html や Markdown のパースはしない。
st.text('Text')

# 普通のテキストその２。Markdown のパースをする他、複数の値を渡せる。
# st.write('### Current date: ', date.today())

# マークダウン。markdown 又は write
st.markdown('*Markdown*')
st.write('**Text parsing**')

# HTMl 記述
import streamlit.components.v1 as components
components.html('''
<a href="http://sample.html">Link</a>
''')

# コードブロック
# st.codde('print("Hello World!")')

# エラーメッセージ。赤文字に薄赤背景
st.error('Error message')

# 警告メッセージ。黄色文字に薄黄色背景
st.warning('Warning message')

# 情報メッセージ。青文字に薄青背景
st.info('Information message')

# 成功メッセージ。緑文字に薄緑背景
st.success('Success message')

# 例外メッセージ。Exception部分が太字の赤文字・薄赤背景
st.exception(Exception('Ooops!'))

def create_random_graphs():
    # ランダムなデータの作成
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20) - 0.5,
        'z': np.random.random(20) - 1.0,
        }
    df = pd.DataFrame(data)

    # ラインチャート
    objLchart = st.line_chart(df)

    # エリアチャート
    objAchart = st.area_chart(df)

    # バーチャート
    objBchart = st.bar_chart(df)

    # チャートにデータを動的に追加する場合
    additional_data = np.random.random(size=(5,2))
    objLchart.add_rows(additional_data)
