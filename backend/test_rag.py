from pathlib import Path
import chromadb
from langchain_text_splitters import CharacterTextSplitter

# 1. Load the file
text = Path("vault/Lore/Factions/Duskfield.md").read_text()

# 2. Split into chunks (~500 chars, 50 overlap)
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator=" ")
chunks = splitter.split_text(text)

# 3 & 4. Embed and store in ChromaDB using its default local embedding model
client = chromadb.Client()
collection = client.get_or_create_collection("duskfield_test")
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))],
)

# 5 & 6. Query for the single most relevant chunk
query = "what is the silence rule?"
results = collection.query(query_texts=[query], n_results=1)

# 7. Print it
print(results["documents"][0][0])
