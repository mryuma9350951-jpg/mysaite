def search_pages(query, pages):

    results = []
    query = query.lower()

    for page in pages:

        name = page["name"].lower()
        url = page["url"].lower()
        category = page["category"].lower()
        description = page["description"].lower()

        if (
            query in name
            or query in url
            or query in category
            or query in description
        ):
            results.append(page)

    return results


def highlight_match(text, query):

    if not query:
        return text

    return text.replace(query, f"**{query}**")