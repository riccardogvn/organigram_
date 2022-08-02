# https://docs.ampligraph.org/en/1.4.0/ampligraph.discovery.html
# discovery of facts
# hmm

from ampligraph.discovery import discover_facts
#top_n=3 the cutoff for rank to be considered true

discover_facts(X, model, top_n=3, max_candidates=10000, strategy='entity_frequency', target_rel='sold_antiquities_to', seed=42)
