import json
import streamlit as st
from search import search_pages, highlight_match

PAGES_FILE = "pages.json"


def load_pages():
    with open(PAGES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pages(pages):
    with open(PAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)


st.title("Tech0 Search v0.1")

tab1, tab2, tab3 = st.tabs(["検索", "登録", "登録データ一覧"])


# -------------------------
# 検索タブ
# -------------------------
with tab1:
    st.header("検索")

    query = st.text_input("検索キーワード")

    if query:
        pages = load_pages()
        results = search_pages(query, pages)

        st.write(f"検索結果: {len(results)} 件")

        for page in results:
            st.subheader(page["name"])

            if "url" in page:
                st.markdown(f"[LPを見る]({page['url']})")

            st.write(f"カテゴリ: {page['category']}")
            st.markdown(highlight_match(page["description"], query))

            st.write("---")


# -------------------------
# 登録タブ
# -------------------------
with tab2:
    st.header("LP登録")

    name = st.text_input("名前")
    url = st.text_input("URL")
    category = st.text_input("カテゴリ")
    description = st.text_area("説明")

    if st.button("登録する"):

        if name and url and category and description:

            new_page = {
                "name": name,
                "url": url,
                "category": category,
                "description": description
            }

            pages = load_pages()
            pages.append(new_page)
            save_pages(pages)

            st.success("登録しました！")

        else:
            st.warning("すべて入力してください")


# -------------------------
# 一覧タブ
# -------------------------
with tab3:
    st.header("LP一覧")

    pages = load_pages()

    st.write(f"登録件数：{len(pages)}件")
    st.write("---")

    for page in pages:
        st.subheader(page["name"])

        if "url" in page:
            st.markdown(f"[LPを見る]({page['url']})")

        st.write(f"カテゴリ: {page['category']}")
        st.write(page["description"])

        st.write("---")