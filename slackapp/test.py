from pymed import PubMed
import time

pubmed = PubMed(tool="MyTool", email="my@email.address")

# Create a query in the PubMed format
query = "(dyslexia)"

# Execute the query against the API
results = pubmed.query(query, max_results=5)
# print(results)
# Loop over the articles and print out each one
for article in results:
    print("Title: ", article.title)
    print("Abstract: ", article.abstract)
    print("\n")