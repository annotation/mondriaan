"""Build an indexer for a collection of documents and their metadata.

We want full-text search for the contents of the letters, and we want faceted search
for the metadata of the letters.

Letters may have parts that also have metadata.

When we do faceted search, we want to be able to search on facets of the letters and of their parts.
so we need to index the metadata of the letters and of their parts.

We use ElasticSearch for full-text search.

The main problem is how to combine facets of the parts of letters with facets of the letters themselves.

We use a two-step approach:

1. We index the letters and their parts separately.
2. We combine the results of the two indexes.

The first step is done in this module.

The second step is done in the module `search.py`.

# Path: indexer.py

We use ElasticSearch for full-text search and for the faceted search.
The faceted search is done by aggregations as follows:

In ElasticSearch we will use the parent id query to go from a part of the letter to its letter.

We will use the nested query to go from a letter to its parts.

We do not need aggregations, because we can do the faceted search in Python.

The challenge is to set up the index in such a way that we can find parts of letters based on the metadata of the parents of those parts.

Give me an example of a query that we want to do.

We want to find all parts of letters that have a certain sender.

We want to find all parts of letters that have a certain sender and a certain recipient.

We want to find all parts of letters that have a certain sender and a certain recipient and a certain date.

We want to find all letters that have a part with a certain type and a certain full text contained in a letter with a certain date.

How can we do that in the DSL of ElasticSearch?

We can do it with a nested query.

Show me how!

We have a nested field `parts` in the letter index.
"""
