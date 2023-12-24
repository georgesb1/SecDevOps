# SecDevOps


SCA and DAST are commented in the pipeline 

run sonarqube: docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest

curl test: curl -X POST -H "Content-Type: application/json" -d "{\"user_message\": \"How do you ensure that version control is effectively implemented?\"}" http://192.168.49.2:32516/chatbot/


kubectl exec manager-bot -- curl -X POST -H "Content-Type: application/json" -d '{
    "rating": "selectedRating",
    "feedback": "userFeedback",
    "feedback_id": "chatHistory.children.length - 3"
}' http://192.168.49.2:32516/submit-feedback/


for the other endpoints check the script.js 

check /etc/hosts on minikube 


To make Harbor image puul on k8s avalaible:

Download the CA of the registry (ca.crt)
by ssh , copy on the /etc/ssl/certs/
Then sudo update-ca-certificates

kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=$HOME/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
