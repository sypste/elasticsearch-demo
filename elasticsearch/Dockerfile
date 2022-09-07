ARG ELASTIC_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
RUN elasticsearch-plugin install analysis-phonetic
RUN elasticsearch-plugin install "https://github.com/spinscale/elasticsearch-ingest-opennlp/releases/download/8.4.0.1/ingest-opennlp-8.4.0.1.zip"
