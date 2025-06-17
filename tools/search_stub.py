def search_web(prompt):
    """
    Simulates a web search. Returns dummy results for now.
    """
    query = prompt.lower().replace("search", "").strip()

    return (
        f"Top search results for: '{query}'\n\n"
        f"1. {query.title()} - Wikipedia Summary\n"
        f"2. Latest article on {query} from TechCrunch\n"
        f"3. Reddit discussion on {query} in r/AskAI\n"
    )
