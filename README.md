# reprocess-files

# PyPi Dependencies

    pip install --upgrade pip
    pip install --upgrade pulsar-client fastavro pygogo
    pip freeze > requirements.txt
    sed -i '/pkg_resources/d' requirements.txt

# Running

    kubectl apply -f kubernetes/deployment.yaml
