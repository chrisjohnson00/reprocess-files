# reprocess-files

# PyPi Dependencies

    pip install --upgrade pip
    pip install --upgrade pulsar-client fastavro pygogo
    pip freeze > requirements.txt
    sed -i '/pkg_resources/d' requirements.txt

# Running

    kubectl apply -f kubernetes/job.yaml

# Deleting the job

    kubectl delete job handbrake-job-file-mover-reprocessor -n handbrake-jobs

# Emptying all messages from the topic 

    kubectl exec -it -n pulsar pulsar-toolset-0 -- bin/pulsar-admin topics unload public/default/handbrake-file-move
