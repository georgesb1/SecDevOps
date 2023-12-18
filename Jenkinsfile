pipeline {
    agent any 
    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }
        stage("CheckSecret"){
            steps{
                sh 'rm trufflehog || true'
                sh 'docker run gesellix/trufflehog --json https://github.com/georgesb1/SecDevOps.git'
            }
        }
        stage("Build"){
            steps{
                git branch: 'main', credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git'
            }
        }
    }
}