def format_response(raw_response: str) -> str:
    """
    Validates or transforms the raw response if needed.
    For now, this function simply returns the response.
    In the future, you can add checks to ensure the output has headers,
    bullet points, and is in markdown format.
    """
    # Example: Check if response starts with a header, if not, prepend one.
    if not raw_response.lstrip().startswith("#"):
        raw_response = "# Farming Insights\n" + raw_response
    return raw_response
