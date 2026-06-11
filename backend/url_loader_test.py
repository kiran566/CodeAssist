from rag.url_loader import load_url

chunks = load_url(
    "https://neetcode.io/solutions/two-sum"
)

print("Total Chunks:", len(chunks))

print(chunks[0].page_content[:500])