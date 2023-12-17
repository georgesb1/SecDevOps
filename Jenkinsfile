pipeline {
    agent any 
    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }
        stage("Test"){
            steps{
                echo 'I should Put certains phase of Test here'
            }
        }
        stage("Build"){
            steps{
                git branch: 'main', credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git'
                sh 'pip install -r requirements.txt'
                sh 'uvicorn main:app --host 0.0.0.0 --port 8000'
            }
        }
    }
}