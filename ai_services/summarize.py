import cohere

def summarize(text):
    co = cohere.Client("XLCLC70MJ3Af9AFaBb8d1v9km3pG582ksTWuluYb")
    response = co.summarize(
        text=text,
    )
    print(response.summary)

