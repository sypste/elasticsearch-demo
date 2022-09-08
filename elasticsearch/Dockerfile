ARG ELASTIC_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
RUN elasticsearch-plugin install analysis-phonetic
RUN elasticsearch-plugin install "https://github.com/spinscale/elasticsearch-ingest-opennlp/releases/download/8.4.1.1/ingest-opennlp-8.4.1.1.zip"
RUN elasticsearch-plugin install mapper-annotated-text
RUN curl http://opennlp.sourceforge.net/models-1.5/en-ner-person.bin --output /usr/share/elasticsearch/en-ner-persons.bin && chmod a+rwx /usr/share/elasticsearch/en-ner-persons.bin
RUN curl http://opennlp.sourceforge.net/models-1.5/en-ner-location.bin --output /usr/share/elasticsearch/en-ner-locations.bin && chmod a+rwx /usr/share/elasticsearch/en-ner-locations.bin
RUN curl http://opennlp.sourceforge.net/models-1.5/en-ner-date.bin --output /usr/share/elasticsearch/en-ner-dates.bin  && chmod a+rwx /usr/share/elasticsearch/en-ner-dates.bin