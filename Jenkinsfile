pipeline {
    agent any 
    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }
        stage("Test"){
            echo 'I should Put certains phase of Test here'
        }
    }
}