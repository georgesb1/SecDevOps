pipeline {
    agent any 
    echo('access_token = "1584987" 
password ="54+78"')
    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git']])
            }
        }
        stage("CheckSecret"){
            steps{
                sh 'rm trufflehog || true'
                sh 'docker run gesellix/trufflehog --json https://github.com/georgesb1/SecDevOps.git > trufflehog'
                sh 'cat trufflehog'
            }
        }
        stage("Build"){
            steps{
                git branch: 'main', credentialsId: 'Boss', url: 'https://github.com/georgesb1/SecDevOps.git'
            }
        }
    }
}