# logsearch-boshworkspace
Intel version of logsearch for cloudfoundry

### Generating new manifest
```
LFC_DIR=/home/ubuntu/logsearch-for-cloudfoundry
spiff merge $LFC_DIR/logsearch-deployment.yml $LFC_DIR/logsearch-filters.yml $LFC_DIR/logsearch-jobs.yml templates/logsearch-infrastructure-aws.yml templates/stub.aws.example.yml | perl -pe 's/(X_\S+)/{{ $1 }}/g' > manifest-aws.yml.j2
```
